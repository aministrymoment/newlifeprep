"""Chemistry final module: final assessment (position 7) and final exam (quiz position 31)."""

FINAL_ASSESS = dict(t="Final Assessment: My Chemistry Investigation and Reflection",
 prompt="""Create a chemistry investigation report and reflection of at least 700 words. Use a safe home investigation with household materials only, such as dissolving sugar or salt in water at different temperatures, testing how temperature affects how fast a tablet or sugar dissolves, or comparing the density of liquids. You must have adult permission and supervision. Do not use fire, strong cleaners, bleach, ammonia, unknown chemicals or anything that could harm you or others, and never mix household cleaners. If you cannot do an investigation safely, design one and describe the data you would expect. Proverbs 25:2 says, It is the glory of God to conceal a thing: but the honour of kings is to search out a matter.

Part 1: Question and Hypothesis. State your question, background and a testable hypothesis. Identify the independent, dependent and controlled variables.
Part 2: Safety and Materials. List your materials and at least five safety rules. Name the adult who gave permission and supervised.
Part 3: Procedure and Data. Describe your steps in order and show a data table with measurements in SI units. Show at least three trials and the average, with correct significant figures.
Part 4: Analysis. Include at least two calculations, such as density, average, percent difference or percent yield, with your work and units. Describe a graph you would make.
Part 5: Chemistry Connections. Explain which of these ideas apply: physical or chemical change, particles and states of matter, solutions and solubility, energy, or reaction rate. Use correct vocabulary from the course.
Part 6: Conclusion. State whether your data support the hypothesis, describe sources of error and explain how you would improve the investigation.
Part 7: Stewardship and Careers. Explain how you disposed of materials safely and wisely, and describe one chemistry career and one way chemistry can serve people.
Part 8: Faith and Reflection. Apply at least three Scripture passages from the King James Version to the study of God's creation and to honest science, and write a reflection on what you learned, what you will improve and your goal for the next year.""",
 rubric="""100 points. Part 1, question and hypothesis: 10 points. Part 2, safety and materials: 10 points. Part 3, procedure and data: 15 points. Part 4, analysis and calculations: 20 points. Part 5, chemistry connections: 15 points. Part 6, conclusion: 10 points. Part 7, stewardship and careers: 5 points. Part 8, faith and reflection: 10 points. Grammar, conventions and accuracy: 5 points. A score of 70 or above is passing."""
)

FINAL_EXAM = [
 ("Anything that has mass and takes up space is:", ["Matter", "Energy", "A solution", "A reaction"], 0, "That is the definition of matter."),
 ("Which is a chemical change?", ["Iron rusting", "Ice melting", "Water boiling", "Breaking glass"], 0, "Rusting forms a new substance."),
 ("The number of protons in an atom is its:", ["Atomic number", "Mass number", "Charge", "Valence number"], 0, "The atomic number identifies the element."),
 ("Atoms of the same element with different numbers of neutrons are:", ["Isotopes", "Ions", "Compounds", "Isomers"], 0, "Isotopes differ in neutrons."),
 ("Elements in the same group of the periodic table have the same number of:", ["Valence electrons", "Protons", "Neutrons", "Energy levels"], 0, "Valence electrons give similar properties."),
 ("An ionic bond forms when electrons are:", ["Transferred", "Shared equally", "Created", "Destroyed"], 0, "Ionic bonding involves transfer."),
 ("The molecule that has a bent shape is:", ["Water", "Carbon dioxide", "Methane", "Nitrogen gas"], 0, "Two lone pairs bend the water molecule."),
 ("The formula for the compound of magnesium and chlorine is:", ["MgCl2", "MgCl", "Mg2Cl", "Mg2Cl2"], 0, "One 2 plus ion balances two 1 minus ions."),
 ("In a balanced equation, the number of atoms of each element is:", ["The same on both sides", "Greater in the products", "Greater in the reactants", "Not important"], 0, "Mass is conserved."),
 ("One mole of a substance contains:", ["6.02 times 10 to the 23rd particles", "100 particles", "One gram", "22.4 particles"], 0, "That is Avogadro's number."),
 ("The molar mass of water is about:", ["18.0 grams per mole", "16.0 grams per mole", "2.0 grams per mole", "34.0 grams per mole"], 0, "2 hydrogen plus 1 oxygen."),
 ("According to Boyle's law, if the volume of a gas decreases at constant temperature, pressure:", ["Increases", "Decreases", "Stays the same", "Becomes zero"], 0, "Pressure and volume are inversely related."),
 ("A solution has a pH of 3. It is:", ["Acidic", "Neutral", "Basic", "A metal"], 0, "Below 7 is acidic."),
 ("In a redox reaction, the substance that loses electrons is:", ["Oxidized", "Reduced", "Neutralized", "Condensed"], 0, "Oxidation is loss of electrons."),
 ("Psalm 24:1 says, The earth is the LORD'S, and the fulness thereof. This teaches us to practice:", ["Stewardship of creation", "Wasting resources", "Ignoring safety", "Avoiding science"], 0, "Creation belongs to God and we care for it."),
]
