"""Geometry, Unit 5: Right Triangles and Trigonometry. Florida B.E.S.T. Mathematics Geometry standards."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."

UNIT5 = dict(
 title="Unit 5: Right Triangles and Trigonometry",
 std="MA.912.T.1.1, MA.912.T.1.2",
 topics=[
 dict(t="5.1 The Pythagorean Theorem and Its Converse", std="MA.912.T.1.2",
 body="""In a right triangle, the two sides that form the right angle are the legs, and the side opposite the right angle is the hypotenuse. It is always the longest side.

Pythagorean Theorem: In a right triangle with legs a and b and hypotenuse c, a squared + b squared = c squared.

Worked example: Legs 6 and 8. Then c squared = 36 + 64 = 100, so c = 10.
Worked example: Hypotenuse 13 and one leg 5. Then b squared = 169 minus 25 = 144, so b = 12.

Pythagorean triples are whole numbers that satisfy the theorem: 3, 4, 5 and 5, 12, 13 and 8, 15, 17 and 7, 24, 25. Multiples such as 6, 8, 10 also work.

Converse: If a squared + b squared = c squared for the three sides of a triangle, then the triangle is a right triangle. Example: 7, 24, 25 gives 49 + 576 = 625 = 25 squared, so it is a right triangle.

Classifying a triangle by its sides, with c the longest side:
If c squared is less than a squared + b squared, the triangle is acute.
If c squared equals a squared + b squared, the triangle is right.
If c squared is greater than a squared + b squared, the triangle is obtuse.
Example: 5, 6, 8 gives 25 + 36 = 61, which is less than 64, so the triangle is obtuse.

The distance formula is the Pythagorean Theorem on the coordinate plane. The horizontal change and the vertical change are the legs, and the distance is the hypotenuse.

Your task: (1) Find the hypotenuse of a right triangle with legs 9 and 12. (2) A right triangle has hypotenuse 17 and one leg 8. Find the other leg. (3) Classify the triangle with sides 6, 8 and 11 as acute, right or obtuse, and show your work.""",
 script="""Welcome to a new unit. Today we study the most famous theorem in all of geometry, the Pythagorean Theorem. First, some names. In a right triangle, the two sides that make the right angle are called the legs. The side across from the right angle is the hypotenuse, and it is always the longest side.

Now watch this. The theorem says that if the legs are a and b, and the hypotenuse is c, then a squared plus b squared equals c squared. Let us use it. The legs are six and eight. Six squared is thirty six, eight squared is sixty four, and together that is one hundred. The square root of one hundred is ten. The hypotenuse is ten.

Now work backward. The hypotenuse is thirteen and one leg is five. Thirteen squared is one hundred sixty nine. Five squared is twenty five. Subtract, and you get one hundred forty four. The square root of one hundred forty four is twelve. The other leg is twelve.

Some sets of whole numbers fit perfectly. We call them Pythagorean triples. Three, four, five. Five, twelve, thirteen. Eight, fifteen, seventeen. Seven, twenty four, twenty five. And any multiple of a triple works too, so six, eight, ten is a triple.

The converse is just as useful. If the three sides of a triangle satisfy a squared plus b squared equals c squared, then the triangle is a right triangle. Test seven, twenty four, twenty five. Forty nine plus five hundred seventy six is six hundred twenty five, and twenty five squared is six hundred twenty five. It is a right triangle.

And we can go one step further. Let c be the longest side. If c squared is less than a squared plus b squared, the triangle is acute. If it is equal, the triangle is right. If it is greater, the triangle is obtuse. Test five, six, eight. Twenty five plus thirty six is sixty one, and eight squared is sixty four. Sixty one is less than sixty four, so the triangle is obtuse.

Your task today. Legs nine and twelve give a hypotenuse of fifteen. A hypotenuse of seventeen and a leg of eight give another leg of fifteen. And for six, eight, eleven, thirty six plus sixty four is one hundred, and eleven squared is one hundred twenty one, so the triangle is obtuse. Take the four question check when you finish.

A true measure is a faithful friend. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("A right triangle has legs 5 and 12. The hypotenuse is:", ["13", "17", "7", "11"], 0, "25 + 144 = 169, and the square root of 169 is 13."),
 ("Which set of sides forms a right triangle?", ["8, 15, 17", "5, 6, 7", "4, 5, 6", "7, 8, 10"], 0, "64 + 225 = 289, which equals 17 squared."),
 ("A right triangle has hypotenuse 10 and one leg 6. The other leg is:", ["8", "4", "16", "64"], 0, "100 minus 36 is 64, and the square root of 64 is 8."),
 ("A triangle has sides 4, 5 and 7. It is:", ["Obtuse", "Acute", "Right", "Equilateral"], 0, "16 + 25 = 41, which is less than 49."),
 ]),
 dict(t="5.2 Special Right Triangles", std="MA.912.T.1.2",
 body="""Two right triangles appear so often that their side ratios are worth remembering.

The 45 45 90 triangle is an isosceles right triangle. Its legs are congruent. If each leg is s, the hypotenuse is s√2.
Why: s squared + s squared = 2 times s squared, so the hypotenuse is s√2.
Worked example: Legs of 7 give a hypotenuse of 7√2.
Worked example: Hypotenuse 10√2 gives legs of 10.
Worked example: A square with side 6 has a diagonal of 6√2.

The 30 60 90 triangle is half of an equilateral triangle. If the short leg (opposite the 30 degree angle) is s, then the long leg (opposite the 60 degree angle) is s√3 and the hypotenuse is 2s.
Worked example: Short leg 5 gives long leg 5√3 and hypotenuse 10.
Worked example: Hypotenuse 12 gives short leg 6 and long leg 6√3.
Worked example: Long leg 9√3 gives short leg 9 and hypotenuse 18.

Strategy: find the short leg first in a 30 60 90 triangle, then multiply to get the other sides. Check that the hypotenuse is the longest side and the short leg is the shortest.

Your task: (1) In a 45 45 90 triangle each leg is 9. Find the hypotenuse. (2) In a 30 60 90 triangle the hypotenuse is 14. Find the other two sides. (3) Find the diagonal of a square with side 6, and find the height of an equilateral triangle with side 10.""",
 script="""Now, let us meet two special right triangles. They show up in buildings, in design, in art and in tests, so they are worth learning well.

The first is the forty five, forty five, ninety triangle. It has two congruent legs, so it is an isosceles right triangle. If each leg is s, the Pythagorean Theorem says the hypotenuse squared is s squared plus s squared, which is two s squared. So the hypotenuse is s times the square root of two. If the legs are seven, the hypotenuse is seven root two. If the hypotenuse is ten root two, the legs are ten. And the diagonal of a square with side six is six root two.

The second is the thirty, sixty, ninety triangle. It is exactly half of an equilateral triangle, cut down the middle. Watch this. If the short leg is s, the hypotenuse is twice s, and the long leg is s times the square root of three. The short leg sits across from the thirty degree angle. The long leg sits across from the sixty degree angle.

Let us use it. Short leg five. The hypotenuse is ten and the long leg is five root three. Hypotenuse twelve. Cut it in half to find the short leg, six, and the long leg is six root three. Long leg nine root three. Divide by root three to find the short leg, nine, and the hypotenuse is eighteen.

A good strategy for the thirty, sixty, ninety triangle is to find the short leg first. Then double it for the hypotenuse, or multiply by root three for the long leg. And always check your answer. The hypotenuse must be the longest side, and the short leg must be the shortest.

Your task today. If each leg of a forty five, forty five, ninety triangle is nine, the hypotenuse is nine root two. If the hypotenuse of a thirty, sixty, ninety triangle is fourteen, the short leg is seven and the long leg is seven root three. The diagonal of a square with side six is six root two. And an equilateral triangle with side ten has a height of five root three, because the height cuts it into two thirty, sixty, ninety triangles. Take the four question check when you finish.

God builds with exact proportion, and so can we. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("In a 45 45 90 triangle each leg is 5. The hypotenuse is:", ["5√2", "10", "5√3", "25"], 0, "The hypotenuse is the leg times the square root of 2."),
 ("In a 30 60 90 triangle the hypotenuse is 16. The short leg is:", ["8", "16√3", "8√3", "32"], 0, "The short leg is half the hypotenuse."),
 ("In a 30 60 90 triangle the short leg is 4. The long leg is:", ["4√3", "8", "4√2", "12"], 0, "The long leg is the short leg times the square root of 3."),
 ("The diagonal of a square with side 3 is:", ["3√2", "6", "3√3", "9"], 0, "A square's diagonal makes a 45 45 90 triangle with the sides."),
 ]),
 dict(t="5.3 Trigonometric Ratios", std="MA.912.T.1.1",
 body="""Trigonometric ratios compare sides of a right triangle. They depend only on the acute angle, because right triangles with the same acute angle are similar.

For an acute angle A, name the sides this way: the hypotenuse is opposite the right angle, the opposite side is across from angle A, and the adjacent side touches angle A (and is not the hypotenuse).

sine of A = opposite divided by hypotenuse
cosine of A = adjacent divided by hypotenuse
tangent of A = opposite divided by adjacent

A memory helper is SOH CAH TOA: Sine is Opposite over Hypotenuse, Cosine is Adjacent over Hypotenuse, Tangent is Opposite over Adjacent.

Worked example: A right triangle has legs 3 and 4 and hypotenuse 5. For the angle A opposite the leg 3: sin A = 3/5, cos A = 4/5, tan A = 3/4.

For the other acute angle B, the sides swap roles: sin B = 4/5, cos B = 3/5, tan B = 4/3. Notice that sin A = cos B. The sine of an angle equals the cosine of its complement.

Because the ratios depend only on the angle, the ratios for the 3 4 5 triangle are the same as those for a 6 8 10 triangle.

Special values: sin 30 degrees = 1/2, cos 60 degrees = 1/2, tan 45 degrees = 1.

Your task: (1) A right triangle has legs 5 and 12 and hypotenuse 13. Let A be opposite the leg 5. Find sin A, cos A and tan A. (2) For the same triangle find sin B, where B is the other acute angle. (3) Explain why sin A and cos B are equal.""",
 script="""Listen, now we enter trigonometry, one of the most useful ideas in all of mathematics. The word trigonometry means triangle measurement. And the heart of it is a set of ratios, comparing the sides of a right triangle.

First we must name the sides from the view of one acute angle, call it A. The hypotenuse is always across from the right angle. The opposite side is across from angle A. The adjacent side touches angle A, and it is not the hypotenuse.

Now watch this. Three ratios. The sine of A is the opposite side divided by the hypotenuse. The cosine of A is the adjacent side divided by the hypotenuse. And the tangent of A is the opposite side divided by the adjacent side. To remember, say SOH CAH TOA. Sine, opposite over hypotenuse. Cosine, adjacent over hypotenuse. Tangent, opposite over adjacent.

Let us practice with the three, four, five triangle. Angle A is across from the three. So the sine of A is three fifths. The cosine of A is four fifths, because the adjacent side is four. And the tangent of A is three fourths.

Now look at the other acute angle, B. The sides swap roles. The sine of B is four fifths, the cosine of B is three fifths, and the tangent of B is four thirds. Do you see it? The sine of A equals the cosine of B. This always happens, because the two acute angles are complementary. The sine of an angle equals the cosine of its complement.

And here is why these ratios are so powerful. They depend only on the angle, not on the size of the triangle. A six, eight, ten triangle has the same ratios as the three, four, five triangle, because they are similar.

We also know some special values. The sine of thirty degrees is one half. The cosine of sixty degrees is one half. And the tangent of forty five degrees is one.

Your task today. For the five, twelve, thirteen triangle with A across from the five, the sine of A is five thirteenths, the cosine is twelve thirteenths, and the tangent is five twelfths. The sine of B is twelve thirteenths. And explain why the sine of A equals the cosine of B. Take the four question check when you finish.

Ratios hold when the sizes change, and truth holds when the seasons change. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("In a right triangle, the sine of an acute angle is:", ["Opposite divided by hypotenuse", "Adjacent divided by hypotenuse", "Opposite divided by adjacent", "Hypotenuse divided by opposite"], 0, "SOH: sine is opposite over hypotenuse."),
 ("A right triangle has sides 6, 8 and 10. For the angle opposite the side 6, the sine is:", ["3/5", "4/5", "3/4", "5/3"], 0, "Opposite 6 divided by hypotenuse 10 is 3/5."),
 ("For the same triangle and angle, the tangent is:", ["3/4", "4/3", "3/5", "4/5"], 0, "Opposite 6 divided by adjacent 8 is 3/4."),
 ("The sine of an acute angle equals the cosine of:", ["Its complement", "Its supplement", "Itself", "Twice the angle"], 0, "In a right triangle the two acute angles are complementary."),
 ]),
 dict(t="5.4 Solving Right Triangles", std="MA.912.T.1.2",
 body="""To solve a right triangle means to find all unknown sides and angles. We use trigonometric ratios, the Pythagorean Theorem and the fact that the acute angles add to 90 degrees.

Useful values (rounded): sin 30 = 0.5, tan 45 = 1, tan 35 = 0.7002, tan 40 = 0.8391, sin 70 = 0.9397, sin 60 = 0.8660.

Finding a side: choose the ratio that has the known side, the unknown side and the angle.
Worked example: A 12 foot ladder makes a 70 degree angle with the ground. The height it reaches is the opposite side, and the ladder is the hypotenuse, so sin 70 = h/12. Then h = 12 times 0.9397, about 11.3 feet.
Worked example: Standing 50 feet from a tree, the angle of elevation to the top is 35 degrees. The height is opposite and the distance is adjacent, so tan 35 = h/50. Then h = 50 times 0.7002, about 35.0 feet.

Finding an angle: use the inverse ratio. If tan A = 5/9 = 0.5556, then A is the angle whose tangent is 0.5556, which is about 29 degrees. The calculator buttons are written sin to the power negative 1, cos to the power negative 1 and tan to the power negative 1.

The angle of elevation is measured upward from the horizontal. The angle of depression is measured downward from the horizontal. They are equal for the same line of sight.

Your task: (1) A right triangle has hypotenuse 20 and a 30 degree angle. Find the side opposite the 30 degree angle. (2) From 60 feet away from a building the angle of elevation to the top is 40 degrees. Find the height. (3) A ramp rises 3 feet over a horizontal distance of 12 feet. Find the angle it makes with the ground.""",
 script="""Now we put trigonometry to work. To solve a right triangle means to find every missing side and angle. We have three tools. The trigonometric ratios, the Pythagorean Theorem, and the fact that the two acute angles add up to ninety degrees.

When you want a side, choose the ratio that includes the side you know, the side you want, and the angle. Let us try one. A twelve foot ladder leans against a wall and makes a seventy degree angle with the ground. How high does it reach? The ladder is the hypotenuse, and the height is the side opposite the angle. Opposite and hypotenuse means sine. So sine of seventy equals h over twelve. Sine of seventy is about point nine three nine seven. Multiply by twelve and the height is about eleven point three feet.

Another. You stand fifty feet from a tree and look up at the top at a thirty five degree angle of elevation. The height is opposite and the distance is adjacent. Opposite and adjacent means tangent. Tangent of thirty five is about point seven zero zero two. Multiply by fifty, and the tree is about thirty five feet tall.

Watch this. What if you want an angle instead? Use the inverse. Suppose the opposite side is five and the adjacent side is nine. The tangent of A is five ninths, about point five five five six. On the calculator, use the inverse tangent button, and you get about twenty nine degrees.

Two more words. The angle of elevation is measured upward from the horizontal line. The angle of depression is measured downward from the horizontal. For the same line of sight, they are equal, because they are alternate interior angles of parallel lines.

Your task today. A right triangle has hypotenuse twenty and a thirty degree angle. The opposite side is twenty times point five, which is ten. From sixty feet away, the angle of elevation to a building is forty degrees. The height is sixty times point eight three nine one, about fifty point three feet. And a ramp rises three feet over twelve feet of horizontal distance. The tangent is one fourth, which is point two five, and the angle is about fourteen degrees. Take the four question check when you finish.

Look up, measure well, and build with confidence. Excellence, Faith, Purpose. I will see you in the next lesson.""",
 quiz=[
 ("To find a height when you know the hypotenuse and an angle, you use:", ["Sine", "Cosine", "The Pythagorean Theorem alone", "Nothing, it cannot be found"], 0, "The height is opposite the angle, so use opposite over hypotenuse."),
 ("A 10 foot ladder makes a 60 degree angle with the ground. It reaches about:", ["8.7 feet", "5 feet", "10 feet", "17.3 feet"], 0, "10 times sin 60, which is 10 times 0.866, is about 8.7."),
 ("If tan A = 1 for an acute angle A, then A is:", ["45 degrees", "30 degrees", "60 degrees", "90 degrees"], 0, "The tangent of 45 degrees is 1."),
 ("A ramp rises 3 feet over a horizontal distance of 12 feet. The tangent of its angle is:", ["1/4", "4", "1/3", "3/4"], 0, "Opposite 3 divided by adjacent 12 is 1/4."),
 ]),
 ],
 assess=dict(t="Assessment 5: Right Triangles and Trigonometry",
 prompt="""Complete all parts, showing your work and explaining your reasoning.

Part A: A right triangle has one leg 15 and hypotenuse 39. Find the other leg. Then classify the triangle with sides 9, 12 and 16 as acute, right or obtuse and show your work.

Part B: In a 45 45 90 triangle the hypotenuse is 18. Find the legs. In a 30 60 90 triangle the long leg is 9√3. Find the short leg and the hypotenuse.

Part C: A right triangle has legs 8 and 15 and hypotenuse 17. Let A be the angle opposite the leg 8. Find sin A, cos A and tan A. Then find sin B and cos B for the other acute angle B, and explain how they relate to the values for A.

Part D: A 25 foot ladder leans against a wall with its base 7 feet from the wall. Find how high the ladder reaches, and use a trigonometric ratio to find the angle the ladder makes with the ground. Then solve this: from a point 80 feet from the base of a tower, the angle of elevation to the top is 28 degrees. Find the height of the tower. You may use tan 28 = 0.5317.""",
 rubric="""100 points. Part A, correct leg and classification: 20 points. Part B, correct special triangle sides: 20 points. Part C, correct ratios and complement explanation: 25 points. Part D, correct ladder height, angle and tower height: 25 points. Clear work and complete sentences: 10 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 5: A Just Weight Is His Delight",
 prompt="""Right triangles let us measure what we cannot reach, but only if our measurements are honest. Write a post of at least 120 words that (1) explains in your own words why the Pythagorean Theorem or a trigonometric ratio is useful for measuring something that cannot be measured directly, (2) describes a real situation, such as a ramp, a roof, a ladder, a tower or a surveyor's work, where an accurate measurement protects people, (3) tells which idea from this unit you found most interesting and why, and (4) connects your answer to Proverbs 11:1, which says, A false balance is abomination to the LORD: but a just weight is his delight. Then write a respectful reply of at least 40 words to another student's post, or answer this question: What could go wrong if a builder rounds a measurement carelessly? Keep your language clean and your tone kind."""),
 unit_quiz=[
 ("A right triangle has legs 6 and 8. The hypotenuse is:", ["10", "14", "12", "9"], 0, "36 + 64 = 100, and the square root of 100 is 10."),
 ("Which set of sides forms a right triangle?", ["9, 40, 41", "5, 6, 7", "4, 5, 6", "7, 8, 10"], 0, "81 + 1600 = 1681, which equals 41 squared."),
 ("In a 45 45 90 triangle each leg is 4. The hypotenuse is:", ["4√2", "8", "4√3", "16"], 0, "The hypotenuse is the leg times the square root of 2."),
 ("In a 30 60 90 triangle the short leg is 6. The long leg is:", ["6√3", "12", "6√2", "18"], 0, "The long leg is the short leg times the square root of 3."),
 ("The sine of an acute angle in a right triangle is:", ["Opposite divided by hypotenuse", "Adjacent divided by hypotenuse", "Opposite divided by adjacent", "Adjacent divided by opposite"], 0, "SOH: sine is opposite over hypotenuse."),
 ("A right triangle has sides 6, 8 and 10. For the angle opposite the side 6, the tangent is:", ["3/4", "4/3", "3/5", "4/5"], 0, "Opposite 6 divided by adjacent 8 is 3/4."),
 ("You stand 50 feet from the base of a tower and the angle of elevation to the top is 45 degrees. The tower is about:", ["50 feet tall", "25 feet tall", "70 feet tall", "100 feet tall"], 0, "The tangent of 45 degrees is 1, so the height equals the distance."),
 ("If sin A = 0.5 for an acute angle A, then A is:", ["30 degrees", "45 degrees", "60 degrees", "90 degrees"], 0, "The sine of 30 degrees is 1/2."),
 ])
