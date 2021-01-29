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
#     spack install py-model-optimization
#
# You can edit this file again by typing:
#
#     spack edit py-model-optimization
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import tempfile


class PyTensorflowModelOptimization(Package):
    """A toolkit to optimize ML models for deployment for Keras and TensorFlow,
    including quantization and pruning."""

    homepage = "https://www.tensorflow.org/model_optimization"
    url = "https://github.com/tensorflow/model-optimization/archive/v0.5.0.tar.gz"

    version(
        '0.5.0', sha256='a758f624b695fe4087388478e8b4d02c9ac8bbd0fd94c38aaf22375ebf84e738')

    extends('python')

    depends_on('python@3.5:', type=('build', 'run'))
    depends_on('py-pip', type=('build'))
    depends_on('py-wheel', type=('build'))
    depends_on('py-setuptools', type=('build'))
    depends_on('bazel', type='build')
    depends_on('py-numpy@1.14:1.99', type=('build', 'run'))
    depends_on('py-six@1.10:1.99', type=('build', 'run'))
    depends_on('py-dm-tree@0.1.1:0.1.99', type=('build', 'run'))
    depends_on('py-tensorflow', type=('build', 'run'))

    phases = ['build', 'install']

    def build(self, spec, prefix):
        args = ['build', '--copt=-O3', '--copt=-march=native', ':pip_pkg']
        bazel(*args)

    def install(self, spec, prefix):
        b = Executable('bazel-bin/pip_pkg')
        b('.')
        pip = which('pip')
        pip('install', '{}/spack-src/*.whl'.format(self.stage.path),
            '--prefix={0}'.format(prefix))
