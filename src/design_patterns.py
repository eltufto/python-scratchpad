def func1():
    result = func2()
    return result

def func2():
    return 1

print func1()
