"""Spanish 2, Unit 2: Talking About the Past. Florida world language standards cited at strand level; recheck exact benchmark codes at CPALMS."""
from sp2_units1 import CLOSE, S2

UNIT2 = dict(
 title="Unit 2: Talking About the Past",
 std=S2,
 topics=[
 dict(t="2.1 The Preterite: Spelling Changes and Stem Changes", std=S2,
 body="""Psalm 105:5 says, Remember his marvellous works that he hath done, his wonders, and the judgments of his mouth. Remembering what God has done begins with the past tense. In Spanish 1 you met the preterite, which tells about completed actions. Here we add the spelling changes.

Review the endings. Ar verbs take é, aste, ó, amos, aron. Er and ir verbs take í, iste, ió, imos, ieron.

In the yo form, verbs that end in car, gar and zar change spelling to keep the sound. Buscar becomes busqué, pagar becomes pagué and empezar becomes empecé. Compare: Busqué mi Biblia. Pagué la cuenta. Empecé a leer.

When an unaccented i falls between two vowels, it becomes y. Leer is leí, leíste, leyó, leímos, leyeron. Oír is oí, oíste, oyó, oímos, oyeron. Creer is creí, creíste, creyó, creímos, creyeron.

Stem changing ir verbs change in the él and ellos forms only: dormir becomes durmió and durmieron, pedir becomes pidió and pidieron, and servir becomes sirvió and sirvieron.

Worked example: Ayer leí el Salmo 23. Mi hermana pidió agua. Common mistake: writing leió for leyó. The i becomes y between vowels.

Your task: (1) Write the yo form of buscar, pagar and empezar in the preterite. (2) Write five sentences about yesterday with leer, oír, pedir, dormir and servir.""",
 script="""Welcome back. Listen, Psalm 105:5 says, Remember his marvellous works that he hath done. Remembering begins with the past tense.

Now watch this. Review the endings. Ar verbs: é, aste, ó, amos, aron. Er and ir verbs: í, iste, ió, imos, ieron.

In the yo form, car becomes qué, gar becomes gué and zar becomes cé. Busqué, pagué, empecé.

When i falls between two vowels, it becomes y. Leyó, leyeron, oyó, oyeron, creyó.

Stem changing ir verbs change only in the él and ellos forms. Durmió, durmieron, pidió, pidieron.

Your task is to write the yo forms and five sentences about yesterday. Take the four question check.""" + CLOSE,
 quiz=[
 ("The yo preterite of buscar is:", ["Busqué", "Buscé", "Busco", "Buscí"], 0, "Car changes to qué in the yo form."),
 ("Ella leyó means:", ["She read", "She reads", "She will read", "She was reading"], 0, "Leyó is the preterite of leer."),
 ("The ellos preterite of dormir is:", ["Durmieron", "Dormieron", "Duermen", "Dormían"], 0, "Ir stem changers change o to u in the third person."),
 ("The yo preterite of empezar is:", ["Empecé", "Empezé", "Empiezo", "Empezí"], 0, "Zar changes to cé."),
 ]),
 dict(t="2.2 Irregular Verbs in the Preterite", std=S2,
 body="""Genesis 1:3 says, And God said, Let there be light: and there was light. In Spanish, Dios dijo, and the verb dijo is one of many irregular preterites you now need.

Many irregular verbs use a special stem and one set of endings with no accents: e, iste, o, imos, ieron. Here are the stems.
Estar is estuv: estuve, estuviste, estuvo, estuvimos, estuvieron.
Tener is tuv: tuve. Poder is pud: pude. Poner is pus: puse. Saber is sup: supe. Querer is quis: quise. Venir is vin: vine. Hacer is hic: hice, hiciste, hizo, hicimos, hicieron.
Decir is dij and traer is traj. These take eron instead of ieron: dijeron, trajeron.

Dar and ver share the same endings as regular er and ir verbs but have no accents: di, diste, dio, dimos, dieron and vi, viste, vio, vimos, vieron.

Worked example: Ayer estuve en la iglesia y vine a casa a las dos. Mis padres hicieron la cena. Ellos dijeron la verdad. Common mistake: adding accents or the wrong endings, as in tuvé. The yo form is tuve with no accent.

Your task: (1) Conjugate tener and decir in the preterite. (2) Write six sentences about last weekend using estuve, hice, tuve, pude, dije and vi.""",
 script="""Welcome back. Listen, Genesis 1:3 says, And God said, Let there be light: and there was light. In Spanish, Dios dijo. Dijo is an irregular preterite.

Now watch this. Many irregular verbs take a special stem and these endings: e, iste, o, imos, ieron. No accents.

Estar is estuve. Tener is tuve. Poder is pude. Poner is puse. Saber is supe. Querer is quise. Venir is vine. Hacer is hice, and the él form is hizo.

Decir and traer use eron. Dijeron, trajeron.

Dar and ver are di, diste, dio, dimos, dieron, and vi, viste, vio, vimos, vieron.

Your task is to conjugate tener and decir and write six sentences. Take the four question check.""" + CLOSE,
 quiz=[
 ("The yo preterite of tener is:", ["Tuve", "Tenié", "Tuvé", "Tené"], 0, "Tener uses the stem tuv with no accent."),
 ("Ellos dijeron means:", ["They said", "They say", "They will say", "They were saying"], 0, "Dijeron is the preterite of decir."),
 ("The él preterite of hacer is:", ["Hizo", "Hicó", "Hacío", "Hace"], 0, "Hacer changes to hizo in the él form."),
 ("The yo preterite of ver is:", ["Vi", "Vio", "Veí", "Vide"], 0, "Ver is vi with no accent."),
 ]),
 dict(t="2.3 The Imperfect Tense", std=S2,
 body="""Luke 2:8 says, And there were in the same country shepherds abiding in the field, keeping watch over their flock by night. This verse describes a scene that was going on, and Spanish uses the imperfect tense for that. The imperfect describes habitual actions, ongoing actions, descriptions, ages and the time of day in the past.

For ar verbs the endings are aba, abas, aba, ábamos, aban. Hablar becomes hablaba, hablabas, hablaba, hablábamos, hablaban. For er and ir verbs the endings are ía, ías, ía, íamos, ían. Comer becomes comía, comías, comía, comíamos, comían.

Only three verbs are irregular in the imperfect. Ser is era, eras, era, éramos, eran. Ir is iba, ibas, iba, íbamos, iban. Ver is veía, veías, veía, veíamos, veían.

Worked example: Cuando era niño, íbamos a la iglesia cada domingo. Mi abuela cantaba en el coro. Hacía calor y eran las tres. Common mistake: using the preterite for a habit. Say Jugaba todos los días, not Jugué todos los días. English phrases that signal the imperfect are used to, would and was or were plus ing.

Your task: (1) Conjugate vivir, ser and ir in the imperfect. (2) Write six sentences about your childhood: where you lived, what you did each week, and what you were like.""",
 script="""Welcome back. Listen, Luke 2:8 says, There were in the same country shepherds abiding in the field, keeping watch over their flock by night. This describes a scene that was going on. Spanish uses the imperfect for that.

Now watch this. The imperfect tells what used to happen, what was going on, descriptions, ages and time.

Ar verbs: aba, abas, aba, ábamos, aban. Er and ir verbs: ía, ías, ía, íamos, ían.

Three verbs are irregular. Ser is era. Ir is iba. Ver is veía.

Cuando era niño, íbamos a la iglesia cada domingo. Hacía calor y eran las tres.

Your task is to conjugate vivir, ser and ir and write six sentences about your childhood. Take the four question check.""" + CLOSE,
 quiz=[
 ("The imperfect of hablar for yo is:", ["Hablaba", "Hablé", "Hablo", "Hablaría"], 0, "Ar verbs take aba."),
 ("Íbamos a la iglesia means:", ["We used to go to church", "We will go to church", "We went once", "We are going"], 0, "Íbamos is the imperfect of ir."),
 ("Which verb is irregular in the imperfect?", ["Ser", "Hablar", "Comer", "Vivir"], 0, "Ser, ir and ver are the irregular imperfects."),
 ("The imperfect is used for:", ["Habits and descriptions in the past", "A single completed event", "The future", "Commands"], 0, "The imperfect describes ongoing or repeated past actions."),
 ]),
 dict(t="2.4 Preterite and Imperfect Together", std=S2,
 body="""In John 9:25 the man healed of blindness said, One thing I know, that, whereas I was blind, now I see. His words show the two ideas of this lesson: what was ongoing and what changed. Spanish uses the imperfect for the background and the preterite for the events that move the story forward.

Use the imperfect for habits, descriptions, ongoing actions, age, weather and time. Use the preterite for completed actions, a specific time, a sudden event and a change. Compare: Llovía cuando salí de la iglesia. It was raining (background) when I left (event). Mientras leía, llegó mi amigo. While I was reading (ongoing), my friend arrived (event).

Signal words help. Imperfect: siempre, a menudo, todos los días, cada año, mientras, de niño. Preterite: ayer, anoche, una vez, de repente, el lunes, la semana pasada.

A few verbs change meaning. Supe means I found out, conocí means I met, pude means I managed, and no quise means I refused. The imperfect forms sabía, conocía, podía and quería describe a state.

Worked example: De niño, vivía en Cuba. Un día, mi familia salió en un barco. Common mistake: choosing only one tense for a whole story. Mix them, with the imperfect setting the scene and the preterite moving the action.

Your task: (1) Write a paragraph of eight sentences about a memory using both tenses. (2) Underline each preterite and circle each imperfect.""",
 script="""Welcome back. Listen, John 9:25 says, Whereas I was blind, now I see. One tense describes what was, and one tells what changed.

Now watch this. The imperfect sets the scene: habits, descriptions, ongoing actions, age, weather and time. The preterite moves the story: completed actions, a specific time and sudden events.

Llovía cuando salí de la iglesia. Mientras leía, llegó mi amigo.

Signal words help. For the imperfect: siempre, todos los días, mientras. For the preterite: ayer, anoche, de repente, una vez.

Some verbs change meaning. Supe means I found out. Conocí means I met.

Your task is to write a paragraph of eight sentences about a memory using both tenses. Take the four question check.""" + CLOSE,
 quiz=[
 ("Which tense describes the background of a story?", ["Imperfect", "Preterite", "Future", "Command"], 0, "The imperfect sets the scene."),
 ("De repente signals the:", ["Preterite", "Imperfect", "Future", "Present"], 0, "A sudden event uses the preterite."),
 ("Mientras leía, llegó mi amigo. Leía is imperfect because it is:", ["An ongoing action", "A completed action", "A future action", "A command"], 0, "The imperfect shows the action in progress."),
 ("Conocí a Pedro ayer means:", ["I met Pedro yesterday", "I knew Pedro yesterday", "I used to know Pedro", "I will meet Pedro"], 0, "Conocí in the preterite means I met."),
 ]),
 ],
 assess=dict(t="Assessment 2: Talking About the Past",
 prompt="""Write a report of at least 300 words in English with Spanish examples. Use complete sentences and label each part. Psalm 105:5 says, Remember his marvellous works that he hath done, his wonders, and the judgments of his mouth.

Part 1: Conjugate one regular ar, er and ir verb in the preterite, and explain the spelling changes for buscar, pagar, empezar, leer and oír.
Part 2: Conjugate tener, estar, hacer and decir in the preterite and write four sentences.
Part 3: Conjugate one regular verb and ser, ir and ver in the imperfect, and explain when to use the imperfect.
Part 4: Write a Spanish paragraph of at least ten sentences about a childhood memory or a family trip using both the preterite and the imperfect, with signal words.
Part 5: Explain the difference in meaning between supe and sabía and between conocí and conocía.
Part 6: Explain how remembering what God has done, in Psalm 105:5 or Psalm 78:4, can shape the way you tell your own story.""",
 rubric="100 points. Part 1: 15 points. Part 2: 15 points. Part 3: 15 points. Part 4: 30 points. Part 5: 10 points. Part 6: 10 points. Conventions: 5 points. A score of 70 or above is passing."),
 disc=dict(t="Discussion 2: Telling Our Stories",
 prompt="""Write a post of at least 120 words that (1) tells in English about one memory from your childhood, (2) shares at least three Spanish sentences about it using the imperfect and the preterite, and (3) connects your answer to Psalm 105:5 or John 9:25. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why is it important for believers to tell what God has done in the past tense?"""),
 unit_quiz=[
 ("The yo preterite of pagar is:", ["Pagué", "Pagé", "Pago", "Pagí"], 0, "Gar changes to gué."),
 ("Ellos oyeron means:", ["They heard", "They hear", "They will hear", "They listen"], 0, "Oyeron is the preterite of oír."),
 ("The yo preterite of poder is:", ["Pude", "Pudé", "Podí", "Puedo"], 0, "Poder uses the stem pud."),
 ("Yo era is:", ["Imperfect of ser", "Preterite of ser", "Present of ir", "Future of ser"], 0, "Era is the imperfect of ser."),
 ("Todos los días jugábamos signals the:", ["Imperfect", "Preterite", "Future", "Command"], 0, "Habitual actions use the imperfect."),
 ("Anoche cenamos pizza uses the preterite because:", ["It happened once, last night", "It was a habit", "It is a description", "It is a future plan"], 0, "A specific completed action uses the preterite."),
 ("Nosotros fuimos can be the preterite of:", ["Ir or ser", "Hacer", "Tener", "Poner"], 0, "Ir and ser share the preterite fui."),
 ("Íbamos, era and veía are all:", ["Imperfect forms", "Preterite forms", "Future forms", "Present forms"], 0, "These are the three irregular imperfects."),
 ]
)
