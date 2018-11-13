{panel type="ct-algorithm"}

# Algorithmic thinking

To identify which group of chests they should look in, students have to follow the algorithm we use to locate data in a hash table. 
The have to first take the number on their partner’s chest, hash it using a hash function (following the steps to hash the number is an algorithm as well!), and now that they know which group of chests to look in they need to look at these one-by-one until the find the right chest.

#### What to look for:

Are students able to accurately follow this algorithm?
Are they able to locate the right chest without performing unnecessary checks (by looking at chests in a different group)?

{panel end}

{panel type="ct-abstraction"}

# Abstraction

The group’s, treasure chests, and numbers on the chests we used in this activity emulate the way a hash table is structured and how it functions. 
A hash table is a type of data structure commonly used by computer scientists and programmers. 
Data structures are abstract concepts, and are explored in the Abstraction section in the unit plan.

If we compare the groups and chests in this activity to a hash table:
    -   The groups the chests were placed in are the slots in a hash table, where data is placed according to its hashed value.
    -   The number on a chest is the “key” of that chest, which is hashed and gives us the slot in the hash table where the chest (our data) should be placed.
    -   The “key” is the information we have (the number on the chest), and the chest itself is the data we want to find in the hash table.

Another example of abstraction that students may demonstrate can happen after they have figured out which group their partner's chest is in. 
Now that they know which group to look at, they can completely ignore all other groups, this is information that is no longer of use to them so it can be discarded.

#### What to look for:

Using the chests activity, are students able to describe the key parts of it that make it a hash table, without needing to think about the context of treasure chests? 
Can they describe it in a way that means it could be used for different contexts, such as using people's names to look for their phone numbers?

Once they had found the group their partner’s chest was in, did they then ignore the other groups, or try and guess chests in those as well?

{panel end}

{panel type="ct-decomposition"}

# Decomposition

As noted under Algorithmic Thinking, the hash table searching algorithm is actually made up of two algorithms (hashing and sequential search) and we can decompose it into these two processes.
If we look at each step in the process of searching a hash table, it becomes clear that we are not performing one large task, but a number of smaller, simpler tasks. 

As we have seen, sequential search becomes less and less efficient as it has to search more data, but if we are searching through a small amount of data, for example just 3 chests, it can still complete this task quickly. 
When the chests are placed into the groups in the hash table they are being divided into smaller sets of chests. 
Since we have decomposed our large set of chests into these smaller groups, when we use sequential search to search one of these groups it can perform much more efficiently than if we had not broken the chests up into smaller groups. 
We have decomposed our problem into a much smaller one!

#### What to look for:

Did students recognise that they are performing a sequential search once they have identified the group/slot that they should be searching?
Did they recognise that by dividing the chests into groups they are decomposing the problem into a smaller subproblem? 
Can they see the connection between this, and why a hash table where everything is in the same group is very inefficient?

{panel end}

{panel type="ct-pattern"}

# Generalising and patterns

Students may observe patterns of values that hash to the same group e.g. 19, 28, 37. This is an interesting maths pattern for them to think about, can they explain why this happens?
As an extension, students may note that instead of taking the last digit to have 10 groups (slots), we can use the modulo function (i.e. remainder after division) instead, and take the sum of the number modulo 10. For 100 slots they can use modulo 100, instead of just taking the last two digits. This can then be generalised to create a rule that can be used for any number of slots: take the sum of the number and then apply the modulo of the number of slots, e.g. if there are 30 slots we can take the sum of the number and then apply modulo 30 to this.

#### What to look for:

Can students come up with a way to work with a hash table that spreads the values over 20 slots instead of 10? (They can't just double the one-digit number, since that won't use all slots; taking the remainder when divided by 20 i.e. modulo 20, is one solution.)
Did students recognise that if they were looking in a group with more than one chest then they had to use a sequential search to look through the chests?

{panel end}

{panel type="ct-evaluation"}

# Evaluation

Much of this lesson is about evaluating the speed of this search method. It involves chance (how the hash values work out), but there are some conclusions that can be drawn about how long it will take. 
For example:
    -   Under what circumstances do you find the right chest on the first try?
    -   What is the largest number of chests you might need to check?

We used a particular hash function in the exercise, but in practice it's important to find a function that spreads the values around the slots as evenly as possible.

    -   If all the serial numbers on the money hashed to the same slot what would happen?
    -   What makes a good hash function? (It would be one that makes it likely that every serial number would hash to a completely different value, but why is this a good thing?)
    -   Can you design a hash function that guarantees every value to end up in a different slot? (This is difficult, since a new value might come along that you don't have any control over, and by chance ends up in the same slot as another value.)
    -   If 60% of the slots have one or more values stored in them, what are the chances that a new value that comes along will end up in a slot that already has something in it? (It would be 60%, since that's the chance of randomly choosing an already used slot).

#### What to look for:

Could students predict the maximum and minimum number of chests that needed to be checked? 
Could they work out the probability of a particular outcome? Can they see that on average over lots of searches this method doesn't need to check many chests?

{panel end}

{panel type="ct-logic"}

# Logic

While evaluating the hash table and hash functions students will have been constantly exercising their logic skills.
They could also use their logical thinking skills when choosing their chest to identify which chests will be easier and which will be harder for their opponent to find.

#### What to look for:

Can students reason that when searching for a value that hashes to an empty group, you don't need to do any more checks to know that the value isn't available in the entire table?
Did students deduce that choosing a chest which is the only one in a slot is a bad strategy, and choosing one from a slot with lots of chests is a good strategy? 
Can they explain how they figured this out?

{panel end}
