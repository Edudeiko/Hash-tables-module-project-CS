'''
# given a string, count how many times each letter occurs in it
# print by descending order, from the most common letter to the least common
'''

our_string = 'supercalifragilisticexpialidocious'

# loop and place in dict

'''
UPER
# Understand
What about spaces and special chars?
Ignore for now, just count alphabet letters

# Plan
loop and place in a dict
use our Python list sorting methods to sort by descending order
of the values not keys

# E
'''


def letter_count(s):
    our_dict = {}

    for letter in s:
        if letter in our_dict:
            our_dict[letter] += 1

        else:
            # ignore non-alphabetic characters
            if letter.isalpha():
                our_dict[letter] = 1

    return our_dict


print(letter_count(our_string))

count_dict = letter_count(our_string)

list_dict = list(count_dict.items())

list_dict.sort(reverse=True, key=lambda pair: pair[1])
# sorted()

for k, v in list_dict:
    print(v, k)


v_set = set()
for k, v in list_dict:
    if v not in v_set:
        print(v, k)
        v_set.add(v)
    else:
        print(' ', k)
