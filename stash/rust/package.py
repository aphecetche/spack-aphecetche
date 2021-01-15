# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from six import iteritems


class Rust(Package):
    """The Rust programming language toolchain

    """

    homepage = "https://www.rust-lang.org"
    url = "https://static.rust-lang.org/dist/rustc-1.49.0-src.tar.gz"
    git = "https://github.com/rust-lang/rust.git"

    phases = ['configure', 'build', 'install']

    extendable = True

    variant(
        'rustfmt',
        default=True,
        description='Formatting tool for Rust code'
    )

    variant(
        'analysis',
        default=True,
        description='Outputs code analysis that can be consumed by other tools'
    )

    variant(
        'clippy',
        default=True,
        description='Linting tool for Rust'
    )

    variant(
        'rls',
        default=False,
        description='The Rust Language Server can be used for IDE integration'
    )

    variant(
        'src',
        default=True,
        description='Install Rust source files'
    )

    depends_on('python@3.9.1:' ,type='build')
    depends_on('gmake@3.81:', type='build')
    depends_on('cmake@3.4.3:', type='build')
    depends_on('pkgconfig', type='build')
    depends_on('openssl')
    depends_on('libssh2')
    depends_on('libgit2')

    # Pre-release Versions
    version('master', branch='master', submodules=True)

    # These version strings are officially supported, but aren't explicitly
    # listed because there's no stable checksum for them.
    # version('nightly')
    # version('beta')

    version('1.49.0', sha256='b50aefa8df1fdfc9bccafdbf37aee611c8dfe81bf5648d5f43699c50289dc779')

    # This routine returns the target architecture we intend to build for.
    def get_rust_target(self):
        if 'platform=linux' in self.spec or 'platform=cray' in self.spec:
            if 'target=x86_64:' in self.spec:
                return 'x86_64-unknown-linux-gnu'
            elif 'target=ppc64le:' in self.spec:
                return 'powerpc64le-unknown-linux-gnu'
            elif 'target=aarch64:' in self.spec:
                return 'aarch64-unknown-linux-gnu'
        elif 'platform=darwin':
            if self.spec.satisfies('target=x86_64'):
               return 'x86_64-apple-darwin'
            elif self.spec.satisfies('target=arm64'):
               return 'aarch64-apple-darwin'

        raise InstallError(
            "rust is not supported for '{0}'".format(
                self.spec.architecture
            ))

    def configure(self, spec, prefix):
        target = self.get_rust_target()

        # Bootstrapping compiler selection:
        # Pre-release compilers use the latest beta release for the
        # bootstrapping compiler.
        # Versioned releases bootstrap themselves.
        if '@beta' in spec or '@nightly' in spec or '@master' in spec:
            bootstrap_version = 'beta'
        else:
            bootstrap_version = spec.version
        # See the NOTE above the resource loop - should be host architecture,
        # not target aarchitecture if we're to support cross-compiling.
        bootstrapping_install = Executable(
            './spack_bootstrap_stage/rust-{version}-{target}/install.sh'
            .format(
                version=bootstrap_version,
                target=target
            )
        )
        # install into the staging area
        bootstrapping_install('--prefix={0}'.format(
            join_path(self.stage.source_path, 'spack_bootstrap')
        ))

        boot_bin = join_path(self.stage.source_path, 'spack_bootstrap/bin')

        # Always build rustc and cargo
        tools = ['rustc', 'cargo']
        # Only make additional components available in 'rust-bootstrap'
        if '+rustfmt' in self.spec:
            tools.append('rustfmt')
        if '+analysis' in self.spec:
            tools.append('analysis')
        if '@1.33: +clippy' in self.spec:
            tools.append('clippy')
        if '+rls' in self.spec:
            tools.append('rls')
        if '+src' in self.spec:
            tools.append('src')

        ar = which('ar', required=True)

        # build.tools was introduced in Rust 1.25
        tools_spec = \
            'tools={0}'.format(tools) if self.check_newer('1.25') else ''

        with open('config.toml', 'w') as out_file:
            out_file.write("""\
[build]
cargo = "{cargo}"
rustc = "{rustc}"
docs = false
vendor = true
extended = true
verbose = 2
{tools_spec}
{rustfmt_spec}
build = 
host = 
target= 

[rust]
channel = "stable"
rpath = true
{deny_warnings_spec}

[target.{target}]
ar = "{ar}"

[install]
prefix = "{prefix}"
sysconfdir = "etc"
""".format(
                cargo=join_path(boot_bin, 'cargo'),
                rustc=join_path(boot_bin, 'rustc'),
                prefix=prefix,
                target=target,
                deny_warnings_spec=deny_warnings_spec,
                ar=ar.path,
                tools_spec=tools_spec,
                rustfmt_spec=rustfmt_spec
            )
            )

    def build(self, spec, prefix):
        python('./x.py', 'build', extra_env={
            # vendored libgit2 wasn't correctly building (couldn't find the
            # vendored libssh2), so let's just have spack build it
            'LIBSSH2_SYS_USE_PKG_CONFIG': '1',
            'LIBGIT2_SYS_USE_PKG_CONFIG': '1'
        })

    def install(self, spec, prefix):
        python('./x.py', 'install')
