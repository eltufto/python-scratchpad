class MyClass(object):
    def f1(self, arg=1):
        print arg * 1
        
    def f2(self, arg=1):
        print arg * 2
        
    def f3(self, arg=1):
        print arg * 3
        


myclass = MyClass()

fl = [myclass.f1, myclass.f2, myclass.f3]

for f in fl:
    f(2)
