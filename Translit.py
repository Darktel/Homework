__author__ = 'Darktel'


def translit(Mystring):
    """
    String (Rus) -> String (Eng)


    """

    RusString = '�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,�,*'
    EngString = "a,b,v,g,d,e,yo,zh,z,i,j,k,l,m,n,o,p,r,s,t,u,f,h,c,ch,sh,xh,y,',`,q,ju,ya,*"

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


if __main__ == '__name__':
    print(translit('�����, �������� ��� ��� �������!'))
