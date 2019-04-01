from cx_Freeze import setup, Executable
import os

## Soluciona error KEY: TCL_LIBRARY
os.environ['TCL_LIBRARY'] = "C:\\Users\\c804324\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\c804324\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tk8.6"

## Soluciona error: ImporError: cannot import name '_methods'
additional_mods = ['numpy.core._methods', 'numpy.lib.format']

setup(name = "take_a_video" ,
      version = "0.1" ,
      description = "Prueba de ejecutable windows..." ,
      options = {'build_exe': {'includes': additional_mods}},
      executables = [Executable("take_a_video.py")])
