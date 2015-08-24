#!usr/bin/env python
# -*- coding^ utf-8 -*-

 # file classtools.py (new)
"Различные утилиты и инструменты для работы с классами"

class AttrDisplay:
    """

    Realizuant inherited method overload output operation showing
    class names and copies of all the attributes in the form name = value pairs,
    available copies (excluding the attributes inherited from the class).
    It can be added to any Slassi and operate with any instances.
    
    """

    def getherAttrs (self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append ('%s=%s' %(key, getattr(self, key)))
        return ', '.join(attrs)

    def __str__ (self):
            return '[%s: %s]' % (self.__class__.__name__, self.getherAttrs()) 
        
if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count + 2
            
    class SubTest(TopTest):
        pass
        
    X,Y = TopTest(), SubTest()
    print (X)                   #Выведет все атрибуты экземпляра
    print (Y)                   #Выведет имя класса. самого близкого в дереве наследования

        
