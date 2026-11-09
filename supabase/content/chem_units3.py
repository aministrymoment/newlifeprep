"""Chemistry, Unit 3: Chemical Bonding and Naming Compounds. Florida science standards cited at strand level (SC.912.P); recheck exact benchmark codes at CPALMS."""
from chem_units1 import CLOSE

UNIT3 = dict(
 title="Unit 3: Chemical Bonding and Naming Compounds",
 std="SC.912.P.8",
 topics=[
 dict(t="3.1 Ionic Bonds and Ionic Compounds", std="SC.912.P.8",
 body="""Atoms bond to reach a more stable arrangement of electrons, usually a full outer energy level. Amos 3:3 asks, Can two walk together, except they be agreed? In chemistry, atoms join when the arrangement is stable for both. An ionic bond forms when one atom transfers electrons to another. This usually happens between a metal, which loses electrons, and a nonmetal, which gains electrons.

Consider sodium and chlorine. Sodium has 1 valence electron and chlorine has 7. Sodium gives its electron to chlorine. Sodium becomes a sodium ion with a charge of 1 plus, and chlorine becomes a chloride ion with a charge of 1 minus. Opposite charges attract, and the attraction between the ions is the ionic bond. The result is sodium chloride, table salt. Magnesium loses 2 electrons to form a 2 plus ion, and oxygen gains 2 electrons to form a 2 minus ion.

Ionic compounds do not form separate molecules. Instead, the ions arrange themselves in a repeating three dimensional pattern called a crystal lattice. The formula shows the simplest whole number ratio of ions, called a formula unit. Magnesium chloride has the formula MgCl2 because one 2 plus ion balances two 1 minus ions. The total charge of an ionic compound is zero.

Ionic compounds have characteristic properties. They usually have high melting points and are hard but brittle. They conduct electricity when melted or dissolved in water, because the ions are free to move, but not as solids. Many dissolve in water.

Your task: (1) Describe how sodium and chlorine form an ionic bond. (2) Predict the formula for the compound made from calcium and chlorine. (3) Explain why ionic compounds conduct electricity when dissolved but not as solids.""",
 script="""Welcome back. Listen, Amos 3:3 asks, Can two walk together, except they be agreed? In chemistry, atoms join when the arrangement is stable for both.

Now watch this. Atoms bond to reach a full outer level. An ionic bond forms when one atom transfers electrons to another, usually from a metal to a nonmetal.

Sodium has 1 valence electron and chlorine has 7. Sodium gives its electron to chlorine. Sodium becomes a 1 plus ion. Chlorine becomes a 1 minus chloride ion. Opposite charges attract. That attraction is the ionic bond, and the compound is table salt.

Ionic compounds form a crystal lattice, not separate molecules. The formula shows the simplest ratio of ions. Magnesium chloride is MgCl2 because one 2 plus ion balances two 1 minus ions. The total charge is zero.

They have high melting points, are hard but brittle, and conduct electricity when melted or dissolved because the ions can move.

Your task is to describe sodium chloride formation, predict calcium chloride's formula and explain conductivity. Take the four question check.""" + CLOSE,
 quiz=[
 ("An ionic bond forms when electrons are:", ["Transferred", "Shared equally", "Destroyed", "Created"], 0, "Ionic bonds involve electron transfer."),
 ("Which pair is most likely to form an ionic bond?", ["Sodium and chlorine", "Carbon and oxygen", "Hydrogen and hydrogen", "Nitrogen and nitrogen"], 0, "A metal and a nonmetal form an ionic bond."),
 ("The formula for the compound of magnesium and chlorine is:", ["MgCl2", "MgCl", "Mg2Cl", "Mg2Cl2"], 0, "One 2 plus ion needs two 1 minus ions."),
 ("Ionic compounds conduct electricity best when they are:", ["Dissolved in water", "Solid", "Powdered", "Cold"], 0, "Free ions carry the charge."),
 ]),
 dict(t="3.2 Covalent Bonds and Lewis Structures", std="SC.912.P.8",
 body="""A covalent bond forms when two atoms share electrons. This usually happens between nonmetals. Colossians 3:14 says, And above all these things put on charity, which is the bond of perfectness. Just as sharing builds strong relationships, shared electrons hold atoms together. A group of atoms joined by covalent bonds is a molecule.

In a single bond, atoms share one pair of electrons. In a double bond they share two pairs, and in a triple bond three pairs. Water has two single bonds between oxygen and hydrogen. Carbon dioxide has two double bonds. Nitrogen gas has a triple bond. More shared pairs mean a shorter, stronger bond. Diatomic molecules such as H2, N2, O2, F2, Cl2, Br2 and I2 exist as pairs of atoms.

A Lewis structure is a diagram that shows valence electrons. Dots represent electrons, and lines represent shared pairs. To draw one: count the total valence electrons; place the least electronegative atom in the center, except hydrogen; connect atoms with single bonds; place remaining electrons as lone pairs to fill the octets of outer atoms and then the central atom; and form double or triple bonds if needed. Hydrogen needs only 2 electrons. For water, the total is 6 plus 2, which is 8 valence electrons: two bonds and two lone pairs on oxygen.

Covalent compounds usually have lower melting and boiling points than ionic compounds, and they do not conduct electricity well. Some covalent substances, like diamond, form giant networks and are very hard.

Your task: (1) Define covalent bond and molecule. (2) Draw or describe the Lewis structure of water. (3) Compare single, double and triple bonds.""",
 script="""Welcome back. Listen, Colossians 3:14 says, And above all these things put on charity, which is the bond of perfectness. Just as sharing builds strong relationships, shared electrons hold atoms together.

Now watch this. A covalent bond forms when atoms share electrons, usually between nonmetals. A group of atoms joined this way is a molecule.

A single bond shares one pair. A double bond shares two pairs. A triple bond shares three pairs. More shared pairs means a shorter, stronger bond. Water has two single bonds. Carbon dioxide has two double bonds. Nitrogen gas has a triple bond. Seven elements exist as diatomic molecules: H2, N2, O2, F2, Cl2, Br2 and I2.

A Lewis structure shows valence electrons. Count total valence electrons. Put the least electronegative atom in the center. Connect with single bonds. Fill the octets with lone pairs. Form multiple bonds if needed. Hydrogen needs only 2.

Covalent compounds usually have lower melting points and do not conduct well.

Your task is to define covalent bond, describe water's Lewis structure and compare bond types. Take the four question check.""" + CLOSE,
 quiz=[
 ("A covalent bond is formed by:", ["Sharing electrons", "Transferring electrons", "Sharing protons", "Losing neutrons"], 0, "Covalent bonds share electrons."),
 ("A triple bond shares how many pairs of electrons?", ["3", "1", "2", "6"], 0, "Triple means three shared pairs."),
 ("Which molecule contains a double bond?", ["Carbon dioxide", "Water", "Hydrogen gas", "Sodium chloride"], 0, "CO2 has two C double bonded to O bonds."),
 ("Hydrogen needs how many electrons for a full outer level?", ["2", "8", "4", "6"], 0, "Hydrogen follows the duet rule."),
 ]),
 dict(t="3.3 Writing Formulas and Naming Compounds", std="SC.912.P.8",
 body="""Chemists use a common naming system so that everyone understands which substance is meant. Genesis 2:19 records that Adam named the animals: and whatsoever Adam called every living creature, that was the name thereof. Names bring clarity and order.

To name an ionic compound with a metal that forms only one ion, name the metal first and then the nonmetal with the ending ide. NaCl is sodium chloride and CaO is calcium oxide. Some metals, especially transition metals, can form more than one ion, so a Roman numeral shows the charge. FeCl2 is iron(II) chloride and FeCl3 is iron(III) chloride. To write a formula from a name, use the charges so the total charge is zero: aluminum oxide uses 2 aluminum ions with a charge of 3 plus and 3 oxide ions with a charge of 2 minus, giving Al2O3.

Polyatomic ions are groups of atoms that carry a charge and act as a unit. Common ones are nitrate NO3, sulfate SO4, hydroxide OH, carbonate CO3, phosphate PO4 and ammonium NH4. Use parentheses when you need more than one polyatomic ion, as in Ca(OH)2.

Covalent compounds between two nonmetals use prefixes to show how many atoms: mono 1, di 2, tri 3, tetra 4, penta 5, hexa 6, hepta 7, octa 8, nona 9 and deca 10. CO2 is carbon dioxide, CO is carbon monoxide, and N2O4 is dinitrogen tetroxide. The prefix mono is usually dropped on the first element.

Acids have special names. Binary acids start with hydro and end with ic, so HCl in water is hydrochloric acid. Many common acids are named from their polyatomic ions, such as sulfuric acid, H2SO4.

Your task: (1) Name Na2S, Mg(OH)2 and CO2. (2) Write the formula for aluminum chloride and calcium nitrate. (3) Explain why a Roman numeral is used in iron(III) oxide.""",
 script="""Welcome back. Listen, Genesis 2:19 says, whatsoever Adam called every living creature, that was the name thereof. Names bring clarity and order, in the garden and in the lab.

Now watch this. For an ionic compound, name the metal first, then the nonmetal ending in ide. NaCl is sodium chloride. If a metal can form more than one ion, use a Roman numeral. FeCl3 is iron three chloride. To write a formula, balance the charges to zero. Aluminum oxide is Al2O3.

Polyatomic ions are groups of atoms with a charge that act as a unit. Nitrate, sulfate, hydroxide, carbonate, phosphate and ammonium. Use parentheses for more than one, like Ca(OH)2.

For covalent compounds use prefixes. Mono, di, tri, tetra, penta, hexa, hepta, octa, nona, deca. CO2 is carbon dioxide. N2O4 is dinitrogen tetroxide.

Acids have special names. HCl in water is hydrochloric acid. H2SO4 is sulfuric acid.

Your task is to name three compounds, write two formulas and explain the Roman numeral. Take the four question check.""" + CLOSE,
 quiz=[
 ("The name of NaCl is:", ["Sodium chloride", "Sodium chlorine", "Sodium chlorate", "Salt oxide"], 0, "Nonmetal ions end in ide."),
 ("The formula for aluminum oxide is:", ["Al2O3", "AlO", "Al3O2", "AlO3"], 0, "Two 3 plus ions balance three 2 minus ions."),
 ("The prefix for four atoms is:", ["Tetra", "Tri", "Penta", "Di"], 0, "Tetra means four."),
 ("A Roman numeral in a compound name shows the:", ["Charge of the metal ion", "Number of molecules", "Mass", "Number of neutrons"], 0, "It identifies which ion the metal formed."),
 ]),
 dict(t="3.4 Molecular Shape, Polarity and Intermolecular Forces", std="SC.912.P.8",
 body="""The shape of a molecule affects how it behaves. Psalm 139:14 says, I will praise thee; for I am fearfully and wonderfully made: marvellous are thy works. The shapes of molecules, including those in our own bodies, show remarkable design.

Valence shell electron pair repulsion theory, called VSEPR, says that electron pairs around a central atom repel each other and spread as far apart as possible. Two bonded atoms and no lone pairs on the center give a linear shape, as in carbon dioxide. Three bonded atoms with no lone pairs give a trigonal planar shape. Four bonded atoms give a tetrahedral shape, as in methane. Water has two bonded atoms and two lone pairs, giving a bent shape. Ammonia has three bonded atoms and one lone pair, giving a trigonal pyramidal shape.

Polarity describes unequal sharing of electrons. When two atoms differ in electronegativity, the electrons are pulled closer to the more electronegative atom, creating a polar bond with a slight negative end and a slight positive end. A molecule is polar if it has polar bonds that do not cancel because of its shape. Water is polar and bent. Carbon dioxide has polar bonds but is linear, so they cancel and the molecule is nonpolar. A common rule is that like dissolves like: polar substances dissolve in polar solvents such as water, and nonpolar substances dissolve in nonpolar solvents such as oil.

Intermolecular forces are attractions between molecules. Dispersion forces exist between all molecules and are weak. Dipole dipole forces act between polar molecules. Hydrogen bonding is a strong attraction involving hydrogen bonded to nitrogen, oxygen or fluorine. Hydrogen bonding gives water its high boiling point, surface tension and the fact that ice floats.

Your task: (1) Predict the shape of methane and water. (2) Explain why carbon dioxide is nonpolar although its bonds are polar. (3) Explain why ice floats.""",
 script="""Welcome back. Listen, Psalm 139:14 says, I will praise thee; for I am fearfully and wonderfully made: marvellous are thy works. The shapes of molecules show remarkable design.

Now watch this. VSEPR says electron pairs around a central atom repel and spread as far apart as possible. Two bonded atoms with no lone pairs is linear, like carbon dioxide. Three is trigonal planar. Four is tetrahedral, like methane. Water is bent. Ammonia is trigonal pyramidal.

Polarity is unequal sharing of electrons. Unequal electronegativity creates a polar bond. A molecule is polar if its polar bonds do not cancel. Water is polar. Carbon dioxide is nonpolar because it is linear and the bonds cancel. Like dissolves like.

Intermolecular forces are attractions between molecules. Dispersion forces are weak and in all molecules. Dipole dipole forces act between polar molecules. Hydrogen bonding is strong and involves hydrogen with nitrogen, oxygen or fluorine. It gives water a high boiling point and makes ice float.

Your task is to predict shapes, explain carbon dioxide's polarity and explain why ice floats. Take the four question check.""" + CLOSE,
 quiz=[
 ("The shape of a water molecule is:", ["Bent", "Linear", "Tetrahedral", "Trigonal planar"], 0, "Two lone pairs bend the molecule."),
 ("Carbon dioxide is nonpolar because:", ["Its polar bonds cancel by its linear shape", "It has no bonds", "It is ionic", "It has no oxygen"], 0, "Symmetry cancels the bond polarities."),
 ("Hydrogen bonding is strongest when hydrogen is bonded to:", ["Oxygen", "Carbon", "Sodium", "Helium"], 0, "Hydrogen bonds involve N, O or F."),
 ("Like dissolves like means polar substances dissolve best in:", ["Polar solvents", "Nonpolar solvents", "No solvents", "Gases only"], 0, "Polar mixes with polar."),
 ]),
 ],
 assess=dict(t="Assessment 3: Chemical Bonding and Naming Compounds",
 prompt="""Write a report of at least 250 words on chemical bonding. Use complete sentences and label each part. Amos 3:3 asks, Can two walk together, except they be agreed?

Part 1: Compare ionic and covalent bonds. Explain how sodium and chlorine form an ionic bond and how two hydrogen atoms form a covalent bond. List four properties of ionic compounds.
Part 2: Draw or describe the Lewis structures of water and carbon dioxide. Explain single, double and triple bonds.
Part 3: Name the following: KBr, CaCO3, FeCl3 and N2O5. Write the formulas for magnesium oxide, sodium sulfate and carbon tetrachloride.
Part 4: Use VSEPR to predict the shapes of methane, ammonia and water. Explain polar and nonpolar molecules and give an example of each.
Part 5: Describe the three kinds of intermolecular forces and explain how hydrogen bonding gives water special properties. Apply Colossians 3:14 or Psalm 139:14 to what you learned.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 15 points. Part 3: 25 points. Part 4: 20 points. Part 5: 15 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 3: Can Two Walk Together, Except They Be Agreed",
 prompt="""Write a post of at least 120 words that (1) compares ionic bonding, where electrons are given, with covalent bonding, where electrons are shared, to two kinds of relationships you see at home, church or school, (2) explains why water, held together by hydrogen bonds, is so important for life, (3) explains how studying molecules can help you appreciate the Creator, and (4) connects your answer to Amos 3:3, Colossians 3:14, Genesis 2:19 or Psalm 139:14. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why is it important that scientists use the same names and symbols? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("Atoms bond mainly to achieve:", ["A stable outer electron arrangement", "More neutrons", "A larger nucleus", "Radioactivity"], 0, "A full outer level is stable."),
 ("Which compound is ionic?", ["NaCl", "CO2", "H2O", "CH4"], 0, "Sodium chloride is a metal and nonmetal compound."),
 ("In a covalent bond, atoms:", ["Share electrons", "Trade protons", "Lose all electrons", "Fuse nuclei"], 0, "Covalent bonds share electrons."),
 ("The formula for calcium chloride is:", ["CaCl2", "CaCl", "Ca2Cl", "Ca2Cl2"], 0, "Ca has a 2 plus charge, Cl a 1 minus."),
 ("The name of CO is:", ["Carbon monoxide", "Carbon oxide", "Carbonic oxygen", "Carbon dioxide"], 0, "One oxygen uses the prefix mono."),
 ("The shape of methane is:", ["Tetrahedral", "Linear", "Bent", "Trigonal pyramidal"], 0, "Four bonded atoms and no lone pairs give a tetrahedral shape."),
 ("The strongest type of intermolecular attraction listed is:", ["Hydrogen bonding", "Dispersion force", "Gravity", "Magnetism"], 0, "Hydrogen bonding is strong among molecules."),
 ("Ionic compounds conduct electricity when:", ["Melted or dissolved", "Solid", "Frozen", "Never"], 0, "Ions must be free to move."),
 ]
)
