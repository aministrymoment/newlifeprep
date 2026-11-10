"""Health Education final module."""
FOCUS = ("Health Education is a one semester course on caring for the whole person: body, mind, relationships and spirit. Students study wellness, nutrition and physical activity, sleep, hygiene and stress, mental and emotional health, alcohol, tobacco, vaping and drugs, disease prevention, safety, first aid and CPR awareness, bullying and online safety, healthy relationships, abstinence and respect, decision making, goal setting and reliable health information. Students learn skills for making wise choices and see what Scripture teaches about the body as the temple of the Holy Ghost. The course gives general education and is not medical advice. It aligns to the Florida health education standards for grades 9 to 12 and ends with a final wellness plan and a final exam. Excellence, Faith, Purpose.")

FINAL_ASSESS = dict(t="Final Assessment: My Personal Wellness Plan",
 prompt="""Create a Personal Wellness Plan of at least 500 words and prepare a short presentation of its main ideas. Use complete sentences and label each part. Do not include private medical details, diagnoses, addresses, phone numbers or passwords, and review your plan with a parent or guardian before you submit it. 1 Corinthians 6:19 and 20 says, What? know ye not that your body is the temple of the Holy Ghost which is in you, which ye have of God, and ye are not your own? For ye are bought with a price: therefore glorify God in your body, and in your spirit, which are God's.

Part 1: Wellness goals. Write one SMART goal for each of the four parts of health: physical, mental and emotional, social and spiritual.
Part 2: Daily habits. Plan a day of meals using the five food groups, sixty minutes of activity, a sleep schedule of eight to ten hours and a hygiene routine.
Part 3: Stress and mental health. Name three healthy coping skills and explain what to do and who to contact if you or a friend is in crisis, including 988 and 911.
Part 4: Risk and prevention. Write a refusal plan for alcohol, nicotine and drugs, a home safety and emergency plan with the steps of Hands only CPR, and four ways to prevent infection.
Part 5: Relationships. Describe your personal standards, your boundaries and how you will treat others with respect, including online safety rules.
Part 6: Health information. Explain how you will check a health claim and where you would go for a checkup, an urgent problem and an emergency.
Part 7: Service and advocacy. Plan one act of health advocacy or service for your family, church or community.
Part 8: Faith and reflection. Apply at least two Scriptures from the King James Version to your plan and explain what you learned and your next step.
Part 9: Presentation plan. List five main points you would share in a three minute talk.""",
 rubric="""100 points. Part 1: 10 points. Part 2: 15 points. Part 3: 15 points. Part 4: 15 points. Part 5: 10 points. Part 6: 10 points. Part 7: 5 points. Part 8: 8 points. Part 9: 4 points. Grammar, conventions and respectful tone: 8 points. A score of 70 or above is passing.""")

FINAL_EXAM = [
 ("The four parts of health are physical, mental and emotional, social and:", ["Spiritual", "Financial", "Political", "Seasonal"], 0, "Whole person health includes spiritual health."),
 ("Half of your plate should be:", ["Fruits and vegetables", "Desserts", "Fried foods", "Soda"], 0, "MyPlate suggests half fruits and vegetables."),
 ("Teens need at least how much activity each day?", ["Sixty minutes", "Five minutes", "One hour per month", "None"], 0, "Daily activity supports health."),
 ("Teens need about how much sleep each night?", ["Eight to ten hours", "Three hours", "Five hours", "Fourteen hours"], 0, "Sleep supports learning, mood and growth."),
 ("To call or text the Suicide and Crisis Lifeline, dial:", ["988", "211", "311", "511"], 0, "988 connects to trained counselors."),
 ("The legal age to buy tobacco and nicotine products is:", ["Twenty one", "Sixteen", "Eighteen", "Fifteen"], 0, "The age is twenty one."),
 ("Pills bought online or from friends may contain:", ["Fentanyl", "Only vitamins", "Only sugar", "Nothing"], 0, "Counterfeit pills can be deadly."),
 ("Antibiotics treat:", ["Bacterial infections", "Colds", "The flu", "Any virus"], 0, "Antibiotics do not work on viruses."),
 ("Hands only CPR is performed at about how many compressions per minute?", ["100 to 120", "30", "60", "200"], 0, "Push hard and fast at that rate."),
 ("An upstander is someone who:", ["Stands with the person and reports bullying", "Joins the bully", "Ignores it", "Reposts it"], 0, "Upstanders take safe action."),
 ("Which is a warning sign of dating violence?", ["Controlling behavior and threats", "Respect", "Kindness", "Honesty"], 0, "Control is not love."),
 ("In the DECIDE model, the first step is to:", ["Define the problem", "Evaluate", "Decide", "Guess"], 0, "You begin by defining the problem."),
 ("Abstinence until marriage is:", ["The only certain way to avoid pregnancy and sexually transmitted infections", "Harmful", "Unknown", "Required by no one"], 0, "It is the expected standard and fully protective."),
 ("A reliable source of health information is:", ["The CDC or a doctor", "A rumor", "An unnamed post", "A miracle cure ad"], 0, "Credible sources use evidence."),
 ("1 Corinthians 6:19 calls the body:", ["The temple of the Holy Ghost", "A machine only", "Unimportant", "A tool for money"], 0, "Scripture calls us to honor the body."),
]
