
records = [
    ('Tara', 'web'),
    ('Kyle', 'web'),
    ('Adrian', 'web'),
    ('Jannessa', 'web'),
    ('Mike', 'web'),
    ('Jho', 'DS'),
    ('GOGo', 'DS'),
    ('Craig', 'IOS')
]

'''
# how could we show in O(n) time everyone in a particular track?

# build an index, or indexing on an attribute

# index on the track: make the track the key, have as value list,
# append the names to the list
'''


def build_index(records):
    idx = {}
    for name, track in records:
        if track in idx:
            idx[track].append(name)

        else:
            idx[track] = [name]

    return idx

# index the datat on an attribute: rooms in a house, pools


indexed_records = build_index(records)
print(indexed_records['DS'])
print(indexed_records['web'])
print(indexed_records['IOS'])
