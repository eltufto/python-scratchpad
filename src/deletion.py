class ContainerClass(object):
    def __init__(self, delete_me):
        self.delete_me = delete_me
    
class DeleteMe(object):
    def __init__(self):
        self.var = 1
        
    def __del__(self):
        self.var = 0

def scoped_function():
    delete_me = DeleteMe()
    container_class = ContainerClass(delete_me)
    
scoped_function()