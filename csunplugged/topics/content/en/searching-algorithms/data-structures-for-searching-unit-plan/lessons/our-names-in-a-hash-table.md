# Our names in a Hash Table

## Key questions

How do we assign data to a particular slot (group or bucket) in a hash table?
How do we find that data later when we search for it?

### Potential answers could include:

-   We work out its hash value, which tells us which slot to use.

-   We hash the data we are searching for and check if it is in that slot

## Lesson starter

Ask the students how they might convert a word (such as their name) to a hash value (number). With some guidance they may work out that you could assign a number to each letter (e.g. a=1, b=2, c=3...) and then add up those numbers. So, for example, "cat" would hash to 3+1+20 = 24. We'll use this system for this lesson.

## Lesson activities

1. Give each student a piece of paper. Have them write their name on it, and some personal detail such as their favourite colour or animal. This should be kept secret.

2. Have each student work out a hash value for their name by converting each letter to a number, and adding up the numbers. For example, Caitlin would be 3+1+9+20+12+9+14=68.

3. Have them work out their hash "slot" by taking the last digit of this number (e.g. 8 for Caitlin).

The next part could either be done as a whole class, or in groups of about 5. You will need a set of 10 boxes or envelopes (numbered from 0 to 9) for each group, or just one set for the whole class.

4. Students should place their paper in the box or envelope that corresponds to the digit they derived from their name.

5. Now pick a student's name, and have the class (or group) calculate their hash total, and therefore which box/envelope their paper is in.

6. Look through the box/envelope for their paper, and call out what their favourite colour/animal is. Repeat this for a few students.

{panel type="teaching"}

# Teaching observations

Students should be getting used to the idea that a good hash table will usually take you directly to the information that you need, but if it is too small then it's not so efficient. Calculating the hash values may become tedious for the students, but of course computers are good at that. They could use a spreadsheet or write a program to do this for them. There are examples in the 'plugging it in' programming exercises that do this. When doing it by hand, you could motivate students by adding some mystery and excitement to finding the information; or you might set up your own pieces of paper and have students find information that you've put on them.

{panel end}

{panel type="math"}

## Follow up

You could try this with 30 envelopes or containers; the hash function would need to be calculated using the total modulo 30. To do this, you could keep subtracting 30 from the number until it is between 0 and 29. Discuss if this is better. (There should be fewer papers in each envelope on average, and it may be that you usually just find one paper and access the information directly.

What if there were 100 envelopes? (It's unlikely that two names would end up in the same envelope). How about 1000 envelopes? (The hashed numbers aren't likely to get up to 1000, so a lot will remain unused. We'd need a better hash function that can generate bigger numbers.)

Discuss what happens to similar names - for example, does Tim end up in a similar place to Tom? (No, they hash to different values - hash tables don't necessarily keep similar things together).

Students could explore other hash functions. For example:

-   Multiply the character values by 1, 2, 3... and then add them e.g. Tracy would give 20x1 + 18x2 + 13x3 + 25x4.

-   There are other hash functions in the "plugging it in" programming activities that follow up from here. Some will be quite tedious for students to calculate, but are more effective at spreading the names out evenl

# Mathematical links

Basic facts: Calculating the hash functions exercises basic arithmetic operations, especially when multiplying each place by a different value.
Statistics: designing good hash tables is very much tied up with recognising that it's a statistical process; you want to minimise collisions (information hashing to the same place), so that most slots have just one item in them when they are reached.

{panel end}

## Applying what we have just learnt

Any information can be turned into a number. In fact, students probably already understand that all information on computers is represented using binary digits (bits), and these can be interpreted as numbers. In fact, because we're dealing with digital devices, you'll always find digits at the bottom of the representation of any data!

Hashing is widely used for searching data, including in databases. Its main weakness is that you can't find nearby values - if you search for "Tim" it won't necessarily be near "Timothy", so hashing is only used if you know exactly what the value is that you're searching for. Otherwise other systems such as the binary search tree (in the next lesson) can be used; the binary search tree is generally slightly slower than hashing, but it is good at finding near matches. In general, choosing algorithms involves many tradeoffs, and computer scientists become good at weighing up the alternatives. There's no one-size-fits-all!

## Lesson reflection

Did students have any surprising outcomes?
Were there some collisions that occurred just by chance that put lots of papers in the same slot?
