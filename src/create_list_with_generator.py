class my_class():
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return str(self.data)

my_list = [
           my_class(1),
           my_class('2'),
           my_class((1,'2')),
]



print my_list
print my_list2
