# Hash Tables

Hash tables are arguably the single most important data structure known to developers. Used to implement everything from objects in JavaScript and dictionaries in Python to Memcached over a distributed computer network, hash tables are beloved by programmers for providing key/value storage with constant big-O time complexity for insertion, deletion and search.

We will be looking underneath the hood at how this delightful data structure works and answering questions like, how do hash tables work? What is a hash function? What is a hash collision and how are they handled? What is the “birthday problem”? What do we do when our hash table is full?

You can think of hash tables as extensions of arrays. In class, we will implement arrays and compare them to linked lists. For your project, you will use this knowledge to implement hash tables in Python.

At first glance, this may seem like a silly task. After all, both of these data structures are already built into Python and their implementations are fast, full of features, and of course, already working.

The reason we are doing this isn’t so that when we’re done we will have an implementation of these data structures. We do it so that we can obtain a deeper understanding of how our predecessors have invented elegant solutions to difficult problems so that we are better equipped to to solve the problems we will encounter on the job.

## Day 1

Task: Implement a basic hash table without collision resolution.

1. Implement a `HashTable` class and `HashTableEntry` class.

2. Implement a good hashing function.

   Recommend either of:

   * DJB2
   * FNV-1 (64-bit)

   Google for these hashing functions and implement from psuedocode.

3. Implement the `hash_index()` that returns an index value for a key.

4. Implement the `put()`, `get()`, and `delete()` methods.

Test this with:

```python
python test_hashtable_no_collisions.py
```

The above test program is _unlikely_ to have collisions, but it's
certainly possible for various hashing functions. With DJB2 (32 bit) and
FNV-1 (64 bit) hashing functions, there are no collisions.

## Day 2

Task: Implement linked-list chaining for collision resolution.

1. Modify `put()`, `get()`, and `delete()` methods to handle collisions.

2. There is no step 2.

Test this with:

```python
python test_hashtable.py
```

Task: Implement load factor measurements and automatic hashtable size
doubling.

1. Compute and maintain load factor.

2. When load factor increases above `0.7`, automatically rehash the
   table to double its previous size.

   Add the `resize()` method.

You can test this with both of:

```python
python test_hashtable.py
python test_hashtable_resize.py
```

Stretch: When load factor decreases below `0.2`, automatically rehash
the table to half its previous size, down to a minimum of 8 slots.

## Day 3 and Day 4

Work on the hashtable applications directory (in any order you
wish--generally arranged from easier to harder, below).

For these, use either the built-in `dict` type, or the hashtable
you built. (Some of these are easier with `dict` since it's more
full-featured.)

* [Lookup Table](applications/lookup_table/)
* [Expensive Sequence](applications/expensive_seq/)
* [Word Count](applications/word_count/)
* [No Duplicates](applications/no_dups/)
* [Markov Chains](applications/markov/)
* [Histogram](applications/histo/)
* [Cracking Caesar Ciphers](applications/crack_caesar/)
* [Sum and Difference](applications/sumdiff/)
