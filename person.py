#!usr/bin/env python
# -*- coding^ utf-8 -*-


class Person:
    def __init__ (self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay
        
    def __str__ (self):
        return '[person: %s, pay = %s]' %(self.name, self.pay)
        
    def lastName (self):
        return self.name.split()[-1]

    def giveRaise (self, percent):
        self.pay = int(self.pay * ( 1 + percent))
        
class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mng', pay)

    def giveRaise (self, percent, bonus = .10):
        Person.giveRaise(self, percent + bonus)
    
    
if __name__ ==  '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue jonse', job = 'dev', pay = 10000)
    print (bob.name, bob.pay)
    print (sue.name, sue.pay)
    print (bob.lastName(), sue.lastName())
    sue.giveRaise(.1)
    print (sue, bob)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
    
    print('--All Tree--')
    for object in (bob, sue, tom):
        object.giveRaise(.1)
        print (object)

        
