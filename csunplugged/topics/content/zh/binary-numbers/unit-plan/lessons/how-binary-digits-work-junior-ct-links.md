{panel type="ct-algorithm"}

# 算法思维

We used an algorithm in this lesson to convert a decimal number to a binary one. 我们称之为算法，因为这是一个逐步求解的过程。只要准确遵循这一过程，将可始终针对您提供的任意输入给出正确解答。

以下算法用于计算出应出示的相应点数卡，其文字表述如下所示：

- Find out the number of dots that is to be displayed. (We'll refer to this as the "number of dots remaining", which initially is the total number to be displayed.)

- For each card, from the left to the right (i.e. 8, 4, 2 then 1):
    
    - If the number of dots on the card is more than the number of dots remaining:
        
        - Hide the card
    
    - Otherwise:
        
        - Show the card
        
        - Subtract the number of dots on the card from the number of dots remaining

#### Examples of what you could look for:

在转换十进制和二进制时，哪些学生成功掌握方法，有条不紊地完成操作？ 哪些学生从最左侧的卡片入手，并每次将一张卡片移动到右侧，而不是随机选择卡片，然后翻来翻去直至找到正确数字？

{panel end}

{panel type="ct-abstraction"}

# 抽象

Abstraction and abstract thinking is generally difficult for young students so only a small amount of this section is likely to be applicable for them. We have included the information here however because it is useful background knowledge for teaching this topic.

Abstraction helps us simplify things because we can ignore the details we don’t currently need to know. Binary number representation is an abstraction that hides the complexity of the electronics and hardware inside a computer that store data.

就此而言，可忽略的详情包括：计算机使用电子电路等物理设备和电路中的电压来存储和移动数据。此外，通过许多复杂的物理和数学理论，均可使其发挥作用。

We don’t need to understand how these circuits work because we can use the abstraction of binary, as numbers made up of bits (0s and 1s), to understand data and work out problems, without having to think about what is happening ‘underneath the hood’ of the computer.

抽象的另一用途是，考虑用二进制表示任何给定数字的所需内容。 答案是，您只需两样不同的事物。 这可以是任何事物！ Two different colours, two animals, two symbols etc. 只要您能凑出两样不同的事物，即可在二进制下将其用来表示任意数字。这与计算机使用电力表示数据的情况一样。

#### Examples of what you could look for:

Who are the students that can demonstrate converting and representing binary numbers using things other than “1’s and 0’s”, “black and white”, and “off and on” (for example using :] and :[, or using people standing up or sitting down). 您若能将“黑色”和“白色”等术语与 0 和 1 交换，而学生不会担心它们之间存在差异，那么他们便已在练习抽象。

{panel end}

{panel type="ct-decomposition"}

# 分解

分解的一个示例是，一次将数字转换为二进制，再转换为一位。 针对每张点数卡的提问“这应该是 1 还是 0”，将问题分解为一系列问题。

#### Examples of what you could look for:

哪些学生认识到重点在于从最左边的卡开始，并且一次只考虑一位？ 哪些学生一次只关注一个位，而非试图一次性解决全部而导致不知所措？

{panel end}

{panel type="ct-pattern"}

# 泛化和模式

Recognising patterns in the way the binary number system works helps give us a deeper understanding of the concepts involved, and assists us in generalising these concepts and patterns so that we can apply them to other problems. Generalising these patterns may be more difficult for junior students, but recognising the patterns is a good exercise.

针对简单程度，我们从数字 1、2 和 4 开始，由学生们将其泛化为两倍的值。 In these exercises we converted to 4-bit numbers, but students (who are able to count high enough) may be able to generalise that to more 8-bit numbers, or larger.

十进制数向二进制数转换的算法，会遵循模式而进行。该模式可以泛化，以解决在个人使用现金支付时找零的问题。 For binary numbers you start with the largest bit and turn it on if it is needed or off if it is not, just like when you’re giving change you start with the largest denomination and then always take a coin (or note) whenever you need it. Jargon note: This is called a greedy algorithm.

{panel type="math"}

# Mathematical links

Ask students what is special about the decimal to binary conversion, in contrast with the general change giving algorithm, and have them observe that in the general case, you may need to give more than one coin of the same denomination, whereas in the binary conversion there is always one (or none) of each.

{panel end}

在二进制中向上计数时，特定卡翻面的频率均设有模式。 The first bit (with 1 dot) turns over every time we count up by one, the 2nd (with 2 dots) turns for every second number, the 3rd (with 4 dots) turns for every fourth… Is there a pattern like this when we count in decimal numbers?

{image file-path="img/topics/col_binary_counting_pattern.png" alt="二进制计数模式"}

If you have 4 of the cards and all are visible, you will have the number 15, which is 1 less than the value of the next card, 16. Is this pattern always true?

使用特定位数所能表示的数字量，与可添加的下一位数值一样。 例如，您可以使用 4 张卡（1、2、4、8）表示 16 个不同的数字（0-15），而序列中的下一张卡将是数字 16。 每次加入下一张卡时，所能表示的不同数字数量也相应翻倍。

要理清所使用的位数及其可表示的功率间关系，使用这些模式绝对意义非凡。

#### Examples of what you could look for:

Which students recognised quickly that each card was doubling the number of dots? Which students easily understand the patterns of cards flipping when counting with binary numbers?

{panel end}

{panel type="ct-logic"}

# 逻辑

逻辑思维是指使用已知规则和逻辑，从中推理出更多规则和信息。 一旦得知每张二进制卡所表示的数字，即可使用这些知识理清利用卡片表示其他数字的方式。 If you memorise how to represent the numbers we can make with 4 cards, does that mean you understand how to represent any number with any number of bits? It doesn’t, but you can understand how to do that if you understand the logic behind how these numbers with the 4 cards are made.

A good example of logical thinking in binary numbers is the reasoning for why each bit "has to" have a particular value (e.g. it has to be on, or it has to be off) to represent a given number. This in turn leads to an argument that there is only one representation for each number.

#### Examples of what you could look for:

Do students explicitly explain that the first bit needs to be a one because it is the only odd number and therefore is needed so that we are able to make any, and all, odd numbers? 若没有它，我们将只能创造出偶数。 Are students able to explain that each card "has to" be up the way it is for a given number e.g. the 8-dot card is needed for the number 9 because without it you only have 7 dots remaining (not enough); but it's not needed for the number 6 because it would give too many dots?

{panel end}

{panel type="ct-evaluation"}

# 评估

An example of evaluation is working out how many different values can be represented by a given number of bits (e.g. 4 bits can represent 16 different values), and vice versa (to represent 1000 different values, you need at least 10 bits).

#### Examples of what you could look for:

Can a student work out the range possible with 2 bits? (4)

3 bits? (8)

4 bits? (16)

如在表示法中多添加一位，范围将会增加多少？（翻倍）

{panel end}