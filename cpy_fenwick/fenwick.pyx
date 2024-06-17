#!python
#cython: language_level=3

import cython

cdef class FenwickTree:
    cdef readonly cython.int size

