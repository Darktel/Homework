def adder (*args):
    res = args[0]
    if len(args) == 0:
        print ('no arguments')
    else:
        for next in args[1:]:
            res += next
    return res
    

if __name__ == '__main__':
    print (adder ('rtyhjtr54', '56h66'))
    print (adder ([5,'6tgge'], [83.90]))
    print (adder (56.00, 3.70))
