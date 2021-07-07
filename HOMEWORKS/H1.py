from functools import wraps

def decorator_with_args(arg1,arg2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            a=[]
            for i in args:
                i=arg1(i)
                a.append(i)
            a=tuple(a)
            args=a
            result=arg2(func(*args,**kwargs))
            return result
        return wrapper
    return decorator

def decorator2(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        with open(func.__name__,'w') as f:
            for i in args:
                f.write(str(i)+ "   ")
    return wrapper


@decorator_with_args(float,str)
@decorator2
def function(*args,**kwargs):
    pass



#just to verify the output type:
print(type(function(1,2,3,4)))

