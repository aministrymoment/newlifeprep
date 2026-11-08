"""Biology 1 final module: final assessment (position 7) and final exam (quiz position 31)."""

FINAL_ASSESS = dict(t="Final Assessment: Stewardship Science Investigation",
 prompt="""Plan and report a science investigation about a living system near your home, school or church, such as a garden, a pond, a tree, a yard or a schoolyard. Show your work, label each part and write complete sentences. Psalm 111:2 says, The works of the LORD are great, sought out of all them that have pleasure therein. Seek out the works of the Lord with care and joy.

Part 1: Question and Hypothesis. State a testable question about the living system and a hypothesis with a reason. Name the independent variable, the dependent variable, at least three controlled variables and a control group.

Part 2: Procedure and Data. Write a numbered procedure that another student could repeat. Include a data table with at least three trials or three sample sites and a safe way to collect data. Invent realistic sample data if you cannot collect it, and say that it is sample data. Find an average for each group and make a labeled graph.

Part 3: Cells and Chemistry. Choose one organism in your system. Name its cell type, three organelles that matter to its life, and one biomolecule it uses. Tell how water helps it survive.

Part 4: Energy and Matter. Show how energy and one cycled element (carbon or nitrogen) move through your system. Write the photosynthesis and cellular respiration equations in words and tell where each occurs.

Part 5: Heredity and Change. Give one trait of an organism in your system and show a Punnett square for a cross that could produce it. Explain how variation and natural selection could change the population over many generations.

Part 6: Ecology and Stewardship. Draw or describe a food web with at least six organisms. Tell what the carrying capacity depends on and one way people help or harm the system. Write three actions for stewardship, using Genesis 2:15, which says, And the LORD God took the man, and put him into the garden of Eden to dress it and to keep it.

Part 7: Reflection. In at least 100 words, explain what this course taught you about the wisdom of God in creation, the value of honest evidence, and your responsibility to care for living things.""",
 rubric="""200 points. Part 1, question and hypothesis: 24 points. Part 2, procedure, data and graph: 36 points. Part 3, cells and chemistry: 28 points. Part 4, energy and matter: 30 points. Part 5, heredity and change: 28 points. Part 6, ecology and stewardship: 32 points. Part 7, reflection: 14 points. Clear organization and complete sentences: 8 points. A score of 140 or above is passing."""
)

FINAL_EXAM = [
 ("A testable explanation or prediction in science is called a:", ["Hypothesis", "Conclusion", "Variable", "Theory"], 0, "A hypothesis is a testable explanation or prediction that evidence can support or reject."),
 ("In an experiment on fertilizer and plant height, the plant height is the:", ["Dependent variable", "Independent variable", "Control group", "Constant"], 0, "The dependent variable is measured as the response."),
 ("The special properties of water, such as cohesion and a high specific heat, result from:", ["Hydrogen bonds", "Peptide bonds", "Chlorophyll", "Mutations"], 0, "Polar water molecules form hydrogen bonds that cause these properties."),
 ("The monomers of proteins are:", ["Amino acids", "Nucleotides", "Simple sugars", "Fatty acids"], 0, "Proteins are chains of amino acids."),
 ("Which organelle is the site of most ATP production in a cell?", ["Mitochondrion", "Ribosome", "Golgi apparatus", "Lysosome"], 0, "Mitochondria carry out most of cellular respiration."),
 ("A red blood cell placed in pure water is in a hypotonic solution and will:", ["Take in water and swell", "Lose water and shrivel", "Stay the same", "Divide"], 0, "There is less solute outside, so water moves into the cell."),
 ("The stage of mitosis in which chromosomes line up in the middle of the cell is:", ["Metaphase", "Prophase", "Anaphase", "Telophase"], 0, "Chromosomes align in the middle during metaphase."),
 ("The overall reaction of photosynthesis uses carbon dioxide, water and light to make:", ["Glucose and oxygen", "ATP and water only", "Lactic acid", "Proteins and DNA"], 0, "Photosynthesis produces glucose and releases oxygen."),
 ("Which process produces the most ATP from a molecule of glucose?", ["Aerobic respiration", "Glycolysis alone", "Fermentation", "Photosynthesis"], 0, "Aerobic respiration yields about 36 to 38 ATP."),
 ("If the DNA template reads TACGGA, the mRNA will read:", ["AUGCCU", "ATGCCT", "UACGGA", "AUGGGA"], 0, "mRNA is complementary to the template and uses uracil instead of thymine."),
 ("Two heterozygous parents (Aa times Aa) have a child. The chance that the child is aa is:", ["25 percent", "50 percent", "75 percent", "100 percent"], 0, "The Punnett square gives 1 AA, 2 Aa and 1 aa."),
 ("Which is a source of genetic variation in sexual reproduction?", ["Crossing over", "Cytokinesis", "Osmosis", "Photosynthesis"], 0, "Crossing over shuffles alleles between homologous chromosomes."),
 ("Natural selection results in a population in which:", ["Helpful inherited traits become more common", "All traits stay the same forever", "Individuals change by wanting to", "Mutations stop"], 0, "Individuals with helpful traits survive and leave more offspring."),
 ("In the scientific name Homo sapiens, sapiens is the:", ["Species", "Genus", "Family", "Domain"], 0, "The second word of a binomial name is the species."),
 ("In a food chain, about how much of the energy at one trophic level reaches the next?", ["10 percent", "50 percent", "90 percent", "100 percent"], 0, "About 10 percent is passed on and the rest is used or lost as heat."),
]
