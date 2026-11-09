"""Digital Technology and Computer Applications, Unit 5: Computational Thinking, Coding, Web and Data. Florida standards cited at strand level (SC.912.CS)."""
from dt_units1 import CLOSE

UNIT5 = dict(
 title="Unit 5: Computational Thinking, Coding, Web and Data",
 std="Florida computer science and digital literacy course standards",
 topics=[
 dict(t="5.1 Algorithms and Problem Solving", std="Florida computer science and digital literacy course standards",
 body="""Computer science is not only about using computers. It is about solving problems with clear, logical steps. Proverbs 24:3 says, Through wisdom is an house builded; and by understanding it is established. Good solutions are built with wisdom and understanding.

Computational thinking is a way of solving problems that a person or a computer can carry out. It has four main parts. Decomposition means breaking a big problem into smaller, manageable parts. Pattern recognition means noticing similarities and repeated ideas. Abstraction means focusing on what matters and ignoring unneeded detail. Algorithm design means writing clear steps to solve the problem.

An algorithm is a step by step set of instructions for completing a task. A recipe, a set of directions and the steps to long division are all algorithms. A good algorithm is clear, ordered, finite and correct, which means it ends and produces the right result. Algorithms can be written in plain language, in pseudocode, which looks like code but is written for people to read, or as a flowchart, which uses shapes and arrows. In a flowchart, an oval marks the start and end, a rectangle marks a process, a diamond marks a decision and arrows show the flow.

For example, an algorithm to decide whether to bring an umbrella could be: check the forecast, then if rain is likely, bring an umbrella, or else leave it at home. That uses a sequence, a decision and a result. Three basic structures appear in all algorithms: sequence, which means steps in order, selection, which means choosing between paths, and iteration, which means repeating steps.

Testing and debugging are part of the work. A bug is an error in an algorithm or program. Debugging means finding and fixing it. Test with different inputs, including unusual ones, trace the steps by hand and fix one problem at a time. Mistakes are a normal part of learning, and patience pays off. Galatians 6:9 says, And let us not be weary in well doing: for in due season we shall reap, if we faint not.

Your task: (1) Define the four parts of computational thinking. (2) Draw or describe a flowchart for making a sandwich. (3) Explain what debugging is.""",
 script="""Welcome back. Listen, Proverbs 24:3 says, Through wisdom is an house builded; and by understanding it is established. Good solutions are built with wisdom and understanding.

Now watch this. Computational thinking has four parts. Decomposition breaks a big problem into smaller parts. Pattern recognition notices similarities. Abstraction focuses on what matters and ignores unneeded detail. Algorithm design writes clear steps.

An algorithm is a step by step set of instructions. A recipe is an algorithm. A good algorithm is clear, ordered, finite and correct. You can write it in plain language, in pseudocode or as a flowchart. In a flowchart, ovals mark start and end, rectangles are processes, diamonds are decisions and arrows show the flow.

Every algorithm uses sequence, selection and iteration. Sequence is steps in order. Selection is choosing between paths. Iteration is repeating steps.

A bug is an error. Debugging is finding and fixing it. Test with different inputs, trace the steps by hand and fix one problem at a time. Galatians 6:9 says, let us not be weary in well doing.

Your task is to define the four parts, describe a flowchart and explain debugging. Take the four question check.""" + CLOSE,
 quiz=[
 ("Breaking a large problem into smaller parts is called:", ["Decomposition", "Abstraction", "Debugging", "Encryption"], 0, "Decomposition makes problems manageable."),
 ("A step by step set of instructions to complete a task is an:", ["Algorithm", "Operating system", "Pixel", "Network"], 0, "That defines an algorithm."),
 ("In a flowchart, a diamond usually shows a:", ["Decision", "Start", "Printer", "Password"], 0, "Diamonds mark decisions."),
 ("Finding and fixing errors in a program is:", ["Debugging", "Compiling only", "Formatting", "Backing up"], 0, "Debugging removes bugs."),
 ]),
 dict(t="5.2 Programming Concepts", std="Florida computer science and digital literacy course standards",
 body="""A program is a set of instructions written in a programming language so a computer can carry out a task. Python, JavaScript, Java and Scratch are popular languages. Each has rules, called syntax, that must be followed exactly, because a computer does only what it is told. Proverbs 2:6 says, For the LORD giveth wisdom: out of his mouth cometh knowledge and understanding. Learn patiently, and ask God for wisdom.

The same big ideas appear in nearly every language. A variable is a named place to store a value, such as score equals 85 or name equals Maria. A data type describes the kind of value, such as an integer for whole numbers, a float for decimals, a string for text and a Boolean for true or false. Operators perform actions: arithmetic operators add, subtract, multiply and divide, and comparison operators test whether values are equal or one is larger.

Conditionals let a program make decisions. In Python, an if statement checks a condition and runs code only when it is true, with else covering other cases. For example: if score is at least 70, print Pass, else print Try again. Loops repeat actions. A for loop repeats a set number of times, and a while loop repeats as long as a condition stays true. Loops save effort and keep code short. Be careful to avoid an infinite loop that never ends.

A function is a named block of code that performs a task and can be reused. Functions take inputs, called parameters, and may return an output. Break big programs into small functions. Comments are notes in the code that explain it for humans, and the computer ignores them. Use clear names for variables and functions so others can read your work.

Input and output let programs interact. A program can ask the user to type a value and then display a message. Test programs with different inputs and fix errors, which come in three kinds: syntax errors that break the rules of the language, runtime errors that crash the program and logic errors that give the wrong answer.

Your task: (1) Define variable, string, loop and function. (2) Explain how an if statement works. (3) Describe the three kinds of programming errors.""",
 script="""Welcome back. Listen, Proverbs 2:6 says, For the LORD giveth wisdom: out of his mouth cometh knowledge and understanding. Learn patiently and ask God for wisdom.

Now watch this. A program is a set of instructions in a programming language such as Python, JavaScript, Java or Scratch. Each language has syntax rules, and a computer does only what it is told.

A variable is a named place to store a value. A data type tells the kind of value: an integer for whole numbers, a float for decimals, a string for text, a Boolean for true or false. Operators add, subtract, multiply, divide and compare.

Conditionals make decisions. If the score is at least 70, print Pass, else print Try again. Loops repeat actions. A for loop repeats a set number of times. A while loop repeats while a condition is true. Avoid an infinite loop.

A function is a named block of code you can reuse. Comments explain code to humans.

There are three kinds of errors. Syntax errors break the rules. Runtime errors crash the program. Logic errors give the wrong answer.

Your task is to define terms, explain an if statement and describe the errors. Take the four question check.""" + CLOSE,
 quiz=[
 ("A named place that stores a value in a program is a:", ["Variable", "Router", "Monitor", "Folder"], 0, "Variables store data."),
 ("A data type for text is a:", ["String", "Boolean", "Integer", "Loop"], 0, "Strings hold text."),
 ("A structure that repeats actions is a:", ["Loop", "Comment", "Variable", "Header"], 0, "Loops repeat code."),
 ("An error that causes the program to give the wrong answer without crashing is a:", ["Logic error", "Syntax error", "Power error", "Screen error"], 0, "Logic errors produce wrong results."),
 ]),
 dict(t="5.3 Web Basics: HTML and CSS", std="Florida computer science and digital literacy course standards",
 body="""Every web page you visit is built with code. The three core languages of the web are HTML, CSS and JavaScript. HTML, or HyperText Markup Language, gives a page its structure and content. CSS, or Cascading Style Sheets, controls how the page looks. JavaScript makes the page interactive. In this lesson we focus on HTML and CSS. 1 Corinthians 3:10 says, let every man take heed how he buildeth thereupon. Whoever builds, whether a house, a ministry or a website, should build with care.

HTML uses tags to mark up content. Most tags come in pairs, an opening tag and a closing tag, with content between them. A basic page has these parts. The html element wraps the page. The head holds information such as the title shown on the browser tab. The body holds what visitors see. Inside the body, the h1 tag marks a main heading, h2 marks subheadings, p marks a paragraph, a with an href attribute marks a link, img with src and alt attributes inserts an image, and ul and li make a bulleted list. Always write alt text that describes an image, so that people who use screen readers can understand it.

CSS uses rules with a selector and properties. A rule might select the h1 tag and set its color to navy and its text alignment to center. Other properties include margin and padding for spacing, border for outlines, width and height for size. CSS can be placed in a separate file linked to many pages, so a whole site can change its look from one place. Brand colors, such as the navy and gold of New Life Preparatory Academy, are applied with color codes written in hexadecimal.

Good web design is simple, readable, consistent and accessible. Use clear headings, strong color contrast, readable text size and links that say where they go. Make pages work on phones as well as computers. This is called responsive design. Test your page in a browser, fix errors and view the source.

A website is also a ministry tool. A clear page can tell visitors about service times, give directions and share the gospel. Keep it truthful and keep information current.

Your task: (1) Describe what HTML and CSS each do. (2) Name five HTML tags and what they do. (3) Explain why alt text is important.""",
 script="""Welcome back. Listen, 1 Corinthians 3:10 says, let every man take heed how he buildeth thereupon. Whoever builds, whether a house, a ministry or a website, should build with care.

Now watch this. Web pages are built with HTML, CSS and JavaScript. HTML gives the structure and content. CSS controls how it looks. JavaScript makes it interactive.

HTML uses tags, usually in pairs. The html element wraps the page. The head holds information like the title on the browser tab. The body holds what visitors see. The h1 tag is a main heading. The p tag is a paragraph. The a tag with href makes a link. The img tag inserts an image with src and alt. The ul and li tags make a bulleted list. Always write alt text.

CSS uses a selector and properties. You might select h1 and set its color to navy and center it. Margin and padding control spacing. Border makes outlines. CSS in a separate file can change a whole site from one place.

Good design is simple, readable, consistent and accessible, and it works on phones. That is responsive design.

A website is a ministry tool. Keep it truthful and current.

Your task is to describe HTML and CSS, name five tags and explain alt text. Take the four question check.""" + CLOSE,
 quiz=[
 ("The language that gives a web page its structure is:", ["HTML", "CSS", "Bluetooth", "DNS"], 0, "HTML structures content."),
 ("The language that controls colors and layout is:", ["CSS", "HTML", "HTTPS", "RAM"], 0, "CSS styles the page."),
 ("The tag for the largest heading is:", ["h1", "p", "ul", "img"], 0, "h1 marks the main heading."),
 ("Alt text on an image helps:", ["Screen reader users understand the image", "The image load slower", "Hide the image", "Change the file type"], 0, "Alt text supports accessibility."),
 ]),
 dict(t="5.4 Data, Databases and Artificial Intelligence", std="Florida computer science and digital literacy course standards",
 body="""Data is the fuel of the modern world. Every search, purchase, photo and message creates data. A database is an organized collection of data stored so that it can be searched, sorted and updated quickly. School records, church membership lists, online stores and banks all use databases.

A relational database stores data in tables. A table has rows called records and columns called fields. For example, a students table might have fields for student ID, name, grade and email, with one record for each student. A primary key is a field that uniquely identifies each record, such as a student ID. Tables can be linked by keys, so that a table of courses can connect to a table of students without repeating information. A language called SQL is used to ask a database questions. For example, a query can select the names of all students whose grade is ten.

Databases need care. Data must be accurate, backed up and secure. Access should be limited by roles, so only the right people can view or change sensitive records. Laws and policies protect student and financial data, and leaders must handle it faithfully.

Artificial intelligence, or AI, is technology that lets computers do tasks that usually need human intelligence, such as recognizing speech, translating language, suggesting videos and writing text. Machine learning is a kind of AI in which a computer finds patterns in large amounts of data instead of being given every rule. The data used to teach a model is called training data. If the training data is biased or incomplete, the results can be biased or wrong. Generative AI creates new text, images, audio and code from patterns it has learned.

AI is a powerful tool but not a person. It does not have a soul or a conscience. Genesis 1:27 says, So God created man in his own image, in the image of God created he him. Humans are made in the image of God and are responsible for their choices. We should use AI with honesty, protect privacy, check its answers and never let it replace wisdom, prayer and the counsel of others. Proverbs 3:5 says, Trust in the LORD with all thine heart; and lean not unto thine own understanding.

Your task: (1) Define database, record, field and primary key. (2) Explain how machine learning works in simple terms. (3) Explain why biased training data is a problem.""",
 script="""Welcome back. Listen, Proverbs 3:5 says, Trust in the LORD with all thine heart; and lean not unto thine own understanding. We use technology, but we trust God.

Now watch this. Every search, purchase, photo and message creates data. A database is an organized collection of data that can be searched, sorted and updated quickly. Schools, churches, stores and banks all use them.

A relational database stores data in tables. Rows are records. Columns are fields. A primary key uniquely identifies each record, like a student ID. SQL is used to ask a database questions, like selecting the names of all students in grade ten. Data must be accurate, backed up and secure, with access limited by role.

Artificial intelligence lets computers do tasks that usually need human intelligence. Machine learning finds patterns in large amounts of data. The data used to teach a model is training data. If it is biased or incomplete, the results can be biased or wrong. Generative AI creates new text, images, audio and code.

AI is a tool, not a person. Genesis 1:27 says God created man in his own image. Use AI with honesty, protect privacy, check its answers and never let it replace wisdom and prayer.

Your task is to define database terms, explain machine learning and explain biased data. Take the four question check.""" + CLOSE,
 quiz=[
 ("In a database table, a column is called a:", ["Field", "Record", "Packet", "Router"], 0, "Columns are fields."),
 ("A field that uniquely identifies each record is a:", ["Primary key", "Comment", "Bit", "Font"], 0, "A primary key is unique for each record."),
 ("Data used to teach a machine learning model is called:", ["Training data", "A password", "A backup", "A hyperlink"], 0, "Models learn from training data."),
 ("Biased training data can cause:", ["Biased or wrong results", "Perfect accuracy", "Faster batteries", "Better spelling only"], 0, "Poor data leads to poor results."),
 ]),
 ],
 assess=dict(t="Assessment 5: Computational Thinking, Coding, Web and Data",
 prompt="""Write a report of at least 250 words on computer science basics. Use complete sentences and label each part. Proverbs 24:3 says, Through wisdom is an house builded; and by understanding it is established.

Part 1: Define decomposition, pattern recognition, abstraction and algorithm. Write an algorithm in numbered steps for a simple task, such as brushing teeth or making a sandwich, that uses at least one decision.
Part 2: Define variable, data type, conditional, loop and function. Write pseudocode that checks whether a score is 70 or higher and prints Pass or Try again. Describe the three kinds of programming errors.
Part 3: Describe what HTML and CSS do. Write a short example of an HTML page with a title, a heading, a paragraph and a link, using tags in words if you prefer. Explain alt text and responsive design.
Part 4: Define database, record, field and primary key. Design a table for a church visitor list with five fields and name the primary key.
Part 5: Explain machine learning, training data and bias in simple words. Explain how Genesis 1:27 and Proverbs 3:5 guide a believer in the use of artificial intelligence.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 25 points. Part 3: 20 points. Part 4: 15 points. Part 5: 15 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 5: Through Wisdom Is an House Builded",
 prompt="""Write a post of at least 120 words that (1) describes a problem in your school, home or church that could be solved by breaking it into smaller steps or by a simple program, with no private details, (2) explains in your own words why careful testing and patience matter when you build something, (3) explains one benefit and one danger of artificial intelligence, and (4) connects your answer to Proverbs 24:3, Proverbs 3:5, Genesis 1:27 or 1 Corinthians 3:10. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Should a computer ever make an important decision about a person without human review? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("Which is NOT part of computational thinking?", ["Guessing without a plan", "Decomposition", "Pattern recognition", "Abstraction"], 0, "Computational thinking is planned and logical."),
 ("The three basic structures in algorithms are sequence, selection and:", ["Iteration", "Encryption", "Compression", "Navigation"], 0, "Iteration means repeating steps."),
 ("A Boolean value is:", ["True or false", "A paragraph of text", "A decimal only", "A file name"], 0, "Booleans are true or false."),
 ("A loop that never ends is called an:", ["Infinite loop", "Ending loop", "Backup loop", "Secure loop"], 0, "Infinite loops never stop."),
 ("The language that provides the structure of a web page is:", ["HTML", "CSS", "SQL", "VPN"], 0, "HTML structures the page."),
 ("The tag used to create a link is:", ["a", "p", "h1", "li"], 0, "The anchor tag makes links."),
 ("In a database table, one row is a:", ["Record", "Field", "Key only", "Packet"], 0, "Rows are records."),
 ("Proverbs 3:5 says to trust in the LORD with all thine heart and:", ["Lean not unto thine own understanding", "Trust only in technology", "Avoid all work", "Ignore counsel"], 0, "Faith in God guides our use of tools."),
 ])
