# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import platform

# THIS PACKAGE SHOULD NOT EXIST
# it exists to make up for the inability to:
# * use an external go compiler
# * have go depend on itself
# * have a sensible way to find gccgo without a dep on gcc

_versions = {
    '1.16beta1': {
        'darwin-arm64': 'fd57f47987bb330fd9b438e7b4c8941b63c3807366602d99c1d99e0122ec62f1',
        'darwin-amd64': 'c3518be5a17c7df746e2596e2ea310cd56348e05454f2bfbb25c5e84708dc2e2'
    }
}

_local2remote = {
    'Darwin-x86_64':'darwin-amd64',
    'Darwin-arm64':'darwin-arm64'
}

class GoBootstrap(Package):
    """Old C-bootstrapped go to bootstrap real go"""

    homepage = "https://golang.org"

    extendable = True

    # For some (recent) platforms, we can't actually build a go bootstrap 
    # with a c-compiler, we need a go one.

    for ver, packages in _versions.items():
        key = "{0}-{1}".format(platform.system(),platform.machine())
        remote = _local2remote.get(key)
        pkg = packages.get(remote)
        if pkg:
            version(ver,sha256=pkg,url='https://golang.org/dl/go{0}.{1}.tar.gz'.format(ver,remote))

    # NOTE: Go@1.4.x is the only supported bootstrapping compiler because all
    # later versions require a Go compiler to build.
    # See: https://golang.org/doc/install/source#go14 and
    # https://github.com/golang/go/issues/17545 and
    # https://github.com/golang/go/issues/16352

    version('1.4-bootstrap-20171003', sha256='f4ff5b5eb3a3cae1c993723f3eab519c5bae18866b5e5f96fe1102f0cb5c3e52',
            url='https://dl.google.com/go/go1.4-bootstrap-20171003.tar.gz')
    version('1.4-bootstrap-20170531', sha256='49f806f66762077861b7de7081f586995940772d29d4c45068c134441a743fa2',
            url='https://storage.googleapis.com/golang/go1.4-bootstrap-20170531.tar.gz')
    version('1.4-bootstrap-20161024', sha256='398c70d9d10541ba9352974cc585c43220b6d8dbcd804ba2c9bd2fbf35fab286',
            url='https://storage.googleapis.com/golang/go1.4-bootstrap-20161024.tar.gz')

    provides('golang@:1.4-bootstrap-20171003',when='@:1.4')
    provides('golang@:1.16',when='@1.16beta1')
 
    conflicts('@1.16beta1', when='platform=linux',msg='1.16beta1 is solely for macOS')
    conflicts('@1.16beta1', when='platform=cray',msg='1.16beta1 is solely for macOS')
    if platform.system() == 'darwin':
        conflicts('@1.16beta4',when='target=arm64')

    depends_on('git', type=('build', 'link', 'run'), when='@:1.4')

    # NOTE: Older versions of Go attempt to download external files that have
    # since been moved while running the test suite.  This patch modifies the
    # test files so that these tests don't cause false failures.
    # See: https://github.com/golang/go/issues/15694
    @when('@:1.4.3')
    def patch(self):
        test_suite_file = FileFilter(join_path('src', 'run.bash'))
        test_suite_file.filter(
            r'^(.*)(\$GOROOT/src/cmd/api/run.go)(.*)$',
            r'# \1\2\3',
        )

    @when('@:1.4')
    def install(self, spec, prefix):
        env['CGO_ENABLED'] = '0'
        bash = which('bash')
        with working_dir('src'):
            bash('{0}.bash'.format('all' if self.run_tests else 'make'))

        install_tree('.', prefix)

    @when('@1.16:')
    def install(self, spec, prefix):
        install_tree('.', prefix)

    def setup_dependent_build_environment(self, env, dependent_spec):
        env.set('GOROOT_BOOTSTRAP', self.spec.prefix)

    def setup_build_environment(self, env):
        env.set('GOROOT_FINAL', self.spec.prefix)
