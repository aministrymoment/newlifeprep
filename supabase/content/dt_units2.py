"""Digital Technology and Computer Applications, Unit 2: Documents, Presentations and Collaboration. Florida standards cited at strand level (SC.912.CS)."""
from dt_units1 import CLOSE

UNIT2 = dict(
 title="Unit 2: Documents, Presentations and Collaboration",
 std="SC.912.CS",
 topics=[
 dict(t="2.1 Word Processing Essentials", std="SC.912.CS",
 body="""A word processor is application software used to write, edit, format and print documents. Common programs include Microsoft Word, Google Docs and Apple Pages. Learning to use one well is a skill needed in school, church, business and ministry.

Begin with keyboarding. Place your fingers on the home row and learn to type without looking at the keys. Accuracy comes first, then speed. Speed is measured in words per minute. Good posture and regular breaks protect your hands, wrists and eyes. Colossians 3:23 says, And whatsoever ye do, do it heartily, as to the Lord, and not unto men.

Know the basic tools. Type and edit text, select text, and use cut, copy and paste. Use undo when you make a mistake. Change the font, size, color and alignment. Choose line spacing and paragraph spacing. Create bulleted and numbered lists. Use spell check and grammar check, but remember that they are not perfect. A word spelled correctly can still be the wrong word, so read your work aloud and proofread carefully.

Save early and often. Give the file a clear name and save it in the right folder. Turn on autosave if it is offered. Learn useful shortcuts, such as holding the Control key and pressing S to save, C to copy, V to paste and Z to undo. On a Mac, the Command key is used.

Plan before you write. Know the purpose and audience, outline your main points, write a first draft, revise for clarity and organization, then edit for spelling and grammar. Good writing comes from rewriting.

Your task: (1) Explain why accuracy matters before speed in keyboarding. (2) List five basic word processing tools. (3) Describe the five steps of the writing process.""",
 script="""Welcome back. Listen, Colossians 3:23 says, And whatsoever ye do, do it heartily, as to the Lord, and not unto men. Learn your tools with excellence.

Now watch this. A word processor is software for writing, editing, formatting and printing documents. Word, Google Docs and Pages are examples.

Start with keyboarding. Fingers on the home row. Accuracy first, then speed, measured in words per minute. Take breaks to protect your hands and eyes.

Know the tools. Cut, copy, paste and undo. Change font, size and alignment. Set line spacing. Make bulleted and numbered lists. Use spell check, but proofread, because a correctly spelled word can still be the wrong word. Read your work aloud.

Save early and often with a clear file name. Learn shortcuts: Control and S to save, C to copy, V to paste, Z to undo.

Plan, draft, revise, edit and proofread. Good writing comes from rewriting.

Your task is to explain accuracy before speed, list five tools and describe the writing process. Take the four question check.""" + CLOSE,
 quiz=[
 ("Typing speed is measured in:", ["Words per minute", "Bytes per second", "Pages per hour", "Files per day"], 0, "WPM measures typing speed."),
 ("The best order for building keyboarding skill is:", ["Accuracy first, then speed", "Speed first, then accuracy", "Neither matters", "Look at keys always"], 0, "Accuracy comes first."),
 ("Spell check may miss:", ["A correctly spelled wrong word", "Every typo", "All capital letters", "Page numbers"], 0, "Proofreading catches wrong word choices."),
 ("Which step comes after writing a first draft?", ["Revising", "Deleting everything", "Printing only", "Closing the file"], 0, "Revision improves clarity and organization."),
 ]),
 dict(t="2.2 Formatting Professional Documents", std="SC.912.CS",
 body="""Formatting is how a document looks, and it affects how easily it is read. Proverbs 22:29 says, Seest thou a man diligent in his business? he shall stand before kings; he shall not stand before mean men. Careful work shows respect for the reader and for God.

Start with structure. Use heading styles for titles and sections instead of just making the text bigger. Styles keep the document consistent, allow an automatic table of contents and help screen readers and navigation. Use a readable font such as Times New Roman, Calibri or Arial at 11 or 12 points. Set margins to one inch unless told otherwise. Use consistent line spacing, often double spacing for school papers. Add page numbers, and use a header or footer for the title or author when needed.

Use lists and tables wisely. A bulleted list shows items with no order, and a numbered list shows steps or ranking. A table organizes information in rows and columns. Add a clear label, and do not use tables just to position text.

Images and graphics should serve the message. Resize them without stretching, wrap text neatly and add alternative text that describes the image for people who cannot see it. Give credit for images you did not create.

Academic work requires citations. Quote exactly with quotation marks, paraphrase in your own words, and list sources in a works cited or reference page in the style your teacher requires, such as MLA or APA. A citation names the author, title, publisher, date and location of a source.

Professional communication has standard forms. A business letter has a date, an address block, a greeting, a clear body and a closing. An email needs a clear subject line, a polite greeting, a short message and a signature. Always proofread before sending. Review the document: check headings, spelling, spacing, page breaks and the title page.

Your task: (1) Explain why heading styles are better than enlarged text. (2) List five formatting settings used in a school paper. (3) Describe the parts of a professional email.""",
 script="""Welcome back. Listen, Proverbs 22:29 says, Seest thou a man diligent in his business? he shall stand before kings; he shall not stand before mean men. Careful work shows respect for the reader and for God.

Now watch this. Formatting affects how easily a document is read. Use heading styles for titles and sections. Styles keep your document consistent, build an automatic table of contents and help screen readers.

Use a readable font at 11 or 12 points. Set one inch margins. Use consistent spacing. Add page numbers and a header or footer.

Bulleted lists show items with no order. Numbered lists show steps. Tables organize rows and columns.

Resize images without stretching them. Add alternative text. Give credit for images you did not create.

Cite your sources. Quote exactly. Paraphrase in your own words. List sources in MLA or APA style.

A business letter has a date, address block, greeting, body and closing. An email needs a clear subject, polite greeting, short message and signature. Proofread before sending.

Your task is to explain heading styles, list formatting settings and describe a professional email. Take the four question check.""" + CLOSE,
 quiz=[
 ("A feature that keeps headings consistent and builds a table of contents is:", ["Heading styles", "Spell check", "Autosave", "Print preview"], 0, "Styles organize and format the document."),
 ("A typical margin setting for a school paper is:", ["One inch", "Five inches", "Zero", "Ten inches"], 0, "One inch margins are standard."),
 ("Alternative text for an image helps:", ["People who cannot see the image", "Printers", "Keyboards", "Batteries"], 0, "Alt text describes images for accessibility."),
 ("A citation tells the reader:", ["Where information came from", "How fast you type", "Your password", "Your folder name"], 0, "Citations credit and locate sources."),
 ]),
 dict(t="2.3 Presentation Design", std="SC.912.CS",
 body="""A presentation is a tool for sharing ideas with an audience. Programs such as PowerPoint, Google Slides and Keynote help you build slides, but the slides support the speaker and do not replace the speaker. Habakkuk 2:2 says, And the LORD answered me, and said, Write the vision, and make it plain upon tables, that he may run that readeth it. Clear communication makes a message easy to receive.

Begin with purpose and audience. Ask what you want people to know, feel or do, and who will be listening. Outline the main points before opening the software. A strong presentation has an opening that gains attention, a body with a few main points and a closing that summarizes and gives a call to action.

Design for the eye. Use one main idea per slide. Keep text short, using key phrases and not full paragraphs. Use large, readable fonts, at least 24 points for body text and larger for titles. Choose strong contrast between text and background, such as dark text on a light background. Keep colors, fonts and layouts consistent by using a theme or master slide. Use no more than a few colors. Leave white space so slides are not crowded.

Use visuals wisely. Choose high quality images, charts or short video clips that support your point. Avoid clip art overload, distracting animations and sound effects. Every transition and animation should have a purpose. Give credit for images and sources on a final slide.

Delivery matters most. Practice aloud, time yourself, and know your material so you speak to people and not to the screen. Never read the slides word for word. Use speaker notes to hold details. Make eye contact, speak clearly, stand with good posture and be ready for questions. Check that equipment works before you begin and have a backup copy of your file.

Your task: (1) Explain how to plan a presentation. (2) List five design rules for slides. (3) Describe three delivery tips.""",
 script="""Welcome back. Listen, Habakkuk 2:2 says, Write the vision, and make it plain upon tables, that he may run that readeth it. Make your message plain.

Now watch this. A presentation supports the speaker. It does not replace the speaker. Start with purpose and audience. What do you want people to know, feel or do? Outline first. Have an opening, a few main points and a closing with a call to action.

Design for the eye. One main idea per slide. Short key phrases, not paragraphs. Large fonts, at least 24 points. Strong contrast. A consistent theme. Leave white space.

Use quality images, charts or short clips. Avoid distracting animations. Credit your sources.

Delivery matters most. Practice aloud and time yourself. Do not read the slides word for word. Use speaker notes. Make eye contact. Speak clearly. Test your equipment and keep a backup copy.

Your task is to explain planning, list five design rules and describe three delivery tips. Take the four question check.""" + CLOSE,
 quiz=[
 ("A good slide generally contains:", ["One main idea in short phrases", "Full paragraphs of text", "Ten different fonts", "No message"], 0, "Short, focused slides are easier to read."),
 ("The minimum body text size suggested for slides is about:", ["24 points", "6 points", "8 points", "10 points"], 0, "Large text is readable from a distance."),
 ("The best way to deliver a presentation is to:", ["Speak to the audience and not read slides word for word", "Read every word", "Face the screen", "Skip practice"], 0, "Slides support the speaker."),
 ("Speaker notes are used to:", ["Hold details for the speaker", "Replace the slides", "Change the file type", "Print the screen"], 0, "Notes help the speaker without crowding slides."),
 ]),
 dict(t="2.4 Collaboration and Cloud Tools", std="SC.912.CS",
 body="""Cloud computing means storing files and running programs on servers over the internet instead of only on your own device. Services such as Google Drive, OneDrive and iCloud keep files available from any device with a connection and also act as a backup. Cloud tools make teamwork easier. Ecclesiastes 4:9 says, Two are better than one; because they have a good reward for their labour. And verse 12 adds, a threefold cord is not quickly broken.

In a shared document, several people can read, comment and edit together. Sharing settings, called permissions, control what others can do. A viewer can only read. A commenter can add comments. An editor can change the content. Give people only the access they need. Share to specific people when possible instead of making a link open to everyone, since anyone with an open link may be able to see the file.

Good collaboration needs rules. Agree on who does what, set deadlines, use comments and suggestions instead of overwriting another person's work, and keep the file name and folder clear. Version history lets you see changes and restore earlier versions, so mistakes can be fixed. Never delete a teammate's work without discussion. Give credit to each person for their part, and do your own share faithfully. Proverbs 27:17 says, Iron sharpeneth iron; so a man sharpeneth the countenance of his friend.

Communicate well. Use email, chat and video meetings respectfully. In a video meeting, join on time, mute when not speaking, dress appropriately, keep your background neat and pay attention. In writing, be clear, kind and professional, since tone is hard to read in text. Respond in a reasonable time.

Be careful with cloud security. Use strong passwords and multifactor authentication, do not share login information, sign out of shared devices and do not store sensitive information such as Social Security numbers in places that are not protected. Know the school or church rules for approved tools.

Your task: (1) Explain what the cloud is. (2) Compare viewer, commenter and editor permissions. (3) List four rules for good online collaboration.""",
 script="""Welcome back. Listen, Ecclesiastes 4:9 says, Two are better than one; because they have a good reward for their labour. Teamwork is powerful, and cloud tools make it easier.

Now watch this. The cloud means storing files and running programs on servers over the internet. Google Drive, OneDrive and iCloud keep files available from any device and also act as a backup.

In a shared document, permissions control what others can do. A viewer can read. A commenter can add comments. An editor can change the content. Give only the access needed. Share with specific people, not an open link.

Good collaboration needs rules. Agree on who does what. Set deadlines. Use comments and suggestions instead of overwriting. Version history lets you restore earlier versions. Give credit and do your share. Proverbs 27:17 says, Iron sharpeneth iron.

In video meetings, join on time, mute when not speaking and pay attention. In writing, be clear and kind.

Use strong passwords, multifactor authentication and sign out of shared devices.

Your task is to explain the cloud, compare permissions and list four rules for collaboration. Take the four question check.""" + CLOSE,
 quiz=[
 ("Cloud storage keeps files:", ["On servers you reach over the internet", "Only on one USB drive", "Only on paper", "Nowhere"], 0, "The cloud means internet based servers."),
 ("A person with commenter permission can:", ["Add comments but not edit", "Delete the file", "Change the owner", "Remove everyone"], 0, "Commenters can leave comments only."),
 ("Version history allows you to:", ["Restore earlier versions of a file", "Speed up the internet", "Erase the file forever", "Change the font only"], 0, "It tracks and restores changes."),
 ("A safe sharing practice is to:", ["Share with specific people when possible", "Make every file public", "Share your password", "Use no permissions"], 0, "Limit access to those who need it."),
 ]),
 ],
 assess=dict(t="Assessment 2: Documents, Presentations and Collaboration",
 prompt="""Write a report of at least 250 words on productivity tools. Use complete sentences and label each part. Proverbs 22:29 says, Seest thou a man diligent in his business? he shall stand before kings; he shall not stand before mean men.

Part 1: Describe the writing process and five basic word processing tools. Explain why proofreading is needed even after spell check.
Part 2: List six formatting settings for a professional school paper. Explain heading styles, page numbers, alternative text and citations.
Part 3: Type a sample professional email of at least five sentences to a pastor or teacher, with a subject line, greeting, message and signature.
Part 4: Plan a five slide presentation on a topic of your choice by listing the title of each slide and one main idea for each. Give four design rules and three delivery tips.
Part 5: Explain cloud storage, three kinds of sharing permissions and four rules for online collaboration. Explain how Colossians 3:23 and Ecclesiastes 4:9 apply to teamwork.""",
 rubric="""100 points. Part 1: 15 points. Part 2: 20 points. Part 3: 15 points. Part 4: 25 points. Part 5: 20 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 2: Two Are Better Than One",
 prompt="""Write a post of at least 120 words that (1) describes a time when you worked on a group project or team task, with no names, (2) explains in your own words why clear communication and fair sharing matter, (3) explains one way presentations or documents can be used to serve a church or community, and (4) connects your answer to Ecclesiastes 4:9, Habakkuk 2:2, Proverbs 22:29 or Colossians 3:23. Then write a respectful reply of at least 40 words to another student's post, or answer this question: How should a team member respond when someone does not do their share? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("A word processor is used to:", ["Write and format documents", "Store only photos", "Run the internet", "Replace the CPU"], 0, "A word processor creates documents."),
 ("A file with the pptx extension is a:", ["Presentation", "Spreadsheet", "Audio file", "Photo"], 0, "Pptx is a presentation format."),
 ("Heading styles help by:", ["Organizing and formatting sections consistently", "Making files smaller only", "Blocking viruses", "Changing the keyboard"], 0, "Styles create structure."),
 ("A strong slide design uses:", ["Short text and strong contrast", "Long paragraphs", "Low contrast colors", "Tiny fonts"], 0, "Simple slides are easy to read."),
 ("Habakkuk 2:2 teaches us to make a message:", ["Plain", "Confusing", "Hidden", "Loud"], 0, "Write the vision and make it plain."),
 ("A shared file link set to open to anyone is:", ["Riskier than sharing with specific people", "Always safest", "Not shareable", "Encrypted"], 0, "Open links may be seen by unintended people."),
 ("Which permission lets a person change the document?", ["Editor", "Viewer", "Commenter", "Guest only"], 0, "Editors can change content."),
 ("Ecclesiastes 4:9 says two are better than one because they have:", ["A good reward for their labour", "More debt", "Less work", "No plan"], 0, "Cooperation brings reward."),
 ])
