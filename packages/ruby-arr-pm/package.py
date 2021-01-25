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
#     spack install ruby-arr-pm
#
# You can edit this file again by typing:
#
#     spack edit ruby-arr-pm
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class RubyArrPm(RubyPackage):
    """Ruby RPM library (pure ruby, no librpm)"""

    homepage = "https://github.com/jordansissel/ruby-arr-pm"
    url      = "https://github.com/jordansissel/ruby-arr-pm/tarball/5e35996f765c3254c64bafeb0aeafdf58a0c9e6b"
 
    version('master',url='https://github.com/jordansissel/ruby-arr-pm/tarball/5e35996f765c3254c64bafeb0aeafdf58a0c9e6b',sha256='8d26b54a216b973821744262cdfe61456c6410cf66ffedf516a6fd64eb351c31')
    depends_on('ruby-cabin', type=('build', 'run'))
 
