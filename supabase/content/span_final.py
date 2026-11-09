"""Spanish 1 final module: final assessment (position 7) and final exam (quiz position 31)."""

FINAL_ASSESS = dict(t="Final Assessment: My Spanish Portfolio and Reflection",
 prompt="""Create a Spanish portfolio and reflection of at least 700 words in total, written in English and Spanish. Write the Spanish yourself. You may use a dictionary or your lesson notes, but do not copy a full translation from a translation tool. Do not include your home address, phone number, passwords or other private details, and have a parent, guardian or teacher review your portfolio before you submit it. Proverbs 4:7 says, Wisdom is the principal thing; therefore get wisdom: and with all thy getting get understanding.

Part 1: Self Introduction. Write a paragraph in Spanish of at least eight sentences that gives your name, age, where you are from, your family, your school, your hobbies and what you like to eat.
Part 2: Conversation. Write a dialogue in Spanish of at least ten lines between two people who meet at a church event or restaurant, using greetings, questions with ¿, a request, a price or a direction, and a farewell.
Part 3: Grammar Showcase. Show correct conjugations of ser, estar, tener, ir, one regular ar verb, one regular er verb and one regular ir verb in the present tense, and one stem changing verb. Write one sentence for each.
Part 4: Past and Future. Write four sentences in Spanish about what you did last weekend using the preterite, and four sentences about your plans using ir a, pensar or querer.
Part 5: Culture Report. Write at least 120 words in English about one Spanish speaking country or Hispanic community in Florida, including its history, foods, music or traditions, with at least six Spanish words.
Part 6: Service Plan. Describe three ways you can use Spanish to serve others honestly and respectfully, including when to ask a trained interpreter for help.
Part 7: Self Assessment. Explain what you learned, what was hardest, what you will practice and your goal for Spanish 2.
Part 8: Faith and Reflection. Apply at least three Scripture passages from the King James Version, such as Genesis 11:9, Acts 2:6, Revelation 7:9 or Matthew 28:19, to the study of language and the call to serve people of every nation.""",
 rubric="""100 points. Part 1, self introduction: 15 points. Part 2, conversation: 15 points. Part 3, grammar showcase: 20 points. Part 4, past and future: 15 points. Part 5, culture report: 10 points. Part 6, service plan: 10 points. Part 7, self assessment: 5 points. Part 8, faith and reflection: 5 points. Accuracy of spelling, accents and conventions: 5 points. A score of 70 or above is passing."""
)

FINAL_EXAM = [
 ("How many letters are in the Spanish alphabet?", ["27", "26", "29", "30"], 0, "It has the 26 English letters plus ñ."),
 ("The letter h in Spanish is:", ["Silent", "Like k", "Like s", "Rolled"], 0, "The h is always silent."),
 ("Buenas noches is used:", ["In the evening or at night", "In the morning", "At noon only", "To say thank you"], 0, "Noche means night."),
 ("Soy de Cuba means:", ["I am from Cuba", "I have Cuba", "I like Cuba", "I go to Cuba"], 0, "Soy de means I am from."),
 ("Treinta y cinco is:", ["35", "53", "30", "15"], 0, "Treinta is 30 and cinco is 5."),
 ("The article for the noun mesa is:", ["La", "El", "Los", "Un"], 0, "Mesa is feminine singular."),
 ("Las chicas altas means:", ["The tall girls", "The tall boys", "A tall girl", "The short girls"], 0, "Adjectives agree with the noun."),
 ("Mi madre ___ en la iglesia.", ["está", "es", "tiene", "hace"], 0, "Location uses estar."),
 ("The yo form of hablar is:", ["Hablo", "Hablas", "Habla", "Hablan"], 0, "Yo takes the o ending."),
 ("Son las tres y media means:", ["It is 3:30", "It is 3:15", "It is 2:30", "It is 3:45"], 0, "Media means half past."),
 ("Me gustan las frutas means:", ["I like fruits", "I eat fruit", "I buy fruit", "I have fruit"], 0, "Gustan is plural."),
 ("The yo form of querer is:", ["Quiero", "Quero", "Quiere", "Queremos"], 0, "Querer changes e to ie."),
 ("Vamos al parque means:", ["We are going to the park", "I am going to the park", "They go home", "We have a park"], 0, "Vamos is the nosotros form of ir."),
 ("Ayer comí arroz means:", ["Yesterday I ate rice", "Tomorrow I will eat rice", "I eat rice daily", "I like rice"], 0, "Comí is the yo preterite form of comer."),
 ("Revelation 7:9 describes people of all nations, and kindreds, and people, and tongues. This teaches us to:", ["Love and serve people of every language", "Avoid other cultures", "Speak only one language", "Ignore strangers"], 0, "The gospel is for every nation and tongue."),
]
