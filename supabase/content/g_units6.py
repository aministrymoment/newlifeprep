"""Geometry, Unit 6: Circles, Area and Volume. Florida B.E.S.T. Mathematics Geometry standards."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."

UNIT6 = dict(
 title="Unit 6: Circles, Area and Volume",
 std="MA.912.GR.4.4, MA.912.GR.4.5, MA.912.GR.4.6, MA.912.GR.6.1, MA.912.GR.6.2, MA.912.GR.6.3, MA.912.GR.6.4, MA.912.GR.7.2, MA.912.GR.7.3",
 topics=[
 dict(t="6.1 Arcs, Central Angles and Inscribed Angles", std="MA.912.GR.6.2, MA.912.GR.6.3",
 body="""A circle is the set of all points in a plane at the same distance (the radius) from a center. A chord joins two points on the circle, and a diameter is a chord through the center. A diameter is twice the radius.

A central angle has its vertex at the center. Its measure equals the measure of its intercepted arc. The whole circle has 360 degrees.
Example: A central angle of 70 degrees intercepts an arc of 70 degrees.

An inscribed angle has its vertex on the circle. Its measure is half the measure of its intercepted arc.
Example: An arc of 80 degrees gives an inscribed angle of 40 degrees. An inscribed angle of 35 degrees intercepts an arc of 70 degrees.

An angle inscribed in a semicircle (an arc of 180 degrees) is a right angle, because half of 180 is 90.

Inscribed angles that intercept the same arc are congruent.

A quadrilateral inscribed in a circle has supplementary opposite angles. Example: if angle A = 100 degrees, then the opposite angle C = 80 degrees.

Worked example: Opposite angles of an inscribed quadrilateral measure 3x + 10 and 5x minus 30. They are supplementary: 8x minus 20 = 180, so x = 25. The angles are 85 and 95 degrees.

Your task: (1) An arc measures 110 degrees. Find the central angle and an inscribed angle that intercept it. (2) Opposite angles of an inscribed quadrilateral are 4x + 5 and 6x minus 25. Find x and the angles. (3) Explain why an angle inscribed in a semicircle is a right angle.""",
 script="""Welcome back. Today we begin our last unit, and it begins with the circle, the shape that has no beginning and no end. A circle is the set of all points in a plane that are the same distance from a center. That distance is the radius. A chord joins two points on the circle, and a diameter is a chord that passes through the center. A diameter is twice the radius.

Now we study angles in circles. A central angle has its vertex at the center. Its measure equals the measure of the arc it cuts off. A central angle of seventy degrees cuts off an arc of seventy degrees. The whole circle is three hundred sixty degrees.

Watch this. An inscribed angle has its vertex on the circle itself. Its measure is half of the arc it cuts off. So if the arc is eighty degrees, the inscribed angle is forty degrees. Or work backward. An inscribed angle of thirty five degrees cuts off an arc of seventy degrees.

Here is a beautiful result. An angle inscribed in a semicircle, which is an arc of one hundred eighty degrees, must be half of that, which is ninety degrees. So an angle inscribed in a semicircle is always a right angle. Also, two inscribed angles that cut off the same arc are congruent.

And one more fact. When a quadrilateral is inscribed in a circle, its opposite angles are supplementary. If one angle is one hundred degrees, the opposite angle is eighty.

Let us solve one. The opposite angles of an inscribed quadrilateral are three x plus ten and five x minus thirty. They add to one hundred eighty. Eight x minus twenty equals one hundred eighty. Eight x is two hundred, so x is twenty five. The angles are eighty five and ninety five degrees, and they do add to one hundred eighty.

Your task today. An arc of one hundred ten degrees has a central angle of one hundred ten and an inscribed angle of fifty five. Set four x plus five plus six x minus twenty five equal to one hundred eighty. Ten x minus twenty is one hundred eighty, so x is twenty, and the angles are eighty five and ninety five. And explain why an angle in a semicircle is ninety degrees. It is half of one hundred eighty. Take the four question check when you finish.

The circle reminds us that God's love has no end. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("A central angle measures 70 degrees. Its intercepted arc measures:", ["70 degrees", "35 degrees", "140 degrees", "110 degrees"], 0, "A central angle equals its intercepted arc."),
 ("An inscribed angle intercepts an arc of 100 degrees. The inscribed angle measures:", ["50 degrees", "100 degrees", "200 degrees", "25 degrees"], 0, "An inscribed angle is half its intercepted arc."),
 ("An angle inscribed in a semicircle measures:", ["90 degrees", "45 degrees", "180 degrees", "60 degrees"], 0, "Half of 180 degrees is 90 degrees."),
 ("An inscribed quadrilateral has an angle of 100 degrees. The opposite angle is:", ["80 degrees", "100 degrees", "260 degrees", "90 degrees"], 0, "Opposite angles of an inscribed quadrilateral are supplementary."),
 ]),
 dict(t="6.2 Chords, Tangents and Secants", std="MA.912.GR.6.1",
 body="""A tangent is a line that touches a circle at exactly one point, the point of tangency. A secant is a line that passes through a circle at two points. A chord is a segment with both endpoints on the circle.

Tangent theorems:
A tangent is perpendicular to the radius drawn to the point of tangency.
Two tangent segments drawn to a circle from the same outside point are congruent.

Worked example: A point P is 13 units from the center of a circle with radius 5. The tangent from P forms a right triangle with the radius and the segment from P to the center. The tangent length is the square root of (169 minus 25) = the square root of 144 = 12.

Intersecting chords: If two chords cross inside a circle, the product of the pieces of one chord equals the product of the pieces of the other: a times b = c times d.
Worked example: One chord has pieces 4 and 6 and the other has pieces 3 and x. Then 4 times 6 = 3 times x, so 24 = 3x and x = 8.

Tangent and secant from an outside point: The square of the tangent length equals the product of the whole secant and its outside piece: t squared = (outside piece) times (whole secant).
Worked example: A secant has an outside piece of 4 and a whole length of 9. Then t squared = 4 times 9 = 36, so t = 6.

Your task: (1) Two chords cross. One has pieces 6 and 8 and the other has pieces 4 and x. Find x. (2) A point is 10 units from the center of a circle of radius 6. Find the length of the tangent from the point. (3) A secant has an outside piece of 5 and a whole length of 20. Find the tangent length from the same point.""",
 script="""Now, let us study three kinds of lines and segments that meet a circle. A tangent touches the circle at exactly one point. Think of a wheel touching the road. A secant cuts through the circle at two points. And a chord is a segment with both endpoints on the circle.

Listen to the first big idea. A tangent is perpendicular to the radius drawn to the point where it touches. That makes a right angle, and a right angle means we can use the Pythagorean Theorem. Also, if you draw two tangents to a circle from the same outside point, the two tangent segments are congruent.

Let us try it. A point P is thirteen units from the center of a circle with radius five. Draw the tangent from P. The radius, the tangent, and the line from P to the center form a right triangle, with the hypotenuse thirteen. The tangent length is the square root of thirteen squared minus five squared. That is one hundred sixty nine minus twenty five, which is one hundred forty four, and the square root is twelve.

Now watch this. When two chords cross inside a circle, the products of their pieces are equal. If one chord has pieces four and six, and the other has pieces three and x, then four times six equals three times x. Twenty four equals three x, and x is eight.

One more rule. Suppose you have a tangent and a secant from the same outside point. The square of the tangent equals the outside piece of the secant times the whole secant. If the outside piece is four and the whole secant is nine, then the tangent squared is thirty six, and the tangent is six.

Your task today. For chords with pieces six and eight and four and x, forty eight equals four x, so x is twelve. For a point ten units from the center of a circle of radius six, the tangent is the square root of one hundred minus thirty six, which is eight. And for a secant with outside piece five and whole length twenty, the tangent squared is one hundred, so the tangent is ten. Take the four question check when you finish.

A good foundation touches the ground at one firm point. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("A tangent to a circle is perpendicular to:", ["The radius at the point of tangency", "Every chord", "The diameter at the center", "Another tangent"], 0, "A tangent meets the radius at a right angle."),
 ("Two chords cross. One has pieces 4 and 6 and the other has pieces 3 and x. Then x is:", ["8", "12", "2", "7"], 0, "4 times 6 = 3 times x, so x = 8."),
 ("A point is 13 units from the center of a circle with radius 5. The tangent from the point has length:", ["12", "8", "18", "144"], 0, "The square root of 169 minus 25 is 12."),
 ("Two tangent segments drawn to a circle from the same outside point are:", ["Congruent", "Parallel", "Perpendicular", "Always diameters"], 0, "Tangent segments from one outside point are congruent."),
 ]),
 dict(t="6.3 Arc Length, Sectors and Equations of Circles", std="MA.912.GR.6.4, MA.912.GR.7.2, MA.912.GR.7.3",
 body="""A fraction of a circle can be measured by its central angle. If the central angle is m degrees, the fraction of the circle is m divided by 360.

Arc length = (m divided by 360) times 2πr. This is the distance along the arc.
Sector area = (m divided by 360) times πr squared. A sector is the region bounded by two radii and an arc.

Worked example: A circle has radius 6 and a central angle of 60 degrees. The fraction is 60/360 = 1/6. Arc length = 1/6 times 2π(6) = 2π, about 6.28. Sector area = 1/6 times π(36) = 6π, about 18.85.

Equation of a circle with center (h, k) and radius r: (x minus h) squared + (y minus k) squared = r squared.

Worked example: Center (3, 4) and radius 5 gives (x minus 3) squared + (y minus 4) squared = 25. The point (6, 8) is on the circle because (6 minus 3) squared + (8 minus 4) squared = 9 + 16 = 25.

Reading an equation: (x minus 2) squared + (y minus 5) squared = 49 has center (2, 5) and radius 7, since 49 = 7 squared.

To write the equation when you know the center and a point on the circle, use the distance formula to find the radius.
Example: Center (1, 2) and the point (4, 6). The radius is the square root of (3 squared + 4 squared) = 5. The equation is (x minus 1) squared + (y minus 2) squared = 25.

Your task: (1) Find the arc length and sector area for radius 9 and central angle 120 degrees. Leave answers in terms of π. (2) State the center and radius of (x minus 7) squared + (y minus 1) squared = 36. (3) Write the equation of the circle with center (2, 3) that passes through the point (5, 7).""",
 script="""Now we measure pieces of a circle. If a central angle is m degrees, then that piece is m divided by three hundred sixty of the whole circle. Using that fraction, we can find two things. The arc length is the fraction times the circumference, two pi r. The sector area is the fraction times the area of the whole circle, pi r squared. A sector is a slice, like a slice of pizza, bounded by two radii and an arc.

Watch this. A circle has radius six and a central angle of sixty degrees. The fraction is sixty over three hundred sixty, which is one sixth. The circumference is two pi times six, twelve pi. One sixth of twelve pi is two pi, about six point two eight. The area is pi times thirty six, thirty six pi. One sixth of that is six pi, about eighteen point eight five.

Now let us put circles on the coordinate plane. A circle with center h, k and radius r has the equation x minus h, squared, plus y minus k, squared, equals r squared. This comes straight from the distance formula, because every point on the circle is the same distance r from the center.

For example, center three, four and radius five gives x minus three, squared, plus y minus four, squared, equals twenty five. Is the point six, eight on the circle? Six minus three is three, and three squared is nine. Eight minus four is four, and four squared is sixteen. Nine plus sixteen is twenty five. Yes, it is on the circle.

Reading an equation works backward. If you see x minus two, squared, plus y minus five, squared, equals forty nine, the center is two, five. The radius is the square root of forty nine, which is seven.

And if you are given a center and a point on the circle, use the distance formula to find the radius. Center one, two and point four, six. The changes are three and four, and the radius is five. So the equation is x minus one, squared, plus y minus two, squared, equals twenty five.

Your task today. For radius nine and a central angle of one hundred twenty degrees, the fraction is one third. The arc length is one third of eighteen pi, which is six pi. The sector area is one third of eighty one pi, which is twenty seven pi. For x minus seven, squared, plus y minus one, squared, equals thirty six, the center is seven, one and the radius is six. And the circle with center two, three through the point five, seven has a radius of five, so its equation is x minus two, squared, plus y minus three, squared, equals twenty five. Take the four question check when you finish.

Every part of a circle belongs to the whole. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("A circle has radius 6 and a central angle of 60 degrees. The arc length is:", ["2π", "6π", "12π", "π"], 0, "One sixth of 12π is 2π."),
 ("For the same circle and angle, the sector area is:", ["6π", "2π", "36π", "12π"], 0, "One sixth of 36π is 6π."),
 ("The circle (x minus 2) squared + (y minus 5) squared = 49 has radius:", ["7", "49", "5", "2"], 0, "The radius is the square root of 49."),
 ("The center of (x minus 3) squared + (y minus 4) squared = 25 is:", ["(3, 4)", "(4, 3)", "(5, 5)", "(negative 3, negative 4)"], 0, "The center is (h, k) = (3, 4)."),
 ]),
 dict(t="6.4 Area, Volume and Surface Area", std="MA.912.GR.4.4, MA.912.GR.4.5, MA.912.GR.4.6",
 body="""Area of two dimensional figures:
Rectangle: A = bh. Parallelogram: A = bh. Triangle: A = 1/2 bh.
Trapezoid: A = 1/2 (b1 + b2) h. Circle: A = πr squared.
Example: A trapezoid with bases 6 and 10 and height 4 has area 1/2 (16)(4) = 32.

Volume (the space inside) and surface area (the total area of the faces) of five solids:
Prism: V = Bh, where B is the area of the base. Surface area = 2B + Ph, where P is the perimeter of the base.
Cylinder: V = πr squared h. Surface area = 2πr squared + 2πrh.
Pyramid: V = 1/3 Bh.
Cone: V = 1/3 πr squared h. Surface area = πr squared + πrℓ, where ℓ is the slant height.
Sphere: V = 4/3 πr cubed. Surface area = 4πr squared.

Worked example: A cylinder has radius 3 and height 5. V = π(9)(5) = 45π, about 141.37. Surface area = 2π(9) + 2π(3)(5) = 18π + 30π = 48π, about 150.80.
Worked example: A sphere has radius 6. V = 4/3 π(216) = 288π, about 904.78. Surface area = 4π(36) = 144π, about 452.39.
Worked example: A cone has radius 3 and height 4. V = 1/3 π(9)(4) = 12π, about 37.70.

A cone has one third the volume of a cylinder with the same base and height. A pyramid has one third the volume of a prism with the same base and height.

Cross sections and rotations: slicing a cylinder parallel to its base gives a circle, and slicing it along its length gives a rectangle. Rotating a rectangle about one side makes a cylinder, and rotating a right triangle about a leg makes a cone.

Your task: (1) Find the area of a circle with radius 7. (2) Find the volume and surface area of a rectangular prism that is 4 by 5 by 6. (3) Find the volume of a cone with radius 6 and height 8.""",
 script="""Now we finish our course by measuring space. First, area, the amount of flat surface inside a figure. A rectangle is base times height. A parallelogram is also base times height. A triangle is one half base times height. A trapezoid is one half, times the sum of the bases, times the height. And a circle is pi r squared.

For example, a trapezoid with bases six and ten and height four. The bases add to sixteen, times four is sixty four, and half is thirty two.

Now three dimensional solids. Volume is the space inside, and surface area is the total area of all the faces. We study five solids. A prism has volume equal to the base area times the height. A cylinder has volume pi r squared h. A pyramid has volume one third of the base area times the height. A cone has volume one third pi r squared h. And a sphere has volume four thirds pi r cubed.

For surface area, a cylinder has two circles and a rolled up rectangle, two pi r squared plus two pi r h. A sphere has four pi r squared. A cone has the circle on the bottom plus the curved side, pi r squared plus pi r times the slant height.

Watch this. A cylinder with radius three and height five. The volume is pi times nine times five, which is forty five pi, about one hundred forty one point three seven cubic units. The surface area is two pi times nine, eighteen pi, plus two pi times three times five, thirty pi. Together that is forty eight pi, about one hundred fifty point eight.

A sphere with radius six. The radius cubed is two hundred sixteen, times four thirds is two hundred eighty eight. So the volume is two hundred eighty eight pi, about nine hundred four point seven eight. The surface area is four pi times thirty six, which is one hundred forty four pi.

A cone with radius three and height four has volume one third, times pi, times nine, times four, which is twelve pi. And notice this, a cone holds exactly one third as much as a cylinder with the same base and height. A pyramid holds one third as much as a prism with the same base and height.

Last, a word about slicing. If you slice a cylinder parallel to its base, you see a circle. If you slice it along its length, you see a rectangle. And if you spin a rectangle around one of its sides, you make a cylinder. Spin a right triangle around a leg and you make a cone.

Your task today. A circle with radius seven has an area of forty nine pi, about one hundred fifty three point nine four. A rectangular prism that is four by five by six has a volume of one hundred twenty. Its surface area is two times, twenty plus twenty four plus thirty, which is one hundred forty eight. And a cone with radius six and height eight has a volume of one third times pi times thirty six times eight, which is ninety six pi, about three hundred one point five nine. Take the four question check when you finish.

You have measured lines, angles, shapes and solids. Now go and build something good. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("The area of a circle with radius 7 is:", ["49π", "14π", "7π", "98π"], 0, "A = πr squared, and 7 squared is 49."),
 ("The volume of a rectangular prism that is 4 by 5 by 6 is:", ["120", "74", "148", "15"], 0, "4 times 5 times 6 = 120."),
 ("The volume of a sphere with radius r is:", ["4/3 πr cubed", "4πr squared", "πr squared h", "1/3 πr squared h"], 0, "The volume of a sphere is four thirds pi r cubed."),
 ("A cone and a cylinder have the same base and height. The cone's volume is:", ["One third of the cylinder's volume", "Half of the cylinder's volume", "Equal to the cylinder's volume", "Twice the cylinder's volume"], 0, "A cone holds one third as much as a cylinder."),
 ]),
 ],
 assess=dict(t="Assessment 6: Circles, Area and Volume",
 prompt="""Complete all parts, showing your work and explaining your reasoning.

Part A: An inscribed angle measures 62 degrees. Find its intercepted arc. A central angle intercepts an arc of 150 degrees. Find an inscribed angle that intercepts the same arc. An inscribed quadrilateral has opposite angles of 5x minus 5 and 3x + 25. Find x and both angles.

Part B: Two chords cross inside a circle. One has pieces 5 and 12 and the other has pieces 6 and x. Find x. A point is 13 units from the center of a circle with radius 5. Find the length of the tangent from the point. A secant has an outside piece of 4 and a whole length of 16. Find the tangent length from the same point.

Part C: A circle has center (4, 3) and radius 6. Write its equation and show that the point (4, 9) is on the circle. Then find the arc length and the sector area for a central angle of 90 degrees. Leave answers in terms of π.

Part D: Find the volume and surface area of a cylinder with diameter 10 and height 12. Find the volume of a sphere with radius 3. Find the volume of a square pyramid with base side 6 and height 5. Find the volume and total surface area of a cone with radius 3, height 4 and slant height 5. Leave answers in terms of π where it applies.""",
 rubric="""100 points. Part A, correct arcs, angles and the inscribed quadrilateral: 25 points. Part B, correct chord, tangent and secant results: 25 points. Part C, correct equation, point check, arc length and sector area: 25 points. Part D, correct volumes and surface areas: 15 points. Clear work and complete sentences: 10 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 6: The Circle of the Earth",
 prompt="""Circles and solids appear in everything from wheels to planets. Write a post of at least 120 words that (1) explains in your own words how a central angle, an arc and a sector are related, (2) describes a real object, such as a wheel, a pizza, a clock, a water tank or a ball, where circle or solid measurements matter, and tells how a measurement would be used, (3) tells which idea from this course you found most interesting and why, and (4) connects your answer to Isaiah 40:22, which says, It is he that sitteth upon the circle of the earth. Then write a respectful reply of at least 40 words to another student's post, or answer this question: How has studying geometry changed the way you look at the world around you? Keep your language clean and your tone kind."""),
 unit_quiz=[
 ("An inscribed angle intercepts an arc of 80 degrees. The inscribed angle measures:", ["40 degrees", "80 degrees", "160 degrees", "20 degrees"], 0, "An inscribed angle is half its intercepted arc."),
 ("A central angle measures 70 degrees. Its intercepted arc measures:", ["70 degrees", "35 degrees", "140 degrees", "110 degrees"], 0, "A central angle equals its intercepted arc."),
 ("An angle inscribed in a semicircle measures:", ["90 degrees", "45 degrees", "180 degrees", "60 degrees"], 0, "Half of 180 degrees is 90 degrees."),
 ("A tangent to a circle is perpendicular to:", ["The radius at the point of tangency", "Every chord", "Every secant", "The center"], 0, "A tangent meets the radius at a right angle."),
 ("Two chords cross. One has pieces 4 and 6 and the other has pieces 3 and x. Then x is:", ["8", "12", "2", "7"], 0, "4 times 6 = 3 times x, so x = 8."),
 ("A circle has radius 6 and a central angle of 60 degrees. The sector area is:", ["6π", "2π", "12π", "36π"], 0, "One sixth of 36π is 6π."),
 ("The center of (x minus 1) squared + (y minus 2) squared = 25 is:", ["(1, 2)", "(2, 1)", "(25, 25)", "(5, 5)"], 0, "The center is (h, k) = (1, 2)."),
 ("A cylinder has radius 3 and height 5. Its volume is:", ["45π", "30π", "15π", "90π"], 0, "V = π times 9 times 5 = 45π."),
 ])
