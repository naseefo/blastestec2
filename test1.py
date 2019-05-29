import numpy.f2py
fsource = '''
      subroutine foo
      print*, "Hello world!"
      end 
'''
numpy.f2py.compile(fsource, modulename='hello', verbose=0)

import hello
hello.foo()