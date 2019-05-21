from distutils.core import setup, Extension

sib_subsidy_module = Extension('sib_subsidy', sources = ['dash_subsidy.cpp'])

setup (name = 'sib_subsidy',
       version = '1.3',
       description = 'Subsidy function for Sibcoin',
       ext_modules = [sib_subsidy_module])
