"""Christian Ethics final module."""
FOCUS = ("Christian Ethics is a one semester course on how followers of Jesus decide what is right and live it out. Students study why ethics matters, the character of God, conscience, the Ten Commandments and the two great commandments, the fruit of the Spirit, and fair summaries of other ways of thinking about right and wrong. Students then apply Scripture to honesty and integrity, purity and self control, money and work, words, anger and forgiveness, the dignity of human life, justice and care for the poor, technology and artificial intelligence, and citizenship and conscience. Students practice respectful discussion and writing with evidence from the King James Version. The course ends with a final ethics portfolio and a final exam. Excellence, Faith, Purpose.")

FINAL_ASSESS = dict(t="Final Assessment: My Christian Ethics Portfolio",
 prompt="""Create a Christian Ethics portfolio of at least 600 words and prepare a short presentation of its main ideas. Use complete sentences and label each part. Do not name real private individuals or share private details. Micah 6:8 says, He hath shewed thee, O man, what is good; and what doth the LORD require of thee, but to do justly, and to love mercy, and to walk humbly with thy God?

Part 1: Foundation. Explain why Christians believe right and wrong rest on the character of God and the authority of Scripture, and explain the role of conscience.
Part 2: The great commandments. Explain the two great commandments and how the Ten Commandments apply to a modern situation.
Part 3: Character. Choose three fruit of the Spirit and write a plan to grow each through daily habits.
Part 4: Case study one. Describe a school or home situation involving honesty, purity, money or anger. Apply the DECIDE style steps: identify the problem, list options, test each by Scripture and love for neighbor, and choose the best response.
Part 5: Case study two. Describe a situation involving justice, technology or artificial intelligence. Explain what Scripture teaches and how a Christian should act.
Part 6: Other views. Compare one other way of thinking about right and wrong with the Christian view, with strengths and weaknesses, fairly and respectfully.
Part 7: Service. Plan one act of service or witness for your church or community and tell how you will speak with gentleness.
Part 8: Faith and reflection. Apply at least three Scriptures from the King James Version to your portfolio and explain what you learned and your next step.
Part 9: Presentation plan. List five main points you would share in a three minute talk.""",
 rubric="""100 points. Part 1: 10 points. Part 2: 10 points. Part 3: 10 points. Part 4: 15 points. Part 5: 15 points. Part 6: 10 points. Part 7: 5 points. Part 8: 10 points. Part 9: 5 points. Grammar, conventions and respectful tone: 10 points. A score of 70 or above is passing.""")

FINAL_EXAM = [
 ("Christian ethics asks first:", ["What does God require?", "What is popular?", "What is easy?", "What is profitable?"], 0, "God's will is the starting point."),
 ("People have dignity because they are made:", ["In the image of God", "By chance", "By law", "By wealth"], 0, "Genesis 1:27."),
 ("Conscience should be:", ["Trained by Scripture and the Holy Spirit", "Ignored", "Always trusted without question", "Silenced"], 0, "A trained conscience guides well."),
 ("Jesus summed up the law as love for God and:", ["Love for neighbor", "Love for rules", "Love for money", "Love for success"], 0, "Matthew 22:37 to 39."),
 ("The fruit of the Spirit is listed in:", ["Galatians 5", "Genesis 1", "Psalm 1", "Acts 1"], 0, "Galatians 5:22 and 23."),
 ("Relativism says right and wrong:", ["Depend on a person or culture", "Come only from God", "Never change", "Do not matter"], 0, "Relativism denies a universal standard."),
 ("Plagiarism is:", ["Presenting another person's work as your own", "Giving credit", "Editing", "Studying"], 0, "It is dishonest."),
 ("Ephesians 4:15 says to speak the truth:", ["In love", "Only when angry", "To win arguments", "Never"], 0, "Truth and love belong together."),
 ("1 Corinthians 6:19 calls the body:", ["The temple of the Holy Ghost", "A trophy", "Unimportant", "A tool for money"], 0, "Our bodies belong to God."),
 ("Stewardship means:", ["Managing what belongs to God", "Owning everything", "Wasting resources", "Avoiding work"], 0, "We manage on God's behalf."),
 ("Ephesians 4:32 teaches us to be:", ["Kind and forgiving", "Angry and proud", "Silent and cold", "Careless"], 0, "Forgive as God forgave in Christ."),
 ("Acts 17:26 says God made all nations of:", ["One blood", "Many origins", "Kings", "Soldiers"], 0, "All people share one human family."),
 ("An ethical rule for using artificial intelligence in schoolwork is to:", ["Follow school rules, check answers and give credit", "Copy it without reading", "Hide that you used it", "Trust every answer"], 0, "Honesty and verification matter."),
 ("Acts 5:29 applies when a law:", ["Requires sin", "Is inconvenient", "Is unpopular", "Is new"], 0, "Obey God rather than men only when commanded to sin."),
 ("James 1:22 says to be:", ["Doers of the word", "Hearers only", "Critics only", "Silent"], 0, "Faith must be lived."),
]
