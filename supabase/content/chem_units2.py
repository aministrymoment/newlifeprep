"""Chemistry, Unit 2: Atomic Structure and the Periodic Table. Florida science standards cited at strand level (SC.912.P); recheck exact benchmark codes at CPALMS."""
from chem_units1 import CLOSE

UNIT2 = dict(
 title="Unit 2: Atomic Structure and the Periodic Table",
 std="SC.912.P.8",
 topics=[
 dict(t="2.1 The Atom and Its Subatomic Particles", std="SC.912.P.8",
 body="""All matter is made of atoms, extremely small particles that are the building blocks of elements. Psalm 147:4 says, He telleth the number of the stars; he calleth them all by their names. The God who knows the stars also designed the tiny atoms of which they are made.

Our understanding of the atom developed over time. John Dalton proposed that elements are made of tiny indivisible atoms and that atoms of different elements differ. J. J. Thomson discovered the electron, a tiny negative particle. Ernest Rutherford showed that most of an atom is empty space, with a small, dense, positive center called the nucleus. Niels Bohr described electrons moving in energy levels around the nucleus. The modern quantum model describes regions of space called orbitals where electrons are most likely to be found.

An atom has three main subatomic particles. A proton has a positive charge and is found in the nucleus. A neutron has no charge and is also in the nucleus. An electron has a negative charge and moves around the nucleus. Protons and neutrons each have a mass of about 1 atomic mass unit, while an electron has a very small mass, about one eighteen hundredth as much. The number of protons is the atomic number, and it identifies the element. In a neutral atom the number of electrons equals the number of protons.

An ion is an atom that has gained or lost electrons. Losing electrons makes a positive ion called a cation, and gaining electrons makes a negative ion called an anion.

Your task: (1) Describe the charge and location of the proton, neutron and electron. (2) Explain what the atomic number tells you. (3) Explain how Rutherford discovered the nucleus.""",
 script="""Welcome back. Listen, Psalm 147:4 says, He telleth the number of the stars; he calleth them all by their names. The God who knows the stars also designed the tiny atoms of which they are made.

Now watch this. Dalton said elements are made of atoms. Thomson discovered the electron. Rutherford showed that most of an atom is empty space with a small, dense, positive nucleus. Bohr described energy levels. The modern model uses orbitals, regions where electrons are likely to be.

Three subatomic particles. The proton is positive and in the nucleus. The neutron has no charge and is in the nucleus. The electron is negative and moves around the nucleus. Protons and neutrons each have a mass of about 1 atomic mass unit. Electrons are far lighter. The number of protons is the atomic number and it identifies the element. A neutral atom has equal protons and electrons.

An ion has gained or lost electrons. A cation is positive. An anion is negative.

Your task is to describe the three particles, explain the atomic number and explain Rutherford's discovery. Take the four question check.""" + CLOSE,
 quiz=[
 ("A particle in the nucleus with a positive charge is the:", ["Proton", "Electron", "Neutron", "Anion"], 0, "Protons are positive and in the nucleus."),
 ("The atomic number equals the number of:", ["Protons", "Neutrons", "Electrons plus neutrons", "Orbitals"], 0, "The number of protons defines the element."),
 ("Rutherford showed that an atom has:", ["A small, dense, positive nucleus", "Evenly spread positive charge", "No empty space", "No electrons"], 0, "His gold foil experiment revealed the nucleus."),
 ("An atom that loses electrons becomes a:", ["Cation", "Anion", "Neutron", "Isotope"], 0, "Losing negative charge leaves a positive ion."),
 ]),
 dict(t="2.2 Isotopes and Atomic Mass", std="SC.912.P.8",
 body="""Every atom of a given element has the same number of protons, but the number of neutrons can differ. Atoms of the same element with different numbers of neutrons are called isotopes. Carbon always has 6 protons, but carbon 12 has 6 neutrons and carbon 14 has 8 neutrons. Isotopes of an element have nearly identical chemical properties but different masses. Some isotopes are radioactive.

The mass number is the total number of protons plus neutrons in the nucleus of one atom. To find the number of neutrons, subtract the atomic number from the mass number. An atom of chlorine with a mass number of 35 and an atomic number of 17 has 18 neutrons. Isotopes can be written with the element name and mass number, such as chlorine 35, or with symbols showing the mass number above and the atomic number below.

The atomic mass shown on the periodic table is a weighted average of the masses of an element's naturally occurring isotopes, measured in atomic mass units. If chlorine is about 76 percent chlorine 35 and about 24 percent chlorine 37, the average atomic mass is about 35.5. To calculate it, multiply each isotope's mass by its fractional abundance and add the results. Matthew 10:30 says, But the very hairs of your head are all numbered. Our Creator knows even the smallest details of what He has made.

Isotopes have many uses. Carbon 14 helps date ancient organic materials, iodine isotopes are used in medicine for the thyroid, and cobalt 60 is used in some cancer treatments. These tools should be used wisely and for human good.

Your task: (1) Define isotope. (2) Find the number of protons, neutrons and electrons in a neutral atom with atomic number 11 and mass number 23. (3) Calculate the average atomic mass of an element with 50 percent of an isotope of mass 10 and 50 percent of an isotope of mass 12.""",
 script="""Welcome back. Listen, Matthew 10:30 says, But the very hairs of your head are all numbered. Our Creator knows even the smallest details of what He has made.

Now watch this. Every atom of an element has the same number of protons, but the number of neutrons can differ. Atoms of the same element with different neutrons are isotopes. Carbon 12 has 6 neutrons. Carbon 14 has 8 neutrons. Isotopes have nearly identical chemical properties but different masses.

The mass number is protons plus neutrons. To find neutrons, subtract the atomic number from the mass number. Chlorine 35 has 17 protons and 18 neutrons.

The atomic mass on the periodic table is a weighted average of the isotopes. Multiply each isotope's mass by its fractional abundance and add. Chlorine averages about 35.5.

Isotopes have uses in dating, medicine and treatment. Use them wisely.

Your task is to define isotope, count particles in sodium 23 and calculate an average atomic mass. Take the four question check.""" + CLOSE,
 quiz=[
 ("Atoms of the same element with different numbers of neutrons are:", ["Isotopes", "Ions", "Compounds", "Molecules"], 0, "Isotopes differ only in neutron number."),
 ("Mass number equals:", ["Protons plus neutrons", "Protons plus electrons", "Neutrons minus protons", "Electrons only"], 0, "Mass number counts nucleons."),
 ("An atom with atomic number 17 and mass number 35 has how many neutrons?", ["18", "17", "35", "52"], 0, "35 minus 17 equals 18."),
 ("The atomic mass on the periodic table is a:", ["Weighted average of isotope masses", "Count of electrons", "Number of protons", "Charge of the atom"], 0, "It accounts for the abundance of each isotope."),
 ]),
 dict(t="2.3 Electron Arrangement and Electron Configuration", std="SC.912.P.8",
 body="""Electrons are arranged around the nucleus in energy levels, also called shells. The first energy level holds up to 2 electrons, the second holds up to 8 in the simplest model, and higher levels hold more. Each level contains sublevels named s, p, d and f. An s sublevel holds up to 2 electrons, a p sublevel up to 6, a d sublevel up to 10 and an f sublevel up to 14. Electrons occupy regions called orbitals, and each orbital holds a maximum of 2 electrons.

Electron configuration shows how electrons fill the sublevels. Three rules guide the filling. The Aufbau principle says electrons fill the lowest energy sublevels first. The Pauli exclusion principle says an orbital holds at most two electrons, and they must have opposite spins. Hund's rule says electrons spread out among orbitals of the same sublevel, one in each, before they pair up. The filling order starts 1s, 2s, 2p, 3s, 3p, 4s, 3d. Oxygen, with 8 electrons, has the configuration 1s2 2s2 2p4. Sodium, with 11 electrons, is 1s2 2s2 2p6 3s1.

Valence electrons are the electrons in the outermost energy level, and they determine how an atom bonds. Sodium has 1 valence electron, and oxygen has 6. Atoms tend to react in a way that gives them a full outer level, usually 8 electrons, which is called the octet rule. Noble gases already have full outer levels and rarely react.

When atoms absorb energy, electrons can jump to higher levels. When they fall back, they release light of specific colors. This is why different elements glow with different colors in flame tests and in neon signs. Genesis 1:3 says, And God said, Let there be light: and there was light.

Your task: (1) Write the electron configuration of nitrogen. (2) State how many valence electrons magnesium has. (3) Explain why different elements give off different colors of light.""",
 script="""Welcome back. Listen, Genesis 1:3 says, And God said, Let there be light: and there was light. Light is also the way atoms tell us about their electrons.

Now watch this. Electrons are arranged in energy levels. Each level has sublevels s, p, d and f. An s holds 2, a p holds 6, a d holds 10 and an f holds 14. Each orbital holds up to 2 electrons.

Three rules. Aufbau: fill the lowest energy first. Pauli: opposite spins in an orbital. Hund: spread out before pairing. Oxygen is 1s2 2s2 2p4. Sodium is 1s2 2s2 2p6 3s1.

Valence electrons are in the outermost level and determine bonding. Atoms tend to reach a full outer level of 8, the octet rule. Noble gases are already full.

When electrons absorb energy they jump up. When they fall back they release light of specific colors. That is why flame tests and neon signs show different colors.

Your task is to write the configuration of nitrogen, count magnesium's valence electrons and explain the colors. Take the four question check.""" + CLOSE,
 quiz=[
 ("A p sublevel can hold up to how many electrons?", ["6", "2", "10", "14"], 0, "A p sublevel has three orbitals holding 6 electrons."),
 ("The electron configuration of oxygen is:", ["1s2 2s2 2p4", "1s2 2s2 2p6", "1s2 2s4 2p2", "1s2 2s1 2p5"], 0, "Oxygen has 8 electrons."),
 ("Electrons in the outermost energy level are called:", ["Valence electrons", "Core electrons", "Neutrons", "Isotopes"], 0, "Valence electrons determine bonding."),
 ("Different elements show different flame colors because:", ["Electrons release specific energies when falling to lower levels", "Their nuclei burn", "They have no electrons", "They are all the same"], 0, "Energy level differences are unique to each element."),
 ]),
 dict(t="2.4 The Periodic Table and Periodic Trends", std="SC.912.P.8",
 body="""The periodic table organizes the elements in order of increasing atomic number. Dmitri Mendeleev published an early version in 1869, arranging elements by properties and leaving gaps for elements not yet discovered. Rows are called periods, and columns are called groups or families. Elements in the same group have the same number of valence electrons and similar chemical properties. 1 Corinthians 14:33 says, For God is not the author of confusion, but of peace. The orderly pattern of the elements reflects the order of creation.

Elements are classified as metals, nonmetals and metalloids. Metals, on the left and center of the table, are generally shiny, good conductors of heat and electricity, malleable and ductile. Nonmetals, on the right, are generally dull, poor conductors and brittle as solids. Metalloids lie along a stair step line and have properties of both. Important families include the alkali metals in group 1, which are very reactive; the alkaline earth metals in group 2; the halogens in group 17, which are very reactive nonmetals; and the noble gases in group 18, which are unreactive.

Periodic trends are patterns across the table. Atomic radius, the size of an atom, decreases from left to right across a period and increases going down a group. Ionization energy, the energy needed to remove an electron, increases from left to right and decreases going down a group. Electronegativity, the tendency of an atom to attract electrons in a bond, increases from left to right and decreases going down a group, with fluorine the most electronegative. These trends result from the number of protons pulling on the electrons and the number of energy levels between the nucleus and the outer electrons.

Your task: (1) Explain why elements in the same group behave alike. (2) Compare the properties of metals and nonmetals. (3) Predict which has a larger atomic radius, sodium or chlorine, and explain why.""",
 script="""Welcome back. Listen, 1 Corinthians 14:33 says, For God is not the author of confusion, but of peace. The orderly pattern of the elements reflects the order of creation.

Now watch this. The periodic table lists elements by atomic number. Mendeleev arranged elements by properties and left gaps for undiscovered ones. Rows are periods. Columns are groups. Elements in a group have the same number of valence electrons and similar properties.

Metals are shiny, conduct heat and electricity, and are malleable and ductile. Nonmetals are dull and poor conductors. Metalloids have both. Group 1 alkali metals are very reactive. Group 17 halogens are reactive nonmetals. Group 18 noble gases are unreactive.

Trends. Atomic radius decreases across a period and increases down a group. Ionization energy increases across and decreases down. Electronegativity increases across and decreases down. Fluorine is the most electronegative.

Your task is to explain group behavior, compare metals and nonmetals and predict sodium versus chlorine size. Take the four question check.""" + CLOSE,
 quiz=[
 ("Columns of the periodic table are called:", ["Groups", "Periods", "Isotopes", "Shells"], 0, "Groups share valence electron counts."),
 ("Group 18 elements are called the:", ["Noble gases", "Halogens", "Alkali metals", "Metalloids"], 0, "The noble gases are unreactive."),
 ("Going from left to right across a period, atomic radius generally:", ["Decreases", "Increases", "Stays the same", "Doubles"], 0, "More protons pull electrons closer."),
 ("The most electronegative element is:", ["Fluorine", "Sodium", "Helium", "Iron"], 0, "Fluorine attracts electrons most strongly."),
 ]),
 ],
 assess=dict(t="Assessment 2: Atomic Structure and the Periodic Table",
 prompt="""Write a report of at least 250 words on atoms and the periodic table. Use complete sentences and label each part. Psalm 147:4 says, He telleth the number of the stars; he calleth them all by their names.

Part 1: Describe the charge, mass and location of protons, neutrons and electrons. Summarize how the models of Dalton, Thomson, Rutherford and Bohr improved our understanding of the atom.
Part 2: Define atomic number, mass number and isotope. For a neutral atom with atomic number 20 and mass number 40, state the number of protons, neutrons and electrons. Explain how average atomic mass is found.
Part 3: Write the electron configurations of carbon and sodium and identify the number of valence electrons in each. Explain the octet rule.
Part 4: Describe periods, groups, metals, nonmetals and metalloids. Explain the trends in atomic radius, ionization energy and electronegativity across a period and down a group.
Part 5: Explain how Psalm 147:4 and 1 Corinthians 14:33 encourage us as we study the order in creation.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 20 points. Part 3: 20 points. Part 4: 25 points. Part 5: 10 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 2: He Calleth Them All by Their Names",
 prompt="""Write a post of at least 120 words that (1) explains in your own words why the periodic table is useful to scientists, (2) describes one element you use or depend on every day and what you know about it, (3) explains how it feels to study something too small to see and how that can build your faith or your curiosity, and (4) connects your answer to Psalm 147:4, Matthew 10:30 or 1 Corinthians 14:33. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why is it important that scientists change their models when new evidence appears? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("The charge of an electron is:", ["Negative", "Positive", "Neutral", "Variable"], 0, "Electrons carry a negative charge."),
 ("The number of protons in an atom is its:", ["Atomic number", "Mass number", "Isotope number", "Valence number"], 0, "Atomic number identifies the element."),
 ("Carbon 14 has how many neutrons?", ["8", "6", "14", "20"], 0, "14 minus 6 equals 8."),
 ("The maximum number of electrons in an orbital is:", ["2", "6", "8", "10"], 0, "Each orbital holds two electrons with opposite spins."),
 ("Sodium has how many valence electrons?", ["1", "2", "8", "11"], 0, "Sodium is in group 1."),
 ("Elements in the same group have similar properties because they have the same number of:", ["Valence electrons", "Neutrons", "Isotopes", "Energy levels"], 0, "Valence electrons control chemical behavior."),
 ("Ionization energy generally increases:", ["Across a period from left to right", "Down a group", "From right to left", "With more energy levels"], 0, "Stronger attraction makes electrons harder to remove."),
 ("Which group contains very reactive nonmetals?", ["Halogens", "Noble gases", "Alkali metals", "Transition metals"], 0, "The halogens in group 17 are reactive nonmetals."),
 ]
)
