""" Your task is to sort the string  in the following manner:
-All sorted lowercase letters are ahead of uppercase letters.
-All sorted uppercase letters are ahead of digits.
-All sorted odd digits are ahead of sorted even digits. """

if __name__ == '__main__':
    string = input("ingrese un string con uper, lower y digitos")
    u = sorted([x for x in string if x.isupper()])
    print('Upper', u)
    l = sorted([x for x in string if x.islower()])
    print('lower', l)
    o = sorted([x for x in string if x.isdigit() and int(x)%2==1])
    print('odd', o)
    e = sorted([x for x in string if x.isdigit() and int(x)%2==0])
    print('even', e)

    print("".join(l+u+o+e))

    