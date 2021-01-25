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
#     spack install ruby-stud
#
# You can edit this file again by typing:
#
#     spack edit ruby-stud
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class RubyStud(RubyPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/jordansissel/ruby-stud/archive/v0.0.23.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.0.23', sha256='7eb2363c72d88064dd4f81461712d2cd28c0b305bab94dccf83a30a2401e821e')
    version('0.0.22', sha256='f9f17e93e9bbb1d0f934413163a2d390477c4fa8b46d9e490cd22c927b1145e1')
    version('0.0.10', sha256='2f7da5f507134d3060ee1c508513f7db793c935d9d856b928dd7be369d15f1ed')
    version('0.0.5',  sha256='686738d4926a9e8f4f1c51922a7435997808997c7f021ddde91ccd2c4d8e8ed6')

    # FIXME: Add dependencies if required. Only add the ruby dependency
    # if you need specific versions. A generic ruby dependency is
    # added implicity by the RubyPackage class.
    # depends_on('ruby@X.Y.Z:', type=('build', 'run'))
    # depends_on('ruby-foo', type=('build', 'run'))

    def build(self, spec, prefix):
        # FIXME: If not needed delete this function
        pass
