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
    #print num
    #replace this for solution
    return 'a'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    checkio("Hello World!")
    #assert checkio(u"Hello World!") == "l", "Hello test"
    #assert checkio(u"How do you do?") == "o", "O is most wanted"
    #assert checkio(u"One") == "e", "All letter only once."
    #assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    #assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    #assert checkio(u"abe") == "a", "The First."
    #print("Start the long test")
    #assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")