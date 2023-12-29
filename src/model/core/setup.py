"""Module for the formation of core model"""
from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        'calculator_lib',
        ['core_calc.cc', 'core_main.cc'],
        include_dirs=[pybind11.get_include()],
        language='c++',
        extra_compile_args=['-std=c++17'],
    ),
]

setup(
    name='calculator_lib',
    version='0.0.1',
    author='kwukong',
    author_email='kwukong@student.21-school.ru',
    description='SmartCalc_v3.0',
    ext_modules=ext_modules,
    requires=['pybind11']
)
