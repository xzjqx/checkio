import re

def checkio(text):
    text = text.lower()
    num = {}
    #print text
    for x in text:
        num[x] = 0
    for x in text:
        if re.match(r'[a-z]', x):
            num[x] = num[x] + 1
    ma = 0
    pos = []
    for k, v in num.items():
        if ma < v:
            ma = v
            pos = []
            pos.append(k)
        elif ma == v:
            pos.append(k)
    pos.sort()
    return pos[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")
