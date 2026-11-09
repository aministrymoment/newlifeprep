"""United States Government final module: final assessment (position 4) and final exam (quiz position 16)."""

FINAL_ASSESS = dict(t="Final Assessment: Civic Action Report and Presentation",
 prompt="""Write a civic report of at least 500 words and prepare a short presentation of its main ideas. Choose one topic: (a) how a bill becomes a law, followed through one real or sample bill; (b) a landmark Supreme Court case and its effect on citizens; (c) a right in the Bill of Rights and how it protects people today; (d) how a local government in Broward County or Florida solves one community problem; or (e) a topic approved by your administrator. Write complete sentences and label each part. Proverbs 11:14 says, Where no counsel is, the people fall: but in the multitude of counsellors there is safety.

Part 1: Question and Thesis. State a clear question and a thesis about your topic.
Part 2: Sources. List at least three reliable sources, such as the Constitution, a government website, a court opinion or a news report, and tell how you judged each.
Part 3: The Report. Explain your topic with an introduction, at least three body paragraphs and a conclusion. Connect it to at least two principles of the Constitution, and name the branch or level of government involved.
Part 4: Scripture Connection. Connect your topic to a passage of Scripture in the King James Version and explain the link.
Part 5: Citizen Action Plan. Describe one peaceful, lawful action you can take as a citizen about your topic, such as registering to vote, writing to an official, attending a meeting or volunteering.
Part 6: Presentation Plan. Write a three part outline and an opening line for a three minute talk.""",
 rubric="""100 points. Part 1, question and thesis: 10 points. Part 2, sources: 10 points. Part 3, report content, accuracy and use of constitutional principles: 40 points. Part 4, Scripture connection: 8 points. Part 5, citizen action plan: 12 points. Part 6, presentation plan: 10 points. Grammar, conventions and respectful tone: 10 points. A score of 70 or above is passing."""
)

FINAL_EXAM = [
 ("Government gets its just powers from:", ["The consent of the governed", "A king", "The army", "The wealthy"], 0, "The Declaration of Independence states this principle."),
 ("The Articles of Confederation failed partly because Congress could not:", ["Tax the people", "Meet", "Elect a governor", "Print a flag"], 0, "The national government lacked the power to tax."),
 ("The Great Compromise created:", ["A House by population and a Senate with equal states", "A monarchy", "A national bank", "Two Presidents"], 0, "It balanced large and small states."),
 ("Separation of powers divides government into:", ["Three branches", "Two parties", "Five courts", "Four houses"], 0, "Legislative, executive and judicial branches."),
 ("The Bill of Rights was ratified in:", ["1791", "1776", "1865", "1920"], 0, "The first ten amendments became law in 1791."),
 ("An amendment is ratified by:", ["Three fourths of the states", "The President alone", "The Supreme Court", "A simple majority in Congress"], 0, "Article V requires three fourths of the states."),
 ("The Senate has:", ["100 members", "435 members", "50 members", "538 members"], 0, "Each state has two Senators."),
 ("A President must be at least:", ["35 years old", "25 years old", "30 years old", "40 years old"], 0, "Article II sets the minimum age at 35."),
 ("A candidate needs how many electoral votes to win?", ["270", "218", "100", "435"], 0, "A majority of 538 electors is 270."),
 ("Judicial review means courts can:", ["Decide if a law violates the Constitution", "Write laws", "Declare war", "Collect taxes"], 0, "Marbury v. Madison established it in 1803."),
 ("Powers shared by nation and states are called:", ["Concurrent powers", "Reserved powers", "Delegated powers", "Impeachment powers"], 0, "Taxing and building roads are examples."),
 ("The Nineteenth Amendment:", ["Gave women the right to vote", "Ended slavery", "Set the voting age at 18", "Banned poll taxes"], 0, "It was ratified in 1920."),
 ("The Establishment Clause means government may not:", ["Set up an official church", "Protect religion", "Tax anyone", "Hold elections"], 0, "It prohibits an official national religion."),
 ("A good poll uses:", ["A random, representative sample", "Leading questions", "Only volunteers", "No margin of error"], 0, "Fair sampling and wording make a reliable poll."),
 ("Jesus said, Render therefore unto Caesar the things which are Caesar's, and unto God the things that are God's, in:", ["Matthew 22:21", "Romans 13:1", "Acts 5:29", "Titus 3:1"], 0, "Jesus taught duty to both government and God."),
]
