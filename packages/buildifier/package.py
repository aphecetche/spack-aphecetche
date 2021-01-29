# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install buildtools
#
# You can edit this file again by typing:
#
#     spack edit buildtools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Buildifier(Package):
    """A bazel BUILD file formatter and editor"""

    homepage = "//www.example.com"
    url      = "https://github.com/bazelbuild/buildtools/archive/3.5.0.tar.gz"

    version('3.5.0', sha256='a02ba93b96a8151b5d8d3466580f6c1f7e77212c4eb181cba53eb2cae7752a23')

    depends_on('go', type='build')

    executables = ['^buildifier$']

    def setup_build_environment(self,env):
        env.prepend_path('GOPATH',self.stage.path)

    def install(self, spec, prefix):
        go_args=['get']
        go = which('go')
        go(*go_args)
        mkdir(prefix.bin)
        install('buildifier',prefix.bin)
