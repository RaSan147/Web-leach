from setuptools import setup
from Cython.Build import cythonize

setup(
    name='rc_lines_cy',
    ext_modules=cythonize("rc_lines_cy.pyx"),
    zip_safe=False
)