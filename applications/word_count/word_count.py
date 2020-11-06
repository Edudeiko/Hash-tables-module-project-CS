import re

test_string = 'Hello, my cat. And my cat doesn"t say "hello" back.'


def word_count(s):

    s = s.lower()
    s = s.split()

    cache = dict()

    for word in s:
        clean_word = re.sub(r'[^a-zA-Z0-9]+', "", word)
        if clean_word in cache:
            cache[clean_word] += 1

        else:
            cache[clean_word] = 1

    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
