"""Chemistry, Unit 5: States of Matter, Gases, Solutions and Energy. Florida science standards cited at strand level (SC.912.P); recheck exact benchmark codes at CPALMS."""
from chem_units1 import CLOSE

UNIT5 = dict(
 title="Unit 5: States of Matter, Gases, Solutions and Energy",
 std="SC.912.P.8, SC.912.P.10",
 topics=[
 dict(t="5.1 States of Matter and Phase Changes", std="SC.912.P.8",
 body="""Matter commonly exists in three states: solid, liquid and gas. The kinetic molecular theory explains them. It says that all matter is made of tiny particles in constant motion, and that the average kinetic energy of the particles depends on the temperature. In a solid, particles vibrate in fixed positions, so a solid has a definite shape and volume. In a liquid, particles are close but can slide past each other, so a liquid has a definite volume but takes the shape of its container. In a gas, particles are far apart and move freely, so a gas has no definite shape or volume. Plasma, a fourth state, is a hot gas of charged particles found in stars and lightning. Job 38:22 asks, Hast thou entered into the treasures of the snow? The changing forms of water display the wonder of creation.

A phase change is a change from one state to another. Melting is solid to liquid, freezing is liquid to solid, vaporization is liquid to gas, condensation is gas to liquid, sublimation is solid to gas, and deposition is gas to solid. Evaporation happens at the surface of a liquid below its boiling point, while boiling happens throughout the liquid when its vapor pressure equals the surrounding pressure.

A heating curve graphs temperature against the energy added. When a substance is heating within one state, the temperature rises. During a phase change, the temperature stays constant, because the added energy is used to overcome attractions between particles instead of raising the temperature. For water, melting and freezing occur at 0 degrees Celsius, and boiling and condensation occur at 100 degrees Celsius at sea level pressure.

Water is unusual. Because of hydrogen bonding, solid water is less dense than liquid water, so ice floats. This protects life in lakes and ponds during winter.

Your task: (1) Compare the particles in solids, liquids and gases. (2) Name the phase change from a gas to a liquid and from a solid to a gas. (3) Explain why the temperature stays constant while ice melts.""",
 script="""Welcome back. Listen, Job 38:22 asks, Hast thou entered into the treasures of the snow? The changing forms of water display the wonder of creation.

Now watch this. Kinetic molecular theory says all matter is made of tiny particles in constant motion. In a solid, particles vibrate in fixed positions, so it has a definite shape and volume. In a liquid, particles slide past each other, so it has definite volume but takes the shape of its container. In a gas, particles are far apart and move freely. Plasma is a hot gas of charged particles.

Phase changes. Melting, freezing, vaporization, condensation, sublimation and deposition. Evaporation happens at the surface. Boiling happens throughout.

On a heating curve, temperature rises within a state but stays constant during a phase change, because the energy is used to overcome attractions between particles. Water melts at 0 degrees Celsius and boils at 100.

Because of hydrogen bonding, ice is less dense than liquid water and floats, protecting life in lakes.

Your task is to compare the states, name two phase changes and explain the constant temperature. Take the four question check.""" + CLOSE,
 quiz=[
 ("In which state do particles have a definite volume but no definite shape?", ["Liquid", "Solid", "Gas", "Crystal"], 0, "Liquids take the shape of their container."),
 ("The phase change from gas to liquid is:", ["Condensation", "Vaporization", "Sublimation", "Melting"], 0, "Condensation is gas to liquid."),
 ("During melting at constant pressure, the temperature of the substance:", ["Stays constant", "Rises quickly", "Falls", "Doubles"], 0, "Energy goes into changing the state."),
 ("Ice floats because solid water is:", ["Less dense than liquid water", "More dense than liquid water", "Made of different atoms", "Not made of molecules"], 0, "Hydrogen bonds hold ice in an open lattice."),
 ]),
 dict(t="5.2 The Gas Laws", std="SC.912.P.8",
 body="""Gases are described by four measurable properties: pressure, volume, temperature and the amount of gas in moles. Job 28:25 says that God made the weight for the winds, and weighed the waters by measure. The behavior of gases follows laws that scientists can measure and predict. In all gas law calculations, temperature must be in kelvin, found by adding 273 to the Celsius temperature.

Boyle's law says that for a fixed amount of gas at constant temperature, pressure and volume are inversely related: as volume decreases, pressure increases. P1 times V1 equals P2 times V2. If 4.0 liters of gas at 2.0 atmospheres is compressed to 1.0 liter, the new pressure is 8.0 atmospheres.

Charles's law says that for a fixed amount of gas at constant pressure, volume and kelvin temperature are directly related. V1 divided by T1 equals V2 divided by T2. If 2.0 liters at 300 kelvin is heated to 600 kelvin, the volume doubles to 4.0 liters.

Gay Lussac's law, in the same way, says pressure and kelvin temperature are directly related at constant volume. The combined gas law brings these together: P1 times V1 divided by T1 equals P2 times V2 divided by T2.

Avogadro's principle says equal volumes of gases at the same temperature and pressure contain equal numbers of particles. At standard temperature and pressure, 0 degrees Celsius and 1 atmosphere, one mole of any ideal gas occupies 22.4 liters.

The ideal gas law combines everything: PV equals nRT, where P is pressure, V is volume, n is moles, T is kelvin temperature and R is the gas constant, 0.0821 liter atmospheres per mole kelvin. Real gases behave most like ideal gases at high temperature and low pressure.

Your task: (1) Use Boyle's law to find the new volume when 6.0 liters at 1.0 atmosphere is compressed to 3.0 atmospheres. (2) Convert 27 degrees Celsius to kelvin. (3) Explain why a sealed balloon shrinks when placed in a freezer.""",
 script="""Welcome back. Listen, Job 28:25 says that God made the weight for the winds, and weighed the waters by measure. The behavior of gases follows laws we can measure.

Now watch this. Gases are described by pressure, volume, temperature and moles. Always use kelvin: add 273 to Celsius.

Boyle's law: pressure and volume are inversely related at constant temperature. P1 V1 equals P2 V2. Compress 4.0 liters at 2.0 atmospheres to 1.0 liter and the pressure is 8.0 atmospheres.

Charles's law: volume and kelvin temperature are directly related at constant pressure. Double the kelvin temperature and the volume doubles.

Gay Lussac: pressure and kelvin temperature are directly related at constant volume. The combined gas law joins them.

Avogadro: equal volumes of gases at the same temperature and pressure hold equal numbers of particles. At standard temperature and pressure, one mole is 22.4 liters.

The ideal gas law is PV equals nRT, with R equal to 0.0821.

Your task is to apply Boyle's law, convert 27 degrees Celsius to kelvin and explain the balloon in the freezer. Take the four question check.""" + CLOSE,
 quiz=[
 ("Boyle's law relates pressure and volume as:", ["Inversely proportional", "Directly proportional", "Unrelated", "Equal"], 0, "When volume goes down, pressure goes up."),
 ("27 degrees Celsius equals how many kelvin?", ["300", "246", "27", "373"], 0, "Add 273."),
 ("One mole of an ideal gas at standard temperature and pressure occupies:", ["22.4 liters", "1.0 liter", "100 liters", "6.02 liters"], 0, "Molar volume at STP is 22.4 liters."),
 ("6.0 liters at 1.0 atmosphere is compressed to 3.0 atmospheres. The new volume is:", ["2.0 liters", "18 liters", "0.5 liters", "6.0 liters"], 0, "P1 V1 equals P2 V2 gives 2.0."),
 ]),
 dict(t="5.3 Solutions, Solubility and Molarity", std="SC.912.P.8",
 body="""A solution is a homogeneous mixture of two or more substances. The solute is the substance that is dissolved, and the solvent is the substance that does the dissolving. In salt water, salt is the solute and water is the solvent. Water is called the universal solvent because of its ability to dissolve so many substances, due to its polarity. Jesus said in Matthew 5:13, Ye are the salt of the earth. Salt dissolves and spreads its flavor and influence. A believer is called to make a positive difference in the world.

Solubility is the maximum amount of solute that dissolves in a given amount of solvent at a given temperature. A solution is unsaturated if it can dissolve more solute, saturated if it holds the maximum, and supersaturated if it holds more than normal, which is unstable. In general, the solubility of most solids increases with temperature, while the solubility of gases decreases with temperature. That is why a warm soft drink goes flat faster. Stirring, crushing the solute and heating speed up dissolving but do not change how much can dissolve at a given temperature.

Concentration describes how much solute is in a solution. Molarity is the most common measure. Molarity equals moles of solute divided by liters of solution, and its unit is M, which means moles per liter. If 2.0 moles of sodium chloride are dissolved to make 4.0 liters of solution, the molarity is 0.50 M. To find the moles needed, multiply molarity by volume. To make 1.0 liter of 2.0 M sodium chloride, you need 2.0 moles, which is 117 grams, since the molar mass is 58.5 grams per mole.

To dilute a solution, add solvent. The moles of solute stay the same, so M1 times V1 equals M2 times V2. To dilute 100 milliliters of 2.0 M solution to 0.50 M, V2 equals 2.0 times 100 divided by 0.50, which is 400 milliliters.

Your task: (1) Define solute and solvent. (2) Calculate the molarity of 3.0 moles of solute in 1.5 liters. (3) Explain why a warm soft drink loses its fizz faster.""",
 script="""Welcome back. Listen, Jesus said in Matthew 5:13, Ye are the salt of the earth. Salt dissolves and spreads its flavor and influence. A believer is called to make a positive difference.

Now watch this. A solution is a homogeneous mixture. The solute is dissolved. The solvent does the dissolving. In salt water, salt is the solute and water is the solvent. Water dissolves many substances because it is polar.

Solubility is the maximum solute that dissolves in a given amount of solvent at a given temperature. Unsaturated can dissolve more. Saturated holds the maximum. Supersaturated holds more than normal and is unstable. Most solids dissolve better when hot, but gases dissolve less, so a warm soft drink goes flat faster.

Molarity is moles of solute divided by liters of solution. Two moles in 4 liters is 0.50 M. To make 1 liter of 2.0 M salt solution, use 117 grams.

For dilution, the moles of solute stay the same. M1 V1 equals M2 V2.

Your task is to define solute and solvent, calculate a molarity and explain the soft drink. Take the four question check.""" + CLOSE,
 quiz=[
 ("In a sugar and water solution, water is the:", ["Solvent", "Solute", "Precipitate", "Product"], 0, "The solvent does the dissolving."),
 ("Molarity is moles of solute per:", ["Liter of solution", "Gram of solvent", "Kilogram of solute", "Milliliter of solute"], 0, "Molarity equals moles per liter of solution."),
 ("The molarity of 3.0 moles of solute in 1.5 liters is:", ["2.0 M", "4.5 M", "0.5 M", "1.5 M"], 0, "3.0 divided by 1.5 equals 2.0."),
 ("The solubility of most gases in water as temperature increases:", ["Decreases", "Increases", "Stays the same", "Doubles"], 0, "Warm liquids hold less dissolved gas."),
 ]),
 dict(t="5.4 Energy and Thermochemistry", std="SC.912.P.10",
 body="""Every chemical and physical change involves energy. Isaiah 40:31 says, But they that wait upon the LORD shall renew their strength; they shall mount up with wings as eagles; they shall run, and not be weary. Spiritual strength comes from the Lord, and physical energy comes from the chemical energy in food, which our bodies release by chemical reactions.

Thermochemistry is the study of heat in chemical reactions. Heat is energy that moves from a warmer object to a cooler one, and temperature measures the average kinetic energy of particles. Energy is measured in joules, and one calorie equals about 4.18 joules. The food Calorie, written with a capital C, is 1000 calories, or one kilocalorie.

A reaction that releases heat to the surroundings is exothermic. Burning wood and the reaction of a hand warmer are exothermic, and the surroundings get warmer. A reaction that absorbs heat is endothermic. An instant cold pack is endothermic, and the surroundings get cooler. Breaking bonds requires energy, and forming bonds releases energy. The overall change depends on which is larger. The change in heat content at constant pressure is called enthalpy change, with a negative sign for exothermic reactions and a positive sign for endothermic reactions.

Specific heat is the energy needed to raise the temperature of 1 gram of a substance by 1 degree Celsius. Water has a high specific heat of 4.18 joules per gram degree Celsius, so it heats and cools slowly. This helps moderate climates and keeps our body temperatures steady. The heat gained or lost is calculated with q equals m times c times the change in temperature. To warm 50 grams of water by 20 degrees Celsius, q equals 50 times 4.18 times 20, which is 4180 joules.

The law of conservation of energy states that energy cannot be created or destroyed, only transferred or changed in form. A catalyst can lower the energy needed to start a reaction without being used up.

Your task: (1) Compare exothermic and endothermic reactions with an example of each. (2) Calculate the heat needed to warm 100 grams of water by 10 degrees Celsius using 4.18 joules per gram degree Celsius. (3) Explain why water's high specific heat is important.""",
 script="""Welcome back. Listen, Isaiah 40:31 says, But they that wait upon the LORD shall renew their strength; they shall mount up with wings as eagles; they shall run, and not be weary. Spiritual strength comes from the Lord, and physical energy comes from chemical reactions in the food we eat.

Now watch this. Thermochemistry studies heat in reactions. Heat is energy moving from warmer to cooler. Temperature measures the average kinetic energy of particles. We measure energy in joules. One calorie is about 4.18 joules.

An exothermic reaction releases heat. Burning wood is exothermic. An endothermic reaction absorbs heat. An instant cold pack is endothermic. Breaking bonds takes energy. Forming bonds releases energy.

Specific heat is the energy to raise 1 gram by 1 degree Celsius. Water's is high, 4.18 joules per gram degree Celsius, so it heats and cools slowly. That moderates climates and keeps our bodies steady. The formula is q equals m times c times the change in temperature. Fifty grams warmed 20 degrees needs 4180 joules.

Energy is conserved. A catalyst lowers the energy needed to start a reaction and is not used up.

Your task is to compare exothermic and endothermic reactions, calculate heat for 100 grams of water and explain specific heat. Take the four question check.""" + CLOSE,
 quiz=[
 ("A reaction that releases heat to its surroundings is:", ["Exothermic", "Endothermic", "Isothermal", "Nuclear"], 0, "Exothermic reactions give off heat."),
 ("An instant cold pack feels cold because the reaction is:", ["Endothermic", "Exothermic", "Combustion", "Nuclear"], 0, "It absorbs heat from the surroundings."),
 ("Heat gained or lost can be calculated with:", ["q equals m times c times change in temperature", "q equals m divided by c", "q equals c plus m", "q equals PV"], 0, "That is the specific heat equation."),
 ("Heat needed to warm 100 grams of water by 10 degrees Celsius is about:", ["4180 joules", "418 joules", "1000 joules", "41.8 joules"], 0, "100 times 4.18 times 10 equals 4180."),
 ]),
 ],
 assess=dict(t="Assessment 5: States of Matter, Gases, Solutions and Energy",
 prompt="""Write a report of at least 250 words on matter, gases, solutions and energy. Use complete sentences and label each part. Isaiah 40:31 says, But they that wait upon the LORD shall renew their strength.

Part 1: Compare solids, liquids and gases using kinetic molecular theory. Name all six phase changes and explain why temperature stays constant during a phase change. Explain why ice floats.
Part 2: State Boyle's law, Charles's law and the ideal gas law. Solve: a gas at 3.0 liters and 1.0 atmosphere is compressed to 1.5 liters at constant temperature. Find the new pressure. Convert 50 degrees Celsius to kelvin.
Part 3: Define solute, solvent, saturated and unsaturated. Calculate the molarity when 0.50 moles of solute are dissolved to make 2.0 liters of solution. Explain how temperature affects the solubility of solids and gases.
Part 4: Explain exothermic and endothermic reactions with an example of each. Use q equals m times c times the change in temperature to find the heat needed to warm 200 grams of water by 5.0 degrees Celsius, using 4.18 joules per gram degree Celsius.
Part 5: Explain how Job 28:25 and Matthew 5:13 or Isaiah 40:31 add meaning to what you learned.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 25 points. Part 3: 20 points. Part 4: 20 points. Part 5: 10 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 5: Ye Are the Salt of the Earth",
 prompt="""Write a post of at least 120 words that (1) explains how salt dissolving in water can illustrate what Jesus meant when He called believers the salt of the earth, (2) describes one everyday example of a gas law, such as a tire, a balloon or a soft drink, (3) explains why water's special properties matter for life, and (4) connects your answer to Matthew 5:13, Job 38:22, Job 28:25 or Isaiah 40:31. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why should people take care to keep water clean? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("Particles in a gas are:", ["Far apart and moving freely", "Locked in place", "Touching in a lattice", "Not moving"], 0, "Gas particles have very weak attractions."),
 ("The phase change from solid directly to gas is:", ["Sublimation", "Deposition", "Condensation", "Freezing"], 0, "Sublimation skips the liquid state."),
 ("Pressure and volume of a gas at constant temperature are:", ["Inversely related", "Directly related", "Equal", "Unrelated"], 0, "That is Boyle's law."),
 ("A temperature of 0 degrees Celsius equals:", ["273 kelvin", "0 kelvin", "100 kelvin", "373 kelvin"], 0, "Add 273."),
 ("A solution that holds the maximum amount of solute at a given temperature is:", ["Saturated", "Unsaturated", "Dilute", "Insoluble"], 0, "Saturated means no more will dissolve."),
 ("The molarity of 1.0 mole of solute in 0.50 liter of solution is:", ["2.0 M", "0.5 M", "1.0 M", "5.0 M"], 0, "1.0 divided by 0.50 equals 2.0."),
 ("A reaction that absorbs heat is called:", ["Endothermic", "Exothermic", "A catalyst", "A precipitate"], 0, "Endothermic reactions take in heat."),
 ("Water's high specific heat means it:", ["Heats and cools slowly", "Boils at a low temperature", "Always freezes quickly", "Cannot absorb heat"], 0, "It takes much energy to change water's temperature."),
 ]
)
