"""United States Government, Unit 2: The Three Branches and Federalism. Florida civics standards cited at strand level (SS.912.CG); recheck exact wording at CPALMS."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."

UNIT2 = dict(
 title="Unit 2: The Three Branches and Federalism",
 std="SS.912.CG.3.1, SS.912.CG.4.1, SS.912.CG.4.2, SS.912.CG.4.3, SS.912.CG.5.1",
 topics=[
 dict(t="2.1 Congress: The Legislative Branch", std="SS.912.CG.4.1, SS.912.CG.4.2",
 body="""Article I of the Constitution creates Congress, the legislative branch, which has two houses. The House of Representatives has 435 voting members, apportioned by state population, who serve two year terms. A Representative must be at least 25 years old, a citizen for seven years, and a resident of the state. The Senate has 100 members, two from each state, who serve six year terms. A Senator must be at least 30 years old and a citizen for nine years.

Congress has the power to make laws, to tax and spend, to borrow money, to regulate commerce, to coin money, to declare war and to raise an army and navy. The Senate also confirms presidential appointments and ratifies treaties by a two thirds vote. The House begins all bills for raising revenue. Only the House can impeach, which means to accuse an official of wrongdoing, and only the Senate can try the case, with a two thirds vote needed to convict.

To become a law, a bill is introduced, sent to a committee, debated and passed by both houses, and then sent to the President. The President may sign it or veto it. Congress can override a veto with a two thirds vote in each house.

Proverbs 11:14 says, Where no counsel is, the people fall: but in the multitude of counsellors there is safety. A body of many voices is slower, but it protects against hasty or selfish decisions.

Your task: (1) Compare the House and the Senate in size, term and age requirement. (2) Describe how a bill becomes a law in five steps. (3) Explain impeachment.""",
 script="""Welcome to the first branch. Listen, Article I of the Constitution creates Congress, the legislative branch, and it has two houses.

The House of Representatives has four hundred thirty five voting members, based on state population. They serve two year terms, and they must be at least twenty five. The Senate has one hundred members, two from every state. They serve six year terms and must be at least thirty.

Now watch this. Congress has the power to make laws, tax and spend, borrow money, regulate commerce, coin money, and declare war. The Senate confirms presidential appointments and approves treaties by a two thirds vote. The House can impeach, which means to accuse an official of wrongdoing. The Senate holds the trial, and it takes two thirds to convict.

Look at how a bill becomes a law. It is introduced. A committee studies it. Both houses debate and pass it. The President signs or vetoes it. And Congress can override a veto with two thirds of each house.

Proverbs 11:14 says, in the multitude of counsellors there is safety. Many voices make the process slower, but they guard against hasty or selfish decisions.

Your task is to compare the House and the Senate, describe how a bill becomes a law, and explain impeachment. Take the four question check. Wise counsel protects the people.""" + CLOSE,
 quiz=[
 ("How many members does the Senate have?", ["100", "435", "50", "538"], 0, "Each state has two Senators, so there are 100."),
 ("Representatives serve terms of:", ["Two years", "Four years", "Six years", "Ten years"], 0, "House members serve two year terms."),
 ("Only the House can:", ["Impeach an official", "Ratify treaties", "Confirm judges", "Try an impeachment case"], 0, "The House impeaches and the Senate tries the case."),
 ("Congress can override a veto with:", ["A two thirds vote in each house", "A simple majority", "The Supreme Court", "The governor"], 0, "An override requires two thirds of both houses."),
 ]),
 dict(t="2.2 The President: The Executive Branch", std="SS.912.CG.4.1, SS.912.CG.4.2",
 body="""Article II vests the executive power in the President, whose job is to carry out and enforce the laws. A President must be a natural born citizen, at least 35 years old, and a resident of the United States for 14 years. The term is four years, and the Twenty Second Amendment limits a President to two elected terms. The Twenty Fifth Amendment explains what happens if the President dies, resigns or becomes unable to serve, with the Vice President taking over.

The President's powers include serving as commander in chief of the armed forces, signing or vetoing bills, making treaties with the approval of the Senate, appointing judges, ambassadors and Cabinet members with Senate confirmation, and granting pardons for federal crimes. The President also gives the State of the Union address and may call Congress into special session.

The executive branch includes the Vice President, the Cabinet and more than a dozen executive departments, such as State, Treasury, Defense, Justice and Education, plus independent agencies. These agencies write rules and carry out the laws.

The President is elected through the Electoral College. Each state has electors equal to its House seats plus its two Senate seats, for a total of 538, and a candidate needs 270 to win.

1 Timothy 2:1 and 2 urge us to make prayers and intercessions for kings and all that are in authority, that we may lead a quiet and peaceable life in all godliness and honesty.

Your task: (1) List the requirements to be President. (2) Name four powers of the President. (3) Explain the Electoral College in two sentences.""",
 script="""Now we turn to the second branch. Listen, Article II places the executive power in the President, whose job is to carry out and enforce the laws.

To be President, a person must be a natural born citizen, at least thirty five years old, and a resident for fourteen years. The term is four years, and the Twenty Second Amendment limits a President to two elected terms. The Twenty Fifth Amendment says what happens if a President dies, resigns or cannot serve. The Vice President takes over.

Now watch this. The President is commander in chief of the armed forces. The President signs or vetoes bills, makes treaties with Senate approval, appoints judges, ambassadors and Cabinet members with Senate confirmation, and grants pardons for federal crimes.

The executive branch also includes the Vice President, the Cabinet and the executive departments like State, Treasury, Defense, Justice and Education.

Look at how we elect a President. The Electoral College has five hundred thirty eight electors, and a candidate needs two hundred seventy to win. Each state gets electors equal to its House seats plus two Senate seats.

First Timothy 2 tells us to pray for all who are in authority, that we may lead a quiet and peaceable life. Your task is to list the requirements, name four powers, and explain the Electoral College. Take the four question check. Pray for your leaders.""" + CLOSE,
 quiz=[
 ("The President serves a term of:", ["Four years", "Two years", "Six years", "Eight years"], 0, "The term is four years, limited to two elected terms."),
 ("Who is commander in chief of the armed forces?", ["The President", "The Speaker of the House", "The Chief Justice", "The Senate Majority Leader"], 0, "Article II names the President commander in chief."),
 ("How many electoral votes does a candidate need to win?", ["270", "218", "435", "100"], 0, "There are 538 electoral votes and 270 is a majority."),
 ("Cabinet members are appointed by the President and:", ["Confirmed by the Senate", "Elected by the House", "Chosen by the Supreme Court", "Chosen by governors"], 0, "The Senate confirms presidential appointments."),
 ]),
 dict(t="2.3 The Courts: The Judicial Branch", std="SS.912.CG.4.1, SS.912.CG.4.3",
 body="""Article III creates the Supreme Court and allows Congress to create lower courts. The federal court system has three levels: district courts, where most federal cases begin; circuit courts of appeals, which review decisions of district courts; and the Supreme Court, the highest court. The Supreme Court has nine justices, one Chief Justice and eight Associate Justices, who are nominated by the President, confirmed by the Senate, and serve for life during good behavior. Life terms protect judges from political pressure.

Courts decide two main types of cases. Criminal cases involve a person accused of breaking the law. Civil cases involve disputes between people or groups. Federal courts hear cases about the Constitution, federal law, treaties and disputes between states.

The Court's greatest power is judicial review, the power to decide whether a law or government action violates the Constitution. The Court claimed this power in Marbury v. Madison in 1803, in a decision written by Chief Justice John Marshall. Other landmark cases include Brown v. Board of Education (1954), which ended legal segregation in public schools, and Gideon v. Wainwright (1963), which guaranteed a lawyer to poor defendants in serious criminal cases.

Scripture calls for fair judgment. Deuteronomy 16:19 says, Thou shalt not wrest judgment; thou shalt not respect persons, neither take a gift.

Your task: (1) Name the three levels of federal courts. (2) Define judicial review and the case that established it. (3) Choose one landmark case and tell why it mattered.""",
 script="""Now we study the third branch. Listen, Article III creates the Supreme Court and lets Congress create lower courts.

The federal court system has three levels. District courts, where most federal cases begin. Circuit courts of appeals, which review those decisions. And the Supreme Court, the highest court in the nation. It has nine justices, one Chief Justice and eight Associate Justices. They are nominated by the President, confirmed by the Senate, and serve for life during good behavior. Life terms protect judges from political pressure.

Now watch this. Criminal cases involve a person accused of breaking the law. Civil cases are disputes between people or groups.

Look at the Court's greatest power, judicial review. That is the power to decide whether a law or government action violates the Constitution. The Court claimed it in Marbury versus Madison in 1803, in a decision by Chief Justice John Marshall.

Other landmark cases. Brown versus Board of Education in 1954 ended legal segregation in public schools. Gideon versus Wainwright in 1963 guaranteed a lawyer to poor defendants in serious criminal cases.

Deuteronomy 16:19 says, Thou shalt not wrest judgment; thou shalt not respect persons. Your task is to name the three levels, define judicial review, and explain one landmark case. Take the four question check. Justice must be fair to all.""" + CLOSE,
 quiz=[
 ("How many justices serve on the Supreme Court?", ["Nine", "Seven", "Twelve", "Fifteen"], 0, "The Court has one Chief Justice and eight Associate Justices."),
 ("Judicial review is the power to:", ["Decide if a law violates the Constitution", "Write laws", "Veto bills", "Declare war"], 0, "Marbury v. Madison established it in 1803."),
 ("Federal judges are:", ["Nominated by the President and confirmed by the Senate", "Elected by voters", "Chosen by the House", "Chosen by governors"], 0, "This is the process set by Article II and Article III."),
 ("Brown v. Board of Education (1954) ended:", ["Legal segregation in public schools", "Slavery", "The draft", "The income tax"], 0, "The Court ruled that separate schools were unequal."),
 ]),
 dict(t="2.4 Federalism and Florida Government", std="SS.912.CG.4.1, SS.912.CG.5.1",
 body="""Federalism divides power between the national government and the state governments. Delegated or enumerated powers belong to the national government, such as coining money, regulating trade between states and declaring war. Reserved powers belong to the states under the Tenth Amendment, such as running schools and elections and licensing professionals. Concurrent powers are shared, such as taxing, building roads and making laws. The Supremacy Clause in Article VI makes the Constitution and federal laws the supreme law of the land, and the Supreme Court confirmed national power in McCulloch v. Maryland in 1819.

Florida has its own government with three branches. The current Florida Constitution was adopted in 1968. The Legislature has a Senate of 40 members and a House of 120 members. The Governor leads the executive branch and serves four year terms, with a limit of two consecutive terms. Florida also elects a Cabinet of the Attorney General, the Chief Financial Officer and the Commissioner of Agriculture. The Florida Supreme Court has seven justices.

Beneath the state are 67 counties and many cities, which handle local matters such as police, fire service, zoning and local roads. Local government is closest to the people, so citizens can speak at meetings, vote and serve.

Jeremiah 29:7 says, Seek the peace of the city whither I have caused you to be carried away captives, and pray unto the LORD for it: for in the peace thereof shall ye have peace.

Your task: (1) Define delegated, reserved and concurrent powers with one example of each. (2) Describe the three branches of Florida government. (3) Name one way you can take part in local government.""",
 script="""Now we study how power is shared. Listen, federalism divides power between the national government and the states.

Delegated powers belong to the national government, like coining money, regulating trade between states and declaring war. Reserved powers belong to the states under the Tenth Amendment, like running schools and elections. Concurrent powers are shared, like taxing and building roads. The Supremacy Clause says the Constitution and federal laws are the supreme law of the land.

Now watch this. Florida has its own government with three branches. The Florida Constitution was adopted in 1968. The Legislature has a forty member Senate and a one hundred twenty member House. The Governor serves four year terms, with a limit of two in a row. Florida also elects a Cabinet, the Attorney General, the Chief Financial Officer and the Commissioner of Agriculture. The Florida Supreme Court has seven justices.

Look closer to home. Florida has sixty seven counties and many cities. They handle police, fire service, zoning and local roads. Local government is closest to you. You can speak at a meeting, vote, and serve.

Jeremiah 29:7, seek the peace of the city, and pray unto the LORD for it. Your task is to define the three kinds of power, describe Florida's three branches, and name one way you can take part locally. Take the four question check. Serve where you live.""" + CLOSE,
 quiz=[
 ("Powers shared by the national and state governments are:", ["Concurrent powers", "Delegated powers", "Reserved powers only", "Implied powers only"], 0, "Taxing and building roads are concurrent powers."),
 ("The Tenth Amendment reserves certain powers to:", ["The states and the people", "Congress alone", "The President", "The Supreme Court"], 0, "Powers not given to the nation belong to the states or the people."),
 ("How many counties does Florida have?", ["67", "50", "120", "40"], 0, "Florida has 67 counties."),
 ("The Supremacy Clause makes the Constitution and federal law:", ["The supreme law of the land", "Optional for states", "Subject to county votes", "Weaker than state law"], 0, "Article VI sets this rule."),
 ]),
 ],
 assess=dict(t="Assessment 2: The Three Branches and Federalism",
 prompt="""Write a report of at least 300 words on the structure of American government. Use complete sentences and label each part. Isaiah 33:22 says, For the LORD is our judge, the LORD is our lawgiver, the LORD is our king; he will save us.

Part 1: Describe the legislative branch: the two houses, their size, terms and key powers.
Part 2: Describe the executive branch: the requirements and powers of the President, and the Electoral College.
Part 3: Describe the judicial branch: the court levels, judicial review and one landmark case.
Part 4: Explain two checks that one branch has on another, and why the founders wanted them.
Part 5: Explain federalism with examples of delegated, reserved and concurrent powers, and name two features of Florida government.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 20 points. Part 3: 20 points. Part 4: 15 points. Part 5: 20 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 2: Serving Through Public Office",
 prompt="""Write a post of at least 120 words that (1) tells which branch of government you think is most important to daily life and why, (2) describes a local or state office, such as city commissioner, school board member or sheriff, that you would like to understand better, (3) explains qualities you want in a public official, and (4) connects your answer to Exodus 18:21, which says, Moreover thou shalt provide out of all the people able men, such as fear God, men of truth, hating covetousness. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why is it good that judges serve for life, and what is the risk? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("Congress is the:", ["Legislative branch", "Executive branch", "Judicial branch", "Federal bank"], 0, "Article I creates Congress to make laws."),
 ("Each state has how many Senators?", ["Two", "One", "Four", "It depends on population"], 0, "Every state has two Senators."),
 ("Who can sign or veto a bill?", ["The President", "The Chief Justice", "The Speaker of the House", "The Secretary of State"], 0, "The President signs or vetoes bills."),
 ("The Electoral College has:", ["538 electors", "435 electors", "100 electors", "270 electors in total"], 0, "A candidate needs 270 of the 538."),
 ("Marbury v. Madison established:", ["Judicial review", "The income tax", "Presidential pardons", "Impeachment"], 0, "The Court claimed the power to review laws in 1803."),
 ("Supreme Court justices serve:", ["For life during good behavior", "Four year terms", "Six year terms", "Until age 50"], 0, "Life tenure protects judges from pressure."),
 ("Powers reserved to the states come from the:", ["Tenth Amendment", "First Amendment", "Nineteenth Amendment", "Preamble"], 0, "The Tenth Amendment reserves powers to the states and the people."),
 ("The Florida Legislature consists of:", ["A 40 member Senate and a 120 member House", "One chamber of 67 members", "A 100 member Senate", "A 435 member House"], 0, "The Florida Senate has 40 members and the House has 120."),
 ])
