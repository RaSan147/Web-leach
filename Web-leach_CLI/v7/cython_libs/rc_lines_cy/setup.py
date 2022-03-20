from setuptools import setup
from Cython.Build import cythonize

setup(
    name='rc_lines_cy',
    ext_modules=cythonize("rc_lines_cy.pyx", language_level = "3"),
    zip_safe=False
)