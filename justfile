format:
    black .

test:
    python -m pytest tests/

type_check:
    mypy .
    
cythonize:
    cython3 cpy_fenwick/fenwick.pyx

clean:
    rm -f cpy_fenwick/*.c