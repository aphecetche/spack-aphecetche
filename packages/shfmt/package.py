# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re
from spack import *
from spack.util.executable import which


class Shfmt(Package):
    """A shell parser, formatter, and interpreter"""

    homepage = "https://gohugo.io"
    url = "https://github.com/mvdan/sh/archive/v3.2.1.tar.gz"

    executables = ['^shfmt$']

    version('3.2.1', sha256='a1470285e04b69ee7a2bb3948b64e1da9cabe59658997b50aac7c64465f330bd')

    depends_on('go@1.15:', type='build')

    def setup_build_environment(self, env):
        env.prepend_path('GOBIN', self.prefix.bin)

    def install(self, spec, prefix):
        go_args = ['install','./cmd/shfmt']
        go = which('go')
        go(*go_args)
