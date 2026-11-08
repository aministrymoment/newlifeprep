"""Algebra 2 final module: final assessment (position 7) and final exam (quiz position 31)."""

FINAL_ASSESS = dict(t="Final Assessment: Ministry Growth and Budget Model Project",
 prompt="""Plan the growth and the budget of a small ministry or school program. Show all work, label each part, and write complete sentences. Colossians 3:23 says, And whatsoever ye do, do it heartily, as to the Lord, and not unto men; A good steward plans carefully and serves with all his heart. Use the algebra you learned in this course to plan yours.

Part 1: Functions and Transformations. A program serves f(x) = 40 + 5x families after x months. Its cost in dollars is g(x) = 12x + 100 per month for supplies. Find the composition g(f(x)) and explain what it measures. Find the inverse of f and tell what the inverse tells the director. Describe how the graph of h(x) = f(x minus 3) + 10 compares with the graph of f.

Part 2: Quadratic Planning. The weekly income from an event is I(p) = negative 5p squared + 100p, where p is the ticket price in dollars. Find the vertex and explain what it means. Find the prices at which the income is 320 dollars, using the quadratic formula or factoring. Solve the inequality negative 5p squared + 100p is at least 320 and explain what the solution says about pricing.

Part 3: Polynomials. A storage box is made from a 12 inch by 18 inch sheet by cutting a square of side x from each corner. Write the volume V(x) as a polynomial in standard form and state the domain. Use technology to estimate the value of x that gives the largest volume. Divide x cubed minus 7x plus 6 by x minus 1 and use the quotient to find all of its zeros.

Part 4: Radical, Rational and Absolute Value Models. The speed of a car in miles per hour that left a skid mark of d feet is modeled by s = the square root of (24d). Find the speed when d = 150 and the skid length when s = 30. A volunteer finishes a mailing in 6 hours and a helper in 3 hours. Write and solve a rational equation for the time working together. Solve |2x minus 5| less than 9 and explain what it could mean for a temperature that must stay within 9 degrees of 5 degrees.

Part 5: Exponential Growth and Stewardship. A ministry fund starts with $4000 and earns 6 percent interest compounded monthly. Write the model, find the balance after 8 years, and use logarithms to find how long it takes to reach $8000. Compare it with simple interest at the same rate and with continuous compounding for 8 years. Then give two sentences of advice about saving, giving and avoiding unnecessary debt.

Part 6: Systems and Data. A ministry sells two kinds of kits with a profit of 3 dollars on kit A and 2 dollars on kit B. Time limits the total to at most 6 kits and materials limit 2x + y to at most 8, with x kits of type A and y kits of type B. Graph the feasible region, list the vertices and find the best profit. Then decide whether the data (0, 3), (1, 6), (2, 11), (3, 18) fit a linear, quadratic or exponential model, write the model and predict the value at x = 5.

Part 7: Reflection. In at least 100 words, explain how the mathematics of this course can help you serve with excellence, plan with wisdom and give an honest account of your results. Mention at least two function families you used and one limit of a model.""",
 rubric="""200 points. Part 1, functions and transformations: 24 points. Part 2, quadratic planning: 32 points. Part 3, polynomials: 30 points. Part 4, radical, rational and absolute value models: 32 points. Part 5, exponential growth and stewardship: 32 points. Part 6, systems and data: 32 points. Part 7, reflection: 12 points. Clear organization, correct units and complete sentences: 6 points. A score of 140 or above is passing."""
)

FINAL_EXAM = [
 ("If f(x) = 2x + 1 and g(x) = x squared, then f(g(3)) equals:", ["19", "49", "10", "28"], 0, "g(3) = 9, and f(9) = 2(9) + 1 = 19."),
 ("The inverse of f(x) = 3x minus 6 is:", ["f inverse of x = (x + 6)/3", "f inverse of x = 3x + 6", "f inverse of x = (x minus 6)/3", "f inverse of x = 1/(3x minus 6)"], 0, "Swap x and y and solve: x = 3y minus 6 gives y = (x + 6)/3."),
 ("(4 minus 3i)(2 + i) equals:", ["11 minus 2i", "5 minus 2i", "8 minus 3i", "11 + 2i"], 0, "8 + 4i minus 6i minus 3i squared = 8 minus 2i + 3 = 11 minus 2i."),
 ("The solutions of x squared + 2x + 5 = 0 are:", ["negative 1 plus or minus 2i", "1 plus or minus 2i", "negative 1 plus or minus 4i", "negative 2 plus or minus i"], 0, "The quadratic formula gives (negative 2 plus or minus the square root of negative 16)/2 = negative 1 plus or minus 2i."),
 ("The vertex of f(x) = x squared minus 6x + 5 is:", ["(3, negative 4)", "(3, 4)", "(negative 3, negative 4)", "(6, 5)"], 0, "The axis is x = 3 and f(3) = 9 minus 18 + 5 = negative 4."),
 ("When f(x) = x cubed minus 4x squared + 2x minus 7 is divided by x minus 3, the remainder is:", ["negative 10", "10", "negative 7", "3"], 0, "By the Remainder Theorem, f(3) = 27 minus 36 + 6 minus 7 = negative 10."),
 ("The end behavior of f(x) = negative 2x to the fourth + x squared minus 3 is:", ["Both ends fall", "Both ends rise", "Falls left, rises right", "Rises left, falls right"], 0, "Even degree with a negative leading coefficient falls on both ends."),
 ("32 to the power 3/5 equals:", ["8", "6", "96", "2"], 0, "The fifth root of 32 is 2, and 2 cubed is 8."),
 ("Solving the square root of (2x + 9) = x + 3 and checking gives:", ["x = 0 only", "x = 0 and x = negative 4", "x = negative 4 only", "No solution"], 0, "Squaring gives x squared + 4x = 0, but x = negative 4 fails the check."),
 ("The solution of |2x + 1| at most 7 is:", ["negative 4 at most x at most 3", "x at most negative 4 or x at least 3", "negative 3 at most x at most 4", "x at most 3"], 0, "Negative 7 at most 2x + 1 at most 7 gives negative 4 at most x at most 3."),
 ("The horizontal asymptote of f(x) = (3x minus 6)/(x + 1) is:", ["y = 3", "y = negative 1", "y = 0", "y = negative 6"], 0, "The degrees are equal, so the asymptote is the ratio of leading coefficients, 3."),
 ("The solution of 5/(x minus 2) = 3/(x + 2) is:", ["x = negative 8", "x = 8", "x = 2", "x = negative 2"], 0, "Cross multiplying gives 5x + 10 = 3x minus 6, so x = negative 8."),
 ("The solution of 7 to the power x = 50, to the nearest thousandth, is:", ["2.010", "7.143", "1.945", "3.912"], 0, "x = (log 50)/(log 7), about 2.010."),
 ("$3000 invested at 4 percent compounded quarterly for 5 years grows to about:", ["$3660.57", "$3600.00", "$3649.97", "$3666.67"], 0, "A = 3000(1.01) to the 20, about $3660.57."),
 ("For P = 2x + 3y over the region with vertices (0, 0), (7, 0), (4, 3) and (0, 5), the maximum value of P is:", ["17", "14", "15", "0"], 0, "P(4, 3) = 8 + 9 = 17, which exceeds 14 and 15."),
]
