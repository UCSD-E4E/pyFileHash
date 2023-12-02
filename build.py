from pathlib import Path

from pybind11.setup_helpers import Pybind11Extension, build_ext


def build(setup_kwargs):
    src_dir = Path('file_hasher/src/')
    src_files = list(src_dir.glob('*.c*'))
    ext_modules = [
        Pybind11Extension('file_hasher',
                          [str(src) for src in src_files if src.name != 'digest.cpp'],
                          extra_compile_args=['-O3'],
                          language='c++',
                          cxx_std=11)
    ]
    setup_kwargs.update({
        'ext_modules': ext_modules,
        'cmd_class': {'build_ext': build_ext},
        'zip_safe': False
    })
