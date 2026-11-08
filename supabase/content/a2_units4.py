"""Algebra 2, Unit 4: Radicals, Rational Exponents, Rational and Absolute Value Functions."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."

UNIT4 = dict(
 title="Unit 4: Radicals, Rational Expressions and Absolute Value",
 std="MA.912.NSO.1.3, MA.912.NSO.1.5, MA.912.AR.1.9, MA.912.AR.4.2, MA.912.AR.4.4, MA.912.AR.7.1, MA.912.AR.7.2, MA.912.AR.7.3, MA.912.AR.8.1, MA.912.AR.8.2, MA.912.AR.8.3",
 topics=[
 dict(t="4.1 Radicals and Rational Exponents", std="MA.912.NSO.1.3, MA.912.NSO.1.5",
 body="""The nth root of a number a is a number that, raised to the nth power, equals a. We write it with a radical sign and the index n. The square root has index 2 and the cube root has index 3.

Rational exponents connect radicals and powers.
a to the power 1/n = the nth root of a.
a to the power m/n = (the nth root of a) to the power m = the nth root of (a to the power m).

Examples:
8 to the power 2/3 = (cube root of 8) squared = 2 squared = 4.
16 to the power 3/4 = (fourth root of 16) cubed = 2 cubed = 8.
27 to the power negative 1/3 = 1 divided by (27 to the power 1/3) = 1/3.

Laws of exponents still hold for rational exponents:
x to the 1/2 times x to the 3/2 = x to the 2 = x squared.
(8x to the 6) to the 1/3 = 2x squared.
(x to the 2/3) divided by (x to the 1/6) = x to the 1/2.

Simplify radicals by pulling out perfect powers.
The square root of 50 = the square root of 25 times the square root of 2 = 5 times the square root of 2.
The cube root of 54 = the cube root of 27 times the cube root of 2 = 3 times the cube root of 2.

Rationalize the denominator, which means removing a radical from the bottom.
6 divided by the square root of 3 = 6 times the square root of 3 divided by 3 = 2 times the square root of 3.
1 divided by (2 + the square root of 3): multiply the top and bottom by the conjugate 2 minus the square root of 3. The bottom becomes 4 minus 3 = 1, so the result is 2 minus the square root of 3.

Add radicals only when the radicals are alike: 3 times the square root of 2 + 5 times the square root of 2 = 8 times the square root of 2.

Your task: (1) Evaluate 32 to the power 3/5 and 81 to the power negative 3/4. (2) Simplify the square root of 72 and the cube root of 250. (3) Rationalize 10 divided by (3 minus the square root of 2).""",
 script="""Welcome to Unit 4. Listen, a radical asks a question. The nth root of a number a is the number that, raised to the nth power, gives a. The square root has index two. The cube root has index three.

Now watch this. Rational exponents connect radicals to powers. A to the one over n is the nth root of a. And a to the m over n is the nth root of a, raised to the power m. So eight to the two thirds is the cube root of eight, squared. The cube root of eight is two, and two squared is four. Sixteen to the three fourths is the fourth root of sixteen, cubed, which is two cubed, which is eight. And twenty seven to the negative one third flips it, so you get one over the cube root of twenty seven, which is one third.

The laws of exponents still work. x to the one half, times x to the three halves, adds the exponents to get x squared. Eight x to the sixth, all to the one third power, is two x squared. And x to the two thirds, divided by x to the one sixth, subtracts the exponents to give x to the one half.

Look at simplifying radicals. Pull out perfect powers. The square root of fifty is the square root of twenty five times the square root of two, which is five times the square root of two. The cube root of fifty four is three times the cube root of two.

Next, rationalizing the denominator. Six over the square root of three becomes six times the square root of three over three, which is two times the square root of three. And one over two plus the square root of three? Multiply top and bottom by the conjugate, two minus the square root of three. The bottom becomes four minus three, which is one. So the answer is two minus the square root of three.

Remember that you can add radicals only when they are alike. Three square roots of two plus five square roots of two is eight square roots of two.

Your task today. Evaluate thirty two to the three fifths and eighty one to the negative three fourths. Simplify the square root of seventy two and the cube root of two hundred fifty. And rationalize ten over three minus the square root of two. Take the four question check when you finish.

There is power in what looks hidden beneath the surface. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("8 to the power 2/3 equals:", ["4", "16", "2", "8/3"], 0, "The cube root of 8 is 2, and 2 squared is 4."),
 ("27 to the power negative 1/3 equals:", ["1/3", "3", "negative 3", "negative 1/3"], 0, "A negative exponent gives the reciprocal, 1 divided by the cube root of 27, which is 1/3."),
 ("The square root of 50 simplifies to:", ["5 times the square root of 2", "25 times the square root of 2", "2 times the square root of 5", "10 times the square root of 5"], 0, "The square root of 25 times the square root of 2 equals 5 times the square root of 2."),
 ("Rationalizing 6 divided by the square root of 3 gives:", ["2 times the square root of 3", "6 times the square root of 3", "the square root of 3", "2"], 0, "Multiply the top and bottom by the square root of 3 to get 6 times the square root of 3 over 3, which is 2 times the square root of 3."),
 ]),
 dict(t="4.2 Radical and Absolute Value Equations and Inequalities", std="MA.912.AR.7.1, MA.912.AR.1.9",
 body="""Radical equations. To solve an equation with a radical, isolate the radical, raise both sides to the power equal to the index, solve, and then check every answer. Squaring can create extraneous solutions that do not satisfy the original equation.

Example: the square root of (x + 5) = x minus 1. Square both sides: x + 5 = x squared minus 2x + 1. Then x squared minus 3x minus 4 = 0, so (x minus 4)(x + 1) = 0 and x = 4 or x = negative 1.
Check x = 4: the square root of 9 = 3 and 4 minus 1 = 3. This works.
Check x = negative 1: the square root of 4 = 2 but negative 1 minus 1 = negative 2. This does not work, so it is extraneous.
The solution is x = 4.

Example: the square root of (3x minus 2) + 4 = 7. Isolate the radical: the square root of (3x minus 2) = 3. Square: 3x minus 2 = 9, so x = 11/3. It checks.

Rational exponent equation: x to the 2/3 = 9. Raise both sides to the 3/2 power: x = plus or minus 9 to the 3/2 = plus or minus 27. Both work.

Absolute value is the distance from zero. |a| equals a when a is at least 0, and negative a when a is less than 0.

Absolute value equations: |2x minus 3| = 7 means 2x minus 3 = 7 or 2x minus 3 = negative 7, so x = 5 or x = negative 2. An equation such as |x minus 2| = negative 3 has no solution because an absolute value cannot be negative.

Absolute value inequalities:
|x + 4| < 6 means negative 6 < x + 4 < 6, so negative 10 < x < 2 (an "and" statement).
|3x minus 1| is at least 5 means 3x minus 1 is at least 5 or at most negative 5, so x is at least 2 or x is at most negative 4/3 (an "or" statement).

Your task: (1) Solve the square root of (2x + 9) = x + 3 and check. (2) Solve |x minus 5| = 3 and |2x + 1| is at most 7. (3) Explain why |x| = negative 4 has no solution.""",
 script="""Now we solve equations with radicals and absolute values. Listen to the plan for radical equations. Isolate the radical, raise both sides to the power equal to the index, solve, and then check every answer. Squaring can create extraneous solutions, answers that fail in the original equation.

Watch this. The square root of x plus five equals x minus one. Square both sides. x plus five equals x squared minus two x plus one. Move everything over, and you have x squared minus three x minus four equals zero, which factors as x minus four, times x plus one. So x is four or negative one. Now check. When x is four, the square root of nine is three, and four minus one is three. That works. When x is negative one, the square root of four is two, but negative one minus one is negative two. That fails. So negative one is extraneous, and the only solution is four.

Look at another. The square root of three x minus two, plus four, equals seven. Isolate the radical to get the square root of three x minus two equals three. Square it. Three x minus two equals nine, so x is eleven thirds, and it checks.

With a rational exponent, x to the two thirds equals nine. Raise both sides to the three halves power. x equals plus or minus twenty seven, and both work.

Now absolute value. Absolute value is the distance from zero. To solve absolute value of two x minus three equals seven, split it into two equations. Two x minus three equals seven, or two x minus three equals negative seven. So x is five or negative two. And an equation like absolute value of x minus two equals negative three has no solution, because a distance cannot be negative.

For inequalities, watch the shape. Absolute value of x plus four less than six means x plus four is between negative six and six, so x is between negative ten and two. That is an and statement. Absolute value of three x minus one at least five means three x minus one is at least five, or at most negative five. So x is at least two, or at most negative four thirds. That is an or statement.

Your task today. Solve the square root of two x plus nine equals x plus three, and check. Solve absolute value of x minus five equals three, and absolute value of two x plus one at most seven. And explain why absolute value of x equals negative four has no solution. Take the four question check when you finish.

Test every answer, because truth survives the check. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("A solution that comes from squaring but fails in the original equation is called:", ["Extraneous", "Rational", "Imaginary", "Repeated"], 0, "Extraneous solutions appear when squaring, so every answer must be checked."),
 ("The solution of the square root of (x + 5) = x minus 1 is:", ["x = 4 only", "x = 4 and x = negative 1", "x = negative 1 only", "No solution"], 0, "x = negative 1 is extraneous because the square root of 4 does not equal negative 2."),
 ("The solutions of |2x minus 3| = 7 are:", ["x = 5 and x = negative 2", "x = 5 only", "x = 2 and x = negative 5", "x = 7 and x = negative 7"], 0, "Solve 2x minus 3 = 7 and 2x minus 3 = negative 7."),
 ("The solution of |x + 4| < 6 is:", ["negative 10 < x < 2", "x < negative 10 or x > 2", "x < 2", "negative 2 < x < 10"], 0, "Less than gives an and statement: negative 6 < x + 4 < 6."),
 ]),
 dict(t="4.3 Rational Expressions and Equations", std="MA.912.AR.4.2, MA.912.AR.4.4",
 body="""A rational expression is a ratio of two polynomials. It is undefined when the denominator is 0, so we state the excluded values.

Simplify by factoring and canceling common factors.
(x squared minus 9)/(x squared + x minus 6) = (x minus 3)(x + 3)/((x + 3)(x minus 2)) = (x minus 3)/(x minus 2), where x is not equal to negative 3 or 2.

Multiply by multiplying tops and bottoms after factoring; divide by multiplying by the reciprocal.
x/(x + 2) times (x squared minus 4)/x squared = (x minus 2)/x, where x is not 0 or negative 2.

Add and subtract by using a common denominator.
1/x + 2/(x + 3) = ((x + 3) + 2x)/(x(x + 3)) = (3x + 3)/(x(x + 3)).

Solve a rational equation by multiplying both sides by the common denominator, solving, and checking for extraneous solutions.
Example: 1/x + 1/(x + 2) = 3/4. Multiply by 4x(x + 2): 4(x + 2) + 4x = 3x(x + 2). That gives 3x squared minus 2x minus 8 = 0, so (3x + 4)(x minus 2) = 0 and x = 2 or x = negative 4/3. Both check.

Extraneous example: x/(x minus 3) = 3/(x minus 3) + 2. Multiply by x minus 3: x = 3 + 2(x minus 3), so x = 3. But 3 makes a denominator 0, so there is no solution.

Work problem: one pipe fills a tank in 6 hours and another fills it in 3 hours. Together, 1/6 + 1/3 = 1/t, so 1/t = 1/2 and t = 2 hours.

Your task: (1) Simplify (x squared minus 16)/(x squared minus x minus 12) and state the excluded values. (2) Solve 5/(x minus 2) = 3/(x + 2). (3) A worker finishes a job in 4 hours and a helper finishes it in 12 hours. How long does the job take together?""",
 script="""Now we work with rational expressions, which are ratios of polynomials. Listen, a rational expression is undefined when its denominator is zero, so we always state the excluded values.

Watch this. To simplify, factor and cancel common factors. x squared minus nine, over x squared plus x minus six, factors into x minus three, times x plus three, over x plus three, times x minus two. Cancel the x plus three, and you have x minus three over x minus two. But x cannot be negative three or two.

To multiply, factor first, then multiply tops and bottoms. To divide, multiply by the reciprocal. x over x plus two, times x squared minus four over x squared, simplifies to x minus two over x.

To add or subtract, use a common denominator. One over x, plus two over x plus three, becomes x plus three plus two x, all over x times x plus three, which is three x plus three over x times x plus three.

Look at solving equations. Multiply both sides by the common denominator, solve, and check. Try one over x plus one over x plus two equals three fourths. Multiply by four x times x plus two. You get four times x plus two, plus four x, equals three x times x plus two. That simplifies to three x squared minus two x minus eight equals zero, which factors as three x plus four, times x minus two. So x is two or negative four thirds, and both check.

Now be careful. x over x minus three equals three over x minus three, plus two. Multiply by x minus three, and you get x equals three plus two times x minus three, so x is three. But three makes a denominator zero. There is no solution. That is the extraneous solution again.

Rational equations model work. If one pipe fills a tank in six hours and another in three hours, then one sixth plus one third equals one over t. So one over t is one half, and t is two hours.

Your task today. Simplify x squared minus sixteen over x squared minus x minus twelve, and state the excluded values. Solve five over x minus two equals three over x plus two. And find how long a job takes when one person finishes in four hours and a helper in twelve. Take the four question check when you finish.

Working together makes the load lighter. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("The excluded values of (x minus 3)/((x + 3)(x minus 2)) are:", ["x = negative 3 and x = 2", "x = 3 only", "x = 3 and x = negative 2", "There are none"], 0, "The denominator is 0 when x = negative 3 or x = 2."),
 ("1/x + 2/(x + 3) equals:", ["(3x + 3)/(x(x + 3))", "3/(x(x + 3))", "3/(2x + 3)", "(x + 5)/(x(x + 3))"], 0, "Use the common denominator x(x + 3): (x + 3 + 2x)/(x(x + 3))."),
 ("The equation x/(x minus 3) = 3/(x minus 3) + 2 has:", ["No solution, because x = 3 is extraneous", "The solution x = 3", "The solution x = 0", "Infinitely many solutions"], 0, "Solving gives x = 3, which makes the denominator 0, so it is extraneous."),
 ("One pipe fills a tank in 6 hours and another in 3 hours. Together they fill it in:", ["2 hours", "4.5 hours", "9 hours", "1 hour"], 0, "1/6 + 1/3 = 1/2, so the time is 2 hours."),
 ]),
 dict(t="4.4 Graphs of Rational and Absolute Value Functions", std="MA.912.AR.8.1, MA.912.AR.8.2, MA.912.AR.8.3",
 body="""Rational functions have the form f(x) = p(x)/q(x). Their graphs have asymptotes, lines the graph approaches.

Vertical asymptote: at a zero of the denominator that is not also a zero of the numerator.
Hole: if a factor cancels, there is a hole at that x value instead of an asymptote.
Horizontal asymptote (compare degrees of top and bottom):
Degree of top less than degree of bottom: y = 0.
Degrees equal: y = ratio of leading coefficients.
Degree of top greater: no horizontal asymptote. If it is exactly one greater, there is a slant asymptote found by division.

Intercepts: the x intercepts are zeros of the numerator, and the y intercept is f(0).

Examples:
f(x) = 1/(x minus 2) + 3 is the parent 1/x shifted right 2 and up 3. The vertical asymptote is x = 2 and the horizontal asymptote is y = 3.
f(x) = (2x + 1)/(x minus 3) has vertical asymptote x = 3 and horizontal asymptote y = 2. The x intercept is negative 1/2 and the y intercept is negative 1/3.
f(x) = (x squared minus 1)/(x minus 1) simplifies to x + 1 with a hole at x = 1, at the point (1, 2).
f(x) = (x squared + 1)/(x minus 2) divides to x + 2 + 5/(x minus 2). The vertical asymptote is x = 2 and the slant asymptote is y = x + 2.

Absolute value functions: f(x) = a|x minus h| + k has vertex (h, k). It opens up if a is positive and down if a is negative, and the graph is V shaped.
f(x) = |x minus 2| + 1 has vertex (2, 1).
g(x) = negative 2|x + 1| + 3 has vertex (negative 1, 3), opens down, and is stretched by a factor of 2. Its x intercepts are where |x + 1| = 3/2, so x = 1/2 and x = negative 5/2.

Your task: (1) Find the asymptotes and intercepts of f(x) = (3x minus 6)/(x + 1). (2) Identify the hole of (x squared minus 4)/(x minus 2). (3) Give the vertex, direction and x intercepts of h(x) = |x + 3| minus 2.""",
 script="""Now we graph rational and absolute value functions. A rational function is a ratio of two polynomials, and its graph has asymptotes. Those are lines the graph gets close to but does not cross in the same way.

Listen to the rules. A vertical asymptote sits at a zero of the denominator that does not cancel. If a factor cancels, you have a hole at that x value instead. For the horizontal asymptote, compare degrees. If the top has a smaller degree, the asymptote is y equals zero. If the degrees are equal, it is y equals the ratio of the leading coefficients. If the top is bigger by exactly one degree, there is a slant asymptote, and you find it by division.

Look at examples. f of x equals one over x minus two, plus three. That is the parent one over x, shifted right two and up three. The vertical asymptote is x equals two, and the horizontal asymptote is y equals three.

Now watch this. f of x equals two x plus one over x minus three. The vertical asymptote is x equals three. The degrees match, so the horizontal asymptote is y equals two. The x intercept is negative one half, and the y intercept is negative one third.

Consider x squared minus one over x minus one. Factor the top, cancel x minus one, and you get x plus one, with a hole at x equals one, at the point one, two.

And x squared plus one over x minus two divides to x plus two, plus five over x minus two. The vertical asymptote is x equals two, and the slant asymptote is y equals x plus two.

Now absolute value functions. The form a times absolute value of x minus h, plus k, has its vertex at h, k, and its graph is a V. If a is positive it opens up. If a is negative it opens down. Take g of x equals negative two times absolute value of x plus one, plus three. The vertex is negative one, three. It opens down and is stretched by a factor of two. To find the x intercepts, set absolute value of x plus one equal to three halves, so x is one half or negative five halves.

Your task today. Find the asymptotes and intercepts of three x minus six over x plus one. Identify the hole of x squared minus four over x minus two. And give the vertex, direction and x intercepts of absolute value of x plus three, minus two. Take the four question check when you finish.

Know the boundaries that guide a path. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("The vertical asymptote of f(x) = (2x + 1)/(x minus 3) is:", ["x = 3", "x = negative 1/2", "y = 2", "x = 2"], 0, "The denominator is 0 at x = 3 and the numerator is not 0 there."),
 ("The horizontal asymptote of f(x) = (2x + 1)/(x minus 3) is:", ["y = 2", "y = 0", "y = 3", "No horizontal asymptote"], 0, "The degrees are equal, so the asymptote is the ratio of leading coefficients, 2/1 = 2."),
 ("The graph of (x squared minus 1)/(x minus 1) has:", ["A hole at x = 1", "A vertical asymptote at x = 1", "A horizontal asymptote at y = 1", "No x intercept and no hole"], 0, "The factor x minus 1 cancels, leaving a hole at x = 1."),
 ("The vertex of f(x) = |x minus 2| + 1 is:", ["(2, 1)", "(negative 2, 1)", "(2, negative 1)", "(1, 2)"], 0, "In a|x minus h| + k the vertex is (h, k)."),
 ]),
 ],
 assess=dict(t="Assessment 4: Radicals, Rational Expressions and Absolute Value",
 prompt="""Complete all parts, showing your work and explaining your reasoning.

Part A: Evaluate 32 to the power 3/5 and 81 to the power negative 3/4. Simplify the square root of 72 and the cube root of 250. Rationalize 10 divided by (3 minus the square root of 2).

Part B: Solve the square root of (2x + 9) = x + 3 and check each answer, identifying any extraneous solution. Solve x to the power 2/3 = 16. Solve |x minus 5| = 3, solve |2x + 1| at most 7, and solve |3x minus 1| at least 5. Explain why |x| = negative 4 has no solution.

Part C: Simplify (x squared minus 16)/(x squared minus x minus 12) and state the excluded values. Add 2/x + 1/(x minus 1). Solve 5/(x minus 2) = 3/(x + 2) and check.

Part D: A worker finishes a job in 4 hours and a helper finishes it in 12 hours. Write and solve an equation for the time needed to finish the job together.

Part E: For f(x) = (3x minus 6)/(x + 1), find the vertical asymptote, horizontal asymptote, x intercept and y intercept. Identify the hole of (x squared minus 4)/(x minus 2). For h(x) = |x + 3| minus 2, give the vertex, direction of opening and x intercepts.

Part F: In at least 60 words, explain why it is wise to check answers to radical and rational equations. Connect your answer to Proverbs 4:7, which says, Wisdom is the principal thing; therefore get wisdom: and with all thy getting get understanding.""",
 rubric="""100 points. Part A, radicals and exponents: 14 points. Part B, radical and absolute value equations: 22 points. Part C, rational expressions and equations: 18 points. Part D, work problem: 10 points. Part E, graph features: 24 points. Part F, written reflection: 8 points. Clear work and complete sentences: 4 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 4: A Lamp for the Path",
 prompt="""Asymptotes and boundaries show us where a graph can and cannot go, and checking answers shows us which solutions are true. Write a post of at least 120 words that (1) explains in your own words what an asymptote tells us about a function, (2) gives an example from daily life, school or ministry where there is a limit that something approaches but does not pass, such as filling a tank or saving toward a goal, (3) tells why extraneous solutions teach us to check our work, and (4) connects your answer to Psalm 119:105, which says, Thy word is a lamp unto my feet, and a light unto my path. Then write a respectful reply of at least 40 words to another student, or answer this question: How can you tell whether a rational function has a hole or a vertical asymptote? Keep your language clean and your tone kind."""),
 unit_quiz=[
 ("16 to the power 3/4 equals:", ["8", "12", "4", "64"], 0, "The fourth root of 16 is 2, and 2 cubed is 8."),
 ("Rationalizing 1 divided by (2 + the square root of 3) gives:", ["2 minus the square root of 3", "2 + the square root of 3", "1 minus the square root of 3", "the square root of 3"], 0, "Multiply by the conjugate: (2 minus the square root of 3)/(4 minus 3) = 2 minus the square root of 3."),
 ("Solving the square root of (x + 5) = x minus 1 and checking leaves the solution:", ["x = 4", "x = negative 1", "x = 4 and x = negative 1", "No solution"], 0, "x = negative 1 is extraneous, so only x = 4 works."),
 ("The solution of |3x minus 1| at least 5 is:", ["x at most negative 4/3 or x at least 2", "negative 4/3 at most x at most 2", "x at least 2 only", "x at most negative 4/3 only"], 0, "At least gives an or statement: 3x minus 1 at least 5 or at most negative 5."),
 ("Simplifying (x squared minus 9)/(x squared + x minus 6) gives:", ["(x minus 3)/(x minus 2)", "(x + 3)/(x minus 2)", "(x minus 3)/(x + 2)", "x minus 3"], 0, "Factor and cancel x + 3 to get (x minus 3)/(x minus 2)."),
 ("Solving 1/x + 1/(x + 2) = 3/4 gives:", ["x = 2 and x = negative 4/3", "x = 2 only", "x = negative 4/3 only", "x = 4 and x = negative 2"], 0, "Clearing denominators gives (3x + 4)(x minus 2) = 0, and both answers check."),
 ("The horizontal asymptote of f(x) = (4x + 1)/(2x minus 5) is:", ["y = 2", "y = 4", "y = 0", "y = 1/2"], 0, "The degrees are equal, so y = 4/2 = 2."),
 ("The graph of g(x) = negative 2|x + 1| + 3 has vertex and direction:", ["(negative 1, 3), opens down", "(1, 3), opens down", "(negative 1, 3), opens up", "(1, negative 3), opens up"], 0, "The vertex is (negative 1, 3) and a = negative 2 means it opens down."),
 ])
