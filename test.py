__author__ = 'root'

class A():
    __slots__ = ['a', 'b']

x = A()
x.a =1
print(x.a)
setattr(x, 's', 5)


print (A.__dict__)
print (x.s)
print(A.__slots__)