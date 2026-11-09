"""Chemistry, Unit 6: Acids and Bases, Rates, Equilibrium, Redox, Nuclear and Organic Chemistry. Florida science standards cited at strand level (SC.912.P, SC.912.L); recheck exact benchmark codes at CPALMS."""
from chem_units1 import CLOSE

UNIT6 = dict(
 title="Unit 6: Acids and Bases, Reaction Rates, Redox, Nuclear and Organic Chemistry",
 std="SC.912.P.8, SC.912.L.18",
 topics=[
 dict(t="6.1 Acids, Bases and pH", std="SC.912.P.8",
 body="""Acids and bases are among the most important groups of compounds. Proverbs 25:20 mentions vinegar poured upon nitre, an everyday picture of a lively chemical reaction. Vinegar is a weak acid, and acids react with many substances.

An acid, according to Arrhenius, produces hydrogen ions in water. A base produces hydroxide ions in water. A broader definition by Bronsted and Lowry says an acid is a proton donor and a base is a proton acceptor. Acids taste sour, turn blue litmus paper red, and react with some metals to produce hydrogen gas. Bases taste bitter, feel slippery, and turn red litmus paper blue. Never taste or touch chemicals in a lab. Common acids include hydrochloric acid, sulfuric acid, nitric acid and acetic acid in vinegar. Common bases include sodium hydroxide, ammonia and the baking soda in your kitchen.

A strong acid or base ionizes almost completely in water, while a weak acid or base ionizes only partly. Strong and weak describe how much it ionizes, and concentrated and dilute describe how much is dissolved. Both strong and weak acids can be dangerous, and strong ones are especially hazardous.

The pH scale measures how acidic or basic a solution is, usually from 0 to 14. A pH of 7 is neutral, as in pure water. A pH below 7 is acidic, and a pH above 7 is basic. Each whole number change in pH is a tenfold change in hydrogen ion concentration, so a solution with pH 3 is ten times more acidic than one with pH 4. Lemon juice is about pH 2, milk about 6.5, blood about 7.4 and household ammonia about 11. Indicators such as litmus, phenolphthalein and universal indicator change color with pH.

In a neutralization reaction, an acid and a base react to form a salt and water. Hydrochloric acid plus sodium hydroxide yields sodium chloride plus water. Neutralization is used in antacids, in treating spills and in titrations. At home, never mix cleaners such as bleach and ammonia, because toxic gases can form.

Your task: (1) Compare acids and bases using three properties each. (2) Explain what pH 3 compared with pH 5 means. (3) Write a word equation for a neutralization reaction.""",
 script="""Welcome back. Listen, Proverbs 25:20 mentions vinegar poured upon nitre, an everyday picture of a lively reaction. Vinegar is a weak acid.

Now watch this. An acid produces hydrogen ions in water. A base produces hydroxide ions. Bronsted and Lowry say an acid donates a proton and a base accepts a proton. Acids taste sour, turn blue litmus red and react with some metals to make hydrogen. Bases taste bitter, feel slippery and turn red litmus blue. Never taste or touch lab chemicals.

Strong acids and bases ionize almost completely. Weak ones ionize partly. Strong and weak are not the same as concentrated and dilute.

The pH scale runs from 0 to 14. Seven is neutral. Below 7 is acidic. Above 7 is basic. Each whole number is a tenfold change. Lemon juice is about 2. Milk is about 6.5. Blood is about 7.4. Ammonia is about 11.

Neutralization produces a salt and water. Hydrochloric acid plus sodium hydroxide yields sodium chloride and water.

At home, never mix bleach with ammonia or other cleaners.

Your task is to compare acids and bases, explain pH 3 versus pH 5 and write a neutralization equation. Take the four question check.""" + CLOSE,
 quiz=[
 ("A solution with a pH of 7 is:", ["Neutral", "Acidic", "Basic", "Radioactive"], 0, "Seven is neutral."),
 ("A solution with pH 3 compared to pH 5 is:", ["100 times more acidic", "Twice as acidic", "Ten times more basic", "The same"], 0, "Two pH units is a factor of 100."),
 ("An acid and a base react in neutralization to form:", ["A salt and water", "Two acids", "Only gas", "Two bases"], 0, "Neutralization forms salt and water."),
 ("According to Bronsted and Lowry, an acid is a:", ["Proton donor", "Proton acceptor", "Electron donor", "Neutron acceptor"], 0, "Acids donate protons."),
 ]),
 dict(t="6.2 Reaction Rates and Chemical Equilibrium", std="SC.912.P.8",
 body="""Some reactions happen in an instant, like an explosion, and others take years, like rusting. The rate of a reaction is how fast reactants are used up or products are formed. Ecclesiastes 3:1 says, To every thing there is a season, and a time to every purpose under the heaven. Chemists study the timing of reactions so they can speed up helpful ones and slow down harmful ones.

Collision theory says that a reaction occurs when particles collide with enough energy and the right orientation. The minimum energy needed is called the activation energy. Several factors change the rate. Raising the temperature makes particles move faster and collide more often and with more energy. Increasing concentration, or pressure for gases, means more collisions. Increasing surface area, such as by crushing a solid, exposes more particles. A catalyst speeds up a reaction by providing a path with lower activation energy and is not used up. Enzymes in our bodies are biological catalysts. Food is stored in a refrigerator to slow reactions that cause spoilage.

Many reactions are reversible, meaning products can turn back into reactants. In a closed system, a reversible reaction can reach chemical equilibrium, the point at which the forward and reverse reactions occur at equal rates. At equilibrium the amounts of reactants and products stay constant, but the reactions have not stopped. They continue in both directions at the same pace. An equilibrium is shown with a double arrow, or in words as reversible.

Le Chatelier's principle says that if a system at equilibrium is disturbed, it shifts to partly counteract the change. Adding more reactant shifts the reaction toward products. Removing a product also shifts it toward products. Raising the temperature favors the endothermic direction. Increasing the pressure on a gas reaction favors the side with fewer gas particles. The industrial production of ammonia for fertilizer uses these ideas to improve the yield. Colossians 1:17 says of Christ, by him all things consist.

Your task: (1) List four ways to speed up a reaction. (2) Explain what a catalyst does. (3) Describe what happens to the system if more reactant is added to a reaction at equilibrium.""",
 script="""Welcome back. Listen, Ecclesiastes 3:1 says, To every thing there is a season, and a time to every purpose under the heaven. Chemists study timing so they can speed up helpful reactions and slow down harmful ones.

Now watch this. Collision theory says a reaction occurs when particles collide with enough energy and the right orientation. The minimum energy is the activation energy.

To speed up a reaction, raise the temperature, increase the concentration, increase the surface area or add a catalyst. A catalyst lowers the activation energy and is not used up. Enzymes are biological catalysts. We refrigerate food to slow spoilage.

Many reactions are reversible. At chemical equilibrium the forward and reverse reactions happen at equal rates. The amounts stay constant, but the reactions have not stopped.

Le Chatelier's principle says that if a system at equilibrium is disturbed, it shifts to partly counteract the change. Add reactant and it shifts toward products. Remove a product and it shifts toward products. Colossians 1:17 says of Christ, by him all things consist.

Your task is to list four ways to speed up a reaction, explain a catalyst and describe adding reactant at equilibrium. Take the four question check.""" + CLOSE,
 quiz=[
 ("The minimum energy needed for a reaction to occur is the:", ["Activation energy", "Heat of fusion", "Molar mass", "Atomic number"], 0, "Reactions must overcome the activation energy."),
 ("A catalyst speeds up a reaction by:", ["Lowering the activation energy", "Being consumed", "Raising the activation energy", "Removing reactants"], 0, "It provides an easier path."),
 ("At chemical equilibrium, the forward and reverse reaction rates are:", ["Equal", "Zero", "Different", "Doubled each second"], 0, "The reactions continue at equal rates."),
 ("Crushing a solid reactant speeds up a reaction because it increases:", ["Surface area", "Molar mass", "Activation energy", "Atomic number"], 0, "More surface exposes more particles."),
 ]),
 dict(t="6.3 Oxidation, Reduction and Electrochemistry", std="SC.912.P.10",
 body="""Many important reactions involve the transfer of electrons. These are oxidation reduction reactions, called redox reactions for short. Oxidation is the loss of electrons, and reduction is the gain of electrons. A memory aid is OIL RIG: Oxidation Is Loss, Reduction Is Gain. The two always occur together, because electrons lost by one substance are gained by another. The substance that is oxidized is the reducing agent, and the substance that is reduced is the oxidizing agent.

Oxidation numbers help track electrons. A pure element has an oxidation number of zero. A simple ion has an oxidation number equal to its charge. If a number increases, the atom was oxidized, and if it decreases, the atom was reduced. When zinc metal is placed in a copper solution, zinc loses 2 electrons and goes into solution, and copper ions gain 2 electrons and form copper metal. Zinc is oxidized and copper is reduced.

Redox reactions are all around us. Rusting is the slow oxidation of iron in the presence of water and oxygen. Combustion and cellular respiration are redox reactions. Metals can be protected by painting, coating with zinc in galvanizing, or keeping them dry. Bleach works by oxidation.

Electrochemistry is the study of how chemical reactions and electrical energy are related. A galvanic cell, or battery, uses a spontaneous redox reaction to produce electric current. Oxidation takes place at the anode and reduction at the cathode, and electrons flow through a wire from anode to cathode. Electrolysis does the reverse: it uses electricity to force a nonspontaneous reaction, as in plating metals or separating aluminum from its ore.

Scripture often uses refining as a picture of God's work. Malachi 3:3 says, And he shall sit as a refiner and purifier of silver. 1 Peter 1:7 says that the trial of your faith is much more precious than of gold that perisheth, though it be tried with fire.

Your task: (1) State what OIL RIG means. (2) Identify what is oxidized and reduced when zinc reacts with copper ions. (3) Explain how a battery produces electric current.""",
 script="""Welcome back. Listen, Malachi 3:3 says, And he shall sit as a refiner and purifier of silver. And 1 Peter 1:7 says the trial of your faith is much more precious than of gold that perisheth, though it be tried with fire. Scripture uses refining to picture God's work.

Now watch this. Redox reactions transfer electrons. Oxidation is loss of electrons. Reduction is gain of electrons. OIL RIG: Oxidation Is Loss, Reduction Is Gain. They always happen together.

The substance oxidized is the reducing agent. The substance reduced is the oxidizing agent.

When zinc is placed in a copper solution, zinc loses 2 electrons and copper ions gain 2. Zinc is oxidized. Copper is reduced.

Rusting is slow oxidation of iron with water and oxygen. Combustion and cellular respiration are redox reactions. Paint and zinc coatings protect metal.

A galvanic cell, or battery, uses a spontaneous redox reaction to make current. Oxidation at the anode, reduction at the cathode, and electrons flow through the wire. Electrolysis uses electricity to force a reaction.

Your task is to explain OIL RIG, identify what is oxidized and reduced and explain how a battery works. Take the four question check.""" + CLOSE,
 quiz=[
 ("Oxidation is the:", ["Loss of electrons", "Gain of electrons", "Loss of protons", "Gain of neutrons"], 0, "OIL: Oxidation Is Loss."),
 ("In a galvanic cell, reduction occurs at the:", ["Cathode", "Anode", "Wire", "Salt bridge only"], 0, "Reduction happens at the cathode."),
 ("Rusting is an example of:", ["Oxidation of iron", "Reduction of iron", "Neutralization", "Sublimation"], 0, "Iron loses electrons to oxygen."),
 ("Using electricity to force a nonspontaneous reaction is:", ["Electrolysis", "Combustion", "Dilution", "Distillation"], 0, "Electrolysis drives reactions with current."),
 ]),
 dict(t="6.4 Nuclear and Organic Chemistry, and Stewardship of Creation", std="SC.912.P.10, SC.912.L.18",
 body="""Chemistry reaches from the nucleus of the atom to the molecules of life. Psalm 24:1 says, The earth is the LORD'S, and the fulness thereof; the world, and they that dwell therein. Genesis 2:15 says that the LORD God took the man, and put him into the garden of Eden to dress it and to keep it. Chemists are called, like all people, to use creation wisely and protect it.

Nuclear chemistry studies changes in the nucleus. Some nuclei are unstable and give off radiation in a process called radioactive decay. Alpha particles are helium nuclei with 2 protons and 2 neutrons, beta particles are fast electrons and gamma rays are high energy radiation. Gamma rays penetrate the most and alpha particles the least. The half life of an isotope is the time for half of a sample to decay. If an isotope has a half life of 5 years, 80 grams will become 40 grams after 5 years, 20 grams after 10 years and 10 grams after 15 years. Fission splits a heavy nucleus such as uranium, releasing great energy, and is used in nuclear power plants. Fusion joins light nuclei and powers the Sun. Radioisotopes are used in medicine, in smoke detectors and in dating. Radiation can also harm living tissue, so it must be handled with care and respect. Isaiah 2:4 speaks of the hope of turning weapons into plowshares.

Organic chemistry is the study of carbon compounds. Carbon forms four bonds and can make long chains and rings, which is why there are millions of organic compounds. Hydrocarbons contain only carbon and hydrogen, such as methane, ethane and propane. Functional groups give families of compounds their properties, such as alcohols, organic acids and amines. The large molecules of life are carbohydrates, lipids, proteins and nucleic acids, and they are built from smaller units.

Chemistry serves people through medicine, food, clean water, fuels, fertilizers and materials. It also raises responsibilities: preventing pollution, using resources wisely, recycling, disposing of chemicals safely and telling the truth about risks. Careers include chemist, chemical engineer, pharmacist, nurse, physician, environmental scientist, forensic scientist and teacher.

Your task: (1) Describe alpha, beta and gamma radiation. (2) Calculate how much of a 40 gram sample remains after 2 half lives. (3) Explain two ways a Christian chemist can practice stewardship.""",
 script="""Welcome back. Listen, Psalm 24:1 says, The earth is the LORD'S, and the fulness thereof; the world, and they that dwell therein. And Genesis 2:15 says the man was put in the garden to dress it and to keep it. Chemists are called, like all people, to use creation wisely and protect it.

Now watch this. Nuclear chemistry studies the nucleus. Unstable nuclei give off radiation by radioactive decay. Alpha particles are helium nuclei. Beta particles are fast electrons. Gamma rays are high energy radiation. Gamma penetrates the most.

A half life is the time for half of a sample to decay. With a half life of 5 years, 80 grams becomes 40, then 20, then 10. Fission splits heavy nuclei. Fusion joins light nuclei and powers the Sun. Radioisotopes are used in medicine and smoke detectors. Radiation can harm tissue, so handle with care.

Organic chemistry is the chemistry of carbon. Carbon forms four bonds and makes chains and rings. Hydrocarbons contain carbon and hydrogen. Carbohydrates, lipids, proteins and nucleic acids are the molecules of life.

Chemistry serves through medicine, food, clean water and materials. It also calls for preventing pollution, safe disposal and truthful reporting.

Your task is to describe the three radiations, calculate a half life and explain stewardship. Take the four question check.""" + CLOSE,
 quiz=[
 ("A 40 gram sample of an isotope after 2 half lives has how many grams left?", ["10", "20", "5", "30"], 0, "40 halves to 20, then to 10."),
 ("The type of radiation that is a helium nucleus is:", ["Alpha", "Beta", "Gamma", "X ray"], 0, "Alpha particles have 2 protons and 2 neutrons."),
 ("The joining of light nuclei, as in the Sun, is called:", ["Fusion", "Fission", "Combustion", "Electrolysis"], 0, "Fusion combines nuclei."),
 ("Organic chemistry is the study of compounds of:", ["Carbon", "Sodium", "Helium", "Iron"], 0, "Carbon forms the backbone of organic compounds."),
 ]),
 ],
 assess=dict(t="Assessment 6: Acids and Bases, Redox, Nuclear and Organic Chemistry and Stewardship",
 prompt="""Write a report of at least 250 words on the final topics of chemistry. Use complete sentences and label each part. Psalm 24:1 says, The earth is the LORD'S, and the fulness thereof; the world, and they that dwell therein.

Part 1: Compare acids and bases and explain the pH scale. State the pH of a neutral solution and explain what a pH of 2 means compared to a pH of 4. Write a word equation for a neutralization reaction and explain a safety rule for household cleaners.
Part 2: Explain collision theory and four factors that change reaction rate. Explain what a catalyst does and what chemical equilibrium means. Apply Le Chatelier's principle to adding reactant.
Part 3: Define oxidation, reduction and OIL RIG. Explain rusting and how a battery produces current.
Part 4: Describe alpha, beta and gamma radiation. Calculate how much of an 80 gram sample remains after 3 half lives. Name one benefit and one risk of nuclear technology.
Part 5: Explain how Psalm 24:1 and Genesis 2:15 guide a chemist in the use of creation, and name a chemistry career you could serve in.""",
 rubric="""100 points. Part 1: 25 points. Part 2: 25 points. Part 3: 15 points. Part 4: 20 points. Part 5: 10 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 6: The Earth Is the LORD'S",
 prompt="""Write a post of at least 120 words that (1) describes one way chemistry has blessed your life, such as medicine, clean water, food or energy, (2) describes one responsibility chemists and citizens have to protect creation, such as safe disposal, recycling or preventing pollution, (3) explains how seeing the order in matter strengthens your faith or your respect for the Creator, and (4) connects your answer to Psalm 24:1, Genesis 2:15, Colossians 1:17 or Malachi 3:3. Then write a respectful reply of at least 40 words to another student's post, or answer this question: How should Christians think about using technologies that can be used for both good and harm? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("Acids turn blue litmus paper:", ["Red", "Green", "Yellow", "Black"], 0, "Acids turn blue litmus red."),
 ("A solution with pH 11 is:", ["Basic", "Acidic", "Neutral", "A metal"], 0, "Above 7 is basic."),
 ("Heating a reaction usually makes it:", ["Faster", "Slower", "Stop", "Reverse permanently"], 0, "Higher temperature increases collisions."),
 ("At equilibrium, the amounts of reactants and products:", ["Stay constant", "Increase forever", "Fall to zero", "Disappear"], 0, "Rates are equal, so amounts do not change."),
 ("Reduction is the:", ["Gain of electrons", "Loss of electrons", "Loss of protons", "Gain of protons"], 0, "RIG: Reduction Is Gain."),
 ("A battery converts:", ["Chemical energy to electrical energy", "Light to sound", "Heat to mass", "Electrical energy to nuclear energy"], 0, "Galvanic cells produce current from chemical change."),
 ("After 3 half lives, what fraction of a radioactive sample remains?", ["One eighth", "One half", "One third", "One sixth"], 0, "Half of half of half is one eighth."),
 ("Genesis 2:15 teaches humans to dress and keep the garden, which supports:", ["Stewardship of creation", "Wasting resources", "Ignoring pollution", "Avoiding science"], 0, "Keeping creation means caring for it."),
 ]
)
