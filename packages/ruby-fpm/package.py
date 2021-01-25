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
#     spack install ruby-fpm
#
# You can edit this file again by typing:
#
#     spack edit ruby-fpm
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class RubyFpm(RubyPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/jordansissel/fpm/archive/v1.12.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.12.0', sha256='3aa5b5d9d24e86601918b25e48dd038ee4cf7451c27009b775c36f59cd017123')

    depends_on('ruby-cabin@0.6.0:', type=('build', 'run'))
    depends_on('ruby-json@1.7.7:2.99', type=('build', 'run'))
    depends_on('ruby-backports@2.6.2:', type=('build', 'run'))
    depends_on('ruby-arr-pm', type=('build', 'run'))
    depends_on('ruby-clamp@1.0.0:1.0.99', type=('build', 'run'))
    depends_on('ruby-childprocess@:1.0.0', type=('build', 'run'))
    depends_on('ruby-ffi@1.12.0:1.12.99', type=('build', 'run'))
    depends_on('ruby-xz@0.2.3:0.2.99', type=('build', 'run'))
    depends_on('ruby-pleaserun@0.0.29:0.0.99', type=('build', 'run'))
    depends_on('ruby-git@1.3.0:2.0', type=('build', 'run'))
    depends_on('ruby-stud', type=('build', 'run'))
    depends_on('ruby-pry', type=('build', 'run'))

    def build(self, spec, prefix):
        # FIXME: If not needed delete this function
        pass
