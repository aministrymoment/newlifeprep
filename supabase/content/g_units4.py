"""Geometry, Unit 4: Transformations, Similarity and Scale. Florida B.E.S.T. Mathematics Geometry standards."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."

UNIT4 = dict(
 title="Unit 4: Transformations, Similarity and Scale",
 std="MA.912.GR.1.2, MA.912.GR.2.1, MA.912.GR.2.2, MA.912.GR.2.3, MA.912.GR.2.5, MA.912.GR.2.6, MA.912.GR.2.8, MA.912.GR.4.3",
 topics=[
 dict(t="4.1 Translations, Reflections and Rotations", std="MA.912.GR.2.1, MA.912.GR.2.2, MA.912.GR.2.5",
 body="""A transformation moves a figure in the plane. The original figure is the preimage and the new figure is the image. A rigid transformation preserves distance and angle measure, so the image is congruent to the preimage. The three rigid transformations are translations, reflections and rotations.

Translation: slides every point the same distance in the same direction. The rule (x, y) becomes (x + 3, y minus 2) moves each point 3 units right and 2 units down. Example: A(1, 4) moves to A'(4, 2).

Reflection: flips a figure across a line.
Across the x axis: (x, y) becomes (x, negative y). Example: B(3, 2) becomes B'(3, negative 2).
Across the y axis: (x, y) becomes (negative x, y). Example: C(5, 1) becomes C'(negative 5, 1).

Rotation about the origin, counterclockwise:
90 degrees: (x, y) becomes (negative y, x). Example: D(2, 3) becomes D'(negative 3, 2).
180 degrees: (x, y) becomes (negative x, negative y). Example: E(4, 1) becomes E'(negative 4, negative 1).

A dilation is not rigid. It changes the size of a figure, so it does not preserve distance.

To describe a transformation algebraically, compare the coordinates of a point and its image and write the rule that connects them.

Your task: (1) Translate triangle P(0, 0), Q(3, 0), R(3, 2) by the rule (x + 2, y + 4). (2) Reflect S(2, 5) across the x axis and then across the y axis. (3) Rotate T(4, 1) by 90 degrees and by 180 degrees counterclockwise about the origin.""",
 script="""Welcome back. Today we begin a new unit about moving shapes. In geometry, a transformation moves a figure in the plane. The starting figure is called the preimage, and the figure after the move is called the image.

Some transformations are rigid. A rigid transformation keeps all distances and all angle measures the same, so the image is congruent to the preimage. There are three of them, translations, reflections and rotations.

A translation slides every point the same distance in the same direction. Think of sliding a book across a table. The rule x plus three, y minus two means every point moves three units right and two units down. So the point one, four moves to four, two.

Now watch this. A reflection flips a figure across a line, like a mirror. When you reflect across the x axis, the x stays the same and the y changes sign. So three, two becomes three, negative two. When you reflect across the y axis, the y stays the same and the x changes sign. So five, one becomes negative five, one.

Next, rotation. We rotate about the origin, counterclockwise. A ninety degree rotation takes x, y to negative y, x. So two, three becomes negative three, two. A one hundred eighty degree rotation takes x, y to negative x, negative y. So four, one becomes negative four, negative one.

There is one more transformation to remember, the dilation. It changes the size of a figure, so it is not rigid and it does not preserve distance. We study it very soon.

To describe a transformation with coordinates, compare a point with its image and find the rule that connects them. Ask yourself, did the x change, did the y change, did a sign change, did they swap places.

Your task today. Translate the triangle with corners zero, zero, three, zero and three, two by adding two to x and four to y. You get two, four, then five, four, then five, six. Reflect two, five across the x axis to get two, negative five, and then across the y axis to get negative two, negative five. And rotate four, one by ninety degrees to get negative one, four, and by one hundred eighty degrees to get negative four, negative one. Take the four question check when you finish.

A mirror shows what is, and the Word shows who we can be. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("Which transformation does NOT preserve distance?", ["Dilation with scale factor 2", "Translation", "Reflection", "Rotation"], 0, "A dilation changes the size of a figure."),
 ("The point (3, 2) is reflected across the x axis. Its image is:", ["(3, negative 2)", "(negative 3, 2)", "(2, 3)", "(negative 3, negative 2)"], 0, "Reflecting across the x axis changes the sign of y."),
 ("The point (2, 3) is rotated 90 degrees counterclockwise about the origin. Its image is:", ["(negative 3, 2)", "(3, negative 2)", "(negative 2, negative 3)", "(3, 2)"], 0, "The rule (x, y) becomes (negative y, x)."),
 ("The rule (x + 3, y minus 2) moves the point (1, 4) to:", ["(4, 2)", "(4, 6)", "(negative 2, 6)", "(3, 8)"], 0, "Add 3 to x and subtract 2 from y."),
 ]),
 dict(t="4.2 Congruence and Sequences of Transformations", std="MA.912.GR.2.3, MA.912.GR.2.6",
 body="""Two figures are congruent if and only if a sequence of rigid transformations maps one onto the other. This gives us a new way to understand congruence: one figure can be moved on top of the other with slides, flips and turns.

A sequence of transformations performs them one after another. Example: Triangle ABC has A(1, 1), B(4, 1), C(4, 3). Reflect it across the y axis to get A'(negative 1, 1), B'(negative 4, 1), C'(negative 4, 3). Then translate by (x, y + 2) to get A''(negative 1, 3), B''(negative 4, 3), C''(negative 4, 5). The final image is congruent to the original because both steps are rigid.

To describe a mapping, compare the figures. Look at orientation (a flipped figure needs a reflection) and position (use a translation or a rotation to place it).

Symmetry: A figure maps onto itself when a transformation leaves it looking the same.
Line symmetry: a reflection maps the figure onto itself. A rectangle has 2 lines of symmetry, a square has 4, and a regular polygon with n sides has n lines of symmetry.
Rotational symmetry: a rotation maps the figure onto itself. A regular polygon with n sides maps onto itself with a rotation of 360 divided by n degrees. An equilateral triangle maps onto itself with 120 degrees. A square with 90 degrees. A regular hexagon with 60 degrees.

Your task: (1) Triangle PQR has P(1, 2), Q(3, 2), R(3, 5). The image has P'(4, negative 2), Q'(6, negative 2), R'(6, negative 5). Describe a sequence of rigid transformations that maps PQR onto P'Q'R'. (2) How many lines of symmetry does a regular pentagon have, and what is its smallest rotation that maps it onto itself? (3) Explain why the image is congruent to the preimage.""",
 script="""Now, let us connect transformations with a big idea, congruence. Two figures are congruent when you can move one onto the other using a sequence of rigid transformations. Slides, flips and turns. If you can do that, the figures have the same size and the same shape.

A sequence just means one transformation after another. Let us try one. Triangle A B C has corners at one, one, four, one, and four, three. First we reflect it across the y axis. That gives negative one, one, then negative four, one, then negative four, three. Then we translate by adding two to y. The new corners are negative one, three, then negative four, three, then negative four, five. Both steps were rigid, so the final triangle is congruent to the first.

Now watch this. To describe a mapping, compare the two figures. First ask, is the figure flipped? If the orientation is reversed, you need a reflection. Then ask where it landed, and use a translation or a rotation to place it. Often there is more than one correct sequence, and the order sometimes matters.

Now symmetry. A figure has symmetry when some transformation maps it onto itself. Line symmetry means a reflection maps the figure onto itself. A rectangle has two lines of symmetry. A square has four. A regular polygon with n sides has n lines of symmetry.

Rotational symmetry means a rotation maps the figure onto itself. A regular polygon with n sides turns onto itself with a rotation of three hundred sixty divided by n degrees. An equilateral triangle, one hundred twenty degrees. A square, ninety degrees. A regular hexagon, sixty degrees.

Your task today. Describe a sequence that maps triangle P Q R, with corners one, two, three, two, and three, five, onto the triangle with corners four, negative two, six, negative two, and six, negative five. One answer, translate three units right, then reflect across the x axis. Find the symmetry of a regular pentagon. It has five lines of symmetry, and its smallest rotation is seventy two degrees. And explain why the image is congruent, because rigid transformations preserve distance and angle measure. Take the four question check when you finish.

God has a pattern for every life, and He moves us into place. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("Two figures are congruent when:", ["A sequence of rigid transformations maps one onto the other", "A dilation maps one onto the other", "They have the same number of sides", "They have the same perimeter only"], 0, "Rigid transformations preserve size and shape."),
 ("The smallest rotation that maps a regular hexagon onto itself is:", ["60 degrees", "30 degrees", "90 degrees", "120 degrees"], 0, "360 divided by 6 is 60."),
 ("How many lines of symmetry does a square have?", ["4", "2", "1", "8"], 0, "A square has 2 lines through opposite sides and 2 through opposite corners."),
 ("Which of these is a rigid transformation?", ["Reflection", "Dilation with scale factor 3", "A horizontal stretch", "Dilation with scale factor one half"], 0, "A reflection keeps distance and angle measure."),
 ]),
 dict(t="4.3 Dilations and Similar Figures", std="MA.912.GR.2.8, MA.912.GR.4.3",
 body="""A dilation changes the size of a figure but not its shape. A dilation with center at the origin and scale factor k sends (x, y) to (kx, ky).

If k is greater than 1, the image is an enlargement. If k is between 0 and 1, the image is a reduction. If k = 1, the image is the same size.

Example: Dilate A(2, 3) with k = 3. The image is A'(6, 9).
Example: Dilate the triangle (4, 2), (8, 2), (8, 6) with k = 1/2. The image is (2, 1), (4, 1), (4, 3).

Two figures are similar if a sequence of rigid transformations and dilations maps one onto the other. Similar figures have congruent corresponding angles and proportional corresponding sides. The scale factor is the ratio of corresponding lengths.

Effects of a scale factor k:
Lengths and perimeter are multiplied by k.
Area is multiplied by k squared.
Volume is multiplied by k cubed.

Example: A 3 by 5 rectangle is dilated with k = 4. The new rectangle is 12 by 20. The perimeter goes from 16 to 64, which is 4 times. The area goes from 15 to 240, which is 16 times, because 4 squared is 16.

Your task: (1) Dilate P(1, 2), Q(3, 2), R(3, 5) with center at the origin and k = 2. (2) A figure has area 8 and is dilated with scale factor 3. Find the new area. (3) Two similar triangles have corresponding sides of 6 and 15. The smaller has perimeter 20. Find the perimeter of the larger.""",
 script="""Listen, now we meet the transformation that changes size, the dilation. A dilation makes a figure larger or smaller, but the shape stays the same. Think of a photograph that you enlarge, or a map that shrinks a whole city onto one page.

A dilation with its center at the origin and scale factor k sends every point x, y to k times x, k times y. If k is greater than one, you get an enlargement. If k is a fraction between zero and one, you get a reduction. If k is exactly one, nothing changes in size.

Let us try it. Dilate the point two, three with scale factor three. Three times two is six, three times three is nine. The image is six, nine. Now the triangle with corners four, two, eight, two, and eight, six, with scale factor one half. Half of each coordinate gives one, one, and four, one, and four, three. A smaller triangle with the same shape.

Watch this. Two figures are similar when a sequence of rigid transformations and a dilation maps one onto the other. Similar figures have congruent corresponding angles and proportional corresponding sides. The scale factor is just the ratio of the corresponding lengths.

Here is something very important. When the scale factor is k, lengths and perimeter are multiplied by k. But area is multiplied by k squared. Take a three by five rectangle and enlarge it by a factor of four. The new rectangle is twelve by twenty. The perimeter goes from sixteen to sixty four, four times as much. But the area goes from fifteen to two hundred forty, which is sixteen times as much, because four squared is sixteen.

Your task today. Dilate the triangle with corners one, two, three, two, and three, five, using k equal to two. You get two, four, then six, four, then six, ten. A figure with area eight and scale factor three has a new area of eight times nine, which is seventy two. And two similar triangles have corresponding sides six and fifteen. The scale factor is fifteen over six, which is two and a half. So the larger perimeter is twenty times two and a half, which is fifty. Take the four question check when you finish.

Little becomes much when God is in the plan. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("A dilation with center at the origin and k = 3 maps (2, 3) to:", ["(6, 9)", "(5, 6)", "(2, 9)", "(9, 6)"], 0, "Multiply each coordinate by 3."),
 ("A dilation with scale factor one half produces:", ["A figure half the size", "A figure twice the size", "A figure the same size", "A rotated figure"], 0, "A scale factor between 0 and 1 reduces the figure."),
 ("A figure is dilated with scale factor 4. Its area is multiplied by:", ["16", "4", "8", "2"], 0, "Area is multiplied by k squared, and 4 squared is 16."),
 ("Similar figures have:", ["Congruent corresponding angles and proportional corresponding sides", "Congruent corresponding sides only", "The same area", "The same perimeter"], 0, "That is the definition of similar figures."),
 ]),
 dict(t="4.4 Similar Triangles and Indirect Measurement", std="MA.912.GR.1.2, MA.912.GR.2.8",
 body="""Triangles are similar if their corresponding angles are congruent and their corresponding sides are proportional. We write triangle ABC ~ triangle DEF. We do not need to check everything. These shortcuts prove similarity:

AA (angle, angle): two pairs of congruent angles. The third pair is automatic, because the angles of a triangle add to 180 degrees.
SAS similarity: two pairs of proportional sides and the included angles congruent.
SSS similarity: all three pairs of corresponding sides proportional.

Worked example: Triangle ABC is similar to triangle DEF. AB = 6, DE = 9 and BC = 8. The ratio DE to AB is 9/6 = 3/2. So EF = 8 times 3/2 = 12. As a proportion: 6/9 = 8/x, so 6x = 72 and x = 12.

Worked example: Triangles with sides 3, 4, 5 and 6, 8, 10 are similar by SSS, with scale factor 2.

Indirect measurement: use similar triangles to find a length you cannot measure directly. At the same moment, objects and their shadows form similar triangles. A 6 foot person casts a 4 foot shadow. A flagpole casts a 20 foot shadow. Let h be its height: h/20 = 6/4, so h = 30 feet.

Your task: (1) Triangles with sides 5, 7, 9 and 10, 14, x are similar. Find x. (2) A 5 foot post casts an 8 foot shadow and a building casts a 40 foot shadow. Find the height of the building. (3) Explain why two pairs of congruent angles are enough to prove two triangles similar.""",
 script="""Now we put similarity to work on triangles. Two triangles are similar when their corresponding angles are congruent and their corresponding sides are proportional. We write it with a little wavy symbol. Triangle A B C is similar to triangle D E F.

The good news is that we do not have to check everything. There are shortcuts. The first is AA, angle angle. If two angles of one triangle are congruent to two angles of another, the triangles are similar. The third angles must match too, because every triangle has one hundred eighty degrees. The second is SAS similarity. Two pairs of sides are proportional and the angles between them are congruent. The third is SSS similarity. All three pairs of sides are proportional.

Watch this. Triangle A B C is similar to triangle D E F. A B is six, D E is nine, and B C is eight. We want E F. The scale factor from the small triangle to the large one is nine over six, which is three halves. Eight times three halves is twelve. Or write a proportion. Six over nine equals eight over x. Cross multiply, six x equals seventy two, so x is twelve.

Another one. Triangles with sides three, four, five and six, eight, ten. Each side of the second is double the first. So they are similar by SSS, with scale factor two.

Now the best part, indirect measurement. How tall is a flagpole you cannot climb? At the same moment, a person and a flagpole make similar triangles with their shadows. Suppose a six foot person casts a four foot shadow, and the flagpole casts a twenty foot shadow. Height over twenty equals six over four. Cross multiply, four h equals one hundred twenty, and h is thirty feet.

Your task today. Triangles with sides five, seven, nine and ten, fourteen, x. The scale factor is two, so x is eighteen. A five foot post casts an eight foot shadow. A building casts a forty foot shadow. Five over eight equals h over forty, so h is twenty five feet. And explain why two angles are enough. The third angles are forced to be equal by the angle sum, so all three angles match. Take the four question check when you finish.

We measure what we can see by the light that shows us what we cannot. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("Two triangles each have angles of 50 and 60 degrees. They are similar by:", ["AA", "SSA", "HL", "CPCTC"], 0, "Two pairs of congruent angles prove similarity."),
 ("Triangle ABC is similar to triangle DEF with AB = 6, DE = 9 and BC = 8. Then EF is:", ["12", "10", "13.5", "6"], 0, "The scale factor is 9/6 = 3/2, and 8 times 3/2 is 12."),
 ("Triangles with sides 3, 4, 5 and 6, 8, 10 are:", ["Similar with scale factor 2", "Congruent", "Not similar", "Similar with scale factor 3"], 0, "Each side of the second triangle is 2 times the first."),
 ("A 6 foot person casts a 4 foot shadow. A tree casts a 20 foot shadow. The tree is:", ["30 feet tall", "13 feet tall", "24 feet tall", "40 feet tall"], 0, "h/20 = 6/4, so h = 30."),
 ]),
 ],
 assess=dict(t="Assessment 4: Transformations, Similarity and Scale",
 prompt="""Complete all parts, showing your work and explaining your reasoning.

Part A: Triangle ABC has A(1, 1), B(5, 1), C(5, 4). Find the image of each vertex after (1) a translation by the rule (x + 2, y + 3), (2) a reflection across the x axis, and (3) a rotation of 90 degrees counterclockwise about the origin. State which of these images are congruent to triangle ABC and explain why.

Part B: Triangle PQR has P(2, 1), Q(5, 1), R(5, 3). Its image has P'(negative 2, 4), Q'(negative 5, 4), R'(negative 5, 6). Describe a sequence of rigid transformations that maps PQR onto its image. Then state how many lines of symmetry a regular octagon has and the smallest rotation that maps it onto itself.

Part C: Dilate triangle (2, 2), (6, 2), (6, 5) with center at the origin and scale factor 2. Give the new coordinates. Find the area and perimeter of the original triangle and of the image. Show how the ratios of the areas and the perimeters relate to the scale factor.

Part D: Triangle ABC is similar to triangle DEF. AB = 8, DE = 12, BC = 10 and AC = 14. Find EF and DF, and the ratio of the perimeters. Then solve this: a 5 foot student casts a 7.5 foot shadow while a building casts a 45 foot shadow. Find the height of the building. Name the similarity shortcut you used.""",
 rubric="""100 points. Part A, three correct images and the congruence explanation: 25 points. Part B, a valid sequence and the symmetry facts: 20 points. Part C, correct coordinates, areas, perimeters and ratios: 25 points. Part D, correct side lengths, perimeter ratio, building height and shortcut: 20 points. Clear work and complete sentences: 10 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 4: Same Pattern, Different Size",
 prompt="""Similar figures share one pattern at many sizes. Write a post of at least 120 words that (1) explains in your own words what it means for two figures to be similar and how that differs from being congruent, (2) describes a real example of scaling, such as a map, a blueprint, a model car, a photograph or a shadow, and tells what stays the same and what changes, (3) tells which idea from this unit you found most interesting and why, and (4) connects your answer to Psalm 139:14, where David says, I am fearfully and wonderfully made. Then write a respectful reply of at least 40 words to another student's post, or answer this question: If a design is doubled in length, why is its area not simply doubled? Keep your language clean and your tone kind."""),
 unit_quiz=[
 ("The rule (x + 4, y minus 1) moves the point (2, 5) to:", ["(6, 4)", "(6, 6)", "(negative 2, 6)", "(8, 5)"], 0, "Add 4 to x and subtract 1 from y."),
 ("The point (4, 3) is reflected across the y axis. Its image is:", ["(negative 4, 3)", "(4, negative 3)", "(negative 4, negative 3)", "(3, 4)"], 0, "Reflecting across the y axis changes the sign of x."),
 ("Which transformation does NOT preserve distance?", ["Dilation with scale factor 2", "Rotation", "Reflection", "Translation"], 0, "A dilation changes size."),
 ("The point (3, 1) is rotated 180 degrees about the origin. Its image is:", ["(negative 3, negative 1)", "(negative 1, 3)", "(3, negative 1)", "(1, 3)"], 0, "The rule (x, y) becomes (negative x, negative y)."),
 ("A dilation with center at the origin and k = 2 maps (3, 5) to:", ["(6, 10)", "(5, 7)", "(3, 10)", "(1.5, 2.5)"], 0, "Multiply each coordinate by 2."),
 ("A figure is dilated with scale factor 3. Its area is multiplied by:", ["9", "3", "6", "27"], 0, "Area is multiplied by k squared, and 3 squared is 9."),
 ("Two triangles have two pairs of congruent angles. They are:", ["Similar by AA", "Congruent by ASA", "Congruent by SSA", "Not necessarily similar"], 0, "Two pairs of congruent angles prove similarity."),
 ("Two triangles are similar. A side of 4 in the first corresponds to a side of 10 in the second. A side of 6 in the first corresponds to:", ["15", "12", "7.5", "20"], 0, "The scale factor is 10/4 = 2.5, and 6 times 2.5 is 15."),
 ])
