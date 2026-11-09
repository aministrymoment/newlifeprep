"""Physical Science, Unit 3: Chemical Bonds and Reactions. Florida NGSSS Physical Science (SC.912.P.8) cited at strand level; recheck exact benchmark codes at CPALMS."""
from psc_units1 import CLOSE

UNIT3 = dict(
 title="Unit 3: Chemical Bonds and Reactions",
 std="SC.912.P.8",
 topics=[
 dict(t="3.1 Ionic and Covalent Bonds", std="SC.912.P.8",
 body="""A chemical bond is the attraction that holds atoms together. Ecclesiastes 4:12 says, And if one prevail against him, two shall withstand him; and a threefold cord is not quickly broken. Strands woven together are stronger than strands apart, and atoms joined by bonds make substances far different from the separate atoms.

Atoms bond to reach a stable, full outer energy level. In an ionic bond, one atom transfers electrons to another. This usually happens between a metal and a nonmetal. Sodium has one valence electron and chlorine has seven. Sodium gives its electron to chlorine, so sodium becomes a positive ion and chlorine becomes a negative ion. Opposite charges attract, and the ions pack into a repeating crystal. Ionic compounds such as table salt, NaCl, are usually hard and brittle, have high melting points, and conduct electricity when melted or dissolved in water. When the charges of the ions are balanced, the formula follows. A magnesium ion has a charge of positive 2 and a chloride ion has a charge of negative 1, so the formula is MgCl2.

In a covalent bond, atoms share electrons. This usually happens between nonmetals. The result is a molecule. In water, each hydrogen shares a pair of electrons with oxygen. In a single bond one pair is shared, in a double bond two pairs are shared, as in carbon dioxide, and in a triple bond three pairs are shared, as in nitrogen gas. Covalent compounds usually have lower melting points than ionic compounds and do not conduct electricity well. When the sharing is unequal, the molecule is polar, as water is, and this helps water dissolve many substances.

In a metallic bond, metal atoms share a sea of freely moving electrons, which explains why metals conduct electricity and can be shaped without breaking.

Your task: (1) Tell how an ionic bond differs from a covalent bond. (2) Predict which bond forms between two elements. (3) Write a formula from the ion charges.""",
 script="""Welcome back. Listen, Ecclesiastes 4:12 says, a threefold cord is not quickly broken. Strands woven together are stronger than strands apart, and atoms joined by bonds make substances far different from separate atoms.

Now watch this. In an ionic bond, one atom transfers electrons to another, usually between a metal and a nonmetal. Sodium gives one electron to chlorine. Sodium becomes a positive ion, chlorine a negative ion, and the opposite charges attract. Table salt, NaCl, is hard and brittle with a high melting point. Magnesium has a charge of positive 2 and chloride negative 1, so the formula is MgCl2.

In a covalent bond, atoms share electrons, usually between nonmetals. That makes a molecule. In water, each hydrogen shares a pair of electrons with oxygen. Carbon dioxide has double bonds. Nitrogen gas has a triple bond. Water is polar, which helps it dissolve many substances.

In a metallic bond, metal atoms share a sea of moving electrons, which is why metals conduct electricity.

Your task is to compare ionic and covalent bonds, predict a bond and write a formula. Take the four question check.""" + CLOSE,
 quiz=[
 ("An ionic bond forms when:", ["Electrons are transferred from one atom to another", "Electrons are shared equally", "Protons are shared", "Neutrons are exchanged"], 0, "Ionic bonds come from electron transfer."),
 ("A covalent bond forms when atoms:", ["Share electrons", "Transfer all their electrons", "Lose neutrons", "Gain protons"], 0, "Covalent bonds are shared pairs of electrons."),
 ("Which compound is held together by ionic bonds?", ["NaCl", "H2O", "CO2", "O2"], 0, "Sodium is a metal and chlorine is a nonmetal."),
 ("Water is a molecule because its atoms are joined by:", ["Covalent bonds", "Ionic bonds", "Nuclear bonds", "Magnetic bonds"], 0, "Hydrogen and oxygen share electrons."),
 ]),
 dict(t="3.2 Chemical Formulas and Balanced Equations", std="SC.912.P.8",
 body="""A chemical reaction rearranges atoms into new substances. Colossians 1:17 says, And he is before all things, and by him all things consist. The matter of the universe holds together by His power, and in every chemical reaction not one atom is lost.

A chemical equation is a short way to describe a reaction. The reactants, which are the starting substances, are written on the left, and the products, which are the new substances, are written on the right, with an arrow read as yields. For example, hydrogen burning in oxygen to make water is written H2 + O2 yields H2O.

The law of conservation of mass, first stated clearly by Antoine Lavoisier, says that in a chemical reaction mass is neither created nor destroyed. The same number of each kind of atom must appear on both sides. The equation H2 + O2 yields H2O has 2 oxygen atoms on the left and only 1 on the right, so it is not balanced.

To balance an equation, change only the coefficients, the large numbers in front of formulas. Never change the subscripts, because that would change the substance. Count the atoms of each element, adjust a coefficient, and count again. Put a 2 in front of H2O, which gives 2 oxygen atoms on each side, but now there are 4 hydrogen atoms on the right, so put a 2 in front of H2. The balanced equation is 2H2 + O2 yields 2H2O. The coefficient multiplies every atom in the formula, so 2H2O has 4 hydrogen atoms and 2 oxygen atoms.

Another example: magnesium burning is Mg + O2 yields MgO. Balancing gives 2Mg + O2 yields 2MgO, with 2 magnesium and 2 oxygen atoms on each side. Rusting is 4Fe + 3O2 yields 2Fe2O3, with 4 iron atoms and 6 oxygen atoms on each side.

Your task: (1) Identify reactants and products. (2) Count atoms on each side. (3) Balance a simple equation using coefficients.""",
 script="""Welcome back. Listen, Colossians 1:17 says, And he is before all things, and by him all things consist. The matter of the universe holds together by His power, and in every chemical reaction not one atom is lost.

Now watch this. In a chemical equation, the reactants are on the left and the products are on the right, joined by an arrow that we read as yields. The law of conservation of mass says mass is neither created nor destroyed, so each kind of atom must appear the same number of times on both sides.

Look at hydrogen burning in oxygen. H2 + O2 yields H2O has 2 oxygen atoms on the left and 1 on the right, so it is not balanced. We change only the coefficients, never the subscripts. Put a 2 in front of H2O, then a 2 in front of H2. The balanced equation is 2H2 + O2 yields 2H2O. Now there are 4 hydrogen and 2 oxygen on each side.

Magnesium burning balances as 2Mg + O2 yields 2MgO. Rusting balances as 4Fe + 3O2 yields 2Fe2O3.

Your task is to name reactants and products, count atoms and balance an equation. Take the four question check.""" + CLOSE,
 quiz=[
 ("In a chemical equation, the substances on the left side are the:", ["Reactants", "Products", "Catalysts", "Isotopes"], 0, "Reactants are the starting substances."),
 ("The law of conservation of mass says that in a chemical reaction:", ["Mass is neither created nor destroyed", "Mass always increases", "Atoms disappear", "The products always weigh less"], 0, "The total mass stays the same."),
 ("Which equation is balanced?", ["2H2 + O2 yields 2H2O", "H2 + O2 yields H2O", "H2 + O2 yields 2H2O", "2H2 + 2O2 yields 2H2O"], 0, "Only the first has equal atoms of each element on both sides."),
 ("To balance an equation you change the:", ["Coefficients", "Subscripts", "Element symbols", "Charges"], 0, "Changing subscripts would change the substance."),
 ]),
 dict(t="3.3 Types of Chemical Reactions", std="SC.912.P.8",
 body="""Chemical reactions fall into patterns. First Peter 1:7 speaks of the trial of your faith, being much more precious than of gold that perisheth, though it be tried with fire. Fire is a chemical reaction, and the refiner's fire shows how a reaction can reveal and purify.

In a synthesis reaction, two or more substances combine to form one product, A + B yields AB. Hydrogen and oxygen forming water is synthesis. In a decomposition reaction, one compound breaks into simpler substances, AB yields A + B. Passing electricity through water gives 2H2O yields 2H2 + O2. In a single replacement reaction, one element takes the place of another in a compound, as in Zn + 2HCl yields ZnCl2 + H2. In a double replacement reaction, two compounds exchange partners, and often a solid called a precipitate forms, as in AgNO3 + NaCl yields AgCl + NaNO3. In a combustion reaction, a substance burns in oxygen and releases energy. Burning methane gives CH4 + 2O2 yields CO2 + 2H2O.

Reactions also involve energy. An exothermic reaction releases energy to the surroundings, as when a fuel burns or a hand warmer works. An endothermic reaction absorbs energy, as when a cold pack feels cold. Photosynthesis is endothermic. Plants use light to turn carbon dioxide and water into sugar and oxygen, 6CO2 + 6H2O + light yields C6H12O6 + 6O2. Cellular respiration is the reverse process and releases energy for the cell.

How do you know a chemical reaction happened? Look for evidence: a gas forming as bubbles, a precipitate, a permanent color change, heat or light given off, or a new odor. A change in size, shape or state alone is physical. Rusting and burning also involve oxidation, where a substance combines with oxygen.

Your task: (1) Classify a reaction by type. (2) Tell whether a reaction is exothermic or endothermic. (3) List evidence of a chemical change.""",
 script="""Welcome back. Listen, First Peter 1:7 speaks of the trial of your faith, being much more precious than of gold that perisheth, though it be tried with fire. Fire is a chemical reaction, and the refiner's fire shows how a reaction can reveal and purify.

Now watch this. In synthesis, substances combine to make one product. In decomposition, one compound breaks into simpler substances, like water splitting into hydrogen and oxygen. In single replacement, one element takes the place of another, like zinc and hydrochloric acid. In double replacement, two compounds trade partners and often a solid forms, called a precipitate. In combustion, a substance burns in oxygen. Methane burning gives carbon dioxide and water.

Look at energy. An exothermic reaction releases energy, like a burning fuel or a hand warmer. An endothermic reaction absorbs energy, like a cold pack. Photosynthesis is endothermic, because plants use light to make sugar and oxygen.

How do you know a reaction happened? Look for bubbles of gas, a precipitate, a permanent color change, heat or light, or a new odor.

Your task is to classify a reaction, tell exothermic from endothermic and list evidence of change. Take the four question check.""" + CLOSE,
 quiz=[
 ("A reaction in which one compound breaks down into simpler substances is:", ["Decomposition", "Synthesis", "Combustion", "Neutralization"], 0, "Decomposition splits a compound apart."),
 ("Burning methane in oxygen to make carbon dioxide and water is a:", ["Combustion reaction", "Decomposition reaction", "Neutralization reaction", "Physical change"], 0, "Burning in oxygen is combustion."),
 ("A reaction that releases energy to its surroundings is:", ["Exothermic", "Endothermic", "Reversible", "Inert"], 0, "Exothermic reactions give off energy."),
 ("Which is evidence of a chemical reaction?", ["Bubbles of gas and a permanent color change", "A change in shape", "A change in size", "Sugar dissolving in water"], 0, "Gas and a new color suggest new substances."),
 ]),
 dict(t="3.4 Reaction Rates, Acids and Bases", std="SC.912.P.8",
 body="""Reactions happen at different speeds, and some liquids are acids or bases. Matthew 5:13 says, Ye are the salt of the earth: but if the salt have lost his savour, wherewith shall it be salted? Salt is a compound formed when an acid and a base react, and Jesus used it to teach about usefulness.

Reaction rate is how fast reactants turn into products. Collisions between particles cause reactions, so anything that makes collisions more frequent or more energetic speeds a reaction. Raising the temperature, increasing the concentration, and increasing the surface area, for example by crushing a tablet, all speed a reaction. A catalyst speeds a reaction without being used up. Enzymes are catalysts in living cells, and they let digestion happen quickly at body temperature.

An acid tastes sour, turns blue litmus red, and releases hydrogen ions in water. Examples are vinegar, lemon juice and stomach acid. A base tastes bitter, feels slippery, turns red litmus blue, and releases hydroxide ions in water. Examples are soap, baking soda and ammonia cleaners. Never taste or touch unknown chemicals, because strong acids and bases burn.

The pH scale runs from 0 to 14. A pH below 7 is acidic, a pH of 7 is neutral, as pure water is, and a pH above 7 is basic. Each step on the scale is a change of ten times in acidity. Stomach acid is about pH 1 to 2, lemon juice about 2, black coffee about 5, blood about 7.4, baking soda solution about 9, and household bleach about 12 to 13. Indicators such as litmus and phenolphthalein change color to show acid or base.

When an acid and a base react, they neutralize each other and form a salt and water. For example, HCl + NaOH yields NaCl + H2O. Antacid tablets use this to settle stomach acid.

Your task: (1) List four ways to speed up a reaction. (2) Classify a solution as acidic, basic or neutral from its pH. (3) Write what forms when an acid neutralizes a base.""",
 script="""Welcome back. Listen, Matthew 5:13 says, Ye are the salt of the earth. Salt is a compound formed when an acid and a base react, and Jesus used it to teach about usefulness.

Now watch this. Reaction rate is how fast reactants turn into products. Particles must collide, so a higher temperature, a higher concentration or a larger surface area speeds a reaction. A catalyst speeds a reaction without being used up. Enzymes are catalysts in living cells.

Look at acids and bases. An acid is sour and releases hydrogen ions in water, like vinegar and lemon juice. A base is bitter and slippery and releases hydroxide ions, like soap and baking soda. Never taste or touch unknown chemicals.

The pH scale runs from 0 to 14. Below 7 is acidic. Seven is neutral, like pure water. Above 7 is basic. Each step is a change of ten times. Stomach acid is about 1 to 2. Bleach is about 12 to 13.

When an acid and a base react, they neutralize each other and form a salt and water. HCl plus NaOH yields NaCl plus water.

Your task is to list ways to speed a reaction, classify solutions by pH and describe neutralization. Take the four question check.""" + CLOSE,
 quiz=[
 ("A catalyst:", ["Speeds up a reaction without being used up", "Is a product of the reaction", "Always slows a reaction", "Is a reactant that gets used up"], 0, "A catalyst is not consumed."),
 ("A solution with a pH of 3 is:", ["Acidic", "Basic", "Neutral", "A pure base"], 0, "A pH below 7 is acidic."),
 ("The pH of pure water is:", ["7", "0", "14", "1"], 0, "Pure water is neutral."),
 ("The products of neutralizing an acid with a base are:", ["A salt and water", "An acid and a base", "Two gases", "Two metals"], 0, "Neutralization forms a salt and water."),
 ]),
 ],
 assess=dict(t="Assessment 3: Chemical Bonds and Reactions",
 prompt="""Write a report of at least 250 words on chemical bonds and reactions. Use complete sentences, show your work and label each part. Colossians 1:17 says, And he is before all things, and by him all things consist.

Part 1: Describe how sodium and chlorine form an ionic bond, and how hydrogen and oxygen form covalent bonds in water. Tell two properties that differ between ionic and covalent compounds.
Part 2: Balance these equations and show your atom counts: H2 + O2 yields H2O, then N2 + H2 yields NH3, then Mg + O2 yields MgO.
Part 3: Classify each reaction as synthesis, decomposition, single replacement, double replacement or combustion: 2H2O yields 2H2 + O2, then Zn + 2HCl yields ZnCl2 + H2, then CH4 + 2O2 yields CO2 + 2H2O. Tell whether burning is exothermic or endothermic.
Part 4: Explain four ways to speed up a reaction and what a catalyst does.
Part 5: Tell whether solutions with pH values of 2, 7 and 11 are acidic, basic or neutral, describe what neutralization makes, and explain how Matthew 5:13 connects to salt.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 25 points. Part 3: 20 points. Part 4: 15 points. Part 5: 15 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 3: Bonds That Hold",
 prompt="""Write a post of at least 120 words that (1) describes a bond between people in your family, church or team that holds strong, (2) explains how atoms bond by sharing or transferring electrons to become stable, (3) tells how the idea that no atom is lost in a reaction shows the order of creation, and (4) connects your answer to Ecclesiastes 4:12, Colossians 1:17 or Matthew 5:13. Then write a respectful reply of at least 40 words to another student's post, or answer this question: What can believers learn about unity from the way atoms bond? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("Sodium gives an electron to chlorine. The bond formed is:", ["Ionic", "Covalent", "Metallic", "Nuclear"], 0, "Electron transfer makes an ionic bond."),
 ("A bond in which two atoms share electrons is:", ["Covalent", "Ionic", "Nuclear", "Magnetic"], 0, "Sharing electrons is a covalent bond."),
 ("How many oxygen atoms are in 2H2O?", ["2", "1", "4", "3"], 0, "The coefficient 2 times 1 oxygen gives 2."),
 ("In 2Mg + O2 yields 2MgO, the coefficient in front of MgO is:", ["2", "1", "3", "4"], 0, "The number in front of MgO is 2."),
 ("Zn + 2HCl yields ZnCl2 + H2 is a:", ["Single replacement reaction", "Synthesis reaction", "Decomposition reaction", "Combustion reaction"], 0, "Zinc replaces hydrogen."),
 ("Raising the temperature usually makes a reaction:", ["Faster", "Slower", "Stop", "Impossible"], 0, "Particles collide more often and with more energy."),
 ("Which pH value is the most basic?", ["13", "7", "3", "1"], 0, "The highest pH is the most basic."),
 ("Which is NOT a sign of a chemical change?", ["Ice melting", "Gas bubbles forming", "A new color appearing", "Heat or light given off"], 0, "Melting is a physical change."),
 ],
)
