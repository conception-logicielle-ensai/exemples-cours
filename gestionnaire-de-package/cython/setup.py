from setuptools import setup
from Cython.Build import cythonize

setup(
    name="example_cython",
    ext_modules=cythonize("example.pyx", language_level="3"),
)