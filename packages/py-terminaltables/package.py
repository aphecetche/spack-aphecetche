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
#     spack install py-terminaltables
#
# You can edit this file again by typing:
#
#     spack edit py-terminaltables
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyTerminaltables(PythonPackage):
    """Generate simple tables in terminals from a nested list of strings."""

    homepage = "https://github.com/Robpol86/terminaltables"
    pypi     = "terminaltables/terminaltables-3.1.0.tar.gz"

    version('3.1.0', sha256='f3eb0eb92e3833972ac36796293ca0906e998dc3be91fbe1f8615b331b853b81')

    depends_on('py-setuptools', type='build')

