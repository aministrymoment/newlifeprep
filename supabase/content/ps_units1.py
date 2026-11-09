"""Probability and Statistics, Unit 1: Data and How We Describe It. Florida B.E.S.T. Data Analysis and Probability strand (MA.912.DP) cited at strand level; recheck exact benchmark codes at CPALMS."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."

UNIT1 = dict(
 title="Unit 1: Data and How We Describe It",
 std="MA.912.DP",
 topics=[
 dict(t="1.1 What Statistics Is and Types of Data", std="MA.912.DP",
 body="""Statistics is the science of collecting, organizing, analyzing and interpreting data so that we can make wise decisions. Data are facts and numbers gathered to answer a question. The Bible records some of the earliest counting of a people. In Numbers 1:2 the LORD told Moses, Take ye the sum of all the congregation of the children of Israel, after their families, by the house of their fathers, with the number of their names. A count like this is a form of data collection, and leaders still count attendance, giving and needs today so that they can serve well.

Every study begins with a question and a group to study. The population is the entire group we want to know about, such as every student in a school. A sample is a smaller part of the population that we actually measure. A parameter is a number that describes a population, and a statistic is a number that describes a sample. Each person or thing we measure is an individual, and each characteristic we record about it is a variable.

Variables come in two main types. A categorical variable places individuals into groups or categories, such as favorite hymn, grade level or eye color. A quantitative variable is a number that can be counted or measured, such as height, age or the number of songs a choir sings. Quantitative variables are discrete when they are counted in whole numbers, such as the number of siblings, and continuous when they can take any value in an interval, such as height or time. Not every number is quantitative. A zip code or a jersey number is only a label, so it is categorical.

Example: a pastor surveys 50 members of a church of 400 and records each person's age, favorite service day and number of children. The population is the 400 members and the sample is the 50. Age is continuous, the number of children is discrete, and favorite service day is categorical.

Your task: (1) Define statistics, population and sample. (2) Tell the difference between a parameter and a statistic. (3) Classify three variables as categorical or quantitative.""",
 script="""Welcome to Probability and Statistics. I am Dr. Alex L. Jenkins Sr. Listen, God Himself told Moses to take the sum of the congregation in Numbers 1:2, so counting people carefully is nothing new. In this course we learn how to gather numbers, read them wisely and tell the truth with them.

Now watch this. Statistics is the science of collecting, organizing, analyzing and interpreting data so that we can make wise decisions. The population is the whole group we want to know about. A sample is the smaller part we actually measure. A number that describes a population is a parameter. A number that describes a sample is a statistic.

Look at the two types of variables. A categorical variable puts people into groups, like favorite hymn or grade level. A quantitative variable is a real number you can count or measure, like height, age or the number of songs a choir sings. A zip code looks like a number, but it is only a label, so it is categorical.

Here is an example. A pastor surveys 50 members of a church of 400. The population is the 400 members. The sample is the 50. Age is continuous. The number of children is discrete. Favorite service day is categorical.

Your task is to define statistics, population and sample, tell a parameter from a statistic, and classify three variables. Take the four question check.""" + CLOSE,
 quiz=[
 ("The entire group a study wants to know about is the:", ["Population", "Sample", "Statistic", "Variable"], 0, "The population is the whole group of interest."),
 ("A number that describes a sample is called a:", ["Statistic", "Parameter", "Population", "Category"], 0, "A statistic describes a sample; a parameter describes a population."),
 ("Which variable is categorical?", ["Favorite hymn", "Height in inches", "Number of siblings", "Time in seconds"], 0, "Favorite hymn places people in groups."),
 ("The number of children in a family is what kind of variable?", ["Discrete quantitative", "Continuous quantitative", "Categorical", "A parameter"], 0, "It is counted in whole numbers, so it is discrete."),
 ]),
 dict(t="1.2 Sampling and Collecting Data Honestly", std="MA.912.DP",
 body="""Because it is usually impossible to ask everyone, statisticians study samples. A good sample represents the population. A bad sample leads to false conclusions. Proverbs 18:13 warns, He that answereth a matter before he heareth it, it is folly and shame unto him, and Proverbs 18:17 adds, He that is first in his own cause seemeth just; but his neighbour cometh and searcheth him. A fair study listens to all sides.

A simple random sample gives every individual an equal chance of being chosen, like drawing names from a hat. A systematic sample picks every kth individual from a list. A stratified sample divides the population into groups, such as grade levels, and takes a random sample from each group. A cluster sample randomly chooses whole groups, such as entire classrooms, and surveys everyone in them. A convenience sample uses whoever is easy to reach, and it is often biased.

Bias is a systematic error that favors some outcomes. Selection bias happens when some people are more likely to be chosen, such as asking only the choir about the best music. A voluntary response sample, where people choose to respond, usually attracts those with strong opinions. Undercoverage happens when part of the population is left out. Wording bias happens when a question leads the answer. Compare: Do you support the wonderful new youth center? and What is your opinion of the proposed youth center? The first question pushes people toward yes.

There are three main ways to gather data. In a sample survey we ask questions of a sample. In an observational study we watch and record without changing anything. In an experiment we apply a treatment to see its effect. In a well designed experiment, subjects are randomly assigned to groups, and there is a control group that does not receive the treatment. Only experiments can show cause and effect.

Your task: (1) Name four sampling methods. (2) Explain three kinds of bias. (3) Rewrite a leading survey question so it is fair.""",
 script="""Welcome back. Listen, Proverbs 18:13 says, He that answereth a matter before he heareth it, it is folly and shame unto him. That is a rule for good statistics too. Hear everyone before you decide.

Now watch this. A simple random sample gives everyone an equal chance of being chosen, like names drawn from a hat. A systematic sample takes every kth person on a list. A stratified sample splits the population into groups, like grade levels, and samples from each group. A cluster sample chooses whole groups, like entire classrooms. A convenience sample uses whoever is easy to reach, and it is often biased.

Look at bias. Selection bias means some people are more likely to be chosen. A voluntary response sample draws people with strong opinions. Undercoverage leaves part of the population out. Wording bias happens when the question leads the answer. Do you support the wonderful new youth center is a leading question. What is your opinion of the proposed youth center is fair.

There are three ways to gather data. A survey asks questions. An observational study watches without changing anything. An experiment applies a treatment, with random assignment and a control group. Only a well designed experiment can show cause and effect.

Your task is to name four sampling methods, explain three kinds of bias and rewrite a leading question. Take the four question check.""" + CLOSE,
 quiz=[
 ("A sample in which every individual has an equal chance of being chosen is a:", ["Simple random sample", "Convenience sample", "Voluntary response sample", "Biased sample"], 0, "Equal chance defines a simple random sample."),
 ("Asking only the choir which music the whole church prefers is an example of:", ["Selection bias", "A control group", "A random sample", "A cluster sample"], 0, "The choir does not represent the whole church."),
 ("Which type of study can show cause and effect?", ["A well designed experiment", "A convenience survey", "A voluntary response poll", "An observational study"], 0, "Random assignment and a control group allow cause and effect conclusions."),
 ("Dividing students by grade level and sampling randomly from each grade is:", ["A stratified sample", "A cluster sample", "A systematic sample", "A convenience sample"], 0, "Stratified sampling samples from each group."),
 ]),
 dict(t="1.3 Displaying Data: Tables and Graphs", std="MA.912.DP",
 body="""Raw numbers are hard to read until we organize them. Psalm 90:12 prays, So teach us to number our days, that we may apply our hearts unto wisdom. Good graphs help us number our days well by showing patterns we could not see in a list.

A frequency table lists each value or category and how many times it occurs. The relative frequency is the frequency divided by the total, often written as a percent. For example, if 40 students are asked their favorite season and 10 say summer, the frequency is 10 and the relative frequency is 10 divided by 40, which is 0.25 or 25 percent.

For categorical data, we use a bar graph, where the height of each bar shows the count in a category, and the bars do not touch. A pie chart shows parts of a whole, and the percents add to 100. For quantitative data, a dot plot places a dot above each value on a number line. A stem and leaf plot splits each number into a stem and a leaf; for example, the scores 72, 75, 78 and 81 are shown as 7 with leaves 2, 5 and 8, and 8 with leaf 1. A histogram groups quantitative data into equal width intervals called bins, and the bars touch because the data are continuous.

When you describe a graph of quantitative data, talk about its shape, center and spread, and any unusual features. A distribution is symmetric if the left and right sides are mirror images. It is skewed right if the tail stretches toward the larger values, and skewed left if the tail stretches toward the smaller values. A peak is a mode, and a distribution with two peaks is bimodal. Gaps and outliers deserve attention.

Example: quiz scores of 5, 6, 6, 7, 7, 7, 8, 8, 9 make a dot plot with the tallest stack at 7 and a nearly symmetric shape.

Your task: (1) Find the relative frequency of a category. (2) Choose a bar graph or a histogram for given data and explain why. (3) Describe the shape of a distribution using the words symmetric, skewed, mode and outlier.""",
 script="""Welcome back. Listen, Psalm 90:12 says, So teach us to number our days, that we may apply our hearts unto wisdom. A good graph helps us see patterns that a list of numbers hides.

Now watch this. A frequency table lists each value and how many times it occurs. The relative frequency is the frequency divided by the total. If 10 of 40 students pick summer, the relative frequency is 0.25, or 25 percent.

Look at the graphs. For categories, use a bar graph with bars that do not touch, or a pie chart whose parts add to 100 percent. For numbers, use a dot plot, a stem and leaf plot or a histogram. A histogram groups data into equal width bins, and its bars touch because the data are continuous.

When you describe a graph, talk about shape, center and spread. A distribution is symmetric when the two sides are mirror images. It is skewed right when the tail stretches toward larger values, and skewed left when the tail stretches toward smaller values. A peak is a mode. Two peaks make it bimodal. Always look for gaps and outliers.

Example. Scores of 5, 6, 6, 7, 7, 7, 8, 8, 9 stack tallest at 7 and look nearly symmetric.

Your task is to find a relative frequency, choose the right graph and describe a shape. Take the four question check.""" + CLOSE,
 quiz=[
 ("Twelve of 48 students chose basketball. The relative frequency is:", ["25 percent", "12 percent", "48 percent", "4 percent"], 0, "12 divided by 48 equals 0.25, or 25 percent."),
 ("Which graph is best for the favorite hymn of each member of a choir?", ["A bar graph", "A histogram", "A scatter plot", "A stem and leaf plot"], 0, "Favorite hymn is categorical, so use a bar graph."),
 ("A distribution with a long tail toward the larger values is:", ["Skewed right", "Skewed left", "Symmetric", "Bimodal"], 0, "The tail side names the skew."),
 ("In a histogram, the bars touch because the data are:", ["Continuous quantitative", "Categorical", "Labels", "Discrete categories"], 0, "Bins cover an unbroken range of values."),
 ]),
 dict(t="1.4 Measures of Center and Spread", std="MA.912.DP",
 body="""A single number can summarize a whole data set. Proverbs 11:1 says, A false balance is abomination to the LORD: but a just weight is his delight. A fair summary uses a just weight, which means it does not hide the truth.

The mean is the average. Add all the values and divide by how many there are. For the data 3, 5, 6, 7 and 9, the sum is 30, and 30 divided by 5 is 6, so the mean is 6. The median is the middle value when the data are in order. If there is an even number of values, the median is the mean of the two middle values. For 3, 5, 6, 7 and 9 the median is also 6. The mode is the value that occurs most often.

The mean and the median can tell different stories. Change the 9 to 39. The data 3, 5, 6, 7 and 39 have a sum of 60, so the mean is 12, but the median is still 6. The mean is pulled toward extreme values, so we say it is not resistant. The median is resistant. For skewed data or data with outliers, the median is usually a better description of a typical value. This matters in real life. A few very high salaries can raise the mean income of a town so that it looks richer than most families really are.

Spread tells how far apart the data are. The range is the maximum minus the minimum. For 3, 5, 6, 7 and 39, the range is 39 minus 3, which is 36. The range uses only two values and is easily distorted. Two data sets can have the same mean but very different spreads. Scores of 78, 80 and 82 and scores of 60, 80 and 100 both have a mean of 80, but the second set is far more spread out.

Your task: (1) Find the mean, median, mode and range of a small data set. (2) Explain why the median is resistant and the mean is not. (3) Tell when the median is the better summary.""",
 script="""Welcome back. Listen, Proverbs 11:1 says, A false balance is abomination to the LORD: but a just weight is his delight. When we summarize data, we must use a just weight.

Now watch this. The mean is the average. Add the values and divide by how many there are. For 3, 5, 6, 7 and 9, the sum is 30, and 30 divided by 5 is 6. The median is the middle value in order, also 6. The mode is the value that occurs most often.

Look at what happens with an extreme value. Change the 9 to 39. Now the sum is 60, so the mean is 12, but the median is still 6. The mean is pulled toward extremes. The median is resistant. For skewed data or data with outliers, the median usually describes a typical value better. A few huge salaries can make a town look richer than most families are.

Spread tells how far apart the data are. The range is the maximum minus the minimum. For 3, 5, 6, 7 and 39 the range is 36. Scores of 78, 80 and 82 and scores of 60, 80 and 100 both have a mean of 80, but the second set is far more spread out.

Your task is to find the mean, median, mode and range, explain resistance and tell when the median is better. Take the four question check.""" + CLOSE,
 quiz=[
 ("The mean of 4, 6, 8 and 10 is:", ["7", "6", "8", "28"], 0, "The sum is 28, and 28 divided by 4 is 7."),
 ("Which measure is resistant to outliers?", ["The median", "The mean", "The sum", "The range"], 0, "The median is not pulled by extreme values."),
 ("The range of 3, 5, 6, 7 and 39 is:", ["36", "39", "12", "6"], 0, "39 minus 3 equals 36."),
 ("A town has a few extremely high incomes. Which summary best shows a typical family?", ["The median", "The mean", "The maximum", "The range"], 0, "The median is not distorted by a few very high values."),
 ]),
 ],
 assess=dict(t="Assessment 1: Data and How We Describe It",
 prompt="""Write a report of at least 250 words on describing data. Use complete sentences, show your work and label each part. Psalm 90:12 says, So teach us to number our days, that we may apply our hearts unto wisdom.

Part 1: Define population, sample, parameter and statistic, and give one example of each from a church or school.
Part 2: Name two sampling methods and two kinds of bias. Rewrite one leading survey question so that it is fair.
Part 3: Make a frequency table, relative frequencies and either a dot plot or a histogram for ten numbers you collect, such as the number of minutes ten family members read Scripture in a week. Describe the shape.
Part 4: Find the mean, median, mode and range of your ten numbers. Add one extreme value and show what happens to the mean and the median.
Part 5: Explain, using Proverbs 11:1, why honest summaries matter.""",
 rubric="""100 points. Part 1: 15 points. Part 2: 20 points. Part 3: 25 points. Part 4: 25 points. Part 5: 10 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 1: Counting with Care",
 prompt="""Write a post of at least 120 words that (1) tells about a time a survey, poll or count affected a decision at home, school or church, (2) explains how a poor sample or a leading question could give a false picture, (3) describes a question you would like to answer with data and how you would collect a fair sample, and (4) connects your answer to Proverbs 18:13 or Numbers 1:2. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why should a leader want honest numbers even when they are not what he hoped to see? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("A pastor surveys 60 of 500 members. The 500 members are the:", ["Population", "Sample", "Statistic", "Variable"], 0, "The whole group is the population."),
 ("Zip codes are what type of variable?", ["Categorical", "Continuous", "Discrete quantitative", "A parameter"], 0, "A zip code is only a label."),
 ("A survey that only counts people who choose to call in is a:", ["Voluntary response sample", "Simple random sample", "Stratified sample", "Cluster sample"], 0, "Self selected responses are usually biased."),
 ("A control group in an experiment:", ["Does not receive the treatment", "Receives the treatment twice", "Chooses its own treatment", "Is never measured"], 0, "The control group provides a comparison."),
 ("Fifteen of 60 students chose pizza. The relative frequency is:", ["25 percent", "15 percent", "60 percent", "4 percent"], 0, "15 divided by 60 equals 0.25."),
 ("The mean of 2, 4, 6, 8 and 10 is:", ["6", "5", "8", "30"], 0, "The sum is 30, and 30 divided by 5 is 6."),
 ("For 3, 5, 6, 7 and 39 the median is:", ["6", "12", "39", "36"], 0, "The middle value is 6."),
 ("A distribution with its tail stretching toward smaller values is:", ["Skewed left", "Skewed right", "Symmetric", "Uniform"], 0, "The tail side names the skew."),
 ],
)
