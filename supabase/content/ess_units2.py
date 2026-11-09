"""Earth and Space Science, Unit 2: Earth's Interior and Plate Tectonics. SC.912.E.6 cited at strand level; recheck at CPALMS."""
from ess_units1 import CLOSE

UNIT2 = dict(
 title="Unit 2: Earth's Interior and Plate Tectonics",
 std="SC.912.E.6",
 topics=[
 dict(t="2.1 Earth's Layers", std="SC.912.E.6",
 body="""No one has ever traveled to the center of the Earth, yet scientists know a great deal about what lies inside. Proverbs 8:29 speaks of the Lord when he appointed the foundations of the earth. The deepest hole ever drilled reaches only about 12 kilometers, while the center of Earth is about 6371 kilometers down, so scientists learn about the interior from indirect evidence.

The best evidence comes from seismic waves, the waves of energy that travel through Earth during an earthquake. P waves are compressional waves that can travel through solids and liquids. S waves are side to side waves that can travel only through solids. Waves speed up, slow down, bend and stop as they pass through different materials. Because S waves do not pass through the outer core, scientists concluded that the outer core is liquid.

Earth has layers of different composition. The crust is the thin, rocky outer layer. Oceanic crust is about 5 to 10 kilometers thick and made of dense basalt. Continental crust averages about 35 kilometers thick, reaches 70 kilometers under big mountains, and is made mostly of lighter granite. The mantle lies below the crust. It is about 2900 kilometers thick, makes up most of Earth's volume, and is hot, dense rock that flows very slowly. The outer core is liquid iron and nickel and reaches to a depth of about 5150 kilometers. The inner core is solid iron and nickel, with a radius of about 1220 kilometers. It stays solid because of the great pressure, even though it is extremely hot, about 5000 degrees Celsius or more.

Scientists also divide Earth by how the rock behaves. The lithosphere is the rigid outer shell made of the crust and the uppermost mantle. It is broken into pieces called plates. Beneath it, the asthenosphere is a hotter, softer layer of the mantle that can flow slowly, and the lithosphere floats on it. Temperature and pressure both increase with depth. Earth's moving liquid outer core also produces the magnetic field, which protects us from charged particles from the Sun.

Your task: (1) Name Earth's layers in order from the surface. (2) Explain how seismic waves show that the outer core is liquid. (3) Tell the difference between the lithosphere and the asthenosphere.""",
 script="""Welcome back. Listen, Proverbs 8:29 speaks of the Lord when he appointed the foundations of the earth. No one has traveled to Earth's center, so how do we know what is inside?

Now watch this. Scientists use seismic waves from earthquakes. P waves travel through solids and liquids. S waves travel only through solids. S waves do not pass through the outer core, so the outer core must be liquid.

Look at the layers. The crust is the thin outer layer. Oceanic crust is dense basalt, about 5 to 10 kilometers thick. Continental crust is lighter granite and averages about 35 kilometers. The mantle is about 2900 kilometers thick, hot rock that flows very slowly. The outer core is liquid iron and nickel. The inner core is solid iron and nickel, held solid by great pressure.

We also divide Earth by behavior. The lithosphere is the rigid outer shell, broken into plates. It floats on the asthenosphere, a soft, flowing part of the mantle. The moving liquid outer core makes Earth's magnetic field.

Your task is to name the layers, explain the evidence for a liquid outer core and tell the lithosphere from the asthenosphere. Take the four question check.""" + CLOSE,
 quiz=[
 ("Which layer of Earth is liquid?", ["Outer core", "Inner core", "Crust", "Lithosphere"], 0, "S waves stop at the outer core, so it is liquid."),
 ("What type of wave cannot travel through a liquid?", ["S wave", "P wave", "Both P and S waves", "Neither type"], 0, "S waves move only through solids."),
 ("The thickest of Earth's layers by volume is the:", ["Mantle", "Crust", "Outer core", "Inner core"], 0, "The mantle is about 2900 kilometers thick."),
 ("The rigid outer shell of Earth, made of the crust and uppermost mantle, is the:", ["Lithosphere", "Asthenosphere", "Outer core", "Atmosphere"], 0, "The lithosphere is broken into plates."),
 ]),
 dict(t="2.2 Plate Tectonics", std="SC.912.E.6",
 body="""The surface of Earth is not one solid piece. Psalm 104:5 says of God, Who laid the foundations of the earth, that it should not be removed for ever. The lithosphere is broken into large plates that move slowly over the asthenosphere. The theory of plate tectonics describes these plates and their motion.

The idea began with Alfred Wegener, a German scientist who proposed continental drift in 1912. He noticed that the coasts of South America and Africa fit together like puzzle pieces. He also pointed to matching rock formations and mountain ranges across the ocean, and to the same fossils of land plants and animals, such as Glossopteris and Mesosaurus, found on continents now far apart. Wegener could not explain what force moved the continents, so many scientists rejected the idea.

New evidence in the 1950s and 1960s changed their minds. Mapping of the ocean floor found the Mid Atlantic Ridge, an underwater mountain chain. Harry Hess proposed seafloor spreading, in which new crust forms at ridges and moves away on both sides. Rocks at the ridge are young and the rocks farther away are older. Magnetic stripes on the seafloor, which record flips in Earth's magnetic field, match on both sides of the ridge. Earthquake and volcano patterns also outline the plate edges.

Plates move because of forces in the mantle. Heat from the deep Earth makes mantle rock slowly circulate in convection currents. Slab pull, in which a cold, heavy plate sinks into the mantle, and ridge push also help drive the motion. Plates move only a few centimeters per year, about as fast as a fingernail grows.

There are three kinds of plate boundaries. At a divergent boundary plates move apart, as at the Mid Atlantic Ridge. At a convergent boundary plates move together. When an oceanic plate meets a continental plate, the denser oceanic plate sinks in a process called subduction, forming a trench and volcanoes. When two continental plates collide, they crumple into mountains, as the Himalayas formed. At a transform boundary plates slide past each other, as along the San Andreas Fault in California.

Your task: (1) List three kinds of evidence for continental drift. (2) Explain seafloor spreading. (3) Describe the three types of plate boundaries.""",
 script="""Welcome back. Listen, Psalm 104:5 says of God, Who laid the foundations of the earth, that it should not be removed for ever. The ground under us feels still, but the plates of the lithosphere move slowly.

Now watch this. In 1912 Alfred Wegener proposed continental drift. He pointed to the fit of the continents, matching rock formations and the same fossils on far apart continents. He could not explain the force, so many rejected the idea. Later, mapping of the seafloor found the Mid Atlantic Ridge. Harry Hess proposed seafloor spreading, where new crust forms at ridges and moves away. Magnetic stripes match on both sides of the ridge.

Plates move because of convection in the mantle, slab pull and ridge push. They move only a few centimeters a year, about as fast as a fingernail grows.

Look at the boundaries. At a divergent boundary, plates move apart. At a convergent boundary, they move together. An oceanic plate sinks under a continental plate in subduction and makes a trench and volcanoes. Two continents colliding build mountains like the Himalayas. At a transform boundary, plates slide past each other, like the San Andreas Fault.

Your task is to list evidence for drift, explain seafloor spreading and describe the boundaries. Take the four question check.""" + CLOSE,
 quiz=[
 ("Who proposed the idea of continental drift in 1912?", ["Alfred Wegener", "Harry Hess", "Isaac Newton", "Charles Richter"], 0, "Wegener proposed that the continents moved."),
 ("At a divergent boundary, two plates:", ["Move apart", "Move together", "Slide past each other", "Stop moving"], 0, "New crust forms where plates separate."),
 ("The San Andreas Fault in California is an example of a:", ["Transform boundary", "Divergent boundary", "Convergent boundary", "Hot spot"], 0, "Plates slide past each other there."),
 ("Which is evidence for seafloor spreading?", ["Magnetic stripes on the ocean floor that match on both sides of a ridge", "The fit of Florida and Cuba", "The depth of the Mariana Trench", "The height of the Himalayas"], 0, "The pattern shows new crust forming at the ridge."),
 ]),
 dict(t="2.3 Earthquakes and Volcanoes", std="SC.912.E.6",
 body="""Most earthquakes and volcanoes occur near plate boundaries. Psalm 46:2 says, Therefore will not we fear, though the earth be removed, and though the mountains be carried into the midst of the sea. God is our refuge even when the ground shakes.

An earthquake is the shaking of the ground caused by the sudden release of energy as rock breaks and slips along a fault. Stress builds up in rock over years until it snaps. The focus is the point underground where the rock breaks, and the epicenter is the point on the surface directly above it. The energy travels outward as seismic waves. P waves arrive first, S waves second, and surface waves last and usually cause the most damage. A seismograph records the waves. Scientists find an epicenter by using the arrival times of the waves at three or more stations.

Earthquakes are measured by magnitude. The moment magnitude scale, which replaced the Richter scale for large earthquakes, is a scale where each whole number increase means the ground motion is ten times as large and the energy released is about 32 times as great. A magnitude 7 earthquake is far more powerful than a magnitude 5. Intensity, which describes the shaking and damage at a place, is measured on a different scale. Earthquakes can cause landslides, fires and tsunamis, which are huge sea waves caused by sudden movement of the ocean floor. If you feel shaking, drop, cover and hold on. Most of Florida has very few earthquakes because it lies in the middle of a plate.

A volcano is an opening in Earth's crust where magma, gas and ash escape. Magma is molten rock underground, and lava is magma that reaches the surface. Volcanoes form at subduction zones and divergent boundaries, and also over hot spots, plumes of hot mantle rock, such as the one that built the Hawaiian Islands. Shield volcanoes, such as Mauna Loa, have gentle slopes and runny lava. Composite volcanoes, such as Mount St. Helens, have steep slopes and explosive eruptions of ash and lava. Cinder cones are small and steep. The eruption of Mount Vesuvius in 79 AD buried the Roman city of Pompeii. The Ring of Fire around the Pacific Ocean has about three quarters of the world's active volcanoes. Florida has no active volcanoes.

Your task: (1) Define focus, epicenter and magnitude. (2) Tell how a seismograph helps find an epicenter. (3) Compare shield and composite volcanoes.""",
 script="""Welcome back. Listen, Psalm 46:2 says, Therefore will not we fear, though the earth be removed, and though the mountains be carried into the midst of the sea. God is our refuge even when the ground shakes.

Now watch this. An earthquake is shaking caused by the sudden release of energy along a fault. The focus is where the rock breaks underground. The epicenter is the spot on the surface directly above it. P waves arrive first, then S waves, then surface waves, which usually cause the most damage. Scientists use arrival times at three or more stations to find the epicenter.

Magnitude measures the size. Each whole number means the ground motion is ten times as large and the energy about 32 times as great. If you feel shaking, drop, cover and hold on. Most of Florida has very few earthquakes.

Look at volcanoes. Magma is molten rock underground, and lava is magma on the surface. Volcanoes form at subduction zones, at divergent boundaries and over hot spots like Hawaii. Shield volcanoes have gentle slopes and runny lava. Composite volcanoes are steep and explosive, like Mount St. Helens. The Ring of Fire around the Pacific holds about three quarters of the world's active volcanoes. Florida has none.

Your task is to define focus, epicenter and magnitude, explain how epicenters are found and compare volcano types. Take the four question check.""" + CLOSE,
 quiz=[
 ("The point on Earth's surface directly above an earthquake's focus is the:", ["Epicenter", "Fault", "Vent", "Crater"], 0, "The epicenter lies above the focus."),
 ("Each increase of one whole number in magnitude means the ground motion is about:", ["Ten times as large", "Twice as large", "One more unit larger", "One tenth as large"], 0, "The scale is logarithmic."),
 ("Molten rock that reaches Earth's surface is called:", ["Lava", "Magma", "Ash", "Basalt"], 0, "Underground it is magma and on the surface it is lava."),
 ("If you feel an earthquake indoors, you should:", ["Drop, cover and hold on", "Run outside quickly", "Stand in a doorway on the top floor", "Use the elevator"], 0, "Protect your head and neck under sturdy furniture."),
 ]),
 dict(t="2.4 Mountains, the Ocean Floor and Changing Landforms", std="SC.912.E.6",
 body="""The surface of Earth is shaped by slow forces from within. Psalm 90:2 says, Before the mountains were brought forth, or ever thou hadst formed the earth and the world, even from everlasting to everlasting, thou art God. Mountains and ocean basins remind us how great and how patient the Creator is.

Stress in the crust squeezes, stretches and shears rock. Compression squeezes rock and can fold it into wavy shapes. An upward fold is an anticline and a downward fold is a syncline. Tension stretches rock, and rock can break along a fault. Where one block drops down relative to another, a normal fault forms. Where compression pushes one block over another, a reverse fault forms. In a strike slip fault, blocks slide sideways.

Mountains form in several ways. Folded mountains, such as the Himalayas and the Appalachians, form when plates collide and crumple the crust. The Himalayas are still rising because India continues to push into Asia, and the Appalachians are older and have been worn down by long erosion. Fault block mountains, such as the Sierra Nevada, form when large blocks tilt and lift along faults. Volcanic mountains, such as Mount Fuji, build up from erupted lava and ash. Dome mountains form when rising magma bulges the rock above it. A hot spot can build a chain of islands, such as Hawaii, as the plate moves over it.

The ocean floor has its own landforms. The continental shelf is the shallow edge of the continent, and the continental slope drops steeply beyond it. Deep ocean trenches mark subduction zones. The Mariana Trench in the Pacific Ocean reaches about 10,900 meters, deeper than Mount Everest is tall. The abyssal plain is the flat deep seafloor. Mid ocean ridges are long mountain chains where new crust forms, and seamounts are underwater volcanoes.

Florida lies on a wide, flat platform of limestone and has no tall mountains. The highest natural point in Florida, Britton Hill, is only about 105 meters above sea level.

Your task: (1) Compare folded, fault block and volcanic mountains. (2) Name three features of the ocean floor. (3) Explain what the three types of faults have in common and how they differ.""",
 script="""Welcome back. Listen, Psalm 90:2 says, Before the mountains were brought forth, or ever thou hadst formed the earth and the world, even from everlasting to everlasting, thou art God.

Now watch this. Stress in the crust squeezes, stretches and shears rock. Compression folds rock. An upward fold is an anticline and a downward fold is a syncline. Tension pulls rock apart and makes faults. In a normal fault one block drops down. In a reverse fault one block is pushed up over another. In a strike slip fault blocks slide sideways.

Look at mountains. Folded mountains, like the Himalayas, form when plates collide. Fault block mountains, like the Sierra Nevada, form when blocks tilt and lift. Volcanic mountains, like Mount Fuji, build up from lava and ash. A hot spot can build a chain of islands like Hawaii.

The ocean floor has a continental shelf, a continental slope, deep trenches, the flat abyssal plain, mid ocean ridges and seamounts. The Mariana Trench is about 10,900 meters deep, deeper than Mount Everest is tall.

Florida sits on a flat limestone platform. Its highest natural point, Britton Hill, is only about 105 meters above sea level.

Your task is to compare mountain types, name ocean floor features and compare faults. Take the four question check.""" + CLOSE,
 quiz=[
 ("The Himalayas are an example of which type of mountains?", ["Folded mountains", "Fault block mountains", "Volcanic mountains", "Dome mountains"], 0, "They formed when India collided with Asia."),
 ("A deep, narrow canyon in the ocean floor where one plate sinks under another is a:", ["Trench", "Ridge", "Abyssal plain", "Seamount"], 0, "Trenches mark subduction zones."),
 ("Compression squeezing rock can cause it to:", ["Fold", "Stretch only", "Melt at once", "Turn to sand"], 0, "Compression produces folds and reverse faults."),
 ("A chain of islands such as Hawaii forms as a plate moves over a:", ["Hot spot", "Transform fault", "Trench", "Glacier"], 0, "A plume of hot mantle rock stays in place while the plate moves."),
 ]),
 ],
 assess=dict(t="Assessment 2: Earth's Interior and Plate Tectonics",
 prompt="""Write a report of at least 250 words on Earth's interior and plate tectonics. Use complete sentences and label each part. Psalm 90:2 says, Before the mountains were brought forth, or ever thou hadst formed the earth and the world, even from everlasting to everlasting, thou art God.

Part 1: Name Earth's layers from the surface to the center, give the state (solid or liquid) of each, and explain how seismic waves show that the outer core is liquid.
Part 2: Describe the lithosphere and asthenosphere and tell how they relate to tectonic plates.
Part 3: Describe the evidence Alfred Wegener used for continental drift, tell why many scientists rejected the idea at first, and explain how seafloor spreading and magnetic stripes later supported plate tectonics.
Part 4: Describe divergent, convergent and transform boundaries, and give one real example of each. Explain subduction.
Part 5: Explain the difference between focus and epicenter, tell what magnitude measures, compare a shield volcano with a composite volcano, and explain why Florida has no active volcanoes and few earthquakes.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 10 points. Part 3: 25 points. Part 4: 25 points. Part 5: 15 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 2: Foundations That Do Not Fail",
 prompt="""Write a post of at least 120 words that (1) describes a time something you thought was solid or secure was shaken, (2) explains in your own words how plate tectonics causes earthquakes, volcanoes or mountains, (3) explains how the ground moving slowly over millions of years shows the patience and power of the Creator, and (4) connects your answer to Psalm 46:2, Psalm 104:5 or Psalm 90:2. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why can believers trust God as a refuge when the earth shakes? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("Earth's inner core is solid because of:", ["Great pressure", "Cold temperatures", "The magnetic field", "Seismic waves"], 0, "Extreme pressure keeps the hot iron solid."),
 ("Oceanic crust is mostly:", ["Basalt", "Granite", "Limestone", "Sandstone"], 0, "Oceanic crust is dense basalt."),
 ("Which evidence did Alfred Wegener use?", ["The same fossils on continents now far apart", "Magnetic stripes on the seafloor", "Satellite measurements of plate speed", "Seismic waves from the outer core"], 0, "Matching fossils, rocks and coastlines were his evidence."),
 ("Mid ocean ridges are places where:", ["New crust forms", "Crust is destroyed", "Plates slide past each other", "Plates collide"], 0, "Magma rises and cools at divergent boundaries."),
 ("When an oceanic plate meets a continental plate, the oceanic plate:", ["Sinks beneath the continental plate", "Rises above it", "Melts instantly", "Stops all movement"], 0, "The denser oceanic plate subducts."),
 ("The first seismic waves to arrive at a station are:", ["P waves", "S waves", "Surface waves", "Tsunami waves"], 0, "P waves travel fastest."),
 ("The Ring of Fire is found around which ocean?", ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"], 0, "Many plate boundaries ring the Pacific."),
 ("The Appalachian Mountains are mostly:", ["Old folded mountains worn down by erosion", "Young volcanic mountains", "Fault block mountains", "Newly forming mountains"], 0, "They are far older than the Himalayas."),
 ],
)
