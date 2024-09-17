#assignment 1 decorator to print name

def decoratorFunc(func):
    def abhi(*args,**kwargs):
        print(f"First {func.__name__}..")
        result = func(*args,**kwargs)
        print(result)
        print(f'Last {func.__name__}...')
        return result
    return abhi

@decoratorFunc
def greet(name):
    print(f'Hello {name}...!')
greet('Jay')