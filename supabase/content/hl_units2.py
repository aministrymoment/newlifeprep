"""Health Education, Unit 2: Risk and Prevention. Florida health standards cited at strand level; recheck exact wording at CPALMS."""
from hl_units1 import CLOSE

UNIT2 = dict(
 title="Unit 2: Risk and Prevention",
 std="HE.912.C.1, HE.912.C.2, HE.912.B.3, HE.912.B.5, HE.912.P.8",
 topics=[
 dict(t="2.1 Alcohol, Tobacco, Vaping and Drugs", std="HE.912.C.1, HE.912.C.2, HE.912.B.4, HE.912.B.5",
 body="""Substances change how the brain and body work. Alcohol slows the brain, hurts judgment and coordination, and is illegal for anyone under twenty one. Tobacco and vaping products contain nicotine, which is highly addictive and can harm the developing teen brain, affecting attention, learning and mood. In the United States and in Florida, the legal age to buy tobacco and nicotine products is twenty one. Marijuana can affect memory and learning and is not legal for teens. Misusing prescription medicine, such as opioids or stimulants, is dangerous. Pills bought from friends or online can be counterfeit and may contain fentanyl, a very strong drug that can cause death in a tiny amount.

Addiction is a brain condition in which a person feels unable to stop using even when it causes harm. Warning signs include needing more of a substance, failed attempts to quit, and loss of interest in other things. Treatment and support work. Proverbs 20:1 says, Wine is a mocker, strong drink is raging: and whosoever is deceived thereby is not wise. Ephesians 5:18 says, be not drunk with wine, wherein is excess; but be filled with the Spirit.

Refusal skills help you say no: say no firmly, give a reason, suggest something else, and leave. Proverbs 1:10 says, My son, if sinners entice thee, consent thou not.

Worked example: a friend offers a vape. Say, No thanks, I am good, and move to another group. Common mistake: believing that vaping is harmless because it has no smoke.

Your task: (1) List three harms of nicotine or alcohol. (2) Explain why pills from friends are dangerous. (3) Write a refusal line and a trusted adult you could tell.""",
 script="""Welcome back. Listen, the choices you make about substances can shape your future for good or for harm.

Substances change how the brain and body work. Alcohol slows the brain and hurts judgment, and it is illegal under twenty one. Tobacco and vaping products contain nicotine, which is highly addictive and can harm the teen brain. The legal age to buy them is twenty one. Misusing prescription medicine is dangerous, and pills from friends or online can be counterfeit and may contain fentanyl, which can kill in a tiny amount.

Now watch this. Addiction is a brain condition where a person cannot stop even when it causes harm. Warning signs are needing more, failed attempts to quit and losing interest in other things. Help and treatment work.

Proverbs 20:1 says, Wine is a mocker, strong drink is raging. Proverbs 1:10 says, My son, if sinners entice thee, consent thou not.

Refusal skills: say no firmly, give a reason, suggest something else and leave.

Your task is to list three harms, explain pill danger and write a refusal line. Take the four question check.""" + CLOSE,
 quiz=[
 ("The legal age to buy tobacco and nicotine products is:", ["Twenty one", "Sixteen", "Eighteen", "Fourteen"], 0, "Federal and Florida law set the age at twenty one."),
 ("Nicotine is harmful to teens because it is:", ["Highly addictive and affects the developing brain", "Harmless", "A vitamin", "Good for focus"], 0, "Nicotine affects teen brain development."),
 ("Pills bought from friends or online may contain:", ["Fentanyl, a deadly drug", "Only vitamins", "Safe medicine", "Candy"], 0, "Counterfeit pills can be deadly."),
 ("A good refusal skill is to:", ["Say no firmly and leave", "Say maybe", "Try it once", "Laugh it off"], 0, "A clear no with a plan protects you."),
 ]),
 dict(t="2.2 Disease Prevention and Immunity", std="HE.912.C.1, HE.912.B.7, HE.912.P.8",
 body="""Diseases are either communicable, spread from person to person, or noncommunicable, such as heart disease and diabetes, which are not spread. Pathogens are germs that cause communicable disease: bacteria, viruses, fungi and parasites. Germs spread by touch, droplets in the air, contaminated food or water, insect bites and body fluids.

Your body defends itself with skin, mucus, white blood cells and antibodies. Vaccines train the immune system to recognize a germ before you meet it, and they have prevented many serious diseases. Talk with a parent and a doctor about which vaccines you need. Antibiotics treat bacterial infections, not viral ones such as colds and flu, and using them wrongly makes germs resistant.

Prevent illness by washing hands, covering coughs, staying home when sick, not sharing drinks or personal items, handling food safely, getting checkups and sleeping well. Infections that spread through sexual contact, including HIV, are avoided most surely by abstinence until marriage and faithfulness in marriage. HIV can also spread through shared needles, so never share needles. Anyone who has questions or symptoms should talk with a parent or doctor. Proverbs 22:3 says, A prudent man foreseeth the evil, and hideth himself: but the simple pass on, and are punished.

Worked example: a classmate has the flu. Wash your hands, avoid sharing cups, and get rest if you feel ill. Common mistake: taking antibiotics for a cold. They do not work on viruses.

Your task: (1) Define communicable and noncommunicable disease and give an example of each. (2) List four ways to prevent infection. (3) Explain how vaccines work.""",
 script="""Welcome back. Listen, prevention is wise. Proverbs 22:3 says, A prudent man foreseeth the evil, and hideth himself.

Diseases are communicable, spread from person to person, or noncommunicable, like heart disease and diabetes. Germs called pathogens, such as bacteria, viruses, fungi and parasites, cause communicable disease. They spread by touch, droplets in the air, contaminated food or water, insect bites and body fluids.

Now watch this. Your body defends itself with skin, mucus, white blood cells and antibodies. Vaccines train your immune system to recognize a germ before you meet it. Talk with a parent and a doctor about the vaccines you need. Antibiotics treat bacteria, not viruses like colds and flu.

To prevent illness, wash your hands, cover coughs, stay home when sick, do not share drinks, handle food safely, get checkups and sleep well. Infections spread through sexual contact, including HIV, are avoided most surely by abstinence until marriage and faithfulness in marriage. HIV can also spread through shared needles, so never share needles. Ask a parent or doctor if you have questions.

Your task is to define the two kinds of disease, list four prevention steps and explain vaccines. Take the four question check.""" + CLOSE,
 quiz=[
 ("A communicable disease is one that:", ["Spreads from person to person", "Is never serious", "Cannot be treated", "Only affects adults"], 0, "Communicable diseases are spread by germs."),
 ("Antibiotics work against:", ["Bacterial infections", "Colds and flu", "All viruses", "Allergies"], 0, "They do not work on viruses."),
 ("Vaccines help the body by:", ["Training the immune system to recognize a germ", "Replacing food", "Stopping sleep", "Curing every illness"], 0, "Vaccines prepare the immune system."),
 ("Which is a noncommunicable disease?", ["Diabetes", "The flu", "A cold", "Strep throat"], 0, "Diabetes does not spread from person to person."),
 ]),
 dict(t="2.3 Safety, Injury Prevention and First Aid", std="HE.912.C.1, HE.912.B.7, HE.912.P.8",
 body="""Injuries are a leading cause of death for teens, and many can be prevented. Wear a seat belt every time. Never drive distracted, impaired or drowsy. Wear helmets for biking, skating and contact sports. Learn to swim and never swim alone. Stay away from weapons and tell an adult if you see one. Test smoke alarms, know two exits from every room and never leave cooking unattended. Proverbs 27:12 says, A prudent man foreseeth the evil, and hideth himself.

In an emergency, stay calm, make sure the scene is safe, and call 911. Give your location, say what happened and stay on the line. For bleeding, apply firm direct pressure with a clean cloth and do not remove it. For a burn, cool it with running water for several minutes. For choking in an adult, give abdominal thrusts. A suspected concussion needs a medical visit, so do not return to play. For poison, call the Poison Help line.

Cardiopulmonary resuscitation, or CPR, can save a life when a heart stops. Hands only CPR for an adult who collapses: call 911, push hard and fast in the center of the chest at 100 to 120 compressions per minute, and keep going until help arrives. If an automated external defibrillator, or AED, is nearby, turn it on and follow its voice prompts. Florida schools teach CPR awareness, and a certified class from a recognized organization gives hands on practice.

Worked example: a person collapses and is not breathing. Shout for help, call 911, start compressions, and send someone for the AED. Common mistake: waiting to see if the person wakes up.

Your task: (1) List five safety habits. (2) Write the steps of Hands only CPR. (3) Describe what to tell the 911 operator.""",
 script="""Welcome back. Listen, one of the best things you can do is to be prepared. Proverbs 27:12 says, A prudent man foreseeth the evil.

Many injuries can be prevented. Wear a seat belt every time. Never drive distracted, impaired or drowsy. Wear a helmet for biking, skating and contact sports. Learn to swim and never swim alone. Know two exits from every room.

Now watch this. In an emergency, stay calm, make sure the scene is safe and call 911. Give your location, say what happened and stay on the line. For bleeding, press firmly with a clean cloth. For a burn, cool it with running water. For a suspected concussion, see a doctor.

CPR can save a life. For an adult who collapses, call 911. Push hard and fast in the center of the chest, one hundred to one hundred twenty times a minute, and keep going until help arrives. If an AED is nearby, turn it on and follow the voice prompts. A certified class gives you hands on practice.

Your task is to list five safety habits, write the steps of Hands only CPR and describe what to tell the operator. Take the four question check.""" + CLOSE,
 quiz=[
 ("What number do you call in an emergency?", ["911", "311", "211", "511"], 0, "911 reaches emergency services."),
 ("Hands only CPR compressions are about:", ["100 to 120 per minute", "20 per minute", "60 per minute", "200 per minute"], 0, "Push hard and fast at that rate."),
 ("For heavy bleeding, you should:", ["Apply firm direct pressure with a clean cloth", "Remove the cloth often", "Ignore it", "Apply no pressure"], 0, "Direct pressure slows bleeding."),
 ("An AED is used to:", ["Restart a normal heart rhythm with a shock when needed", "Stop bleeding", "Cool a burn", "Treat a cold"], 0, "AEDs give voice prompts and deliver a shock when needed."),
 ]),
 dict(t="2.4 Violence, Bullying and Online Safety", std="HE.912.C.2, HE.912.B.4, HE.912.B.5, HE.912.P.8",
 body="""Violence and bullying harm health. Bullying is repeated unwanted behavior meant to hurt, and it can be physical, verbal, social or online. Cyberbullying uses phones and the internet. Bullying and harassment can lead to anxiety, poor sleep and trouble at school. Ephesians 4:32 says, And be ye kind one to another, tenderhearted, forgiving one another, even as God for Christ's sake hath forgiven you.

If you are bullied: stay calm, do not retaliate, save messages, block the account, and tell a trusted adult. If you see bullying, be an upstander: stand with the person, do not join in, and report it. Florida law requires schools to have policies against bullying and harassment.

Online safety: keep your accounts private, use strong passwords, never share personal information, do not meet strangers from the internet, and think before you post because content can last. Sending or asking for private pictures is dangerous, can be illegal for minors and can be used to hurt you. Anyone who pressures you online should be reported to a parent, school or law enforcement. Predators sometimes pretend to be peers. Talk to a trusted adult if something feels wrong.

Dating violence is controlling or harming a partner. Warning signs are jealousy, isolating you, checking your phone, threats, pushing or humiliating you. Love does not hurt or control. Teens can get help from a trusted adult, a counselor, or the National Domestic Violence Hotline.

Worked example: a classmate is mocked in a group chat. Do not reply with a joke. Send a kind private message, save the evidence and report it. Common mistake: staying silent because it is not about you.

Your task: (1) Define bullying and cyberbullying. (2) List three online safety rules. (3) Write two signs of an unhealthy relationship and who you would tell.""",
 script="""Welcome back. Listen, every person is made in the image of God and deserves to be safe and treated with respect.

Bullying is repeated unwanted behavior meant to hurt. It can be physical, verbal, social or online. Cyberbullying happens through phones and the internet. It can lead to anxiety, poor sleep and trouble at school. Ephesians 4:32 says, Be ye kind one to another, tenderhearted, forgiving one another.

Now watch this. If you are bullied, stay calm, do not retaliate, save the messages, block the account and tell a trusted adult. If you see bullying, be an upstander. Stand with the person, do not join in and report it.

Online, keep accounts private, use strong passwords, never share personal information and never meet strangers from the internet. Think before you post. Sending or asking for private pictures is dangerous and can be illegal for minors. Predators sometimes pretend to be peers.

Dating violence is controlling or harming a partner. Warning signs are jealousy, isolating you, threats and humiliation. Love does not hurt or control.

Your task is to define bullying, list three online rules and name two signs of an unhealthy relationship. Take the four question check.""" + CLOSE,
 quiz=[
 ("Cyberbullying is bullying that happens:", ["Through phones and the internet", "Only at school", "Only in person", "Only at night"], 0, "Online harassment is cyberbullying."),
 ("An upstander:", ["Stands with the person and reports bullying", "Joins in", "Watches silently", "Spreads the post"], 0, "Upstanders support others and report."),
 ("Which is a warning sign of dating violence?", ["Jealousy, isolating you and checking your phone", "Respecting your friends", "Kind words", "Honest talk"], 0, "Control is a warning sign."),
 ("If a stranger pressures you online, you should:", ["Report it to a trusted adult", "Meet them", "Send personal pictures", "Share your address"], 0, "Tell a trusted adult right away."),
 ]),
 ],
 assess=dict(t="Assessment 2: Risk and Prevention",
 prompt="""Write a report of at least 250 words on prevention and safety. Use complete sentences and label each part. Do not include private details about yourself or others. Proverbs 22:3 says, A prudent man foreseeth the evil, and hideth himself: but the simple pass on, and are punished.

Part 1: Explain three harms of alcohol, nicotine or other drugs and write a refusal plan with a trusted adult you would tell.
Part 2: Explain the difference between communicable and noncommunicable disease and describe four ways to prevent infection.
Part 3: Write a home safety and emergency plan, including what to say when you call 911 and the steps of Hands only CPR.
Part 4: Describe bullying, cyberbullying and three online safety rules, and tell how an upstander helps.
Part 5: Explain how Scripture encourages prudence, kindness and protection of others.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 20 points. Part 3: 25 points. Part 4: 20 points. Part 5: 10 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 2: Choosing Prudence",
 prompt="""Write a post of at least 120 words that (1) describes one risk teens face today, (2) explains a refusal or safety skill that helps, (3) tells how you can support a friend who feels pressured, and (4) connects your answer to Proverbs 22:3 or Proverbs 1:10. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why is it wise to prepare before an emergency happens? Do not share private details about yourself or others."""),
 unit_quiz=[
 ("Which is illegal for anyone under twenty one in Florida?", ["Buying alcohol", "Drinking water", "Eating vegetables", "Sleeping"], 0, "The legal age for alcohol is twenty one."),
 ("Nicotine can harm teens by affecting the:", ["Developing brain", "Hair color", "Eye color", "Height only"], 0, "Nicotine affects attention, learning and mood."),
 ("Pills from a friend might contain:", ["Fentanyl", "Only sugar", "Only vitamins", "Nothing"], 0, "Counterfeit pills are deadly."),
 ("A vaccine works by:", ["Training the immune system", "Cooling a burn", "Stopping bleeding", "Replacing sleep"], 0, "It prepares the body to recognize a germ."),
 ("Antibiotics treat:", ["Bacterial infections", "Colds", "Flu", "All viruses"], 0, "They are not for viruses."),
 ("Hands only CPR begins with:", ["Calling 911 then pushing hard and fast in the center of the chest", "Waiting", "Giving water", "Shaking the person"], 0, "Call 911 and start compressions."),
 ("A cyberbully uses:", ["Phones and the internet to hurt others", "Only fists", "Only notes", "Only voice calls"], 0, "Cyberbullying happens online."),
 ("A warning sign of an unhealthy relationship is:", ["Jealous control and threats", "Respect", "Trust", "Honesty"], 0, "Control and threats are not love."),
 ],
)
