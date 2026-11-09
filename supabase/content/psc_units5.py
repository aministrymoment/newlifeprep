"""Physical Science, Unit 5: Energy, Work and Heat. Florida NGSSS Physical Science (SC.912.P.10) cited at strand level; recheck exact benchmark codes at CPALMS."""
from psc_units1 import CLOSE

UNIT5 = dict(
 title="Unit 5: Energy, Work and Heat",
 std="SC.912.P.10",
 topics=[
 dict(t="5.1 Forms of Energy and Conservation of Energy", std="SC.912.P.10",
 body="""Energy is the ability to cause change, and it is measured in joules. Psalm 62:11 says, God hath spoken once; twice have I heard this; that power belongeth unto God. All the energy of the universe comes from His hand.

Kinetic energy is the energy of motion. It depends on mass and speed, and the formula is one half times mass times speed squared. A 2 kilogram ball moving at 3 meters per second has a kinetic energy of one half times 2 times 9, which is 9 joules. Doubling the speed makes the kinetic energy four times as great, which is why speed matters so much in car crashes.

Potential energy is stored energy. Gravitational potential energy depends on height and equals mass times the acceleration due to gravity times height. A 5 kilogram box held 2 meters above the floor has 5 times 9.8 times 2, which is 98 joules. Elastic potential energy is stored in a stretched spring or rubber band. Chemical energy is stored in food, fuel and batteries. Other forms include thermal energy, electrical energy, light, sound and nuclear energy.

Energy changes from one form to another. In a pendulum, the bob has the most potential energy at the top of its swing and the most kinetic energy at the bottom. On a roller coaster, the car at the top of the first hill has the most potential energy, and it changes to kinetic energy as the car goes down. A lamp changes electrical energy into light and heat.

The law of conservation of energy says that energy cannot be created or destroyed, only changed from one form to another. The total energy of a closed system stays the same. When it seems that energy is lost, it has usually become thermal energy spread into the surroundings through friction.

Your task: (1) Calculate kinetic and potential energy. (2) Describe an energy change in a pendulum or roller coaster. (3) State the law of conservation of energy.""",
 script="""Welcome back. Listen, Psalm 62:11 says, God hath spoken once; twice have I heard this; that power belongeth unto God. All the energy of the universe comes from His hand.

Now watch this. Kinetic energy is the energy of motion, one half times mass times speed squared. A 2 kilogram ball moving at 3 meters per second has 9 joules. Doubling the speed makes the kinetic energy four times as great.

Potential energy is stored energy. Gravitational potential energy is mass times 9.8 times height. A 5 kilogram box 2 meters up has 98 joules. Chemical energy is stored in food, fuel and batteries.

Look at energy changes. At the top of a pendulum swing, the potential energy is greatest. At the bottom, the kinetic energy is greatest. A roller coaster at the top of the first hill has the most potential energy, and it changes to kinetic energy on the way down.

The law of conservation of energy says energy cannot be created or destroyed, only changed from one form to another. When energy seems lost, it has usually become thermal energy through friction.

Your task is to calculate kinetic and potential energy, describe an energy change and state the law. Take the four question check.""" + CLOSE,
 quiz=[
 ("The energy of motion is called:", ["Kinetic energy", "Potential energy", "Chemical energy", "Nuclear energy"], 0, "Kinetic energy is the energy of motion."),
 ("A 2 kg ball moves at 3 m/s. Its kinetic energy is:", ["9 J", "6 J", "18 J", "3 J"], 0, "One half times 2 times 9 equals 9."),
 ("Energy stored because of an object's height is:", ["Gravitational potential energy", "Kinetic energy", "Thermal energy", "Sound energy"], 0, "Height gives gravitational potential energy."),
 ("The law of conservation of energy states that:", ["Energy is changed from one form to another but not created or destroyed", "Energy is completely used up", "Energy can be made from nothing", "Kinetic energy always equals potential energy"], 0, "Total energy stays constant."),
 ]),
 dict(t="5.2 Work, Power and Simple Machines", std="SC.912.P.10",
 body="""In science, work has a special meaning. Colossians 3:23 says, And whatsoever ye do, do it heartily, as to the Lord, and not unto men. Our daily work is service to God, and physics lets us measure the work done by a force.

Work is done when a force moves an object in the direction of the force. Work equals force times distance, and it is measured in joules. A joule is one newton of force through one meter. Lifting a 20 newton box 3 meters up does 20 times 3, which is 60 joules of work. If you hold a heavy box in place, you may get tired, but you do no work in the physics sense, because the box does not move.

Power is the rate of doing work. Power equals work divided by time, and it is measured in watts, where one watt is one joule per second. If you do 60 joules of work in 2 seconds, your power is 30 watts. One horsepower is about 746 watts.

A machine makes work easier by changing the size or direction of a force. It does not reduce the amount of work. The six simple machines are the lever, pulley, wheel and axle, inclined plane, wedge and screw. To lift a 600 newton barrel 1.5 meters straight up takes 900 joules of work. Pushing it up a ramp 6 meters long needs only 150 newtons of force, since 900 divided by 6 is 150, but you push over a longer distance. The mechanical advantage is the output force divided by the input force, which is 600 divided by 150, or 4.

No real machine is perfectly efficient, because friction turns some of the work into heat. Efficiency equals useful work out divided by work in, multiplied by 100 percent.

Your task: (1) Calculate work and power. (2) Name the six simple machines. (3) Explain how a ramp makes work easier.""",
 script="""Welcome back. Listen, Colossians 3:23 says, And whatsoever ye do, do it heartily, as to the Lord, and not unto men. Our daily work is service to God, and physics lets us measure it.

Now watch this. Work is done when a force moves an object in the direction of the force. Work equals force times distance, in joules. Lifting a 20 newton box 3 meters does 60 joules. Holding a box still does no work in the physics sense.

Power is the rate of doing work, work divided by time, in watts. Sixty joules in 2 seconds is 30 watts.

Look at machines. A machine changes the size or direction of a force, but it does not reduce the work. The six simple machines are the lever, pulley, wheel and axle, inclined plane, wedge and screw. Lifting a 600 newton barrel 1.5 meters takes 900 joules. A 6 meter ramp needs only 150 newtons, but you push over a longer distance. The mechanical advantage is 600 divided by 150, which is 4.

No real machine is perfectly efficient, because friction turns some work into heat.

Your task is to calculate work and power, name the simple machines and explain a ramp. Take the four question check.""" + CLOSE,
 quiz=[
 ("Work equals:", ["Force times distance", "Force divided by distance", "Mass times velocity", "Speed times time"], 0, "Work is force multiplied by distance."),
 ("A 20 N box is lifted 3 meters. The work done is:", ["60 J", "23 J", "6.7 J", "17 J"], 0, "20 times 3 equals 60."),
 ("Power is the rate of doing:", ["Work", "Force", "Distance", "Mass"], 0, "Power is work per unit of time."),
 ("60 joules of work done in 2 seconds is a power of:", ["30 W", "120 W", "62 W", "58 W"], 0, "60 divided by 2 equals 30."),
 ]),
 dict(t="5.3 Temperature, Heat and Heat Transfer", std="SC.912.P.10",
 body="""Heat and temperature are related but different. Psalm 19:6 says of the sun, His going forth is from the end of the heaven, and his circuit unto the ends of it: and there is nothing hid from the heat thereof. The heat of the sun reaches Earth across empty space, and understanding heat helps us understand the world.

All matter is made of particles in constant motion. Temperature measures the average kinetic energy of the particles. Thermal energy is the total energy of all the particles, so a large bathtub of warm water has more thermal energy than a small cup of hot water. Heat is the transfer of thermal energy from a hotter object to a cooler one, and it flows until both reach the same temperature, called thermal equilibrium.

Temperature is measured in degrees Celsius, degrees Fahrenheit or kelvins. Fahrenheit equals nine fifths of the Celsius temperature plus 32, so 25 degrees Celsius is 77 degrees Fahrenheit. Kelvins equal degrees Celsius plus 273, so 25 degrees Celsius is 298 kelvins. Absolute zero is 0 kelvins, about negative 273 degrees Celsius, where particle motion is at a minimum.

Specific heat is the energy needed to raise the temperature of 1 gram of a substance by 1 degree Celsius. Water has a high specific heat, 4.18 joules per gram per degree Celsius. The heat needed equals mass times specific heat times the temperature change. Warming 100 grams of water by 10 degrees Celsius takes 100 times 4.18 times 10, which is 4180 joules. Water's high specific heat keeps coastal areas milder than inland areas.

Heat moves in three ways. Conduction is transfer by direct contact, as a metal spoon heats in hot soup. Convection is transfer by the movement of a fluid, as warm air rises and cool air sinks. Radiation is transfer by waves that can cross empty space, as sunlight does. Insulators such as foam, wool and air slow conduction, and metals are good conductors.

Your task: (1) Tell heat from temperature. (2) Convert temperature scales. (3) Name the three ways heat moves with an example of each.""",
 script="""Welcome back. Listen, Psalm 19:6 says of the sun, there is nothing hid from the heat thereof. The heat of the sun crosses empty space to reach us, and understanding heat helps us understand the world.

Now watch this. All matter is made of particles in constant motion. Temperature measures their average kinetic energy. Thermal energy is the total. A bathtub of warm water has more thermal energy than a cup of hot water. Heat is thermal energy moving from a hotter object to a cooler one, until they reach thermal equilibrium.

Look at the scales. Fahrenheit is nine fifths of Celsius plus 32, so 25 degrees Celsius is 77 degrees Fahrenheit. Kelvins are Celsius plus 273, so 25 degrees Celsius is 298 kelvins.

Water has a high specific heat, 4.18 joules per gram per degree Celsius. Warming 100 grams of water by 10 degrees takes 4180 joules. That keeps coastal areas milder.

Heat moves by conduction, which is direct contact, by convection, which is the movement of a fluid, and by radiation, which can cross empty space.

Your task is to tell heat from temperature, convert scales and name the three ways heat moves. Take the four question check.""" + CLOSE,
 quiz=[
 ("Temperature measures the average:", ["Kinetic energy of the particles", "Mass of the particles", "Volume of the particles", "Charge of the particles"], 0, "Temperature reflects average particle motion."),
 ("Heat flows naturally from:", ["A hotter object to a cooler object", "A cooler object to a hotter object", "A larger object to a smaller one", "A heavier object to a lighter one"], 0, "Heat moves from hot to cold."),
 ("Heat transfer by direct contact is called:", ["Conduction", "Convection", "Radiation", "Reflection"], 0, "Conduction needs direct contact."),
 ("On the Kelvin scale, 0 degrees Celsius is:", ["273 K", "0 K", "100 K", "373 K"], 0, "Kelvins equal Celsius plus 273."),
 ]),
 dict(t="5.4 Energy Resources and Good Stewardship", std="SC.912.P.10",
 body="""People use energy every day for light, heat, travel and food. Genesis 8:22 says, While the earth remaineth, seedtime and harvest, and cold and heat, and summer and winter, and day and night shall not cease. God built the earth with energy cycles, and He gave people the work of caring for it. Genesis 2:15 says the LORD God took the man, and put him into the garden of Eden to dress it and to keep it.

Two laws of thermodynamics guide us. The first law says energy is conserved. The second says that in any energy conversion some energy spreads out as waste heat that is no longer easy to use, and that heat flows on its own from hot to cold. No machine is perfectly efficient. A gasoline car engine turns only about one fourth of the fuel's energy into motion, and the rest leaves as heat. A modern power plant is more efficient but still loses energy.

Nonrenewable resources are used faster than nature replaces them. Fossil fuels, which are coal, oil and natural gas, formed over millions of years from the remains of ancient plants and animals. They store a great deal of energy and power most of the world, but burning them releases carbon dioxide and other pollutants. Nuclear power uses fission, the splitting of uranium atoms, to make heat without burning, but it produces radioactive waste that must be stored safely.

Renewable resources are replaced by natural processes. Solar cells turn sunlight into electricity. Wind turbines use moving air. Hydroelectric dams use falling water. Geothermal plants use heat from inside Earth. Biomass uses plant material. Each source has benefits and costs, such as cost, reliability when the sun does not shine or the wind does not blow, effects on land and wildlife, and the amount of energy it can supply.

Wise stewardship uses energy carefully. Saving energy at home, choosing efficient appliances and LED lighting, insulating buildings and avoiding waste are practical steps. Good decisions weigh the facts, the costs and the care of creation and our neighbors.

Your task: (1) State the first and second laws of thermodynamics in your own words. (2) Compare a renewable and a nonrenewable resource. (3) List three ways to use energy wisely.""",
 script="""Welcome back. Listen, Genesis 8:22 says, While the earth remaineth, seedtime and harvest, and cold and heat, and summer and winter, and day and night shall not cease. God built the earth with energy cycles, and in Genesis 2:15 He gave people the work to dress it and to keep it.

Now watch this. The first law says energy is conserved. The second says some energy always spreads out as waste heat, and heat flows from hot to cold. A gasoline engine turns only about one fourth of its fuel into motion.

Nonrenewable resources are used faster than nature replaces them. Fossil fuels, coal, oil and natural gas, formed from ancient plants and animals. They store a great deal of energy, but burning them releases carbon dioxide. Nuclear power splits uranium atoms to make heat, and it produces waste that must be stored safely.

Renewable resources are replaced naturally. They are solar, wind, hydroelectric, geothermal and biomass. Each has benefits and costs, such as price, reliability, effects on land and wildlife and how much energy it supplies.

Wise stewardship saves energy with efficient appliances, LED lighting and good insulation. Good decisions weigh the facts, the costs and the care of creation and our neighbors.

Your task is to state the two laws, compare two resources and list ways to use energy wisely. Take the four question check.""" + CLOSE,
 quiz=[
 ("In any energy conversion, some energy is usually:", ["Spread out as waste heat", "Destroyed", "Created", "Turned into matter"], 0, "Some energy becomes waste heat, though it is not destroyed."),
 ("Which is a renewable energy source?", ["Wind", "Coal", "Natural gas", "Oil"], 0, "Wind is replaced naturally."),
 ("Fossil fuels formed from:", ["The remains of ancient plants and animals", "Volcanic ash only", "Meteorites", "Salt water"], 0, "Coal, oil and gas come from ancient living things."),
 ("Genesis 2:15 supports using energy resources with:", ["Careful stewardship", "No limits at all", "Waste", "Fear"], 0, "Humans were told to dress and keep the earth."),
 ]),
 ],
 assess=dict(t="Assessment 5: Energy, Work and Heat",
 prompt="""Write a report of at least 250 words on energy, work and heat. Use complete sentences, show every calculation and label each part. Psalm 62:11 says, God hath spoken once; twice have I heard this; that power belongeth unto God.

Part 1: Find the kinetic energy of a 3 kilogram cart moving at 4 meters per second, and the gravitational potential energy of a 4 kilogram book held 5 meters high. Describe the energy changes in a roller coaster and state the law of conservation of energy.
Part 2: A student lifts a 50 newton weight 4 meters in 5 seconds. Find the work and the power. Explain how a ramp makes the job easier without reducing the work.
Part 3: Convert 30 degrees Celsius to degrees Fahrenheit and to kelvins. Explain the difference between heat and temperature, and give an example of conduction, convection and radiation.
Part 4: Find the energy needed to warm 200 grams of water by 5 degrees Celsius, using 4.18 joules per gram per degree Celsius. Explain why water's high specific heat matters for coastal climates.
Part 5: Compare one renewable and one nonrenewable energy source, giving at least two benefits and two costs for each. Explain how Genesis 2:15 guides wise stewardship and give three ways to use energy wisely.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 20 points. Part 3: 20 points. Part 4: 15 points. Part 5: 20 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 5: Work, Power and Stewardship",
 prompt="""Write a post of at least 120 words that (1) describes work you do at home, school or church and what it takes to do it well, (2) explains in your own words the difference between work and power, or between heat and temperature, (3) tells one way your family or church could use energy more wisely, and (4) connects your answer to Colossians 3:23, Genesis 2:15 or Psalm 62:11. Then write a respectful reply of at least 40 words to another student's post, or answer this question: How does caring for the earth and its energy show love for our neighbors? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("A 4 kg object moves at 5 m/s. Its kinetic energy is:", ["50 J", "100 J", "20 J", "10 J"], 0, "One half times 4 times 25 equals 50."),
 ("A 5 kg box is lifted 2 meters near Earth. Its gain in potential energy is about:", ["98 J", "10 J", "49 J", "196 J"], 0, "5 times 9.8 times 2 equals 98."),
 ("A roller coaster car at the top of a hill has the most:", ["Potential energy", "Kinetic energy", "Sound energy", "Mass"], 0, "The highest point has the greatest potential energy."),
 ("A ramp makes lifting easier by:", ["Reducing the force needed while increasing the distance", "Reducing the work needed", "Creating energy", "Changing the mass"], 0, "The work stays the same but the force is smaller."),
 ("A machine does 500 J of useful work from 625 J of input. Its efficiency is:", ["80 percent", "125 percent", "20 percent", "50 percent"], 0, "500 divided by 625 equals 0.8."),
 ("Warming 100 g of water by 10 degrees Celsius takes about (specific heat 4.18):", ["4180 J", "418 J", "41.8 J", "418,000 J"], 0, "100 times 4.18 times 10 equals 4180."),
 ("Heat from the Sun reaches Earth by:", ["Radiation", "Conduction", "Convection", "Condensation"], 0, "Radiation can cross empty space."),
 ("Which is a nonrenewable energy source?", ["Coal", "Solar", "Wind", "Geothermal"], 0, "Coal is used faster than it forms."),
 ],
)
