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
#     spack install ncdu
#
# You can edit this file again by typing:
#
#     spack edit ncdu
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Ncdu(AutotoolsPackage):
    """Ncdu is a disk usage analyzer with an ncurses interface. It is designed
    to find space hogs on a remote server where you don't have an entire
    gaphical setup available, but it is a useful tool even on regular desktop
    systems. Ncdu aims to be fast, simple and easy to use, and should be able
    to run in any minimal POSIX-like environment with ncurses installed.
    """

    homepage = "http://dev.yorhel.nl/ncdu"
    url      = "http://dev.yorhel.nl/download/ncdu-1.14.2.tar.gz"

    version('1.14.2', sha256='947a7f5c1d0cd4e338e72b4f5bc5e2873651442cec3cb012e04ad2c37152c6b1')
    version('1.14.1', sha256='be31e0e8c13a0189f2a186936f7e298c6390ebdc573bb4a1330bc1fcbf56e13e')
    version('1.14',   sha256='c694783aab21e27e64baad314b7c1ff34541bfa219fe9645ef6780f1c5558c44')
    version('1.13',   sha256='f4d9285c38292c2de05e444d0ba271cbfe1a705eee37c2b23ea7c448ab37255a')
    version('1.12',   sha256='820e4e4747a2a2ec7a2e9f06d2f5a353516362c22496a10a9834f871b877499a')
    version('1.11',   sha256='d0aea772e47463c281007f279a9041252155a2b2349b18adb9055075e141bb7b')
    version('1.10',   sha256='f5994a4848dbbca480d39729b021f057700f14ef72c0d739bbd82d862f2f0c67')
    version('1.9',    sha256='ea7349544a9da77764293d84e52862110ab49ee29b949158bc4bab908d3dd3a5')
    version('1.8',    sha256='42aaf0418c05e725b39b220166a9c604a9c54c0fbf7692c9c119b36d0ed5d099')
    version('1.7',    sha256='70dfe10b4c0843050ee17ab27b7ad4d65714682f117079b85d779f83431fb333')
    version('1.6',    sha256='0922916eab6371adb2f7a567bf4477c0a738910e799dbdf477f30d138eff470c')
    version('1.5',    sha256='f63292b80d0eae4968624eade660bb42c3180890d7ca887a5470f3d75bae8e08')
    version('1.4',    sha256='cb1bdd4835d3e80854f19722e0bf1458097d966a9f10da8f88c873ca94a23616')
    version('1.3',    sha256='f556a4b07c07bb66eabb5f2a20b3c52ea22020a68f2b5302d03e7b93b0ffee54')
    version('1.2',    sha256='10a9f50fcdd662196058f1e5f4e4300a33130b722e1552c0f1b513a07efd386d')
    version('1.1',    sha256='cbd7c6a6372920aa63579e9ba6c07d41b1c22030bd031d3c236349e01e3f5aed')
    version('1.0',    sha256='0bd0323b2415a5479afe624498fd21196d4063395c7b6223d0ac081756050a73')
    version('0.3',    sha256='c13498ef9e81ad5919c1385debe6fd8370b3b8ec3dd15d32d8c6eb5d77f8d1a0')
    version('0.2',    sha256='4a18e0edec5694ffb3ef956dda50564b25ac6de1ca013bba400143121a8906b4')
    version('0.1',    sha256='fc38325312ce105c5290a80707539823d864377e5f8a99a1630baaea767eda46')

    depends_on('ncurses~termlib')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
