# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
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
#     spack install php-cs-fixer
#
# You can edit this file again by typing:
#
#     spack edit php-cs-fixer
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PhpCsFixer(Package):
    """A tool to automatically fix PHP Coding Standards issues."""

    homepage = "https://cs.symfony.com"
    url      = "https://github.com/FriendsOfPHP/PHP-CS-Fixer/releases/download/v2.16.3/php-cs-fixer.phar"

    version('2.16.3', sha256='0b16375c2356d4a00c21c34d61953b154549670503180a622fb6adb77030b2a4',expand=False)
    version('2.16.2', sha256='24b0d6ad53c726725b9a75f85783ebfe9daa4cc285e84fd75101f701aacb3ed3',expand=False)
    version('2.16.1', sha256='c84c676a4d0aa5dde99534317115b301f21d24e452bbe94833ef1b633cb401b7',expand=False)
    version('2.16.0', sha256='59a5f7fe8c6e946fdd7426c39e11d502c48549b1c79e87ddebdbf9d4c022c194',expand=False)
    version('2.15.7', sha256='69d34697f774cf9c9b9f921bd2ed2afe70d3f9227f7208f2c168e8e214483115',expand=False)
    version('2.15.6', sha256='45dce6fa948329638eece3dad98bcdff7fe3cc97146fc66d873e7a6639f65c98',expand=False)
    version('2.15.5', sha256='3ccdc7e52917c781e0f4176962cfc230593c87ae007587bd2787f38c544e690a',expand=False)
    version('2.15.4', sha256='9d3cbccfc35e972fb2fec633fadc790773b06839a7a1353786d092078e9abde2',expand=False)
    version('2.15.3', sha256='8c94ede44b66560c3867ed10ce42ec8e4eb8ce0bf7511a0802ad9963864f6c41',expand=False)
    version('2.14.6', sha256='6e6b06a4ead9a1b9c7bbde97cb197bac7a2b899401b5dc55c01a3b009a89e260',expand=False)

    depends_on('php')

    def install(self, spec, prefix):
        set_executable(self.stage.archive_file)
        copy(sef.stage.archive_file,prefix)
