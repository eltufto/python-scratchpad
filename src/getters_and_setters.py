class MyClass(object):
    def __init__(self, var1=None, var2=None):
        self.var1 = var1
        self.var2 = var2
    
    def __str__(self):
        return str(self.var1) + " " + str(self.var2) + " " + str(self.var3) + " " + self.var4


    def get_var3(self):
        return self.var1
    var3 = property(get_var3) 
    
    @property
    def var4(self):
        return str(self.var1)
    
    def get_some_derived_variable(self):
        return self.var4

myclass1 = MyClass({'mykey':'myvalue'}, "word up")
myclass1.var1 = "hello"
myclass2 = MyClass({'mykey':'myvalue'}, 2)

print myclass1
print myclass1.var4
print myclass2
print myclass2.get_some_derived_variable()
