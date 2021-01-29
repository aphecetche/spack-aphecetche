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
#     spack install py-qkeras
#
# You can edit this file again by typing:
#
#     spack edit py-qkeras
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyQkeras(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/google/qkeras/archive/v0.8.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('0.8.0', sha256='00f00e036789f02670b71e52aa21d3d04c7dcdf9c8519d3982d80922eb0c9a2a')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    depends_on('py-setuptools@41.0.0:', type='build')
    depends_on('py-numpy@1.16.0:',type=('build', 'run'))
    depends_on('py-scipy@1.4.1:',type=('build', 'run'))
    depends_on('py-pyparser',type=('build', 'run'))
    depends_on('py-tensorflow-model-optimization@0.2.1:',type=('build', 'run'))
    depends_on('py-networkx@2.1:',type=('build', 'run'))
    depends_on('py-keras-tuner@1.0.1:',type=('build', 'run'))

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
