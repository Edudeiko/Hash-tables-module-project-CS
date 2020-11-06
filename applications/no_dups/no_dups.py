
def no_dups(s):
    string = ''
    cache = dict()
    s = s.split()
    for word in s:
        if word not in cache:
            cache[word] = 1
            # string = string + word + ' '
            string += ' ' + word
            # cache[string] = 1

    return string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
