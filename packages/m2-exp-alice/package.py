# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class M2ExpAlice(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    git      = "https://github.com/aphecetche/m2-exp-alice.git"
    url      = "https://github.com/aphecetche/m2-exp-alice/archive/refs/tags/v0.0.1.tar.gz"
    
    extends('python')
    generator = "Ninja"

    version('dev',branch='dev')
    version('0.0.1', sha256='0e9fb4f778417a62170888d558426107f30c64d64634e3799e38f37278c5998d')

    variant('aliroot',default=True,description='use aliroot-lite library')
    variant('aliphysics',default=True,description='use aliphysics-lite library',when='+aliroot')

    depends_on('root')
    depends_on('fmt')
    depends_on('py-pybind11',type='build')
    depends_on('py-vector')
    depends_on('boost')
    depends_on('rapidjson')
    depends_on('ninja',type='build')
    depends_on('jalien-root',when='+aliroot')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("BUILD_ALIROOT","aliroot"))
        args.append(self.define_from_variant("BUILD_ALIPHYSICS","aliphysics"))
        args.append(self.define("CMAKE_EXPORT_COMPILE_COMMANDS",True))
        return args
