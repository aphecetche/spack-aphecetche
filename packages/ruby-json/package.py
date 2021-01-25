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
#     spack install ruby-json
#
# You can edit this file again by typing:
#
#     spack edit ruby-json
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class RubyJson(RubyPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/flori/json/archive/v2.5.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version(
        '2.5.1', sha256='2c36c15571725b5b25a2ccbb10277539b39f17f0a72089b62238cd83b93c2025')
    version('2.5.0',
            sha256='8401dbc62a7ff54611d661732e63ad6652d290e288c7838fdebe5d1cde9bfb9e')
    version('2.4.1',
            sha256='055559e609861fd903ebb08f22692ad161e50a92f9f951afc7f86f922efa9be4')
    version('2.4.0',
            sha256='a3c107d964a128912538642e8543dce1c75b94b43371b12784d71cdfbd7d6081')
    version('2.3.1',
            sha256='466380ffc1e29b416ba9498983a9242726a5c0fb07c171514374d5e222f0e275')
    version('2.3.0',
            sha256='b8a7576b9b6dfb997d9b3911e13b2e5b1bde50ff1f5aea46b116c560649ec1a4')
    version('2.2.0',
            sha256='d6b990eb29289a76bfca3cf1eb2c96c213506de1f3cb812bbe9542c01373424f')
    version('2.1.0',
            sha256='c6faf2742e742a65a7bc8a268dc1303824772a4ac1b6b7a43318e29083d2c6b5')
    version('2.0.4',
            sha256='f0e0ce65aa722d8f70d97deb3cb09924e8f4cb7fcb955fd5fa947e8820824821')
    version('1.8.6',
            sha256='c5b7d4ebb5bcbdc724ae1e04f5ecde4df320b39236e64df53fcbd93ce5bc1592')

    # FIXME: Add dependencies if required. Only add the ruby dependency
    # if you need specific versions. A generic ruby dependency is
    # added implicity by the RubyPackage class.
    # depends_on('ruby@X.Y.Z:', type=('build', 'run'))
    # depends_on('ruby-foo', type=('build', 'run'))

    def build(self, spec, prefix):
        # FIXME: If not needed delete this function
        pass
