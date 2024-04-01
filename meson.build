project('flomb', 'c',
  version : '0.1',
  license: 'BSD-3',
  meson_version: '>=1.4.0',
  default_options : ['warning_level=2'],
)
MODULE_NAME = 'flomb'

add_languages('fortran')
 
py_mod = import('python')
py = py_mod.find_installation(pure: true)
py_dep = py.dependency()

incdir_numpy = run_command(py,
  ['-c', 'import os; os.chdir(".."); import numpy; print(numpy.get_include())'],
  check : true
).stdout().strip()

incdir_f2py = run_command(py,
    ['-c', 'import os; os.chdir(".."); import numpy.f2py; print(numpy.f2py.get_include())'],
    check : true
).stdout().strip()

# CXX = meson.get_compiler('c')
# libs_you_need_to_link = ['openmp', 'gomp']
# deps = []
# foreach lib_name : libs_you_need_to_link 
#     deps += CXX.find_library(lib_name, dirs : [meson.current_source_dir() + '/lib'])
# endforeach

openmp = dependency('openmp')
lgomp =  meson.get_compiler('c').find_library('gomp')

lomb_fortran_custom_target = custom_target('flomb.c',
  input : ['src/lomb_fortran.f90'], 
  output : [MODULE_NAME+'module.c', 
#   MODULE_NAME+'-f2pywrappers2.f90', 
  MODULE_NAME+'-f2pywrappers.f'],
  command : [py, '-m', 'numpy.f2py', '@INPUT@', '-m', MODULE_NAME, '--lower']
)

inc_np = include_directories(incdir_numpy, incdir_f2py)

py.extension_module(MODULE_NAME,
  ['src/lomb_fortran.f90', lomb_fortran_custom_target],
  incdir_f2py / 'fortranobject.c', # f2py file
  include_directories: inc_np,
  dependencies : [py_dep, openmp, lgomp],
  install : false
)
