from distutils.core import setup, Extension

setup(name="Hello",	version="1.0",	ext_modules=[Extension(name='_example',sources=["example.i","testcpp.cpp"], swig_opts=['-c++'])])