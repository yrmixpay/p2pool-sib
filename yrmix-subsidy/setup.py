from distutils.core import setup, Extension

sib_subsidy_module = Extension('yrmix_subsidy', sources = ['dash_subsidy.cpp'])

setup (name = 'yrmix_subsidy',
       version = '1.3',
       description = 'Subsidy function for Yrmixcoin',
       ext_modules = [yrmix_subsidy_module])
