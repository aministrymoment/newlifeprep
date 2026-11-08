"""Algebra 2, Unit 2: Quadratics and Complex Numbers. Florida B.E.S.T. Mathematics Algebra 2 standards."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."

UNIT2 = dict(
 title="Unit 2: Quadratics and Complex Numbers",
 std="MA.912.NSO.2.1, MA.912.AR.3.2, MA.912.AR.3.3, MA.912.AR.3.4, MA.912.AR.3.8, MA.912.AR.3.9, MA.912.AR.3.10",
 topics=[
 dict(t="2.1 Complex Numbers", std="MA.912.NSO.2.1",
 body="""Some quadratic equations, such as x squared + 1 = 0, have no real solution. To solve them we extend the real numbers by defining the imaginary unit i, where i = the square root of negative 1 and i squared = negative 1.

A complex number has the form a + bi, where a and b are real numbers. The number a is the real part and b is the imaginary part.

Addition and subtraction: combine like parts.
(3 + 2i) + (1 minus 4i) = 4 minus 2i.
(5 + 6i) minus (2 + 9i) = 3 minus 3i.

Multiplication: use the distributive property and replace i squared with negative 1.
(2 + 3i)(1 minus i) = 2 minus 2i + 3i minus 3i squared = 2 + i + 3 = 5 + i.

Conjugates: the conjugate of a + bi is a minus bi. The product of conjugates is a real number:
(3 + 2i)(3 minus 2i) = 9 minus 4i squared = 9 + 4 = 13.

Division: multiply the top and bottom by the conjugate of the bottom.
(5 + i)/(2 minus i) = (5 + i)(2 + i)/((2 minus i)(2 + i)) = (10 + 5i + 2i + i squared)/5 = (9 + 7i)/5.

Powers of i repeat in a cycle of four: i, negative 1, negative i, 1. To find i to the 27th power, divide 27 by 4. The remainder is 3, so i to the 27th power = negative i.

Square roots of negative numbers: the square root of negative 36 = 6i. The square root of negative 20 = 2 times i times the square root of 5.

Your task: (1) Simplify (4 minus 3i)(2 + i). (2) Divide (6 + 2i) by (1 minus i). (3) Simplify i to the 50th power and the square root of negative 49.""",
 script="""Welcome to Unit 2. Listen, some equations have no answer among the real numbers. Take x squared plus one equals zero. No real number squared gives negative one. So mathematicians made a new number. We call it i, the imaginary unit, and we define i as the square root of negative one. That means i squared equals negative one.

A complex number looks like a plus b i, where a and b are real numbers. The a is the real part and the b is the imaginary part.

Now watch this. To add or subtract, combine like parts. Three plus two i, plus one minus four i, gives four minus two i. To multiply, use the distributive property and replace i squared with negative one. Two plus three i, times one minus i, gives two, minus two i, plus three i, minus three i squared. That is two plus i plus three, which is five plus i.

Look at conjugates. The conjugate of a plus b i is a minus b i. When you multiply conjugates, the imaginary part disappears. Three plus two i, times three minus two i, equals nine minus four i squared, which is nine plus four, which is thirteen. We use that fact to divide. To divide five plus i by two minus i, multiply the top and bottom by two plus i. The bottom becomes five. The top becomes ten, plus five i, plus two i, plus i squared, which is nine plus seven i. So the answer is nine plus seven i, all over five.

Powers of i follow a cycle of four. i, negative one, negative i, one, and then it repeats. To find i to the twenty seventh, divide twenty seven by four. The remainder is three, so the answer is negative i.

And square roots of negative numbers. The square root of negative thirty six is six i.

Your task today. Simplify four minus three i, times two plus i. Divide six plus two i by one minus i. And simplify i to the fiftieth power and the square root of negative forty nine. Take the four question check when you finish.

God can bring a solution out of what looks impossible. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("The value of i squared is:", ["negative 1", "1", "i", "negative i"], 0, "By definition, i squared equals negative 1."),
 ("(3 + 2i) + (1 minus 4i) equals:", ["4 minus 2i", "4 + 6i", "2 + 6i", "4 + 2i"], 0, "Combine real parts 3 + 1 = 4 and imaginary parts 2i minus 4i = negative 2i."),
 ("(2 + 3i)(1 minus i) equals:", ["5 + i", "2 minus 3i", "5 minus i", "2 + i"], 0, "2 minus 2i + 3i minus 3i squared = 2 + i + 3 = 5 + i."),
 ("(3 + 2i)(3 minus 2i) equals:", ["13", "5", "9 minus 4", "9 + 4i"], 0, "The product of conjugates is 9 minus 4i squared = 9 + 4 = 13."),
 ]),
 dict(t="2.2 Solving Quadratic Equations over the Complex Numbers", std="MA.912.AR.3.2",
 body="""A quadratic equation has the form ax squared + bx + c = 0 with a not equal to 0. There are four main solving methods.

1. Factoring. Example: x squared minus 5x + 6 = 0 factors as (x minus 2)(x minus 3) = 0, so x = 2 or x = 3.
Example: 2x squared + 3x minus 5 = 0 factors as (2x + 5)(x minus 1) = 0, so x = negative 5/2 or x = 1.

2. Square roots. Example: (x minus 4) squared = 25 gives x minus 4 = plus or minus 5, so x = 9 or x = negative 1.

3. Completing the square. Example: x squared + 6x + 2 = 0. Move 2: x squared + 6x = negative 2. Add 9 to both sides: (x + 3) squared = 7. So x = negative 3 plus or minus the square root of 7.

4. The quadratic formula: x = (negative b plus or minus the square root of (b squared minus 4ac)) / (2a).
Example: x squared minus 4x + 13 = 0 has a = 1, b = negative 4, c = 13. The discriminant is b squared minus 4ac = 16 minus 52 = negative 36. Then x = (4 plus or minus the square root of negative 36)/2 = (4 plus or minus 6i)/2 = 2 plus or minus 3i.

The discriminant b squared minus 4ac tells the type of solutions:
Positive: two different real solutions.
Zero: one repeated real solution.
Negative: two complex nonreal solutions that are conjugates of each other.

Write and solve: A rectangle's length is 3 more than its width, and its area is 40 square units. Then w(w + 3) = 40, so w squared + 3w minus 40 = 0, which factors as (w + 8)(w minus 5) = 0. The width is 5 and the length is 8. The solution w = negative 8 is rejected because a width cannot be negative.

Your task: (1) Solve x squared minus 8x + 15 = 0 by factoring. (2) Solve x squared + 2x + 5 = 0 with the quadratic formula. (3) Find the discriminant of 3x squared minus 2x + 4 = 0 and state the type of solutions.""",
 script="""Now we solve quadratic equations in every way you will ever need. A quadratic has the form a x squared plus b x plus c equals zero. Listen, there are four main methods.

Method one, factoring. x squared minus five x plus six equals zero becomes the quantity x minus two times the quantity x minus three equals zero. So x is two or three. Another, two x squared plus three x minus five factors into two x plus five times x minus one, so x is negative five halves or one.

Method two, square roots. If the quantity x minus four, squared, equals twenty five, then x minus four is plus or minus five, so x is nine or negative one.

Method three, completing the square. Take x squared plus six x plus two equals zero. Move the two over. x squared plus six x equals negative two. Add nine to both sides, and you have the quantity x plus three, squared, equals seven. So x equals negative three plus or minus the square root of seven.

Method four, the quadratic formula. x equals negative b, plus or minus the square root of b squared minus four a c, all over two a. Now watch this. Try x squared minus four x plus thirteen equals zero. The discriminant, b squared minus four a c, is sixteen minus fifty two, which is negative thirty six. Then x equals four, plus or minus the square root of negative thirty six, over two. That is four plus or minus six i, over two, which is two plus or minus three i.

The discriminant tells the story before you solve. Positive means two different real solutions. Zero means one repeated real solution. Negative means two complex solutions that are conjugates of each other.

Look at a real situation. A rectangle's length is three more than its width, and the area is forty. So w times w plus three equals forty. That gives w squared plus three w minus forty equals zero, which factors as w plus eight times w minus five. The width is five and the length is eight. We reject negative eight, because a width cannot be negative.

Your task today. Solve x squared minus eight x plus fifteen by factoring. Solve x squared plus two x plus five with the quadratic formula. And find the discriminant of three x squared minus two x plus four and state the type of solutions. Take the four question check when you finish.

Check every answer against reality, and keep the ones that make sense. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("The solutions of x squared minus 5x + 6 = 0 are:", ["x = 2 or x = 3", "x = negative 2 or x = negative 3", "x = 1 or x = 6", "x = 5 or x = 1"], 0, "The equation factors as (x minus 2)(x minus 3) = 0."),
 ("The discriminant of x squared minus 4x + 13 = 0 is:", ["negative 36", "36", "68", "negative 68"], 0, "b squared minus 4ac = 16 minus 52 = negative 36."),
 ("A negative discriminant means the quadratic equation has:", ["Two complex nonreal solutions", "Two equal real solutions", "Two different real solutions", "No solutions of any kind"], 0, "A negative discriminant gives a pair of complex conjugate solutions."),
 ("Solving x squared + 6x + 2 = 0 by completing the square gives x =", ["negative 3 plus or minus the square root of 7", "3 plus or minus the square root of 7", "negative 3 plus or minus the square root of 11", "negative 6 plus or minus the square root of 2"], 0, "(x + 3) squared = 7, so x = negative 3 plus or minus the square root of 7."),
 ]),
 dict(t="2.3 Graphing and Writing Quadratic Functions", std="MA.912.AR.3.4, MA.912.AR.3.8",
 body="""A quadratic function can be written in three forms.
Standard form: f(x) = ax squared + bx + c.
Vertex form: f(x) = a(x minus h) squared + k, with vertex (h, k).
Factored form: f(x) = a(x minus r)(x minus s), with x intercepts r and s.

Key features: the vertex, the axis of symmetry, the x intercepts, the y intercept, and whether the parabola opens up (a positive) or down (a negative).

In standard form, the axis of symmetry is x = negative b/(2a), and the vertex y value is found by substituting.

Example: f(x) = x squared minus 6x + 5. The axis is x = 6/2 = 3. Then f(3) = 9 minus 18 + 5 = negative 4, so the vertex is (3, negative 4). The x intercepts come from (x minus 1)(x minus 5) = 0, so x = 1 and x = 5. The y intercept is 5.

Writing a quadratic from a graph: A parabola has vertex (2, 3) and passes through (0, negative 1). Start with f(x) = a(x minus 2) squared + 3. Substitute (0, negative 1): negative 1 = a(4) + 3, so 4a = negative 4 and a = negative 1. The function is f(x) = negative (x minus 2) squared + 3.

Writing a quadratic from x intercepts: Roots at 2 and 7 and a y intercept of 28 give f(x) = a(x minus 2)(x minus 7). Using x = 0, 28 = a(14), so a = 2.

Modeling: The height of a ball is h(t) = negative 16t squared + 64t + 5 feet after t seconds. The maximum occurs at t = 64/32 = 2 seconds, and h(2) = negative 64 + 128 + 5 = 69 feet. The ball lands when h(t) = 0. By the quadratic formula, t = (64 plus or minus the square root of 4416)/32. The positive value is about 4.08 seconds.

Your task: (1) Find the vertex, axis, x intercepts and y intercept of f(x) = x squared minus 4x minus 5. (2) Write the quadratic with vertex (1, 4) that passes through (3, 0). (3) A ball has height h(t) = negative 16t squared + 48t + 4. Find the maximum height and when it occurs.""",
 script="""Now we draw and write quadratic functions. A quadratic can be written in three forms. Standard form, f of x equals a x squared plus b x plus c. Vertex form, f of x equals a times the quantity x minus h, squared, plus k, where the vertex is h, k. And factored form, f of x equals a times x minus r times x minus s, where r and s are the x intercepts.

Listen to the key features. The vertex, the axis of symmetry, the x intercepts, the y intercept, and whether the parabola opens up or down. If a is positive it opens up. If a is negative it opens down.

Now watch this. In standard form, the axis of symmetry is x equals negative b over two a. Take x squared minus six x plus five. The axis is x equals three. Plug in three, nine minus eighteen plus five, equals negative four. So the vertex is three, negative four. Factor to get x minus one times x minus five, so the x intercepts are one and five. The y intercept is five.

To write a quadratic from a graph, suppose the vertex is two, three and it passes through zero, negative one. Start with a times the quantity x minus two, squared, plus three. Substitute x equals zero and y equals negative one. Negative one equals four a plus three. So four a is negative four, and a is negative one. The function is negative times the quantity x minus two, squared, plus three.

Look at modeling. A ball's height is h of t equals negative sixteen t squared plus sixty four t plus five. The maximum happens at t equals sixty four over thirty two, which is two seconds. The height then is negative sixty four, plus one twenty eight, plus five, which is sixty nine feet. To find when it lands, set the height to zero and use the quadratic formula. The positive solution is about four point zero eight seconds.

Your task today. Find the vertex, axis, x intercepts and y intercept of x squared minus four x minus five. Write the quadratic with vertex one, four that passes through three, zero. And for a ball with height negative sixteen t squared plus forty eight t plus four, find the maximum height and when it happens. Take the four question check when you finish.

Every throw rises to a peak and returns, and wise people plan for both. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("The vertex of f(x) = x squared minus 6x + 5 is:", ["(3, negative 4)", "(3, 4)", "(negative 3, negative 4)", "(6, 5)"], 0, "The axis is x = 3, and f(3) = 9 minus 18 + 5 = negative 4."),
 ("A parabola with vertex (2, 3) that passes through (0, negative 1) has a equal to:", ["negative 1", "1", "negative 4", "4"], 0, "Negative 1 = a(4) + 3 gives a = negative 1."),
 ("For h(t) = negative 16t squared + 64t + 5, the maximum height is:", ["69 feet", "64 feet", "5 feet", "37 feet"], 0, "The maximum occurs at t = 2, and h(2) = 69."),
 ("The axis of symmetry of f(x) = ax squared + bx + c is:", ["x = negative b/(2a)", "x = b/(2a)", "x = negative b/a", "x = c/a"], 0, "The axis of symmetry is x = negative b divided by 2a."),
 ]),
 dict(t="2.4 Quadratic Inequalities", std="MA.912.AR.3.3, MA.912.AR.3.9, MA.912.AR.3.10",
 body="""A quadratic inequality compares a quadratic expression with 0, using less than, greater than, at most or at least.

One variable. Steps:
1. Move everything to one side so the other side is 0.
2. Find the roots (the boundary points).
3. Mark the roots on a number line and test a value in each section.
4. Write the solution as an inequality or in interval form.

Example: (x minus 3)(x + 2) > 0. The roots are 3 and negative 2. Test x = 0: (negative 3)(2) = negative 6, which is not greater than 0. Test x = 5: (2)(7) = 14, which works. Test x = negative 4: (negative 7)(negative 2) = 14, which works. The solution is x less than negative 2 or x greater than 3.

Example: x squared minus 4 is at most 0. The roots are negative 2 and 2. The parabola is at or below the x axis between them, so the solution is negative 2 to 2, including both ends.

Example: x squared minus x minus 6 is at least 0. Factor as (x minus 3)(x + 2). The solution is x at most negative 2 or x at least 3.

Two variables. The solution set of y > x squared minus 2x minus 3 is a region of the plane.
1. Graph the boundary parabola y = x squared minus 2x minus 3. Use a dashed curve for greater than or less than, and a solid curve for at most or at least.
2. Test a point not on the curve. The origin (0, 0) gives 0 > negative 3, which is true, so shade the side that contains the origin, which is the region above the parabola.

Writing an inequality from a graph: a solid parabola y = x squared with the region below it shaded is described by y at most x squared.

Your task: (1) Solve x squared minus 2x minus 8 is at least 0. (2) Solve x squared + 3x minus 10 < 0. (3) Describe how to graph y is at most x squared minus 1, including the boundary style and the shading.""",
 script="""Today we solve quadratic inequalities. A quadratic inequality compares a quadratic expression with zero, using greater than, less than, at least or at most.

Listen to the steps for one variable. Step one, move everything to one side so the other side is zero. Step two, find the roots. Those are the boundary points. Step three, mark them on a number line and test a value in each section. Step four, write the solution.

Look at this one. The quantity x minus three, times the quantity x plus two, is greater than zero. The roots are three and negative two. Test x equals zero. Negative three times two is negative six, which is not greater than zero. Test x equals five. Two times seven is fourteen, which works. Test x equals negative four. Negative seven times negative two is fourteen, which works. So the solution is x less than negative two, or x greater than three.

Another. x squared minus four is at most zero. The roots are negative two and two. The parabola sits at or below the x axis between the roots, so the solution is negative two to two, including both ends.

Now watch this. Two variables. Consider y greater than x squared minus two x minus three. First, graph the boundary parabola. Use a dashed curve for greater than or less than, and a solid curve for at least or at most. Next, test a point that is not on the curve. The origin gives zero greater than negative three, which is true. So shade the side with the origin, which is the region above the parabola.

You can also write an inequality from a graph. A solid parabola y equals x squared with the region below it shaded is described by y at most x squared.

Your task today. Solve x squared minus two x minus eight is at least zero. Solve x squared plus three x minus ten is less than zero. And describe how to graph y at most x squared minus one, including the boundary style and the shading. Take the four question check when you finish.

Test everything, hold fast to what is good. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("The solution of (x minus 3)(x + 2) > 0 is:", ["x < negative 2 or x > 3", "negative 2 < x < 3", "x > 3 only", "x < negative 2 only"], 0, "The expression is positive outside the roots negative 2 and 3."),
 ("The solution of x squared minus 4 at most 0 is:", ["negative 2 to 2, including both ends", "x at most negative 2 or x at least 2", "x at most 2 only", "x at least negative 2 only"], 0, "The parabola is at or below the x axis between the roots negative 2 and 2."),
 ("To graph y > x squared minus 2x minus 3, the boundary curve should be:", ["Dashed, with the region above shaded", "Solid, with the region below shaded", "Solid, with the region above shaded", "Dashed, with the region below shaded"], 0, "Strict inequalities use a dashed curve, and the origin test shows the region above is the solution."),
 ("To decide which side of a boundary to shade, you:", ["Test a point not on the boundary", "Always shade above", "Always shade below", "Shade the inside only"], 0, "A test point shows whether that side satisfies the inequality."),
 ]),
 ],
 assess=dict(t="Assessment 2: Complex Numbers and Quadratics",
 prompt="""Complete all parts, showing your work and explaining your reasoning.

Part A: Simplify (4 minus 3i)(2 + i). Divide (6 + 2i) by (1 minus i) and write the answer in the form a + bi. Simplify i to the 50th power.

Part B: Solve x squared minus 8x + 15 = 0 by factoring. Solve 3x squared + x minus 2 = 0 by factoring. Solve x squared + 2x + 5 = 0 by the quadratic formula and write the complex solutions. State the discriminant of each equation and what it tells you.

Part C: For f(x) = x squared minus 4x minus 5, find the vertex, axis of symmetry, x intercepts and y intercept, and tell whether the parabola opens up or down. Then write the quadratic function whose graph has vertex (1, 4) and passes through (3, 0).

Part D: A ball is thrown so that its height in feet after t seconds is h(t) = negative 16t squared + 48t + 4. Find the maximum height and when it occurs. Then find, to the nearest hundredth of a second, when the ball hits the ground.

Part E: Solve x squared minus 2x minus 8 is at least 0 and write the solution as inequalities. Describe how to graph y is at most x squared minus 1, including the boundary style and the shading.

Part F: In at least 60 words, explain how a quadratic model can help a ministry or school plan, such as choosing the best price or the best size of a space. Connect your answer to Ecclesiastes 3:1, which says, To every thing there is a season, and a time to every purpose under the heaven.""",
 rubric="""100 points. Part A, complex arithmetic: 12 points. Part B, three solutions with discriminants: 22 points. Part C, features and function from vertex: 18 points. Part D, projectile model: 18 points. Part E, inequality and graph description: 14 points. Part F, written reflection: 10 points. Clear work and complete sentences: 6 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 2: Seasons, Peaks and Purpose",
 prompt="""Quadratic functions describe things that rise to a peak and then fall, such as a thrown ball, a fountain of water or the profit of a small event. Write a post of at least 120 words that (1) explains in your own words what the vertex of a parabola tells us in a real situation, (2) describes an example from sports, business or ministry where a maximum or a minimum matters, (3) tells why it is wise to check whether a solution makes sense in the real world, as when a negative width is rejected, and (4) connects your answer to Ecclesiastes 3:1, which says, To every thing there is a season, and a time to every purpose under the heaven. Then write a respectful reply of at least 40 words to another student, or answer this question: What does the discriminant tell us before we solve an equation? Keep your language clean and your tone kind."""),
 unit_quiz=[
 ("The imaginary unit i is defined so that i squared equals:", ["negative 1", "1", "0", "i"], 0, "By definition i squared equals negative 1."),
 ("(1 + 2i)(1 minus 2i) equals:", ["5", "negative 3", "1 minus 4i", "1 + 4i"], 0, "The product of conjugates is 1 + 4 = 5."),
 ("The value of i to the 27th power is:", ["negative i", "i", "1", "negative 1"], 0, "27 divided by 4 leaves a remainder of 3, and i cubed is negative i."),
 ("The solutions of x squared + 4 = 0 are:", ["2i and negative 2i", "2 and negative 2", "4i and negative 4i", "No solutions"], 0, "x squared = negative 4, so x = plus or minus 2i."),
 ("A quadratic with discriminant 0 has:", ["One repeated real solution", "Two different real solutions", "Two complex solutions", "No solutions"], 0, "A discriminant of 0 gives exactly one repeated real solution."),
 ("The vertex of f(x) = (x minus 2) squared + 7 is:", ["(2, 7)", "(negative 2, 7)", "(2, negative 7)", "(7, 2)"], 0, "In vertex form a(x minus h) squared + k, the vertex is (h, k)."),
 ("The solution of x squared minus 9 < 0 is:", ["negative 3 < x < 3", "x < negative 3 or x > 3", "x < 3 only", "x > negative 3 only"], 0, "The parabola is below the x axis between the roots negative 3 and 3."),
 ("When graphing y is at least x squared, the boundary curve is:", ["Solid, with the region above shaded", "Dashed, with the region above shaded", "Solid, with the region below shaded", "Dashed, with the region below shaded"], 0, "At least uses a solid curve, and the test point (0, 1) shows the region above is the solution."),
 ])
