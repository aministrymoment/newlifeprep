"""Algebra 2, Unit 5: Exponential and Logarithmic Functions and Financial Literacy."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."

UNIT5 = dict(
 title="Unit 5: Exponential and Logarithmic Functions and Financial Literacy",
 std="MA.912.NSO.1.6, MA.912.NSO.1.7, MA.912.AR.5.2, MA.912.AR.5.4, MA.912.AR.5.5, MA.912.AR.5.7, MA.912.AR.5.8, MA.912.AR.5.9, MA.912.DP.2.9, MA.912.FL.3.1, MA.912.FL.3.2, MA.912.FL.3.4",
 topics=[
 dict(t="5.1 Exponential Functions and Equations", std="MA.912.AR.5.2, MA.912.AR.5.4, MA.912.NSO.1.6",
 body="""An exponential function has the form f(x) = a times b to the power x, where a is not 0, b is positive and b is not 1.
If b > 1 the function models growth. If 0 < b < 1 it models decay.
The y intercept is a, and the horizontal asymptote is y = 0 for the parent form.

Growth example: a town has 500 people and grows 4 percent each year. P(t) = 500(1.04) to the power t. After 10 years, P(10) = 500(1.04) to the power 10, which is about 740 people.

Decay example: a medicine has 80 milligrams and a half life of 5 years in a sample. A(t) = 80(1/2) to the power (t/5). After 15 years, A(15) = 80(1/2) cubed = 10 milligrams.

The base can be written from the percent change: growth of r gives b = 1 + r, and decay of r gives b = 1 minus r.

Transformations: g(x) = 2 to the power (x minus 3) + 1 shifts the parent 2 to the power x right 3 and up 1, so the horizontal asymptote becomes y = 1.

Solving exponential equations with the same base: write both sides as powers of one base, then set the exponents equal.
2 to the power (x + 1) = 32 gives 2 to the power (x + 1) = 2 to the 5, so x + 1 = 5 and x = 4.
9 to the power x = 27 gives 3 to the power 2x = 3 cubed, so 2x = 3 and x = 3/2.

Rational exponents are exponential facts too: 4 to the power 3/2 = (the square root of 4) cubed = 8.

Your task: (1) A bank account grows 5 percent each year from $2000. Write the function and find the balance after 3 years. (2) Solve 3 to the power (2x minus 1) = 81. (3) Describe the transformation and asymptote of h(x) = 2 to the power (x + 2) minus 4.""",
 script="""Welcome to Unit 5. Listen, some things grow by adding the same amount, and other things grow by multiplying by the same factor. Those that multiply are exponential. An exponential function has the form f of x equals a times b to the power x. If b is greater than one, you have growth. If b is between zero and one, you have decay. The y intercept is a, and the parent form has the horizontal asymptote y equals zero.

Now watch this. A town has five hundred people and grows four percent each year. The function is P of t equals five hundred times one point zero four to the power t. After ten years, that is about seven hundred forty people.

Look at decay. A sample has eighty milligrams with a half life of five years. The amount is eighty times one half to the power t over five. After fifteen years that is three half lives, so eighty times one half cubed, which is ten milligrams.

You can build the base from the percent change. Growth of r gives b equals one plus r. Decay of r gives b equals one minus r.

Transformations work as they did before. Two to the power x minus three, plus one, shifts the parent right three and up one, so the horizontal asymptote moves to y equals one.

To solve exponential equations with the same base, write both sides as powers of one base, then set the exponents equal. Two to the power x plus one equals thirty two. Thirty two is two to the fifth, so x plus one is five and x is four. Nine to the x equals twenty seven. Write both as powers of three. Three to the two x equals three cubed. So two x is three, and x is three halves.

Your task today. A bank account grows five percent each year from two thousand dollars. Write the function and find the balance after three years. Solve three to the power two x minus one equals eighty one. And describe the transformation and asymptote of two to the power x plus two, minus four. Take the four question check when you finish.

Faithful small steps multiply into great harvests. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("In f(x) = a times b to the power x with b greater than 1, the function models:", ["Exponential growth", "Exponential decay", "Linear growth", "A constant"], 0, "A base greater than 1 gives growth."),
 ("A quantity of 80 with a half life of 5 years is A(t) = 80(1/2) to the power (t/5). After 15 years it is:", ["10", "40", "20", "5"], 0, "15 years is three half lives, and 80 times (1/2) cubed = 10."),
 ("The solution of 2 to the power (x + 1) = 32 is:", ["x = 4", "x = 5", "x = 3", "x = 16"], 0, "32 = 2 to the 5, so x + 1 = 5 and x = 4."),
 ("The horizontal asymptote of g(x) = 2 to the power (x minus 3) + 1 is:", ["y = 1", "y = 0", "y = 3", "y = negative 1"], 0, "The vertical shift of 1 moves the asymptote from y = 0 to y = 1."),
 ]),
 dict(t="5.2 Logarithms and Their Properties", std="MA.912.NSO.1.7, MA.912.AR.5.5, MA.912.AR.5.7",
 body="""A logarithm is the exponent. The statement log base b of a = c means b to the power c = a. It asks, "To what power must b be raised to get a?"

Examples:
log base 2 of 32 = 5 because 2 to the 5 = 32.
log base 10 of 1000 = 3 because 10 cubed = 1000.
log base 3 of (1/9) = negative 2 because 3 to the negative 2 = 1/9.
The natural logarithm ln x is log base e, where e is about 2.718. So ln(e to the 4) = 4.

Logarithmic and exponential functions are inverses. The graph of y = log base b of x has a vertical asymptote at x = 0, passes through (1, 0) and (b, 1), and has domain x > 0.

Properties of logarithms:
Product: log of (mn) = log m + log n.
Quotient: log of (m/n) = log m minus log n.
Power: log of (m to the p) = p times log m.
Change of base: log base b of a = (log a)/(log b), using either log base 10 or ln.

Examples:
log base 2 of 6 + log base 2 of (4/3) = log base 2 of 8 = 3.
Expand log of (x squared y / z) = 2 log x + log y minus log z.
Write 3 ln 2 + ln 5 as ln 40.

Solving equations:
log base 3 of x = 4 gives x = 3 to the 4 = 81.
5 to the power x = 20 gives x = (log 20)/(log 5), about 1.861.
log base 2 of x + log base 2 of (x minus 2) = 3 gives x(x minus 2) = 8, so x squared minus 2x minus 8 = 0 and x = 4 or x = negative 2. Since the log of a negative number is undefined, only x = 4 works.

Your task: (1) Evaluate log base 4 of 64 and log base 5 of (1/25). (2) Expand log of (a cubed b / c squared). (3) Solve 7 to the power x = 50 using logarithms and give the answer to the nearest thousandth.""",
 script="""Now we meet logarithms. Listen, a logarithm is an exponent. The statement log base b of a equals c means b to the power c equals a. It asks, to what power must I raise b to get a.

Watch this. Log base two of thirty two is five, because two to the fifth is thirty two. Log base ten of one thousand is three. Log base three of one ninth is negative two, because three to the negative two is one ninth. And the natural logarithm, written l n, uses the base e, which is about two point seven one eight. So l n of e to the fourth is just four.

Logarithms and exponentials are inverses. The graph of y equals log base b of x has a vertical asymptote at x equals zero, passes through one, zero, and has domain x greater than zero.

The properties save you work. The log of a product is the sum of the logs. The log of a quotient is the difference. The log of a power brings the exponent down in front. And the change of base formula says log base b of a equals log a over log b, using either common logs or natural logs.

Look at examples. Log base two of six plus log base two of four thirds is log base two of eight, which is three. To expand log of x squared y over z, you get two log x, plus log y, minus log z. And three l n two plus l n five becomes l n of forty.

Now solving. Log base three of x equals four means x equals three to the fourth, which is eighty one. Five to the x equals twenty means x is log twenty over log five, about one point eight six one. And log base two of x, plus log base two of x minus two, equals three. Combine them to get x times x minus two equals eight. That gives x squared minus two x minus eight equals zero, so x is four or negative two. We cannot take the log of a negative number, so only four works.

Your task today. Evaluate log base four of sixty four, and log base five of one twenty fifth. Expand log of a cubed b over c squared. And solve seven to the x equals fifty, rounding to the nearest thousandth. Take the four question check when you finish.

Every answer has an exponent behind it that tells how far it came. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("log base 2 of 32 equals:", ["5", "16", "6", "4"], 0, "2 to the 5 equals 32."),
 ("log base 3 of (1/9) equals:", ["negative 2", "2", "negative 3", "1/2"], 0, "3 to the negative 2 equals 1/9."),
 ("log base 2 of 6 + log base 2 of (4/3) equals:", ["3", "5", "4", "2"], 0, "By the product property, log base 2 of 8 = 3."),
 ("Solving log base 2 of x + log base 2 of (x minus 2) = 3 gives:", ["x = 4 only", "x = 4 and x = negative 2", "x = negative 2 only", "x = 8"], 0, "x = negative 2 is rejected because the logarithm of a negative number is undefined."),
 ]),
 dict(t="5.3 Compound Interest and Wise Stewardship", std="MA.912.FL.3.1, MA.912.FL.3.2, MA.912.FL.3.4",
 body="""Interest is the cost of borrowing or the reward of saving. Understanding it is part of good stewardship.

Simple interest: I = Prt, where P is the principal, r is the annual rate as a decimal and t is the time in years. $2000 at 5 percent for 3 years earns I = 2000(0.05)(3) = $300, for a total of $2300.

Compound interest: A = P(1 + r/n) to the power (nt), where n is the number of compounding periods per year.
Example: $5000 at 6 percent for 10 years.
Annually (n = 1): about $8954.24.
Quarterly (n = 4): about $9070.09.
Monthly (n = 12): about $9096.98.
More frequent compounding earns a little more.

Continuous compounding: A = P times e to the power (rt). $5000 at 6 percent for 10 years gives 5000 e to the 0.6, about $9110.59.

Time to double: solve 2 = 1.06 to the power t using logarithms, t = (ln 2)/(ln 1.06), about 11.9 years. The Rule of 72 estimates doubling time as 72 divided by the percent rate: 72/6 = 12 years.

Comparing choices: $2000 at 5 percent compounded monthly for 3 years grows to 2000(1 + 0.05/12) to the 36, about $2322.94, compared with $2300 for simple interest.

Borrowing works the same way against you. A credit card balance that charges a high rate compounds quickly, so paying the balance in full each month avoids interest. Wise planning includes saving, giving, avoiding unnecessary debt and comparing rates before you borrow.

Your task: (1) Find the balance when $3000 is invested at 4 percent compounded quarterly for 5 years. (2) Use e to find the value of $12,000 at 5 percent compounded continuously for 5 years. (3) Use logarithms to find how long it takes money to triple at 7 percent compounded annually.""",
 script="""Now we apply exponents to money, because stewardship is a skill that can be learned. Interest is the cost of borrowing and the reward of saving.

Listen to simple interest. I equals P times r times t. Two thousand dollars at five percent for three years earns two thousand times point zero five times three, which is three hundred dollars, for a total of twenty three hundred.

Now watch this. Compound interest. A equals P times one plus r over n, to the power n t, where n is the number of times it compounds each year. Take five thousand dollars at six percent for ten years. Compounded annually you have about eight thousand nine hundred fifty four dollars. Compounded quarterly, about nine thousand seventy. Compounded monthly, about nine thousand ninety seven. The more often it compounds, the more you earn, though the difference is modest.

Continuous compounding uses e. A equals P times e to the power r t. Five thousand dollars at six percent for ten years gives five thousand times e to the point six, about nine thousand one hundred eleven dollars.

How long to double? Solve two equals one point zero six to the t. Take logs. t equals l n two over l n one point zero six, about eleven point nine years. The Rule of Seventy Two gives a quick estimate. Divide seventy two by the percent rate. Seventy two over six is twelve years.

Compare the choices. Two thousand dollars at five percent compounded monthly for three years grows to about twenty three hundred twenty three dollars, which beats the twenty three hundred from simple interest.

Remember that interest also works against borrowers. A credit card with a high rate compounds quickly, so paying the balance in full avoids the cost. Wise planning means saving, giving, avoiding unnecessary debt and comparing rates before you borrow.

Your task today. Find the balance when three thousand dollars is invested at four percent compounded quarterly for five years. Find the value of twelve thousand dollars at five percent compounded continuously for five years. And use logarithms to find how long it takes money to triple at seven percent compounded annually. Take the four question check when you finish.

Be faithful with a little, and let it grow. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("The simple interest on $2000 at 5 percent for 3 years is:", ["$300", "$100", "$315.25", "$2300"], 0, "I = Prt = 2000(0.05)(3) = $300."),
 ("In A = P(1 + r/n) to the power (nt), the letter n stands for:", ["The number of compounding periods per year", "The number of years", "The principal", "The annual rate"], 0, "n is the number of times interest compounds each year."),
 ("Compared with annual compounding, monthly compounding on the same deposit and rate earns:", ["A little more interest", "Less interest", "The same interest", "No interest"], 0, "More frequent compounding earns slightly more."),
 ("The Rule of 72 estimates the doubling time at 6 percent as:", ["12 years", "6 years", "72 years", "36 years"], 0, "72 divided by 6 equals 12 years."),
 ]),
 dict(t="5.4 Modeling with Exponential and Logarithmic Functions", std="MA.912.AR.5.8, MA.912.AR.5.9, MA.912.DP.2.9",
 body="""Real data often grow or shrink by a constant ratio. To decide whether an exponential model fits, check whether equal steps in x give a constant ratio of y values.

Example data: (0, 100), (1, 130), (2, 169), (3, 220). The ratios are 130/100 = 1.3, 169/130 = 1.3 and 220/169 is about 1.3. The model is y = 100(1.3) to the power x.
Prediction at x = 5: y = 100(1.3) to the 5 is about 371.
Time to reach 1000: solve 100(1.3) to the power x = 1000, so 1.3 to the x = 10 and x = (log 10)/(log 1.3), about 8.78.

Exponential regression: with technology, enter the data in a table and compute the exponential regression y = a times b to the power x. Compare it with a linear regression by checking how closely each curve follows the points. A linear model has a constant difference, while an exponential model has a constant ratio.

Interpreting the model: the value a is the starting amount, and b tells the growth or decay factor for each step. A value of b = 1.3 means 30 percent growth per step.

Logarithms in science:
pH = negative log of the hydrogen ion concentration. A concentration of 10 to the negative 3 gives pH 3.
Earthquake magnitudes use base 10. A magnitude 7 earthquake is 10 times as strong in measured amplitude as a magnitude 6.

Be careful with limits: exponential models describe a stretch of time but cannot grow forever. Population and spread models usually level off, so state the domain where your model is reliable.

Your task: (1) Show that the data (0, 50), (1, 60), (2, 72), (3, 86.4) fit an exponential model and write the model. (2) Use your model to predict the value at x = 6 and tell when it first passes 200. (3) Explain in one sentence why a model may stop being accurate far outside the data.""",
 script="""Now we model with exponentials and logarithms. Listen, real data often grow or shrink by a constant ratio. To decide if an exponential model fits, check whether equal steps in x give a constant ratio of y values.

Watch this. The data are zero, one hundred; one, one hundred thirty; two, one hundred sixty nine; three, two hundred twenty. The ratios are one point three, one point three, and about one point three again. So the model is y equals one hundred times one point three to the power x. At x equals five, y is about three hundred seventy one. To find when it reaches one thousand, solve one hundred times one point three to the x equals one thousand. Then one point three to the x equals ten, and x is log ten over log one point three, about eight point seven eight.

Now technology. Enter the data in a table and compute the exponential regression, which gives you a and b. Compare it with a linear regression and see which curve follows the points more closely. A linear model has a constant difference. An exponential model has a constant ratio.

Interpret the model. The value a is the starting amount, and b is the growth or decay factor for each step. A value of one point three means thirty percent growth per step.

Look at logarithms in science. pH is the negative of the log of the hydrogen ion concentration. A concentration of ten to the negative three gives a pH of three. Earthquake magnitudes use base ten, so a magnitude seven earthquake has ten times the measured amplitude of a magnitude six.

Be careful about limits. Exponential models describe a stretch of time, but nothing grows forever. Populations and spreading models usually level off, so state the domain where your model is reliable.

Your task today. Show that the data zero, fifty; one, sixty; two, seventy two; three, eighty six point four fit an exponential model, and write the model. Use it to predict the value at x equals six and to tell when it first passes two hundred. And explain in one sentence why a model may stop being accurate far outside the data. Take the four question check when you finish.

Wise planners ask not only how fast, but how far. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("An exponential model has a constant:", ["Ratio between y values for equal steps in x", "Difference between y values", "Slope", "x intercept"], 0, "Exponential change multiplies by the same factor each step."),
 ("For y = 100(1.3) to the power x, the growth per step is:", ["30 percent", "13 percent", "1.3 percent", "130 percent"], 0, "A factor of 1.3 means 30 percent growth."),
 ("A solution to 1.3 to the power x = 10 is found with:", ["x = (log 10)/(log 1.3)", "x = 10/1.3", "x = 10 minus 1.3", "x = 13"], 0, "Take the logarithm of both sides and divide."),
 ("The pH of a solution with hydrogen ion concentration 10 to the negative 3 is:", ["3", "negative 3", "10", "0.001"], 0, "pH = negative log of 10 to the negative 3 = 3."),
 ]),
 ],
 assess=dict(t="Assessment 5: Exponential and Logarithmic Functions and Financial Literacy",
 prompt="""Complete all parts, showing your work and explaining your reasoning.

Part A: A bank account grows 5 percent each year from $2000. Write the function and find the balance after 3 years. Solve 3 to the power (2x minus 1) = 81 and 9 to the power x = 27. Describe the transformation and the horizontal asymptote of h(x) = 2 to the power (x + 2) minus 4.

Part B: Evaluate log base 4 of 64 and log base 5 of (1/25). Expand log of (a cubed b / c squared). Write 3 ln 2 + ln 5 as a single logarithm. Solve 7 to the power x = 50 using logarithms and round to the nearest thousandth. Solve log base 2 of x + log base 2 of (x minus 2) = 3 and check your answers.

Part C: Find the balance when $3000 is invested at 4 percent compounded quarterly for 5 years. Find the value of $12,000 at 5 percent compounded continuously for 5 years. Use logarithms to find how long it takes money to triple at 7 percent compounded annually.

Part D: Compare $2000 at 5 percent for 3 years under simple interest and under interest compounded monthly. Which earns more and by how much? In two sentences, advise a young adult about using credit cards wisely.

Part E: Show that the data (0, 50), (1, 60), (2, 72), (3, 86.4) fit an exponential model and write the model. Use it to predict the value at x = 6 and find when it first passes 200.

Part F: In at least 60 words, explain how understanding compound interest can help a family or ministry plan wisely for saving, giving and borrowing. Connect your answer to Proverbs 22:7, which says, The rich ruleth over the poor, and the borrower is servant to the lender.""",
 rubric="""100 points. Part A, exponential functions and equations: 14 points. Part B, logarithms and equations: 22 points. Part C, interest calculations: 18 points. Part D, comparison and advice: 12 points. Part E, modeling from data: 20 points. Part F, written reflection: 10 points. Clear work and complete sentences: 4 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 5: Faithful Stewards",
 prompt="""Money and time grow by the same mathematics. Small, steady choices multiply over years, whether they are saving, giving or paying down debt. Write a post of at least 120 words that (1) explains in your own words the difference between simple interest and compound interest, (2) describes a goal you could reach by saving steadily, such as a car, a school, a mission trip or a ministry project, and how compounding could help, (3) tells why avoiding high interest debt is wise, and (4) connects your answer to Proverbs 13:11, which says, Wealth gotten by vanity shall be diminished: but he that gathereth by labour shall increase. Then write a respectful reply of at least 40 words to another student, or answer this question: Why does more frequent compounding earn only a little more interest? Keep your language clean and your tone kind."""),
 unit_quiz=[
 ("A town of 500 people grows 4 percent each year. The function is:", ["P(t) = 500(1.04) to the power t", "P(t) = 500 + 0.04t", "P(t) = 500(0.04) to the power t", "P(t) = 504 to the power t"], 0, "Growth of 4 percent gives a base of 1.04."),
 ("The solution of 9 to the power x = 27 is:", ["x = 3/2", "x = 3", "x = 2/3", "x = 18"], 0, "3 to the power 2x = 3 cubed gives 2x = 3."),
 ("log base 10 of 1000 equals:", ["3", "100", "10", "1000"], 0, "10 cubed equals 1000."),
 ("Expanding log of (x squared y / z) gives:", ["2 log x + log y minus log z", "log x squared + log y + log z", "2 log x times log y divided by log z", "log 2x + log y minus log z"], 0, "Use the power, product and quotient properties."),
 ("Solving 5 to the power x = 20 gives x equal to:", ["(log 20)/(log 5), about 1.861", "20 minus 5", "20/5", "(log 5)/(log 20)"], 0, "Take logs of both sides and divide."),
 ("The formula for continuous compounding is:", ["A = P times e to the power (rt)", "A = P(1 + r) times t", "A = Prt", "A = P(1 + r/n) to the power (nt)"], 0, "Continuous compounding uses the base e."),
 ("Money grows 6 percent a year. By the Rule of 72 it doubles in about:", ["12 years", "6 years", "72 years", "24 years"], 0, "72 divided by 6 equals 12."),
 ("Data with a constant ratio between y values for equal steps in x fit:", ["An exponential model", "A linear model", "A quadratic model", "An absolute value model"], 0, "A constant ratio is the signature of exponential change."),
 ])
