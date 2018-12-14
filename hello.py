def compose(f, g):
    def wrapper(x):
        return f(g(x))
    wrapper.__name__ = compose({f.__name__}), ({g.__name__})
    return wrapper

def ntimes(n):
    def wrap(funtion):
        if n == 1: return func
        return compose(funtion, ntimes(n-1)(func))
    return wrap
