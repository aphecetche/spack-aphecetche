# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os.path


class Jq(AutotoolsPackage):
    """jq is a lightweight and flexible command-line JSON processor."""

    homepage = "https://stedolan.github.io/jq/"
    url = "https://github.com/stedolan/jq/releases/download/jq-1.6/jq-1.6.tar.gz"
    git = "https://github.com/stedolan/jq.git"

    version('2020-12-17', commit='80052e5275ae8c45b20411eecdd49c945a64a412')
    version(
        '1.6', sha256='5de8c8e29aaa3fb9cc6b47bb27299f271354ebb72514e3accadc7d38b5bbaa72')
    version(
        '1.5', sha256='c4d2bfec6436341113419debf479d833692cc5cdab7eb0326b5a4d4fbe9f493c')

    patch('lgamma.patch',when='@2020-12-17')

    depends_on('oniguruma')
    depends_on('bison@3.0:', type='build')
    depends_on('autoconf', type='build', when='@2020-12-17')
    depends_on('automake', type='build', when='@2020-12-17')
    depends_on('libtool',  type='build', when='@2020-12-17')
    depends_on('m4',       type='build', when='@2020-12-17')


@run_after('install')
@on_package_attributes(run_tests=True)
def install_test(self):
    jq = self.spec['jq'].command
    f = os.path.join(os.path.dirname(__file__), 'input.json')

    assert jq('.bar', input=f, output=str) == '2\n'
