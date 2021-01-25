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
#     spack install ruby-pleaserun
#
# You can edit this file again by typing:
#
#     spack edit ruby-pleaserun
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class RubyPleaserun(RubyPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/jordansissel/pleaserun/archive/v0.0.30.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.0.30', sha256='b53db0e4735e23b38d197b0816e0a4fa398a77a671873c0536f5303d37d1b012')
    version('0.0.29', sha256='6be0cf29f3ae9558bfc4221df5aa56082bbe3b60bc68986e5b7fc2000200fc2d')
    version('0.0.27', sha256='2bdc3bdc851d51a1554749152e9e6d9064832bdfd24f353bbdb2f7a683ac058d')
    version('0.0.26', sha256='e9befaf64377644445d237dfdf2fe70b53969e5f4047cd82d33ee82481d61e13')
    version('0.0.24', sha256='81496fc25183216c4c040a3e12880bf226806ae543186e4a3acbbc212572baff')
    version('0.0.23', sha256='429552fde551812d241641bef7df72cade812a75ed5d624590b25f8dd20a55b7')
    version('0.0.22', sha256='5ec9faece024db38ac4e6d72146a3bf9d4401bec3c0f072f113c6a6f40df8c1b')
    version('0.0.21', sha256='2745c6cb17667a81db499ff5f47be40a853b9e9dabc7b5f3681ec0c4a35ca9c4')
    version('0.0.20', sha256='2ea75e99e805ac0a1f5f610c857f2e65ed6db1dc31389cf71688b33ae5eb2518')
    version('0.0.19', sha256='e069eb42a1995a7c1f8f4b49724cf8419f607c9c927e26a96c53892a8006a4f3')

    # FIXME: Add dependencies if required. Only add the ruby dependency
    # if you need specific versions. A generic ruby dependency is
    # added implicity by the RubyPackage class.
    # depends_on('ruby@X.Y.Z:', type=('build', 'run'))
    # depends_on('ruby-foo', type=('build', 'run'))

    def build(self, spec, prefix):
        # FIXME: If not needed delete this function
        pass
