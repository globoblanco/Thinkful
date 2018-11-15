# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 12:14:14 2018

@author: Owner
"""

class Vector(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "({}, {})".format(self.x, self.y)
    
    def add(self, a):
        return Vector((self.x + a.x), (self.y + a.y))

if __name__ == "__main__":
#    import Vector
    
    a = Vector(3, 4)
    print(a)
    b = Vector(1, 2)
    print(b)
    c = a.add(b)
    print(c)
    print(dir(a))
    print(a.x)
    print(a.y)