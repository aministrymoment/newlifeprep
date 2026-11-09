"""Probability and Statistics, Unit 6: Inference and Honest Statistics. Florida B.E.S.T. Data Analysis and Probability strand (MA.912.DP) cited at strand level; recheck at CPALMS."""
from ps_units1 import CLOSE

UNIT6 = dict(
 title="Unit 6: Inference and Honest Statistics",
 std="MA.912.DP",
 topics=[
 dict(t="6.1 Sampling Variability and Margin of Error", std="MA.912.DP",
 body="""Inference means using a sample to draw conclusions about a population. Proverbs 18:17 says, He that is first in his own cause seemeth just; but his neighbour cometh and searcheth him. A single report may sound convincing until someone checks it. In statistics, we check by asking how much a result would change if we took another sample.

Suppose 60 percent of a random sample of students say they favor a later start time. If we took another random sample from the same school, we would probably not get exactly 60 percent again. This difference from sample to sample is sampling variability. A sample proportion is written p hat, and it is a statistic that estimates the population proportion p. Because p hat changes from sample to sample, we describe how much it typically varies.

Three facts guide us. First, with a random sample, the sample proportions center on the true population proportion, so random sampling is not biased. Second, larger samples vary less than smaller samples. Third, the variation depends on the sample size and not on the size of the population, as long as the population is much larger than the sample. A random sample of 400 from a school of 2,000 is just as informative as 400 from a school of 20,000.

The margin of error tells how far a sample result is likely to be from the truth. For a poll with about 95 percent confidence, a quick estimate of the margin of error for a sample proportion is 1 divided by the square root of the sample size. For 100 people, the margin of error is about 1 divided by 10, which is 10 percentage points. For 400 people it is about 5 points. For 900 it is about 3.3 points. For 1,600 it is about 2.5 points. Notice that to cut the margin of error in half, we must multiply the sample size by 4. This is why most national polls survey around 1,000 people.

The margin of error accounts only for chance variation in random sampling. It does not correct for biased samples, poor questions or people who do not respond.

Your task: (1) Explain sampling variability. (2) Estimate the margin of error for samples of 100 and 400. (3) Tell why a larger sample gives a more reliable estimate and what the margin of error does not cover.""",
 script="""Welcome back. Listen, Proverbs 18:17 says, He that is first in his own cause seemeth just; but his neighbour cometh and searcheth him. A single report may sound convincing until someone checks it. In statistics we check by asking how much a result would change with another sample.

Now watch this. Inference means using a sample to draw conclusions about a population. Suppose 60 percent of a random sample favor a later start time. Another random sample would probably not give exactly 60 percent. That difference from sample to sample is sampling variability. The sample proportion is written p hat, and it estimates the population proportion p.

Look at three facts. Random samples center on the true value. Larger samples vary less. And the variation depends on the sample size, not on the size of the population.

The margin of error tells how far a result is likely to be from the truth. A quick estimate at about 95 percent confidence is 1 divided by the square root of the sample size. For 100 people it is about 10 points. For 400 it is about 5 points. For 900 it is about 3.3. For 1,600 it is about 2.5. To cut the margin in half, multiply the sample size by 4.

But remember, the margin of error covers only chance variation. It does not correct for bias, bad questions or people who do not respond.

Your task is to explain sampling variability, estimate a margin of error and say what the margin of error does not cover. Take the four question check.""" + CLOSE,
 quiz=[
 ("The difference in results from one random sample to the next is called:", ["Sampling variability", "Bias", "A parameter", "A residual"], 0, "Random samples give somewhat different results."),
 ("The quick margin of error for a sample of 400 is about:", ["5 percentage points", "10 percentage points", "2.5 percentage points", "20 percentage points"], 0, "1 divided by the square root of 400 equals 1/20, or 5 percent."),
 ("To cut the margin of error in half, the sample size must be:", ["Multiplied by 4", "Doubled", "Halved", "Unchanged"], 0, "The margin shrinks with the square root of n."),
 ("The margin of error does NOT correct for:", ["A biased sampling method", "Random chance", "Sample size", "Sampling variability"], 0, "Bias is a different problem from chance variation."),
 ]),
 dict(t="6.2 Confidence Intervals for a Proportion", std="MA.912.DP",
 body="""A single number is a good guess, but a range is more honest. Luke 14:28 says, For which of you, intending to build a tower, sitteth not down first, and counteth the cost, whether he have sufficient to finish it? A confidence interval counts the cost of uncertainty, so that we do not claim more than our data support.

A confidence interval gives a range of plausible values for a population parameter. For a population proportion, an approximate 95 percent confidence interval is p hat plus or minus 2 times the standard error. The standard error is the square root of p hat times the quantity 1 minus p hat, divided by n. The number 2 is a rounded form of 1.96.

Example: a random sample of 400 students shows that 240 favor a new lunch schedule. The sample proportion p hat is 240 divided by 400, which is 0.60. The standard error is the square root of 0.60 times 0.40 divided by 400. The product 0.60 times 0.40 is 0.24, and 0.24 divided by 400 is 0.0006. The square root of 0.0006 is about 0.0245. Twice that is about 0.049. So the interval runs from 0.60 minus 0.049 to 0.60 plus 0.049, which is about 0.551 to 0.649. We say we are 95 percent confident that between about 55 percent and 65 percent of all the students favor the new schedule.

Interpret carefully. The confidence level describes the method. If we repeated the process many times with new random samples, about 95 percent of the intervals would capture the true proportion. It does not mean that 95 percent of students are in the interval, and it does not mean there is a 95 percent chance that the true value changes. The true value is fixed. The interval is what varies.

Intervals have conditions. The sample must be random, the trials independent, and there should be at least 10 successes and 10 failures in the sample. A higher confidence level makes a wider interval, and a larger sample makes a narrower one.

Your task: (1) Compute a 95 percent confidence interval for a proportion. (2) Interpret it in a sentence. (3) Tell how sample size and confidence level change the width.""",
 script="""Welcome back. Listen, Luke 14:28 says, For which of you, intending to build a tower, sitteth not down first, and counteth the cost? A confidence interval counts the cost of uncertainty, so we do not claim more than the data support.

Now watch this. A confidence interval gives a range of plausible values for a parameter. For a proportion, an approximate 95 percent interval is p hat plus or minus 2 times the standard error. The standard error is the square root of p hat times 1 minus p hat, divided by n.

Look at an example. A random sample of 400 students shows that 240 favor a new lunch schedule. So p hat is 0.60. The standard error is the square root of 0.24 divided by 400, which is the square root of 0.0006, or about 0.0245. Twice that is about 0.049. The interval runs from about 0.551 to 0.649. We are 95 percent confident that between about 55 percent and 65 percent of all students favor the new schedule.

Interpret carefully. The confidence level describes the method. If we repeated the process with many new random samples, about 95 percent of the intervals would capture the true proportion. The true proportion is fixed. The interval is what varies.

A higher confidence level makes the interval wider. A larger sample makes it narrower. The sample must be random and have at least 10 successes and 10 failures.

Your task is to compute an interval, interpret it and tell how sample size changes its width. Take the four question check.""" + CLOSE,
 quiz=[
 ("An approximate 95 percent confidence interval for a proportion is:", ["p hat plus or minus 2 standard errors", "p hat times 2", "p hat plus 95", "The mean plus the median"], 0, "Use about 2 standard errors on each side."),
 ("A sample of 400 has p hat equal to 0.60. The standard error is about:", ["0.0245", "0.24", "0.6", "0.049"], 0, "The square root of 0.24 divided by 400 is about 0.0245."),
 ("The 95 percent confidence interval from that sample is about:", ["0.551 to 0.649", "0.40 to 0.80", "0.595 to 0.605", "0.60 to 0.70"], 0, "0.60 plus or minus 0.049."),
 ("A larger sample size makes a confidence interval:", ["Narrower", "Wider", "Biased", "Impossible"], 0, "More data means a more precise estimate."),
 ]),
 dict(t="6.3 Testing a Claim: The Idea of Significance", std="MA.912.DP",
 body="""Statistics helps us test claims. Acts 17:11 says of the believers in Berea, These were more noble than those in Thessalonica, in that they received the word with all readiness of mind, and searched the scriptures daily, whether those things were so. The Bereans did not accept a claim just because a respected teacher made it. They tested it against evidence. Careful thinkers test claims and then hold to what is true.

A significance test follows a pattern. First we state a null hypothesis, which is the claim we start with, such as a coin is fair, so p equals 0.5. Next we state an alternative hypothesis, such as the coin is not fair. Then we collect data and ask how likely a result at least this extreme would be if the null hypothesis were true. That probability is the p value. A small p value means the result would be very surprising if the claim were true, which is evidence against the claim.

Suppose a coin is tossed 10 times and lands heads 10 times. If the coin were fair, the probability of 10 heads in a row is 1/2 to the 10th power, which is 1/1024, or about 0.001. This is very unlikely, so we have strong evidence the coin is not fair.

Now suppose 60 heads in 100 tosses. If the coin were fair, the standard error of the sample proportion is the square root of 0.5 times 0.5 divided by 100, which is 0.05. The result 0.60 is 0.10 above 0.50, and 0.10 divided by 0.05 is 2 standard errors. A result 2 standard errors from the claimed value is on the edge of what we would expect by chance. The p value is about 0.05. A common cutoff, called the significance level, is 0.05. If the p value is less than the significance level, we reject the null hypothesis and call the result statistically significant.

Take care with the meaning. A significance test can make two kinds of errors. A Type I error rejects a true claim, and a Type II error fails to reject a false claim. Also, statistically significant does not mean important. With a huge sample, even a tiny difference can be significant. Always ask how big the difference is and whether it matters.

Your task: (1) State a null and alternative hypothesis for a claim. (2) Explain what a p value tells you. (3) Explain why statistically significant does not always mean important.""",
 script="""Welcome back. Listen, Acts 17:11 says the Bereans searched the scriptures daily, whether those things were so. They did not accept a claim just because a respected teacher made it. They tested it against evidence.

Now watch this. A significance test starts with a null hypothesis, the claim we begin with, such as a coin is fair, so p equals 0.5. The alternative hypothesis says the coin is not fair. We collect data and ask how likely a result this extreme would be if the null hypothesis were true. That probability is the p value. A small p value means the result would be very surprising if the claim were true.

Look at the coin. Ten heads in ten tosses has probability 1/2 to the 10th power, which is 1/1024, or about 0.001. That is strong evidence the coin is not fair.

Now suppose 60 heads in 100 tosses. The standard error under a fair coin is 0.05. The result of 0.60 is 0.10 above 0.50, which is 2 standard errors. The p value is about 0.05. A common significance level is 0.05. If the p value is smaller, we reject the null hypothesis and call the result statistically significant.

Be careful. A Type I error rejects a true claim. A Type II error fails to reject a false claim. And statistically significant does not mean important. With a huge sample, even a tiny difference can be significant. Always ask how big the difference is.

Your task is to state hypotheses, explain a p value and explain why significant does not always mean important. Take the four question check.""" + CLOSE,
 quiz=[
 ("The null hypothesis is:", ["The claim we start with, often of no effect", "The proof that an effect exists", "The sample size", "The margin of error"], 0, "The null hypothesis is the starting claim being tested."),
 ("A small p value means the observed result would be:", ["Very surprising if the null hypothesis were true", "Very likely if the null hypothesis were true", "Certain", "Caused by the sample size alone"], 0, "A small p value is evidence against the claim."),
 ("The probability of 10 heads in 10 tosses of a fair coin is:", ["1/1024", "1/10", "1/20", "1/2"], 0, "1/2 to the 10th power equals 1/1024."),
 ("Rejecting a true null hypothesis is called a:", ["Type I error", "Type II error", "Correct decision", "Residual"], 0, "A Type I error is a false alarm."),
 ]),
 dict(t="6.4 Honest Statistics and Wise Use of Numbers", std="MA.912.DP",
 body="""Numbers can reveal the truth, and numbers can also be used to mislead. Proverbs 20:10 says, Divers weights, and divers measures, both of them are alike abomination to the LORD. Exodus 20:16 commands, Thou shalt not bear false witness against thy neighbour. Proverbs 14:15 adds, The simple believeth every word: but the prudent man looketh well to his going. A person who uses statistics must be honest, and a person who reads statistics must be prudent.

Here are common ways statistics mislead. A truncated axis starts a bar graph at a number other than zero, so a small difference looks huge. A stretched or squeezed scale on a line graph can make a trend look steep or flat. Pictures drawn in three dimensions can make one part look larger than it is. Cherry picking reports only the data that support a point and hides the rest. A biased sample or a leading question produces the answer the writer wanted. A percent without the number behind it can deceive: a 50 percent increase from 2 cases to 3 cases is tiny. A reported average may be the mean when the median would be fairer, or the other way around. A claim that two things are linked may hide a lurking variable. A result that was not significant may simply not be reported.

A prudent reader asks several questions. Who collected the data and why? How was the sample chosen and how large is it? What was the exact question? What do the axes and scales show? Is a percent or an average hiding the real picture? Is the margin of error reported? Could another factor explain the pattern?

A prudent writer follows the same rules. Choose graphs that start at zero for bar charts. Label axes and units. Report the sample size and the margin of error. Explain your methods and admit limits. Say what the data cannot tell us.

Statistics will be useful to you in many callings. Pastors read attendance and giving trends. Nurses read medical studies. Teachers use test results. Business owners study sales. Voters hear claims about polls. In every case, a person of integrity tells the truth with numbers, serves the good of others, and gives glory to God.

Your task: (1) List four ways a graph or a statistic can mislead. (2) Write five questions a prudent reader should ask. (3) Explain how Proverbs 20:10 applies to the use of data.""",
 script="""Welcome to our last lesson. Listen, Proverbs 20:10 says, Divers weights, and divers measures, both of them are alike abomination to the LORD. Exodus 20:16 says, Thou shalt not bear false witness against thy neighbour. And Proverbs 14:15 says, the prudent man looketh well to his going. A person who uses statistics must be honest, and a person who reads statistics must be prudent.

Now watch this. Here are ways statistics mislead. A truncated axis starts a bar graph above zero so a small difference looks huge. A stretched scale makes a trend look steep or flat. Three dimensional pictures make one part look larger. Cherry picking reports only data that support a point. A biased sample or leading question gives the answer the writer wanted. A percent without the number behind it can deceive. A lurking variable can hide behind a link. And results that did not work may simply not be reported.

Look at the questions a prudent reader asks. Who collected the data and why? How was the sample chosen and how large is it? What was the exact question? What do the axes and scales show? Is the margin of error reported? Could another factor explain the pattern?

A prudent writer follows the same rules. Start bar charts at zero. Label axes and units. Report the sample size and margin of error. Admit the limits.

Pastors, nurses, teachers, business owners and voters all meet statistics. In every case, a person of integrity tells the truth with numbers, serves others and gives glory to God.

Your task is to list four ways statistics mislead, write five questions for a reader and explain Proverbs 20:10. Take the four question check.""" + CLOSE,
 quiz=[
 ("A bar graph that does not start at zero is an example of a:", ["Truncated axis that can mislead", "Normal curve", "Random sample", "Box plot"], 0, "A truncated axis exaggerates differences."),
 ("Reporting only the data that support your point is called:", ["Cherry picking", "Random sampling", "Stratifying", "Replication"], 0, "Cherry picking hides the rest of the evidence."),
 ("A 50 percent increase from 2 cases to 3 cases is:", ["A small change in actual numbers", "A very large change", "Impossible", "A decrease"], 0, "A percent without the counts can mislead."),
 ("Which question should a prudent reader ask about a poll?", ["How was the sample chosen and how large is it?", "Is the poll on the front page?", "Is the chart colorful?", "Is the headline short?"], 0, "Sample method and size determine reliability."),
 ]),
 ],
 assess=dict(t="Assessment 6: Inference and Honest Statistics",
 prompt="""Write a report of at least 250 words on inference and honest statistics. Use complete sentences, show every calculation and label each part. Proverbs 20:10 says, Divers weights, and divers measures, both of them are alike abomination to the LORD.

Part 1: A random sample of 900 adults shows that 540 attend church at least once a month. Find p hat, the quick margin of error, and an approximate 95 percent confidence interval using the standard error. Interpret your interval in one sentence.
Part 2: Explain sampling variability and tell why a larger sample gives a more reliable estimate. Tell what the margin of error does not correct for.
Part 3: A coin is tossed 100 times and lands heads 70 times. State the null and alternative hypotheses, find the number of standard errors from 0.5, and explain what this suggests.
Part 4: Describe three ways a graph or statistic can mislead, with an example of each, and rewrite one misleading claim honestly.
Part 5: Explain, using Exodus 20:16 or Proverbs 14:15, how a Christian should use and read statistics in school, church or work.""",
 rubric="""100 points. Part 1: 30 points. Part 2: 15 points. Part 3: 20 points. Part 4: 20 points. Part 5: 10 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 6: Telling the Truth with Numbers",
 prompt="""Write a post of at least 120 words that (1) describes a statistic, poll or graph you have seen in the news or on social media and what question you would ask about it, (2) explains why honest numbers matter to a church, school or business, (3) describes how you will use what you learned in this course in your future calling, and (4) connects your answer to Proverbs 20:10, Proverbs 14:15 or Acts 17:11. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why is it a form of false witness to use a misleading graph on purpose? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("A sample proportion is written:", ["p hat", "mu", "z", "r"], 0, "P hat is the sample proportion."),
 ("The quick margin of error for a sample of 900 is about:", ["3.3 percentage points", "10 percentage points", "5 percentage points", "30 percentage points"], 0, "1 divided by 30 is about 0.033."),
 ("A 95 percent confidence interval for a proportion is about p hat plus or minus:", ["2 standard errors", "1 standard error", "10 standard errors", "The mean"], 0, "Two standard errors gives about 95 percent."),
 ("The 95 percent confidence level describes:", ["How often the method captures the true value", "The percent of the population in the interval", "The sample size", "The p value"], 0, "Confidence describes the long run success of the method."),
 ("A p value of 0.001 suggests:", ["Strong evidence against the null hypothesis", "Strong evidence for the null hypothesis", "No evidence", "A biased sample"], 0, "A tiny p value is surprising under the null hypothesis."),
 ("A Type II error is:", ["Failing to reject a false null hypothesis", "Rejecting a true null hypothesis", "A correct decision", "A margin of error"], 0, "A Type II error misses a real effect."),
 ("A bar graph with its axis starting far above zero can:", ["Exaggerate differences", "Make all bars equal", "Improve accuracy", "Remove bias"], 0, "A truncated axis can mislead."),
 ("Exodus 20:16 applies to statistics because we must not:", ["Give false witness with numbers", "Count anything", "Use graphs", "Take samples"], 0, "Honest data respects our neighbor."),
 ],
)
