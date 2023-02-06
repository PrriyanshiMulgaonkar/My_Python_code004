def greet(fx):
    def mfx(*args,**kwargs):
        print("Good morning")
        fx(*args,**kwargs) #tuple or dictinory
        print("Thanks for using function")
    return mfx
@greet
def func():
    print("Hello world")

def add(a,b):
    print(a+b)
func()
greet(add)(1,3)

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b