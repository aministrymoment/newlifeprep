"""Algebra 2, Unit 1: Functions, Transformations and Inverses. Florida B.E.S.T. Mathematics Algebra 2 standards."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."

UNIT1 = dict(
 title="Unit 1: Functions, Transformations and Inverses",
 std="MA.912.AR.1.1, MA.912.F.1.1, MA.912.F.1.7, MA.912.F.1.9, MA.912.F.2.2, MA.912.F.2.3, MA.912.F.2.5, MA.912.F.3.2, MA.912.F.3.4, MA.912.F.3.6, MA.912.F.3.7",
 topics=[
 dict(t="1.1 Function Families and Key Features", std="MA.912.F.1.1, MA.912.F.1.7, MA.912.AR.1.1",
 body="""A function is a rule that gives exactly one output for each input. Algebra 2 studies several families of functions.

Linear: f(x) = mx + b. The graph is a line.
Quadratic: f(x) = ax squared + bx + c. The graph is a parabola.
Absolute value: f(x) = |x|. The graph is a V shape.
Square root: f(x) = the square root of x. The graph starts at a point and curves.
Exponential: f(x) = a times b to the power x. The graph grows or decays by a constant factor.
Logarithmic, rational and polynomial functions will join the list in later units.

Telling the family from a table (with equally spaced x values):
Constant first differences means linear.
Constant second differences means quadratic.
A constant ratio between neighboring y values means exponential.

Example 1: x = 0, 1, 2, 3 and y = 3, 6, 12, 24. Each y value is 2 times the one before, so the function is exponential: f(x) = 3 times 2 to the power x.
Example 2: x = 0, 1, 2, 3 and y = 1, 2, 5, 10. First differences are 1, 3, 5 and second differences are 2, 2, so the function is quadratic: f(x) = x squared + 1.

Interpreting parts of an expression: In A(t) = 500 times (1.04) to the power t, the number 500 is the starting amount, the number 1.04 is the yearly growth factor (a 4 percent increase), and t is time in years.

Comparing two functions: Let f(x) = 2x + 3 and g(x) = 3 to the power x. At x = 2, f(2) = 7 and g(2) = 9. The exponential g grows faster over time because it multiplies instead of adding the same amount.

Your task: (1) A table shows y = 2, 6, 18, 54 for x = 0, 1, 2, 3. Name the function family and write the rule. (2) In P(t) = 1200 times (0.95) to the power t, explain what 1200 and 0.95 mean. (3) Compare f(x) = 5x and g(x) = 2 to the power x at x = 3 and x = 6.""",
 script="""Welcome to Algebra 2. I am Dr. Alex L. Jenkins Sr., and I am glad you are here. Listen, this course builds on everything you learned in Algebra 1 and Geometry, and by the end you will be able to model real situations with powerful functions.

Let us begin with the big idea. A function is a rule that gives exactly one output for each input. In Algebra 2 we meet families of functions. Linear, where the graph is a line. Quadratic, where the graph is a parabola. Absolute value, which makes a V shape. Square root, which starts at a point and curves. And exponential, which grows or decays by a constant factor. Later we will add logarithmic, rational and polynomial functions.

Now watch this. How do you tell the family from a table? Make sure the x values are equally spaced. Then look at the differences. If the first differences are constant, the function is linear. If the second differences are constant, it is quadratic. And if each y value is the same multiple of the one before, it is exponential.

Look at this. x is zero, one, two, three, and y is three, six, twelve, twenty four. Each y is two times the one before. That is a constant ratio, so the function is exponential, f of x equals three times two to the x. Now another. y is one, two, five, ten. The first differences are one, three, five. The second differences are two, two. Constant second differences, so quadratic, f of x equals x squared plus one.

We also read the parts of an expression. In A of t equals five hundred times one point zero four to the t, the five hundred is the starting amount. The one point zero four is the yearly growth factor, which means a four percent increase. And t is time in years.

When we compare two functions, f of x equals two x plus three, and g of x equals three to the x. At x equals two, f is seven and g is nine. The exponential grows faster over time because it multiplies instead of adding the same amount each step.

Your task today. A table shows y equals two, six, eighteen, fifty four for x equals zero, one, two, three. Name the family and write the rule. In P of t equals twelve hundred times point nine five to the t, explain what twelve hundred and point nine five mean. And compare f of x equals five x with g of x equals two to the x, at x equals three and x equals six. Take the four question check when you finish.

God is a God of order, and patterns are His fingerprints in creation. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("A table has y values 3, 6, 12, 24 for x values 0, 1, 2, 3. The function family is:", ["Exponential", "Linear", "Quadratic", "Absolute value"], 0, "Each y value is 2 times the one before, so the ratio is constant. That is exponential."),
 ("A table has y values 1, 2, 5, 10 for x values 0, 1, 2, 3. Because the second differences are constant (2, 2), the function is:", ["Quadratic", "Linear", "Exponential", "Square root"], 0, "Constant second differences mean a quadratic function."),
 ("In A(t) = 500 times (1.04) to the power t, the number 1.04 represents:", ["The yearly growth factor", "The starting amount", "The number of years", "The final amount"], 0, "A factor of 1.04 means a 4 percent increase each year."),
 ("For f(x) = 2x + 3 and g(x) = 3 to the power x, which is larger at x = 2?", ["g, because g(2) = 9 and f(2) = 7", "f, because f(2) = 7 and g(2) = 9", "They are equal", "Neither is defined"], 0, "f(2) = 7 and g(2) = 9, so g is larger."),
 ]),
 dict(t="1.2 Even and Odd Functions and Transformations", std="MA.912.F.1.9, MA.912.F.2.2, MA.912.F.2.3, MA.912.F.2.5",
 body="""Even and odd functions:
A function is even if f(negative x) = f(x) for every x in the domain. The graph is symmetric about the y axis. Example: f(x) = x squared, because f(negative 2) = 4 = f(2).
A function is odd if f(negative x) = negative f(x). The graph is symmetric about the origin. Example: f(x) = x cubed, because f(negative 2) = negative 8 = negative f(2).
If neither rule holds, the function is neither. Example: f(x) = x squared + x. Here f(2) = 6 and f(negative 2) = 2, which is not equal to 6 or to negative 6.

Transformations of a parent function f:
g(x) = f(x) + k shifts the graph up k units (down if k is negative).
g(x) = f(x minus h) shifts the graph right h units (left if h is negative).
g(x) = a times f(x) stretches the graph vertically by a factor of a. If a is negative, the graph is also reflected across the x axis.
g(x) = f(bx) compresses the graph horizontally by a factor of 1/b when b is greater than 1.

Combined example: Start with f(x) = x squared. Then g(x) = 2(x minus 3) squared + 1 has these effects: shift right 3, stretch vertically by 2, shift up 1. The vertex moves from (0, 0) to (3, 1).

Finding a constant from a table: If f(x) values are 0, 1, 4 for x = 0, 1, 2 and g(x) values are 5, 6, 9, then each output is 5 more, so g(x) = f(x) + 5 and k = 5.

Creating a transformed function: To shift f(x) = |x| left 2 and down 4, write g(x) = |x + 2| minus 4.

Your task: (1) Decide whether f(x) = x to the 4th power minus x squared is even, odd or neither, and show a test. (2) Describe all transformations of g(x) = negative (x + 1) squared + 5 compared with x squared and give its vertex. (3) Write the function that shifts f(x) = the square root of x right 4 and up 3.""",
 script="""Now we learn to read symmetry and movement. First, symmetry. A function is even if f of negative x equals f of x for every x in the domain. The graph is a mirror image across the y axis. The function x squared is even, because f of negative two is four, the same as f of two.

A function is odd if f of negative x equals the opposite of f of x. The graph is symmetric about the origin. The function x cubed is odd, because f of negative two is negative eight, which is the opposite of f of two. If neither rule works, the function is neither. Try f of x equals x squared plus x. f of two is six and f of negative two is two. Two is not six and it is not negative six, so the function is neither even nor odd.

Now watch this. Transformations. Start with a parent function f. Adding k outside, f of x plus k, shifts the graph up k units, or down if k is negative. Subtracting h inside, f of x minus h, shifts the graph right h units. A number a multiplying the whole function stretches it vertically by a, and if a is negative the graph also flips across the x axis. And f of b x compresses the graph horizontally when b is greater than one.

Look at this combined example. Start with x squared. Then g of x equals two times the quantity x minus three, squared, plus one. The graph shifts right three, stretches vertically by two, and shifts up one. The vertex moves from zero, zero to three, one.

You can also find a constant from a table. If f has outputs zero, one, four, and g has outputs five, six, nine, every output is five more. So g of x equals f of x plus five, and k is five. And to create a transformed function, to shift absolute value of x left two and down four, write absolute value of x plus two, minus four.

Your task today. Decide whether x to the fourth minus x squared is even, odd or neither, and show a test. Describe the transformations of negative times the quantity x plus one, squared, plus five, and give the vertex. And write the function that shifts the square root of x right four and up three. Take the four question check when you finish.

A good life is built the same way, shifting, stretching and flipping our perspective until we see clearly. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("A function is even when:", ["f(negative x) = f(x) for every x in the domain", "f(negative x) = negative f(x) for every x", "f(x) = 0 for every x", "Its graph is always a line"], 0, "Even functions satisfy f(negative x) = f(x) and are symmetric about the y axis."),
 ("The function f(x) = x cubed is:", ["Odd", "Even", "Neither", "Both even and odd"], 0, "f(negative x) = negative x cubed = negative f(x), so it is odd."),
 ("Compared with f(x) = x squared, the graph of g(x) = (x minus 4) squared is shifted:", ["4 units right", "4 units left", "4 units up", "4 units down"], 0, "Subtracting h inside moves the graph right h units."),
 ("The graph of g(x) = negative f(x) is the graph of f(x):", ["Reflected across the x axis", "Reflected across the y axis", "Shifted down 1 unit", "Stretched horizontally"], 0, "A negative outside multiplier reflects the graph across the x axis."),
 ]),
 dict(t="1.3 Combining and Composing Functions", std="MA.912.F.3.2, MA.912.F.3.4",
 body="""Functions can be combined with arithmetic operations.
(f + g)(x) = f(x) + g(x)
(f minus g)(x) = f(x) minus g(x)
(f times g)(x) = f(x) times g(x)
(f / g)(x) = f(x) / g(x), with g(x) not equal to 0

The domain of a combined function is the set of x values that work in both functions. For a quotient, remove every x that makes g(x) = 0.

Example: f(x) = x + 2 and g(x) = x minus 5. Then (f / g)(x) = (x + 2)/(x minus 5), and the domain excludes x = 5.

Composition means using the output of one function as the input of another. (f of g)(x) = f(g(x)). Work from the inside out.

Example: f(x) = 2x + 1 and g(x) = x squared.
f(g(x)) = 2(x squared) + 1 = 2x squared + 1.
g(f(x)) = (2x + 1) squared = 4x squared + 4x + 1.
The two results are different, so order matters.

Evaluating: g(f(2)): f(2) = 5, then g(5) = 25.

Domain of a composition: Let f(x) = the square root of x and g(x) = x minus 3. Then f(g(x)) = the square root of (x minus 3). The expression under the root must be at least 0, so x must be at least 3. The domain is x greater than or equal to 3. The range is all values greater than or equal to 0.

Your task: (1) With f(x) = 3x minus 2 and g(x) = x squared + 1, find (f + g)(x), f(g(x)) and g(f(x)). (2) Find the domain of (f / g)(x) when f(x) = x squared and g(x) = x minus 7. (3) Find f(g(x)) and its domain when f(x) = the square root of x and g(x) = x + 6.""",
 script="""Now we put functions together. Listen, you can add, subtract, multiply and divide functions just like numbers. f plus g of x means f of x plus g of x. f times g of x means f of x times g of x. And for a quotient, f over g of x equals f of x divided by g of x, but only when g of x is not zero.

The domain of a combined function is the set of x values that work in both functions. For a quotient, remove every x that makes the bottom zero. For example, f of x equals x plus two, g of x equals x minus five. The quotient is x plus two over x minus five, and the domain excludes x equals five.

Now watch this. Composition means using the output of one function as the input of another. We write f of g of x, and we work from the inside out. Let f of x equal two x plus one, and g of x equal x squared. Then f of g of x is two times x squared, plus one. But g of f of x is the quantity two x plus one, squared, which is four x squared plus four x plus one. Different answers. Order matters in composition.

To evaluate g of f of two, first find f of two, which is five. Then g of five is twenty five.

Look at the domain of a composition. Let f of x be the square root of x, and g of x be x minus three. Then f of g of x is the square root of x minus three. The expression under the root must be at least zero, so x must be at least three. The domain is x greater than or equal to three, and the range is all values greater than or equal to zero.

Your task today. With f of x equals three x minus two and g of x equals x squared plus one, find f plus g, f of g, and g of f. Find the domain of f over g when f is x squared and g is x minus seven. And find f of g and its domain when f is the square root of x and g is x plus six. Take the four question check when you finish.

Every gift builds on another gift, and God composes our lives with care. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("If f(x) = 2x + 1 and g(x) = x squared, then f(g(x)) equals:", ["2x squared + 1", "(2x + 1) squared", "2x + x squared", "2x cubed + 1"], 0, "Replace x in f with x squared to get 2(x squared) + 1."),
 ("With f(x) = 2x + 1 and g(x) = x squared, g(f(2)) equals:", ["25", "9", "11", "5"], 0, "f(2) = 5, and then g(5) = 25."),
 ("For f(x) = x + 2 and g(x) = x minus 5, the domain of (f / g)(x) excludes x =", ["5", "2", "negative 2", "0"], 0, "The denominator x minus 5 equals 0 when x = 5."),
 ("If f(x) = the square root of x and g(x) = x minus 3, the domain of f(g(x)) is:", ["x is at least 3", "x is at least 0", "All real numbers", "x is at most 3"], 0, "The expression x minus 3 must be at least 0, so x is at least 3."),
 ]),
 dict(t="1.4 Inverse Functions", std="MA.912.F.3.6, MA.912.F.3.7",
 body="""An inverse function reverses the action of a function. If f takes 2 to 7, then the inverse takes 7 back to 2. We write the inverse of f as f inverse.

When does an inverse function exist? Only when f is one to one, which means each output comes from exactly one input. A graph tests this with the horizontal line test: if any horizontal line crosses the graph more than once, the function has no inverse as written.

Example: f(x) = x squared is not one to one on all real numbers, because f(2) = f(negative 2) = 4. If we restrict the domain to x greater than or equal to 0, then f is one to one and its inverse is f inverse(x) = the square root of x.

Finding an inverse by steps:
1. Write y = f(x).
2. Swap x and y.
3. Solve for y.
4. Write y as f inverse(x).

Example: f(x) = 3x minus 6.
y = 3x minus 6. Swap: x = 3y minus 6. Solve: 3y = x + 6, so y = (x + 6)/3. Then f inverse(x) = (x + 6)/3.

Verifying with composition: f(f inverse(x)) = 3 times (x + 6)/3 minus 6 = x + 6 minus 6 = x. Also f inverse(f(x)) = (3x minus 6 + 6)/3 = x. Both give x, so the functions are inverses.

Graphs: The graph of f inverse is the reflection of the graph of f across the line y = x. Domain and range trade places: the domain of f is the range of f inverse, and the range of f is the domain of f inverse.

Your task: (1) Find the inverse of f(x) = 2x + 10. (2) Verify your answer using composition in both orders. (3) Explain why f(x) = |x| has no inverse unless the domain is restricted, and give a restriction that works.""",
 script="""Today we learn how to undo a function. An inverse function reverses the action of a function. If f takes two to seven, the inverse takes seven back to two. We write it as f inverse.

Listen, an inverse only exists when the function is one to one. That means each output comes from exactly one input. We test this on a graph with the horizontal line test. If any horizontal line crosses the graph more than once, the function has no inverse as written.

Look at x squared. f of two and f of negative two are both four, so it is not one to one on all real numbers. But if we restrict the domain to x greater than or equal to zero, it becomes one to one, and the inverse is the square root of x.

Now watch this. Here are the steps to find an inverse. Step one, write y equals f of x. Step two, swap x and y. Step three, solve for y. Step four, write y as f inverse of x.

Let us try f of x equals three x minus six. Write y equals three x minus six. Swap, so x equals three y minus six. Solve. Three y equals x plus six, so y equals x plus six all over three. That is the inverse.

We verify using composition. f of f inverse of x is three times x plus six over three, minus six, which is x plus six minus six, which is x. And f inverse of f of x is three x minus six plus six, over three, which is x. Both give x, so they are inverses.

On a graph, the inverse is the reflection of the original across the line y equals x. And the domain and range trade places. The domain of f is the range of f inverse, and the range of f is the domain of f inverse.

Your task today. Find the inverse of f of x equals two x plus ten. Verify it using composition in both orders. And explain why absolute value of x has no inverse unless the domain is restricted, and give a restriction that works. Take the four question check when you finish.

Grace undoes what sin has done, and that is the greatest inverse of all. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("A function has an inverse function when it is:", ["One to one, passing the horizontal line test", "Even", "Quadratic", "Always a line"], 0, "Only one to one functions have inverse functions."),
 ("The inverse of f(x) = 3x minus 6 is:", ["(x + 6)/3", "3x + 6", "(x minus 6)/3", "x/3 minus 6"], 0, "Swap x and y, x = 3y minus 6, then solve to get y = (x + 6)/3."),
 ("The graphs of a function and its inverse are reflections of each other across the line:", ["y = x", "y = 0", "x = 0", "y = negative x"], 0, "Inverse graphs reflect across the line y = x."),
 ("If f(2) = 7 and f has an inverse, then f inverse of 7 equals:", ["2", "7", "14", "1/7"], 0, "The inverse takes the output 7 back to the input 2."),
 ]),
 ],
 assess=dict(t="Assessment 1: Function Families, Transformations and Inverses",
 prompt="""Complete all parts, showing your work and explaining your reasoning.

Part A: Three tables each use x = 0, 1, 2, 3. Table 1 has y = 5, 7, 9, 11. Table 2 has y = 2, 6, 18, 54. Table 3 has y = 4, 3, 4, 7. Name the function family for each table and write a rule for each. Show the differences or ratios you used.

Part B: Compare g(x) = negative 2(x + 1) squared + 5 with f(x) = x squared. Describe each transformation in order and give the vertex of g. Then decide whether f(x) = x squared is even, odd or neither, and test with x = 3.

Part C: Let f(x) = x + 3 and g(x) = 2x minus 1. Find f(g(x)) and g(f(x)). Tell whether they are equal. Find (f / g)(x) and the value of x that must be excluded from its domain.

Part D: Find the inverse of g(x) = 2x minus 1 and verify it with composition in both orders.

Part E: In at least 60 words, explain how recognizing patterns in tables and graphs helps a person plan wisely. Connect your answer to Psalm 111:2, which says, The works of the LORD are great, sought out of all them that have pleasure therein.""",
 rubric="""100 points. Part A, three families with rules and work: 24 points. Part B, transformations, vertex and even odd test: 20 points. Part C, compositions, quotient and excluded value: 22 points. Part D, inverse and verification: 20 points. Part E, written reflection: 10 points. Clear work and complete sentences: 4 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 1: Patterns That Point to a Creator",
 prompt="""Mathematicians find patterns in tables, graphs and equations. Write a post of at least 120 words that (1) explains in your own words what a function is and why a rule with exactly one output for each input is useful, (2) describes a real pattern from nature, money or daily life that grows linearly, quadratically or exponentially, (3) tells how seeing a pattern early can help a family or ministry plan wisely, and (4) connects your answer to Psalm 111:2, which says, The works of the LORD are great, sought out of all them that have pleasure therein. Then write a respectful reply of at least 40 words to another student, or answer this question: Why does composing functions in a different order change the result? Keep your language clean and your tone kind."""),
 unit_quiz=[
 ("A table where each y value is 3 times the previous y value represents which function family?", ["Exponential", "Linear", "Quadratic", "Absolute value"], 0, "A constant ratio between neighboring values means an exponential function."),
 ("A table with constant first differences represents a:", ["Linear function", "Quadratic function", "Exponential function", "Logarithmic function"], 0, "Constant first differences mean linear."),
 ("The function f(x) = x squared is:", ["Even", "Odd", "Neither", "Both even and odd"], 0, "f(negative x) = x squared = f(x), so it is even."),
 ("The graph of g(x) = f(x minus 3) + 2 is the graph of f shifted:", ["3 right and 2 up", "3 left and 2 up", "3 right and 2 down", "2 right and 3 up"], 0, "Subtracting 3 inside moves it right 3 and adding 2 outside moves it up 2."),
 ("If f(x) = x + 3 and g(x) = 2x minus 1, then f(g(x)) equals:", ["2x + 2", "2x + 5", "2x minus 4", "3x + 2"], 0, "f(g(x)) = (2x minus 1) + 3 = 2x + 2."),
 ("The domain of (f / g)(x) must exclude all x for which:", ["g(x) = 0", "f(x) = 0", "x = 0", "f(x) = g(x)"], 0, "Division by zero is not allowed, so g(x) cannot equal 0."),
 ("The inverse of f(x) = 2x + 10 is:", ["(x minus 10)/2", "(x + 10)/2", "2x minus 10", "x/2 + 10"], 0, "Swap x and y: x = 2y + 10, so y = (x minus 10)/2."),
 ("To check that two functions f and g are inverses, you should show that:", ["f(g(x)) = x and g(f(x)) = x", "f(x) = g(x)", "f(x) + g(x) = 0", "f(g(x)) = 0"], 0, "Inverse functions undo each other in both orders of composition."),
 ])
