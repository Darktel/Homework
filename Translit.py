__author__ = 'Darktel'


def translit(Mystring):
    """
    String (Rus) -> String (Eng)


    """

    RusString = 'а,б,в,г,д,е,ё,ж,з,и,й,к,л,м,н,о,п,р,с,т,у,ф,х,ц,ч,ш,щ,ы,ь,ъ,э,ю,я,*, ,'
    EngString = "a,b,v,g,d,e,yo,zh,z,i,j,k,l,m,n,o,p,r,s,t,u,f,h,c,ch,sh,xh,y,',`,q,ju,ya,*,-,"

    RusChar = RusString.split(',')
    EngChar = EngString.split(',')

    translitString = ''

    for char in Mystring:
        try:
            if char.isupper():
                charlow = char.lower()
                index = RusChar.index(charlow)
                translitString += EngChar[index].upper()
            else:
                index = RusChar.index(char)
                translitString += EngChar[index]
        except:
            translitString += char

    return translitString



testString = translit('''доска обрезная 50х150х6000
доска обрезная краснодар цена
цена куба доски обрезной
куб обрезной доски
купить доску обрезную
''')
print(testString)
