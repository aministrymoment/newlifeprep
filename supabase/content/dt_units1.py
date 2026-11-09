"""Digital Technology and Computer Applications, Unit 1: Computing Foundations and Digital Citizenship. Florida digital literacy and computer science standards cited at strand level (SC.912.CS); recheck exact benchmark codes at CPALMS."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."

UNIT1 = dict(
 title="Unit 1: Computing Foundations and Digital Citizenship",
 std="Florida computer science and digital literacy course standards",
 topics=[
 dict(t="1.1 Computers, Hardware and Software", std="Florida computer science and digital literacy course standards",
 body="""A computer is an electronic machine that accepts input, processes it, stores it and produces output. Every device you use follows this cycle. When you type a key, that is input. The processor works on it. The screen showing the letter is output. Saved files are storage.

Hardware is the physical part of a computer that you can touch. The central processing unit, or CPU, is the brain that carries out instructions. Random access memory, or RAM, is short term working memory that is cleared when the power goes off. Storage, such as a solid state drive, keeps files even when the power is off. The motherboard connects the parts. Input devices include a keyboard, mouse, microphone and camera. Output devices include a monitor, printer and speakers. Phones, tablets and laptops are computers too.

Software is the set of instructions that tells hardware what to do. System software, such as an operating system, manages the machine. Application software, such as a word processor, a browser or a game, helps you do tasks.

Computers store everything as bits. A bit is a single zero or one. Eight bits make a byte, and bytes are counted in kilobytes, megabytes, gigabytes and terabytes. Binary code is the zeros and ones that machines understand.

God gives people skill to build useful things. Exodus 31:3 says of Bezaleel, And I have filled him with the spirit of God, in wisdom, and in understanding, and in knowledge, and in all manner of workmanship. Technology is a tool, and a believer can learn it with excellence and use it to serve God and others. Colossians 3:23 says, And whatsoever ye do, do it heartily, as to the Lord, and not unto men.

Your task: (1) Name the four parts of the computing cycle. (2) Explain the difference between RAM and storage. (3) Explain the difference between hardware and software.""",
 script="""Welcome back. Listen, Exodus 31:3 says God filled Bezaleel with wisdom, and understanding, and knowledge, and in all manner of workmanship. God gives people skill to build useful things, and technology is one of them.

Now watch this. A computer accepts input, processes it, stores it and produces output. Type a key, that is input. The CPU, the brain, processes it. The screen shows the output. Saved files are storage.

Hardware is the part you can touch. The CPU thinks. RAM is short term working memory that clears when the power goes off. Storage keeps files when the power is off. Keyboards, mice and microphones are input devices. Monitors, printers and speakers are output devices.

Software is the instructions. System software like an operating system manages the machine. Application software like a word processor or browser helps you do tasks.

Everything is stored as bits, zeros and ones. Eight bits make a byte.

Your task is to name the computing cycle, compare RAM and storage and compare hardware and software. Take the four question check.""" + CLOSE,
 quiz=[
 ("The physical parts of a computer that you can touch are called:", ["Hardware", "Software", "Binary", "Output"], 0, "Hardware is the physical equipment."),
 ("Short term working memory that clears when power is off is:", ["RAM", "A solid state drive", "A monitor", "A keyboard"], 0, "RAM is temporary working memory."),
 ("Eight bits make one:", ["Byte", "Kilobyte", "Gigabyte", "Pixel"], 0, "A byte is eight bits."),
 ("A keyboard is an example of:", ["An input device", "An output device", "System software", "A network"], 0, "A keyboard sends information into the computer."),
 ]),
 dict(t="1.2 Operating Systems, Files and Folders", std="Florida computer science and digital literacy course standards",
 body="""An operating system, or OS, is the main software that manages a computer. It controls the hardware, runs applications, provides the screen you see and organizes files. Common operating systems include Windows, macOS, ChromeOS and Linux for computers, and Android and iOS for phones and tablets. An application must be made to work with the operating system it runs on.

A file is a named collection of information. A folder, also called a directory, holds files and other folders. Good organization saves time. 1 Corinthians 14:40 says, Let all things be done decently and in order. Use clear names such as Science Report Draft 2 instead of New Document. Group files in folders by subject or project. Avoid spaces and symbols that cause trouble when files are shared, and never rely on a vague name like final final.

The end of a file name, called the file extension, tells the computer what kind of file it is. A docx file is a word processing document, an xlsx file is a spreadsheet, a pptx file is a presentation, a pdf file is a fixed layout document, a jpg or png file is an image, an mp3 file is audio and an mp4 file is video. Knowing the format helps you choose the right program and share files correctly.

Learn basic file skills: create, name, open, save, copy, move, rename, delete and search. Know the difference between Save and Save As. Use the recycle bin or trash carefully, since deleted files may not return.

Protect your work with backups. A common rule is to keep three copies of important files, on two kinds of storage, with one copy in a different place such as cloud storage. Hard drives fail, phones are lost and files are deleted by mistake, so back up often.

Your task: (1) Name four jobs of an operating system. (2) Match five file extensions with their file types. (3) Describe your backup plan.""",
 script="""Welcome back. Listen, 1 Corinthians 14:40 says, Let all things be done decently and in order. That applies to our files too.

Now watch this. The operating system is the main software that manages the computer. It controls hardware, runs applications, gives you the screen and organizes files. Windows, macOS, ChromeOS and Linux run on computers. Android and iOS run on phones and tablets.

A file is a named collection of information. A folder holds files. Use clear names, like Science Report Draft 2, not New Document. Group files by subject or project.

The file extension tells the computer the type. Docx is a word document. Xlsx is a spreadsheet. Pptx is a presentation. Pdf is a fixed layout document. Jpg and png are images. Mp3 is audio. Mp4 is video.

Learn to create, name, save, copy, move, rename, delete and search. Know Save and Save As.

Back up your work. Keep three copies, on two kinds of storage, with one in a different place like the cloud.

Your task is to name the jobs of an operating system, match extensions and describe your backup plan. Take the four question check.""" + CLOSE,
 quiz=[
 ("The main software that manages a computer is the:", ["Operating system", "Browser", "Monitor", "Printer"], 0, "The OS controls hardware and software."),
 ("A pptx file is a:", ["Presentation", "Spreadsheet", "Image", "Audio file"], 0, "Pptx files are presentations."),
 ("Which is an operating system for phones?", ["Android", "Excel", "Chrome extension", "Keyboard"], 0, "Android and iOS run on phones."),
 ("A good backup plan keeps copies:", ["In more than one place", "Only on the desktop", "Only in the recycle bin", "Nowhere"], 0, "Separate copies protect against loss."),
 ]),
 dict(t="1.3 Digital Citizenship, Ethics and Stewardship of Technology", std="Florida computer science and digital literacy course standards",
 body="""A digital citizen uses technology responsibly, respectfully and safely. The Lord is as concerned with how we behave online as how we behave in person. Matthew 7:12 says, Therefore all things whatsoever ye would that men should do to you, do ye even so to them: for this is the law and the prophets. Ephesians 4:29 says, Let no corrupt communication proceed out of your mouth, but that which is good to the use of edifying, that it may minister grace unto the hearers.

Your digital footprint is the record of everything you post, share, search and click. It can last for years, be copied and be seen by schools, employers and others. Before posting, ask whether it is true, kind and necessary, and whether you would be comfortable if a parent or pastor saw it. Netiquette means good manners online: avoid all capital letters that look like shouting, think before replying, and do not forward rumors.

Cyberbullying is the use of technology to harass, embarrass or threaten others. It is wrong. If you are targeted, save the evidence, do not respond in anger, block the person, and tell a trusted adult. If you see it happening, do not join in, and support the person who is hurt.

Respect creators. Plagiarism is presenting another person's words or ideas as your own. Copyright law protects original works from the moment they are created. Fair use allows limited use of copyrighted material for purposes such as education or commentary, but it is a defense judged case by case and not a free pass to copy. To use materials legally, look for permission, public domain works or Creative Commons licenses, and always give credit. Downloading pirated music, movies or software is stealing.

Technology also calls for balance. Time is a gift, and a faithful steward should manage screen time, sleep, study, family, church and service. Philippians 4:8 teaches us what to dwell on: whatsoever things are true, whatsoever things are honest, whatsoever things are just, whatsoever things are pure, whatsoever things are lovely.

Your task: (1) Define digital footprint. (2) List three steps to take if you are cyberbullied. (3) Explain the difference between plagiarism and giving credit.""",
 script="""Welcome back. Listen, Matthew 7:12 says, all things whatsoever ye would that men should do to you, do ye even so to them. And Ephesians 4:29 says, Let no corrupt communication proceed out of your mouth, but that which is good to the use of edifying. That is how we behave online.

Now watch this. Your digital footprint is the record of what you post, share, search and click. It can last for years. Before you post, ask if it is true, kind and necessary.

Netiquette is good manners online. Think before replying and do not forward rumors.

Cyberbullying is wrong. If you are targeted, save the evidence, do not answer in anger, block the person and tell a trusted adult. If you see it, do not join in.

Respect creators. Plagiarism is presenting someone else's work as your own. Copyright protects original works from the moment they are created. Fair use is limited and judged case by case. Look for permission, public domain or Creative Commons, and give credit. Pirated downloads are stealing.

Manage your time. Philippians 4:8 says think on whatsoever things are true, honest, just, pure and lovely.

Your task is to define digital footprint, list steps for cyberbullying and explain plagiarism. Take the four question check.""" + CLOSE,
 quiz=[
 ("The record of everything you post, share and click online is your:", ["Digital footprint", "Operating system", "Backup", "Firewall"], 0, "Your digital footprint can last for years."),
 ("Presenting someone else's work as your own is:", ["Plagiarism", "Fair use", "Netiquette", "Backup"], 0, "Plagiarism is dishonest."),
 ("If you are cyberbullied, a wise first step is to:", ["Save the evidence and tell a trusted adult", "Reply in anger", "Delete everything and say nothing", "Join in"], 0, "Evidence and adult help are important."),
 ("Copyright protection begins:", ["When a work is created", "Only after a fee is paid", "After 50 years", "Never"], 0, "Original works are protected from creation."),
 ]),
 dict(t="1.4 Online Safety, Passwords and Privacy", std="Florida computer science and digital literacy course standards",
 body="""The internet is a useful place and also a place with dangers. Proverbs 22:3 says, A prudent man foreseeth the evil, and hideth himself: but the simple pass on, and are punished. Proverbs 4:23 says, Keep thy heart with all diligence; for out of it are the issues of life. Online safety protects your heart, your mind, your information and your family.

Protect personal information such as your full name, address, school, phone number, passwords, birth date and financial details. Never post them publicly, and be careful about what you share even with friends. Turn off location sharing for photos and posts unless you need it. Remember that people online may not be who they say they are. Never meet someone you only know online, and tell a parent or trusted adult if a stranger contacts you or asks for photos or secrets.

Passwords are the keys to your accounts. A strong password is long, at least twelve to sixteen characters, and unique for each account. A passphrase made of several unrelated words is easy to remember and hard to guess. Do not use names, birthdays or common words such as password. Never reuse a password, never share it, and never write it where others can see it. A password manager can create and store strong passwords safely.

Turn on multifactor authentication where it is offered. After your password, the account asks for a second proof, such as a code sent to your phone or an app. This stops most attackers even when a password is stolen.

Review privacy settings on apps and social media, and limit who can see your posts. Read what permissions an app asks for, and do not install apps that ask for more than they need. Log out of shared computers. Keep software updated, since updates fix security problems. Be careful on public WiFi, and avoid banking or entering passwords on it.

Sinful content and unsafe sites are traps. Psalm 101:3 says, I will set no wicked thing before mine eyes. Use filters, ask for accountability and turn away from what harms you.

Your task: (1) List five kinds of personal information to protect. (2) Create an example of a strong passphrase that is not your real password. (3) Explain multifactor authentication.""",
 script="""Welcome back. Listen, Proverbs 22:3 says, A prudent man foreseeth the evil, and hideth himself. And Proverbs 4:23 says, Keep thy heart with all diligence; for out of it are the issues of life. Online safety protects your heart, your mind and your family.

Now watch this. Protect personal information: your full name, address, school, phone number, passwords and birth date. Turn off location sharing unless you need it. People online may not be who they say they are. Never meet someone you only know online, and tell a trusted adult if a stranger contacts you.

A strong password is long, at least twelve to sixteen characters, and unique. A passphrase of several unrelated words is easy to remember and hard to guess. Never reuse or share it. A password manager can help.

Turn on multifactor authentication. After the password, the account asks for a second proof, like a code sent to your phone.

Review privacy settings. Keep software updated. Be careful on public WiFi.

Psalm 101:3 says, I will set no wicked thing before mine eyes. Use filters and accountability.

Your task is to list personal information, create a sample passphrase and explain multifactor authentication. Take the four question check.""" + CLOSE,
 quiz=[
 ("A strong password is generally:", ["Long and unique", "Short and easy", "Your birthday", "The word password"], 0, "Length and uniqueness protect accounts."),
 ("Multifactor authentication adds:", ["A second proof of identity", "A louder alarm", "More storage", "A faster screen"], 0, "It asks for another proof after the password."),
 ("Which should you NOT post publicly?", ["Your home address and passwords", "A Bible verse you like", "A school achievement without private details", "A sermon quote"], 0, "Private details can be misused."),
 ("If a stranger online asks you for photos or secrets, you should:", ["Tell a parent or trusted adult", "Send them", "Keep it a secret", "Meet them"], 0, "A trusted adult can help protect you."),
 ]),
 ],
 assess=dict(t="Assessment 1: Computing Foundations and Digital Citizenship",
 prompt="""Write a report of at least 250 words on computers and responsible technology use. Use complete sentences and label each part. Colossians 3:23 says, And whatsoever ye do, do it heartily, as to the Lord, and not unto men.

Part 1: Explain the computing cycle of input, processing, storage and output. Give an example of each. Define hardware and software, and explain the difference between RAM and storage.
Part 2: Name four jobs of an operating system and three examples of operating systems. Match five file extensions with their file types, and describe a folder system you would use for school work.
Part 3: Describe your backup plan using the rule of three copies, two kinds of storage and one different location.
Part 4: Define digital footprint, plagiarism and copyright. Explain the steps you would take if you were bullied online.
Part 5: Describe how to protect personal information, create strong passwords and use multifactor authentication. Explain how Matthew 7:12, Proverbs 22:3 and Philippians 4:8 guide a believer online.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 20 points. Part 3: 10 points. Part 4: 20 points. Part 5: 25 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 1: Whatsoever Ye Would That Men Should Do to You",
 prompt="""Write a post of at least 120 words that (1) describes a time when technology helped you or someone you know, with no names, (2) explains in your own words what it means to be a good digital citizen, (3) explains one habit you will practice to stay safe and kind online, and (4) connects your answer to Matthew 7:12, Ephesians 4:29, Proverbs 22:3 or Philippians 4:8. Then write a respectful reply of at least 40 words to another student's post, or answer this question: How can a Christian use social media to encourage others? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("The CPU is best described as the:", ["Brain that carries out instructions", "Printer", "Cloud", "Password"], 0, "The CPU processes instructions."),
 ("Software that manages the computer and its files is the:", ["Operating system", "Monitor", "Keyboard", "Speaker"], 0, "The OS manages the machine."),
 ("A pdf file is best described as a:", ["Fixed layout document", "Spreadsheet", "Video", "Audio file"], 0, "A pdf keeps its layout."),
 ("Which is an output device?", ["Printer", "Keyboard", "Microphone", "Mouse"], 0, "A printer produces output."),
 ("Ephesians 4:29 teaches that our words should be:", ["Good to the use of edifying", "Sarcastic", "Secret", "Angry"], 0, "Our words should build up."),
 ("The best response to a phishing style message from a stranger is to:", ["Ignore it and tell a trusted adult", "Click the link", "Reply with your password", "Forward it to friends"], 0, "Do not engage with suspicious messages."),
 ("A passphrase is:", ["Several unrelated words used as a long password", "Your name", "A short number", "A shared code"], 0, "Long passphrases are strong and memorable."),
 ("Proverbs 22:3 says a prudent man:", ["Foreseeth the evil, and hideth himself", "Passeth on", "Believeth every word", "Never works"], 0, "Prudence means preparing for danger."),
 ])
