"""Physical Science, Unit 4: Motion and Forces. Florida NGSSS Physical Science (SC.912.P.12) cited at strand level; recheck exact benchmark codes at CPALMS."""
from psc_units1 import CLOSE

UNIT4 = dict(
 title="Unit 4: Motion and Forces",
 std="SC.912.P.12",
 topics=[
 dict(t="4.1 Speed, Velocity and Displacement", std="SC.912.P.12",
 body="""Motion is a change in position, and we always describe it compared with a reference point. Hebrews 12:1 says, let us run with patience the race that is set before us. A race is a good picture of motion, and the Christian life has a course to run with steady endurance.

Distance is the total length of the path traveled. Displacement is the straight line change in position, including direction. If you run once around a 400 meter track and stop where you started, your distance is 400 meters but your displacement is zero. Distance has size only, while displacement has size and direction.

Speed is how fast an object moves. Average speed equals distance divided by time. A runner covers 400 meters in 50 seconds, so her average speed is 400 divided by 50, which is 8 meters per second. A car that travels 150 kilometers in 2 hours has an average speed of 75 kilometers per hour. Rearranging gives distance equals speed times time, and time equals distance divided by speed. If you ride at 6 meters per second for 30 seconds, you travel 180 meters.

Velocity is speed in a given direction. A car moving at 20 meters per second north has a different velocity from a car moving at 20 meters per second south, even though their speeds are the same. Velocity is a vector, which has both size and direction, and speed is a scalar, which has size only.

A distance time graph shows motion. A straight line that slopes upward shows constant speed. The steeper the line, the greater the speed. A flat line shows that the object is at rest. A curved line shows a changing speed.

Your task: (1) Tell distance from displacement. (2) Calculate average speed and distance. (3) Read a distance time graph.""",
 script="""Welcome back. Listen, Hebrews 12:1 says, let us run with patience the race that is set before us. A race is a good picture of motion, and the Christian life has a course to run with steady endurance.

Now watch this. Distance is the total length of the path. Displacement is the straight line change in position, with direction. If you run once around a 400 meter track, your distance is 400 meters but your displacement is zero.

Look at speed. Average speed is distance divided by time. A runner covers 400 meters in 50 seconds, so her speed is 8 meters per second. A car that travels 150 kilometers in 2 hours averages 75 kilometers per hour. Distance equals speed times time, so 6 meters per second for 30 seconds is 180 meters.

Velocity is speed in a given direction. Twenty meters per second north and twenty meters per second south are different velocities with the same speed.

On a distance time graph, the steeper the line, the greater the speed. A flat line means the object is at rest.

Your task is to tell distance from displacement, calculate speed and read a graph. Take the four question check.""" + CLOSE,
 quiz=[
 ("Average speed equals:", ["Distance divided by time", "Time divided by distance", "Distance times time", "Mass divided by volume"], 0, "Speed is distance per unit of time."),
 ("A runner covers 400 meters in 50 seconds. Her average speed is:", ["8 m/s", "350 m/s", "20,000 m/s", "0.125 m/s"], 0, "400 divided by 50 equals 8."),
 ("Velocity differs from speed because velocity includes:", ["Direction", "Mass", "Time only", "Energy"], 0, "Velocity is speed with direction."),
 ("On a distance time graph, a steeper line means:", ["Greater speed", "Lower speed", "No motion", "Greater mass"], 0, "The slope of the line is the speed."),
 ]),
 dict(t="4.2 Acceleration and Free Fall", std="SC.912.P.12",
 body="""Acceleration is how quickly velocity changes. Ecclesiastes 9:11 says, the race is not to the swift, nor the battle to the strong. Speed alone does not decide every outcome, and we remember that God rules over all.

Acceleration equals the final velocity minus the initial velocity, divided by the time. A car speeds up from 0 to 20 meters per second in 5 seconds. The change in velocity is 20, and 20 divided by 5 is 4, so the acceleration is 4 meters per second squared. That means the velocity increases by 4 meters per second every second.

Slowing down is also acceleration. A cyclist slows from 12 meters per second to 4 meters per second in 4 seconds. The change in velocity is negative 8, so the acceleration is negative 8 divided by 4, which is negative 2 meters per second squared. The negative sign tells us the acceleration points opposite the motion.

Because velocity includes direction, an object accelerates when it speeds up, slows down or changes direction. A car going around a curve at a steady speed is still accelerating, because its direction keeps changing. The same is true of a planet in orbit.

Free fall is motion with only gravity acting. Near Earth's surface, an object in free fall gains about 9.8 meters per second of speed every second, so the acceleration is 9.8 meters per second squared. Starting from rest, after 1 second the speed is 9.8 meters per second, and after 3 seconds it is 29.4 meters per second. In air, resistance slows the fall. A falling skydiver reaches terminal velocity when air resistance balances the weight, and the speed stops increasing.

A speed time graph helps. A rising line shows speeding up, and its slope is the acceleration. A flat line shows constant speed.

Your task: (1) Calculate acceleration. (2) Explain how a car at constant speed on a curve accelerates. (3) Find the speed of a falling object after a given time.""",
 script="""Welcome back. Listen, Ecclesiastes 9:11 says, the race is not to the swift, nor the battle to the strong. Speed alone does not decide every outcome, and we remember that God rules over all.

Now watch this. Acceleration is the final velocity minus the initial velocity, divided by the time. A car goes from 0 to 20 meters per second in 5 seconds. That is 20 divided by 5, so the acceleration is 4 meters per second squared.

Slowing down is acceleration too. A cyclist slows from 12 to 4 meters per second in 4 seconds. The change is negative 8, so the acceleration is negative 2 meters per second squared.

Velocity includes direction, so an object also accelerates when it changes direction. A car on a curve at steady speed is accelerating.

Free fall is motion with only gravity acting. Near Earth's surface the acceleration is about 9.8 meters per second squared. From rest, the speed after 3 seconds is 29.4 meters per second. Air resistance slows the fall, and a skydiver reaches terminal velocity when air resistance balances weight.

Your task is to calculate acceleration, explain acceleration on a curve and find a falling speed. Take the four question check.""" + CLOSE,
 quiz=[
 ("Acceleration is the rate of change of:", ["Velocity", "Distance", "Mass", "Force"], 0, "Acceleration measures how quickly velocity changes."),
 ("A car speeds up from 0 to 20 m/s in 5 seconds. Its acceleration is:", ["4 m/s squared", "100 m/s squared", "15 m/s squared", "0.25 m/s squared"], 0, "20 divided by 5 equals 4."),
 ("An object moving in a circle at constant speed is accelerating because:", ["The direction of its velocity is changing", "Its mass is changing", "Its speed is changing", "Its weight is changing"], 0, "Changing direction means changing velocity."),
 ("Near Earth's surface, an object in free fall accelerates at about:", ["9.8 m/s squared", "98 m/s squared", "1 m/s squared", "0 m/s squared"], 0, "Gravity gives about 9.8 meters per second squared."),
 ]),
 dict(t="4.3 Forces and Newton's Laws of Motion", std="SC.912.P.12",
 body="""A force is a push or a pull, measured in newtons. Job 26:7 says of God, He stretcheth out the north over the empty place, and hangeth the earth upon nothing. The laws of motion describe how the Creator governs everything from a rolling ball to the planets.

Forces combine. The net force is the sum of all the forces on an object, taking direction into account. Balanced forces cancel, so the net force is zero and the motion does not change. Unbalanced forces change the motion.

Newton's first law says that an object at rest stays at rest, and an object in motion stays in motion at a constant velocity, unless an unbalanced force acts on it. This tendency is inertia, and the more mass an object has, the more inertia it has. Passengers lurch forward when a car brakes because their bodies keep moving, which is why seat belts matter.

Newton's second law says that acceleration equals the net force divided by the mass, or force equals mass times acceleration. A 2 kilogram cart that accelerates at 3 meters per second squared has a net force of 2 times 3, which is 6 newtons. A net force of 60 newtons on a 12 kilogram object gives an acceleration of 5 meters per second squared. A bigger force gives a bigger acceleration, and a bigger mass gives a smaller acceleration.

Newton's third law says that for every action there is an equal and opposite reaction. When you push on a wall, the wall pushes back with the same force. The two forces act on different objects, so they do not cancel. A rocket moves forward because it pushes hot gas backward.

Friction is a force that opposes motion between surfaces. Static friction holds an object that is not moving, sliding friction acts when surfaces slide, and rolling friction acts on wheels. Friction produces heat and wears surfaces, yet without it we could not walk or stop a car.

Your task: (1) State each of Newton's laws with an example. (2) Use force equals mass times acceleration. (3) Explain why action and reaction forces do not cancel.""",
 script="""Welcome back. Listen, Job 26:7 says of God, He stretcheth out the north over the empty place, and hangeth the earth upon nothing. The laws of motion describe how the Creator governs everything from a rolling ball to the planets.

Now watch this. The net force is the sum of all forces on an object. Balanced forces cancel and the motion does not change. Unbalanced forces change the motion.

Newton's first law says an object keeps its motion unless an unbalanced force acts on it. That tendency is inertia, and more mass means more inertia. Seat belts matter because your body keeps moving when the car stops.

Newton's second law says force equals mass times acceleration. A 2 kilogram cart accelerating at 3 meters per second squared has a net force of 6 newtons. Sixty newtons on a 12 kilogram object gives 5 meters per second squared.

Newton's third law says for every action there is an equal and opposite reaction. When you push a wall, it pushes back. The forces act on different objects, so they do not cancel. A rocket moves forward by pushing gas backward.

Friction opposes motion. Without it we could not walk or stop a car.

Your task is to state the three laws, use force equals mass times acceleration and explain action and reaction. Take the four question check.""" + CLOSE,
 quiz=[
 ("Newton's first law says an object at rest stays at rest unless acted on by:", ["An unbalanced force", "A balanced force", "Its own color", "Its temperature"], 0, "An unbalanced force changes motion."),
 ("A 2 kg cart accelerates at 3 m/s squared. The net force is:", ["6 N", "1.5 N", "5 N", "0.67 N"], 0, "Force equals 2 times 3."),
 ("When you push on a wall, the wall pushes back with an equal force. This is Newton's:", ["Third law", "First law", "Second law", "Law of gravity"], 0, "Action and reaction describe the third law."),
 ("Which object has the most inertia?", ["A 10 kg box", "A 1 kg ball", "A 2 kg book", "A 5 gram marble"], 0, "Inertia increases with mass."),
 ]),
 dict(t="4.4 Gravity, Momentum and Orbits", std="SC.912.P.12",
 body="""Gravity is the force that pulls masses toward each other. Psalm 8:3 says, When I consider thy heavens, the work of thy fingers, the moon and the stars, which thou hast ordained. The same gravity that holds us to the ground holds the Moon in its path.

Newton's law of universal gravitation says every mass attracts every other mass. The force is greater when the masses are larger and weaker when the objects are farther apart. If the distance doubles, the force becomes one fourth as strong. Because Earth is so massive, we feel its pull strongly.

Weight is the force of gravity on an object, equal to mass times the acceleration due to gravity. A 50 kilogram person has a weight of 50 times 9.8, which is 490 newtons. The Moon has less mass, so its gravity is about one sixth of Earth's. A 50 kilogram person has the same mass on the Moon but a much smaller weight. Without air resistance, all objects fall with the same acceleration regardless of mass. In 1971 an astronaut on the Moon dropped a hammer and a feather together, and they landed at the same time.

An orbit is a path in which an object falls around another object. A satellite moves sideways so fast that as it falls toward Earth, the ground curves away beneath it. Gravity keeps pulling it into a curved path.

Momentum equals mass times velocity. A 1000 kilogram car moving at 20 meters per second has a momentum of 20,000 kilogram meters per second. Momentum is conserved in a collision when no outside forces act, so the total momentum before equals the total after. A 2 kilogram cart moving at 3 meters per second has a momentum of 6. If it sticks to a 1 kilogram cart at rest, the total momentum is still 6, and the combined mass of 3 kilograms moves at 6 divided by 3, which is 2 meters per second.

Your task: (1) Explain how mass and distance affect gravity. (2) Calculate weight and momentum. (3) Use conservation of momentum in a collision.""",
 script="""Welcome back. Listen, Psalm 8:3 says, When I consider thy heavens, the work of thy fingers, the moon and the stars, which thou hast ordained. The same gravity that holds us to the ground holds the Moon in its path.

Now watch this. Every mass attracts every other mass. The force grows with larger masses and weakens with distance. If the distance doubles, the force becomes one fourth as strong.

Weight is mass times the acceleration due to gravity. A 50 kilogram person weighs 50 times 9.8, which is 490 newtons. The Moon's gravity is about one sixth of Earth's. Without air resistance, all objects fall with the same acceleration. An astronaut on the Moon dropped a hammer and a feather together and they landed at the same time.

An orbit is a path in which an object falls around another. A satellite moves sideways so fast that the ground curves away as it falls.

Momentum is mass times velocity. A 1000 kilogram car at 20 meters per second has a momentum of 20,000. In a collision the total momentum is conserved. A 2 kilogram cart at 3 meters per second sticks to a 1 kilogram cart at rest. Total momentum is 6, and the 3 kilograms move at 2 meters per second.

Your task is to explain gravity, calculate weight and momentum and use conservation of momentum. Take the four question check.""" + CLOSE,
 quiz=[
 ("The force of gravity between two objects increases when:", ["Their masses increase or the distance between them decreases", "The distance between them increases", "Their masses decrease", "They move faster"], 0, "Gravity grows with mass and weakens with distance."),
 ("A 50 kg person has a weight on Earth of about:", ["490 N", "50 N", "5 N", "4900 N"], 0, "50 times 9.8 equals 490."),
 ("Momentum equals:", ["Mass times velocity", "Mass divided by velocity", "Force times distance", "Velocity divided by time"], 0, "Momentum is mass multiplied by velocity."),
 ("A 2 kg cart moving at 3 m/s sticks to a 1 kg cart at rest. Their speed afterward is:", ["2 m/s", "3 m/s", "1 m/s", "6 m/s"], 0, "Total momentum 6 divided by total mass 3 equals 2."),
 ]),
 ],
 assess=dict(t="Assessment 4: Motion and Forces",
 prompt="""Write a report of at least 250 words on motion and forces. Use complete sentences, show every calculation and label each part. Job 26:7 says, He stretcheth out the north over the empty place, and hangeth the earth upon nothing.

Part 1: A cyclist rides 90 kilometers in 3 hours. Find the average speed. Then explain the difference between distance and displacement using a runner who circles a 400 meter track once.
Part 2: A car speeds up from 5 meters per second to 25 meters per second in 4 seconds. Find its acceleration. Then find the speed of a ball dropped from rest after 2 seconds of free fall, using 9.8 meters per second squared.
Part 3: State Newton's three laws and give one everyday example of each. Find the net force needed to accelerate a 1500 kilogram car at 2 meters per second squared.
Part 4: Find the weight in newtons of a 60 kilogram student on Earth. Explain what happens to the force of gravity between two objects when the distance between them doubles.
Part 5: A 1 kilogram cart moving at 4 meters per second hits and sticks to a 3 kilogram cart at rest. Find their speed afterward. Explain how seat belts and Job 26:7 show care in using the laws of motion.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 20 points. Part 3: 25 points. Part 4: 15 points. Part 5: 15 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 4: Forces and Finishing the Race",
 prompt="""Write a post of at least 120 words that (1) describes a time you had to keep going at a steady pace, in sports, school or life, (2) explains Newton's first law and how it relates to staying in motion or staying at rest, (3) explains how safety devices such as seat belts use the laws of motion to protect people, and (4) connects your answer to Hebrews 12:1, Job 26:7 or Psalm 8:3. Then write a respectful reply of at least 40 words to another student's post, or answer this question: What does it mean that God hangs the earth upon nothing, and how does gravity describe His order? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("A car travels 150 km in 2 hours. Its average speed is:", ["75 km/h", "300 km/h", "152 km/h", "0.013 km/h"], 0, "150 divided by 2 equals 75."),
 ("A runner goes once around a 400 meter track and ends where she started. Her displacement is:", ["0 meters", "400 meters", "200 meters", "800 meters"], 0, "She ended at the starting point."),
 ("A cyclist slows from 12 m/s to 4 m/s in 4 seconds. Her acceleration is:", ["Negative 2 m/s squared", "Positive 2 m/s squared", "Negative 8 m/s squared", "Positive 3 m/s squared"], 0, "Negative 8 divided by 4 equals negative 2."),
 ("A net force of 20 N acts on a 4 kg object. Its acceleration is:", ["5 m/s squared", "80 m/s squared", "0.2 m/s squared", "16 m/s squared"], 0, "20 divided by 4 equals 5."),
 ("Which law explains why passengers lurch forward when a car brakes suddenly?", ["Newton's first law", "Newton's third law", "The law of conservation of mass", "The law of reflection"], 0, "Inertia keeps the passengers moving."),
 ("The weight of a 10 kg object near Earth's surface is about:", ["98 N", "10 N", "9.8 N", "980 N"], 0, "10 times 9.8 equals 98."),
 ("A 1000 kg car moves at 20 m/s. Its momentum is:", ["20,000 kilogram meters per second", "50 kilogram meters per second", "1020 kilogram meters per second", "200 kilogram meters per second"], 0, "1000 times 20 equals 20,000."),
 ("Without air resistance, a heavy ball and a light ball dropped together:", ["Hit the ground at the same time", "Land with the heavy one first", "Land with the light one first", "Never land"], 0, "All objects fall with the same acceleration."),
 ],
)
