from functools import reduce

def lambda_print(text):
    return lambda : print(text)

def tap(f):
    def a(x):
        f()

        return x

    return a

def composite(*funcs):
    def compose(f, g):
        return lambda x : f(g(x))
    
    return reduce(compose, funcs, lambda x : x)


def tap_print(t):
    return tap(lambda_print(t))
