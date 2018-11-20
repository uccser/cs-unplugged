Many of the connections are the same as for lesson 1. Here we've made some extra observations that come out of this lesson.

{panel type="ct-algorithm"}

# Algorithmic thinking

The algorithm for creating a hash table is very similar to the one for searching it; you generate the hash value, and simply add it to the appropriate slot.

#### What to look for:

Are students able to accurately construct a hash table that can be searched correctly? Did they recognise the similarities between the algorithm for searching a hash table and the one they have used for building a hash table?

{panel end}

{panel type="ct-abstraction"}

# Abstraction

This process will work with any size number, and could use a different hash function (such as multiplying every second digit by 2 before adding it). A hash table is an abstract model, which can then be applied to different, specific situations, such as different amounts, and types, of data.

#### What to look for:

Can students recognise that any range of numbers could be used for the searching, and that different hash functions could be used as long as the same function is used to store and retrieve the values?

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
