"""Algebra 2, Unit 3: Polynomials. Florida B.E.S.T. Mathematics Algebra 2 standards."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."

UNIT3 = dict(
 title="Unit 3: Polynomial Expressions, Equations and Functions",
 std="MA.912.AR.1.3, MA.912.AR.1.5, MA.912.AR.1.6, MA.912.AR.1.8, MA.912.AR.6.1, MA.912.AR.6.5",
 topics=[
 dict(t="3.1 Operations with Polynomials", std="MA.912.AR.1.3",
 body="""A polynomial is a sum of terms of the form a times x to a whole number power. Its degree is the highest power of x, and its leading coefficient is the coefficient of that term.

Add and subtract by combining like terms.
(2x squared minus 3x + 4) + (x squared + 5x minus 7) = 3x squared + 2x minus 3.
(2x squared minus 3x + 4) minus (x squared + 5x minus 7) = x squared minus 8x + 11. Distribute the minus sign to every term of the second polynomial.

Multiply with the distributive property, multiplying every term by every term.
(x + 3)(x squared minus 2x + 5) = x cubed minus 2x squared + 5x + 3x squared minus 6x + 15 = x cubed + x squared minus x + 15.

Special products to know:
Difference of squares: (a minus b)(a + b) = a squared minus b squared. Example: (2x minus 5)(2x + 5) = 4x squared minus 25.
Perfect square: (a + b) squared = a squared + 2ab + b squared.
Cube of a binomial: (x + 4) cubed = x cubed + 12x squared + 48x + 64.
Sum of cubes: a cubed + b cubed = (a + b)(a squared minus ab + b squared). Example: x cubed + 8 = (x + 2)(x squared minus 2x + 4).
Difference of cubes: a cubed minus b cubed = (a minus b)(a squared + ab + b squared).

The binomial pattern: the coefficients of (x minus 2) to the fourth power come from row four of Pascal's triangle, 1, 4, 6, 4, 1. So (x minus 2) to the fourth = x to the fourth minus 8x cubed + 24x squared minus 32x + 16.

Closure: adding, subtracting or multiplying polynomials always gives another polynomial, so polynomials are closed under these operations.

Your task: (1) Multiply (3x squared + x minus 2)(x minus 4). (2) Subtract (5x cubed minus 2x + 1) minus (2x cubed + x squared minus 6). (3) Factor x cubed minus 27 and state the degree of your product from part 1.""",
 script="""Welcome to Unit 3. Listen, polynomials are the workhorse expressions of algebra. A polynomial is a sum of terms, each one a number times x to a whole number power. The degree is the highest power, and the leading coefficient is the number on that highest term.

Now watch this. To add or subtract, combine like terms. Two x squared minus three x plus four, plus x squared plus five x minus seven, gives three x squared plus two x minus three. When you subtract, distribute the minus sign to every term of the second polynomial. That gives x squared minus eight x plus eleven.

To multiply, multiply every term by every term. x plus three, times x squared minus two x plus five, becomes x cubed minus two x squared plus five x, plus three x squared minus six x plus fifteen. Combine, and you have x cubed plus x squared minus x plus fifteen.

Look at the special products, because they save time. A difference of squares gives a squared minus b squared. So two x minus five, times two x plus five, is four x squared minus twenty five. A perfect square gives a squared plus two a b plus b squared. And a binomial cubed follows a pattern. x plus four, cubed, is x cubed plus twelve x squared plus forty eight x plus sixty four. The sum of cubes factors as a plus b, times a squared minus a b plus b squared. So x cubed plus eight is x plus two, times x squared minus two x plus four.

The coefficients of a binomial raised to a power come from Pascal's triangle. For the fourth power the row is one, four, six, four, one. So x minus two, to the fourth, is x to the fourth, minus eight x cubed, plus twenty four x squared, minus thirty two x, plus sixteen.

Remember that adding, subtracting or multiplying polynomials always gives another polynomial. We call that closure.

Your task today. Multiply three x squared plus x minus two, by x minus four. Subtract five x cubed minus two x plus one, minus the quantity two x cubed plus x squared minus six. And factor x cubed minus twenty seven. Take the four question check when you finish.

Good builders know the pattern before they cut the board. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("The degree of 4x cubed minus 7x squared + 2 is:", ["3", "4", "2", "7"], 0, "The degree is the highest power of x, which is 3."),
 ("(2x squared minus 3x + 4) minus (x squared + 5x minus 7) equals:", ["x squared minus 8x + 11", "x squared + 2x minus 3", "x squared minus 8x minus 3", "3x squared + 2x minus 3"], 0, "Distribute the minus sign: 2x squared minus x squared = x squared, negative 3x minus 5x = negative 8x, and 4 + 7 = 11."),
 ("(2x minus 5)(2x + 5) equals:", ["4x squared minus 25", "4x squared + 25", "4x squared minus 10x + 25", "2x squared minus 25"], 0, "A product of conjugates is a difference of squares: 4x squared minus 25."),
 ("x cubed + 8 factors as:", ["(x + 2)(x squared minus 2x + 4)", "(x + 2)(x squared + 2x + 4)", "(x + 2) cubed", "(x minus 2)(x squared + 2x + 4)"], 0, "The sum of cubes pattern gives (a + b)(a squared minus ab + b squared) with a = x and b = 2."),
 ]),
 dict(t="3.2 Polynomial Division, the Remainder Theorem and the Factor Theorem", std="MA.912.AR.1.5, MA.912.AR.1.6",
 body="""To divide a polynomial by x minus c, use synthetic division. Write the coefficients of the polynomial (use 0 for a missing power) and use c as the divisor.

Example: divide x cubed minus 2x squared minus 5x + 6 by x minus 3. Use c = 3 with coefficients 1, negative 2, negative 5, 6.
Bring down 1. Multiply 3 times 1 = 3 and add to negative 2 to get 1. Multiply 3 times 1 = 3 and add to negative 5 to get negative 2. Multiply 3 times negative 2 = negative 6 and add to 6 to get 0.
The quotient is x squared + x minus 2 and the remainder is 0.

Example with a remainder: divide x cubed + 2x squared minus x + 5 by x + 1, so c = negative 1. The quotient is x squared + x minus 2 and the remainder is 7.

The Remainder Theorem: when a polynomial f(x) is divided by x minus c, the remainder is f(c). Check: f(negative 1) = negative 1 + 2 + 1 + 5 = 7, which matches.

The Factor Theorem: x minus c is a factor of f(x) if and only if f(c) = 0.
Since the first example has remainder 0, x minus 3 is a factor, and x cubed minus 2x squared minus 5x + 6 = (x minus 3)(x squared + x minus 2) = (x minus 3)(x minus 1)(x + 2). The zeros are 3, 1 and negative 2.

Use the Remainder Theorem to evaluate quickly: if f(x) = 2x cubed minus x squared + 4x minus 5, then f(2) = 16 minus 4 + 8 minus 5 = 15, which is the remainder when f(x) is divided by x minus 2.

Long division works for any divisor. It follows the same steps as long division of numbers: divide the leading terms, multiply, subtract, bring down, and repeat.

Your task: (1) Use synthetic division to divide 2x cubed minus 3x squared + x + 6 by x + 1. (2) Use the Remainder Theorem to find f(3) when f(x) = x cubed minus 4x squared + 2x minus 7. (3) Show that x minus 2 is a factor of x cubed minus x squared minus 4x + 4.""",
 script="""Now we divide polynomials. Listen, when the divisor has the form x minus c, there is a shortcut called synthetic division. Write the coefficients of the polynomial, and use zero for any missing power. Then use c as the divisor.

Watch this. Divide x cubed minus two x squared minus five x plus six by x minus three. The coefficients are one, negative two, negative five, six, and c is three. Bring down the one. Three times one is three, and negative two plus three is one. Three times one is three, and negative five plus three is negative two. Three times negative two is negative six, and six plus negative six is zero. The quotient is x squared plus x minus two, and the remainder is zero.

Look at one with a remainder. Divide x cubed plus two x squared minus x plus five by x plus one. Here c is negative one. The quotient is x squared plus x minus two, and the remainder is seven.

Now the Remainder Theorem. It says the remainder when you divide f of x by x minus c is simply f of c. Check it. f of negative one is negative one plus two plus one plus five, which is seven. It matches.

The Factor Theorem follows right behind. x minus c is a factor of f of x exactly when f of c equals zero. In our first example the remainder was zero, so x minus three is a factor. The polynomial equals x minus three, times x squared plus x minus two, which factors further into x minus three, x minus one, and x plus two. The zeros are three, one, and negative two.

You can also evaluate quickly. If f of x is two x cubed minus x squared plus four x minus five, then f of two is sixteen minus four plus eight minus five, which is fifteen.

Long division works for any divisor, and it follows the same steps you used with numbers. Divide the leading terms, multiply, subtract, bring down, and repeat.

Your task today. Divide two x cubed minus three x squared plus x plus six by x plus one using synthetic division. Find f of three when f of x is x cubed minus four x squared plus two x minus seven. And show that x minus two is a factor of x cubed minus x squared minus four x plus four. Take the four question check when you finish.

A zero remainder tells you the pieces fit perfectly. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("When x cubed minus 2x squared minus 5x + 6 is divided by x minus 3, the remainder is:", ["0", "3", "6", "negative 6"], 0, "Synthetic division with c = 3 ends in a remainder of 0."),
 ("The Remainder Theorem says that dividing f(x) by x minus c leaves a remainder of:", ["f(c)", "f(negative c)", "c", "f(0)"], 0, "The remainder equals the value of the function at c."),
 ("If f(c) = 0, then:", ["x minus c is a factor of f(x)", "x + c is a factor of f(x)", "c is the leading coefficient", "f(x) has degree c"], 0, "By the Factor Theorem, f(c) = 0 means x minus c is a factor."),
 ("For f(x) = 2x cubed minus x squared + 4x minus 5, the value f(2) is:", ["15", "5", "21", "11"], 0, "f(2) = 16 minus 4 + 8 minus 5 = 15."),
 ]),
 dict(t="3.3 Solving Polynomial Equations", std="MA.912.AR.1.8, MA.912.AR.6.1",
 body="""To solve a polynomial equation, set one side to 0, factor, and use the zero product property: if a product equals 0, one of its factors equals 0.

Common factor and difference of squares: x cubed minus 4x = 0 gives x(x minus 2)(x + 2) = 0, so x = 0, 2 or negative 2.

Factoring by grouping: x cubed + 3x squared minus 4x minus 12 = 0. Group as x squared(x + 3) minus 4(x + 3) = (x + 3)(x squared minus 4) = (x + 3)(x minus 2)(x + 2). The solutions are negative 3, 2 and negative 2.

Quadratic form: x to the fourth minus 5x squared + 4 = 0. Let u = x squared, so u squared minus 5u + 4 = 0, giving (u minus 1)(u minus 4) = 0. Then x squared = 1 or 4, so x = plus or minus 1 or plus or minus 2.

The Rational Root Theorem: if a polynomial with integer coefficients has a rational root p/q in lowest terms, then p divides the constant term and q divides the leading coefficient.
Example: 2x cubed minus 3x squared minus 11x + 6 = 0. The possible values of p are plus or minus 1, 2, 3, 6 and q are 1, 2. Test x = 3: 54 minus 27 minus 33 + 6 = 0, so 3 is a root. Synthetic division by x minus 3 gives the quotient 2x squared + 3x minus 2 = (2x minus 1)(x + 2). The roots are 3, 1/2 and negative 2.

Complex roots: x cubed minus 1 = 0 factors as (x minus 1)(x squared + x + 1). The quadratic formula gives x = (negative 1 plus or minus i times the square root of 3)/2. So there are three roots in all: one real and two complex.

Always check your solutions by substituting, and be sure that each one makes sense in the real situation.

Your task: (1) Solve x cubed minus 2x squared minus 9x + 18 = 0 by grouping. (2) Solve x to the fourth minus 13x squared + 36 = 0. (3) List the possible rational roots of x cubed minus 6x squared + 11x minus 6 = 0 and find one root.""",
 script="""Now we solve polynomial equations. Listen to the plan. Set one side to zero, factor, and use the zero product property. If a product equals zero, then one of the factors equals zero.

Watch this. x cubed minus four x equals zero. Pull out an x, and you have x times x minus two times x plus two. The solutions are zero, two and negative two.

Look at factoring by grouping. x cubed plus three x squared minus four x minus twelve. Group the first two terms and the last two terms. You get x squared times x plus three, minus four times x plus three. Factor out x plus three, and you get x plus three, times x squared minus four, which is x plus three, x minus two, x plus two. The solutions are negative three, two and negative two.

Some equations hide a quadratic. x to the fourth minus five x squared plus four. Let u equal x squared. Then u squared minus five u plus four factors as u minus one, times u minus four. So x squared is one or four, and x is plus or minus one, or plus or minus two.

Now the Rational Root Theorem. If a polynomial with integer coefficients has a rational root p over q in lowest terms, then p divides the constant term and q divides the leading coefficient. Try two x cubed minus three x squared minus eleven x plus six. The possible p values are one, two, three and six, and the q values are one and two. Test x equals three. Fifty four, minus twenty seven, minus thirty three, plus six, equals zero. So three is a root. Synthetic division leaves two x squared plus three x minus two, which factors as two x minus one, times x plus two. The roots are three, one half, and negative two.

Roots can be complex too. x cubed minus one factors as x minus one, times x squared plus x plus one. The quadratic formula gives negative one plus or minus i times the square root of three, all over two. That is three roots in all.

Always check by substituting, and make sure each answer fits the real situation.

Your task today. Solve x cubed minus two x squared minus nine x plus eighteen by grouping. Solve x to the fourth minus thirteen x squared plus thirty six. And list the possible rational roots of x cubed minus six x squared plus eleven x minus six, then find one root. Take the four question check when you finish.

Good work factors out what is hidden. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("The solutions of x cubed minus 4x = 0 are:", ["0, 2 and negative 2", "2 and negative 2 only", "0 and 4", "4 and negative 4"], 0, "Factor as x(x minus 2)(x + 2) = 0."),
 ("To solve x to the fourth minus 5x squared + 4 = 0, a helpful substitution is:", ["u = x squared", "u = x cubed", "u = 2x", "u = x + 4"], 0, "With u = x squared the equation becomes the quadratic u squared minus 5u + 4 = 0."),
 ("By the Rational Root Theorem, a rational root p/q of 2x cubed minus 3x squared minus 11x + 6 has p dividing:", ["6", "2", "11", "3x"], 0, "p divides the constant term 6, and q divides the leading coefficient 2."),
 ("The equation x cubed minus 1 = 0 has:", ["One real root and two complex roots", "Three real roots", "Only complex roots", "Two real roots and one complex root"], 0, "It factors as (x minus 1)(x squared + x + 1), and the quadratic has complex roots."),
 ]),
 dict(t="3.4 Graphs of Polynomial Functions", std="MA.912.AR.1.8, MA.912.AR.6.5",
 body="""The graph of a polynomial is smooth and continuous. Its shape is controlled by the degree, the leading coefficient and the zeros.

End behavior depends on the degree and the sign of the leading coefficient.
Even degree, positive leading coefficient: both ends rise.
Even degree, negative leading coefficient: both ends fall.
Odd degree, positive leading coefficient: falls on the left and rises on the right.
Odd degree, negative leading coefficient: rises on the left and falls on the right.

Zeros and multiplicity: if x minus c appears as a factor m times, then c is a zero of multiplicity m.
Odd multiplicity: the graph crosses the x axis at c.
Even multiplicity: the graph touches the x axis at c and turns around.

Example: f(x) = (x + 1) squared (x minus 2). The degree is 3 with a positive leading coefficient, so the graph falls on the left and rises on the right. It touches the x axis at negative 1 (multiplicity 2) and crosses at 2. The y intercept is f(0) = (1)(negative 2) = negative 2.

The Fundamental Theorem of Algebra: a polynomial of degree n has exactly n zeros in the complex numbers, counting multiplicity. A polynomial with real coefficients that has the complex zero a + bi must also have the zero a minus bi.

Writing a polynomial from its zeros: zeros 1, 2 + i and 2 minus i give f(x) = (x minus 1)(x minus (2 + i))(x minus (2 minus i)) = (x minus 1)(x squared minus 4x + 5) = x cubed minus 5x squared + 9x minus 5.

Turning points: a polynomial of degree n has at most n minus 1 turning points.

Modeling: an open box is made from a 12 by 18 inch sheet by cutting squares of side x from each corner. The volume is V(x) = x(12 minus 2x)(18 minus 2x), with 0 < x < 6. A graphing tool shows the largest volume near x = 2.35 inches.

Your task: (1) Describe the end behavior of f(x) = negative 2x to the fourth + x squared minus 3. (2) For f(x) = x squared (x minus 3)(x + 2), list the zeros with their multiplicities and tell whether the graph crosses or touches at each. (3) Write a polynomial with real coefficients whose zeros are 3 and 1 minus 2i.""",
 script="""Now we study the graphs of polynomial functions. Listen, these graphs are smooth, continuous curves, and three things control their shape: the degree, the leading coefficient and the zeros.

First, end behavior. With an even degree and a positive leading coefficient, both ends rise. With an even degree and a negative leading coefficient, both ends fall. With an odd degree and a positive leading coefficient, the graph falls on the left and rises on the right. With an odd degree and a negative leading coefficient, it rises on the left and falls on the right.

Now watch this. Zeros and multiplicity. If x minus c appears m times as a factor, then c is a zero of multiplicity m. If m is odd, the graph crosses the x axis at c. If m is even, the graph touches the axis and turns around.

Look at f of x equals x plus one, squared, times x minus two. The degree is three with a positive leading coefficient, so the graph falls on the left and rises on the right. It touches the x axis at negative one, and it crosses at two. The y intercept is one times negative two, which is negative two.

The Fundamental Theorem of Algebra says a polynomial of degree n has exactly n zeros in the complex numbers, counting multiplicity. And if a polynomial has real coefficients and the complex zero a plus b i, then a minus b i is a zero as well. Complex zeros come in conjugate pairs.

So we can write a polynomial from its zeros. Take zeros one, two plus i, and two minus i. The function is x minus one, times x squared minus four x plus five. Multiply it out, and you get x cubed minus five x squared plus nine x minus five.

A polynomial of degree n has at most n minus one turning points.

Look at a real use. Cut squares of side x from the corners of a twelve by eighteen inch sheet and fold up an open box. The volume is x times twelve minus two x, times eighteen minus two x, and x must be between zero and six. A graphing tool shows the largest volume near two point three five inches.

Your task today. Describe the end behavior of negative two x to the fourth plus x squared minus three. List the zeros of x squared times x minus three times x plus two, with multiplicities, and tell whether the graph crosses or touches. And write a polynomial with real coefficients whose zeros are three and one minus two i. Take the four question check when you finish.

Know where you are headed and where you will turn. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("A polynomial of even degree with a positive leading coefficient has end behavior:", ["Both ends rise", "Both ends fall", "Falls left, rises right", "Rises left, falls right"], 0, "Even degree with a positive leading coefficient rises on both ends."),
 ("At a zero of even multiplicity, the graph:", ["Touches the x axis and turns around", "Crosses the x axis", "Has a vertical asymptote", "Has no intercept"], 0, "Even multiplicity means the graph touches the axis and turns."),
 ("A polynomial of degree 5 has exactly how many complex zeros, counting multiplicity?", ["5", "4", "6", "Cannot be determined"], 0, "The Fundamental Theorem of Algebra says a degree n polynomial has n zeros."),
 ("If a polynomial with real coefficients has the zero 2 + i, it must also have the zero:", ["2 minus i", "negative 2 minus i", "negative 2 + i", "i"], 0, "Complex zeros of real polynomials come in conjugate pairs."),
 ]),
 ],
 assess=dict(t="Assessment 3: Polynomial Expressions, Equations and Graphs",
 prompt="""Complete all parts, showing your work and explaining your reasoning.

Part A: Multiply (3x squared + x minus 2)(x minus 4). Subtract (5x cubed minus 2x + 1) minus (2x cubed + x squared minus 6). Factor x cubed minus 27 completely over the real numbers.

Part B: Use synthetic division to divide 2x cubed minus 3x squared + x + 6 by x + 1 and state the quotient and remainder. Use the Remainder Theorem to find f(3) when f(x) = x cubed minus 4x squared + 2x minus 7. Show that x minus 2 is a factor of x cubed minus x squared minus 4x + 4 and factor it completely.

Part C: Solve x cubed minus 2x squared minus 9x + 18 = 0 by grouping. Solve x to the fourth minus 13x squared + 36 = 0. List the possible rational roots of x cubed minus 6x squared + 11x minus 6 = 0, then find all of its roots.

Part D: Describe the end behavior of f(x) = negative 2x to the fourth + x squared minus 3. For g(x) = x squared (x minus 3)(x + 2), list each zero with its multiplicity, tell whether the graph crosses or touches at each, and find the y intercept. Write a polynomial with real coefficients whose zeros are 3 and 1 minus 2i.

Part E: An open box is made from a 12 inch by 18 inch sheet by cutting a square of side x from each corner. Write the volume as a function of x, state the domain, and use a graphing tool to estimate the value of x that gives the largest volume.

Part F: In at least 60 words, explain how the pattern of a polynomial, its zeros and its factors, is like building a plan from smaller parts. Connect your answer to Proverbs 24:3, which says, Through wisdom is an house builded; and by understanding it is established:""",
 rubric="""100 points. Part A, operations and factoring: 14 points. Part B, division, remainder and factor: 18 points. Part C, solving polynomial equations: 22 points. Part D, graph features and writing a polynomial: 20 points. Part E, modeling with volume: 14 points. Part F, written reflection: 8 points. Clear work and complete sentences: 4 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 3: Understanding Builds the House",
 prompt="""A polynomial can be taken apart into factors, and the factors reveal the zeros, which tell us where a graph meets the x axis. Write a post of at least 120 words that (1) explains in your own words why finding the factors of a polynomial helps you understand its graph, (2) gives an example from building, business or ministry where breaking a big problem into smaller parts helped, (3) tells why it is wise to check an answer by substituting it back, and (4) connects your answer to Proverbs 3:13, which says, Happy is the man that findeth wisdom, and the man that getteth understanding. Then write a respectful reply of at least 40 words to another student, or answer this question: How do the end behavior and the zeros together help you sketch a polynomial? Keep your language clean and your tone kind."""),
 unit_quiz=[
 ("The product (x + 3)(x squared minus 2x + 5) equals:", ["x cubed + x squared minus x + 15", "x cubed minus x squared + x + 15", "x cubed + 5x squared minus x + 15", "x cubed + x squared + x + 15"], 0, "Multiplying every term gives x cubed + x squared minus x + 15."),
 ("x cubed minus 27 factors as:", ["(x minus 3)(x squared + 3x + 9)", "(x minus 3)(x squared minus 3x + 9)", "(x minus 3) cubed", "(x + 3)(x squared minus 3x + 9)"], 0, "The difference of cubes pattern gives (a minus b)(a squared + ab + b squared)."),
 ("When x cubed + 2x squared minus x + 5 is divided by x + 1, the remainder is:", ["7", "5", "negative 7", "0"], 0, "By the Remainder Theorem the remainder is f(negative 1) = 7."),
 ("If x minus 4 is a factor of f(x), then:", ["f(4) = 0", "f(negative 4) = 0", "f(0) = 4", "f(4) = 4"], 0, "The Factor Theorem says f(c) = 0 when x minus c is a factor."),
 ("The solutions of x to the fourth minus 5x squared + 4 = 0 are:", ["plus or minus 1 and plus or minus 2", "1 and 4 only", "plus or minus 1 only", "plus or minus 4 and plus or minus 1"], 0, "With u = x squared, u = 1 or 4, so x = plus or minus 1 or plus or minus 2."),
 ("A polynomial of odd degree with a negative leading coefficient:", ["Rises on the left and falls on the right", "Falls on the left and rises on the right", "Falls on both ends", "Rises on both ends"], 0, "Odd degree and negative leading coefficient rises left and falls right."),
 ("The zero 3 of f(x) = (x minus 3) squared (x + 1) has multiplicity:", ["2", "1", "3", "0"], 0, "The factor x minus 3 appears twice, so the multiplicity is 2 and the graph touches the axis."),
 ("A polynomial with real coefficients and zeros 3 and 1 minus 2i must also have the zero:", ["1 + 2i", "negative 1 + 2i", "negative 3", "2i"], 0, "Complex zeros come in conjugate pairs, so 1 + 2i is also a zero."),
 ])
