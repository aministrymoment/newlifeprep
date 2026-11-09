"""Physical Science, Unit 2: Atoms and the Periodic Table. Florida NGSSS Physical Science (SC.912.P.8) cited at strand level; recheck exact benchmark codes at CPALMS."""
from psc_units1 import CLOSE

UNIT2 = dict(
 title="Unit 2: Atoms and the Periodic Table",
 std="SC.912.P.8",
 topics=[
 dict(t="2.1 Atomic Structure and Isotopes", std="SC.912.P.8",
 body="""Everything you can touch is built from tiny particles. Hebrews 11:3 says, Through faith we understand that the worlds were framed by the word of God, so that things which are seen were not made of things which do appear. Atoms are too small to see, yet they are the building blocks of the visible world.

An atom has a small, dense center called the nucleus, which holds protons and neutrons. A proton has a positive charge. A neutron has no charge. Electrons have a negative charge and move around the nucleus in a region called the electron cloud. A proton and a neutron each have a mass of about 1 atomic mass unit, while an electron has only about one eighteen hundredth of that. An atom is mostly empty space.

Our picture of the atom grew over time. Dalton described atoms as tiny solid spheres. Thomson discovered the electron. Rutherford shot particles at gold foil and found that most passed straight through while a few bounced back, which showed a tiny dense nucleus. Bohr proposed energy levels, and the modern model describes an electron cloud.

The atomic number is the number of protons, and it identifies the element. The mass number is the number of protons plus the number of neutrons. A neutral atom has equal numbers of protons and electrons. Sodium has atomic number 11 and mass number 23, so it has 11 protons, 11 electrons and 23 minus 11, or 12, neutrons.

Isotopes are atoms of the same element with different numbers of neutrons. Carbon 12 has 6 protons and 6 neutrons. Carbon 14 has 6 protons and 8 neutrons. The atomic mass on the periodic table is an average of the isotopes. An ion forms when an atom gains or loses electrons. Losing an electron makes a positive ion, and gaining one makes a negative ion.

Your task: (1) Name the three particles and their charges. (2) Find protons, neutrons and electrons from the atomic number and mass number. (3) Explain what an isotope is.""",
 script="""Welcome back. Listen, Hebrews 11:3 says, Through faith we understand that the worlds were framed by the word of God, so that things which are seen were not made of things which do appear. Atoms are too small to see, yet they build the visible world.

Now watch this. The nucleus holds protons, which are positive, and neutrons, which have no charge. Electrons are negative and move around the nucleus in an electron cloud. An atom is mostly empty space. Rutherford learned this when most particles passed straight through gold foil and a few bounced back.

Look at the numbers. The atomic number is the number of protons, and it identifies the element. The mass number is protons plus neutrons. Sodium has atomic number 11 and mass number 23, so it has 11 protons, 11 electrons and 12 neutrons.

Isotopes are atoms of the same element with different numbers of neutrons. Carbon 12 has 6 neutrons. Carbon 14 has 8. An ion forms when an atom gains or loses electrons.

Your task is to name the particles, find the numbers in an atom and explain isotopes. Take the four question check.""" + CLOSE,
 quiz=[
 ("The particle with a positive charge found in the nucleus is the:", ["Proton", "Neutron", "Electron", "Ion"], 0, "Protons are positive and are in the nucleus."),
 ("An atom has 11 protons and 12 neutrons. Its mass number is:", ["23", "11", "12", "1"], 0, "11 plus 12 equals 23."),
 ("Atoms of the same element with different numbers of neutrons are:", ["Isotopes", "Ions", "Compounds", "Molecules"], 0, "Different neutron counts make isotopes."),
 ("Rutherford's gold foil experiment showed that an atom has:", ["A small dense nucleus", "A solid positive sphere", "No electrons", "Uniform charge throughout"], 0, "A few particles bounced back from a tiny dense nucleus."),
 ]),
 dict(t="2.2 The Periodic Table", std="SC.912.P.8",
 body="""The periodic table is an organized chart of the elements. First Corinthians 14:40 says, Let all things be done decently and in order. Order helps us find patterns, and the periodic table is one of the most useful charts in science.

In 1869 Dmitri Mendeleev arranged the known elements by atomic mass and left gaps for elements not yet discovered, correctly predicting some of their properties. The modern table arranges the elements by increasing atomic number, and 118 elements have been named. Each box shows the symbol, atomic number, name and atomic mass.

A horizontal row is a period, and there are seven. A vertical column is a group or family, and there are eighteen. Elements in the same group have similar chemical properties because they have the same number of valence electrons, the electrons in the outermost energy level.

The table is divided into regions. Metals are on the left and center. They are generally shiny, malleable, ductile and good conductors of heat and electricity. Nonmetals are on the right and are generally dull, brittle as solids and poor conductors. Metalloids lie along the staircase between them and have properties of both. Group 1 contains the alkali metals, which are very reactive. Group 2 contains the alkaline earth metals. Groups 3 to 12 are the transition metals. Group 17 contains the halogens, which are very reactive nonmetals. Group 18 contains the noble gases, which are almost unreactive.

There are also trends. Moving left to right across a period, atoms generally get smaller and hold their electrons more tightly. Moving down a group, atoms get larger because they have more energy levels.

Your task: (1) Tell what a period and a group are. (2) Locate metals, nonmetals and metalloids. (3) Explain why elements in one group behave alike.""",
 script="""Welcome back. Listen, First Corinthians 14:40 says, Let all things be done decently and in order. Order helps us see patterns, and the periodic table is one of the most useful charts in science.

Now watch this. Mendeleev arranged the elements in 1869 by atomic mass and left gaps for elements not yet found, and he predicted some of their properties correctly. The modern table is arranged by atomic number, and 118 elements have been named.

Look at the layout. A horizontal row is a period, and there are seven. A vertical column is a group, and there are eighteen. Elements in a group behave alike because they have the same number of valence electrons.

Metals are on the left and center. They are shiny, malleable and good conductors. Nonmetals are on the right. Metalloids lie along the staircase between them. Group 1 is the alkali metals. Group 17 is the halogens. Group 18 is the noble gases, which almost never react.

Moving down a group, atoms get larger because they have more energy levels.

Your task is to explain periods and groups, locate the regions and explain why a group behaves alike. Take the four question check.""" + CLOSE,
 quiz=[
 ("A horizontal row on the periodic table is called a:", ["Period", "Group", "Block", "Isotope"], 0, "Rows are periods."),
 ("Elements in the same group have similar properties because they have the same number of:", ["Valence electrons", "Neutrons", "Protons", "Total electrons"], 0, "Valence electrons control chemical behavior."),
 ("The elements in Group 18 are the:", ["Noble gases", "Alkali metals", "Halogens", "Transition metals"], 0, "Group 18 holds the noble gases."),
 ("The modern periodic table is arranged by increasing:", ["Atomic number", "Density", "Melting point", "Number of neutrons"], 0, "Atomic number orders the modern table."),
 ]),
 dict(t="2.3 Electrons and Energy Levels", std="SC.912.P.8",
 body="""Electrons are arranged around the nucleus in energy levels, sometimes called shells. Genesis 1:3 says, And God said, Let there be light: and there was light. Light and electrons are closely connected, because atoms give off light when their electrons move between energy levels.

Each energy level can hold only a certain number of electrons. For the first 18 elements, the first level holds up to 2 electrons, the second holds up to 8, and the third holds up to 8. Electrons fill the lowest energy levels first. Sodium has 11 electrons, so its arrangement is 2, 8, 1. Chlorine has 17 electrons, arranged 2, 8, 7. Neon has 10 electrons, arranged 2, 8.

The electrons in the outermost energy level are the valence electrons. They determine how an atom reacts. For the main group elements, the number of valence electrons matches the group number, ignoring the tens digit. Group 1 has one valence electron, group 2 has two, group 17 has seven and group 18 has eight, except helium, which has two. An electron dot diagram shows the symbol with a dot for each valence electron.

Atoms are most stable when the outer level is full, which for many atoms means eight electrons. This is the octet rule. Sodium can lose one electron to reach a full level and becomes a positive ion. Chlorine can gain one electron to reach a full level and becomes a negative ion. Noble gases already have full outer levels, so they rarely react.

When an electron absorbs energy it jumps to a higher level, and when it falls back it releases energy, sometimes as light. Each element releases its own colors, which is why a flame test and a neon sign show different colors for different elements.

Your task: (1) Write the electron arrangement of an element. (2) Find its valence electrons. (3) Predict whether it tends to gain or lose electrons.""",
 script="""Welcome back. Listen, Genesis 1:3 says, And God said, Let there be light: and there was light. Light and electrons are closely connected, because atoms give off light when their electrons move.

Now watch this. Electrons sit in energy levels. For the first 18 elements, the first level holds up to 2 electrons, the second up to 8, and the third up to 8. Sodium has 11 electrons, arranged 2, 8, 1. Chlorine has 17, arranged 2, 8, 7.

The electrons in the outer level are the valence electrons, and they control how an atom reacts. Atoms are most stable with a full outer level, usually 8 electrons. That is the octet rule. Sodium loses one electron and becomes a positive ion. Chlorine gains one and becomes a negative ion. Noble gases already have full outer levels, so they rarely react.

When an electron absorbs energy it jumps up, and when it falls back it releases energy, sometimes as light. That is why a neon sign glows with its own color.

Your task is to write an electron arrangement, find valence electrons and predict gain or loss. Take the four question check.""" + CLOSE,
 quiz=[
 ("The maximum number of electrons in the first energy level is:", ["2", "8", "18", "1"], 0, "The first level holds only 2."),
 ("Sodium has 11 electrons. Its electron arrangement is:", ["2, 8, 1", "2, 9", "8, 3", "2, 2, 7"], 0, "Fill 2, then 8, then the last 1."),
 ("Electrons in the outermost energy level are called:", ["Valence electrons", "Core electrons", "Isotopes", "Nuclear particles"], 0, "Valence electrons are in the outer level."),
 ("An atom with a full outer energy level is generally:", ["Stable and unreactive", "Highly reactive", "Positively charged", "Radioactive"], 0, "A full outer level makes an atom stable."),
 ]),
 dict(t="2.4 Elements, Compounds and Mixtures", std="SC.912.P.8",
 body="""Matter can be sorted by what it is made of. Psalm 104:24 says, O LORD, how manifold are thy works! in wisdom hast thou made them all: the earth is full of thy riches. The variety of materials around us comes from a limited set of elements combined in many ways.

A pure substance has a fixed composition. An element is a pure substance made of only one kind of atom, and it cannot be broken down into simpler substances by chemical means. Examples are gold, oxygen and iron. A compound is a pure substance made of two or more elements chemically combined in a fixed ratio. Water is a compound written H2O, which means two hydrogen atoms for each oxygen atom. Table salt, NaCl, has one sodium atom for each chlorine atom, and carbon dioxide, CO2, has one carbon and two oxygen atoms. A compound has properties different from its elements, and it can be separated only by a chemical change.

A mixture is two or more substances that are together but not chemically combined. Each substance keeps its own properties, and the amounts can vary. A heterogeneous mixture, such as a salad or sand in water, is not evenly mixed. A homogeneous mixture, also called a solution, is evenly mixed throughout. Salt water is a solution, with salt as the solute and water as the solvent. Air is a solution of gases, about 78 percent nitrogen and 21 percent oxygen. Steel is a solid solution of iron and carbon.

Mixtures are separated by physical methods. A magnet pulls iron filings from sand. Filtering separates a solid from a liquid. Evaporation leaves the dissolved salt behind. Distillation separates liquids by their boiling points. Chromatography separates colors in an ink.

Your task: (1) Sort examples into elements, compounds and mixtures. (2) Read a chemical formula. (3) Choose a method to separate a mixture.""",
 script="""Welcome back. Listen, Psalm 104:24 says, O LORD, how manifold are thy works! in wisdom hast thou made them all. The variety around us comes from a limited set of elements combined in many ways.

Now watch this. An element is made of only one kind of atom, like gold or oxygen. A compound is two or more elements chemically combined in a fixed ratio. Water, H2O, has two hydrogen atoms for each oxygen atom. Salt, NaCl, has one sodium for each chlorine. A compound has properties different from its elements and needs a chemical change to separate it.

Look at mixtures. A mixture is substances together but not chemically combined, and each keeps its own properties. A salad is heterogeneous. Salt water is homogeneous, also called a solution, with salt as the solute and water as the solvent. Air is a solution of gases, about 78 percent nitrogen and 21 percent oxygen.

Mixtures are separated by physical methods. A magnet pulls iron from sand. Filtering separates a solid from a liquid. Evaporation leaves salt behind. Distillation separates liquids by boiling point.

Your task is to sort examples, read a formula and choose a separation method. Take the four question check.""" + CLOSE,
 quiz=[
 ("A pure substance made of two or more elements chemically combined is a:", ["Compound", "Mixture", "Solution", "Element"], 0, "A compound has a fixed ratio of elements."),
 ("Salt water is an example of a:", ["Homogeneous mixture", "Compound", "Element", "Heterogeneous mixture"], 0, "Salt water is evenly mixed, so it is a solution."),
 ("Which method best separates iron filings from sand?", ["Using a magnet", "Distillation", "Chemical decomposition", "Evaporation"], 0, "Iron is attracted to a magnet and sand is not."),
 ("The formula H2O shows that water has:", ["2 hydrogen atoms and 1 oxygen atom", "2 oxygen atoms and 1 hydrogen atom", "2 compounds", "1 atom of each element"], 0, "The subscript 2 follows the hydrogen."),
 ]),
 ],
 assess=dict(t="Assessment 2: Atoms and the Periodic Table",
 prompt="""Write a report of at least 250 words on atoms and the periodic table. Use complete sentences, show your work and label each part. Hebrews 11:3 says, Through faith we understand that the worlds were framed by the word of God, so that things which are seen were not made of things which do appear.

Part 1: An atom has atomic number 17 and mass number 35. Find its protons, neutrons and electrons, and tell what element it is.
Part 2: Explain what isotopes are, using carbon 12 and carbon 14 as your example.
Part 3: Describe how the periodic table is organized, define period and group, and explain why sodium and potassium react in similar ways.
Part 4: Write the electron arrangement of magnesium, which has 12 electrons, and of fluorine, which has 9 electrons. Give the valence electrons of each and predict the charge each forms as an ion.
Part 5: Classify salt water, gold, carbon dioxide and a salad as an element, a compound or a mixture, and describe how to separate a mixture of sand, salt and iron filings.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 15 points. Part 3: 20 points. Part 4: 25 points. Part 5: 15 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 2: Order in the Unseen",
 prompt="""Write a post of at least 120 words that (1) describes something you cannot see that you know is real, (2) explains how the order of the periodic table helps scientists predict what elements will do, (3) explains what it teaches us that a few kinds of atoms make up so many materials, and (4) connects your answer to First Corinthians 14:40, Hebrews 11:3 or Psalm 104:24. Then write a respectful reply of at least 40 words to another student's post, or answer this question: How does the order we see in the periodic table point to a wise Creator? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("The atomic number of an element equals its number of:", ["Protons", "Neutrons", "Isotopes", "Energy levels"], 0, "Atomic number counts protons."),
 ("A neutral atom with atomic number 17 has how many electrons?", ["17", "18", "35", "1"], 0, "Neutral atoms have as many electrons as protons."),
 ("Carbon 12 and carbon 14 differ in their number of:", ["Neutrons", "Protons", "Electrons only", "Atomic number"], 0, "They are isotopes with different neutron counts."),
 ("Mendeleev first arranged the elements by:", ["Atomic mass", "Atomic number", "Color", "Date of discovery"], 0, "Mendeleev used atomic mass and left gaps."),
 ("Metals are generally:", ["Good conductors of heat and electricity", "Poor conductors of electricity", "Mostly gases at room temperature", "Always brittle"], 0, "Metals conduct heat and electricity well."),
 ("Chlorine has 7 valence electrons, so it tends to:", ["Gain one electron", "Lose seven electrons", "Share no electrons", "Lose one electron"], 0, "Gaining one electron gives a full outer level."),
 ("Which is a heterogeneous mixture?", ["A salad", "Salt water", "Air", "Steel"], 0, "A salad is not evenly mixed."),
 ("Which cannot be broken down into simpler substances by chemical means?", ["An element", "A compound", "A solution", "A mixture"], 0, "An element is made of one kind of atom."),
 ],
)
