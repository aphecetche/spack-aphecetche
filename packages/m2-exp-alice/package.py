# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class M2ExpAlice(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    git      = "https://github.com/aphecetche/m2-exp-alice.git"
    url      = "https://github.com/aphecetche/m2-exp-alice/archive/refs/tags/v0.0.1.tar.gz"
    
    extends('python')
    generator = "Ninja"
    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('dev',branch='dev')
    version('0.0.1', sha256='0e9fb4f778417a62170888d558426107f30c64d64634e3799e38f37278c5998d')

    # FIXME: Add dependencies if required.
    depends_on('root')
    depends_on('fmt')
    depends_on('py-pybind11',type='build')
    depends_on('py-vector')
    depends_on('boost')
    depends_on('rapidjson')
    depends_on('ninja',type='build')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
