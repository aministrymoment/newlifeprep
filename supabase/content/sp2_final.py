"""Spanish 2 final assessment and final exam. Correct answer is always first; the builder shuffles."""

FINAL_ASSESS = dict(t="Final Assessment: My Spanish 2 Portfolio and Reflection",
 prompt="""Create a Spanish portfolio and reflection of at least 900 words in total, written in English and Spanish. Write the Spanish yourself. You may use a dictionary or your lesson notes, but do not copy a full translation from a translation tool. Do not include your home address, phone number, passwords or other private details, and have a parent, guardian or teacher review your portfolio before you submit it. Proverbs 1:5 says, A wise man will hear, and will increase learning; and a man of understanding shall attain unto wise counsels.

Part 1: My Day. Write a paragraph in Spanish of at least ten sentences about your daily routine using at least five reflexive verbs, three irregular yo verbs, saber and conocer.
Part 2: My Story. Write a story in Spanish of at least twelve sentences about a childhood memory or a Bible story, using the preterite for events and the imperfect for the scene.
Part 3: Conversation. Write a dialogue in Spanish of at least twelve lines that includes direct and indirect object pronouns, a comparison, por and para, and at least two formal commands.
Part 4: Community. Write a dialogue of at least eight lines about travel, directions, a pharmacy visit or an emergency, and explain when a volunteer should call a trained interpreter.
Part 5: Plans and Careers. Write at least eight sentences in Spanish about your future using the present progressive and the future tense, including a career you may choose.
Part 6: Letters. Write a formal email and an informal note, five sentences each.
Part 7: Culture Report. Write at least 150 words in English about one Spanish speaking country, community or tradition, with at least eight Spanish words and a respectful description.
Part 8: Service Plan. Describe four ways you will use Spanish to serve others honestly and respectfully.
Part 9: Faith and Reflection. Apply at least three Scripture passages from the King James Version, such as Psalm 78:4, Philippians 4:6, Romans 1:7 or Matthew 25:40, to your study of Spanish and your calling to serve, and explain what you learned, what was hardest and your goal for Spanish 3.""",
 rubric="100 points. Part 1: 10 points. Part 2: 15 points. Part 3: 15 points. Part 4: 10 points. Part 5: 10 points. Part 6: 10 points. Part 7: 10 points. Part 8: 5 points. Part 9: 10 points. Accuracy of spelling, accents and conventions: 5 points. A score of 70 or above is passing.")

FINAL_EXAM = [
 ("Me despierto a las seis means:", ["I wake up at six", "I wake him at six", "I sleep at six", "I eat at six"], 0, "Despertarse is reflexive and changes e to ie."),
 ("The yo form of hacer in the present is:", ["Hago", "Hazo", "Hacio", "Hace"], 0, "Hacer is a yo go verb."),
 ("To say you know a person, use:", ["Conocer", "Saber", "Ser", "Poder"], 0, "Conocer is for people and places."),
 ("The yo preterite of buscar is:", ["Busqué", "Buscé", "Busco", "Buscí"], 0, "Car changes to qué."),
 ("The preterite of tener for yo is:", ["Tuve", "Tenía", "Tendré", "Tengo"], 0, "Tener has the stem tuv."),
 ("Íbamos a la iglesia cada domingo uses the imperfect because it describes:", ["A habit", "A single event", "A future plan", "A command"], 0, "The imperfect describes habitual past actions."),
 ("Mientras leía, llegó mi amigo. Llegó is in the:", ["Preterite", "Imperfect", "Future", "Command"], 0, "A sudden event uses the preterite."),
 ("The pronoun that replaces la Biblia is:", ["La", "Lo", "Las", "Le"], 0, "La replaces a feminine singular noun."),
 ("Le doy el libro becomes:", ["Se lo doy", "Le lo doy", "Lo le doy", "Me lo doy"], 0, "Le becomes se before lo."),
 ("Mi hermano es más alto que yo means:", ["My brother is taller than I am", "My brother is as tall as I am", "My brother is the tallest", "I am taller than my brother"], 0, "Más plus an adjective plus que compares."),
 ("Gracias ___ la ayuda.", ["por", "para", "de", "con"], 0, "Por shows the reason for thanks."),
 ("The usted command of hablar is:", ["Hable", "Habla", "Hablas", "Hablar"], 0, "Ar verbs take e in the formal command."),
 ("The affirmative tú command of hacer is:", ["Haz", "Hace", "Hagas", "Hazo"], 0, "Hacer is irregular and becomes haz."),
 ("Mañana ___ la tarea.", ["haré", "hice", "hacía", "hago ayer"], 0, "The future of hacer uses the stem har."),
 ("Matthew 25:40 teaches us that serving the least of these is like serving:", ["Christ", "A teacher", "A friend only", "Ourselves"], 0, "Jesus said what we do for the least of these we do for Him."),
]
