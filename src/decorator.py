def _func(func):
    def wrapper():
        print("wrapper")
        return func
    print("func")
    return wrapper


def show():
    print("show")
x = _func(show)
x()

l = [i for i in range(10) if i%2==0]

print(l)




