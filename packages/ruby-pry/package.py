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
#     spack install ruby-pry
#
# You can edit this file again by typing:
#
#     spack edit ruby-pry
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class RubyPry(RubyPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/pry/pry/archive/v0.13.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.13.1', sha256='e57cf388ffb5779e4effb34b83a2f3fa238ec73e952272b48c235059b9f634f8')
    version('0.13.0', sha256='aa347b8fb9cbe8b14ce5e9bb9229556a5bbce054e959f90abb939424b26d14c3')
    version('0.12.2', sha256='2e9dce86323cabc948a58b4230bc7c7f173036edc952a3cea194e445c308d112')
    version('0.12.1', sha256='03458951c4ef9fa6154303b71657136c452a12fb35f1553cb467c94673c0ebd2')
    version('0.12.0', sha256='d58ef42a556b30a0cddf577f13830b15f78daebf1ca64e66ee6402eed4d61f3f')
    version('0.11.3', sha256='e223f9d59cf1dbec54be9d36523531e4d1350e0376c00f598c0c7a5bd550afe5')
    version('0.11.2', sha256='9db18a35678facc73f6d2c6e2bad33086ba3302fdc900a4ba9fa0ba8561476c2')
    version('0.11.1', sha256='98cf974540db143ad4e30a71eddd211874e1b080d95eda984073a316cafb06ce')
    version('0.11.0', sha256='fd1d79ac50dbadfbfbc4721510922bd6cb830b4ead70f3abb29b7979cc31db77')
    version('0.10.4', sha256='8c4afb4e2c3fea9ed8b9f17323b5a670db08f9995f2031fe52b3c0c4b41dcd67')

    # FIXME: Add dependencies if required. Only add the ruby dependency
    # if you need specific versions. A generic ruby dependency is
    # added implicity by the RubyPackage class.
    # depends_on('ruby@X.Y.Z:', type=('build', 'run'))
    # depends_on('ruby-foo', type=('build', 'run'))

    def build(self, spec, prefix):
        # FIXME: If not needed delete this function
        pass
