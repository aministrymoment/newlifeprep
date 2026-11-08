"""English 2, Final module: final assessment (argumentative essay) and final exam (15 questions)."""
FINAL_ASSESS = dict(t="Final Assessment: Argumentative Essay (500 words or more)",
 prompt="""Write an argumentative essay of at least 500 words on this question: Should every high school student be required to complete a course in personal finance before graduating? Take a clear position.

Your essay must include: an introduction with a hook and a clear thesis; at least three body paragraphs, each with a reason supported by evidence and reasoning; a counterclaim with a rebuttal; transitions; and a conclusion. Use at least one quotation from Scripture (KJV) or from a text read in this course, and use ethos, pathos and logos on purpose. Avoid fallacies. Cite any outside source you use and give credit honestly. Revise and edit your draft before you submit it.""",
 rubric="""Total 100. Clear, debatable thesis: 10. Organization and transitions: 15. Evidence from at least two sources and reasoning: 25. Counterclaim and rebuttal: 15. Use of rhetorical appeals: 10. Style and word choice: 10. Conventions (grammar, spelling, punctuation): 15. Honest citation and no plagiarism: pass or fail requirement. A score of 70 or above is passing.""")
FINAL_EXAM = [
 ("A theme is best stated as:", ["A full statement of a message about life", "One word", "The title of the text", "A list of characters"], 0, "A theme is a complete statement of the message."),
 ("Comparing two unlike things using the word like or as is a:", ["Simile", "Metaphor", "Rhyme", "Fragment"], 0, "A simile uses like or as."),
 ("'The LORD is my shepherd' is an example of a:", ["Metaphor", "Simile", "Statistic", "Fallacy"], 0, "It says the LORD is a shepherd without using like or as."),
 ("Mood is:", ["The feeling a text creates in the reader", "The author's age", "The number of lines", "The setting only"], 0, "Mood is the atmosphere or feeling the reader gets."),
 ("A good paraphrase:", ["Restates the idea in your own words and keeps the meaning", "Changes three words only", "Adds new facts", "Leaves out credit"], 0, "A paraphrase uses your own words and keeps the meaning."),
 ("A text that explains why something happened and what followed uses:", ["Cause and effect", "Chronological order only", "Description only", "No structure"], 0, "That is cause and effect."),
 ("Repeating a pattern of words or phrases for effect is:", ["Parallel structure", "A fragment", "A footnote", "A comma splice"], 0, "Parallel structure repeats a pattern."),
 ("A central idea in a speech is:", ["The most important point the speaker makes", "The first sentence only", "The date", "The speaker's title"], 0, "The central idea is the main point."),
 ("An appeal to a speaker's credibility is:", ["Ethos", "Pathos", "Logos", "Irony"], 0, "Ethos builds trust in the speaker."),
 ("An appeal that uses facts, numbers and clear reasoning is:", ["Logos", "Pathos", "Ethos", "Imagery"], 0, "Logos appeals to logic."),
 ("'Do not trust her plan; she is new here' is an example of:", ["Ad hominem", "A statistic", "Evidence", "A rebuttal"], 0, "It attacks the person, not the plan."),
 ("In an argument, a rebuttal:", ["Answers the counterclaim", "States the title", "Lists the sources", "Describes the setting"], 0, "The rebuttal responds to the opposing view."),
 ("Which task is editing?", ["Fixing a comma splice", "Adding a new main idea", "Reorganizing the paragraphs", "Choosing a new topic"], 0, "Editing corrects errors in conventions."),
 ("Using another person's words or ideas without credit is:", ["Plagiarism", "A paraphrase with credit", "A summary with credit", "A citation"], 0, "That is plagiarism."),
 ("A letter written by a soldier during a war is a:", ["Primary source", "Secondary source", "Textbook", "Rumor"], 0, "A letter from the time is a first hand record."),
]
