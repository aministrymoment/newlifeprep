"""Probability and Statistics, Unit 2: Distributions, Spread and the Normal Curve. Florida B.E.S.T. Data Analysis and Probability strand (MA.912.DP) cited at strand level; recheck at CPALMS."""
from ps_units1 import CLOSE

UNIT2 = dict(
 title="Unit 2: Distributions, Spread and the Normal Curve",
 std="MA.912.DP",
 topics=[
 dict(t="2.1 Quartiles, the Five Number Summary and Box Plots", std="MA.912.DP",
 body="""The median splits ordered data into two halves, and quartiles split it further. Psalm 139:17 exclaims, How precious also are thy thoughts unto me, O God! how great is the sum of them! Large amounts of data can feel as vast as that, but a few well chosen numbers can organize them.

The five number summary lists the minimum, the first quartile Q1, the median, the third quartile Q3 and the maximum. To find them, put the data in order and find the median. The first quartile Q1 is the median of the lower half, and Q3 is the median of the upper half. When the number of values is odd, leave out the middle value when you split the halves.

Example: the data 2, 4, 5, 7, 8, 9, 11, 12, 14, 16 and 20 have 11 values. The median is the sixth value, 9. The lower half is 2, 4, 5, 7 and 8, so Q1 is 5. The upper half is 11, 12, 14, 16 and 20, so Q3 is 14. The five number summary is 2, 5, 9, 14 and 20.

The interquartile range, or IQR, is Q3 minus Q1. Here it is 14 minus 5, which is 9. The IQR measures the spread of the middle half of the data and is resistant to outliers.

A box plot, also called a box and whisker plot, draws the five number summary. A box runs from Q1 to Q3 with a line at the median, and whiskers extend toward the minimum and maximum. About one quarter of the data lies in each section. A box plot makes it easy to compare two groups side by side. If the median line sits near one end of the box, or one whisker is much longer, the data are skewed in that direction.

Your task: (1) Find the five number summary and IQR of a data set. (2) Draw or describe a box plot. (3) Tell what percent of the data lies between Q1 and Q3.""",
 script="""Welcome back. Listen, Psalm 139:17 says, How precious also are thy thoughts unto me, O God! how great is the sum of them! Big collections of numbers can feel overwhelming, but a few good summary numbers can organize them.

Now watch this. The five number summary is the minimum, Q1, the median, Q3 and the maximum. Put the data in order, find the median, then find the median of the lower half for Q1 and the median of the upper half for Q3.

Look at an example. The data 2, 4, 5, 7, 8, 9, 11, 12, 14, 16 and 20 have 11 values. The median is the sixth value, 9. The lower half is 2, 4, 5, 7, 8, so Q1 is 5. The upper half is 11, 12, 14, 16, 20, so Q3 is 14. The five number summary is 2, 5, 9, 14 and 20.

The interquartile range is Q3 minus Q1, which is 14 minus 5, or 9. It measures the spread of the middle half of the data and it is resistant to outliers.

A box plot draws the five number summary. The box runs from Q1 to Q3 with a line at the median, and the whiskers reach toward the minimum and maximum. Each section holds about one quarter of the data.

Your task is to find a five number summary and IQR, describe a box plot and say what percent lies between Q1 and Q3. Take the four question check.""" + CLOSE,
 quiz=[
 ("The five number summary includes the minimum, Q1, the median, Q3 and the:", ["Maximum", "Mean", "Mode", "Range"], 0, "The five values are min, Q1, median, Q3 and max."),
 ("For the data 2, 4, 5, 7, 8, 9, 11, 12, 14, 16 and 20, Q3 is:", ["14", "12", "16", "9"], 0, "The upper half is 11, 12, 14, 16, 20, and its median is 14."),
 ("The IQR equals:", ["Q3 minus Q1", "The maximum minus the minimum", "The median minus the mean", "Q1 plus Q3"], 0, "The interquartile range is Q3 minus Q1."),
 ("About what percent of the data lies between Q1 and Q3?", ["50 percent", "25 percent", "75 percent", "100 percent"], 0, "The box holds the middle half of the data."),
 ]),
 dict(t="2.2 Outliers and Standard Deviation", std="MA.912.DP",
 body="""An outlier is a value that lies far from the rest of the data. Outliers may be mistakes, or they may be real and important. We should never throw one away without asking why it is there. Isaiah 40:12 asks, Who hath measured the waters in the hollow of his hand, and meted out heaven with the span, and comprehended the dust of the earth in a measure, and weighed the mountains in scales, and the hills in a balance? God alone measures perfectly, and we measure carefully because we are not Him.

One rule uses the IQR. Compute the lower fence, Q1 minus 1.5 times the IQR, and the upper fence, Q3 plus 1.5 times the IQR. Any value beyond a fence is a suspected outlier. For the data in the last lesson, Q1 is 5, Q3 is 14 and the IQR is 9. The upper fence is 14 plus 13.5, which is 27.5. The lower fence is 5 minus 13.5, which is negative 8.5. No value lies beyond a fence, so there are no outliers. If a value of 40 were added, it would exceed 27.5 and be flagged.

The standard deviation measures how far data typically fall from the mean. To find it, follow these steps for the data 2, 4, 4, 4, 5, 5, 7 and 9. First find the mean, which is 40 divided by 8, or 5. Next find each deviation from the mean: negative 3, negative 1, negative 1, negative 1, 0, 0, 2 and 4. Square each deviation: 9, 1, 1, 1, 0, 0, 4 and 16. Add them to get 32. For a whole population, divide by the number of values, 8, to get 4, and take the square root to get a standard deviation of 2. For a sample, divide by one less than the number of values, 7, and take the square root of 32 divided by 7, which is about 2.14.

A small standard deviation means the data cluster near the mean, and a large one means they are spread out. The mean and standard deviation are not resistant, so use them for roughly symmetric data. For skewed data, report the median and IQR.

Your task: (1) Use the 1.5 times IQR rule to test for outliers. (2) Compute a standard deviation step by step. (3) Choose the best measures of center and spread for skewed data.""",
 script="""Welcome back. Listen, Isaiah 40:12 asks, Who hath measured the waters in the hollow of his hand? Only God measures perfectly. We measure carefully because we are not Him.

Now watch this. An outlier is a value far from the rest. Do not throw one away without asking why it is there. To test, find the fences. The lower fence is Q1 minus 1.5 times the IQR. The upper fence is Q3 plus 1.5 times the IQR. With Q1 equal to 5, Q3 equal to 14 and an IQR of 9, the upper fence is 27.5. A value of 40 would be flagged.

Look at standard deviation. It measures how far data typically fall from the mean. Take 2, 4, 4, 4, 5, 5, 7 and 9. The mean is 5. The deviations are negative 3, negative 1, negative 1, negative 1, 0, 0, 2 and 4. Square them to get 9, 1, 1, 1, 0, 0, 4 and 16. Add to get 32. Divide by 8 to get 4. The square root is 2. For a sample, divide by one less than the number of values.

A small standard deviation means the data cluster near the mean. A large one means they are spread out. For skewed data, report the median and the IQR instead.

Your task is to test for outliers, compute a standard deviation and choose the best measures for skewed data. Take the four question check.""" + CLOSE,
 quiz=[
 ("The upper fence for outliers is:", ["Q3 plus 1.5 times the IQR", "Q3 minus 1.5 times the IQR", "The maximum plus the IQR", "The mean plus the median"], 0, "Values beyond Q3 plus 1.5 times the IQR are suspected outliers."),
 ("For the data 2, 4, 4, 4, 5, 5, 7 and 9, the mean is:", ["5", "4", "6", "40"], 0, "The sum is 40, and 40 divided by 8 is 5."),
 ("The population standard deviation of that data set is:", ["2", "4", "5", "32"], 0, "The variance is 32 divided by 8, which is 4, and its square root is 2."),
 ("A small standard deviation means the data:", ["Cluster close to the mean", "Are widely spread out", "Contain no mean", "Must be skewed"], 0, "Small spread means values stay near the mean."),
 ]),
 dict(t="2.3 The Normal Distribution", std="MA.912.DP",
 body="""Many measurements in nature and in life follow a pattern shaped like a bell. Psalm 19:1 says, The heavens declare the glory of God; and the firmament sheweth his handywork. Order and pattern in creation invite us to study it. A normal distribution is a smooth, symmetric, bell shaped curve that is centered at its mean. Heights of adults, the weights of packages filled by a machine, and the errors in repeated measurements are often close to normal.

A normal curve has special properties. It is symmetric, so the mean and the median are equal and sit at the center. The curve is tallest at the mean and tapers off in both directions without ever touching the horizontal axis. The curve is described by two numbers, its mean and its standard deviation. A larger standard deviation makes the curve wider and flatter, and a smaller one makes it narrower and taller. The total area under the curve is 1, or 100 percent, and the area over an interval is the proportion of the data in that interval.

Example: suppose test scores are approximately normal with a mean of 70 and a standard deviation of 10. The score 70 is at the center. The curve is balanced, so half the students score below 70 and half score above it. A score of 80 is one standard deviation above the mean, and a score of 60 is one standard deviation below it.

A normal model is only an approximation. Not all data are normal. Income, for example, is usually skewed right. Before using a normal model, draw a histogram or dot plot and check that the shape is roughly symmetric, with a single peak and no strong outliers.

Your task: (1) List four properties of a normal curve. (2) Explain how the mean and the standard deviation change its position and shape. (3) Tell how you would check whether a data set is close to normal.""",
 script="""Welcome back. Listen, Psalm 19:1 says, The heavens declare the glory of God; and the firmament sheweth his handywork. Order and pattern in creation invite us to study it.

Now watch this. A normal distribution is a smooth, symmetric, bell shaped curve centered at its mean. Heights of adults and the errors in repeated measurements are often close to normal.

Look at its properties. It is symmetric, so the mean and median are equal and sit at the center. It is tallest at the mean and tapers off in both directions. Two numbers describe it, the mean and the standard deviation. A larger standard deviation makes the curve wider and flatter. A smaller one makes it narrower and taller. The total area under the curve is 100 percent, and the area over an interval is the proportion of data in that interval.

Here is an example. Suppose test scores are about normal with a mean of 70 and a standard deviation of 10. Half the students score below 70 and half above. A score of 80 is one standard deviation above the mean, and a score of 60 is one below.

But a normal model is only an approximation. Income is usually skewed right. Draw a histogram first and check for a single peak, symmetry and no strong outliers.

Your task is to list four properties of a normal curve, explain how the mean and standard deviation shape it and tell how to check for normality. Take the four question check.""" + CLOSE,
 quiz=[
 ("In a normal distribution the mean and the median are:", ["Equal", "Never equal", "Always zero", "Equal to the range"], 0, "A symmetric curve has the same mean and median."),
 ("A larger standard deviation makes a normal curve:", ["Wider and flatter", "Narrower and taller", "Skewed", "Disappear"], 0, "More spread means a wider, flatter bell."),
 ("The total area under a normal curve is:", ["1, or 100 percent", "0.5", "The mean", "The standard deviation"], 0, "The whole distribution has proportion 1."),
 ("Which data would most likely be skewed rather than normal?", ["Household incomes", "Heights of adult men", "Measurement errors", "Weights of filled packages"], 0, "Income is typically skewed right."),
 ]),
 dict(t="2.4 z Scores and the Empirical Rule", std="MA.912.DP",
 body="""To compare values from different distributions, we measure how many standard deviations a value is from its mean. This number is the z score. Job 38:5 asks, Who hath laid the measures thereof, if thou knowest? A z score is a way to measure a value against a standard.

The formula is that z equals the value minus the mean, divided by the standard deviation. A positive z means above the mean and a negative z means below it. On a test with a mean of 70 and a standard deviation of 10, a score of 85 has z equal to 15 divided by 10, which is 1.5. A score of 55 has a z of negative 1.5. A z of 0 is exactly the mean.

Z scores let us compare apples to apples. Suppose Maria scored 85 on a test with a mean of 70 and a standard deviation of 10. Jordan scored 68 on a different test with a mean of 60 and a standard deviation of 5. Maria's z is 1.5. Jordan's z is 8 divided by 5, which is 1.6. Jordan did slightly better compared with his own class, even though his raw score was lower.

The empirical rule, or 68, 95, 99.7 rule, applies to normal distributions. About 68 percent of the data fall within one standard deviation of the mean, about 95 percent fall within two, and about 99.7 percent fall within three. With a mean of 70 and a standard deviation of 10, about 68 percent of scores fall from 60 to 80, about 95 percent from 50 to 90, and about 99.7 percent from 40 to 100. The tails are symmetric. Since 95 percent lies within two standard deviations, 5 percent lies outside, so about 2.5 percent of scores are above 90.

A z score beyond 2 or negative 2 is unusual, and beyond 3 or negative 3 is very unusual.

Your task: (1) Compute a z score. (2) Compare two scores from different tests using z scores. (3) Use the empirical rule to find a percent of a normal distribution.""",
 script="""Welcome back. Listen, Job 38:5 asks, Who hath laid the measures thereof, if thou knowest? A z score is a way to measure a value against a standard.

Now watch this. The z score equals the value minus the mean, divided by the standard deviation. It tells how many standard deviations a value is from the mean. On a test with a mean of 70 and a standard deviation of 10, a score of 85 has a z of 1.5. A score of 55 has a z of negative 1.5.

Look at the comparison. Maria scored 85 where the mean was 70 and the standard deviation was 10, so her z is 1.5. Jordan scored 68 where the mean was 60 and the standard deviation was 5, so his z is 1.6. Jordan did slightly better compared with his own class.

Now the empirical rule. For a normal distribution, about 68 percent of the data fall within one standard deviation of the mean, about 95 percent within two and about 99.7 percent within three. With a mean of 70 and a standard deviation of 10, about 68 percent score from 60 to 80, about 95 percent from 50 to 90 and about 99.7 percent from 40 to 100. About 2.5 percent score above 90.

A z score beyond 2 or negative 2 is unusual. Beyond 3 is very unusual.

Your task is to compute a z score, compare two scores and use the empirical rule. Take the four question check.""" + CLOSE,
 quiz=[
 ("A score of 85 with a mean of 70 and a standard deviation of 10 has a z score of:", ["1.5", "15", "0.15", "8.5"], 0, "The z score is 15 divided by 10, which is 1.5."),
 ("About what percent of a normal distribution lies within two standard deviations of the mean?", ["95 percent", "68 percent", "99.7 percent", "50 percent"], 0, "The empirical rule says about 95 percent."),
 ("With a mean of 70 and a standard deviation of 10, about 68 percent of scores fall between:", ["60 and 80", "50 and 90", "40 and 100", "70 and 80"], 0, "One standard deviation each side gives 60 to 80."),
 ("A student has a z score of 0. This means the score:", ["Equals the mean", "Is zero points", "Is an outlier", "Is below average"], 0, "Zero standard deviations from the mean is the mean."),
 ]),
 ],
 assess=dict(t="Assessment 2: Distributions, Spread and the Normal Curve",
 prompt="""Write a report of at least 250 words on distributions and the normal curve. Use complete sentences, show every calculation and label each part. Psalm 19:1 says, The heavens declare the glory of God; and the firmament sheweth his handywork.

Part 1: For the data 3, 5, 6, 8, 9, 10, 12, 14, 15, 18 and 30, find the five number summary and the IQR, apply the 1.5 times IQR rule, and describe a box plot.
Part 2: For the data 4, 6, 6, 6, 8, 8, 10 and 12, find the mean and the population standard deviation step by step.
Part 3: Explain four properties of a normal curve and how to check whether a data set is close to normal.
Part 4: Test scores are approximately normal with a mean of 72 and a standard deviation of 8. Find the z score for 88 and for 64, and use the empirical rule to find the range containing about 95 percent of scores.
Part 5: Compare two students, one with 80 on a test with mean 70 and standard deviation 5, and one with 90 on a test with mean 75 and standard deviation 10, using z scores.""",
 rubric="""100 points. Part 1: 25 points. Part 2: 20 points. Part 3: 15 points. Part 4: 20 points. Part 5: 15 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 2: Patterns in Creation",
 prompt="""Write a post of at least 120 words that (1) names something you have noticed that follows a pattern, such as heights in a family, the growth of a plant or the time it takes to travel to church, (2) explains why a single average can hide important differences, (3) describes a situation where a z score or a standard deviation would help a leader decide fairly, and (4) connects your answer to Psalm 19:1 or Job 38:5. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why is it wrong to treat one unusual value as if it were typical? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("The first quartile Q1 is the median of the:", ["Lower half of the data", "Upper half of the data", "Entire data set", "Outliers"], 0, "Q1 splits the lower half."),
 ("If Q1 is 20 and Q3 is 50, the IQR is:", ["30", "70", "35", "20"], 0, "50 minus 20 equals 30."),
 ("A value beyond Q3 plus 1.5 times the IQR is a:", ["Suspected outlier", "Quartile", "Median", "Mode"], 0, "The fences identify suspected outliers."),
 ("The standard deviation of 2, 4, 4, 4, 5, 5, 7 and 9 (as a population) is:", ["2", "4", "5", "8"], 0, "The sum of squared deviations is 32, divided by 8 is 4, and its square root is 2."),
 ("A normal curve is:", ["Symmetric and bell shaped", "Skewed right", "Flat", "Always bimodal"], 0, "The normal curve is a symmetric bell."),
 ("Mean 60 and standard deviation 5. A score of 70 has a z score of:", ["2", "10", "0.5", "5"], 0, "10 divided by 5 equals 2."),
 ("About what percent of a normal distribution lies within one standard deviation of the mean?", ["68 percent", "95 percent", "99.7 percent", "34 percent"], 0, "The empirical rule gives 68 percent."),
 ("Which is best for skewed data?", ["The median and the IQR", "The mean and the standard deviation", "The mode only", "The z score"], 0, "Resistant measures suit skewed data."),
 ],
)
