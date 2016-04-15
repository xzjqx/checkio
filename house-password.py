def checkio(data):
    if len(data) >= 10:
        f0 = True
    else:
        f0 = False
    f1 = False
    f2 = False
    f3 = False
    for x in data:
        str = x
        if str.isdigit():
            f1 = True
        if str.islower():
            f2 = True
        if str.isupper():
            f3 = True
    flag = f0 & f1 & f2 & f3
    #replace this for solution
    return flag

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"
