# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class SimpleWebServer(CMakePackage):
    """A very simple, fast, multithreaded, platform independent HTTP and HTTPS
    server and client library implemented using C++11 and Boost.Asio. Created
    to be an easy way to make REST resources available from C++ applications."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://gitlab.com/eidheim/Simple-Web-Server"
    url      = "https://gitlab.com/eidheim/Simple-Web-Server/-/archive/v3.1.1/Simple-Web-Server-v3.1.1.tar.gz"


    version('3.1.1', sha256='f8f656d941647199e0a2db3cb07788b0e8c30d0f019d28e6ee9281bc48db132d')

    # FIXME: Add dependencies if required.
    depends_on('boost')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        args.append(self.define("BUILD_TESTING",False))
        return args
