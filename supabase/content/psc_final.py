"""Physical Science final module: final assessment (position 7) and final exam (quiz position 31)."""

FINAL_ASSESS = dict(t="Final Assessment: Physical Science Investigation Report",
 prompt="""Complete a safe investigation and write a report of at least 600 words. Ask a parent, guardian or teacher for permission and supervision before you begin. Use only everyday household items. Do not use open flames, unknown chemicals, household electrical outlets or anything that could cause harm. If you choose a circuit, use only a small battery of 9 volts or less. Choose one question: (a) Which household objects float or sink, and what are their densities? (b) How does the container affect how fast hot water cools? (c) How does the height of a ramp change the speed or acceleration of a toy car? (d) How do series and parallel arrangements change the brightness of small bulbs on a low voltage battery? Write complete sentences, show every calculation and label each part. Proverbs 25:2 says, It is the glory of God to conceal a thing: but the honour of kings is to search out a matter.

Part 1: The Question and Hypothesis. State your question and your hypothesis, and explain the science that led to your prediction.
Part 2: Plan and Safety. List your materials, your independent variable, dependent variable and at least three controls. List the safety rules you followed and how an adult supervised.
Part 3: Procedure. Describe your steps clearly enough that another student could repeat them.
Part 4: Data. Present at least 5 trials or measurements in a table with units, and make a graph or chart.
Part 5: Calculations. Show at least three calculations with units, such as density, speed, acceleration, work, power, energy, heat or current, and apply the correct formula to each.
Part 6: Analysis. Tell what your data show, name the physical science principles involved (such as density, Newton's laws, energy conservation, heat transfer or Ohm's law), and compare your result with your hypothesis.
Part 7: Sources of Error. Describe at least three sources of error and how you could improve the test.
Part 8: Faith and Application. Explain how Psalm 111:2 and Proverbs 11:1 guide honest, careful science, and describe how you could use physical science in a future calling.""",
 rubric="""100 points. Part 1, question and hypothesis: 10 points. Part 2, plan and safety: 15 points. Part 3, procedure: 10 points. Part 4, data: 15 points. Part 5, calculations: 15 points. Part 6, analysis: 15 points. Part 7, sources of error: 5 points. Part 8, faith and application: 10 points. Grammar, conventions and respectful tone: 5 points. A score of 70 or above is passing."""
)

FINAL_EXAM = [
 ("In a fair test, the variable you deliberately change is the:", ["Independent variable", "Dependent variable", "Control", "Conclusion"], 0, "The independent variable is the one you change."),
 ("A sample has a mass of 60 g and a volume of 20 cubic centimeters. Its density is:", ["3 g per cubic centimeter", "0.33 g per cubic centimeter", "80 g per cubic centimeter", "40 g per cubic centimeter"], 0, "60 divided by 20 equals 3."),
 ("A gas changing directly into a solid, as frost forms, is called:", ["Deposition", "Sublimation", "Condensation", "Melting"], 0, "Gas to solid is deposition."),
 ("An atom has 8 protons and 8 neutrons. Its mass number is:", ["16", "8", "24", "0"], 0, "8 plus 8 equals 16."),
 ("Elements in the same group of the periodic table have the same number of:", ["Valence electrons", "Neutrons", "Total electrons", "Energy levels"], 0, "Valence electrons give similar chemical behavior."),
 ("Which pair of elements forms an ionic bond?", ["Sodium and chlorine", "Hydrogen and oxygen", "Carbon and oxygen", "Nitrogen and nitrogen"], 0, "A metal gives an electron to a nonmetal."),
 ("In the balanced equation 2H2 + O2 yields 2H2O, how many hydrogen atoms are on each side?", ["4", "2", "6", "1"], 0, "2 times 2 equals 4 on each side."),
 ("A solution with a pH of 10 is:", ["Basic", "Acidic", "Neutral", "Impossible to classify"], 0, "A pH above 7 is basic."),
 ("A car travels 120 km in 2 hours. Its average speed is:", ["60 km/h", "240 km/h", "122 km/h", "0.017 km/h"], 0, "120 divided by 2 equals 60."),
 ("A 5 kg object accelerates at 2 m/s squared. The net force is:", ["10 N", "2.5 N", "7 N", "0.4 N"], 0, "Force equals 5 times 2."),
 ("A 2 kg object moves at 4 m/s. Its kinetic energy is:", ["16 J", "8 J", "32 J", "4 J"], 0, "One half times 2 times 16 equals 16."),
 ("A lever, a pulley and an inclined plane are all examples of:", ["Simple machines", "Compounds", "Waves", "Circuits"], 0, "These are three of the six simple machines."),
 ("Heat transferred through empty space by waves is:", ["Radiation", "Conduction", "Convection", "Condensation"], 0, "Radiation does not need a medium."),
 ("A wave has a frequency of 10 Hz and a wavelength of 3 m. Its speed is:", ["30 m/s", "3.3 m/s", "13 m/s", "7 m/s"], 0, "Speed equals 10 times 3."),
 ("A 12 volt battery drives current through a 6 ohm resistor. The current is:", ["2 A", "72 A", "18 A", "0.5 A"], 0, "12 divided by 6 equals 2."),
]
