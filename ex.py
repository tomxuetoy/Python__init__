import os
 
class Dir:
    def __init__(self, path):
        self.path = path
    def __iter__(self):
        return iter(os.listdir(self.path))
 
d = Dir("c:\\")
x = list(d)
print x
