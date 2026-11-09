"""Probability and Statistics, Unit 4: Counting and Random Variables. Florida B.E.S.T. Data Analysis and Probability strand (MA.912.DP) cited at strand level; recheck at CPALMS."""
from ps_units1 import CLOSE

UNIT4 = dict(
 title="Unit 4: Counting and Random Variables",
 std="MA.912.DP",
 topics=[
 dict(t="4.1 The Counting Principle and Permutations", std="MA.912.DP",
 body="""To find a probability we often need to count the outcomes. Psalm 147:4 says, He telleth the number of the stars; he calleth them all by their names. God counts what we cannot, and we learn smart ways to count what we can.

The fundamental counting principle says that if one choice can be made in m ways and a second choice in n ways, the two choices together can be made in m times n ways. A student has 3 shirts and 4 pairs of pants, so there are 3 times 4, or 12, outfits. A four digit code, where each digit can be 0 through 9 and digits may repeat, has 10 times 10 times 10 times 10, or 10,000, possibilities. A license tag with three letters has 26 times 26 times 26, or 17,576, possibilities.

When order matters and no item is used twice, we count arrangements. A factorial is the product of a whole number and every positive whole number below it. We write 5 factorial as 5 followed by an exclamation point, and it equals 5 times 4 times 3 times 2 times 1, which is 120. By definition, 0 factorial equals 1. Four students can stand in a line in 4 factorial ways, which is 24.

A permutation is an ordered arrangement of some items chosen from a larger group. If five people run for president, vice president and secretary, the president can be chosen 5 ways, the vice president 4 ways, and the secretary 3 ways. The number of permutations is 5 times 4 times 3, which is 60. In symbols, the number of permutations of n items taken r at a time equals n factorial divided by the factorial of n minus r. Here, 5 factorial divided by 2 factorial is 120 divided by 2, which is 60.

The key question is whether order matters. If first place, second place and third place are different honors, order matters. The word arrangement signals a permutation.

Your task: (1) Use the counting principle to count outfits or codes. (2) Compute a factorial. (3) Count the permutations when 5 people compete for 3 different offices.""",
 script="""Welcome back. Listen, Psalm 147:4 says, He telleth the number of the stars; he calleth them all by their names. God counts what we cannot. We learn smart ways to count what we can.

Now watch this. The fundamental counting principle says that if one choice can be made in m ways and another in n ways, together they can be made in m times n ways. Three shirts and four pairs of pants give 12 outfits. A four digit code gives 10 times 10 times 10 times 10, which is 10,000 possibilities.

Look at factorials. 5 factorial is 5 times 4 times 3 times 2 times 1, which is 120. Zero factorial is defined to be 1. Four students can stand in a line in 4 factorial, or 24, ways.

A permutation is an ordered arrangement of some items from a larger group. Five people run for president, vice president and secretary. The president can be chosen 5 ways, the vice president 4 ways, the secretary 3 ways. That is 5 times 4 times 3, or 60.

The key question is whether order matters. If first, second and third place are different honors, order matters, and that signals a permutation.

Your task is to use the counting principle, compute a factorial and count permutations. Take the four question check.""" + CLOSE,
 quiz=[
 ("A student has 3 shirts and 4 pairs of pants. The number of outfits is:", ["12", "7", "1", "24"], 0, "3 times 4 equals 12."),
 ("5 factorial equals:", ["120", "25", "60", "5"], 0, "5 times 4 times 3 times 2 times 1 equals 120."),
 ("Five candidates compete for president, vice president and secretary. The number of ways to fill the offices is:", ["60", "10", "125", "15"], 0, "5 times 4 times 3 equals 60."),
 ("A four digit code using digits 0 through 9 with repeats allowed has how many possibilities?", ["10,000", "5,040", "40", "9,999"], 0, "10 times 10 times 10 times 10 equals 10,000."),
 ]),
 dict(t="4.2 Combinations", std="MA.912.DP",
 body="""Sometimes order does not matter. Luke 6:13 says, And when it was day, he called unto him his disciples: and of them he chose twelve, whom also he named apostles. The Lord chose a group of twelve from a larger group of disciples. The group itself mattered. The order in which He named them is not what defines the group.

A combination is a selection of items in which order does not matter. Choosing three students for a committee gives the same committee whether we name Ann, Ben and Chris, or Chris, Ben and Ann. To count combinations, start with the number of permutations and divide by the number of ways to arrange the chosen items. The number of combinations of n items taken r at a time equals n factorial divided by the product of r factorial and the factorial of n minus r.

Example: how many 3 person committees can be formed from 5 people? The permutations of 5 taken 3 at a time are 5 times 4 times 3, which is 60. Each committee of 3 can be arranged in 3 factorial, or 6, orders, so we divide: 60 divided by 6 is 10. Another example: choosing 3 people from 8 gives 8 times 7 times 6 divided by 3 times 2 times 1, which is 336 divided by 6, or 56. Choosing 2 from 10 gives 10 times 9 divided by 2, which is 45.

We can combine counting with probability. A committee of 3 is chosen at random from 5 girls and 3 boys. The total number of committees is 56. The number of committees with all girls is the number of ways to choose 3 of 5 girls, which is 10. So the probability that the committee is all girls is 10/56, or 5/28.

To decide between the two, ask whether the order changes the result. A president and vice president is a permutation. A pair of co chairs is a combination.

Your task: (1) Explain the difference between a permutation and a combination. (2) Compute the number of ways to choose 3 people from 8. (3) Find the probability that a random committee is all girls.""",
 script="""Welcome back. Listen, Luke 6:13 says, And when it was day, he called unto him his disciples: and of them he chose twelve. The Lord chose a group from a larger group. The group mattered, not the order in which He named them.

Now watch this. A combination is a selection in which order does not matter. A committee of Ann, Ben and Chris is the same committee as Chris, Ben and Ann. To count combinations, take the number of permutations and divide by the number of ways to arrange the chosen items.

Look at an example. How many 3 person committees can we form from 5 people? The permutations are 5 times 4 times 3, which is 60. Each committee can be arranged in 3 factorial, or 6, ways, so 60 divided by 6 is 10. Choosing 3 from 8 gives 336 divided by 6, which is 56. Choosing 2 from 10 gives 45.

Now combine counting with probability. A committee of 3 is chosen at random from 5 girls and 3 boys. There are 56 possible committees, and 10 of them are all girls. The probability is 10/56, or 5/28.

To decide which to use, ask whether the order changes the result. President and vice president is a permutation. Two co chairs is a combination.

Your task is to explain permutation and combination, count a selection and find a probability. Take the four question check.""" + CLOSE,
 quiz=[
 ("A selection in which order does not matter is a:", ["Combination", "Permutation", "Factorial", "Complement"], 0, "That is the definition of a combination."),
 ("The number of ways to choose 3 people from 5 is:", ["10", "60", "15", "5"], 0, "60 divided by 6 equals 10."),
 ("The number of ways to choose 2 people from 10 is:", ["45", "90", "20", "100"], 0, "10 times 9 divided by 2 equals 45."),
 ("Choosing a president and a vice president from a group is a:", ["Permutation", "Combination", "Factorial", "Complement"], 0, "The two offices are different, so order matters."),
 ]),
 dict(t="4.3 Random Variables and Expected Value", std="MA.912.DP",
 body="""A random variable is a numerical outcome of a random process. Proverbs 13:11 says, Wealth gotten by vanity shall be diminished: but he that gathereth by labour shall increase. Expected value helps us see why get rich quick plans so often fail.

A discrete random variable takes a list of separate values, each with a probability. A probability distribution lists the values and their probabilities, and the probabilities add to 1. Let X be the number of heads in two tosses of a fair coin. The outcomes TT, HT, TH and HH give X equal to 0 with probability 1/4, X equal to 1 with probability 1/2, and X equal to 2 with probability 1/4.

The expected value of X is the long run average value. We find it by multiplying each value by its probability and adding the results. For the coin, the expected value is 0 times 1/4, plus 1 times 1/2, plus 2 times 1/4, which is 0 plus 1/2 plus 1/2, or 1. Over many repetitions we expect an average of 1 head per pair of tosses, even though a single pair can never show exactly the average in every case.

Expected value is used in business and in fairness. Suppose a school carnival game costs 2 dollars to play. A spinner has a 1 in 5 chance of winning a 5 dollar prize and otherwise wins nothing. The expected prize is 5 times 1/5, which is 1 dollar. Because the player pays 2 dollars, the player expects to come out 1 dollar behind on average, and the school expects to raise 1 dollar per play. Such a game is fine as a fundraiser when everyone knows the rules and plays for fun. The same arithmetic shows why casinos and lotteries are designed so that players lose money over time. A sensible believer counts the cost and does not stake the family budget on a game that is built to take money.

Insurance works the same way. Companies charge a little more than the expected cost of claims so that families are protected from rare large losses.

Your task: (1) Build a probability distribution for a random variable. (2) Compute an expected value. (3) Explain why a game with a negative expected value for the player is a poor way to build wealth.""",
 script="""Welcome back. Listen, Proverbs 13:11 says, Wealth gotten by vanity shall be diminished: but he that gathereth by labour shall increase. Expected value shows us why get rich quick plans so often fail.

Now watch this. A random variable is a numerical outcome of a random process. A probability distribution lists the values and their probabilities, and the probabilities add to 1. Let X be the number of heads in two coin tosses. X is 0 with probability 1/4, 1 with probability 1/2, and 2 with probability 1/4.

The expected value is the long run average. Multiply each value by its probability and add. For the coin, 0 times 1/4, plus 1 times 1/2, plus 2 times 1/4, equals 1.

Look at a carnival game. It costs 2 dollars to play. A spinner has a 1 in 5 chance of winning 5 dollars. The expected prize is 5 times 1/5, which is 1 dollar. The player pays 2 dollars, so on average the player comes out 1 dollar behind and the school raises 1 dollar per play. As a fundraiser with open rules, that is fun. But the same arithmetic shows why casinos and lotteries are built so that players lose over time. A wise believer counts the cost and does not stake the family budget on a game designed to take money.

Insurance works the same way. It protects families from rare large losses.

Your task is to build a distribution, compute an expected value and explain why a losing game is a poor way to build wealth. Take the four question check.""" + CLOSE,
 quiz=[
 ("The probabilities in a probability distribution add to:", ["1", "0", "100 dollars", "The mean"], 0, "All outcomes together are certain."),
 ("The expected number of heads in two fair coin tosses is:", ["1", "2", "1/2", "4"], 0, "0 times 1/4 plus 1 times 1/2 plus 2 times 1/4 equals 1."),
 ("A game pays 5 dollars with probability 1/5 and nothing otherwise. The expected prize is:", ["1 dollar", "5 dollars", "25 cents", "2 dollars"], 0, "5 times 1/5 equals 1 dollar."),
 ("If a game costs 2 dollars and the expected prize is 1 dollar, the player on average:", ["Loses 1 dollar per play", "Gains 1 dollar per play", "Breaks even", "Wins every time"], 0, "The player expects to be 1 dollar behind."),
 ]),
 dict(t="4.4 The Binomial Distribution", std="MA.912.DP",
 body="""Many situations repeat the same chance process again and again. Galatians 6:9 says, And let us not be weary in well doing: for in due season we shall reap, if we faint not. Repeated trials add up over time, and the binomial distribution gives the pattern for counting successes in a fixed number of repeated trials.

A situation is binomial when four conditions are met. There are a fixed number of trials, which we call n. Each trial has only two outcomes, success or failure. The trials are independent. The probability of success, p, is the same on every trial.

Example: a student makes 80 percent of her free throws. She shoots 3 times. Let X be the number she makes. Here n is 3 and p is 0.8, so the probability of a miss is 0.2. The probability of exactly k successes is the number of ways to choose which k trials succeed, times p to the power k, times the probability of failure to the power n minus k.

To find exactly 2 makes, there are 3 ways to choose which 2 shots go in, so the probability is 3 times 0.8 times 0.8 times 0.2, which is 3 times 0.64 times 0.2, or 0.384. Exactly 3 makes is 0.8 times 0.8 times 0.8, which is 0.512. Exactly 1 make is 3 times 0.8 times 0.2 times 0.2, which is 0.096. No makes is 0.2 times 0.2 times 0.2, which is 0.008. These four probabilities add to 1. The probability of at least 2 makes is 0.384 plus 0.512, which is 0.896.

The mean of a binomial random variable is n times p. Here it is 3 times 0.8, which is 2.4 makes per set of three shots. The standard deviation is the square root of n times p times the probability of failure.

Galatians 6:7 reminds us that whatsoever a man soweth, that shall he also reap. Practice, like seed, produces a harvest over many trials.

Your task: (1) Decide whether a situation is binomial and name n and p. (2) Find the probability of exactly 2 successes in 3 trials. (3) Find the mean of a binomial random variable.""",
 script="""Welcome back. Listen, Galatians 6:9 says, And let us not be weary in well doing: for in due season we shall reap, if we faint not. Repeated trials add up over time.

Now watch this. A situation is binomial when there are a fixed number of trials, each trial has two outcomes, the trials are independent, and the probability of success is the same each time.

Look at an example. A student makes 80 percent of her free throws and shoots three times. Here n is 3, p is 0.8, and the chance of a miss is 0.2. For exactly 2 makes, there are 3 ways to choose which two shots go in. The probability is 3 times 0.8 times 0.8 times 0.2, which is 0.384. Exactly 3 makes is 0.512. Exactly 1 make is 0.096. No makes is 0.008. Those four add to 1. The chance of at least 2 makes is 0.384 plus 0.512, which is 0.896.

The mean of a binomial random variable is n times p. Here it is 3 times 0.8, or 2.4 makes.

Galatians 6:7 says, whatsoever a man soweth, that shall he also reap. Practice, like seed, produces a harvest over many trials.

Your task is to decide whether a situation is binomial, find the probability of exactly 2 successes in 3 trials and find a mean. Take the four question check.""" + CLOSE,
 quiz=[
 ("Which is NOT a condition for a binomial situation?", ["The probability of success changes each trial", "A fixed number of trials", "Two outcomes per trial", "Independent trials"], 0, "The success probability must stay the same."),
 ("A shooter makes 80 percent of free throws. The mean number of makes in 3 shots is:", ["2.4", "0.8", "3", "1.6"], 0, "n times p equals 3 times 0.8."),
 ("The probability of exactly 2 makes in 3 shots at 80 percent is:", ["0.384", "0.64", "0.512", "0.096"], 0, "3 times 0.64 times 0.2 equals 0.384."),
 ("The probability of making all 3 shots at 80 percent is:", ["0.512", "0.8", "0.24", "0.384"], 0, "0.8 times 0.8 times 0.8 equals 0.512."),
 ]),
 ],
 assess=dict(t="Assessment 4: Counting and Random Variables",
 prompt="""Write a report of at least 250 words on counting and random variables. Use complete sentences, show every calculation and label each part. Galatians 6:9 says, And let us not be weary in well doing: for in due season we shall reap, if we faint not.

Part 1: A lunch menu offers 4 sandwiches, 3 sides and 5 drinks. Use the counting principle to find the number of different meals. Find 6 factorial.
Part 2: Seven students compete for first, second and third place. Find the number of possible outcomes. Then explain whether choosing a team of 3 from the same 7 students is a permutation or a combination, and find the number of teams.
Part 3: A committee of 3 is chosen at random from 4 girls and 3 boys. Find the probability that it is all boys.
Part 4: A fundraiser game costs 3 dollars to play. A spinner wins a 10 dollar prize with probability 1/5, and otherwise wins nothing. Find the expected prize and the expected result for the player. Explain, using Proverbs 13:11, why believers should be careful with games of chance.
Part 5: A basketball player makes 70 percent of free throws and shoots 3 times. Build the probability distribution for the number of makes and find the mean.""",
 rubric="""100 points. Part 1: 15 points. Part 2: 20 points. Part 3: 15 points. Part 4: 25 points. Part 5: 20 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 4: Counting the Cost",
 prompt="""Write a post of at least 120 words that (1) describes a situation from school, church or home where counting the number of choices or arrangements would help, (2) explains in your own words the difference between a permutation and a combination, (3) explains why expected value shows that games built to take money are a poor plan for building wealth, and (4) connects your answer to Proverbs 13:11, Luke 6:13 or Galatians 6:9. Then write a respectful reply of at least 40 words to another student's post, or answer this question: How does counting the cost before we begin a project show wisdom? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("The counting principle says two choices with m and n options can be made in:", ["m times n ways", "m plus n ways", "m minus n ways", "m divided by n ways"], 0, "Multiply the number of options."),
 ("4 factorial equals:", ["24", "10", "16", "12"], 0, "4 times 3 times 2 times 1 equals 24."),
 ("The number of ways to award first, second and third place among 5 runners is:", ["60", "10", "15", "125"], 0, "5 times 4 times 3 equals 60."),
 ("The number of ways to choose 3 members from a group of 8 is:", ["56", "336", "24", "11"], 0, "336 divided by 6 equals 56."),
 ("The expected value of a random variable is its:", ["Long run average", "Smallest value", "Most unlikely value", "Standard deviation"], 0, "Expected value is the long run mean."),
 ("A spinner pays 5 dollars with probability 1/5 and costs 2 dollars to play. The expected result for the player is:", ["A loss of 1 dollar", "A gain of 1 dollar", "Zero", "A gain of 3 dollars"], 0, "The expected prize is 1 dollar, and the player pays 2 dollars."),
 ("A binomial situation requires that trials be:", ["Independent", "Dependent", "Unlimited", "Without outcomes"], 0, "Independence is one of the four conditions."),
 ("The mean number of successes in 10 trials with p equal to 0.3 is:", ["3", "0.3", "7", "10"], 0, "n times p equals 10 times 0.3."),
 ],
)
