"""Geometry final module: final assessment (position 7) and final exam (quiz position 31)."""

FINAL_ASSESS = dict(t="Final Assessment: Community Garden Design Project",
 prompt="""Design a community garden for a church or neighborhood. Show all work, label each part, and write complete sentences. Luke 14:28 says, For which of you, intending to build a tower, sitteth not down first, and counteth the cost, whether he have sufficient to finish it? A good plan counts the cost before it builds. Use the geometry you learned in this course to count yours.

Part 1: Lot and Layout. The garden lot has corners A(0, 0), B(40, 0), C(40, 30) and D(0, 30), measured in feet. Use slopes to show that ABCD is a rectangle. Use the distance formula to show that its diagonals are congruent. Find the perimeter and area of the lot. Then place a trapezoid shaped path with bases of 18 feet and 30 feet and a height of 6 feet, and find its midsegment and its area.

Part 2: Right Triangles. A triangular flower bed has legs of 12 feet and 16 feet. Find the length of its hypotenuse and its area. A wheelchair ramp must rise 2 feet at an angle of 5 degrees with the ground. Use sin 5 degrees = 0.0872 to find the length of the ramp to the nearest tenth of a foot. Find the horizontal distance the ramp covers by using tan 5 degrees = 0.0875.

Part 3: Circles. A circular fountain has its center at (20, 15) and a radius of 4 feet. Write its equation and tell whether the point (24, 15) is on the circle. Find the area of the fountain in terms of π. A sector shaped flower bed has a central angle of 90 degrees and a radius of 10 feet. Find its arc length and its area in terms of π.

Part 4: Scale and Transformations. A scale model of the lot uses a scale factor of 1/20. Find the model's length and width in feet, and explain how the model's area compares to the real area. Triangle PQR has P(2, 2), Q(6, 2) and R(6, 5). Describe a reflection across the y axis and a translation that maps it to a new bed, and explain why the new bed is congruent to the original.

Part 5: Volume. A cylindrical water tank has a radius of 3 feet and a height of 5 feet. Find its volume and its total surface area in terms of π. Estimate how many cubic feet of soil are needed to fill a rectangular raised bed that is 8 feet long, 4 feet wide and 2 feet deep.

Part 6: Reflection. In at least 100 words, explain which geometric idea helped you the most in planning this garden, how counting the cost protects people, and how your plan could serve your community.""",
 rubric="""100 points. Part 1, rectangle proof, perimeter, area, midsegment and trapezoid area: 20 points. Part 2, hypotenuse, area, ramp length and horizontal distance: 18 points. Part 3, circle equation, point check, areas, arc length and sector: 18 points. Part 4, scale model, area ratio and transformation description: 16 points. Part 5, volume, surface area and soil estimate: 14 points. Part 6, reflection of at least 100 words: 10 points. Clear work and complete sentences: 4 points. A score of 70 or above is passing.""")

FINAL_EXAM = [
 ("Parallel lines are cut by a transversal. Alternate interior angles are:", ["Congruent", "Supplementary", "Complementary", "Always right angles"], 0, "Alternate interior angles are congruent when the lines are parallel."),
 ("A triangle has angles of 50 and 65 degrees. The third angle is:", ["65 degrees", "75 degrees", "115 degrees", "130 degrees"], 0, "The angles of a triangle add to 180, and 180 minus 115 is 65."),
 ("Two sides and the included angle of one triangle match those of another. The triangles are congruent by:", ["SAS", "SSA", "AAA", "HL"], 0, "SAS uses two sides and the angle between them."),
 ("The interior angles of a hexagon add to:", ["720 degrees", "360 degrees", "540 degrees", "1080 degrees"], 0, "(6 minus 2) times 180 is 720."),
 ("The diagonals of a rhombus are:", ["Perpendicular", "Always congruent", "Parallel", "Always unequal"], 0, "A rhombus has perpendicular diagonals."),
 ("The bases of a trapezoid are 10 and 18. The midsegment is:", ["14", "28", "8", "7"], 0, "(10 + 18) divided by 2 is 14."),
 ("The point (3, 2) is reflected across the y axis. Its image is:", ["(negative 3, 2)", "(3, negative 2)", "(2, 3)", "(negative 3, negative 2)"], 0, "Reflecting across the y axis changes the sign of x."),
 ("A figure is dilated with scale factor 3. Its area is multiplied by:", ["9", "3", "6", "27"], 0, "Area is multiplied by k squared, and 3 squared is 9."),
 ("Triangle ABC is similar to triangle DEF with AB = 4, DE = 10 and BC = 6. Then EF is:", ["15", "12", "9", "24"], 0, "The scale factor is 10/4 = 2.5, and 6 times 2.5 is 15."),
 ("A right triangle has legs 9 and 12. The hypotenuse is:", ["15", "21", "13", "17"], 0, "81 + 144 = 225, and the square root of 225 is 15."),
 ("In a 30 60 90 triangle the short leg is 5. The hypotenuse is:", ["10", "5√3", "5√2", "15"], 0, "The hypotenuse is twice the short leg."),
 ("In a right triangle with sides 5, 12 and 13, the tangent of the angle opposite the side 5 is:", ["5/12", "12/5", "5/13", "12/13"], 0, "Tangent is opposite divided by adjacent."),
 ("An inscribed angle intercepts an arc of 120 degrees. The inscribed angle measures:", ["60 degrees", "120 degrees", "240 degrees", "30 degrees"], 0, "An inscribed angle is half its intercepted arc."),
 ("The circle (x minus 2) squared + (y minus 3) squared = 16 has radius:", ["4", "16", "2", "3"], 0, "The radius is the square root of 16."),
 ("The volume of a sphere with radius 3 is:", ["36π", "12π", "108π", "27π"], 0, "(4/3) times π times 27 is 36π."),
]
