# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import sys

class ExuberantCtags(AutotoolsPackage):
    """The canonical ctags generator"""
    homepage = "http://ctags.sourceforge.net"
    url      = "http://downloads.sourceforge.net/project/ctags/ctags/5.8/ctags-5.8.tar.gz"

    version('5.8', sha256='0e44b45dcabe969e0bbbb11e30c246f81abe5d32012db37395eb57d66e9e99c7')

    patch('do_not_define_unused_macro.patch',when=(sys.platform=='darwin'),
           sha256='f6606deed7c9acc64381191d37b6fa7ece3a997c9977ef72031f4da6e9b49ac5',level=0)
