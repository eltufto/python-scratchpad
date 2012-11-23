#Compare all variables in a class
class Foo(object):
    def __init__(self):
        self.a = None
        self.b = None

#foo1 = Foo()
#foo1.a = 1
#foo1.b = 2
#
#print vars(foo1)


#List objects within a class
class FooMore(object):
    def __init__(self):
        self.my_list = []
        
foomore = FooMore()
foomore.my_list.append("hello")
print vars(foomore)
