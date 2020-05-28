# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
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
#     spack install hub
#
# You can edit this file again by typing:
#
#     spack edit hub
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Hub(MakefilePackage):
    """The github git wrapper"""

    homepage = "https://github.com/github/hub"
    git = "https://github.com/github/hub.git"
    url      = "https://github.com/github/hub/archive/v2.11.2.tar.gz"

    version('master',branch='master')
    version('2.14.2', sha256='e19e0fdfd1c69c401e1c24dd2d4ecf3fd9044aa4bd3f8d6fd942ed1b2b2ad21a')
    version('2.14.1', sha256='62c977a3691c3841c8cde4906673a314e76686b04d64cab92f3e01c3d778eb6f')
    version('2.14.0', sha256='cdb33dac329d1cf2741d35a93b478fd24d779b2943e8e7cf21b4127f5c5c5868')
    version('2.13.0', sha256='0b5147a25aa8dff37d6c88b2a30ed38c05d35e03c64d79039925dcb49de80940')
    version('2.12.8', sha256='72d09397967c85b118fc1be25dc0fc54353f4dea09f804687a287949c7de7ebe')
    version('2.12.7', sha256='53d812b09aed87c49cc62d09a8827c2dfe7b776732b71287b800320bd23ea028')
    version('2.12.6', sha256='4b9fdb9926dd8db3aa9b6300265fe5ea7430960eeddf6046a2d4efb13889a4f3')
    version('2.12.5', sha256='2fad48fa9431216ecd6d91674dbc766b7a1eb27cdbf02e40d9654a31678f91f1')
    version('2.12.4', sha256='82f445505866319c6bbad78cf149afca27c5542e98132cdff2f31c26a700d05a')
    version('2.12.3', sha256='197242fea670353688c541d2e4584b449f18c354a01d89bf1667ea33c0071ddc')

    depends_on("go@1.11:",type="build")
    

    def edit(self, spec, prefix):
        env['PREFIX'] = prefix


