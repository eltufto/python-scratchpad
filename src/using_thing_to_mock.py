from class_to_mock import ClassToMock

def myfunc():
    c1 = ClassToMock()

    result1 = c1.m1()

    result2 = c1.m2()
        
    return result1, result2
