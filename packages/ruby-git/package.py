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
#     spack install ruby-git
#
# You can edit this file again by typing:
#
#     spack edit ruby-git
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class RubyGit(RubyPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/ruby-git/ruby-git/archive/v1.8.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.8.1',      sha256='a992b2cbf6175a0dabb7735a63e94db3f72ec0408c909e44414615fec78d8a91')
    version('1.8.0',      sha256='d2462f701cca6a4ab323fad384ba3e70ab3cf474d19ddd4acfeb7d9d424bf07d')
    version('1.7.0',      sha256='c44019e1b314f39b392d2e61ddabbc9e7d311ec5f3276bd02f69e4d0e4133f27')
    version('1.6.0.pre1', sha256='7439d263f6b93d36ed5522d1f26a5a12702b62148a31cc06f25eaab053711742')
    version('1.6.0',      sha256='44d516691d0347a21f1da444628ee8853aff393747218c519dfc73fa961d95f9')
    version('1.5.0',      sha256='dbb89c376cd84324de0a3a74d0798bd1c5c7795e34c3be313bc8b644ea2ff530')
    version('1.4.0',      sha256='465162cee516069415977ad2da77998ae6b7a8c295db7f35a2a063a6c8bec73a')
    version('1.3.0',      sha256='8830ac37bd6305c3766876e693f355f366d80fd4980093114d54e39f68f49270')
    version('1.2.10',     sha256='a383b7daec071b459f72ae235f5dbeebfcf2449f70b7b181e5b7b6d343e7fed8')
    version('1.2.9.1',    sha256='4c260dcb8103eb6410386352859884fdfcb8246a0d8b1ec9f0feb8c33e10ef23')

    # FIXME: Add dependencies if required. Only add the ruby dependency
    # if you need specific versions. A generic ruby dependency is
    # added implicity by the RubyPackage class.
    # depends_on('ruby@X.Y.Z:', type=('build', 'run'))
    # depends_on('ruby-foo', type=('build', 'run'))

    def build(self, spec, prefix):
        # FIXME: If not needed delete this function
        pass
