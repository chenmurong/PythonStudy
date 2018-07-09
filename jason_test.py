
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            print("jjjjjjjjjjjjj")
        print("jjjjjjjjjjjjj")
        return cls._instances[cls]


class MyClass(object):
    __metaclass__ = Singleton

    # def __init__(self):
    #     print("__init__")


a = MyClass()
b = MyClass()

print(id(a))
print(id(b))
