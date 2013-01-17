from collections import namedtuple
class SomeClass(object):
    def __init__(self, data1=None, data2=None):
        self.data1 = data1
        self.data2 = data2
    def __str__(self):
        return self.data1 + " " + self.data2

some_class = SomeClass('aa','bb')

#define the fields        
MyNamedTuple = namedtuple('MyNamedTuple','some_class, some_var1, some_var2')
#create an instance
mnt = MyNamedTuple(some_class, 1, "hello")

#access fields
print str(mnt.some_class)
print mnt.some_var1
print mnt.some_var2
