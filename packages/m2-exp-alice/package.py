# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *
import os

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
    variant('converters',default=True,description='build various data converters')
    variant('tracking',default=True,description='build tracking library')
    variant('mapping',default=True,description='build mapping library')

    depends_on('root')
    depends_on('fmt')
    depends_on('py-pybind11',type='build')
    depends_on('py-pytest',type='build')
    depends_on('py-vector')
    depends_on('boost')
    depends_on('rapidjson')
    depends_on('ninja',type='build')
    depends_on('jalien-root',when='+aliroot')
    depends_on('vmc',when='+aliphysics')
    depends_on('fairlogger',when='+tracking')
    depends_on('cppgsl',when='+mapping')
    depends_on('py-jupyterlab')
    depends_on('py-pandas')
    depends_on('py-matplotlib')
    depends_on('py-uproot')
    depends_on('py-awkward')

    def cmake_args(self):
        args = []
        args.append(self.define_from_variant("BUILD_ALIPHYSICS","aliphysics"))
        args.append(self.define_from_variant("BUILD_ALIROOT","aliroot"))
        args.append(self.define_from_variant("BUILD_CONVERTERS","converters"))
        args.append(self.define_from_variant("BUILD_MAPPING","mapping"))
        args.append(self.define_from_variant("BUILD_TRACKING","tracking"))
        args.append(self.define("CMAKE_EXPORT_COMPILE_COMMANDS",True))
        return args

    def setup_build_environment(self,env):
        env.set('O2_ROOT',os.path.join(self.build_directory,'stage'))
        env.prepend_path('PYTHONPATH',os.path.join(self.build_directory,'stage/lib'))

    def setup_run_environment(self,env):
        env.set('O2_ROOT',self.prefix)
        env.set('ALICE_ROOT',self.prefix)
        env.set('ALICE_PHYSICS',self.prefix)
        env.append_path('ROOT_INCLUDE_PATH',os.path.join(self.prefix,'include'))
