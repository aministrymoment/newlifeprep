"""Earth and Space Science, Unit 4: Geologic Time, Fossils and Florida Geology. SC.912.E.6 cited at strand level; recheck at CPALMS."""
from ess_units1 import CLOSE

UNIT4 = dict(
 title="Unit 4: Geologic Time, Fossils and Florida Geology",
 std="SC.912.E.6",
 topics=[
 dict(t="4.1 Relative Dating and the Rock Record", std="SC.912.E.6",
 body="""Rock layers keep a record of the past. Ecclesiastes 3:1 says, To every thing there is a season, and a time to every purpose under the heaven. Geologists read the layers like pages of a book to learn in what order events happened. This is called relative dating, because it tells which rock or event is older or younger without giving an exact age.

Several simple rules guide relative dating. The law of superposition says that in undisturbed layers of sedimentary rock, the oldest layer is on the bottom and the youngest is on top. The principle of original horizontality says that sediment is deposited in flat, horizontal layers, so tilted or folded layers were moved later. The principle of cross cutting relationships says that a fault, a dike of igneous rock or any feature that cuts across rock layers is younger than the layers it cuts. Inclusions, which are pieces of one rock inside another, are older than the rock that contains them.

The rock record is not always complete. An unconformity is a gap in the record where layers were eroded away or never deposited. For example, rock might be lifted, eroded for a long time and then buried by new sediment. A geologist who finds an unconformity knows that time is missing from the record at that place.

Fossils also help with dating. An index fossil is the remains of an organism that lived in many places for a short span of geologic time and is easy to recognize. When the same index fossil is found in layers in two different places, scientists can match, or correlate, the layers even if they are far apart. Trilobites are index fossils for the early part of the Paleozoic Era, and ammonites are useful for the Mesozoic Era.

Using these rules, a student can order the events in a diagram. If layers A, B and C lie from bottom to top, then A is the oldest and C the youngest. If a fault cuts layers A and B but not C, the fault happened after A and B formed and before C was laid down.

Your task: (1) State the law of superposition. (2) Explain how a cross cutting relationship shows which feature is younger. (3) Describe what an index fossil and an unconformity tell us.""",
 script="""Welcome back. Listen, Ecclesiastes 3:1 says, To every thing there is a season, and a time to every purpose under the heaven. Rock layers keep a record of the past, and geologists read them like pages of a book.

Now watch this. Relative dating tells which rock is older without giving an exact age. The law of superposition says that in undisturbed layers, the oldest is on the bottom and the youngest is on top. Original horizontality says layers form flat, so tilted layers were moved later. Cross cutting says that a fault or dike that cuts across layers is younger than the layers. Inclusions are older than the rock around them.

Look at gaps. An unconformity is a gap in the record where layers eroded away or were never deposited. Time is missing at that place.

An index fossil lived in many places for a short span of time and is easy to recognize. If two faraway layers contain the same index fossil, we can match them. Trilobites are index fossils of the early Paleozoic.

Your task is to state superposition, explain cross cutting and describe index fossils and unconformities. Take the four question check.""" + CLOSE,
 quiz=[
 ("In undisturbed sedimentary layers, the oldest layer is usually:", ["On the bottom", "On the top", "In the middle", "The thickest one"], 0, "That is the law of superposition."),
 ("A fault that cuts across several rock layers is:", ["Younger than the layers it cuts", "Older than the layers it cuts", "The same age as all the layers", "Not related to the layers"], 0, "A feature that cuts across rock must come after the rock."),
 ("A gap in the rock record where layers are missing is called a(n):", ["Unconformity", "Index fossil", "Inclusion", "Fault block"], 0, "Erosion or no deposition leaves a gap."),
 ("An index fossil is useful because the organism lived:", ["Widely but only for a short span of time", "Only in one cave", "For all of Earth's history", "Only in the ocean"], 0, "That makes it a good marker for matching layers."),
 ]),
 dict(t="4.2 Absolute Dating and the Geologic Time Scale", std="SC.912.E.6",
 body="""Absolute dating gives an estimated age in years. Psalm 102:25 says, Of old hast thou laid the foundation of the earth: and the heavens are the work of thy hands. Believers agree that God is the Creator of the earth, and thoughtful Christians have held different views about how to read the days of Genesis 1 and about the age of the earth. This lesson explains how scientists measure ages and what results they report, so that you can understand the science and discuss it with your parents and pastor.

Absolute dating uses radioactive decay. Some atoms are unstable and change into other atoms at a steady, known rate. The original unstable atom is the parent isotope, and the atom it becomes is the daughter isotope. The half life is the time it takes for half of the parent atoms in a sample to decay. If a sample starts with 80 grams of a parent isotope, then after one half life 40 grams remain, after two half lives 20 grams remain, and after three half lives 10 grams remain.

Different isotopes have different half lives, so they suit different jobs. Carbon 14 has a half life of 5730 years and is used on once living material, such as wood, bone or cloth, up to about 50,000 years old. If a wooden tool has one eighth of its original carbon 14, then three half lives have passed, so it is about 3 times 5730, or 17,190 years old. Uranium 238 decays to lead 206 with a half life of about 4.5 billion years, so it is used for very old igneous rocks. Scientists use many checks, including several methods on the same rock, and the results of the oldest Earth rocks and meteorites give an estimated age for the Earth of about 4.54 billion years. Some Christians accept this estimate, and others hold that Earth is much younger. Both sides want to honor God and the Bible, and both are encouraged to study the evidence carefully and to speak with respect.

Geologists organize Earth history in the geologic time scale. The great span before about 541 million years ago is called the Precambrian. Then come the Paleozoic Era, from about 541 to 252 million years ago, with the rise of fish, land plants and amphibians. Next is the Mesozoic Era, from 252 to 66 million years ago, the age of dinosaurs. The Cenozoic Era, from 66 million years ago to today, includes mammals and the arrival of humans. Mass extinctions mark the boundaries of some eras.

Your task: (1) Define half life. (2) Solve a half life problem. (3) List the eras of the geologic time scale in order.""",
 script="""Welcome back. Listen, Psalm 102:25 says, Of old hast thou laid the foundation of the earth: and the heavens are the work of thy hands. Believers agree that God is the Creator. Thoughtful Christians differ on how to read the days of Genesis 1 and the age of the earth. In this lesson we learn how scientists measure ages, so you can understand the science and discuss it with your parents and pastor.

Now watch this. Some atoms are unstable and decay into other atoms at a steady rate. The half life is the time for half of the parent atoms to decay. Start with 80 grams. After one half life, 40 grams remain. After two, 20 grams. After three, 10 grams.

Carbon 14 has a half life of 5730 years and dates once living things up to about 50,000 years old. If a wooden tool has one eighth of its carbon 14, three half lives have passed, so it is about 17,190 years old. Uranium 238 has a half life of about 4.5 billion years and is used on very old rocks. Scientists estimate Earth's age at about 4.54 billion years. Some Christians accept this and others hold that Earth is younger. Both should study carefully and speak with respect.

The eras are Precambrian, Paleozoic, Mesozoic and Cenozoic.

Your task is to define half life, solve a problem and list the eras. Take the four question check.""" + CLOSE,
 quiz=[
 ("The half life of a radioactive isotope is the time for:", ["Half of the parent atoms to decay", "All of the atoms to decay", "The daughter atoms to double", "The sample to melt"], 0, "Half life is a fixed time for half to change."),
 ("A sample begins with 80 grams of a parent isotope. After two half lives, how much parent isotope remains?", ["20 grams", "40 grams", "10 grams", "0 grams"], 0, "80 halves to 40 and then to 20."),
 ("Carbon 14 dating is best used on:", ["Once living material less than about 50,000 years old", "Very old igneous rocks", "Minerals only", "Metals"], 0, "Carbon 14 decays too quickly for older samples."),
 ("The era known as the age of dinosaurs is the:", ["Mesozoic Era", "Paleozoic Era", "Cenozoic Era", "Precambrian"], 0, "The Mesozoic ran from about 252 to 66 million years ago."),
 ]),
 dict(t="4.3 Fossils and What They Tell Us", std="SC.912.E.6",
 body="""A fossil is the preserved remains or traces of a living thing from the past. Job 12:8 says, Or speak to the earth, and it shall teach thee: and the fishes of the sea shall declare unto thee. Fossils are one way the earth teaches us about creatures that once lived.

Most organisms never become fossils. The best chances come when an organism is buried quickly by sediment, has hard parts such as shells, bones or teeth, and lies where oxygen and scavengers are not present. There are several kinds of fossils. In permineralization, minerals carried by water fill the empty spaces in bone or wood and harden it into stone. Petrified wood is an example. A mold is an empty impression left in rock after a shell dissolves, and a cast forms when minerals fill the mold. A carbon film is a thin black outline left when the other elements in a leaf or fish escape. Amber is hardened tree resin that can trap insects whole. Some organisms are preserved by freezing or in tar. Trace fossils, such as footprints, burrows and nests, show how animals lived and moved.

Fossils help scientists reconstruct past environments. Fossil corals, shells and fish in rock far from the sea show that the place was once covered by a warm, shallow sea. Fossil ferns in a cold place suggest a warmer, wetter climate in the past. Fossils also help match layers of rock through index fossils, show how types of organisms have changed through geologic time, and mark mass extinctions.

Florida is rich in fossils. Visitors search for fossil shark teeth, including teeth of the huge extinct shark Megalodon, near Venice and along the Peace River. Florida also has fossils of mammoths, mastodons, giant ground sloths and saber toothed cats. Fossil collecting on public land may require a permit. Fossil hunters should always ask permission to enter private land.

Many believers also think about fossils in light of the flood in Genesis 6 to 9, and people hold different views about how the flood relates to the rock record. A good scientist looks at the evidence carefully, tests ideas honestly and shows humility. Proverbs 25:2 says, It is the glory of God to conceal a thing: but the honour of kings is to search out a matter.

Your task: (1) Describe three ways fossils form. (2) Explain why quick burial and hard parts matter. (3) Tell what a fossil can show about an ancient environment.""",
 script="""Welcome back. Listen, Job 12:8 says, Or speak to the earth, and it shall teach thee: and the fishes of the sea shall declare unto thee. Fossils are one way the earth teaches us about creatures that once lived.

Now watch this. A fossil is the preserved remains or traces of a living thing. Quick burial, hard parts like shells and bones, and a place with little oxygen give the best chance. In permineralization, minerals fill the spaces in bone or wood and make it stone. A mold is an impression and a cast is the mineral fill. A carbon film is a thin black outline. Amber is hardened resin that can trap insects. Trace fossils such as footprints show how animals moved.

Fossils show past environments. Fossil corals and shells in rock far from the sea show a warm, shallow sea once covered the place. Fossils also help match rock layers and show changes through time.

Florida is rich in fossils, such as Megalodon teeth near Venice and along the Peace River, and mammoths and mastodons. Always get permits and permission. Many believers also think about fossils in light of the flood of Genesis 6 to 9. Examine the evidence honestly with humility.

Your task is to describe how fossils form, why burial and hard parts matter, and what fossils show. Take the four question check.""" + CLOSE,
 quiz=[
 ("Fossils are most likely to form when an organism is:", ["Buried quickly and has hard parts", "Left on the surface in the open air", "Soft bodied and eaten", "Moved by wind for years"], 0, "Quick burial protects the remains."),
 ("A footprint preserved in rock is an example of a:", ["Trace fossil", "Cast", "Amber", "Index fossil"], 0, "Trace fossils show activity."),
 ("Hardened tree resin that traps insects is:", ["Amber", "Petrified wood", "A carbon film", "A mold"], 0, "Amber preserves small organisms in great detail."),
 ("Marine fossils found in rock on dry land show that the area was once:", ["Covered by a sea", "A desert", "A glacier", "A volcano"], 0, "Fossils reveal past environments."),
 ]),
 dict(t="4.4 Florida Geology: Limestone, Sinkholes and Sea Level", std="SC.912.E.6",
 body="""Florida has a geology all its own. Deuteronomy 8:7 says, For the LORD thy God bringeth thee into a good land, a land of brooks of water, of fountains and depths that spring out of valleys and hills. Florida has springs, lakes, beaches and rivers that depend on the rock under our feet.

Florida sits on the Florida Platform, a thick stack of limestone that built up over tens of millions of years in warm, shallow seas. The limestone is made mostly of shells, corals and the skeletons of small marine organisms. The rock is hundreds of meters thick. Above it lie sand, clay and shell deposited by the sea and by wind. Because the state has risen only slightly above the sea, Florida is very flat. The highest natural point, Britton Hill, is about 105 meters above sea level, and southeast Florida, including Pompano Beach, is only a few meters above sea level.

Limestone dissolves in slightly acidic water. Rainwater picks up carbon dioxide from the air and soil and becomes weakly acidic, so it slowly dissolves the limestone and opens cracks, caves and underground channels. A landscape shaped like this is called karst. When the roof of a cavity collapses, a sinkhole forms. Sinkholes often appear after a drought followed by heavy rain, or when too much groundwater is pumped. Many Florida lakes and springs began as sinkholes.

The Floridan aquifer system is one of the most productive aquifers in the world. It lies in the limestone below Florida and parts of Georgia, Alabama and South Carolina. It supplies drinking water for millions of people and feeds the state's springs. In southeast Florida the Biscayne aquifer, which lies closer to the surface, supplies water for Broward and Miami Dade counties. Pumping too much can pull in salt water from the ocean, which is called saltwater intrusion.

Sea level has changed many times. During the last ice age, so much water was locked in ice that sea level was about 120 meters lower than it is today, and Florida was about twice as wide as it is now. Since then sea level has risen. Today the sea is rising again, and low, flat Florida is especially exposed to flooding and beach erosion. Wise planning for roads, buildings and water supply, and protection of springs and aquifers, are part of faithful stewardship.

Your task: (1) Describe what Florida's bedrock is made of. (2) Explain how karst and a sinkhole form. (3) Explain why a low coastline is at special risk from rising seas.""",
 script="""Welcome back. Listen, Deuteronomy 8:7 says, For the LORD thy God bringeth thee into a good land, a land of brooks of water, of fountains and depths that spring out of valleys and hills. Florida has springs, lakes, beaches and rivers that depend on the rock under our feet.

Now watch this. Florida sits on the Florida Platform, a thick stack of limestone made of shells, corals and the skeletons of small sea creatures that built up in warm, shallow seas over tens of millions of years. The state is very flat. Britton Hill, the highest natural point, is about 105 meters. Pompano Beach is only a few meters above sea level.

Limestone dissolves in slightly acidic water. Rain with carbon dioxide slowly opens cracks and caves. That landscape is called karst. When a cave roof collapses, a sinkhole forms. Many Florida lakes and springs began as sinkholes.

The Floridan aquifer is one of the most productive in the world. In Broward County we rely on the Biscayne aquifer. Pumping too much can pull in salt water, called saltwater intrusion.

During the last ice age, sea level was about 120 meters lower, and Florida was twice as wide. Today the sea is rising again, and a low coast is exposed to flooding. Wise planning is part of stewardship.

Your task is to describe the bedrock, explain karst and sinkholes and explain the risk of rising seas. Take the four question check.""" + CLOSE,
 quiz=[
 ("Florida's bedrock is mostly:", ["Limestone", "Granite", "Basalt", "Slate"], 0, "It built up from marine shells and coral."),
 ("A landscape shaped by the dissolving of limestone, with caves and sinkholes, is called:", ["Karst", "Delta", "Moraine", "Rift"], 0, "Karst forms where rock dissolves."),
 ("When too much fresh groundwater is pumped near the coast, the aquifer may suffer:", ["Saltwater intrusion", "Deposition", "Folding", "Subduction"], 0, "Salt water moves into the empty spaces."),
 ("During the last ice age, sea level was lower because:", ["Much water was locked in ice sheets", "The Moon was closer", "The oceans were evaporating faster", "The land sank"], 0, "Ice sheets held a great deal of the world's water."),
 ]),
 ],
 assess=dict(t="Assessment 4: Geologic Time, Fossils and Florida Geology",
 prompt="""Write a report of at least 250 words on geologic time, fossils and the geology of Florida. Use complete sentences, show every calculation and label each part. Proverbs 25:2 says, It is the glory of God to conceal a thing: but the honour of kings is to search out a matter.

Part 1: Explain the law of superposition, original horizontality and cross cutting relationships. Describe an unconformity and an index fossil.
Part 2: Define half life. A sample starts with 160 grams of a parent isotope. Find how much remains after three half lives. A wooden bowl has one fourth of its original carbon 14, and the half life of carbon 14 is 5730 years. Find its age and show the work.
Part 3: List the eras of the geologic time scale in order, with one major change that marks each era, and explain in a respectful paragraph how thoughtful Christians can agree that God is Creator while differing on the age of the earth.
Part 4: Describe three ways fossils form, explain why most organisms do not become fossils, and tell what fossils can show about past environments.
Part 5: Describe Florida's bedrock, explain how a sinkhole forms, explain what the Floridan and Biscayne aquifers do, and tell why rising sea level is a special concern for a low coast like Pompano Beach.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 20 points. Part 3: 15 points. Part 4: 20 points. Part 5: 20 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 4: Reading the Record with Humility",
 prompt="""Write a post of at least 120 words that (1) describes a fossil, a rock layer or a landform in Florida or elsewhere that you have seen or would like to see, (2) explains in your own words one way scientists tell how old a rock or fossil is, (3) explains how a believer can study the rock record with both honesty and humility, honoring both God's Word and careful evidence, and (4) connects your answer to Proverbs 25:2, Psalm 102:25 or Job 12:8. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why is it important to speak with respect when believers differ about how to read Genesis? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("A tilted layer of sedimentary rock shows that it was:", ["Moved after it formed", "Formed by a volcano", "Formed upside down", "Never a sedimentary rock"], 0, "Sediment is deposited in flat layers, so tilting came later."),
 ("A dike of igneous rock cuts across three layers of sandstone. The dike is:", ["Younger than the sandstone layers", "Older than the sandstone layers", "The same age", "Not a rock"], 0, "The sandstone had to be there for the dike to cut it."),
 ("After three half lives, what fraction of the parent isotope remains?", ["One eighth", "One half", "One fourth", "One sixteenth"], 0, "Half of half of half is one eighth."),
 ("The Cenozoic Era is the one that:", ["Runs from about 66 million years ago to today", "Ended with the Paleozoic", "Began at the formation of Earth", "Was the age of fish only"], 0, "It includes the age of mammals."),
 ("Petrified wood forms by:", ["Permineralization", "Freezing", "Carbon film formation", "Cementation of sand"], 0, "Minerals fill spaces in the wood."),
 ("The main rock of the Florida Platform formed from:", ["Marine shells, corals and tiny sea organisms", "Volcanic lava", "Glacial till", "Desert sand dunes"], 0, "Warm shallow seas built thick limestone."),
 ("A sinkhole most often forms when:", ["The roof of a cavity in limestone collapses", "A glacier melts", "A volcano erupts", "The wind blows hard"], 0, "Groundwater dissolves limestone and leaves voids."),
 ("About 20,000 years ago, Florida's land area was larger because sea level was:", ["Much lower", "Much higher", "The same as today", "Unknown to scientists"], 0, "Ice sheets held water on land."),
 ],
)
