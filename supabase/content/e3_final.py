"""English 3 final module: final assessment (position 7) and final exam (quiz position 31)."""

FINAL_ASSESS = dict(t="Final Assessment: Literary Analysis Research Essay",
 prompt="""Write a literary analysis research essay of at least 500 words on one author, speech, poem or movement from American literature studied in this course. Proverbs 18:15 says, The heart of the prudent getteth knowledge; and the ear of the wise seeketh knowledge. A good scholar seeks knowledge with care and shares it with honesty.

Part 1: Research Question and Thesis. Choose a topic from this course, such as Franklin and the plain style, the rhetoric of the Declaration of Independence, Hawthorne and allegory, Emerson and self reliance, the freedom narratives, Lincoln's language, Realism and Regionalism, Naturalism, the Harlem Renaissance, or Modernism. Write one research question and a debatable thesis.

Part 2: Sources. Identify at least one primary source (the original text, speech or poem) and at least one secondary source (a reliable article, biography or reference). Give a simple citation for each, naming the author, title, publisher or website, and date. Explain in two sentences why each source is reliable.

Part 3: Essay. Write a literary analysis with an introduction (hook, background, thesis), at least three body paragraphs using the PIE pattern (point, illustration with a quotation or specific detail, explanation), and a conclusion that restates the thesis freshly and tells why it matters. Name and explain at least three literary or rhetorical techniques, such as symbol, allegory, contrast, imagery, parallelism, ethos, pathos or logos. Explain how the historical context shaped the work.

Part 4: Scripture Connection. Connect one idea in your essay to a passage of Scripture in the King James Version, quoted accurately.

Part 5: Presentation Plan. In a short paragraph, outline a three minute presentation of your essay, naming your opening, three key points, closing and two helpful visuals.

Part 6: Revision. List two changes you made after rereading or receiving feedback, and tell how they improved your essay.""",
 rubric="""100 points. Part 1, research question and thesis: 10 points. Part 2, sources and citations: 10 points. Part 3, essay structure, evidence, technique analysis and context: 45 points. Part 4, Scripture connection: 7 points. Part 5, presentation plan: 10 points. Part 6, revision: 8 points. Grammar, conventions and academic voice: 10 points. A score of 70 or above is passing.""")

FINAL_EXAM = [
 ("The main idea of a passage is:", ["What the whole passage is mostly about", "The first word", "The longest sentence", "The title only"], 0, "The main idea is the central point of the passage."),
 ("An appeal to the speaker's credibility is called:", ["Ethos", "Pathos", "Logos", "Irony"], 0, "Ethos builds trust in the speaker."),
 ("The Declaration of Independence is organized as principles, grievances and:", ["A conclusion declaring independence", "A recipe", "A song", "A map"], 0, "The document ends by declaring the colonies free and independent."),
 ("Parallelism is:", ["Similar grammatical form repeated in a series", "A kind of rhyme", "A setting", "A character"], 0, "Parallelism repeats a pattern to build rhythm."),
 ("An allegory has:", ["A surface story and a deeper meaning", "No characters", "Only facts", "Only dates"], 0, "Allegories work on two levels."),
 ("A symbol is:", ["An object that stands for a bigger idea", "A type of verb", "A date", "A rhyme"], 0, "Symbols represent larger ideas."),
 ("Transcendentalists such as Emerson and Thoreau valued:", ["Self reliance and nature", "Following the crowd", "Ignoring nature", "Only wealth"], 0, "They taught independence of thought and love of nature."),
 ("Free verse is poetry that:", ["Does not follow regular rhyme or meter", "Always rhymes", "Has no images", "Has no words"], 0, "Free verse has no set pattern."),
 ("Contrast in a narrative is used to:", ["Place differences side by side to shape meaning", "Repeat the same word", "List dates", "Avoid the point"], 0, "Contrast highlights differences."),
 ("A counterargument is:", ["An answer to the other side", "A repeated claim", "A title", "A rhyme"], 0, "Good arguments respond to opposing views."),
 ("Lincoln's warning in Mark 3:25 was that a house divided against itself:", ["Cannot stand", "Will prosper", "Is invisible", "Will always win"], 0, "Mark 3:25 says that house cannot stand."),
 ("Naturalism often shows characters:", ["Struggling against forces they cannot control", "Controlling everything", "Living in fairy tales", "Avoiding conflict"], 0, "Naturalist writers emphasize powerful outside forces."),
 ("Hemingway's iceberg theory means that:", ["Most meaning lies beneath the surface", "Everything must be said", "Stories must be cold", "Stories need no people"], 0, "Hemingway left much unsaid."),
 ("The Harlem Renaissance was centered in:", ["Harlem in New York City", "Boston", "Dallas", "Seattle"], 0, "It flourished in Harlem in the 1920s and 1930s."),
 ("In a PIE paragraph, the three parts are:", ["Point, illustration and explanation", "Plot, image and ending", "Poem, idea and example", "Place, intro and end"], 0, "PIE means point, illustration, explanation."),
]
