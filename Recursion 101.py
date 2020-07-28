# https://www.codewars.com/kata/5b752a42b11814b09c00005d/train/python
import types

def one(a, b):
    print('one', a, b)

    if a == 0 or b == 0:
        yield [a, b]
    else:
        yield two(a, b)
    
def two(a, b):
    print('two', a, b)

    if a >= 2 * b:
        yield one(a - 2 * b, b)
    else:
        yield three(a, b)

def three(a, b):
    print('three', a, b)

    if b >= 2 * a:
        yield one(a, b - 2 * a)
    else:
        yield [a, b]
    
def solve(a, b):
    print(a, b)
    gen = one(a, b)
    while isinstance(gen, types.GeneratorType):
        gen = gen.__next__()
    return gen    
