"""Geometry, Unit 2: Parallel Lines, Triangles and Congruence. Florida B.E.S.T. Mathematics Geometry standards."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."

UNIT2 = dict(
 title="Unit 2: Parallel Lines, Triangles and Congruence",
 std="MA.912.GR.1.1, MA.912.GR.1.2, MA.912.GR.1.3, MA.912.GR.1.6",
 topics=[
 dict(t="2.1 Parallel Lines and Transversals", std="MA.912.GR.1.1",
 body="""Parallel lines are lines in the same plane that never meet. A transversal is a line that crosses two or more other lines. When a transversal crosses two lines, it forms eight angles with special names.

Corresponding angles are in the same position at each crossing. Alternate interior angles are between the two lines on opposite sides of the transversal. Alternate exterior angles are outside the two lines on opposite sides. Same side interior angles are between the two lines on the same side of the transversal.

Theorems for parallel lines:
If the lines are parallel, then corresponding angles are congruent.
If the lines are parallel, then alternate interior angles are congruent.
If the lines are parallel, then alternate exterior angles are congruent.
If the lines are parallel, then same side interior angles are supplementary (they add to 180 degrees).

The converses are also true. If a pair of corresponding angles (or alternate interior angles) is congruent, then the lines are parallel.

Worked example: Parallel lines are cut by a transversal. Alternate interior angles measure 4x + 5 and 2x + 35. Set them equal: 4x + 5 = 2x + 35, so 2x = 30 and x = 15. Each angle measures 65 degrees.

Worked example: Same side interior angles measure 3x + 20 and 2x + 40. They are supplementary: 5x + 60 = 180, so x = 24. The angles measure 92 and 88 degrees.

Your task: (1) Parallel lines are cut by a transversal and one of the eight angles measures 110 degrees. Find the measure of all eight angles and name two pairs of alternate interior angles. (2) Same side interior angles measure 5x and 4x + 9. Find x and the angles. (3) Two lines are cut by a transversal and a pair of alternate interior angles are both 72 degrees. What can you conclude, and why?""",
 script="""Welcome back. Today we study one of the most useful ideas in geometry, parallel lines cut by a transversal. Parallel lines are lines in the same plane that never meet, like the two rails of a train track. A transversal is a line that crosses them, like a road crossing the tracks.

When a transversal crosses two lines, it makes eight angles, and the angles have special names. Corresponding angles are in the same position at each crossing, for example both in the upper left. Alternate interior angles are between the two lines and on opposite sides of the transversal. Alternate exterior angles are outside the two lines and on opposite sides. And same side interior angles are between the two lines and on the same side of the transversal.

Now watch this. Here are the four theorems. If the lines are parallel, then corresponding angles are congruent. If the lines are parallel, alternate interior angles are congruent. If the lines are parallel, alternate exterior angles are congruent. And if the lines are parallel, same side interior angles are supplementary, which means they add to one hundred eighty degrees.

The converses are also true, and they are how we prove lines are parallel. If a pair of corresponding angles is congruent, or a pair of alternate interior angles is congruent, then the lines are parallel.

Let us solve one. Parallel lines are cut by a transversal. The alternate interior angles measure four x plus five and two x plus thirty five. They are congruent, so four x plus five equals two x plus thirty five. Subtract two x, two x plus five equals thirty five. Subtract five, two x equals thirty. So x is fifteen. Substitute, four times fifteen is sixty, plus five is sixty five degrees. Check the other, two times fifteen is thirty, plus thirty five is sixty five. They match.

Now same side interior. The angles measure three x plus twenty and two x plus forty. They are supplementary, so five x plus sixty equals one hundred eighty. Five x is one hundred twenty, and x is twenty four. The angles are ninety two and eighty eight, and they do add to one hundred eighty.

Your task today. If one of the eight angles is one hundred ten degrees, find all eight. Every angle is either one hundred ten or seventy, because angles are congruent or supplementary. Solve for x when same side interior angles measure five x and four x plus nine. Five x plus four x plus nine equals one hundred eighty, so nine x is one hundred seventy one and x is nineteen. And explain what you can conclude if a pair of alternate interior angles are both seventy two degrees. They are congruent, so the lines are parallel. Take the four question check when you finish.

Straight lines and steady rails remind us that order is a gift. Excellence, Faith, Purpose. I will see you in the next lesson.""" ,
 quiz=[
 ("Parallel lines cut by a transversal. Alternate interior angles are:", ["Congruent", "Supplementary", "Complementary", "Always right angles"], 0, "Alternate interior angles are congruent when the lines are parallel."),
 ("Same side interior angles formed by parallel lines are:", ["Supplementary", "Congruent", "Complementary", "Vertical"], 0, "They add to 180 degrees."),
 ("Alternate interior angles measure 4x + 5 and 2x + 35. The value of x is:", ["15", "10", "20", "30"], 0, "4x + 5 = 2x + 35 gives x = 15."),
 ("If a pair of alternate interior angles is congruent, then the lines are:", ["Parallel", "Perpendicular", "Intersecting at a point", "Skew"], 0, "The converse tells us the lines are parallel."),
 ]),

 dict(t="2.2 Angles of Triangles", std="MA.912.GR.1.3",
 body="""A triangle has three sides and three angles. Triangles can be classified by their sides (scalene: no sides equal, isosceles: at least two sides equal, equilateral: all three sides equal) and by their angles (acute: all acute, right: one right angle, obtuse: one obtuse angle).

Triangle Angle Sum Theorem: The three angles of a triangle add to 180 degrees.

Worked example: A triangle has angles x, 2x + 10 and 3x + 20. Then 6x + 30 = 180, so x = 25 and the angles are 25, 60 and 95 degrees.

Exterior Angle Theorem: An exterior angle of a triangle equals the sum of the two remote interior angles (the two angles not next to it).
Worked example: Remote interior angles are 48 and 62 degrees, so the exterior angle is 110 degrees.

Isosceles Triangle Theorem: If two sides of a triangle are congruent, then the angles opposite those sides are congruent. Its converse is also true.
Worked example: An isosceles triangle has a vertex angle of 40 degrees. The base angles share 140 degrees, so each is 70 degrees.

Triangle Inequality: The sum of any two sides of a triangle must be greater than the third side. Sides 3, 4 and 8 cannot make a triangle, since 3 + 4 is not greater than 8.

Your task: (1) Find the third angle of a triangle with angles 50 and 65 degrees. (2) An exterior angle measures 130 degrees and one remote interior angle is 80 degrees. Find the other remote interior angle. (3) Can sides 5, 7 and 11 form a triangle? Explain.""",
 script="""Now, let us talk about triangles, the strongest and simplest polygon. Builders use triangles in bridges and rooftops because a triangle does not bend out of shape.

First, how we name them. By sides, a scalene triangle has no equal sides, an isosceles triangle has at least two equal sides, and an equilateral triangle has three equal sides. By angles, an acute triangle has all acute angles, a right triangle has one right angle, and an obtuse triangle has one obtuse angle.

Now the big theorem. The Triangle Angle Sum Theorem says the three angles of any triangle add up to one hundred eighty degrees. Always. Let us use it. A triangle has angles x, two x plus ten, and three x plus twenty. Add them, six x plus thirty equals one hundred eighty. Subtract thirty, six x equals one hundred fifty, and x is twenty five. So the angles are twenty five, sixty, and ninety five degrees. Do they add to one hundred eighty? Twenty five plus sixty is eighty five, plus ninety five is one hundred eighty. Yes.

Watch this. The Exterior Angle Theorem. An exterior angle is formed when you extend one side of a triangle. It equals the sum of the two remote interior angles, which are the two angles that are not next to it. If the remote interior angles are forty eight and sixty two, the exterior angle is one hundred ten degrees.

Next, the Isosceles Triangle Theorem. If two sides of a triangle are congruent, then the angles opposite those sides are congruent. We call these the base angles. And the converse is true too. If two angles are congruent, then the sides opposite them are congruent. Suppose the vertex angle is forty degrees. The other two angles share one hundred forty, so each is seventy degrees.

One more rule, the Triangle Inequality. The sum of any two sides must be greater than the third side. If sides are three, four and eight, then three plus four is seven, which is not greater than eight. Those sides cannot meet to make a triangle.

Your task today. Find the third angle of a triangle with angles fifty and sixty five, which is sixty five. Find the missing remote angle when the exterior angle is one hundred thirty and one remote angle is eighty, which is fifty. And decide whether five, seven and eleven make a triangle. Five plus seven is twelve, which is greater than eleven. Check the other pairs too, and you will see that they work. Take the four question check when you finish.

A strong shape is a shape with a purpose. Excellence, Faith, Purpose. I will see you in the next lesson.""" ,
 quiz=[
 ("The angles of a triangle add to:", ["180 degrees", "90 degrees", "360 degrees", "270 degrees"], 0, "The Triangle Angle Sum Theorem."),
 ("A triangle has angles 50 and 65 degrees. The third angle is:", ["65 degrees", "75 degrees", "115 degrees", "130 degrees"], 0, "180 minus 115 is 65."),
 ("An exterior angle equals:", ["The sum of the two remote interior angles", "The third interior angle", "180 degrees", "Twice the vertex angle"], 0, "That is the Exterior Angle Theorem."),
 ("An isosceles triangle has a vertex angle of 40 degrees. Each base angle measures:", ["70 degrees", "40 degrees", "140 degrees", "50 degrees"], 0, "The base angles share 140 degrees equally."),
 ]),

 dict(t="2.3 Proving Triangles Congruent", std="MA.912.GR.1.2",
 body="""Two triangles are congruent if all three pairs of corresponding sides and all three pairs of corresponding angles are congruent. We do not need to check all six pairs. These shortcuts guarantee congruence:

SSS (side, side, side): three pairs of congruent sides.
SAS (side, angle, side): two pairs of congruent sides and the included angle (the angle between them).
ASA (angle, side, angle): two pairs of congruent angles and the included side (the side between them).
AAS (angle, angle, side): two pairs of congruent angles and a non included side.
HL (hypotenuse, leg): for right triangles only, a congruent hypotenuse and a congruent leg.

These do NOT prove congruence: AAA (equal angles give the same shape, not necessarily the same size) and SSA (the angle is not between the sides).

Helpful facts: A shared side is congruent to itself by the Reflexive Property. Vertical angles are congruent. Parallel lines give congruent alternate interior angles. A midpoint splits a segment into two congruent parts.

Worked example: Triangle ABC has AB = 5, BC = 7, angle B = 40 degrees. Triangle DEF has DE = 5, EF = 7, angle E = 40 degrees. The angle is between the two sides in each triangle, so the triangles are congruent by SAS.

Your task: (1) Name the shortcut: two pairs of congruent angles and the side between them. (2) Triangles have sides 6, 8, 10 and 6, 8, 10. Which shortcut applies? (3) Why does AAA not prove congruence?""",
 script="""Listen, two figures are congruent when they have exactly the same size and the same shape. One can be moved onto the other, with a slide, a turn or a flip, and match perfectly. For triangles that means all three sides and all three angles match. But we do not have to check all six pairs. There are shortcuts, and today we learn five of them.

The first is SSS, side side side. If three sides of one triangle are congruent to three sides of another, the triangles are congruent. The second is SAS, side angle side. Two sides and the angle between them. The word between is very important. The angle must be the included angle, the one formed by those two sides.

Watch this. The third is ASA, angle side angle. Two angles and the side between them. The fourth is AAS, angle angle side. Two angles and a side that is not between them. And the fifth is HL, hypotenuse leg, which works only for right triangles. If the hypotenuse and one leg of one right triangle match those of another, the triangles are congruent.

Now, two warnings. AAA does not prove congruence. Two triangles can have the same three angles and be very different sizes, like a small triangle and a giant one with the same shape. Those are similar, which we study later, but not congruent. And SSA does not work either. The angle is not between the sides, so the triangle can be built two different ways.

Here are four helpful facts. A side shared by both triangles is congruent to itself, by the Reflexive Property. Vertical angles are congruent. Parallel lines make alternate interior angles congruent. And a midpoint cuts a segment into two congruent pieces.

Let us practice. Triangle A B C has A B equal to five, B C equal to seven, and angle B equal to forty degrees. Triangle D E F has D E equal to five, E F equal to seven, and angle E equal to forty degrees. The angle is between the two sides in each triangle. So the triangles are congruent by SAS.

Your task today. Name the shortcut for two angles and the side between them, which is ASA. Triangles with sides six, eight, ten and six, eight, ten are congruent by SSS. And explain why AAA fails. Take the four question check when you finish.

Be exact, and what you build will last. Excellence, Faith, Purpose. I will see you in the next lesson.""" ,
 quiz=[
 ("Two sides and the included angle of one triangle match those of another. The shortcut is:", ["SAS", "SSA", "AAA", "ASA"], 0, "SAS uses two sides and the angle between them."),
 ("Which shortcut is used only for right triangles?", ["HL", "SAS", "ASA", "SSS"], 0, "HL means hypotenuse and leg."),
 ("Which does NOT prove triangles congruent?", ["AAA", "SSS", "ASA", "AAS"], 0, "AAA gives similar triangles, not necessarily congruent ones."),
 ("A side shared by two triangles is congruent to itself by the:", ["Reflexive Property", "Transitive Property", "Symmetric Property", "Distributive Property"], 0, "A segment equals itself: the Reflexive Property."),
 ]),

 dict(t="2.4 Proofs with Congruent Triangles", std="MA.912.GR.1.2, MA.912.GR.1.3, MA.912.GR.1.6",
 body="""A proof is a logical argument that shows a statement is true. A two column proof lists statements on the left and a reason for each on the right. Reasons are definitions, given information, properties and theorems.

CPCTC means Corresponding Parts of Congruent Triangles are Congruent. Once you prove two triangles congruent, you may conclude that any pair of their corresponding sides or angles are congruent.

Proof 1: Segments AB and CD cross at E. E is the midpoint of both. Prove triangle AEC is congruent to triangle BED.
Statement 1: AE = EB. Reason: E is the midpoint of AB (given).
Statement 2: CE = ED. Reason: E is the midpoint of CD (given).
Statement 3: Angle AEC = angle BED. Reason: Vertical angles are congruent.
Statement 4: Triangle AEC is congruent to triangle BED. Reason: SAS.
Statement 5: AC = BD. Reason: CPCTC.

Proof 2 (Isosceles Triangle Theorem): Given AB = AC in triangle ABC. Prove angle B = angle C. Draw the angle bisector from A to point D on BC. Then AB = AC (given), angle BAD = angle CAD (definition of angle bisector), AD = AD (Reflexive Property). So triangle ABD is congruent to triangle ACD by SAS, and angle B = angle C by CPCTC.

Strategy: (1) Mark the given information on a sketch. (2) Look for shared sides, vertical angles and parallel lines. (3) Choose a shortcut. (4) Write the proof. (5) Use CPCTC for the final goal.

Your task: Segments PQ and RS bisect each other at T (T is the midpoint of both). Prove triangle PTR is congruent to triangle QTS, and then explain why PR = QS.""",
 script="""Now we put it all together. A proof is a logical argument that shows a statement must be true. In geometry the most common form is the two column proof. On the left, statements. On the right, a reason for each. Every reason must be a definition, a given fact, a property or a theorem you already know. No guessing.

There is one more tool you need, CPCTC. It stands for Corresponding Parts of Congruent Triangles are Congruent. It works like this. Once you have proved two triangles congruent, every pair of matching sides and matching angles is congruent. So CPCTC is how we get to the final goal of a proof, after we use a shortcut like SAS to prove the triangles congruent.

Let us walk through Proof 1. Segments A B and C D cross at point E. And E is the midpoint of both. We want to prove triangle A E C is congruent to triangle B E D. Statement one, A E equals E B, because E is the midpoint of A B. That was given. Statement two, C E equals E D, because E is the midpoint of C D, also given. Statement three, angle A E C equals angle B E D, because vertical angles are congruent. Statement four, the triangles are congruent by SAS, because two sides and the included angle match. Statement five, A C equals B D by CPCTC.

Watch this. Now the Isosceles Triangle Theorem. We are told A B equals A C. We want angle B equals angle C. We draw the angle bisector from A to a point D on side B C. Now we have two triangles, A B D and A C D. A B equals A C, given. Angle B A D equals angle C A D, by the definition of an angle bisector. A D equals A D, by the Reflexive Property. So the triangles are congruent by SAS, and angle B equals angle C by CPCTC. We just proved a theorem we have been using.

Here is a strategy for any proof. One, mark the given information on a sketch. Two, look for shared sides, vertical angles and parallel lines. Three, choose a shortcut, SSS, SAS, ASA, AAS or HL. Four, write the proof line by line. Five, finish with CPCTC if the goal is about sides or angles.

Your task today. Segments P Q and R S bisect each other at T. Prove triangle P T R is congruent to triangle Q T S. P T equals T Q and R T equals T S, since T is the midpoint of both. Angle P T R equals angle Q T S, since they are vertical. So the triangles are congruent by SAS. Then P R equals Q S by CPCTC. Take the four question check when you finish.

A true proof is a gift. It gives everyone who follows a reason to believe. Excellence, Faith, Purpose. I will see you in the next lesson.""" ,
 quiz=[
 ("CPCTC stands for:", ["Corresponding Parts of Congruent Triangles are Congruent", "Congruent Parts of Corresponding Triangles are Congruent", "Common Parts of Corresponding Triangles Congruent", "Corresponding Points of Congruent Triangles Compared"], 0, "CPCTC is a reason used after triangles are proved congruent."),
 ("In a two column proof, the right column contains:", ["Reasons", "Diagrams", "Answers only", "Guesses"], 0, "Each statement needs a reason."),
 ("When two segments bisect each other at E, what does E do?", ["Is the midpoint of both segments", "Makes the segments parallel", "Makes the segments unequal", "Is outside the segments"], 0, "A bisector cuts a segment into two congruent parts at its midpoint."),
 ("Which reason justifies angle AEC = angle BED when lines cross at E?", ["Vertical angles are congruent", "SSS", "Definition of a circle", "Parallel lines"], 0, "Vertical angles formed by crossing lines are congruent."),
 ]),
 ],
 assess=dict(t="Assessment 2: Parallel Lines, Triangles and Proof",
 prompt="""Complete all parts, showing your work and explaining your reasoning.

Part A: Parallel lines are cut by a transversal. A pair of alternate interior angles measures 6x + 8 and 4x + 30 degrees. Find x and the measure of each angle. Then name one pair of same side interior angles and state their measure.

Part B: A triangle has angles measuring x, 3x minus 10, and 2x plus 10 degrees. Find x and all three angles. Classify the triangle by its angles.

Part C: Triangle ABC is isosceles with AB = AC and angle A = 50 degrees. Find angle B and angle C. An exterior angle is formed at C by extending BC. Find that exterior angle two ways: using the Exterior Angle Theorem, and using a linear pair.

Part D: In a two column proof, prove this: Given that segment WX is congruent to segment YZ and that angle WXZ is congruent to angle YZX, with the segment XZ shared by triangles WXZ and YZX, prove that triangle WXZ is congruent to triangle YZX. Name the shortcut you used and explain why each statement is true.""",
 rubric="""100 points. Part A, correct x, both angles and same side interior pair: 25 points. Part B, correct x, angles and classification: 20 points. Part C, base angles, both exterior angle methods agree: 25 points. Part D, valid proof with correct statements, reasons and shortcut: 20 points. Clear work and complete sentences: 10 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 2: Building on a Firm Foundation",
 prompt="""Every proof builds on earlier facts. Write a post of at least 120 words that (1) explains in your own words why a proof must start with given information and known theorems, (2) describes a time in life when building step by step on a solid foundation mattered, (3) tells which idea from this unit, such as parallel lines, triangle angle sum, or congruence shortcuts, you found most interesting and why, and (4) connects your answer to Matthew 7:24, where the wise man 'built his house upon a rock.' Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why can one weak step ruin a whole proof? Keep your language clean and your tone kind."""),
 unit_quiz=[
 ("Parallel lines are cut by a transversal. Corresponding angles are:", ["Congruent", "Supplementary", "Complementary", "Vertical"], 0, "Corresponding angles are congruent when the lines are parallel."),
 ("Same side interior angles for parallel lines add to:", ["180 degrees", "90 degrees", "360 degrees", "60 degrees"], 0, "They are supplementary."),
 ("A triangle has angles 40 and 85 degrees. The third angle is:", ["55 degrees", "45 degrees", "65 degrees", "95 degrees"], 0, "180 minus 125 is 55."),
 ("An exterior angle of a triangle is 120 degrees. One remote interior angle is 45 degrees. The other is:", ["75 degrees", "60 degrees", "165 degrees", "45 degrees"], 0, "120 minus 45 is 75."),
 ("Which sides can form a triangle?", ["5, 6 and 10", "2, 3 and 8", "1, 2 and 3", "4, 4 and 9"], 0, "5 + 6 is greater than 10, and the other pairs also work."),
 ("Which shortcut proves triangles congruent using two angles and the side between them?", ["ASA", "SSA", "AAA", "SSS"], 0, "Angle, side, angle."),
 ("Which is NOT a valid way to prove triangles congruent?", ["SSA", "SSS", "SAS", "ASA"], 0, "SSA does not work in general."),
 ("After proving two triangles congruent, you can conclude that other corresponding parts are congruent by:", ["CPCTC", "Reflexive Property", "AAA", "Converse"], 0, "CPCTC lets you use corresponding parts."),
 ])
