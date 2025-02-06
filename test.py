
'''
# 装饰器
from functools import wraps

def my_decorator(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        print("开始...")
        func(*args, **kwargs)
        print("结束...")
        print(func.__name__)
        return "hello!"
    return wrapper

# def say_hello(name):
#     print(f"{name},hello函数运行")
# enhanced_hello = my_decorator(say_hello)
# enhanced_hello("aaa")

@my_decorator
def say_hello(name, age):
    print(f"{age},hello函数运行,{name}")

print(say_hello.__name__)
print(say_hello("aaa",1))
'''

# 带参数的装饰器需要创建3层嵌套函数  外层参数 中间层被装饰函数 内层具体逻辑
from functools import wraps
def decorator_with_args(arg):
    def my_decorator(func):
        # @wraps(func)
        def wrapper(*args, **kwargs):
            print(arg)
            print("开始...")
            func(*args, **kwargs)
            print("结束...")
            print(func.__name__)
            return "hello!"
        return wrapper
    return my_decorator


@decorator_with_args("aaa")
def say_hello(name, age):
    print(f"{age},hello函数运行,{name}")

print(say_hello.__name__)
print(say_hello("name",1))
