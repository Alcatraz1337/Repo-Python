import time, functools

def log(func):
    print(func)
    if callable(func):
        @functools.wraps(func)
        def wrap(args, **kw):
            print('no args %s():' % (func.name))
            print("begin call")
            #r = func(args, kw)
            #print("end call")
            return func(*args,kw)
        print("end call")
        return wrap

    def decorator(func):
        @functools.wraps(func)
        def wrap(args, **kw):
            print('args  %s %s():' % (func, func.name))
            print("begin call")
            r = func(args, **kw)
            print("end call")
            return r
        return wrap
    return decorator

if '__name__' == '__main__':
    log(main)