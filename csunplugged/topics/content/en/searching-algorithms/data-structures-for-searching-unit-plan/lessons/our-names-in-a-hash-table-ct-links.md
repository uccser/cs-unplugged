The CT connections for this lesson are similar to lessons 1 and 2. Some extra connections are noted here.

{panel type="ct-algorithm"}

# Algorithmic thinking

Converting words to numbers can be done many ways; we used two algorithms to do this (add up the values; and add the values multiplied by their position). There are many other algorithms that could have been used.

Students can also create their own hash function algorithms.

#### What to look for:

Did students recognise that they could design their own hash function algorithm?

{panel end}

{panel type="ct-abstraction"}

# Abstraction

Treating all data as numbers is an abstract concept, as it hides the details of what the data is and represents by replacing it with just numbers. This is crucial to hashing.

#### What to look for:

Did students recognise that any type of data could be represented as a number?
Can they see that his means we could store any type of data in a hash table?

{panel end}

{panel type="ct-decomposition"}

# Decomposition

If students used a system that generated one digit at a time (e.g. drawing digits from a hat), then the problem of generating large numbers has been decomposed into generating one random digit.

#### What to look for:

Did students realise that long random numbers can be generated from single random digits?

{panel end}

{panel type="ct-pattern"}

# Generalising and patterns

As described above in Algorithmic thinking, the algorithm for building a hash table is very similar to the one used for searching it.

#### What to look for:

Did students identify common patterns between the algorithms for building a hash table and for searching it? Can they explain the similarities between these and identify the differences? 
Can students explain why the algorithms for building and searching in a hash table are so similar? This is also related to, and listed under, Logic.

{panel end}

{panel type="ct-evaluation"}

# Evaluation

As the number of collisions affects the performance of the hash table, it is important to evaluate a hash table's size; is it suitably large enough for the amount of data it needs to store? The hash functions used should also be evaluated. The more widely the function spreads data between the slots in the table, the better it is.

#### What to look for:

Do students observe that a larger hash table (e.g. the one with 20 slots) will usually be faster to search because each slot is likely to have fewer items in it?
Can students explain why some hash functions are better than others?

{panel end}

{panel type="ct-logic"}

# Logic

The main challenge to fast searching in a hash table is collisions - having two different values in the same slot. Collisions decrease the efficiency of a hash table, because they cause searches to take longer, as more data has to be checked.

#### What to look for:

Can students reason that even with a very large hash table, it's possible for everything to end up in one slot (but extremely unlikely)?
Can they explain why collisions decrease the efficiency of a hash table?
Can students explain why the algorithms for building and searching in a hash table are so similar? This is also related to, and listed under, Generalising and patterns.

{panel end}
