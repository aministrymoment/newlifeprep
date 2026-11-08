"""Geometry, Unit 3: Quadrilaterals and Coordinate Proofs. Florida B.E.S.T. Mathematics Geometry standards."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."

UNIT3 = dict(
 title="Unit 3: Quadrilaterals and Coordinate Proofs",
 std="MA.912.GR.1.4, MA.912.GR.1.5, MA.912.GR.3.2",
 topics=[
 dict(t="3.1 Parallelograms and Polygon Angles", std="MA.912.GR.1.4",
 body="""A polygon is a closed figure made of straight segments. The interior angles of a polygon with n sides add to (n minus 2) times 180 degrees. The exterior angles of any convex polygon, one at each vertex, add to 360 degrees.

Examples: A pentagon has n = 5, so the interior angles add to 3 times 180 = 540 degrees. A regular hexagon has six equal angles, so each one is 720 divided by 6 = 120 degrees.

A parallelogram is a quadrilateral with two pairs of parallel sides. Theorems for a parallelogram:
Opposite sides are congruent.
Opposite angles are congruent.
Consecutive angles are supplementary (they add to 180 degrees).
The diagonals bisect each other.

Converses help us prove a figure is a parallelogram. If both pairs of opposite sides are congruent, or both pairs of opposite angles are congruent, or the diagonals bisect each other, or one pair of opposite sides is both parallel and congruent, then the quadrilateral is a parallelogram.

Worked example: In parallelogram ABCD, angle A = 2x + 10 and angle B = 3x minus 5. Consecutive angles add to 180, so 5x + 5 = 180, x = 35. Angle A = 80 degrees and angle B = 100 degrees.

Worked example: The diagonals meet at E. AE = 3y + 2 and EC = 5y minus 6. The diagonals bisect each other, so 3y + 2 = 5y minus 6, which gives y = 4. AE = 14, so the whole diagonal AC = 28.

Your task: (1) Find the sum of the interior angles of an octagon and the measure of one angle of a regular octagon. (2) In a parallelogram one angle is 70 degrees. Find the other three angles. (3) A quadrilateral has diagonals that bisect each other. What can you conclude, and why?""",
 script="""Welcome back. Today we study polygons, and then one of the most useful polygons of all, the parallelogram. A polygon is a closed figure made of straight segments. If a polygon has n sides, its interior angles add up to n minus two, times one hundred eighty degrees. Why? Because you can cut it into n minus two triangles, and each triangle has one hundred eighty degrees. A pentagon has five sides, so three triangles, and three times one hundred eighty is five hundred forty degrees.

Now watch this. The exterior angles, one at each vertex, always add up to three hundred sixty degrees for a convex polygon, no matter how many sides it has. So a regular hexagon has six equal interior angles. Seven hundred twenty divided by six gives one hundred twenty degrees each.

Now the parallelogram. It is a quadrilateral with two pairs of parallel sides. Here is what is always true. Opposite sides are congruent. Opposite angles are congruent. Consecutive angles are supplementary, which means they add to one hundred eighty. And the diagonals bisect each other.

The converses are how we prove a quadrilateral is a parallelogram. If both pairs of opposite sides are congruent, it is a parallelogram. If both pairs of opposite angles are congruent, it is a parallelogram. If the diagonals bisect each other, it is a parallelogram. And if one pair of opposite sides is both parallel and congruent, it is a parallelogram.

Let us solve one. Angle A is two x plus ten, and angle B is three x minus five. They are consecutive, so they add to one hundred eighty. Five x plus five equals one hundred eighty. Five x is one hundred seventy five, and x is thirty five. Angle A is eighty degrees and angle B is one hundred degrees.

One more. The diagonals meet at E. A E is three y plus two, and E C is five y minus six. The diagonals bisect each other, so these are equal. Subtract three y, two equals two y minus six. Add six, eight equals two y, so y is four. A E is fourteen, and the whole diagonal is twenty eight.

Your task today. Find the angle sum of an octagon. Eight minus two is six, six times one hundred eighty is one thousand eighty degrees, and a regular octagon has one hundred thirty five degrees at each corner. If one angle of a parallelogram is seventy degrees, the opposite angle is also seventy, and the other two are one hundred ten. And if the diagonals of a quadrilateral bisect each other, it is a parallelogram, by the converse. Take the four question check when you finish.

Every strong house has walls that agree with one another. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("The interior angles of a pentagon add to:", ["540 degrees", "360 degrees", "720 degrees", "900 degrees"], 0, "(5 minus 2) times 180 is 540."),
 ("Opposite angles of a parallelogram are:", ["Congruent", "Supplementary", "Complementary", "Always right angles"], 0, "Opposite angles of a parallelogram are congruent."),
 ("The diagonals of a parallelogram:", ["Bisect each other", "Are always congruent", "Are always perpendicular", "Are parallel"], 0, "Each diagonal cuts the other in half."),
 ("One angle of a parallelogram is 70 degrees. A consecutive angle measures:", ["110 degrees", "70 degrees", "20 degrees", "290 degrees"], 0, "Consecutive angles are supplementary, and 180 minus 70 is 110."),
 ]),
 dict(t="3.2 Rectangles, Rhombuses and Squares", std="MA.912.GR.1.4",
 body="""Three special parallelograms have extra properties, and each one keeps every parallelogram property.

Rectangle: a parallelogram with four right angles. Its diagonals are congruent.
Rhombus: a parallelogram with four congruent sides. Its diagonals are perpendicular, and each diagonal bisects a pair of opposite angles.
Square: a parallelogram that is both a rectangle and a rhombus. It has four right angles, four congruent sides, and diagonals that are congruent and perpendicular.

Converses: A parallelogram with congruent diagonals is a rectangle. A parallelogram with perpendicular diagonals is a rhombus. A parallelogram with one right angle is a rectangle. A parallelogram with two congruent consecutive sides is a rhombus.

Worked example: The diagonals of a rectangle measure 5x + 3 and 8x minus 12. They are congruent, so 5x + 3 = 8x minus 12, 15 = 3x, x = 5. Each diagonal is 28.

Worked example: A rhombus has diagonals of 12 and 16. The diagonals bisect each other at right angles, so each side is the hypotenuse of a right triangle with legs 6 and 8. By the Pythagorean Theorem the side is 10.

Worked example: One angle of a rhombus is 50 degrees. A diagonal through that vertex bisects it, making two 25 degree angles.

Your task: (1) The diagonals of a rectangle are 3y + 7 and 5y minus 9. Find y. (2) A rhombus has diagonals 10 and 24. Find its side length and perimeter. (3) Explain why every square is a rectangle but not every rectangle is a square.""",
 script="""Now, let us meet three special members of the parallelogram family. Each of them keeps every property of a parallelogram, and then adds something more.

The rectangle is a parallelogram with four right angles. Its special gift is that the diagonals are congruent. The rhombus is a parallelogram with four congruent sides. Its gifts are that the diagonals are perpendicular, and each diagonal bisects a pair of opposite angles. And the square is both at once. Four right angles, four equal sides, and diagonals that are congruent and perpendicular.

Watch this. The converses are very useful. If a parallelogram has congruent diagonals, it is a rectangle. If a parallelogram has perpendicular diagonals, it is a rhombus. If a parallelogram has one right angle, it is a rectangle. And if a parallelogram has two congruent consecutive sides, it is a rhombus.

Let us solve some. The diagonals of a rectangle are five x plus three and eight x minus twelve. They are congruent, so five x plus three equals eight x minus twelve. Subtract five x, three equals three x minus twelve. Add twelve, fifteen equals three x, so x is five. Each diagonal is five times five plus three, which is twenty eight.

Next, a rhombus with diagonals twelve and sixteen. The diagonals bisect each other at right angles, so half of each diagonal is six and eight. Those are the legs of a right triangle, and the side of the rhombus is the hypotenuse. Six squared is thirty six, eight squared is sixty four, and together that is one hundred. The square root of one hundred is ten. Each side is ten.

And if one angle of a rhombus is fifty degrees, the diagonal through that corner cuts it in half, so you get two angles of twenty five degrees.

Your task today. Set three y plus seven equal to five y minus nine and find y, which is eight. For the rhombus with diagonals ten and twenty four, the half diagonals are five and twelve, so the side is thirteen and the perimeter is fifty two. And explain why every square is a rectangle, but not every rectangle is a square. A rectangle needs only right angles. A square needs equal sides as well. Take the four question check when you finish.

Order and beauty come from the same Creator. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("A parallelogram with four congruent sides is a:", ["Rhombus", "Rectangle", "Trapezoid", "Kite"], 0, "A rhombus has four congruent sides."),
 ("The diagonals of a rectangle are:", ["Congruent", "Perpendicular", "Parallel", "Always unequal"], 0, "Rectangles have congruent diagonals."),
 ("A rhombus has diagonals of 12 and 16. Its side length is:", ["10", "14", "20", "28"], 0, "Half diagonals 6 and 8 form a right triangle with hypotenuse 10."),
 ("Which figure is both a rectangle and a rhombus?", ["Square", "Trapezoid", "Kite", "Scalene triangle"], 0, "A square has four right angles and four congruent sides."),
 ]),
 dict(t="3.3 Trapezoids and Kites", std="MA.912.GR.1.5",
 body="""A trapezoid is a quadrilateral with exactly one pair of parallel sides. The parallel sides are the bases, and the other two sides are the legs.

Isosceles trapezoid: a trapezoid whose legs are congruent. Its base angles are congruent, its opposite angles are supplementary, and its diagonals are congruent.

Midsegment of a trapezoid: the segment joining the midpoints of the legs. It is parallel to the bases, and its length is half the sum of the bases: m = (b1 + b2) divided by 2.

Worked example: The bases of a trapezoid are 10 and 18. The midsegment is (10 + 18) divided by 2 = 14.

Worked example: A midsegment is 15 and one base is 11. Then 11 + b = 30, so the other base is 19.

Worked example: In an isosceles trapezoid one base angle is 65 degrees. The other angle on that base is also 65. Each angle on the other base is 180 minus 65 = 115 degrees, because angles along a leg are supplementary.

Kite: a quadrilateral with two pairs of adjacent congruent sides, and no opposite sides congruent. The diagonals of a kite are perpendicular. One diagonal bisects the other, and it also bisects the angles at the vertices it joins.

Your task: (1) Find the midsegment of a trapezoid with bases 14 and 30. (2) The midsegment of a trapezoid is 20 and one base is 26. Find the other base. (3) In an isosceles trapezoid, one base angle is 72 degrees. Find the other three angles.""",
 script="""Listen, not every quadrilateral is a parallelogram. Today we meet two that are not, the trapezoid and the kite.

A trapezoid has exactly one pair of parallel sides. Those parallel sides are called the bases, and the other two sides are the legs. If the legs are congruent, we call it an isosceles trapezoid. And an isosceles trapezoid has special gifts. The base angles are congruent. The diagonals are congruent. And opposite angles are supplementary.

Now watch this, because there is a beautiful formula. The midsegment of a trapezoid connects the midpoints of the two legs. It is parallel to the bases, and its length is the average of the bases. Add the bases and divide by two. So if the bases are ten and eighteen, add to get twenty eight, divide by two, and the midsegment is fourteen.

You can also work backward. If the midsegment is fifteen and one base is eleven, then the two bases add up to thirty, because fifteen times two is thirty. Thirty minus eleven is nineteen. The other base is nineteen.

Now angles. In an isosceles trapezoid, suppose one base angle is sixty five degrees. The other angle on the same base is also sixty five. The angles on the other base are each one hundred eighty minus sixty five, which is one hundred fifteen degrees, because the angles along each leg add to one hundred eighty.

Next, the kite. A kite has two pairs of adjacent sides that are congruent, but opposite sides are not congruent. Think of a kite flying in the sky. Its diagonals are perpendicular. One diagonal bisects the other, and it also bisects the angles at the corners it connects.

Your task today. Find the midsegment when the bases are fourteen and thirty. Add to get forty four and divide by two to get twenty two. Find the other base when the midsegment is twenty and one base is twenty six. The bases add to forty, so the other base is fourteen. And find the angles of an isosceles trapezoid with a seventy two degree base angle. Two angles are seventy two and two angles are one hundred eight. Take the four question check when you finish.

A kite rises because the wind meets a good design. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("The bases of a trapezoid are 8 and 20. The midsegment is:", ["14", "12", "28", "7"], 0, "(8 + 20) divided by 2 is 14."),
 ("The base angles of an isosceles trapezoid are:", ["Congruent", "Supplementary", "Complementary", "Always right angles"], 0, "In an isosceles trapezoid the base angles are congruent."),
 ("The diagonals of a kite are:", ["Perpendicular", "Always congruent", "Parallel", "Always equal in length"], 0, "A kite has perpendicular diagonals."),
 ("A trapezoid has a midsegment of 12 and one base of 9. The other base is:", ["15", "3", "21", "10.5"], 0, "The bases add to 24, and 24 minus 9 is 15."),
 ]),
 dict(t="3.4 Quadrilaterals on the Coordinate Plane", std="MA.912.GR.3.2",
 body="""Coordinate geometry lets us prove facts about shapes using numbers. Three formulas do most of the work.

Slope of the line through (x1, y1) and (x2, y2): m = (y2 minus y1) divided by (x2 minus x1). Parallel lines have equal slopes. Perpendicular lines have slopes that are negative reciprocals, so their product is negative 1. A horizontal line has slope 0 and a vertical line has no slope.

Distance: d = the square root of [(x2 minus x1) squared + (y2 minus y1) squared].

Midpoint: the average of the coordinates, ((x1 + x2) divided by 2, (y1 + y2) divided by 2).

Worked example: A(1, 2), B(5, 2), C(7, 5), D(3, 5). Slope of AB = 0 and slope of DC = 0, so AB is parallel to DC. Slope of AD = (5 minus 2) divided by (3 minus 1) = 3/2 and slope of BC = (5 minus 2) divided by (7 minus 5) = 3/2, so AD is parallel to BC. Both pairs of opposite sides are parallel, so ABCD is a parallelogram. Check with the midpoints of the diagonals: AC has midpoint (4, 3.5) and BD has midpoint (4, 3.5). They match, so the diagonals bisect each other.

Is it a rhombus? AB = 4, and AD = the square root of (2 squared + 3 squared) = the square root of 13. The sides are not equal, so it is not a rhombus.

Worked example: P(0, 0), Q(4, 0), R(4, 3), S(0, 3). PQ is horizontal and QR is vertical, so they are perpendicular. The diagonals PR and QS both have length 5. A parallelogram with congruent diagonals is a rectangle.

Your task: A(0, 0), B(4, 0), C(5, 3), D(1, 3). (1) Use slopes to show ABCD is a parallelogram. (2) Decide whether it is a rhombus, using side lengths. (3) Decide whether it is a rectangle, using slopes.""",
 script="""Now we bring algebra and geometry together. This is called coordinate geometry, and it lets us prove facts about shapes using numbers on a grid.

We need three tools. First, slope. The slope of a line through two points is the change in y divided by the change in x. Parallel lines have equal slopes. Perpendicular lines have slopes that are negative reciprocals, so when you multiply them you get negative one. A horizontal line has slope zero. Second, the distance formula. Subtract the x values and square, subtract the y values and square, add, and take the square root. Third, the midpoint. Average the x values and average the y values.

Watch this. Here is a quadrilateral with corners A at one, two. B at five, two. C at seven, five. And D at three, five. Side A B is horizontal, so its slope is zero. Side D C is also horizontal, so its slope is zero. They are parallel. Now side A D. The y changes by three and the x changes by two, so the slope is three halves. Side B C also changes by three in y and two in x, so its slope is three halves. Those are parallel too. Two pairs of parallel sides means a parallelogram.

We can double check with midpoints. The midpoint of diagonal A C is four, three and a half. The midpoint of diagonal B D is four, three and a half. Same point, so the diagonals bisect each other. That confirms it.

Is it a rhombus? Side A B has length four. Side A D has length the square root of two squared plus three squared, which is the square root of thirteen. Four and the square root of thirteen are not equal, so it is not a rhombus.

Now a rectangle. P at zero, zero. Q at four, zero. R at four, three. And S at zero, three. P Q is horizontal and Q R is vertical, so they are perpendicular. The diagonals P R and Q S both have length five, from the three, four, five triangle. A parallelogram with congruent diagonals is a rectangle.

Your task today. Take A at zero, zero, B at four, zero, C at five, three, and D at one, three. Show it is a parallelogram using slopes. A B and D C have slope zero. A D and B C both have slope three. Decide if it is a rhombus. A B is four, and A D is the square root of ten, so no. Decide if it is a rectangle. Slopes zero and three are not negative reciprocals, so no. Take the four question check when you finish.

Numbers are a language of truth, and truth is a language of God. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("The midpoint of the segment from (2, 6) to (8, 10) is:", ["(5, 8)", "(10, 16)", "(6, 4)", "(3, 2)"], 0, "Average the coordinates: (2 + 8) divided by 2 is 5 and (6 + 10) divided by 2 is 8."),
 ("The distance from (1, 1) to (4, 5) is:", ["5", "7", "25", "3"], 0, "The square root of 3 squared plus 4 squared is the square root of 25, which is 5."),
 ("Which fact shows a quadrilateral is a parallelogram on the coordinate plane?", ["Both pairs of opposite sides have equal slopes", "Only one pair of sides has slope 0", "The diagonals have the same slope", "Two sides have the same length"], 0, "Equal slopes on both pairs of opposite sides mean both pairs are parallel."),
 ("The slope of the segment from A(1, 2) to B(5, 2) is:", ["0", "1", "4", "Undefined"], 0, "The y values do not change, so the slope is 0."),
 ]),
 ],
 assess=dict(t="Assessment 3: Quadrilaterals and Coordinate Proofs",
 prompt="""Complete all parts, showing your work and explaining your reasoning.

Part A: Find the sum of the interior angles of a decagon (10 sides) and the measure of one angle of a regular decagon. In parallelogram PQRS, angle P = 4x + 12 and angle Q = 2x + 18. Find x and all four angles.

Part B: The diagonals of a rectangle measure 7y minus 4 and 4y + 14. Find y and the length of each diagonal. A rhombus has diagonals of 18 and 24. Find its side length and its perimeter.

Part C: A trapezoid has bases of 16 and 34. Find its midsegment. An isosceles trapezoid has a base angle of 58 degrees. Find the other three angles. Explain how a kite is different from a parallelogram.

Part D: Quadrilateral ABCD has A(1, 1), B(7, 1), C(9, 5), D(3, 5). Use slopes to show it is a parallelogram. Use the distance formula to decide whether it is a rhombus. Use the midpoints of the diagonals to confirm your answer. Write a short conclusion that names the most specific type of quadrilateral that ABCD is.""",
 rubric="""100 points. Part A, correct angle sums and the parallelogram angles: 25 points. Part B, correct y, diagonals, side and perimeter: 25 points. Part C, correct midsegment, trapezoid angles and kite explanation: 20 points. Part D, correct slopes, distances, midpoints and conclusion: 20 points. Clear work and complete sentences: 10 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 3: Wisdom Builds and Understanding Establishes",
 prompt="""Shapes tell us how things hold together. Write a post of at least 120 words that (1) explains in your own words why a quadrilateral needs to be classified by its properties and not just by how it looks, (2) describes a real object, such as a bridge, a door frame, a kite or a field, where a certain quadrilateral does an important job, (3) tells which idea from this unit you found most interesting and why, and (4) connects your answer to Proverbs 24:3, which says, Through wisdom is an house builded; and by understanding it is established. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why might a builder prefer a figure with congruent diagonals? Keep your language clean and your tone kind."""),
 unit_quiz=[
 ("The interior angles of a hexagon add to:", ["720 degrees", "360 degrees", "540 degrees", "1080 degrees"], 0, "(6 minus 2) times 180 is 720."),
 ("The exterior angles of a convex polygon, one at each vertex, add to:", ["360 degrees", "180 degrees", "720 degrees", "It depends on the number of sides"], 0, "The exterior angles of any convex polygon add to 360 degrees."),
 ("In a parallelogram, consecutive angles are:", ["Supplementary", "Congruent", "Complementary", "Vertical"], 0, "Consecutive angles add to 180 degrees."),
 ("A parallelogram with perpendicular diagonals is a:", ["Rhombus", "Rectangle", "Trapezoid", "Kite"], 0, "Perpendicular diagonals in a parallelogram make it a rhombus."),
 ("A rectangle has diagonals 3y + 7 and 5y minus 9. The value of y is:", ["8", "4", "16", "2"], 0, "3y + 7 = 5y minus 9 gives 16 = 2y, so y = 8."),
 ("The bases of a trapezoid are 14 and 30. The midsegment is:", ["22", "16", "44", "8"], 0, "(14 + 30) divided by 2 is 22."),
 ("The midpoint of the segment from (0, 4) to (6, 10) is:", ["(3, 7)", "(6, 14)", "(3, 3)", "(6, 6)"], 0, "Average each coordinate: 3 and 7."),
 ("A quadrilateral has opposite sides with equal slopes, and its diagonals have equal lengths. It is a:", ["Rectangle", "Kite", "Trapezoid", "Rhombus only"], 0, "A parallelogram with congruent diagonals is a rectangle."),
 ])
