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
#     spack install py-keras-tuner
#
# You can edit this file again by typing:
#
#     spack edit py-keras-tuner
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyKerasTuner(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/keras-team/keras-tuner/archive/1.0.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.0.2',    sha256='c5e5ef66f149f00a703da6441ff3d62f63bad99992b6d25255bde3e3dc1ac69d')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-future',        type=('build', 'run'))
    depends_on('py-numpy',        type=('build', 'run'))
    depends_on('py-tabulate',        type=('build', 'run'))
    depends_on('py-terminaltables',        type=('build', 'run'))
    depends_on('py-colorama',        type=('build', 'run'))
    depends_on('py-tqdm',        type=('build', 'run'))
    depends_on('py-requests',        type=('build', 'run'))
    depends_on('py-scipy',        type=('build', 'run'))
    depends_on('py-scikit-learn',        type=('build', 'run'))

    def build_args(self, spec, prefix):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
