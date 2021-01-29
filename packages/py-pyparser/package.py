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
#     spack install py-pyparser
#
# You can edit this file again by typing:
#
#     spack edit py-pyparser
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyPyparser(PythonPackage):
    """PyParser is a simple library that makes it easier to parse files."""

    homepage = "https://keep.imfreedom.org/grim/pyparser/"
    pypi     = "pyparser/pyparser-1.0.tar.gz"

    version('1.0', sha256='d1b76e2dabdd2952cadfd545229cc144afee6130bf171a031d5bf53f11b912f5')

    depends_on('py-setuptools', type='build')
