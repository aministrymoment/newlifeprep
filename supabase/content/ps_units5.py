"""Probability and Statistics, Unit 5: Relationships Between Variables. Florida B.E.S.T. Data Analysis and Probability strand (MA.912.DP) cited at strand level; recheck at CPALMS."""
from ps_units1 import CLOSE

UNIT5 = dict(
 title="Unit 5: Relationships Between Variables",
 std="MA.912.DP",
 topics=[
 dict(t="5.1 Scatter Plots and Correlation", std="MA.912.DP",
 body="""So far we have studied one variable at a time. Often we want to know whether two quantitative variables are related. Proverbs 27:17 says, Iron sharpeneth iron; so a man sharpeneth the countenance of his friend. Things in our world are linked, and statistics gives us tools to describe those links.

A scatter plot graphs pairs of values as points. The explanatory variable, usually called x, is placed on the horizontal axis. It is the variable we think helps explain or predict the other. The response variable, usually called y, is placed on the vertical axis. For example, a youth leader records the hours a student spends on Scripture study each week and the number of verses the student memorizes. The five students give the pairs (1, 2), (2, 4), (3, 5), (4, 4) and (5, 5).

To describe a scatter plot, talk about direction, form, strength and unusual points. Direction is positive if the points rise from left to right and negative if they fall. Form is linear if the points follow a straight line pattern, or curved otherwise. Strength tells how closely the points follow the pattern. Outliers are points far from the pattern.

The correlation coefficient, written r, measures the strength and direction of a linear relationship. It is always between negative 1 and 1. A value near 1 shows a strong positive linear relationship, a value near negative 1 shows a strong negative linear relationship, and a value near 0 shows little or no linear relationship. For the five students, r is about 0.77, a fairly strong positive relationship. Correlation has no units, does not change if we switch x and y, and measures only straight line patterns. A strong curved pattern can have r near 0. Outliers can pull r up or down a great deal.

The square of the correlation, r squared, tells the fraction of the variation in y that is accounted for by the straight line relationship with x. Here r squared is about 0.6, so about 60 percent of the variation in memorized verses is accounted for by study hours.

Your task: (1) Identify the explanatory and response variables in a situation. (2) Describe the direction, form and strength of a scatter plot. (3) Explain what r equal to 0.77 means.""",
 script="""Welcome back. Listen, Proverbs 27:17 says, Iron sharpeneth iron; so a man sharpeneth the countenance of his friend. Things in our world are linked, and statistics gives us tools to describe those links.

Now watch this. A scatter plot graphs pairs of values as points. The explanatory variable, x, goes on the horizontal axis. The response variable, y, goes on the vertical axis. A youth leader records the hours five students study Scripture each week and the number of verses they memorize. The pairs are 1 and 2, 2 and 4, 3 and 5, 4 and 4, and 5 and 5.

Look at how to describe a scatter plot. Direction is positive if the points rise from left to right and negative if they fall. Form is linear or curved. Strength tells how closely the points follow the pattern. And watch for outliers.

The correlation coefficient r measures the strength and direction of a linear relationship. It is between negative 1 and 1. Near 1 is a strong positive relationship. Near negative 1 is a strong negative relationship. Near 0 is little or no linear relationship. For our five students, r is about 0.77. Correlation has no units and measures only straight line patterns. R squared is about 0.6, so about 60 percent of the variation in memorized verses is accounted for by study hours.

Your task is to identify the variables, describe a scatter plot and explain r. Take the four question check.""" + CLOSE,
 quiz=[
 ("In a scatter plot, the response variable goes on the:", ["Vertical axis", "Horizontal axis", "Either axis randomly", "Neither axis"], 0, "The response variable y is on the vertical axis."),
 ("A correlation of negative 0.9 indicates:", ["A strong negative linear relationship", "A weak positive relationship", "No relationship", "A perfect positive relationship"], 0, "The sign shows direction and the size shows strength."),
 ("The correlation coefficient r must lie between:", ["Negative 1 and 1", "0 and 100", "0 and 10", "Negative 100 and 100"], 0, "The value of r is always from negative 1 to 1."),
 ("If r equals 0.77, then r squared is about 0.6. This means about 60 percent of the variation in y is:", ["Accounted for by the linear relationship with x", "Caused by x", "Due to outliers", "Random noise"], 0, "R squared measures the share of variation accounted for by the line."),
 ]),
 dict(t="5.2 The Line of Best Fit", std="MA.912.DP",
 body="""When a scatter plot looks linear, we can draw a line through it to describe the trend and make predictions. Proverbs 6:6 says, Go to the ant, thou sluggard; consider her ways, and be wise. Wisdom begins with careful observation of patterns, and a line of best fit is a way to put an observed pattern into a rule.

The least squares regression line is the line that makes the sum of the squared vertical distances from the points to the line as small as possible. It has the form y hat equals a plus b times x, where y hat is the predicted value, b is the slope and a is the intercept. For the five students from the last lesson, the line is y hat equals 2.2 plus 0.6 times x.

The slope is the predicted change in y for each increase of 1 in x. The slope 0.6 means that for each additional hour of study, we predict about 0.6 more verses memorized. The intercept is the predicted value of y when x is 0. The intercept 2.2 says that a student who studies zero hours is predicted to memorize 2.2 verses, which may or may not make sense in context. Always interpret slope and intercept using the units of the variables.

To predict, substitute x. For 4 hours, y hat equals 2.2 plus 0.6 times 4, which is 4.6 verses. A residual is the actual value minus the predicted value. The student who studied 4 hours actually memorized 4, so the residual is 4 minus 4.6, or negative 0.6. A student who studied 2 hours memorized 4, and the predicted value was 3.4, so the residual is positive 0.6. A positive residual means the point is above the line. The residuals from a least squares line add to zero. A residual plot with no pattern shows that a line is a good model.

Predicting inside the range of the data is interpolation and is usually reliable. Predicting far outside the range is extrapolation and can be foolish. The line predicts 26.2 verses for 40 hours of study in a week, which is impossible because a week has only 168 hours and a student must also eat, sleep and serve.

Your task: (1) Interpret the slope and intercept of a regression line. (2) Make a prediction and compute a residual. (3) Explain why extrapolation is risky.""",
 script="""Welcome back. Listen, Proverbs 6:6 says, Go to the ant, thou sluggard; consider her ways, and be wise. Wisdom begins with careful observation of patterns.

Now watch this. The least squares regression line is the line that makes the sum of the squared vertical distances from the points as small as possible. It has the form y hat equals a plus b times x. For our five students the line is y hat equals 2.2 plus 0.6 times x.

Look at what the numbers mean. The slope 0.6 means that for each additional hour of study we predict about 0.6 more verses memorized. The intercept 2.2 is the predicted value when x is 0. Always say what they mean in the units of the problem.

To predict, substitute x. For 4 hours, y hat is 2.2 plus 0.6 times 4, which is 4.6 verses. A residual is the actual value minus the predicted value. That student memorized 4, so the residual is negative 0.6. A student who studied 2 hours memorized 4, and the prediction was 3.4, so the residual is positive 0.6.

Predicting inside the range of the data is interpolation. Predicting far outside the range is extrapolation and can be foolish. The line predicts 26.2 verses for 40 hours of study in one week, but a week has only 168 hours and a student must also eat, sleep and serve.

Your task is to interpret slope and intercept, make a prediction and compute a residual, and explain the risk of extrapolation. Take the four question check.""" + CLOSE,
 quiz=[
 ("In the line y hat equals 2.2 plus 0.6 times x, the slope is:", ["0.6", "2.2", "2.8", "1"], 0, "The coefficient of x is the slope."),
 ("The predicted value for x equal to 4 is:", ["4.6", "2.8", "3.4", "5"], 0, "2.2 plus 0.6 times 4 equals 4.6."),
 ("A residual is:", ["The actual value minus the predicted value", "The predicted value minus the mean", "The slope times x", "The correlation squared"], 0, "Residual equals actual minus predicted."),
 ("Predicting far outside the range of the data is called:", ["Extrapolation", "Interpolation", "Correlation", "Sampling"], 0, "Extrapolation goes beyond the observed data and can be unreliable."),
 ]),
 dict(t="5.3 Two Way Tables and Association", std="MA.912.DP",
 body="""Not every pair of variables is quantitative. We can also study how two categorical variables relate. Matthew 7:16 says, Ye shall know them by their fruits. Evidence is found by looking at results, and a two way table helps us look at the results for different groups.

A two way table shows counts for two categorical variables at the same time. Suppose 200 students were asked whether they use a written study plan and whether they earned a B or higher on their last major exam. The counts are as follows. Of the 120 students who use a plan, 96 earned a B or higher and 24 earned below a B. Of the 80 students who do not use a plan, 40 earned a B or higher and 40 earned below a B. The column totals are 136 students with a B or higher and 64 students with below a B.

The joint relative frequency is a count divided by the grand total. The share of all students who both use a plan and earned a B or higher is 96 divided by 200, which is 0.48 or 48 percent. The marginal relative frequency uses a row or column total. The share of all students who earned a B or higher is 136 divided by 200, which is 68 percent.

To compare groups fairly, use conditional relative frequencies. Among students who use a plan, 96 divided by 120 is 80 percent earned a B or higher. Among students who do not use a plan, 40 divided by 80 is 50 percent. A segmented bar graph shows these two percents side by side. Because the percents differ, there is an association between using a plan and the exam result. If the percents were equal, we would say there is no association, and the variables would be independent.

An association describes a pattern in the data. It does not prove that the plan caused the better grades. Perhaps students who use plans are also more motivated. We study that issue in the next lesson.

Your task: (1) Find joint, marginal and conditional relative frequencies from a two way table. (2) Decide whether there is an association. (3) Explain why an association is not proof of cause.""",
 script="""Welcome back. Listen, Matthew 7:16 says, Ye shall know them by their fruits. Evidence is found by looking at results, and a two way table helps us look at results for different groups.

Now watch this. Suppose 200 students are asked whether they use a written study plan and whether they earned a B or higher on the last major exam. Of the 120 who use a plan, 96 earned a B or higher and 24 earned below a B. Of the 80 who do not use a plan, 40 earned a B or higher and 40 earned below a B. In all, 136 earned a B or higher and 64 earned below a B.

Look at the relative frequencies. The joint relative frequency of using a plan and earning a B or higher is 96 out of 200, which is 48 percent. The marginal relative frequency of earning a B or higher is 136 out of 200, which is 68 percent.

To compare groups fairly, use conditional relative frequencies. Among plan users, 96 out of 120 is 80 percent earned a B or higher. Among students with no plan, 40 out of 80 is 50 percent. The percents differ, so there is an association.

But an association does not prove cause. Perhaps students who use plans are also more motivated.

Your task is to find joint, marginal and conditional relative frequencies, decide on association and explain why association is not proof of cause. Take the four question check.""" + CLOSE,
 quiz=[
 ("In the study plan table, the number of students who use a plan and earned a B or higher is:", ["96", "136", "120", "40"], 0, "The cell for plan and B or higher holds 96."),
 ("Among students who use a plan, the percent who earned a B or higher is:", ["80 percent", "48 percent", "68 percent", "50 percent"], 0, "96 divided by 120 equals 0.80."),
 ("Among students who do not use a plan, the percent who earned a B or higher is:", ["50 percent", "40 percent", "80 percent", "20 percent"], 0, "40 divided by 80 equals 0.50."),
 ("Different conditional percents for the two groups suggest:", ["An association between the variables", "That the variables are independent", "That the data are wrong", "Proof of cause"], 0, "Unequal conditional percents indicate an association."),
 ]),
 dict(t="5.4 Correlation Is Not Causation", std="MA.912.DP",
 body="""One of the most important lessons in statistics is that two things can be linked without one causing the other. In John 9:2 and 3, the disciples saw a man blind from birth and asked, Master, who did sin, this man, or his parents, that he was born blind? Jesus answered, Neither hath this man sinned, nor his parents: but that the works of God should be made manifest in him. The disciples assumed a cause they could not know. Statistics teaches us to slow down before we name a cause.

Causation means that a change in one variable produces a change in the other. Correlation only means they move together. A famous example is that ice cream sales and drowning accidents both rise in the summer. Eating ice cream does not cause drowning. A lurking variable, hot weather, affects both. When a lurking variable is mixed with the explanatory variable so that their effects cannot be separated, we say the two are confounded.

There are three common explanations for a strong correlation. X may cause Y. Y may cause X, which is called reverse causation. Or a lurking variable may cause both. For example, students who attend tutoring have lower grades. Tutoring does not lower grades. Students with lower grades are more likely to get tutoring.

How can we establish cause? The best way is a well designed experiment, which randomly assigns subjects to treatment and control groups, so that lurking variables are balanced between them. When an experiment is not possible or ethical, evidence from many studies can build a strong case. Such evidence includes a strong association, the same result across many studies and settings, a plausible mechanism, and a response that grows with the dose. Even then, we speak carefully.

When you read a headline that says a food, a habit or a program is linked to a result, ask: Was it an experiment or an observational study? What else could explain the link? How large and how varied was the sample? Careful thinkers avoid hasty claims.

Your task: (1) Define lurking variable and confounding. (2) Give an example of reverse causation. (3) Tell why a randomized experiment can show cause.""",
 script="""Welcome back. Listen, in John 9:2 and 3 the disciples saw a man blind from birth and asked, Master, who did sin, this man, or his parents? Jesus answered, Neither hath this man sinned, nor his parents. The disciples assumed a cause they could not know. Statistics teaches us to slow down before we name a cause.

Now watch this. Causation means a change in one variable produces a change in the other. Correlation only means they move together. Ice cream sales and drowning accidents both rise in the summer, but ice cream does not cause drowning. Hot weather, a lurking variable, affects both. When a lurking variable is mixed with the explanatory variable so we cannot separate their effects, we say they are confounded.

Look at three explanations for a strong correlation. X causes Y. Y causes X, which is called reverse causation. Or a lurking variable causes both. Students who attend tutoring have lower grades, but tutoring does not lower grades. Students with lower grades are more likely to get tutoring.

To establish cause, the best way is a well designed experiment with random assignment and a control group. When that is not possible, a strong case needs a strong association, consistent results across many studies, a plausible mechanism and a response that grows with the dose.

When you read a headline, ask what else could explain the link. Careful thinkers avoid hasty claims.

Your task is to define lurking variable, give an example of reverse causation and explain why a randomized experiment can show cause. Take the four question check.""" + CLOSE,
 quiz=[
 ("A variable that affects both the explanatory and response variables is a:", ["Lurking variable", "Residual", "Parameter", "Control group"], 0, "A lurking variable can create a false appearance of cause."),
 ("Ice cream sales and drownings both rise in summer. The best explanation is:", ["Hot weather affects both", "Ice cream causes drowning", "Drowning causes ice cream sales", "It is only a coincidence in every year"], 0, "A lurking variable, summer heat, explains the link."),
 ("Which study design can best show cause and effect?", ["A randomized experiment", "A voluntary online poll", "A convenience sample", "A scatter plot"], 0, "Random assignment balances lurking variables."),
 ("Students who get tutoring tend to have lower grades. This is most likely an example of:", ["Reverse causation", "Tutoring lowering grades", "A perfect correlation", "Random chance only"], 0, "Lower grades lead students to seek tutoring."),
 ]),
 ],
 assess=dict(t="Assessment 5: Relationships Between Variables",
 prompt="""Write a report of at least 250 words on relationships between variables. Use complete sentences, show your work and label each part. Proverbs 27:17 says, Iron sharpeneth iron; so a man sharpeneth the countenance of his friend.

Part 1: Ten students recorded hours of sleep (x) and minutes needed to finish a math quiz (y). Describe the explanatory and response variables, sketch a scatter plot of your own ten made up but realistic pairs, and describe the direction, form and strength.
Part 2: A regression line for hours of practice x and number of hymns learned y is y hat equals 1.5 plus 0.5 times x. Interpret the slope and intercept, predict y for x equal to 6, and find the residual for a student who practiced 6 hours and learned 5 hymns.
Part 3: Explain what a correlation of 0.85 and a correlation of negative 0.85 mean, and tell why a correlation of 0 does not always mean no relationship.
Part 4: In a survey of 100 students, 60 use a planner and 40 do not. Among planner users, 45 turned in all assignments on time. Among non users, 20 turned in all assignments on time. Make a two way table, find the conditional percents and tell whether there is an association.
Part 5: Explain, using John 9:2 and 3, why we must not conclude cause from association alone. Give one example of a lurking variable.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 25 points. Part 3: 15 points. Part 4: 20 points. Part 5: 15 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 5: Patterns and Causes",
 prompt="""Write a post of at least 120 words that (1) describes two things you have noticed that seem to be related, such as sleep and mood or practice and skill, (2) explains how you could test whether one really causes the other, (3) describes a headline or claim you have heard that confused correlation and causation, and (4) connects your answer to John 9:2 and 3, Proverbs 27:17 or Matthew 7:16. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why is it unfair to blame a person for a hardship just because two things seem linked? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("In a scatter plot, a pattern where points rise from left to right shows a:", ["Positive association", "Negative association", "No association", "Causal relationship"], 0, "Rising points indicate a positive direction."),
 ("A correlation near 0 suggests:", ["Little or no linear relationship", "A strong positive relationship", "A strong negative relationship", "Perfect prediction"], 0, "Values near 0 show a weak linear pattern."),
 ("In y hat equals 3 plus 2 times x, the predicted y when x is 5 is:", ["13", "10", "8", "17"], 0, "3 plus 2 times 5 equals 13."),
 ("The slope of a regression line tells us:", ["The predicted change in y for each 1 unit increase in x", "The value of y when x is zero", "The correlation", "The residual"], 0, "Slope is the rate of change."),
 ("A residual of negative 2 means the actual value was:", ["2 below the predicted value", "2 above the predicted value", "Equal to the predicted value", "Zero"], 0, "Actual minus predicted is negative, so the point is below the line."),
 ("In a two way table, a conditional relative frequency divides a cell count by:", ["The row or column total", "The grand total", "The largest count", "Zero"], 0, "Conditional percents use the group total."),
 ("A lurking variable can make two variables appear:", ["Related when neither causes the other", "Unrelated always", "Identical", "Certain"], 0, "It may create a false link."),
 ("Which can best establish that a treatment causes an effect?", ["A randomized experiment", "A strong correlation alone", "A scatter plot", "A news headline"], 0, "Random assignment controls lurking variables."),
 ],
)
