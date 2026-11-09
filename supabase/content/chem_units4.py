"""Chemistry, Unit 4: Chemical Reactions and Stoichiometry. Florida science standards cited at strand level (SC.912.P); recheck exact benchmark codes at CPALMS."""
from chem_units1 import CLOSE

UNIT4 = dict(
 title="Unit 4: Chemical Reactions and Stoichiometry",
 std="SC.912.P.8",
 topics=[
 dict(t="4.1 Chemical Reactions and Balancing Equations", std="SC.912.P.8",
 body="""A chemical reaction is a process in which one or more substances change into new substances. The starting materials are called reactants, and the new substances are called products. A chemical equation uses formulas to show a reaction, with reactants on the left, products on the right and the word yields or an arrow between them. Hebrews 1:3 says that Christ is upholding all things by the word of his power. The order we see in matter, including the way it is conserved in reactions, points to that faithful upholding.

The law of conservation of mass states that matter is neither created nor destroyed in an ordinary chemical reaction. The atoms in the reactants are rearranged into the products, so the number of atoms of each element must be the same on both sides. We balance equations by placing numbers called coefficients in front of formulas. We never change the small subscripts inside a formula, because that would change the substance. For example, hydrogen plus oxygen yields water is first written H2 plus O2 yields H2O. Oxygen is not balanced, so we write 2H2 plus O2 yields 2H2O. Now there are 4 hydrogen atoms and 2 oxygen atoms on each side.

Reactions fall into patterns. In a synthesis reaction, two or more substances combine into one. In a decomposition reaction, one compound breaks into simpler substances. In a single replacement reaction, one element replaces another in a compound. In a double replacement reaction, the ions of two compounds trade partners, often forming a precipitate, a gas or water. In a combustion reaction, a substance reacts rapidly with oxygen, releasing energy, as when a hydrocarbon burns to form carbon dioxide and water.

Your task: (1) State the law of conservation of mass. (2) Balance: Mg plus O2 yields MgO. (3) Identify each reaction type: 2H2O yields 2H2 plus O2, and CH4 plus 2O2 yields CO2 plus 2H2O.""",
 script="""Welcome back. Listen, Hebrews 1:3 says that Christ is upholding all things by the word of his power. The order we see in matter points to that faithful upholding.

Now watch this. A chemical reaction changes reactants into products. An equation shows the reactants on the left and the products on the right.

The law of conservation of mass says matter is neither created nor destroyed in an ordinary reaction. The atoms are rearranged, so each element must have the same number of atoms on both sides. We balance by placing coefficients in front of formulas. Never change the subscripts. H2 plus O2 yields H2O becomes 2H2 plus O2 yields 2H2O.

Types of reactions. Synthesis combines substances. Decomposition breaks one compound apart. Single replacement swaps one element for another. Double replacement trades partners and may form a precipitate, a gas or water. Combustion is rapid reaction with oxygen that releases energy.

Your task is to state the law, balance magnesium plus oxygen and identify two reaction types. Take the four question check.""" + CLOSE,
 quiz=[
 ("The law of conservation of mass says that in a chemical reaction:", ["Atoms are rearranged but not created or destroyed", "Mass is lost", "New atoms are made", "Mass always doubles"], 0, "Atoms are conserved."),
 ("When balancing an equation you may change:", ["Coefficients", "Subscripts", "Element symbols", "The reactants"], 0, "Only coefficients may be adjusted."),
 ("What coefficient goes in front of H2O in H2 plus O2 yields H2O when balanced as 2H2 plus O2 yields 2H2O?", ["2", "1", "3", "4"], 0, "Two water molecules balance the oxygen."),
 ("A reaction in which a compound breaks into simpler substances is:", ["Decomposition", "Synthesis", "Combustion", "Double replacement"], 0, "Decomposition separates a compound."),
 ]),
 dict(t="4.2 The Mole and Molar Mass", std="SC.912.P.8",
 body="""Atoms and molecules are far too small to count one at a time, so chemists use a counting unit called the mole. One mole of anything contains 6.02 times 10 to the 23rd particles. This number is called Avogadro's number. A mole of carbon atoms, a mole of water molecules and a mole of sodium chloride formula units each contain 6.02 times 10 to the 23rd particles. The mole is like a dozen, but for atoms. Proverbs 16:11 reminds us of the honesty of correct amounts: A just weight and balance are the LORD'S.

The molar mass of a substance is the mass in grams of one mole of it. It is numerically equal to the atomic mass from the periodic table, in grams per mole. Carbon has a molar mass of about 12.0 grams per mole. To find the molar mass of a compound, add the molar masses of all the atoms in the formula. For water, H2O, add 2 times 1.0 for hydrogen and 16.0 for oxygen to get 18.0 grams per mole. For carbon dioxide, add 12.0 and 2 times 16.0 to get 44.0 grams per mole.

Moles can be converted to grams and back. To change moles to grams, multiply by molar mass. To change grams to moles, divide by molar mass. For example, 36 grams of water divided by 18.0 grams per mole equals 2.0 moles. To change moles to particles, multiply by 6.02 times 10 to the 23rd. So 2.0 moles of water contain 1.2 times 10 to the 24th molecules.

Percent composition tells what percentage of a compound's mass comes from each element. In water, hydrogen makes up 2.0 divided by 18.0, or about 11 percent, and oxygen makes up about 89 percent.

Your task: (1) Find the molar mass of CaCO3 using Ca 40.1, C 12.0 and O 16.0. (2) Convert 88 grams of CO2 to moles. (3) Explain why chemists use the mole.""",
 script="""Welcome back. Listen, Proverbs 16:11 says, A just weight and balance are the LORD'S. Correct amounts matter.

Now watch this. Atoms are too small to count one at a time, so chemists use the mole. One mole is 6.02 times 10 to the 23rd particles. That is Avogadro's number. The mole is like a dozen, but for atoms.

Molar mass is the mass in grams of one mole. It equals the atomic mass from the periodic table, in grams per mole. For a compound, add the atoms in the formula. Water is 2 times 1.0 plus 16.0, which is 18.0 grams per mole. Carbon dioxide is 12.0 plus 2 times 16.0, which is 44.0.

Moles to grams, multiply by molar mass. Grams to moles, divide by molar mass. Thirty six grams of water is 2.0 moles. Moles to particles, multiply by 6.02 times 10 to the 23rd.

Percent composition tells the percentage of the mass from each element.

Your task is to find the molar mass of calcium carbonate, convert 88 grams of carbon dioxide to moles and explain the mole. Take the four question check.""" + CLOSE,
 quiz=[
 ("One mole contains how many particles?", ["6.02 times 10 to the 23rd", "6.02 times 10 to the 32nd", "One thousand", "One million"], 0, "Avogadro's number is 6.02 times 10 to the 23rd."),
 ("The molar mass of water is about:", ["18.0 grams per mole", "16.0 grams per mole", "10.0 grams per mole", "34.0 grams per mole"], 0, "2 hydrogen plus 1 oxygen gives 18.0."),
 ("To convert grams to moles you:", ["Divide by molar mass", "Multiply by molar mass", "Add molar mass", "Divide by 6.02"], 0, "Moles equal grams divided by molar mass."),
 ("How many moles are in 44 grams of CO2 (molar mass 44.0 grams per mole)?", ["1.0", "2.0", "0.5", "44"], 0, "44 divided by 44 equals 1."),
 ]),
 dict(t="4.3 Stoichiometry: Mole Ratios and Mass Calculations", std="SC.912.P.8",
 body="""Stoichiometry is the calculation of the amounts of reactants and products in a chemical reaction. It uses the balanced equation as a recipe. Proverbs 25:2 reminds us that it is the glory of God to conceal a thing, and a faithful scientist searches it out with careful work. A baker follows a recipe to make the right number of loaves, and a chemist follows the coefficients to predict the right amount of product.

The coefficients in a balanced equation give the mole ratio. In the reaction N2 plus 3H2 yields 2NH3, one mole of nitrogen reacts with three moles of hydrogen to make two moles of ammonia. The mole ratio of hydrogen to ammonia is 3 to 2. If 6 moles of hydrogen react, the amount of ammonia is 6 times 2 over 3, which is 4 moles.

To solve a mass problem, follow a pattern. First, write the balanced equation. Second, convert the given mass to moles using molar mass. Third, use the mole ratio from the coefficients to find moles of the wanted substance. Fourth, convert moles to grams with molar mass. For example, consider 2H2 plus O2 yields 2H2O. How many grams of water form from 4.0 grams of hydrogen? Hydrogen has a molar mass of 2.0 grams per mole, so 4.0 grams is 2.0 moles. The ratio of water to hydrogen is 2 to 2, so 2.0 moles of water form. Water has a molar mass of 18.0 grams per mole, so 2.0 moles is 36 grams.

Always write units, check that the answer is reasonable, and remember that mass is conserved: the total mass of the reactants equals the total mass of the products.

Your task: (1) In 2H2 plus O2 yields 2H2O, find the moles of water from 3 moles of oxygen. (2) Describe the four steps for a mass to mass problem. (3) Explain why the balanced equation must come first.""",
 script="""Welcome back. Listen, Proverbs 25:2 says, It is the glory of God to conceal a thing: but the honour of kings is to search out a matter. A faithful scientist searches it out with careful work.

Now watch this. Stoichiometry predicts the amounts of reactants and products. The balanced equation is the recipe, and the coefficients give the mole ratio.

N2 plus 3H2 yields 2NH3. One mole of nitrogen reacts with three moles of hydrogen to make two moles of ammonia. If 6 moles of hydrogen react, you get 4 moles of ammonia.

For a mass problem. One, write the balanced equation. Two, convert grams to moles. Three, use the mole ratio. Four, convert moles to grams.

Example. 2H2 plus O2 yields 2H2O. How many grams of water from 4.0 grams of hydrogen? That is 2.0 moles of hydrogen. The ratio is 2 to 2, so 2.0 moles of water. Times 18.0 grams per mole is 36 grams.

Write units. Check that the answer is reasonable. Mass is conserved.

Your task is to find moles of water from 3 moles of oxygen, describe the four steps and explain why the equation comes first. Take the four question check.""" + CLOSE,
 quiz=[
 ("In N2 plus 3H2 yields 2NH3, the mole ratio of H2 to NH3 is:", ["3 to 2", "2 to 3", "1 to 2", "1 to 3"], 0, "Coefficients give the ratio."),
 ("The first step in a stoichiometry problem is to:", ["Write the balanced equation", "Convert to particles", "Find percent yield", "Measure the volume"], 0, "The balanced equation gives the ratios."),
 ("In 2H2 plus O2 yields 2H2O, how many moles of water form from 2 moles of oxygen?", ["4", "2", "1", "8"], 0, "Ratio of water to oxygen is 2 to 1."),
 ("Total mass of reactants compared to total mass of products is:", ["Equal", "Greater", "Smaller", "Unrelated"], 0, "Mass is conserved."),
 ]),
 dict(t="4.4 Limiting Reactants and Percent Yield", std="SC.912.P.8",
 body="""In real reactions, reactants are often not present in exactly the right proportions. The limiting reactant is the reactant that is used up first and so limits how much product can form. The reactant that remains is the excess reactant. Luke 14:28 says, For which of you, intending to build a tower, sitteth not down first, and counteth the cost, whether he have sufficient to finish it? A wise builder counts what supplies are on hand, and so does a chemist.

Think of making sandwiches with 10 slices of bread and 4 slices of cheese, where each sandwich needs 2 slices of bread and 1 slice of cheese. The bread could make 5 sandwiches, but the cheese makes only 4, so the cheese is the limiting reactant. To find the limiting reactant, calculate how much product each reactant could make, using the balanced equation. The smaller amount of product shows the limiting reactant, and that smaller amount is the theoretical yield.

For example, in 2H2 plus O2 yields 2H2O, suppose there are 2 moles of hydrogen and 2 moles of oxygen. Two moles of hydrogen would need only 1 mole of oxygen, so hydrogen is limiting and oxygen is in excess. The 2 moles of hydrogen produce 2 moles of water.

The theoretical yield is the maximum amount of product predicted by the calculation. The actual yield is the amount actually obtained in the lab. Percent yield equals actual yield divided by theoretical yield, times 100. If the theoretical yield is 10.0 grams and 8.0 grams is obtained, the percent yield is 80 percent. Yields are lower than 100 percent because of incomplete reactions, side reactions and losses during collection. John 6:12 says, Gather up the fragments that remain, that nothing be lost. Industry works to reduce waste and improve yield.

Your task: (1) Define limiting reactant. (2) Find the limiting reactant if 3 moles of hydrogen and 2 moles of oxygen react in 2H2 plus O2 yields 2H2O. (3) Calculate percent yield for an actual yield of 15 grams and a theoretical yield of 20 grams.""",
 script="""Welcome back. Listen, Luke 14:28 says, For which of you, intending to build a tower, sitteth not down first, and counteth the cost, whether he have sufficient to finish it? A wise builder counts supplies, and so does a chemist.

Now watch this. The limiting reactant is used up first and limits the product. The reactant left over is the excess reactant.

With 10 slices of bread and 4 slices of cheese, and each sandwich needing 2 bread and 1 cheese, the bread could make 5 sandwiches but the cheese only 4. The cheese is limiting.

In chemistry, calculate how much product each reactant could make. The smaller amount shows the limiting reactant and is the theoretical yield. For 2 moles of hydrogen and 2 moles of oxygen, hydrogen needs only 1 mole of oxygen, so hydrogen is limiting and makes 2 moles of water.

Percent yield is actual yield divided by theoretical yield, times 100. Eight grams from a theoretical 10 grams is 80 percent. John 6:12 says, Gather up the fragments that remain, that nothing be lost.

Your task is to define limiting reactant, find it for 3 moles hydrogen and 2 moles oxygen and calculate a percent yield. Take the four question check.""" + CLOSE,
 quiz=[
 ("The reactant that is completely used up first is the:", ["Limiting reactant", "Excess reactant", "Catalyst", "Product"], 0, "It limits how much product forms."),
 ("Percent yield equals:", ["Actual divided by theoretical, times 100", "Theoretical divided by actual, times 100", "Actual plus theoretical", "Actual minus theoretical"], 0, "Percent yield compares actual to theoretical."),
 ("An actual yield of 8.0 grams and a theoretical yield of 10.0 grams gives a percent yield of:", ["80 percent", "125 percent", "8 percent", "18 percent"], 0, "8 divided by 10 times 100 equals 80."),
 ("The maximum amount of product a reaction can make is the:", ["Theoretical yield", "Actual yield", "Excess", "Percent yield"], 0, "Theoretical yield comes from the calculation."),
 ]),
 ],
 assess=dict(t="Assessment 4: Chemical Reactions and Stoichiometry",
 prompt="""Write a report of at least 250 words on chemical reactions and calculations. Use complete sentences and label each part. Luke 14:28 says, For which of you, intending to build a tower, sitteth not down first, and counteth the cost, whether he have sufficient to finish it?

Part 1: State the law of conservation of mass and explain why we balance equations. Balance Na plus Cl2 yields NaCl, and C3H8 plus O2 yields CO2 plus H2O. Name the five types of reactions and give an example of each.
Part 2: Define mole and Avogadro's number. Find the molar mass of Na2SO4 and calculate how many moles are in 71 grams of it, showing your work. Use Na 23.0, S 32.0 and O 16.0.
Part 3: Using 2H2 plus O2 yields 2H2O, find the grams of water made from 8.0 grams of hydrogen, showing all steps.
Part 4: Define limiting reactant, theoretical yield, actual yield and percent yield. Calculate percent yield when 18 grams are obtained from a theoretical 24 grams.
Part 5: Explain how John 6:12 and Luke 14:28 apply to wise use of resources in industry and in life.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 25 points. Part 3: 20 points. Part 4: 20 points. Part 5: 10 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 4: Counteth the Cost",
 prompt="""Write a post of at least 120 words that (1) explains in your own words why chemical equations must be balanced and how conservation of mass shows order in creation, (2) describes a real life situation, such as cooking, building or budgeting, where a limiting resource decides how much you can make, (3) explains why waste should be reduced in industry and at home, and (4) connects your answer to Hebrews 1:3, Luke 14:28 or John 6:12. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why do you think the mole was invented? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("In a chemical reaction the starting substances are the:", ["Reactants", "Products", "Catalysts", "Isotopes"], 0, "Reactants are on the left side."),
 ("Which type of reaction produces carbon dioxide and water from a hydrocarbon and oxygen?", ["Combustion", "Synthesis", "Decomposition", "Single replacement"], 0, "Burning in oxygen is combustion."),
 ("A mole of any substance contains:", ["6.02 times 10 to the 23rd particles", "One gram", "One liter", "100 particles"], 0, "Avogadro's number."),
 ("The molar mass of CO2 is about:", ["44 grams per mole", "28 grams per mole", "12 grams per mole", "32 grams per mole"], 0, "12 plus 2 times 16 equals 44."),
 ("How many moles are in 36 grams of water?", ["2.0", "1.0", "18", "0.5"], 0, "36 divided by 18 equals 2."),
 ("In 2H2 plus O2 yields 2H2O, 3 moles of oxygen make how many moles of water?", ["6", "3", "1.5", "2"], 0, "The ratio of water to oxygen is 2 to 1."),
 ("The limiting reactant is the one that:", ["Runs out first", "Is left over", "Has the most mass", "Is a catalyst"], 0, "It limits the product."),
 ("Percent yield of 15 grams actual and 20 grams theoretical is:", ["75 percent", "133 percent", "5 percent", "25 percent"], 0, "15 divided by 20 times 100 equals 75."),
 ]
)
