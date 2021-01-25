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
#     spack install ruby-xz
#
# You can edit this file again by typing:
#
#     spack edit ruby-xz
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class RubyXz(RubyPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/Quintus/ruby-xz/archive/v1.0.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.0.0', sha256='e52dddb05da572bed0799393dae5e9697b7cfb145b3c929571c8b93263aa14af')
    version('0.2.3', sha256='7b4acb9387fe94f0eed3126bf9f84b76fae0b6be04aa3e09e312f2733e349236')
    version('0.2.2', sha256='879063b4ede92b04a91fae8a818fdbb6663853200f8137b9873acee5939ba3e6')
    version('0.2.1', sha256='5914e2d7981c9a1b9538cbb5bb79f1ad57926ab7e8fddbee6008671ca2d97262')
    version('0.2.0', sha256='6947fbd2d69b7236f692b5a61fb7eac7478cdaf477afd47a93d47d7f27dc4369')
    version('0.1.1', sha256='8697db4036ad959f607d08ff6d4d370c262d1867134aad26ff5e8e26b770b17b')

    # FIXME: Add dependencies if required. Only add the ruby dependency
    # if you need specific versions. A generic ruby dependency is
    # added implicity by the RubyPackage class.
    # depends_on('ruby@X.Y.Z:', type=('build', 'run'))
    # depends_on('ruby-foo', type=('build', 'run'))

    def build(self, spec, prefix):
        # FIXME: If not needed delete this function
        pass
