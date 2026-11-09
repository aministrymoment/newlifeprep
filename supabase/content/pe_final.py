"""Physical Education with Personal Fitness final module: final assessment (position 7) and final exam (quiz position 31)."""

FINAL_ASSESS = dict(t="Final Assessment: Personal Fitness Plan and Portfolio",
 prompt="""Create a personal fitness plan and portfolio of at least 600 words with your activity log attached, and prepare a short presentation of its main ideas. Get approval from a parent or guardian before you begin, and ask a doctor if you have any health concern. Write complete sentences and label each part. First Corinthians 6:19 says, What? know ye not that your body is the temple of the Holy Ghost which is in you, which ye have of God, and ye are not your own?

Part 1: Starting Point. Describe your health habits and your results on at least three assessments, such as a timed walk or run, resting heart rate, push ups or curl ups, and the sit and reach.
Part 2: Goals. Write at least three SMART goals, including at least one for cardiorespiratory fitness, one for strength or endurance and one for flexibility, health or wellness.
Part 3: The Plan. Design a four week program that follows the FITT principle, with a warm up and cool down, aerobic, strength and flexibility work, rest days and the national guideline of 60 minutes of daily activity for teens.
Part 4: Nutrition, Sleep and Wellness. Describe your plan for hydration, meals and snacks, sleep and stress, and one step to avoid tobacco, alcohol and drugs.
Part 5: Safety. Explain how you will handle Florida heat, prevent injury and respond if you or someone else is hurt.
Part 6: Results and Reflection. Attach your activity log for at least four weeks. Report your retest results, what you learned and what you will change.
Part 7: Scripture and Service. Connect your plan to a passage of Scripture in the King James Version and describe one way you will use your health to serve others.
Part 8: Presentation Plan. Write a three part outline and an opening line for a three minute talk.""",
 rubric="""100 points. Part 1, starting point: 10 points. Part 2, goals: 10 points. Part 3, the plan and use of FITT: 20 points. Part 4, nutrition, sleep and wellness: 15 points. Part 5, safety: 10 points. Part 6, results, activity log and reflection: 15 points. Part 7, Scripture and service: 5 points. Part 8, presentation plan: 5 points. Grammar, conventions and respectful tone: 10 points. A score of 70 or above is passing."""
)

FINAL_EXAM = [
 ("Teens should get at least how much moderate to vigorous activity each day?", ["60 minutes", "5 minutes", "10 minutes", "3 hours"], 0, "The national guideline is 60 minutes a day for ages 6 to 17."),
 ("The ability of the heart, lungs and blood vessels to supply oxygen during long activity is:", ["Cardiorespiratory endurance", "Flexibility", "Agility", "Reaction time"], 0, "It is the first of the health related components."),
 ("In the FITT principle, the F stands for:", ["Frequency", "Fitness", "Fat", "Force"], 0, "FITT stands for frequency, intensity, time and type."),
 ("A rough estimate of maximum heart rate is:", ["220 minus your age", "100 plus your age", "Your age times 3", "60 minus your age"], 0, "It is only an estimate, and individuals differ."),
 ("A sign of heat stroke that needs an immediate 911 call is:", ["Confusion and very hot skin", "Mild thirst", "A sore muscle", "A small scrape"], 0, "Heat stroke is a medical emergency."),
 ("When the biceps contracts, the triceps:", ["Relaxes", "Disappears", "Contracts fully", "Turns to bone"], 0, "Muscles work in opposing pairs."),
 ("A beginner strength routine should include:", ["Good form and rest between sets", "A maximum lift without a spotter", "Holding the breath", "Steroids"], 0, "Safety and form come first."),
 ("Static stretching is best done:", ["After exercise when muscles are warm", "Bouncing on cold muscles", "Never", "Only before sleep"], 0, "Warm muscles stretch more safely."),
 ("In the RICE method, the I stands for:", ["Ice", "Intensity", "Inflammation", "Injury"], 0, "RICE means rest, ice, compression and elevation."),
 ("MyPlate suggests filling about half your plate with:", ["Fruits and vegetables", "Sweets", "Fried foods", "Soda"], 0, "Fruits and vegetables belong on half the plate."),
 ("A sign of good hydration is urine that is:", ["Pale yellow", "Dark yellow", "Brown", "Bright orange"], 0, "Pale yellow suggests that you are drinking enough."),
 ("Teens need about how many hours of sleep each night?", ["8 to 10", "3 to 4", "5 to 6", "12 to 14"], 0, "Sleep supports growth, mood and learning."),
 ("Nicotine in cigarettes and vapes is:", ["Highly addictive", "Harmless", "A vitamin", "A fruit"], 0, "Nicotine is the addictive drug in tobacco and vaping products."),
 ("A person who is worried about their eating or mood should:", ["Talk with a trusted adult, counselor or doctor", "Hide it", "Wait without telling anyone", "Take supplements"], 0, "Help is available and recovery is possible."),
 ("First Timothy 4:8 says that godliness is:", ["Profitable unto all things", "Profitable in nothing", "Only for adults", "A waste of time"], 0, "Exercise is useful, but godliness is profitable unto all things."),
]
