"""Physical Science, Unit 1: Science, Measurement and Matter. Florida NGSSS Nature of Science (SC.912.N) and Physical Science (SC.912.P) cited at strand level; recheck exact benchmark codes at CPALMS."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."

UNIT1 = dict(
 title="Unit 1: Science, Measurement and Matter",
 std="SC.912.N.1",
 topics=[
 dict(t="1.1 The Nature of Science and Lab Safety", std="SC.912.N.1",
 body="""Science is the careful study of the natural world through observation, measurement and testing. Psalm 111:2 says, The works of the LORD are great, sought out of all them that have pleasure therein. God made an orderly creation, and that order is why careful study works. Genesis 1:1 says, In the beginning God created the heaven and the earth. Scientists ask how things work, and believers can do this work with joy and humility.

Scientific work often follows steps like these. Make an observation and ask a question. Form a hypothesis, which is a testable explanation. Design an experiment that changes one factor at a time. The factor you change on purpose is the independent variable. The factor you measure is the dependent variable. The conditions you keep the same are the controls. A control group is the group that does not get the treatment, so that you have something to compare. Collect data, analyze it, draw a conclusion and share the results so that others can repeat the test.

A scientific law describes what happens in nature, often with an equation. A scientific theory is a well tested explanation of why it happens and is supported by a large body of evidence. A theory does not turn into a law. They do different jobs.

Safety is part of good science. Proverbs 22:3 says, A prudent man foreseeth the evil, and hideth himself: but the simple pass on, and are punished. Wear goggles and follow your teacher's directions. Never taste or smell unknown chemicals. Tie back long hair, keep your work area clean and know where the eyewash, fire extinguisher and exits are. Tell an adult about every spill or injury right away. First Thessalonians 5:21 says, Prove all things; hold fast that which is good.

Your task: (1) List the steps of a fair experiment. (2) Name the independent variable, dependent variable and controls in an example. (3) State three lab safety rules.""",
 script="""Welcome back. Listen, Psalm 111:2 says, The works of the LORD are great, sought out of all them that have pleasure therein. God made an orderly creation, and that order is why careful study works.

Now watch this. A fair experiment starts with an observation and a question. Then we form a hypothesis, a testable explanation. We change one factor on purpose, the independent variable. We measure the result, the dependent variable. And we keep everything else the same, the controls. A control group gives us something to compare.

Look at the difference between a law and a theory. A law describes what happens, often with an equation. A theory is a well tested explanation of why it happens. A theory does not turn into a law. They do different jobs.

Safety is part of good science. Proverbs 22:3 says, A prudent man foreseeth the evil, and hideth himself. Wear goggles, follow directions, never taste unknown chemicals and report every spill. First Thessalonians 5:21 says, Prove all things; hold fast that which is good.

Your task is to list the steps of a fair experiment, name the variables and state three safety rules. Take the four question check.""" + CLOSE,
 quiz=[
 ("A testable explanation that can be supported or rejected by evidence is a:", ["Hypothesis", "Measurement", "Unit", "Hazard"], 0, "A hypothesis is a testable explanation."),
 ("The factor that a scientist deliberately changes in an experiment is the:", ["Independent variable", "Dependent variable", "Control group", "Conclusion"], 0, "The independent variable is the one you change."),
 ("Which is a safe lab practice?", ["Wear goggles and follow directions", "Taste chemicals to identify them", "Run in the lab", "Mix unknown chemicals"], 0, "Goggles and following directions prevent injuries."),
 ("A scientific law:", ["Describes what happens in nature, often with an equation", "Is an unproven guess", "Is what a theory becomes after enough proof", "Is never tested"], 0, "Laws describe patterns. Theories explain why."),
 ]),
 dict(t="1.2 Measurement, SI Units and Scientific Notation", std="SC.912.N.1",
 body="""Science depends on measurement. Proverbs 11:1 says, A false balance is abomination to the LORD: but a just weight is his delight. Honest, careful measuring is part of integrity.

Scientists around the world use the International System of Units, called SI. The base unit of length is the meter, of mass the kilogram, of time the second, and of temperature the kelvin. Volume is often measured in liters. Prefixes change the size of a unit by powers of ten. Kilo means 1000, centi means one hundredth, and milli means one thousandth. So 2.5 kilometers equals 2500 meters, and 350 milliliters equals 0.35 liters. To convert, multiply or divide by the right power of ten, and always write the unit.

Very large and very small numbers are written in scientific notation, a number from 1 up to 10 multiplied by a power of ten. The number 4,500,000 is 4.5 times 10 to the 6th. The number 0.00032 is 3.2 times 10 to the negative 4. The speed of light is about 3.0 times 10 to the 8th meters per second.

Good measurements are accurate and precise. A measurement is accurate if it is close to the true value. It is precise if repeated measurements agree with each other. A scale that always reads 2 grams too high is precise but not accurate. Read an instrument at eye level, include one estimated digit past the smallest mark, and repeat measurements to find an average.

Your task: (1) Convert between metric units. (2) Write a number in scientific notation. (3) Explain the difference between accuracy and precision.""",
 script="""Welcome back. Listen, Proverbs 11:1 says, A false balance is abomination to the LORD: but a just weight is his delight. Honest, careful measuring is part of integrity.

Now watch this. Scientists use the International System of Units, called SI. Length is in meters, mass in kilograms, time in seconds and temperature in kelvins. Prefixes change the size by powers of ten. Kilo is 1000, centi is one hundredth and milli is one thousandth. So 2.5 kilometers is 2500 meters, and 350 milliliters is 0.35 liters.

Look at scientific notation. It is a number from 1 up to 10 times a power of ten. 4,500,000 is 4.5 times 10 to the 6th. 0.00032 is 3.2 times 10 to the negative 4. The speed of light is about 3.0 times 10 to the 8th meters per second.

Accurate means close to the true value. Precise means repeated measurements agree. A scale that always reads 2 grams too high is precise but not accurate. Read at eye level and repeat your measurements.

Your task is to convert units, write scientific notation and explain accuracy and precision. Take the four question check.""" + CLOSE,
 quiz=[
 ("The SI base unit of length is the:", ["Meter", "Liter", "Gram", "Kelvin"], 0, "The meter is the SI unit of length."),
 ("2.5 kilometers equals:", ["2500 meters", "250 meters", "25 meters", "25000 meters"], 0, "Kilo means 1000, so 2.5 times 1000 equals 2500."),
 ("4,500,000 written in scientific notation is:", ["4.5 times 10 to the 6th", "4.5 times 10 to the 5th", "0.45 times 10 to the 6th", "45 times 10 to the 6th"], 0, "Move the decimal 6 places to get 4.5."),
 ("A measurement that is close to the true value is:", ["Accurate", "Hypothetical", "Variable", "Convertible"], 0, "Accuracy means closeness to the true value."),
 ]),
 dict(t="1.3 Properties of Matter and Density", std="SC.912.P.8",
 body="""Matter is anything that has mass and takes up space. Isaiah 40:12 asks, Who hath measured the waters in the hollow of his hand, and meted out heaven with the span, and comprehended the dust of the earth in a measure, and weighed the mountains in scales, and the hills in a balance? God knows the measure of all matter. We learn to measure it a little at a time.

Mass is the amount of matter in an object, measured in kilograms or grams. Weight is the pull of gravity on that mass and is measured in newtons. Your mass stays the same on the Moon, but your weight is smaller. Volume is the space an object takes up. For a box, volume equals length times width times height. For an irregular solid, measure how much water it displaces.

Physical properties can be observed without changing what the substance is. Examples are color, hardness, melting point, boiling point, conductivity and density. Chemical properties describe how a substance can change into a new substance, such as flammability or the ability to rust.

Density equals mass divided by volume. A block of aluminum has a mass of 54 grams and a volume of 20 cubic centimeters. Its density is 54 divided by 20, which is 2.7 grams per cubic centimeter. Pure water has a density of about 1.0 gram per cubic centimeter. An object floats in a liquid if it is less dense than the liquid and sinks if it is more dense. Ice has a density of about 0.92 grams per cubic centimeter, so ice floats on water. This unusual property helps lakes freeze from the top down and protects the life beneath.

Your task: (1) Tell the difference between mass and weight. (2) Calculate a density. (3) Predict whether an object floats or sinks in water.""",
 script="""Welcome back. Listen, Isaiah 40:12 asks, Who hath measured the waters in the hollow of his hand? God knows the measure of all matter, and we learn to measure it a little at a time.

Now watch this. Matter is anything that has mass and takes up space. Mass is the amount of matter, measured in kilograms. Weight is the pull of gravity on that mass, measured in newtons. Your mass is the same on the Moon, but your weight is smaller. Volume is the space an object takes up.

Look at properties. Physical properties can be observed without changing the substance, such as color, hardness, melting point and density. Chemical properties describe how a substance can change into something new, such as flammability.

Density is mass divided by volume. A block of aluminum has a mass of 54 grams and a volume of 20 cubic centimeters, so its density is 2.7 grams per cubic centimeter. Water is about 1.0. An object floats if it is less dense than the liquid and sinks if it is more dense. Ice is about 0.92, so ice floats. That helps a lake freeze from the top down and protects the life beneath.

Your task is to tell mass from weight, calculate a density and predict floating or sinking. Take the four question check.""" + CLOSE,
 quiz=[
 ("Density equals:", ["Mass divided by volume", "Volume divided by mass", "Mass times volume", "Weight plus volume"], 0, "Density is mass per unit volume."),
 ("A block has a mass of 54 g and a volume of 20 cubic centimeters. Its density is:", ["2.7 g per cubic centimeter", "1.1 g per cubic centimeter", "74 g per cubic centimeter", "34 g per cubic centimeter"], 0, "54 divided by 20 equals 2.7."),
 ("Ice floats on liquid water because ice is:", ["Less dense than liquid water", "More dense than liquid water", "Made of a different substance", "Always lighter in mass"], 0, "Lower density means it floats."),
 ("Which is a physical property?", ["Melting point", "Flammability", "Ability to rust", "Reactivity with acid"], 0, "Melting point can be observed without forming a new substance."),
 ]),
 dict(t="1.4 States of Matter and Changes of State", std="SC.912.P.8",
 body="""Matter exists in several states. Psalm 147:18 says, He sendeth out his word, and melteth them: he causeth his wind to blow, and the waters flow. The Lord is Lord over ice, water and vapor alike.

The particle model explains the states. In a solid, particles are packed closely and vibrate in fixed positions, so a solid has a definite shape and volume. In a liquid, particles are close but slide past each other, so a liquid has a definite volume but takes the shape of its container. In a gas, particles are far apart and move freely, so a gas has no definite shape or volume. Plasma is a fourth state, a hot gas of charged particles found in lightning and in stars.

A change of state is a physical change, because the substance is still the same. Melting is solid to liquid. Freezing is liquid to solid. Vaporization is liquid to gas and includes boiling and evaporation. Condensation is gas to liquid. Sublimation is solid directly to gas, as when dry ice fades. Deposition is gas directly to solid, as when frost forms. At sea level, water freezes at 0 degrees Celsius and boils at 100 degrees Celsius. Temperature conversions are kelvins equal degrees Celsius plus 273, so 100 degrees Celsius is 373 kelvins. Energy must be added for melting and vaporization, and energy is released for freezing and condensation.

A chemical change forms new substances. Signs include a new color, bubbles of gas, a solid forming in a liquid, light or heat, and an odor. Burning wood and rusting iron are chemical changes. In every change, mass is conserved. The total mass before equals the total mass after.

Your task: (1) Describe the particles in a solid, liquid and gas. (2) Name each change of state. (3) Tell a physical change from a chemical change.""",
 script="""Welcome back. Listen, Psalm 147:18 says, He sendeth out his word, and melteth them: he causeth his wind to blow, and the waters flow. The Lord is Lord over ice, water and vapor alike.

Now watch this. In a solid, particles are packed close and vibrate in place, so a solid keeps its shape and volume. In a liquid, particles slide past each other, so a liquid keeps its volume but takes the shape of its container. In a gas, particles are far apart and move freely. Plasma is a hot gas of charged particles, found in lightning and in stars.

Look at the changes of state. Melting is solid to liquid. Freezing is liquid to solid. Vaporization is liquid to gas. Condensation is gas to liquid. Sublimation is solid straight to gas. Deposition is gas straight to solid. At sea level, water freezes at 0 degrees Celsius and boils at 100. These are physical changes because the substance stays the same.

A chemical change makes new substances. Look for a new color, bubbles, a solid forming, light, heat or an odor. Burning wood is chemical. Mass is conserved in every change.

Your task is to describe the particles in each state, name the changes of state and tell physical from chemical changes. Take the four question check.""" + CLOSE,
 quiz=[
 ("The change from liquid to gas is called:", ["Vaporization", "Condensation", "Sublimation", "Freezing"], 0, "Liquid to gas is vaporization."),
 ("A solid changing directly into a gas is:", ["Sublimation", "Deposition", "Melting", "Condensation"], 0, "Sublimation skips the liquid state."),
 ("The particles in a gas:", ["Move freely and are far apart", "Are packed in fixed positions", "Slide past each other while touching", "Do not move"], 0, "Gas particles are far apart and move freely."),
 ("Which is a chemical change?", ["Burning wood", "Melting ice", "Cutting paper", "Boiling water"], 0, "Burning forms new substances."),
 ]),
 ],
 assess=dict(t="Assessment 1: Science, Measurement and Matter",
 prompt="""Write a report of at least 250 words on science, measurement and matter. Use complete sentences, show every calculation and label each part. Psalm 111:2 says, The works of the LORD are great, sought out of all them that have pleasure therein.

Part 1: Design a fair experiment to test which brand of paper towel absorbs the most water. Name the question, the hypothesis, the independent variable, the dependent variable and at least three controls.
Part 2: Convert 4.2 kilometers to meters and 750 milliliters to liters. Write 6,200,000 and 0.00045 in scientific notation.
Part 3: A metal sample has a mass of 90 grams and a volume of 30 cubic centimeters. Find its density and tell whether it floats or sinks in water, which has a density of 1.0 gram per cubic centimeter.
Part 4: Describe the particles and the shape and volume of a solid, a liquid and a gas, and name the change of state when each of these happens: ice becomes water, steam becomes water, dry ice becomes gas.
Part 5: Explain the difference between a physical change and a chemical change with two examples of each, and explain why Proverbs 22:3 applies to lab safety.""",
 rubric="""100 points. Part 1: 25 points. Part 2: 20 points. Part 3: 20 points. Part 4: 15 points. Part 5: 15 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 1: Wonder and Order",
 prompt="""Write a post of at least 120 words that (1) describes something in nature that made you stop and wonder, (2) explains why an orderly creation makes careful measurement and testing possible, (3) explains how honest measuring shows integrity, and (4) connects your answer to Psalm 111:2, Genesis 1:1 or Proverbs 11:1. Then write a respectful reply of at least 40 words to another student's post, or answer this question: How can a believer study science with both curiosity and humility? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("A fair test changes how many variables at a time?", ["One", "Three", "All of them", "None"], 0, "Change one variable and keep the rest the same."),
 ("The SI base unit of mass is the:", ["Kilogram", "Newton", "Liter", "Pound"], 0, "The kilogram is the SI unit of mass."),
 ("3.2 times 10 to the 3rd equals:", ["3200", "320", "32000", "0.0032"], 0, "Multiplying by 1000 gives 3200."),
 ("350 milliliters equals how many liters?", ["0.35", "3.5", "35", "350"], 0, "Milli means one thousandth."),
 ("A sample has a mass of 120 g and a volume of 40 cubic centimeters. Its density is:", ["3 g per cubic centimeter", "0.3 g per cubic centimeter", "80 g per cubic centimeter", "160 g per cubic centimeter"], 0, "120 divided by 40 equals 3."),
 ("At sea level, water freezes at:", ["0 degrees Celsius", "100 degrees Celsius", "32 degrees Celsius", "273 degrees Celsius"], 0, "Pure water freezes at 0 degrees Celsius."),
 ("A change that forms new substances is:", ["A chemical change", "A physical change", "A change of state", "A change of size"], 0, "New substances mean a chemical change."),
 ("Which state of matter has a definite volume but no definite shape?", ["Liquid", "Solid", "Gas", "Plasma"], 0, "A liquid takes the shape of its container."),
 ],
)
