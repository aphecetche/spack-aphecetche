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
#     spack install ruby-childprocess
#
# You can edit this file again by typing:
#
#     spack edit ruby-childprocess
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class RubyChildprocess(RubyPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/enkessler/childprocess/archive/v0.9.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('4.0.0', sha256='07b65ef9b6ed6549110c29febf3b48164e59ca11a1d58ca30d118fa1ce91ca7b')
    version('3.0.0', sha256='71fac4bbc86cb7344df2184280476174e86e1d6181fcbd1b35eb955aa5e1c195')
    version('2.0.0', sha256='45b2874d183c526771d179668364fde905b841005dcd86b805a56bc38f798009')
    version('1.0.1', sha256='86ef43c46216d151d52114ba0ca90e08c8a127a783c6c95c60c6bb4fced62376')
    version('1.0.0', sha256='91fbc42e7619536dd0750d424498d260ca5a76d679ff6bdba3c11ab1bb45a50e')
    version('0.9.0', sha256='dcc1d66af54dcfccc0d6eb123f3fc37dae1880c152d40d121a3c170adb8d3cbc')
    version('0.8.0', sha256='cc693bb00ba8b5efca26919eb7ec2a80d7fc7fd9c7433fd0db25423068cabcd8')

    # FIXME: Add dependencies if required. Only add the ruby dependency
    # if you need specific versions. A generic ruby dependency is
    # added implicity by the RubyPackage class.
    # depends_on('ruby@X.Y.Z:', type=('build', 'run'))
    # depends_on('ruby-foo', type=('build', 'run'))

    def build(self, spec, prefix):
        # FIXME: If not needed delete this function
        pass
