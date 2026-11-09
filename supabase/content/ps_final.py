"""Probability and Statistics final module: final assessment (position 7) and final exam (quiz position 31)."""

FINAL_ASSESS = dict(t="Final Assessment: Statistical Investigation Report",
 prompt="""Complete a statistical investigation and write a report of at least 600 words. Choose a question that can be answered with data from at least 30 people or items, such as how many hours students sleep, how long families travel to church, or how many verses students memorize in a month. Do not collect private or sensitive information, and ask a parent, guardian or teacher for permission before surveying other people. Write complete sentences, show every calculation and label each part. Proverbs 20:10 says, Divers weights, and divers measures, both of them are alike abomination to the LORD.

Part 1: The Question and the Plan. State your question, the population and the sample, and explain how you chose a sample and what bias you worked to avoid.
Part 2: The Data. Present your data in a table and a graph (a dot plot, histogram or bar graph) and describe the shape, center and spread.
Part 3: Summary Statistics. Find the mean, median, five number summary, IQR and standard deviation, test for outliers, and explain which measures of center and spread best fit your data.
Part 4: The Normal Curve. Tell whether your data are close to normal, and use the empirical rule or a z score to describe one value.
Part 5: Probability. Use your data to find one probability, one conditional probability from a two way table, and one probability using counting or the binomial model.
Part 6: Relationships. If you collected two quantitative variables, make a scatter plot, find or estimate the line of best fit and the correlation, and interpret them. Otherwise make a two way table from two categorical variables and compare conditional percents. Explain why you cannot claim cause.
Part 7: Inference. Find a 95 percent confidence interval for a proportion from your data and interpret it, and state the margin of error.
Part 8: Integrity and Application. List the limits of your study and explain how Exodus 20:16 and Proverbs 14:15 guide the honest use of statistics. Describe how you would use statistics in a future calling.""",
 rubric="""100 points. Part 1, question and plan: 10 points. Part 2, data and graph: 10 points. Part 3, summary statistics: 15 points. Part 4, normal curve: 10 points. Part 5, probability: 15 points. Part 6, relationships: 15 points. Part 7, inference: 10 points. Part 8, integrity and application: 10 points. Grammar, conventions and respectful tone: 5 points. A score of 70 or above is passing."""
)

FINAL_EXAM = [
 ("A number that describes a sample is called a:", ["Statistic", "Parameter", "Population", "Variable"], 0, "A statistic describes a sample."),
 ("A poll in which people choose whether to respond is a:", ["Voluntary response sample that is often biased", "Simple random sample", "Stratified sample", "Experiment"], 0, "Self selection attracts strong opinions."),
 ("Which measure of center is resistant to outliers?", ["The median", "The mean", "The range", "The standard deviation"], 0, "The median is not pulled by extreme values."),
 ("The quick margin of error for a random sample of 100 is about:", ["10 percentage points", "1 percentage point", "50 percentage points", "5 percentage points"], 0, "1 divided by the square root of 100 equals 0.10."),
 ("If Q1 is 12 and Q3 is 30, the IQR is:", ["18", "42", "21", "12"], 0, "30 minus 12 equals 18."),
 ("In a normal distribution, about what percent of values lie within two standard deviations of the mean?", ["95 percent", "68 percent", "99.7 percent", "50 percent"], 0, "That is the empirical rule."),
 ("A score of 90 on a test with mean 80 and standard deviation 5 has a z score of:", ["2", "10", "0.5", "5"], 0, "10 divided by 5 equals 2."),
 ("The probability of a sum of 7 when rolling two fair dice is:", ["1/6", "1/12", "7/36", "1/7"], 0, "Six of 36 outcomes."),
 ("The probability of at least one head in three fair coin tosses is:", ["7/8", "1/8", "3/8", "1/2"], 0, "One minus the chance of no heads."),
 ("Independent events with probabilities 1/2 and 1/5 both occur with probability:", ["1/10", "7/10", "3/10", "2/5"], 0, "Multiply: 1/2 times 1/5 equals 1/10."),
 ("The number of ways to choose 2 people from 6 when order does not matter is:", ["15", "30", "12", "36"], 0, "6 times 5 divided by 2 equals 15."),
 ("A random variable equals 10 with probability 0.2 and 0 with probability 0.8. Its expected value is:", ["2", "10", "8", "5"], 0, "10 times 0.2 plus 0 times 0.8 equals 2."),
 ("The mean number of successes in 20 trials with p equal to 0.5 is:", ["10", "5", "20", "0.5"], 0, "n times p equals 20 times 0.5."),
 ("For the line y hat equals 4 plus 3 times x, the predicted y when x is 2 is:", ["10", "9", "8", "14"], 0, "4 plus 3 times 2 equals 10."),
 ("Which study design can best show that a treatment causes an effect?", ["A randomized experiment", "A strong correlation", "A convenience survey", "A scatter plot"], 0, "Random assignment controls lurking variables."),
]
