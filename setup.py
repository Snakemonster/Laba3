from distutils.core import setup, Extension

setup(ext_modules=[Extension(name='_example',sources=["example.i","testcpp.cpp"], swig_opts=['-c++'], extra_compile_args=['-std=c++17'])])