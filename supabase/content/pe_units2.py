"""Physical Education with Personal Fitness, Unit 2: Cardiorespiratory Fitness. Florida physical education standards cited at strand level (PE.912.M, PE.912.C, PE.912.L); recheck exact wording at CPALMS."""
from pe_units1 import CLOSE

UNIT2 = dict(
 title="Unit 2: Cardiorespiratory Fitness",
 std="PE.912.M.1, PE.912.C.2, PE.912.L.3",
 topics=[
 dict(t="2.1 The Heart, Lungs and Circulation", std="PE.912.C.2",
 body="""The cardiorespiratory system includes the heart, the lungs and the blood vessels. The heart is a muscle about the size of a fist. It has four chambers and pumps blood through two loops: one to the lungs to pick up oxygen, and one to the rest of the body to deliver it. Arteries carry blood away from the heart, veins carry it back, and tiny capillaries pass oxygen and nutrients to the cells.

When you breathe in, air travels through the windpipe into the lungs, where tiny air sacs called alveoli pass oxygen into the blood and take carbon dioxide out. When you exercise, your muscles need more oxygen, so your breathing rate and heart rate rise. A fit heart pumps more blood with each beat, so it beats more slowly at rest and recovers faster after effort.

Regular aerobic exercise strengthens the heart muscle, widens the supply of blood to the muscles, lowers blood pressure and helps keep the arteries healthy. Smoking and vaping, a poor diet and inactivity harm the system. Proverbs 4:23 says, Keep thy heart with all diligence; for out of it are the issues of life. This is true of the spiritual heart and the physical heart alike.

Learn to find your pulse at the wrist or the side of the neck by pressing lightly with two fingers. Count the beats for 15 seconds and multiply by 4 to find beats per minute.

Your task: (1) Describe the path of blood through the heart, lungs and body. (2) Explain what happens to breathing and heart rate during exercise and why. (3) Find your pulse and calculate your heart rate at rest.""",
 script="""Welcome back. Listen, there is an engine in your chest that has never taken a day off, and today we learn how it works.

The cardiorespiratory system includes the heart, lungs and blood vessels. The heart is a muscle about the size of your fist. It has four chambers and pumps blood in two loops. One loop goes to the lungs to pick up oxygen. The other goes to the rest of the body to deliver it. Arteries carry blood away from the heart. Veins carry it back. Capillaries pass oxygen to the cells.

Now watch this. When you breathe in, air reaches tiny air sacs in the lungs called alveoli. Oxygen passes into your blood and carbon dioxide leaves. When you exercise, your muscles want more oxygen, so your breathing and heart rate go up.

Look at the benefit. A fit heart pumps more blood with each beat, so it beats more slowly at rest and recovers faster. Smoking, vaping, a poor diet and inactivity harm this system.

Proverbs 4:23 says, Keep thy heart with all diligence. That is true of the spiritual heart and the physical heart.

Your task is to describe the path of blood, explain what happens during exercise, and find your pulse. Take the four question check.""" + CLOSE,
 quiz=[
 ("Blood vessels that carry blood away from the heart are:", ["Arteries", "Veins", "Alveoli", "Tendons"], 0, "Arteries carry blood away and veins carry it back."),
 ("Oxygen enters the blood in tiny air sacs called:", ["Alveoli", "Capillaries", "Valves", "Ligaments"], 0, "Gas exchange happens in the alveoli of the lungs."),
 ("During exercise, heart rate and breathing rate:", ["Increase", "Decrease", "Stop", "Stay the same"], 0, "Muscles need more oxygen, so the system works harder."),
 ("A fit heart usually has a:", ["Lower resting heart rate", "Higher resting heart rate", "Weaker beat", "Smaller chamber count"], 0, "A stronger heart pumps more blood per beat."),
 ]),
 dict(t="2.2 Aerobic Activities and Training Methods", std="PE.912.M.1, PE.912.L.3",
 body="""Aerobic means with oxygen. Aerobic activities use the large muscles, are rhythmic and can be kept up for a long time. Examples are brisk walking, jogging, swimming, cycling, dancing, jumping rope, hiking, rowing and playing soccer or basketball. In South Florida, swimming, walking on the beach, cycling and playing outdoors in cooler hours are all good choices. Choose activities that you enjoy, because you will keep doing them.

Several training methods build endurance. Continuous training means keeping a steady pace for a set time, such as a 30 minute jog. Interval training alternates harder efforts with easy recovery, such as one minute of fast walking and two minutes of slow walking, repeated. Circuit training moves through a series of stations, such as jumping jacks, squats and high knees, with short rests. Cross training mixes different activities, which reduces boredom and the strain on any one body part.

Start easy. A beginner may walk 15 to 20 minutes on 3 or 4 days a week, then add a few minutes each week. A good rule is to add no more than about 10 percent to the total time or distance each week. Include rest days to let the body adapt. Isaiah 40:31 says, They that wait upon the LORD shall renew their strength; they shall mount up with wings as eagles; they shall run, and not be weary; and they shall walk, and not faint.

Your task: (1) Define aerobic and list five aerobic activities you could do. (2) Compare continuous, interval and circuit training. (3) Write a beginner schedule for 2 weeks.""",
 script="""Welcome back. Listen, the best exercise is the one you will actually do.

Aerobic means with oxygen. Aerobic activities use the big muscles, they are rhythmic, and you can keep them up for a long time. Think of brisk walking, jogging, swimming, cycling, dancing, jumping rope and playing soccer or basketball. In South Florida we have swimming, beach walks and cycling in the cooler hours. Choose what you enjoy.

Now watch this. There are several training methods. Continuous training is a steady pace for a set time, like a 30 minute jog. Interval training alternates harder effort with easy recovery. Circuit training moves through stations with short rests. Cross training mixes different activities, which fights boredom and spares your body from strain in one place.

Look at how to begin. A beginner might walk 15 to 20 minutes on three or four days a week, then add a few minutes weekly. Add no more than about 10 percent to your time or distance each week, and take rest days.

Isaiah 40:31 says that they that wait upon the LORD shall run, and not be weary.

Your task is to define aerobic, compare the three training methods, and write a two week beginner schedule. Take the four question check.""" + CLOSE,
 quiz=[
 ("Aerobic activity is activity that:", ["Uses oxygen and can be kept up for a long time", "Lasts only seconds", "Needs no breathing", "Is only for athletes"], 0, "Aerobic means with oxygen."),
 ("Alternating hard effort with easy recovery is called:", ["Interval training", "Continuous training", "Static stretching", "Resting"], 0, "Intervals mix harder and easier efforts."),
 ("A safe way for a beginner to progress is to:", ["Add small amounts each week", "Double the time every day", "Skip rest days", "Run to exhaustion"], 0, "Gradual progression lowers injury risk."),
 ("Mixing different activities to reduce boredom and strain is:", ["Cross training", "Specificity", "Reversibility", "Warming up"], 0, "Cross training builds fitness in varied ways."),
 ]),
 dict(t="2.3 Measuring Intensity", std="PE.912.C.2, PE.912.M.1",
 body="""Intensity is how hard your body is working. You can measure it in three simple ways. The first is heart rate. A rough estimate of your maximum heart rate is 220 minus your age. A 16 year old would have an estimated maximum of about 204 beats a minute. Moderate intensity is about 50 to 70 percent of that number, and vigorous intensity is about 70 to 85 percent. This formula is only an estimate, and individuals differ, so use it as a guide and not a rule.

The second way is the talk test. During moderate activity, you can talk but not sing. During vigorous activity, you can say only a few words before you must breathe. If you cannot talk at all, slow down.

The third way is the rating of perceived exertion, called RPE. Rate how hard you feel you are working on a scale from 0 to 10, where 0 is rest, 3 is light, 5 or 6 is moderate, 7 or 8 is vigorous and 10 is the hardest you could go. Most aerobic training for general fitness should feel like a 5 to 7.

Recovery heart rate also shows fitness. Check your pulse right after exercise and again after one minute of rest. A faster drop means better fitness. Hebrews 12:1 says, Let us run with patience the race that is set before us. Patience means pacing yourself, not starting at a sprint and quitting.

Your task: (1) Estimate your maximum heart rate and your moderate range using the formula. (2) Explain the talk test and the RPE scale. (3) Record your heart rate and RPE during a 10 minute walk.""",
 script="""Welcome back. Listen, how do you know whether you are working too easy, too hard or just right? You measure intensity.

There are three simple ways. First, heart rate. A rough estimate of your maximum heart rate is 220 minus your age. A 16 year old would have about 204 beats a minute. Moderate intensity is about 50 to 70 percent of that, and vigorous is about 70 to 85 percent. This is only an estimate. People differ, so use it as a guide, not a rule.

Now watch this. Second, the talk test. At moderate intensity, you can talk but not sing. At vigorous intensity, you can say only a few words before you need a breath. If you cannot talk at all, slow down.

Third, the rating of perceived exertion, or RPE. Rate how hard you feel you are working from 0 to 10. Rest is 0. Moderate is 5 or 6. Vigorous is 7 or 8. Most training for general fitness should feel like a 5 to 7.

Look at recovery. Check your pulse right after exercise and again after one minute of rest. A faster drop shows better fitness.

Hebrews 12:1 says, run with patience the race that is set before us. Pace yourself.

Your task is to estimate your heart rate range, explain the talk test and RPE, and record a 10 minute walk. Take the four question check.""" + CLOSE,
 quiz=[
 ("A rough estimate of maximum heart rate is:", ["220 minus your age", "100 plus your age", "Your age times 2", "60 plus your weight"], 0, "It is only an estimate and individuals differ."),
 ("During moderate activity, the talk test says you should be able to:", ["Talk but not sing", "Sing easily", "Not breathe", "Say only one word"], 0, "Talking but not singing is a sign of moderate effort."),
 ("On the 0 to 10 RPE scale, moderate effort is about:", ["5 or 6", "0", "1", "10"], 0, "Most general fitness training should feel like 5 to 7."),
 ("A faster drop in heart rate after exercise generally shows:", ["Better fitness", "Poorer fitness", "Dehydration only", "Nothing"], 0, "A fitter heart recovers faster."),
 ]),
 dict(t="2.4 Building Endurance and Preventing Heat Illness", std="PE.912.L.3, PE.912.R.5",
 body="""Endurance grows by steady, patient work. Galatians 6:9 says, Let us not be weary in well doing: for in due season we shall reap, if we faint not. A simple plan is to walk briskly and add short jogging segments. For example, jog one minute and walk two minutes, repeated for 15 to 20 minutes. Each week, lengthen the jogging and shorten the walking. Listen to your body and take a rest day when you need it.

Pacing helps. Start slower than you think you need to, keep an even effort, and finish strong. Run on safe, well lit paths with a friend or an adult nearby, and carry identification and a phone when possible. Wear bright clothing near roads and run facing traffic.

Heat is a special risk in Florida. Heat cramps are painful muscle spasms. Heat exhaustion shows as heavy sweating, cold and clammy skin, a fast, weak pulse, nausea, headache and dizziness. If you see these signs, stop, move to a cool place, loosen clothing, sip water and cool the body with wet cloths. Heat stroke is a medical emergency. Signs include a very high body temperature, hot skin, confusion, fainting or seizures. Call 911 at once and cool the person while waiting for help.

Prevent heat illness by drinking water before, during and after activity, wearing light clothing, using sunscreen, resting often in the shade, and slowly getting used to the heat over several days. Never leave a child or pet in a parked car.

Your task: (1) Write a four week walk and jog plan. (2) List the signs of heat exhaustion and heat stroke and tell what to do for each. (3) List five ways to prevent heat illness.""",
 script="""Welcome back. Listen, endurance is built a little at a time, and the Word says it plainly. Galatians 6:9. Let us not be weary in well doing: for in due season we shall reap, if we faint not.

Here is a simple plan. Walk briskly, then add short jogging pieces. Jog one minute, walk two, and repeat for 15 to 20 minutes. Each week, jog a little more and walk a little less. Rest when your body needs it.

Now watch this. Pace yourself. Start slower than you think you need to, keep an even effort and finish strong. Use safe, well lit paths. Run with a friend or an adult nearby. Face traffic and wear bright clothing.

Look at the heat. This is South Florida. Heat exhaustion shows as heavy sweating, cold and clammy skin, a weak, fast pulse, nausea and dizziness. Stop, get to a cool place, sip water and cool your body with wet cloths. Heat stroke is an emergency. Signs include very high body temperature, hot skin, confusion, fainting or seizures. Call 911 right away.

To prevent it, drink water before, during and after, wear light clothing, use sunscreen, rest in the shade, and get used to the heat slowly. Never leave a child or a pet in a parked car.

Your task is to write a four week plan, list heat illness signs and responses, and list five prevention steps. Take the four question check.""" + CLOSE,
 quiz=[
 ("Which is a sign of heat stroke that needs a 911 call?", ["Confusion and very hot skin", "Mild thirst", "A small blister", "Sore muscles"], 0, "Heat stroke is a medical emergency."),
 ("A good first response to heat exhaustion is to:", ["Move to a cool place and sip water", "Run faster", "Wear more clothes", "Drink nothing"], 0, "Rest, cooling and fluids help the body recover."),
 ("A sensible way to build endurance is to:", ["Alternate walking and jogging and lengthen the jogs weekly", "Sprint at once", "Skip warm ups", "Train only in noon heat"], 0, "Gradual progress builds endurance safely."),
 ("Which habit helps prevent heat illness?", ["Drinking water before, during and after activity", "Avoiding shade", "Wearing heavy clothing", "Training in the hottest hour"], 0, "Fluids and shade are key protections."),
 ]),
 ],
 assess=dict(t="Assessment 2: Cardiorespiratory Fitness",
 prompt="""Write a report of at least 250 words on cardiorespiratory fitness. Use complete sentences and label each part. Proverbs 4:23 says, Keep thy heart with all diligence; for out of it are the issues of life.

Part 1: Describe how the heart, lungs and blood vessels work together, and explain what happens to them during exercise.
Part 2: Name five aerobic activities and compare continuous, interval and circuit training.
Part 3: Explain how to measure intensity using heart rate, the talk test and the RPE scale, and give your own estimated moderate heart rate range.
Part 4: Write a four week plan to build endurance that follows the FITT principle.
Part 5: Describe the signs of heat exhaustion and heat stroke, what to do for each, and how you will stay safe in the Florida heat. Attach or describe your activity log for two weeks.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 20 points. Part 3: 20 points. Part 4: 20 points. Part 5: 15 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 2: Running the Race with Patience",
 prompt="""Write a post of at least 120 words that (1) tells which aerobic activity you will use to build endurance and why, (2) explains how you will pace yourself and stay safe, (3) describes one change you notice in your body after two weeks of regular activity, and (4) connects your answer to Hebrews 12:1, which says, Let us run with patience the race that is set before us. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why is rest as important as exercise? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("The heart pumps blood to the lungs to:", ["Pick up oxygen", "Make bone", "Digest food", "Store fat"], 0, "Blood picks up oxygen in the lungs and gives off carbon dioxide."),
 ("Capillaries are:", ["Tiny vessels that pass oxygen to cells", "Large muscles", "Air sacs", "Heart valves"], 0, "Capillaries link arteries and veins."),
 ("Which is an aerobic activity?", ["Brisk walking", "A single heavy lift", "A one second jump", "Holding still"], 0, "Brisk walking can be kept up for a long time."),
 ("Interval training:", ["Alternates hard effort with easy recovery", "Uses no movement", "Is only for swimmers", "Is only stretching"], 0, "Intervals mix effort and rest."),
 ("The estimated maximum heart rate for a 16 year old using 220 minus age is about:", ["204 beats a minute", "140 beats a minute", "60 beats a minute", "300 beats a minute"], 0, "220 minus 16 equals 204."),
 ("At moderate intensity, you can usually:", ["Talk but not sing", "Sing a song", "Not speak", "Sleep"], 0, "That is the talk test."),
 ("Heat stroke requires:", ["A call to 911 and rapid cooling", "More exercise", "Hot drinks", "Waiting an hour"], 0, "It is a life threatening emergency."),
 ("A good rule for progress is to add no more than about:", ["10 percent to weekly time or distance", "100 percent", "50 percent", "Nothing ever"], 0, "Small steps lower injury risk."),
 ])
