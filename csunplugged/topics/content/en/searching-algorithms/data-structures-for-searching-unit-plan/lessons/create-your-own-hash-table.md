# Create your own Hash Table

## Key questions

Where do people rely on computers to look up numbers and names for them quickly?

### Potential answers could include:

-   Search engines.

-   Finding a word in a text file.

-   When you log in to a site, it needs to look up your information e.g. documents that you've stored under your account name, if you have entered the correct password.

-   A system for generating random digits e.g. 10-sided dice, drawing numbers out of a hat, spinner pointing to 10 digits, or an online random number generator (e.g. random.org).

## Lesson starter

1. Give out two sheets, with 10 slots, to each student. Explain that they are going to create their own hash tables with treasure chests in them.

2. Remind them how the hash function from lesson 1 works i.e. you add all the digits together, then use the last digit as the slot. For example, the number 457 adds up to 4+5+7 = 16, so would point to slot.

## Lesson activities

1. Choose how many digits you will have in the numbers that you will use to label the treasure chests (about 4 or 5 digits is suitable).s.

2. Get students to generate a random number for their first treasure chest to put in their hash table. This could be done one digit at a time using a 10-sided die, drawing digits out of a hat, or a spinner pointing to 10 digits; or it could be done using an online random number generator such as random.org ([this link](https://www.random.org/integer-sets/?sets=1&num=8&min=1&max=99999&commas=on&order=random&format=html&rnd=new) will generate 8 5-digit numbers).

3. Once the students have a number for a treasure chest, get them to calculate its hash total, and put the number in its correct slot in the table. On their second sheet, they should draw a chest (a rectangle is sufficient) in the same slot. The entry just put on each sheet should both be labeled with the letter "A".
 
4. Have them add about 7 more treasure chests to their hash table, each with a different number generated randomly. They will need to label them with letters of the alphabet (sequentially), and put the corresponding blank chest on their second sheet.

5. Explain that when two chests end up in the same slot it is called a “collision”. Get the students to work out which of their slots had the most collisions, and ask around the class to find out how many collisions each student had. (Some students may have two or three collisions, or even more. It's possible, but extremely unlikely, that a student had all 8 values hash to the same slot.).

{panel type="teaching"}

# Teaching observations

Students might recognise that it's hard to get a large number of collisions by chance, but they could force it to happen by deliberately choosing numbers that will hash to the same slot. They could also do it by creating a (very) bad hash function, which will always give the same slot no matter what, for example it could be “divide the number by itself”, which would put every number in the first slot!

{panel end}

{panel type="math"}

# Mathematical links

Collisions are a statistical phenomenon, and working out what will happen in a hash table requires a good understanding of statistics. One simple observation is that if 70% of the slots have a value in them, and a random value is to be added, there is a 70% chance that it will have a collision. In other words, it is more likely than not! For this reason, in practice hash tables avoid getting too full; ideally they would be less than half full, but this wastes a lot of space, so in practice around 60% or 70% full is a common rule of thumb. Beyond this, the chance of a collision is very high, and this makes the tables much less efficient.

{panel end}

6. Now have students pair up, and give their blank sheet to their partner. They can now play the searching game, where each nominates which chest their partner needs to find, and then they take turns guessing the letter of the chest. (Students who have lots of collisions will have the best opportunity to give their partner a longer challenge!).

## Extension activity

Have the students do this again, but with the sheets with 20 slots. They should observe that for the 8 values there are fewer collisions, and searching is faster.

Students could also try a different hash function. For example, instead of just adding each digit, they could multiply the first digit by 1, the next by 2, the next by 3, and so on. This means that numbers with the same digits probably won't hash to the same value. For example, 4251 hashes to 4x1 + 2x2 + 5x3 + 1x4 = 27, whereas 2451 hashes to 2x1 +4x2 + 5x3 + 1x4 = 29. More importantly, it gives a bigger range of hash values.

Observing the chance of collisions is often associated with the ["Birthday problem"](https://en.wikipedia.org/wiki/Birthday_problem), which is that the chances of two people in a room having the same birthday (day and month) is surprisingly high. If you have 23 people in a room, there's a 50% chance that two of them share a birthday, and with 70 people, there's a 99.9% chance. You can try this with a class - have each student call out their birthday (if that is sensitive, have them think of the birthdate of a parent or friend who isn't in the class), write them on the board, and see how many you need to ask before two have the same birthday. What they see on the board is the same as the hash table slots filling up - each new birthday provides an extra "target" for a collision, and it becomes clear that it's hard to avoid a collision. (In practice it's even more likely that two students have the same birthday because more people are born in some months than others.).

## Applying what we have just learnt

Designing hash tables is a task that requires a tradeoff between making it as big as possible (to reduce collisions) without wasting too much space. It also involves making the hash function as random as possible so that values are spread evenly around the table. Of course, you can never be sure that by chance everything won't hash to the same location, even with a great hash function and a huge table. But when computer scientists design hash tables, they can make tradeoffs to ensure that it's likely to work well in normal circumstances.

## Lesson reflection

What were the surprises in this lesson? Did students realise that "random" is actually quite hard to achieve, but is important for developing efficient computer programs?
