from collections import namedtuple
class SomeClass(object):
    def __init__(self, data1=None, data2=None):
        self.data1 = data1
        self.data2 = data2
    def __str__(self):
        return self.data1 + " " + self.data2
        
MyNamedTuple = namedtuple('MyNamedTuple','some_class, some_var1, some_var2')
some_class = SomeClass('aa','bb')
mnt = MyNamedTuple(some_class, 1, "hello")

print str(mnt.some_class)
print mnt.some_var1
print mnt.some_var2
