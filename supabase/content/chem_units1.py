"""Chemistry, Unit 1: Matter, Measurement and Safe Investigation. Florida science standards cited at strand level (SC.912.N and SC.912.P); recheck exact benchmark codes at CPALMS."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."

UNIT1 = dict(
 title="Unit 1: Matter, Measurement and Safe Investigation",
 std="SC.912.P, SC.912.N",
 topics=[
 dict(t="1.1 Matter and Its Properties", std="SC.912.P.8",
 body="""Chemistry is the study of matter, its properties, how it changes and the energy involved. Matter is anything that has mass and takes up space. Everything you can touch, taste or smell is matter, from a glass of water to the air in a balloon. Job 38:4 asks, Where wast thou when I laid the foundations of the earth? declare, if thou hast understanding. The more we learn about matter, the more we see the order God built into it.

Matter is described by its properties. A physical property can be observed or measured without changing what the substance is, such as color, density, melting point, boiling point and hardness. A chemical property describes how a substance can change into a different substance, such as flammability or the tendency to rust. In a physical change, such as ice melting or sugar dissolving, the identity of the substance stays the same. In a chemical change, such as wood burning or iron rusting, new substances form. Signs of a chemical change include a new color, a gas given off, a solid forming in a liquid, or a change in temperature or light.

Matter is classified. A pure substance has a fixed composition and is either an element or a compound. An element is made of one kind of atom and cannot be broken down by ordinary chemical means. A compound is made of two or more elements chemically combined in a fixed ratio, such as water. A mixture is two or more substances physically combined. A homogeneous mixture, or solution, is the same throughout, like salt water. A heterogeneous mixture has visibly different parts, like sand and water. Mixtures can be separated by physical means such as filtering, evaporating or distilling.

Your task: (1) Define matter. (2) Give one physical property and one chemical property of iron. (3) Classify salt water, table salt, oxygen and a salad as element, compound or mixture.""",
 script="""Welcome back. Listen, Job 38:4 asks, Where wast thou when I laid the foundations of the earth? declare, if thou hast understanding. The more we learn about matter, the more we see the order God built into it.

Now watch this. Chemistry is the study of matter, its properties and how it changes. Matter is anything that has mass and takes up space.

A physical property can be observed without changing the substance, like color, density, melting point and boiling point. A chemical property describes how a substance changes into something new, like flammability or rusting. In a physical change, the substance stays the same, like ice melting. In a chemical change, new substances form, like wood burning. Look for a new color, a gas, a solid forming or a change in temperature or light.

Matter is classified. An element is made of one kind of atom. A compound is two or more elements chemically combined in a fixed ratio. A mixture is physically combined. A solution is the same throughout. A heterogeneous mixture has visible parts.

Your task is to define matter, give a physical and a chemical property and classify four examples. Take the four question check.""" + CLOSE,
 quiz=[
 ("Anything that has mass and takes up space is:", ["Matter", "Energy", "A solution only", "A compound only"], 0, "That is the definition of matter."),
 ("Which is a chemical change?", ["Wood burning", "Ice melting", "Sugar dissolving in water", "Cutting paper"], 0, "Burning forms new substances."),
 ("A substance made of two or more elements chemically combined in a fixed ratio is a:", ["Compound", "Element", "Heterogeneous mixture", "Solution of one atom"], 0, "Compounds have a fixed composition."),
 ("Salt water is an example of a:", ["Homogeneous mixture", "Pure element", "Compound", "Heterogeneous mixture"], 0, "Salt water is the same throughout."),
 ]),
 dict(t="1.2 Measurement, SI Units and Significant Figures", std="SC.912.N.1",
 body="""Science depends on careful measurement. Proverbs 11:1 says, A false balance is abomination to the LORD: but a just weight is his delight. Honest, accurate measurement matters in the lab and in business, medicine and daily life.

Scientists use the International System of Units, called SI. The base unit of length is the meter, of mass the kilogram, of time the second, of temperature the kelvin, and of amount of substance the mole. Volume is often measured in liters. Prefixes make units larger or smaller: kilo means one thousand, centi means one hundredth and milli means one thousandth. So one kilometer is 1000 meters and one meter is 100 centimeters or 1000 millimeters. Celsius and kelvin are related by adding 273 to the Celsius temperature to get kelvin, so water freezes at 0 degrees Celsius or 273 kelvin.

No measurement is perfect. Accuracy tells how close a measurement is to the true value. Precision tells how close repeated measurements are to each other. A scale that always reads 2 grams too high is precise but not accurate.

Significant figures show how reliable a measurement is. They include all the digits you are sure of plus one estimated digit. Rules: nonzero digits are always significant; zeros between nonzero digits are significant; leading zeros are not significant; trailing zeros are significant when there is a decimal point. When multiplying or dividing, the answer has as many significant figures as the measurement with the fewest. When adding or subtracting, the answer has as many decimal places as the measurement with the fewest. Scientific notation, such as 3.2 times 10 to the 4th, writes very large or small numbers neatly.

Your task: (1) Convert 2.5 kilometers to meters. (2) Explain the difference between accuracy and precision. (3) State how many significant figures are in 0.0450.""",
 script="""Welcome back. Listen, Proverbs 11:1 says, A false balance is abomination to the LORD: but a just weight is his delight. Honest, accurate measurement matters in the lab and in life.

Now watch this. Scientists use SI units. Meter for length, kilogram for mass, second for time, kelvin for temperature and mole for amount of substance. Prefixes change size. Kilo is one thousand. Centi is one hundredth. Milli is one thousandth. Kelvin equals Celsius plus 273.

Accuracy is how close to the true value. Precision is how close repeated measurements are to each other.

Significant figures show how reliable a measurement is. Nonzero digits count. Zeros between nonzero digits count. Leading zeros do not. Trailing zeros count when there is a decimal point. When multiplying or dividing, keep the fewest significant figures. When adding or subtracting, keep the fewest decimal places.

Your task is to convert 2.5 kilometers to meters, explain accuracy and precision and count the significant figures in 0.0450. Take the four question check.""" + CLOSE,
 quiz=[
 ("The SI base unit of mass is the:", ["Kilogram", "Gram only", "Liter", "Newton"], 0, "The kilogram is the SI base unit of mass."),
 ("How many meters are in 2.5 kilometers?", ["2500", "250", "25", "0.25"], 0, "Multiply by 1000."),
 ("Measurements that are close to each other but far from the true value are:", ["Precise but not accurate", "Accurate but not precise", "Both accurate and precise", "Neither precise nor accurate"], 0, "Precision is about agreement among measurements."),
 ("How many significant figures are in 0.0450?", ["3", "2", "4", "5"], 0, "The 4, 5 and trailing 0 count; leading zeros do not."),
 ]),
 dict(t="1.3 Lab Safety and the Scientific Investigation", std="SC.912.N.1",
 body="""Science is the careful search for knowledge about the natural world. Proverbs 25:2 says, It is the glory of God to conceal a thing: but the honour of kings is to search out a matter. Investigation is a good and godly activity, and it must be done with care. Proverbs 14:15 says, The simple believeth every word: but the prudent man looketh well to his going.

A scientific investigation often follows these steps: ask a question, do background research, form a testable hypothesis, design an experiment, collect data, analyze the results, draw a conclusion and share the findings. A hypothesis is a testable prediction. In a good experiment you change one variable at a time. The independent variable is the one you change, the dependent variable is the one you measure, and the controlled variables are kept the same. A control group is used for comparison. Repeating trials makes results more reliable. Data are recorded honestly, even when they do not support your hypothesis. A scientific theory is a well supported explanation based on a large body of evidence, and a scientific law describes a pattern in nature.

Safety comes first. Proverbs 22:3 says, A prudent man foreseeth the evil, and hideth himself. In a lab, always follow your instructor's directions, read the whole procedure first, wear safety goggles and protective clothing, tie back long hair, never taste or directly sniff chemicals, never mix chemicals unless directed, know where the eyewash, safety shower, fire extinguisher and exits are, and report spills and accidents at once. Read labels and safety data sheets. Dispose of chemicals only as directed.

In this course, any hands on activity at home must use only safe household materials and have adult permission and supervision. Never experiment with unknown chemicals, fire, strong cleaners or anything that could harm you or others.

Your task: (1) Name the independent and dependent variables in an experiment on how temperature affects how fast sugar dissolves. (2) List five lab safety rules. (3) Explain the difference between a theory and a hypothesis.""",
 script="""Welcome back. Listen, Proverbs 25:2 says, It is the glory of God to conceal a thing: but the honour of kings is to search out a matter. Investigation is a good and godly activity, and it must be done with care.

Now watch this. Ask a question, do research, form a testable hypothesis, design an experiment, collect data, analyze the results, draw a conclusion and share the findings. Change one variable at a time. The independent variable is the one you change. The dependent variable is the one you measure. Controlled variables stay the same. Repeat trials. Record data honestly, even when it does not support your hypothesis.

Now safety. Proverbs 22:3 says, A prudent man foreseeth the evil, and hideth himself. Follow directions, read the whole procedure first, wear goggles, tie back long hair, never taste chemicals, never mix unless directed, know where the exits and eyewash are, and report spills.

At home, use only safe household materials with adult permission and supervision.

Your task is to name the variables, list five safety rules and explain theory and hypothesis. Take the four question check.""" + CLOSE,
 quiz=[
 ("The variable you change on purpose in an experiment is the:", ["Independent variable", "Dependent variable", "Controlled variable", "Constant result"], 0, "You change the independent variable."),
 ("A testable prediction is a:", ["Hypothesis", "Law only", "Conclusion", "Control"], 0, "A hypothesis must be testable."),
 ("Before starting a lab you should:", ["Read the whole procedure", "Taste the chemicals", "Skip the goggles", "Mix to see what happens"], 0, "Reading first prevents mistakes and accidents."),
 ("Data that do not support your hypothesis should be:", ["Recorded honestly", "Changed to match", "Thrown away", "Hidden"], 0, "Honesty is essential in science."),
 ]),
 dict(t="1.4 Dimensional Analysis and Density", std="SC.912.P.8",
 body="""Chemistry uses math as a tool. Dimensional analysis, also called the factor label method, is a way to convert from one unit to another by multiplying by conversion factors. A conversion factor is a fraction equal to one, such as 1000 meters over 1 kilometer. Set up the problem so that the unit you do not want cancels and the unit you want remains. For example, to change 3.5 hours to seconds, multiply by 60 minutes over 1 hour and then by 60 seconds over 1 minute. The hours cancel, the minutes cancel, and you get 12,600 seconds. Always write the units and check that your answer is reasonable. Proverbs 16:11 says, A just weight and balance are the LORD'S: all the weights of the bag are his work.

Density is the mass of a substance in a given volume. The formula is density equals mass divided by volume. Density is a physical property that can help identify a substance. Typical units are grams per cubic centimeter or grams per milliliter. Water has a density of about 1.00 gram per milliliter. Substances less dense than water float on it, and substances more dense than water sink. If a block has a mass of 54 grams and a volume of 20 cubic centimeters, its density is 54 divided by 20, which is 2.7 grams per cubic centimeter.

You can rearrange the formula. Mass equals density times volume, and volume equals mass divided by density. The volume of an irregular solid can be found by water displacement: place it in a graduated cylinder and subtract the starting volume from the final volume. Give answers with the correct units and significant figures.

Your task: (1) Convert 72 kilometers per hour to meters per second using conversion factors. (2) Calculate the density of an object with a mass of 36 grams and a volume of 12 cubic centimeters. (3) Explain why oil floats on water.""",
 script="""Welcome back. Listen, Proverbs 16:11 says, A just weight and balance are the LORD'S: all the weights of the bag are his work. Careful calculations honor careful work.

Now watch this. Dimensional analysis converts units by multiplying by conversion factors. A conversion factor is a fraction equal to one, like 1000 meters over 1 kilometer. Set it up so unwanted units cancel. To change 3.5 hours to seconds, multiply by 60 minutes over 1 hour, then 60 seconds over 1 minute. The answer is 12,600 seconds. Always write your units.

Density is mass divided by volume. It is a physical property that helps identify a substance. Water is about 1.00 gram per milliliter. Less dense floats. More dense sinks. A 54 gram block with a volume of 20 cubic centimeters has a density of 2.7 grams per cubic centimeter. You can find the volume of an irregular solid by water displacement.

Your task is to convert 72 kilometers per hour to meters per second, calculate a density and explain why oil floats. Take the four question check.""" + CLOSE,
 quiz=[
 ("A conversion factor is a fraction that equals:", ["One", "Zero", "Ten", "The density"], 0, "Multiplying by one changes units, not value."),
 ("Density equals:", ["Mass divided by volume", "Volume divided by mass", "Mass times volume", "Mass plus volume"], 0, "Density is mass per unit volume."),
 ("A 36 gram object with a volume of 12 cubic centimeters has a density of:", ["3 grams per cubic centimeter", "24 grams per cubic centimeter", "0.33 grams per cubic centimeter", "432 grams per cubic centimeter"], 0, "36 divided by 12 equals 3."),
 ("An object with density greater than water will:", ["Sink", "Float", "Evaporate", "Dissolve"], 0, "More dense objects sink in water."),
 ]),
 ],
 assess=dict(t="Assessment 1: Matter, Measurement and Safe Investigation",
 prompt="""Write a report of at least 250 words on the foundations of chemistry. Use complete sentences and label each part. Proverbs 25:2 says, It is the glory of God to conceal a thing: but the honour of kings is to search out a matter.

Part 1: Define matter, element, compound and mixture, and give an example of each. Explain the difference between a physical change and a chemical change with two examples of each.
Part 2: Name the SI base units for length, mass, time, temperature and amount of substance. Explain accuracy and precision, and state the rules for counting significant figures.
Part 3: Outline a safe investigation of your choice using household materials, naming the question, hypothesis, independent variable, dependent variable and controlled variables. List five safety rules.
Part 4: Solve and show the work: convert 4.2 liters to milliliters, and find the density of an object with a mass of 45 grams and a volume of 15 cubic centimeters.
Part 5: Explain how Proverbs 11:1 and Proverbs 22:3 apply to honest measurement and lab safety.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 20 points. Part 3: 25 points. Part 4: 20 points. Part 5: 10 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 1: It Is the Glory of God to Search Out a Matter",
 prompt="""Write a post of at least 120 words that (1) describes something in everyday life that you have measured or could measure, and why accuracy matters for it, (2) explains why honesty in recording data is important even when the result is not what you expected, (3) explains one safety habit you will practice in any lab or kitchen, and (4) connects your answer to Proverbs 25:2, Proverbs 11:1 or Proverbs 22:3. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Can a person of faith be a good scientist? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("Which is a chemical property?", ["Flammability", "Color", "Melting point", "Density"], 0, "Flammability describes how a substance reacts."),
 ("A mixture that is uniform throughout is called:", ["Homogeneous", "Heterogeneous", "An element", "A compound"], 0, "Solutions are homogeneous mixtures."),
 ("The prefix milli means:", ["One thousandth", "One thousand", "One hundredth", "One hundred"], 0, "Milli is one thousandth."),
 ("How many kelvin is 25 degrees Celsius?", ["298", "248", "25", "Negative 25"], 0, "Add 273 to the Celsius temperature."),
 ("In 3.040, how many significant figures are there?", ["4", "3", "2", "5"], 0, "All four digits count because of the decimal point."),
 ("The variable that is measured as the result of an experiment is the:", ["Dependent variable", "Independent variable", "Hypothesis", "Control"], 0, "The dependent variable depends on the change you make."),
 ("Which is a safe lab habit?", ["Wearing safety goggles", "Tasting a chemical", "Running in the lab", "Mixing unknown chemicals"], 0, "Goggles protect the eyes."),
 ("An object has a mass of 90 grams and a volume of 30 cubic centimeters. Its density is:", ["3 grams per cubic centimeter", "0.33 grams per cubic centimeter", "2700 grams per cubic centimeter", "60 grams per cubic centimeter"], 0, "90 divided by 30 equals 3."),
 ]
)
