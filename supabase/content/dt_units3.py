"""Digital Technology and Computer Applications, Unit 3: Spreadsheets and Data. Florida standards cited at strand level (SC.912.CS)."""
from dt_units1 import CLOSE

UNIT3 = dict(
 title="Unit 3: Spreadsheets and Data",
 std="SC.912.CS",
 topics=[
 dict(t="3.1 Spreadsheet Basics", std="SC.912.CS",
 body="""A spreadsheet is a program that organizes data in rows and columns and performs calculations. Common programs include Microsoft Excel and Google Sheets. Churches, schools and businesses use spreadsheets for budgets, attendance records, schedules, inventories and grade books. Proverbs 27:23 says, Be thou diligent to know the state of thy flocks, and look well to thy herds. Good records help leaders know the true state of their work.

Learn the parts. A workbook is the whole file, and it holds one or more worksheets, also called sheets or tabs. A worksheet is a grid. A column runs up and down and is labeled with letters. A row runs across and is labeled with numbers. A cell is where a row and a column meet, and each cell has an address called a cell reference, such as B3, which is column B, row 3. A range is a group of cells, written as B2 to B10 with a colon in the program. The active cell is the one you have selected, and the formula bar shows its contents.

Cells can hold text, numbers, dates and formulas. Text labels describe the data, such as Name or Amount. Numbers can be formatted as whole numbers, decimals, currency, percentages or dates. Choose the right format so the data is clear. A column of dollar amounts should show currency symbols, and a date should be recognized as a date.

Plan your sheet before you begin. Put a title at the top, use one row for column headings, put each record in its own row and keep each kind of information in its own column. Do not leave random blank rows or columns in a table. Use bold headings, borders, shading and column width to make it readable. Freeze the top row so headings stay visible when you scroll. Name each worksheet clearly.

Enter data carefully, since one wrong number can make every result wrong. Check your work.

Your task: (1) Explain what a cell reference is and give an example. (2) Define workbook, worksheet, row and column. (3) Design a simple table for a class attendance record.""",
 script="""Welcome back. Listen, Proverbs 27:23 says, Be thou diligent to know the state of thy flocks, and look well to thy herds. Good records help leaders know the true state of their work.

Now watch this. A spreadsheet organizes data in rows and columns and performs calculations. Excel and Google Sheets are examples.

A workbook is the whole file. A worksheet is one tab in it. Columns run up and down and have letters. Rows run across and have numbers. A cell is where a row and column meet. Its address is the cell reference, like B3. A range is a group of cells.

Cells hold text, numbers, dates and formulas. Format numbers as currency, percentages or dates so the data is clear.

Plan before you begin. Put a title at the top. Use one row for headings. Put each record in its own row. Keep each kind of information in its own column. Freeze the top row. Name your sheets.

Enter data carefully. One wrong number can make every result wrong.

Your task is to explain a cell reference, define the parts of a spreadsheet and design an attendance table. Take the four question check.""" + CLOSE,
 quiz=[
 ("The address of the cell in column C, row 5 is:", ["C5", "5C row", "CC5", "R5C"], 0, "Cell references use the column letter then the row number."),
 ("A whole spreadsheet file is called a:", ["Workbook", "Cell", "Range", "Formula"], 0, "A workbook holds one or more worksheets."),
 ("Columns in a spreadsheet are labeled with:", ["Letters", "Numbers only", "Colors", "Symbols"], 0, "Columns use letters; rows use numbers."),
 ("Freezing the top row helps by:", ["Keeping headings visible while scrolling", "Deleting data", "Locking the file forever", "Adding formulas"], 0, "Headings stay in view."),
 ]),
 dict(t="3.2 Formulas and Functions", std="SC.912.CS",
 body="""The real power of a spreadsheet is its ability to calculate. A formula is an instruction that tells the spreadsheet to compute a value. Every formula begins with an equals sign. For example, typing equals B2 plus B3 in a cell adds the values in those two cells. The symbols for math are plus for addition, the minus sign for subtraction, an asterisk for multiplication and a slash for division. Spreadsheets follow the order of operations, so parentheses are done first, then multiplication and division, then addition and subtraction.

The great advantage is that formulas use cell references. If you change a number in B2, every formula using B2 updates automatically. This saves time and reduces errors. Luke 14:28 says, For which of you, intending to build a tower, sitteth not down first, and counteth the cost, whether he have sufficient to finish it? A spreadsheet is a good tool for counting the cost.

A function is a built in formula. The SUM function adds a range. The AVERAGE function finds the mean. MIN finds the smallest value, MAX finds the largest, and COUNT counts the cells that contain numbers. The IF function makes a decision. For example, an IF formula can display Pass when a score is at least 70 and Review when it is lower. Use the formula help in the program to learn others.

Copying a formula changes its references automatically. This is called a relative reference. If you copy a formula down a column, each row uses its own data. Sometimes you need a reference to stay fixed. A dollar sign makes it an absolute reference, as in a tax rate stored in one cell and used in many formulas. A reference like $B$2 does not change when copied.

Learn to read errors. A divide by zero error appears when a formula divides by zero. A reference error appears when a cell used in a formula was deleted. A name error appears when the program does not recognize a function name, often because of a typing mistake. Check your formulas, test them with simple numbers, and compare results to your own estimate.

Your task: (1) Write the formula to add cells B2 through B6 using a function. (2) Explain relative and absolute references. (3) Explain what an IF function does.""",
 script="""Welcome back. Listen, Luke 14:28 says, For which of you, intending to build a tower, sitteth not down first, and counteth the cost? A spreadsheet is a good tool for counting the cost.

Now watch this. A formula is an instruction that calculates a value. Every formula begins with an equals sign. Use plus, minus, an asterisk for multiply and a slash for divide. Parentheses are done first, then multiply and divide, then add and subtract.

Formulas use cell references. Change a number and every formula using it updates automatically.

A function is a built in formula. SUM adds a range. AVERAGE finds the mean. MIN is the smallest. MAX is the largest. COUNT counts cells with numbers. IF makes a decision, like showing Pass when a score is at least 70.

A relative reference changes when you copy a formula. An absolute reference with dollar signs, like $B$2, stays fixed.

Learn the errors. Divide by zero. Reference error when a cell was deleted. Name error when a function is mistyped. Test with simple numbers.

Your task is to write a SUM formula, explain relative and absolute references and explain IF. Take the four question check.""" + CLOSE,
 quiz=[
 ("Every spreadsheet formula begins with:", ["An equals sign", "A period", "A dollar sign", "A quotation mark"], 0, "Formulas start with equals."),
 ("Which function adds a range of numbers?", ["SUM", "COUNT", "MIN", "IF"], 0, "SUM totals values."),
 ("A reference that does not change when copied is:", ["Absolute", "Relative", "Broken", "Hidden"], 0, "Dollar signs make references absolute."),
 ("The AVERAGE of 10, 20 and 30 is:", ["20", "60", "10", "30"], 0, "60 divided by 3 equals 20."),
 ]),
 dict(t="3.3 Charts and Data Visualization", std="SC.912.CS",
 body="""Numbers are easier to understand when they are shown in a picture. A chart turns data into a visual that reveals patterns, comparisons and trends. Habakkuk 2:2 says, Write the vision, and make it plain upon tables, that he may run that readeth it. A good chart makes information plain.

Choose the right chart for the job. A column or bar chart compares amounts among categories, such as attendance by service or giving by month. A line chart shows change over time, such as weekly attendance across a year. A pie chart shows parts of a whole, such as a budget, and works best with a small number of slices that add to one hundred percent. A scatter chart shows the relationship between two numbers, such as hours studied and test score. Choose the simplest chart that tells the story.

Build a chart in steps. Organize your data in a clear table with headings. Select the data. Insert the chart type. Then improve it. Add a clear title that says what the chart shows. Label the axes, including units such as dollars or people. Add a legend when there is more than one data series. Use readable colors with good contrast, and consider people who have trouble telling certain colors apart. Remove clutter such as heavy gridlines and three dimensional effects that make values hard to read.

Charts can mislead, so be honest. Proverbs 14:15 says, The simple believeth every word: but the prudent man looketh well to his going. A bar chart that starts its vertical axis above zero can make a small difference look huge. Leaving out part of the data, using uneven scales or choosing only favorable dates can mislead the reader. Proverbs 11:1 says, A false balance is abomination to the LORD: but a just weight is his delight. Present data truthfully and cite where it came from.

A dashboard combines several charts and key numbers on one page so leaders can see how things stand at a glance.

Your task: (1) Match four chart types to the data they show best. (2) List five parts of a good chart. (3) Give one example of a misleading chart and explain how to fix it.""",
 script="""Welcome back. Listen, Habakkuk 2:2 says, Write the vision, and make it plain upon tables, that he may run that readeth it. A good chart makes information plain.

Now watch this. A chart turns data into a picture that shows patterns and trends.

Choose the right chart. A column or bar chart compares categories. A line chart shows change over time. A pie chart shows parts of a whole, with a few slices that total one hundred percent. A scatter chart shows the relationship between two numbers.

To build one, organize your data, select it, insert the chart, then improve it. Add a clear title. Label the axes with units. Add a legend when needed. Use readable colors. Remove clutter.

Be honest. Proverbs 14:15 says, The simple believeth every word: but the prudent man looketh well to his going. A bar chart that does not start at zero can make a small difference look huge. Proverbs 11:1 says, a just weight is his delight. Show data truthfully and cite the source.

A dashboard combines charts and key numbers on one page.

Your task is to match charts to data, list the parts of a good chart and fix a misleading chart. Take the four question check.""" + CLOSE,
 quiz=[
 ("Which chart best shows change over time?", ["Line chart", "Pie chart", "Photograph", "Table of contents"], 0, "Line charts show trends over time."),
 ("A pie chart is best for showing:", ["Parts of a whole", "Hourly change", "Two unrelated lists", "A password"], 0, "Pie slices represent shares of a total."),
 ("A chart title should:", ["Say what the chart shows", "Be left blank", "Use only symbols", "Hide the data"], 0, "Titles explain the chart."),
 ("A vertical axis that starts far above zero on a bar chart can:", ["Exaggerate small differences", "Make data more accurate", "Remove errors", "Print faster"], 0, "Truncated axes can mislead."),
 ]),
 dict(t="3.4 Data Analysis and Data Ethics", std="SC.912.CS",
 body="""Data is facts and figures collected for a purpose. Data analysis is the process of cleaning, organizing and studying data to answer questions and make decisions. Proverbs 18:13 says, He that answereth a matter before he heareth it, it is folly and shame unto him. Wise leaders look at the facts before they decide.

Begin by cleaning the data. Look for typing errors, misspelled names, inconsistent formats such as two ways of writing the same date, blank cells and duplicate records. Dirty data produces wrong answers. Keep an untouched copy of the original data, and do your cleaning on a copy.

Learn core tools. Sorting puts rows in order, such as from the highest amount to the lowest or by last name. Filtering shows only the rows that meet a condition, such as members who attended in March. Conditional formatting colors cells that meet a rule, such as turning a low balance red. A pivot table summarizes large data, for example totalling giving by month or counting students by grade. Formulas such as SUMIF and COUNTIF add or count only items that meet a condition.

Ask good questions and read results carefully. What is the data telling you? What does it not tell you? A pattern does not always show cause. Two things can happen together without one causing the other. Be careful about small samples and about numbers with no context. Check that your conclusions follow from the evidence.

Data ethics matters because data often concerns people. Collect only what you need, and protect it. Sensitive information such as financial records, health information, student records and attendance of minors must be kept private and shared only with those who have a right to see it. Get permission when you collect data about others. Protect files with passwords and limited access. Avoid bias by not choosing data that supports only what you hope to find. Report honestly, including results you did not expect. Exodus 20:16 says, Thou shalt not bear false witness against thy neighbour.

Your task: (1) List four steps in cleaning data. (2) Explain the difference between sorting and filtering. (3) Describe two ways to protect private data.""",
 script="""Welcome back. Listen, Proverbs 18:13 says, He that answereth a matter before he heareth it, it is folly and shame unto him. Wise leaders look at the facts before they decide.

Now watch this. Data analysis means cleaning, organizing and studying data to answer questions. Start by cleaning. Look for typing errors, inconsistent formats, blank cells and duplicates. Keep an untouched copy of the original.

Sorting puts rows in order. Filtering shows only the rows that meet a condition. Conditional formatting colors cells that meet a rule. A pivot table summarizes large data. SUMIF and COUNTIF add or count only what meets a condition.

Ask good questions. Two things can happen together without one causing the other. Be careful with small samples and numbers with no context.

Data ethics matters. Collect only what you need and protect it. Financial records, health information and student records are private. Get permission. Use passwords and limited access. Do not choose data to support only what you hope to find. Exodus 20:16 says, Thou shalt not bear false witness.

Your task is to list steps for cleaning data, compare sorting and filtering and describe two ways to protect private data. Take the four question check.""" + CLOSE,
 quiz=[
 ("Showing only the rows that meet a condition is called:", ["Filtering", "Sorting", "Freezing", "Backing up"], 0, "A filter hides rows that do not match."),
 ("Duplicate records and typing errors are examples of:", ["Dirty data", "Clean data", "Charts", "Passwords"], 0, "They must be fixed before analysis."),
 ("A pivot table is used to:", ["Summarize large data", "Delete files", "Change the font", "Send email"], 0, "Pivot tables summarize and group data."),
 ("Student records and financial records should be:", ["Kept private and protected", "Posted online", "Shared with everyone", "Left unlocked"], 0, "Sensitive data needs protection."),
 ]),
 ],
 assess=dict(t="Assessment 3: Spreadsheets and Data",
 prompt="""Write a report of at least 250 words, with calculations, on spreadsheets and data. Use complete sentences and label each part. Proverbs 27:23 says, Be thou diligent to know the state of thy flocks, and look well to thy herds.

Part 1: Explain the terms workbook, worksheet, cell, cell reference, row, column and range. Design a table for a church attendance record with at least five column headings.
Part 2: A set of five weekly attendance numbers is 45, 52, 38, 60 and 55. Calculate the sum, the average, the minimum and the maximum by hand, and write the spreadsheet function you would use for each.
Part 3: Explain relative and absolute references, and write an IF formula idea that shows Pass when a score is 70 or higher.
Part 4: Choose the best chart type for each of these: giving by month, parts of a budget, attendance across a year, and hours studied against test score. Explain how a chart can mislead and how to prevent it.
Part 5: Describe four steps for cleaning data, explain sorting, filtering and pivot tables, and describe how to protect private data. Apply Proverbs 18:13 and Exodus 20:16.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 25 points. Part 3: 15 points. Part 4: 20 points. Part 5: 15 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 3: Look Well to Thy Herds",
 prompt="""Write a post of at least 120 words that (1) describes a record or list that a church, team or family might keep in a spreadsheet, with no private details, (2) explains in your own words why accurate records matter, (3) explains why honest charts and careful handling of private data are matters of integrity, and (4) connects your answer to Proverbs 27:23, Proverbs 11:1, Proverbs 18:13 or Exodus 20:16. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Who should be allowed to see the attendance and giving records of a church? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("A spreadsheet cell reference is made up of:", ["A column letter and a row number", "Two letters", "A password", "A file extension"], 0, "For example, D7."),
 ("The formula that adds cells B2 to B6 uses the function:", ["SUM", "COUNT", "MIN", "PRINT"], 0, "SUM adds a range."),
 ("The AVERAGE of 40, 50 and 60 is:", ["50", "150", "40", "60"], 0, "150 divided by 3 equals 50."),
 ("The symbols $B$2 show a:", ["Absolute reference", "Relative reference", "Chart", "Filter"], 0, "Dollar signs fix the reference."),
 ("The best chart for parts of a budget is a:", ["Pie chart", "Line chart", "Scatter chart only", "Bar code"], 0, "A pie shows shares of a whole."),
 ("A chart axis that starts well above zero on a bar chart may:", ["Mislead the reader", "Improve honesty", "Fix the data", "Protect privacy"], 0, "Truncated axes exaggerate differences."),
 ("Before analyzing data, it is wise to:", ["Clean it and keep a copy of the original", "Delete the original", "Ignore errors", "Publish it"], 0, "Clean on a copy."),
 ("Exodus 20:16 forbids:", ["Bearing false witness", "Working hard", "Saving data", "Using charts"], 0, "Data must be reported truthfully."),
 ])
