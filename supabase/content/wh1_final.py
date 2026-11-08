"""World History 1 final module: final assessment (position 7) and final exam (quiz position 31)."""

FINAL_ASSESS = dict(t="Final Assessment: Historical Inquiry Project",
 prompt="""Complete a historical inquiry project on one turning point from this course. Choose from: the fall of Constantinople, the Magna Carta, the Black Death, the rise of Mali under Mansa Musa, the printing press, the Reformation, the Columbian Exchange, the French Revolution or the Industrial Revolution. Write complete sentences and label each part. Proverbs 25:2 says, It is the glory of God to conceal a thing: but the honour of kings is to search out a matter.

Part 1: Question and Timeline. State a clear historical question about your turning point. Make a timeline of at least eight dates, marked BC or AD, that show the causes and effects.
Part 2: Sources. Identify at least one primary source and one secondary source about your topic (a sample is acceptable if you cannot find a real one, and you must say it is a sample). Tell who made each, when, why, and what each leaves out.
Part 3: Causes. Explain at least two long term causes and one immediate trigger.
Part 4: Effects. Explain at least three effects on religion, government, economy, learning or daily life.
Part 5: Competing Interpretations. Describe how two historians or viewpoints might disagree about your turning point and tell which argument you find stronger and why.
Part 6: Identity and Connections. Tell how the turning point still shapes the world, your community or your own faith today, and connect it to another unit in this course.
Part 7: Reflection. In at least 100 words, explain what this course taught you about God's rule over the times and seasons, honest use of evidence, and how to treat people of every nation with dignity. Use Daniel 2:21, which says, And he changeth the times and the seasons: he removeth kings, and setteth up kings: he giveth wisdom unto the wise, and knowledge to them that know understanding.""",
 rubric="""200 points. Part 1, question and timeline: 24 points. Part 2, sources: 30 points. Part 3, causes: 28 points. Part 4, effects: 30 points. Part 5, competing interpretations: 32 points. Part 6, identity and connections: 28 points. Part 7, reflection: 20 points. Clear organization and complete sentences: 8 points. A score of 140 or above is passing."""
)

FINAL_EXAM = [
 ("A source created during the time being studied is a:", ["Primary source", "Secondary source", "Theory", "Timeline"], 0, "Primary sources come from the period under study."),
 ("Checking a source against other sources is called:", ["Corroboration", "Imitation", "Conquest", "Migration"], 0, "Corroboration tests whether a source can be trusted."),
 ("The Byzantine capital, built by Constantine, was:", ["Constantinople", "Rome", "Alexandria", "Athens"], 0, "Constantine dedicated it in 330."),
 ("The Great Schism of 1054 divided the Church into:", ["Roman Catholic and Eastern Orthodox", "Sunni and Shia", "Lutheran and Calvinist", "Jesuit and Benedictine"], 0, "Rome and Constantinople separated."),
 ("The Islamic calendar begins with the:", ["Hijra in 622", "Fall of Rome", "Crusades", "Founding of Baghdad"], 0, "Muhammad moved from Mecca to Medina in 622."),
 ("The Abbasid dynasty ruled from the capital of:", ["Baghdad", "Damascus", "Cairo", "Tours"], 0, "Baghdad was founded in 762."),
 ("In feudalism, a lord gave land called a fief to a:", ["Vassal", "Serf only", "Pope", "Merchant"], 0, "Land was granted in exchange for loyalty and service."),
 ("The Magna Carta of 1215 helped establish that:", ["The king is under the law", "Peasants rule", "Parliament is forbidden", "The Pope appoints kings"], 0, "It limited the power of King John."),
 ("The Black Death of 1347 to 1351 was a:", ["Plague that killed a large share of Europe", "War between England and France", "Council of the Church", "Religious schism"], 0, "The plague changed European society and economy."),
 ("In Japan, the military ruler who held real power was the:", ["Shogun", "Daimyo", "Priest", "Merchant"], 0, "The emperor was a symbol and the shogun ruled."),
 ("Mansa Musa, ruler of Mali, is known for his:", ["Pilgrimage to Mecca in 1324", "Voyage to America", "Conquest of Constantinople", "Writing of the Ninety Five Theses"], 0, "His gold and generosity were famous."),
 ("The Aztec capital Tenochtitlan was built:", ["On an island in Lake Texcoco", "On the Bosporus", "In the Andes", "On the Niger River"], 0, "It stood where Mexico City stands now."),
 ("The Inca recorded numbers and records using:", ["Quipu", "Glyph books", "Printed paper", "Clay tablets from Sumer"], 0, "Knotted cords served as records."),
 ("Martin Luther began the Reformation in:", ["1517", "1066", "1215", "1789"], 0, "He posted the Ninety Five Theses in Wittenberg."),
 ("The printing press with movable type was developed by:", ["Johannes Gutenberg", "Isaac Newton", "Galileo", "John Locke"], 0, "Gutenberg printed his Bible around 1455."),
]
