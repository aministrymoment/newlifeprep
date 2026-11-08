"""Algebra 2, Unit 6: Systems, Modeling and Review."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."

UNIT6 = dict(
 title="Unit 6: Systems, Data Modeling and Review",
 std="MA.912.AR.9.2, MA.912.AR.9.3, MA.912.AR.9.5, MA.912.AR.9.7, MA.912.DP.2.8, MA.912.DP.2.9, MA.912.F.1.7",
 topics=[
 dict(t="6.1 Systems of Three Linear Equations", std="MA.912.AR.9.2",
 body="""A system of three linear equations in three variables asks for the ordered triple (x, y, z) that makes all three equations true. Geometrically each equation is a plane, and the solution is where the three planes meet.

Method: use elimination to reduce three variables to two, then to one.

Example:
x + y + z = 6
2x minus y + z = 3
x + 2y minus z = 2

Step 1: Add the first and third equations to eliminate z: 2x + 3y = 8.
Step 2: Add the second and third equations to eliminate z: 3x + y = 5.
Step 3: Solve the two variable system. From 3x + y = 5, y = 5 minus 3x. Substitute: 2x + 3(5 minus 3x) = 8, so 2x + 15 minus 9x = 8, then negative 7x = negative 7 and x = 1. Then y = 2.
Step 4: Substitute into the first equation: 1 + 2 + z = 6, so z = 3.
Check in the second: 2 minus 2 + 3 = 3. Check in the third: 1 + 4 minus 3 = 2. The solution is (1, 2, 3).

Special cases: if elimination produces a false statement such as 0 = 5, the system is inconsistent and has no solution. If it produces a true statement such as 0 = 0, the system is dependent and has infinitely many solutions.

Application: A school sells student, adult and senior tickets. Write one equation for the number of tickets, one for the income and one for a relationship between ticket types, then solve the system.

Your task: (1) Solve x + y + z = 9, 2x minus y + z = 5, x + 2y minus z = 4. (2) Check your answer in all three equations. (3) Explain what it means geometrically if a system is inconsistent.""",
 script="""Welcome to Unit 6. Listen, many real situations have more than one unknown, so we solve systems. A system of three linear equations in three variables asks for the ordered triple x, y, z that makes all three equations true. Each equation is a plane, and the solution is where the planes meet.

Watch this. The method is elimination. Use two equations to eliminate one variable, then use another pair to eliminate the same variable. That leaves a system with two variables. Solve it, then back substitute.

Take these three. x plus y plus z equals six. Two x minus y plus z equals three. x plus two y minus z equals two. Add the first and third to eliminate z, and you get two x plus three y equals eight. Add the second and third to eliminate z, and you get three x plus y equals five. From the second of those, y equals five minus three x. Substitute into the first. Two x plus fifteen minus nine x equals eight. So negative seven x equals negative seven, and x is one. Then y is two. Put those in the first original equation, and one plus two plus z equals six, so z is three.

Always check in the other equations. In the second, two minus two plus three is three. In the third, one plus four minus three is two. The solution is one, two, three.

Look at special cases. If elimination gives a false statement like zero equals five, the system is inconsistent and has no solution. The planes never meet at a common point. If it gives a true statement like zero equals zero, the system is dependent, with infinitely many solutions.

You can use this for ticket sales, mixtures, budgets and more. Write one equation for the counts, one for the income, and one for a relationship between the types, then solve.

Your task today. Solve x plus y plus z equals nine, two x minus y plus z equals five, and x plus two y minus z equals four. Check your answer in all three equations. And explain what it means geometrically if a system is inconsistent. Take the four question check when you finish.

Several truths held together make one clear answer. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("The solution of a system of three linear equations is an:", ["Ordered triple (x, y, z)", "Ordered pair (x, y)", "Single number", "Inequality"], 0, "Three variables give an ordered triple."),
 ("The solution of x + y + z = 6, 2x minus y + z = 3, x + 2y minus z = 2 is:", ["(1, 2, 3)", "(2, 2, 2)", "(3, 2, 1)", "(1, 3, 2)"], 0, "Elimination gives x = 1, y = 2, z = 3."),
 ("If elimination produces the false statement 0 = 5, the system is:", ["Inconsistent, with no solution", "Dependent, with infinitely many solutions", "Consistent, with one solution", "Quadratic"], 0, "A false statement means the equations cannot all be true together."),
 ("If elimination produces the true statement 0 = 0, the system is:", ["Dependent, with infinitely many solutions", "Inconsistent", "Solved with exactly one solution", "Impossible"], 0, "A true statement means the equations share infinitely many solutions."),
 ]),
 dict(t="6.2 Systems with Linear and Nonlinear Equations", std="MA.912.AR.9.3",
 body="""A system can include a nonlinear equation such as a parabola or a circle. The solutions are the points where the graphs intersect, and the number of solutions can be 0, 1 or 2 (or more with higher degree curves).

Substitution is the usual method.

Line and parabola: y = x + 2 and y = x squared.
Set the right sides equal: x squared = x + 2, so x squared minus x minus 2 = 0 and (x minus 2)(x + 1) = 0. Then x = 2 or x = negative 1. The points are (2, 4) and (negative 1, 1).

Line and circle: x squared + y squared = 25 and y = x + 1.
Substitute: x squared + (x + 1) squared = 25, so 2x squared + 2x + 1 = 25 and 2x squared + 2x minus 24 = 0, which simplifies to x squared + x minus 12 = 0. Then (x + 4)(x minus 3) = 0 and x = negative 4 or x = 3. The points are (negative 4, negative 3) and (3, 4). Check (3, 4): 9 + 16 = 25 and 4 = 3 + 1.

Number of solutions: a line may cross a parabola twice, touch it once (the line is tangent) or miss it. The discriminant of the combined quadratic tells which: positive means two points, zero means one point and negative means no real points.

Graphing check: graph both equations with technology and find the intersections. Compare with your algebra.

Modeling: A company's cost is C(x) = 2x + 50 and its revenue is R(x) = negative x squared + 14x. Setting cost equal to revenue gives the break even points: negative x squared + 14x = 2x + 50, so x squared minus 12x + 50 = 0. The discriminant is 144 minus 200 = negative 56, so there is no break even point for this model.

Your task: (1) Solve y = 2x minus 1 and y = x squared minus 4. (2) Solve x squared + y squared = 10 and y = 3x. (3) Explain how the discriminant tells how many times a line meets a parabola.""",
 script="""Now we solve systems that include a curve. Listen, the solutions are the points where the graphs intersect, and the number of solutions can be zero, one, two, or more for higher degree curves. Substitution is the usual method.

Watch this. A line and a parabola. y equals x plus two, and y equals x squared. Set the right sides equal. x squared equals x plus two, so x squared minus x minus two equals zero. That factors as x minus two, times x plus one. So x is two or negative one. The points are two, four and negative one, one.

Look at a line and a circle. x squared plus y squared equals twenty five, and y equals x plus one. Substitute for y. x squared plus the quantity x plus one, squared, equals twenty five. That becomes two x squared plus two x plus one equals twenty five, then two x squared plus two x minus twenty four equals zero. Divide by two, and you have x squared plus x minus twelve equals zero. That factors as x plus four, times x minus three. The points are negative four, negative three, and three, four. Check three, four. Nine plus sixteen is twenty five, and four equals three plus one.

The discriminant helps. After you combine into one quadratic, a positive discriminant means two intersection points. Zero means one point, a tangent line. Negative means the graphs miss each other.

Use technology to graph both equations and find the intersections, then compare with your algebra.

Now a business model. Cost is two x plus fifty. Revenue is negative x squared plus fourteen x. Set them equal, and you get x squared minus twelve x plus fifty equals zero. The discriminant is one forty four minus two hundred, which is negative fifty six. There is no break even point in this model, and that tells a leader to change the plan.

Your task today. Solve y equals two x minus one with y equals x squared minus four. Solve x squared plus y squared equals ten with y equals three x. And explain how the discriminant tells how many times a line meets a parabola. Take the four question check when you finish.

Where paths cross, wise people take note. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("The solutions of y = x + 2 and y = x squared are:", ["(2, 4) and (negative 1, 1)", "(2, 4) only", "(1, 3) and (negative 2, 0)", "(4, 2) and (1, negative 1)"], 0, "Solving x squared = x + 2 gives x = 2 or x = negative 1."),
 ("The line y = x + 1 meets the circle x squared + y squared = 25 at:", ["(3, 4) and (negative 4, negative 3)", "(4, 3) and (negative 3, negative 4)", "(3, 4) only", "No points"], 0, "Substitution gives x = 3 or x = negative 4."),
 ("If the combined quadratic has a negative discriminant, the line and the parabola:", ["Do not intersect", "Intersect once", "Intersect twice", "Are identical"], 0, "A negative discriminant means no real intersection points."),
 ("A line that touches a parabola at exactly one point is called:", ["Tangent", "Parallel", "Perpendicular", "An asymptote"], 0, "A discriminant of zero gives one point, a tangent line."),
 ]),
 dict(t="6.3 Systems of Inequalities and Optimization", std="MA.912.AR.9.5, MA.912.AR.9.7",
 body="""A system of inequalities is solved by graphing each inequality and shading the region where all of them are true. That overlap is called the feasible region.

Steps:
1. Graph each boundary line, dashed for strict inequalities and solid otherwise.
2. Test a point to decide which side to shade.
3. Find the overlap and its corner points (vertices).

Linear programming uses a feasible region to find the best value of an objective function. The maximum or minimum always occurs at a vertex.

Example: A ministry sells two kinds of items. Let x and y be the numbers sold. The constraints are:
x is at least 0, y is at least 0.
x + y is at most 6 (time).
2x + y is at most 8 (materials).
The objective is to maximize profit P = 3x + 2y.

Vertices: (0, 0), (4, 0), (0, 6) and the intersection of x + y = 6 and 2x + y = 8. Subtracting gives x = 2, then y = 4, so the vertex is (2, 4).
P at (0, 0) = 0.
P at (4, 0) = 12.
P at (0, 6) = 12.
P at (2, 4) = 6 + 8 = 14.
The maximum profit is 14 at (2, 4).

Interpreting the answer: sell 2 of the first item and 4 of the second item. Always check that the point makes sense, since you cannot sell a fraction of an item if items are whole.

Nonlinear systems: shading works the same way for a parabola and a line, such as y at least x squared and y at most x + 2. Test a point to choose the shading and find the intersection points by solving.

Your task: (1) Graph x at least 0, y at least 0, x + 2y at most 10 and x + y at most 7, and list the vertices. (2) Find the maximum of P = 2x + 3y over that region. (3) Explain why the best value of the objective function is found at a vertex.""",
 script="""Now we graph systems of inequalities and use them to make decisions. Listen, to solve a system of inequalities, graph each inequality and shade the region where all of them are true. That overlap is the feasible region.

Here are the steps. Graph each boundary line, dashed for strict inequalities and solid otherwise. Test a point to see which side to shade. Then find the overlap and its corner points.

Now watch this. Linear programming uses the feasible region to find the best value of an objective function, and the maximum or minimum always occurs at a vertex. Consider a ministry selling two items. Let x and y be the numbers sold. The constraints are that x and y are at least zero, x plus y is at most six because of time, and two x plus y is at most eight because of materials. We want to maximize profit, three x plus two y.

Find the vertices. Zero, zero. Four, zero. Zero, six. And the intersection of x plus y equals six with two x plus y equals eight. Subtract the equations, and x is two. Then y is four. So the vertex is two, four.

Compute the profit at each vertex. At zero, zero it is zero. At four, zero it is twelve. At zero, six it is twelve. At two, four it is six plus eight, which is fourteen. The maximum profit is fourteen at two, four.

Interpret it. Sell two of the first item and four of the second. Always check that the answer makes sense. If items must be whole, the point must have whole numbers.

Shading also works with nonlinear inequalities. For y at least x squared and y at most x plus two, test a point to choose the side, and solve to find where the boundaries meet.

Your task today. Graph x at least zero, y at least zero, x plus two y at most ten, and x plus y at most seven. List the vertices. Find the maximum of two x plus three y over the region. And explain why the best value is found at a vertex. Take the four question check when you finish.

Good planning respects the limits and uses them well. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("The overlap of the solution regions of all inequalities in a system is called the:", ["Feasible region", "Asymptote", "Vertex of a parabola", "Boundary line"], 0, "The feasible region satisfies every constraint."),
 ("In linear programming, the maximum or minimum occurs at:", ["A vertex of the feasible region", "The center of the region", "The origin only", "Any interior point"], 0, "The best value of a linear objective occurs at a corner point."),
 ("For P = 3x + 2y with vertices (0, 0), (4, 0), (2, 4) and (0, 6), the maximum is:", ["14", "12", "18", "0"], 0, "P(2, 4) = 6 + 8 = 14, the greatest value."),
 ("A strict inequality such as y > 2x + 1 has a boundary line that is:", ["Dashed", "Solid", "Curved", "Vertical"], 0, "Strict inequalities do not include the boundary, so it is dashed."),
 ]),
 dict(t="6.4 Modeling with Data and Course Review", std="MA.912.DP.2.8, MA.912.DP.2.9, MA.912.F.1.7",
 body="""To choose a model for data, look at how the y values change for equal steps in x.
Constant first differences: a linear model.
Constant second differences: a quadratic model.
Constant ratios: an exponential model.

Quadratic example: (0, 3), (1, 6), (2, 11), (3, 18). First differences are 3, 5, 7. Second differences are 2, 2. The model is y = x squared + 2x + 3, which can be confirmed with a quadratic regression. Check x = 2: 4 + 4 + 3 = 11.

Regression with technology: enter the data, choose linear, quadratic or exponential regression, and read the equation. Graph the data and the curve together and check how closely the curve follows the points. A residual is the difference between an actual value and the value from the model, and small residuals that are scattered randomly suggest a good fit.

Average rate of change of f from a to b is (f(b) minus f(a))/(b minus a). For f(x) = x squared + 2x + 3 from x = 1 to x = 3 it is (18 minus 6)/2 = 6. Compare rates: a linear function has a constant rate, while a quadratic rate changes and an exponential rate grows or shrinks by a factor.

Interpolation estimates within the data, and extrapolation predicts beyond it and is less reliable.

Review of the course function families:
Quadratic: parabola, vertex and zeros.
Polynomial: end behavior and zeros.
Radical: starts at a point, domain limits.
Rational: asymptotes and holes.
Absolute value: V shape.
Exponential and logarithmic: growth, decay and inverse.
Each family can be shifted, stretched or reflected with f(x minus h) + k and a times f(x).

Your task: (1) Decide which model fits (0, 2), (1, 3), (2, 6), (3, 11) and write it. (2) Find the average rate of change of your model from x = 1 to x = 3. (3) Choose two function families from this course and describe one real situation each could model.""",
 script="""Welcome to the last lesson of the course content. Today we use data to choose a model, and then we review everything. Listen, to choose a model, look at how the y values change for equal steps in x. Constant first differences mean a linear model. Constant second differences mean a quadratic model. Constant ratios mean an exponential model.

Watch this. The points are zero, three; one, six; two, eleven; three, eighteen. The first differences are three, five, seven. The second differences are two and two. So the model is quadratic, y equals x squared plus two x plus three. Check x equals two. Four plus four plus three is eleven. A quadratic regression on technology would confirm it.

For regression, enter the data, choose linear, quadratic or exponential regression, and read the equation. Graph the data together with the curve and see how closely the curve follows the points. A residual is the difference between an actual value and the model's value. Small residuals with no pattern suggest a good fit.

Now rate of change. The average rate of change of f from a to b is f of b minus f of a, over b minus a. For x squared plus two x plus three from x equals one to x equals three, that is eighteen minus six, over two, which is six. A linear function has a constant rate. A quadratic rate changes. An exponential rate grows or shrinks by a factor.

Interpolation estimates inside the data. Extrapolation predicts beyond it, and it is less reliable.

Look back at our families. Quadratics have a vertex and zeros. Polynomials have end behavior and zeros. Radical functions start at a point and have domain limits. Rational functions have asymptotes and holes. Absolute value makes a V. Exponential and logarithmic functions describe growth, decay and their inverses. Each can be shifted, stretched or reflected.

Your task today. Decide which model fits zero, two; one, three; two, six; three, eleven, and write it. Find the average rate of change of your model from x equals one to x equals three. And choose two function families from this course and describe one real situation each could model. Take the four question check when you finish, and then prepare for the final assessment.

You have grown in understanding, and now you are ready to use it. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("Data whose second differences are constant fit:", ["A quadratic model", "A linear model", "An exponential model", "An absolute value model"], 0, "Constant second differences identify a quadratic model."),
 ("The average rate of change of f from a to b is:", ["(f(b) minus f(a))/(b minus a)", "f(b) + f(a)", "(b minus a)/(f(b) minus f(a))", "f(b)/f(a)"], 0, "It is the change in output divided by the change in input."),
 ("For f(x) = x squared + 2x + 3, the average rate of change from x = 1 to x = 3 is:", ["6", "12", "2", "9"], 0, "(18 minus 6)/(3 minus 1) = 6."),
 ("Predicting a value beyond the range of the data is called:", ["Extrapolation", "Interpolation", "Regression", "Residual"], 0, "Extrapolation goes beyond the data and is less reliable."),
 ]),
 ],
 assess=dict(t="Assessment 6: Systems, Data Models and Course Review",
 prompt="""Complete all parts, showing your work and explaining your reasoning.

Part A: Solve the system x + y + z = 9, 2x minus y + z = 5, x + 2y minus z = 4. Check your answer in all three equations. Explain what an inconsistent system and a dependent system look like when you use elimination.

Part B: Solve y = 2x minus 1 and y = x squared minus 4. Solve x squared + y squared = 10 and y = 3x. Explain how the discriminant tells how many times a line meets a parabola.

Part C: Graph x at least 0, y at least 0, x + 2y at most 10 and x + y at most 7, and list the vertices. Find the maximum of P = 2x + 3y over the region and say what the answer means if x and y are numbers of items made.

Part D: Decide which model fits the data (0, 2), (1, 3), (2, 6), (3, 11) and write it. Find the average rate of change of your model from x = 1 to x = 3. Then use your model to predict the value at x = 5 and say whether that is interpolation or extrapolation.

Part E: Choose any three function families from this course (quadratic, polynomial, radical, rational, absolute value, exponential or logarithmic). For each, give its general form, one key feature of its graph, and a real situation it could model.

Part F: In at least 60 words, explain how studying mathematics can help a person serve others with order and care. Connect your answer to 1 Corinthians 14:40, which says, Let all things be done decently and in order.""",
 rubric="""100 points. Part A, three variable system: 18 points. Part B, linear and nonlinear systems: 18 points. Part C, inequalities and optimization: 20 points. Part D, data modeling and rate of change: 18 points. Part E, function families: 16 points. Part F, written reflection: 6 points. Clear work and complete sentences: 4 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 6: Two Are Better Than One",
 prompt="""A system of equations brings two or more truths together to find one answer, and a good model brings data together to describe the world. Write a post of at least 120 words that (1) explains in your own words what it means to solve a system, (2) describes a situation from school, business or ministry in which two or more conditions had to be met together, such as a budget and a time limit, (3) tells why we should be honest about the limits of a model when we use it to make decisions, and (4) connects your answer to Ecclesiastes 4:9, which says, Two are better than one; because they have a good reward for their labour. Then write a respectful reply of at least 40 words to another student, or answer this question: How do you decide whether data fit a linear, quadratic or exponential model? Keep your language clean and your tone kind."""),
 unit_quiz=[
 ("The solution of the system x + y + z = 9, 2x minus y + z = 5, x + 2y minus z = 4 is:", ["(2, 3, 4)", "(3, 3, 3)", "(4, 3, 2)", "(2, 4, 3)"], 0, "Substituting (2, 3, 4) makes all three equations true."),
 ("A system of equations with no solution is called:", ["Inconsistent", "Dependent", "Linear", "Quadratic"], 0, "An inconsistent system has no solution."),
 ("The line y = 2x minus 1 meets the parabola y = x squared minus 4 at:", ["(3, 5) and (negative 1, negative 3)", "(3, 5) only", "(1, 1) and (negative 3, negative 7)", "No points"], 0, "x squared minus 2x minus 3 = 0 gives x = 3 or x = negative 1."),
 ("A line meets a parabola in exactly one point when the discriminant of the combined equation is:", ["0", "Positive", "Negative", "Undefined"], 0, "A zero discriminant gives one repeated solution, a tangent line."),
 ("The maximum of a linear objective function over a feasible region occurs at:", ["A vertex", "An interior point", "The midpoint of an edge only", "Infinity"], 0, "The best value of a linear function over a polygon occurs at a vertex."),
 ("Data with a constant ratio between y values fit:", ["An exponential model", "A linear model", "A quadratic model", "A rational model"], 0, "A constant ratio identifies exponential change."),
 ("The model y = x squared + 2 fits the data (0, 2), (1, 3), (2, 6), (3, 11). Its value at x = 5 is:", ["27", "12", "17", "37"], 0, "5 squared + 2 = 27."),
 ("Predicting inside the range of the data is called:", ["Interpolation", "Extrapolation", "Elimination", "Substitution"], 0, "Interpolation estimates within the data and is generally more reliable."),
 ])
