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
#     spack install ruby-clamp
#
# You can edit this file again by typing:
#
#     spack edit ruby-clamp
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class RubyClamp(RubyPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/mdub/clamp/archive/v0.6.5.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.3.2',       sha256='44ea5597355de98b88b194a418f971265d9626dff8124c7ea93c3e1fdbde4203')
    version('1.3.1',       sha256='86fdb0c3555c2b8a800b39b53a2cda973e1360a0d5ffbe09ebb5648ee215caad')
    version('1.3.0',       sha256='582b461ab37339fa5b1e8661ede4ba1660bc2dac90fb651a0e609000c4aee68e')
    version('1.2.1',       sha256='2dbc9972e907ab67815be4c36abf647cdd5b8c81f94ba8fb1f627e983366762c')
    version('1.2.0.beta1', sha256='739077677ea75237feb642b108f17751a28bb58b6ab940a3de14cf4c185a78d4')
    version('1.2.0',       sha256='a08adfca741ee19226faaa0bae89f62b8b5602a6e37418d1fc374d278ae40f70')
    version('1.1.2',       sha256='7a2162718b2eef6767d86bb4df1e96e5b17a9dea05594412485ca6ff477dfba6')
    version('1.1.1',       sha256='7a94be3cd108f3d23a93d8775e9bff094f9b6b13a132000b03cdc4c9d261adc8')
    version('1.1.0',       sha256='5754cbe93161be7f45f829807f5e12b32cc6ba2332993cb1682f22a904d8b903')
    version('1.0.1',       sha256='e2fb2e71476e980c779f4e1b398628b6240b9e24438b5da531146be402119f34')
    version('0.6.5',       sha256='d5d8171faa02a7db6323964e815359cdf47cc5afa7f9825409acc4b6ce2bf30e')

    # FIXME: Add dependencies if required. Only add the ruby dependency
    # if you need specific versions. A generic ruby dependency is
    # added implicity by the RubyPackage class.
    # depends_on('ruby@X.Y.Z:', type=('build', 'run'))
    # depends_on('ruby-foo', type=('build', 'run'))

    def build(self, spec, prefix):
        # FIXME: If not needed delete this function
        pass
