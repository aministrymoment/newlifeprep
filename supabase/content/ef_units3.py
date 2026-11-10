"""Economics with Financial Literacy, Unit 3: Financial Literacy."""
from ef_units1 import CLOSE, S1, S2, S3

UNIT3 = dict(
 title="Unit 3: Financial Literacy",
 std=S3,
 topics=[
 dict(t="3.1 Budgeting, Saving and Emergency Funds", std=S3,
 body="""A budget is a plan for your money. It lists your income and your expenses so that you decide where every dollar goes before you spend it. Fixed expenses, such as rent, stay the same each month. Variable expenses, such as food and gas, change. Discretionary spending covers wants. A simple starting guide is to give first, then plan about half of income for needs, about thirty percent for wants and about twenty percent for saving and debt payments. Adjust the percentages to your situation.

To build a budget, follow these steps: list your net income, list your fixed and variable expenses, set savings and giving goals, track your spending for a month, then compare plans to actual results and adjust. Apps and spreadsheets help, but the habit matters more than the tool. Pay yourself first by moving savings aside as soon as you are paid.

Saving prepares you for the unexpected and for goals. An emergency fund is money set aside for surprises such as a car repair or a lost job. Many advisors suggest working toward three to six months of basic expenses, starting with a smaller goal such as one thousand dollars. Keep it in a safe, easy to reach account, such as an insured savings account. Short term goals, such as a phone or a trip, and long term goals, such as college or a home, each need their own plan.

Scripture praises planning. Proverbs 21:20 says, There is treasure to be desired and oil in the dwelling of the wise; but a foolish man spendeth it up. Proverbs 13:11 says, Wealth gotten by vanity shall be diminished: but he that gathereth by labour shall increase. Proverbs 6:6 says, Go to the ant, thou sluggard; consider her ways, and be wise.

Worked example: a teen earns two hundred dollars a month, gives twenty, saves forty and spends the rest by plan. Common mistake: having no plan and wondering where the money went.

Your task: (1) Define budget, fixed expense and variable expense. (2) List the steps to make a budget. (3) Create a sample monthly budget for a two hundred dollar income that includes giving and saving.""",
 script="""Welcome back. Listen, this unit is about the money in your own hands.

A budget is a plan for your money. It lists income and expenses so you decide where every dollar goes before you spend it. Fixed expenses stay the same each month. Variable expenses change. A simple guide is to give first, then plan about half for needs, thirty percent for wants and twenty percent for saving and debt payments.

Now watch this. To build a budget, list your net income, list your expenses, set savings and giving goals, track your spending for a month and adjust. Pay yourself first by moving savings aside when you are paid.

An emergency fund covers surprises like a car repair or a lost job. Start with a goal like one thousand dollars and work toward three to six months of basic expenses. Keep it in a safe, insured account.

Proverbs 21:20 says, There is treasure to be desired and oil in the dwelling of the wise; but a foolish man spendeth it up. Proverbs 13:11 says, he that gathereth by labour shall increase.

Your task is to define budget terms, list the steps and make a sample budget. Take the four question check.""" + CLOSE,
 quiz=[
 ("A budget is:", ["A plan for your income and expenses", "A kind of loan", "A tax form", "A bank fee"], 0, "It tells your money where to go."),
 ("An emergency fund is meant for:", ["Unexpected costs", "Shopping sales", "Vacations only", "Gifts only"], 0, "It prevents debt during surprises."),
 ("Paying yourself first means:", ["Setting savings aside when you are paid", "Spending first", "Skipping bills", "Borrowing"], 0, "Saving is planned, not leftover."),
 ("Rent is usually a:", ["Fixed expense", "Variable expense", "Gift", "Tax"], 0, "It stays the same each month."),
 ]),
 dict(t="3.2 Banking, Credit, Debt and Credit Scores", std=S3,
 body="""Banks and credit unions offer checking accounts for daily spending and savings accounts that earn interest. Learn the fees, minimum balances and overdraft rules, and check that the institution is insured by the FDIC or, for credit unions, the NCUA. Debit cards take money directly from your account. Credit cards borrow money that you must repay.

Credit means borrowing with a promise to repay, usually with interest. The annual percentage rate, or APR, is the yearly cost of borrowing. If you carry a balance on a credit card with a twenty percent APR, a thousand dollars of debt costs about two hundred dollars a year in interest, and paying only the minimum can keep you in debt for years. Pay the full statement balance each month and you avoid interest. In the United States, a person under twenty one must show income or have a cosigner to get a credit card. Loans such as car loans and student loans also carry interest and fees, so compare the total cost before borrowing.

Your credit score, usually from 300 to 850, helps lenders decide whether to lend to you and at what rate. The main factors are payment history, the amount you owe compared with your limits, the length of your credit history, new credit applications, and the mix of credit types. Pay on time every time, keep balances low, and check your free credit reports at AnnualCreditReport.com.

Scripture warns about debt. Proverbs 22:7 says, The rich ruleth over the poor, and the borrower is servant to the lender. Romans 13:8 says, Owe no man any thing, but to love one another: for he that loveth another hath fulfilled the law. Debt is not always a sin, but it is a serious commitment, and Christians keep their word and repay what they borrow. Psalm 37:21 says, The wicked borroweth, and payeth not again.

Worked example: you pay only the minimum on a card and the balance grows because interest is added. Common mistake: thinking that a credit limit is money you can afford to spend.

Your task: (1) Define APR and credit score. (2) List three factors in a credit score. (3) Explain how to use a credit card without paying interest.""",
 script="""Welcome back. Listen, credit can be a tool or a trap, and you must know the difference.

Banks and credit unions offer checking and savings accounts. Learn the fees and be sure the institution is insured. A debit card takes money from your account. A credit card borrows money you must repay.

The annual percentage rate, or APR, is the yearly cost of borrowing. At twenty percent, a thousand dollars of card debt costs about two hundred dollars a year in interest. Paying only the minimum keeps you in debt for years. Pay the full statement balance and you avoid interest.

Now watch this. Your credit score runs from 300 to 850. The main factors are payment history, the amount you owe compared with your limits, the length of your history, new credit and your mix of credit. Pay on time and keep balances low.

Proverbs 22:7 says, the borrower is servant to the lender. Romans 13:8 says, Owe no man any thing, but to love one another. Psalm 37:21 says, The wicked borroweth, and payeth not again. Keep your word.

Your task is to define APR and credit score, list three factors and explain how to avoid card interest. Take the four question check.""" + CLOSE,
 quiz=[
 ("APR stands for:", ["Annual percentage rate", "Average payment ratio", "Account payment record", "Annual profit report"], 0, "It is the yearly cost of borrowing."),
 ("The most important way to protect your credit score is:", ["Paying on time", "Opening many cards", "Ignoring bills", "Maxing out cards"], 0, "Payment history carries the most weight."),
 ("To avoid credit card interest you should:", ["Pay the full statement balance each month", "Pay only the minimum", "Skip payments", "Use the limit fully"], 0, "No balance carried means no interest."),
 ("Romans 13:8 says:", ["Owe no man any thing", "Borrow freely", "Spend quickly", "Trust riches"], 0, "Debt is a serious commitment."),
 ]),
 dict(t="3.3 Investing, Compound Interest and Risk", std=S3,
 body="""Saving keeps money safe. Investing puts money to work to grow over a long time, with the risk that the value can go down. Simple interest is paid only on the original amount. Compound interest is paid on the original amount plus the interest already earned, so growth speeds up over time. The earlier you start, the more time works for you.

A quick way to estimate is the rule of 72. Divide 72 by the annual rate of return to find about how many years it takes money to double. At 8 percent, 72 divided by 8 is 9, so money roughly doubles in nine years. At 4 percent it takes about eighteen years. The same rule shows how fast debt can grow at a high interest rate.

Common investments include stocks, which are shares of ownership in a company, bonds, which are loans to governments or companies, and mutual funds and exchange traded funds, which hold many investments in one package. In general, higher possible returns come with higher risk. Diversification means spreading money across many investments so that one failure does not ruin you. Fees matter too, because they reduce returns every year. Retirement accounts such as a 401(k) at work or an IRA offer tax advantages, and if an employer offers a match, that is free money worth capturing.

Scripture supports diversifying and warns against get rich quick schemes. Ecclesiastes 11:2 says, Give a portion to seven, and also to eight; for thou knowest not what evil shall be upon the earth. Proverbs 28:20 says, A faithful man shall abound with blessings: but he that maketh haste to be rich shall not be innocent. Be wary of anyone who promises guaranteed high returns, because that is a classic sign of fraud.

Worked example: one thousand dollars at 8 percent doubles to about two thousand in nine years and to about four thousand in eighteen years. Common mistake: waiting to start because the amount is small.

Your task: (1) Explain compound interest. (2) Use the rule of 72 to estimate doubling time at 6 percent. (3) Explain diversification and name two warning signs of an investment scam.""",
 script="""Welcome back. Listen, saving protects your money, and investing helps it grow.

Compound interest is interest on your original amount plus the interest you already earned. Growth speeds up over time, so start early. The rule of 72 estimates doubling time. Divide 72 by the annual return. At 8 percent, money doubles in about nine years.

Now watch this. A stock is a share of ownership in a company. A bond is a loan to a government or company. A mutual fund or exchange traded fund holds many investments in one package. Higher possible returns come with higher risk. Diversification spreads your money so one failure does not ruin you. Watch the fees, and capture any employer match in a retirement plan.

Ecclesiastes 11:2 says, Give a portion to seven, and also to eight; for thou knowest not what evil shall be upon the earth. Proverbs 28:20 says, he that maketh haste to be rich shall not be innocent. Guaranteed high returns are a sign of fraud.

Your task is to explain compound interest, use the rule of 72 at 6 percent and explain diversification and two scam warnings. Take the four question check.""" + CLOSE,
 quiz=[
 ("Compound interest is paid on:", ["The original amount plus earned interest", "The original amount only", "Taxes", "Fees"], 0, "Growth builds on growth."),
 ("By the rule of 72, money at 8 percent doubles in about:", ["9 years", "2 years", "20 years", "72 years"], 0, "72 divided by 8 is 9."),
 ("Diversification means:", ["Spreading money across many investments", "Putting everything in one stock", "Avoiding all risk", "Borrowing to invest"], 0, "It reduces the harm of one failure."),
 ("A sign of an investment scam is:", ["Guaranteed high returns", "Clear fees", "Public records", "Slow growth"], 0, "No honest investment can guarantee high returns."),
 ]),
 dict(t="3.4 Taxes, Insurance, Fraud Protection and Giving", std=S3,
 body="""Most workers file a federal income tax return each year, usually by mid April, using information from forms such as the W2. You report income, claim deductions and credits you qualify for, and either pay more or receive a refund if too much was withheld. A refund is your own money returned, not a bonus. Keep records, file on time and be honest, because tax fraud is a crime.

Insurance protects you from large losses by sharing risk among many people. You pay a premium, and if a covered loss happens the insurer pays, after you pay your deductible. Common types are health, auto, renters or homeowners, and life insurance. Florida requires drivers to carry certain minimum auto coverages, and renters insurance is inexpensive protection for belongings. Choose coverage you need, compare quotes and read what is excluded.

Fraud and identity theft are growing threats. Phishing uses fake emails, texts or calls that pretend to be a bank, a school or a government office to steal your information. Warning signs include pressure to act now, requests for gift cards, wire transfers or payment apps from strangers, and prizes you never entered to win. Protect yourself: never share your Social Security number, passwords or one time codes; use strong, different passwords and two step verification; check statements often; and freeze your credit if your information is stolen. Report scams to the Federal Trade Commission at ReportFraud.ftc.gov. Proverbs 14:15 teaches wisdom: The simple believeth every word: but the prudent man looketh well to his going.

God's people are also called to give. Malachi 3:10 says, Bring ye all the tithes into the storehouse, that there may be meat in mine house, and prove me now herewith, saith the LORD of hosts, if I will not open you the windows of heaven, and pour you out a blessing, that there shall not be room enough to receive it. 2 Corinthians 9:7 says, Every man according as he purposeth in his heart, so let him give; not grudgingly, or of necessity: for God loveth a cheerful giver. Giving is worship and trust, not a way to buy wealth. Generosity also includes helping the poor and supporting your church.

Worked example: a teen gets a text saying a package needs a fee paid by gift card. This is a scam, so delete it and tell a trusted adult. Common mistake: acting quickly under pressure.

Your task: (1) Define premium and deductible. (2) List four ways to protect yourself from fraud. (3) Write a personal giving plan that includes your church and a service project.""",
 script="""Welcome back. Listen, this lesson helps you keep what God has entrusted to you and use it well.

Most workers file a federal tax return each year, usually by mid April. A refund is your own money returned, not a bonus. Keep records and be honest.

Insurance shares risk. You pay a premium, and if a covered loss happens the insurer pays after you pay your deductible. Common types are health, auto, renters and life. Florida requires drivers to carry certain minimum auto coverages.

Now watch this. Phishing uses fake emails, texts and calls to steal your information. Be alert to pressure to act now, requests for gift cards or payment apps, and prizes you never entered to win. Never share your Social Security number, passwords or codes. Use strong passwords and two step verification. Report scams to the Federal Trade Commission. Proverbs 14:15 says, the prudent man looketh well to his going.

God also calls us to give. Malachi 3:10 says, Bring ye all the tithes into the storehouse, that there may be meat in mine house, and prove me now herewith, saith the LORD of hosts. Second Corinthians 9:7 says, God loveth a cheerful giver. Giving is worship and trust, not a way to buy wealth.

Your task is to define premium and deductible, list four fraud protections and write a giving plan. Take the four question check.""" + CLOSE,
 quiz=[
 ("A premium is:", ["The regular price you pay for insurance", "A tax refund", "A prize", "A loan"], 0, "Premiums buy protection."),
 ("A deductible is:", ["The amount you pay before insurance pays", "A bank fee", "A tax form", "A discount"], 0, "It is your share of a covered loss."),
 ("A sign of a phishing scam is:", ["Pressure to act now or pay with gift cards", "A clear statement", "A bank letter you expected", "A school notice"], 0, "Scammers use urgency."),
 ("2 Corinthians 9:7 says God loveth:", ["A cheerful giver", "A quick spender", "A hidden saver", "A proud lender"], 0, "Giving should come from the heart."),
 ]),
 ],
 assess=dict(t="Assessment 3: Financial Literacy",
 prompt="""Write a report of at least 250 words on financial literacy. Use complete sentences and label each part. Proverbs 21:5 says, The thoughts of the diligent tend only to plenteousness; but of every one that is hasty only to want.

Part 1: Create a sample monthly budget for a net income of one thousand dollars that includes giving, saving and both fixed and variable expenses, and explain your choices.
Part 2: Explain an emergency fund and how you would build one.
Part 3: Explain APR, credit scores and how to use credit wisely, with reference to Romans 13:8 or Proverbs 22:7.
Part 4: Explain compound interest, the rule of 72, and diversification. Use the rule of 72 to estimate doubling time at 9 percent.
Part 5: Explain insurance, two fraud protections and your personal plan for giving.""",
 rubric="""100 points. Part 1: 25 points. Part 2: 10 points. Part 3: 20 points. Part 4: 20 points. Part 5: 20 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 3: Faithful Stewards",
 prompt="""Write a post of at least 120 words that (1) describes one money habit you want to build this year, (2) explains the first step you will take, (3) names one scam or money trap teens should avoid, and (4) connects your answer to Proverbs 21:20, Romans 13:8 or 2 Corinthians 9:7. Then write a respectful reply of at least 40 words to another student's post, or answer this question: How can saving and giving work together?"""),
 unit_quiz=[
 ("A budget helps you decide:", ["Where every dollar goes before you spend it", "Which stocks will rise", "How to avoid all taxes", "When to borrow"], 0, "Planning prevents waste."),
 ("A three to six month emergency fund is meant to cover:", ["Basic expenses", "Entertainment", "Luxury items", "Investments only"], 0, "It protects against job loss or surprises."),
 ("Credit scores usually range from:", ["300 to 850", "1 to 10", "0 to 100", "500 to 5000"], 0, "Higher scores earn better rates."),
 ("Paying only the minimum on a credit card balance usually:", ["Keeps you in debt longer", "Eliminates interest", "Raises your credit limit", "Saves money"], 0, "Interest keeps growing."),
 ("Using the rule of 72, money at 6 percent doubles in about:", ["12 years", "6 years", "72 years", "2 years"], 0, "72 divided by 6 is 12."),
 ("Diversification reduces:", ["The harm if one investment fails", "All taxes", "Your income", "Interest"], 0, "Do not put everything in one place."),
 ("Insurance works by:", ["Sharing risk among many people", "Guaranteeing profit", "Avoiding all loss", "Replacing savings"], 0, "Many pay premiums so a few can be covered."),
 ("Malachi 3:10 and 2 Corinthians 9:7 teach that giving is:", ["An act of worship and trust", "A way to guarantee wealth", "A requirement of the tax code", "A tax"], 0, "Give with a cheerful heart."),
 ],
)
