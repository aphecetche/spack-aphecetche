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
#     spack install ruby-ffi
#
# You can edit this file again by typing:
#
#     spack edit ruby-ffi
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class RubyFfi(RubyPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/ffi/ffi/archive/1.14.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.14.2', sha256='e3bacaf7cb71315faf96936993f343175d49cd71777c25b9d4843442d023638f')
    version('1.14.1', sha256='481519f39822c2930e0874d5f1953fe6319d9429d5f04538f50bf69d3986ab15')
    version('1.14.0', sha256='8f480d9f83e557aa7842ab5718974016baaf03c9c5224767f66ee93b30d7711f')
    version('1.13.1', sha256='75cdca0fe11be2444a9d6cd93ea8f39142c56359ecdb9dcc56a895638065483c')
    version('1.13.0', sha256='103571e1fe578df878862692ab7aae05aa70de95e15ccc4bac4e96aa00f88573')
    version('1.12.2', sha256='b055a7bb84714d512c74446076e25e2e40096bb98bd53761159b6db93bdc4a80')
    version('1.12.1', sha256='3f22caa4ae7afe45ad8954807f5e2043dee5d3b12746c84d7729854940a1e13b')
    version('1.12.0', sha256='1e6f695ef700c7558ebd32fb3d415c6486f84ba5886b59c1789ff2a69e27586d')
    version('1.11.3', sha256='f9d539f3e8dbc2e764b36703d33cadd3f1b822253da58563126603a81585723d')
    version('1.11.2', sha256='90049b41290dbd05774b9f737185ccaa41f982c1a238b418703a3ef4a38d7242')

    # FIXME: Add dependencies if required. Only add the ruby dependency
    # if you need specific versions. A generic ruby dependency is
    # added implicity by the RubyPackage class.
    # depends_on('ruby@X.Y.Z:', type=('build', 'run'))
    # depends_on('ruby-foo', type=('build', 'run'))

    def build(self, spec, prefix):
        # FIXME: If not needed delete this function
        pass
