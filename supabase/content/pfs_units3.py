"""Personal Finance and Stewardship, Unit 3: Banking, Payments, Fraud and Interest. Florida financial literacy standards (SS.912.FL) cited at strand level; recheck exact benchmark codes at CPALMS."""
from pfs_units1 import CLOSE

UNIT3 = dict(
 title="Unit 3: Banking, Payments, Fraud and Interest",
 std="SS.912.FL",
 topics=[
 dict(t="3.1 Banks, Credit Unions and Accounts", std="SS.912.FL",
 body="""Financial institutions keep money safe and help it move. Proverbs 27:23 reminds us to look well to what we manage, and a safe place for money is part of good care. The main kinds of institutions are banks, which are for profit businesses owned by shareholders, and credit unions, which are nonprofit cooperatives owned by their members. Online banks have no branches and often charge lower fees.

A checking account is for everyday spending. Money can be deposited, and withdrawn by debit card, check or electronic transfer. A savings account is for money you do not plan to use soon and usually pays interest. A money market account and a certificate of deposit, or CD, may pay higher interest, but a CD locks your money for a set term, and withdrawing early costs a penalty.

Deposits are protected. The Federal Deposit Insurance Corporation, or FDIC, insures deposits at member banks, and the National Credit Union Administration, or NCUA, insures deposits at federal credit unions. The standard coverage is up to 250,000 dollars per depositor, per insured institution, per ownership category. Always confirm that an institution is insured.

Before opening an account, compare features: monthly fees and how to avoid them, minimum balance requirements, interest rates, overdraft policies, ATM access, mobile banking and customer service. Read the account agreement and fee schedule. Minors usually need a parent or guardian as a joint owner or custodian to open an account.

Good account habits include checking balances often, setting up alerts, using strong passwords with two step verification, and never sharing your PIN. Keep your savings in a separate account from your spending so that you are not tempted. Reconcile your account each month by comparing your records with the bank statement.

Your task: (1) Compare a bank and a credit union. (2) Describe checking, savings and a CD. (3) Explain what FDIC insurance covers.""",
 script="""Welcome back. Listen, Proverbs 27:23 says, Be thou diligent to know the state of thy flocks. A safe place for money is part of good care.

Now watch this. Banks are for profit businesses. Credit unions are nonprofit cooperatives owned by members. Online banks have no branches and often lower fees.

Checking is for everyday spending. Savings is for money you will not use soon and pays interest. A CD locks money for a set term, and early withdrawal costs a penalty.

Deposits are protected. The FDIC insures bank deposits and the NCUA insures federal credit union deposits, up to 250,000 dollars per depositor, per institution, per ownership category. Confirm that the institution is insured.

Compare fees, minimums, interest, overdraft rules, ATM access and mobile banking. Read the fee schedule. Minors usually need a parent as joint owner.

Check balances, set alerts, use strong passwords and never share your PIN. Reconcile your account each month.

Your task is to compare banks and credit unions, describe account types and explain FDIC insurance. Take the four question check.""" + CLOSE,
 quiz=[
 ("A nonprofit financial cooperative owned by its members is a:", ["Credit union", "Stock exchange", "Pawn shop", "Payday lender"], 0, "Credit unions are member owned."),
 ("Deposits at member banks are insured by the:", ["FDIC", "NFL", "FDA", "EPA"], 0, "The FDIC insures bank deposits."),
 ("An account that locks your money for a set term at a fixed rate is a:", ["CD", "Checking account", "Debit card", "Credit card"], 0, "A certificate of deposit has a fixed term."),
 ("Comparing your records with your bank statement each month is called:", ["Reconciling", "Overdrawing", "Refinancing", "Withholding"], 0, "Reconciling catches errors."),
 ]),
 dict(t="3.2 Ways to Pay: Cash, Debit, Checks and Apps", std="SS.912.FL",
 body="""People pay in many ways, and each has strengths and risks. Proverbs 11:1 says, A false balance is abomination to the LORD: but a just weight is his delight. Honest, careful payment habits reflect honest character.

Cash is simple and does not create debt, but it can be lost or stolen and it does not leave a record. A debit card takes money directly from your checking account. It is convenient, but if the number is stolen, your own money is at risk right away. A check is a written order to pay. It carries your account and routing numbers, so protect it. Electronic transfers, often called ACH, move money between banks for bills and payroll. Mobile payment and peer to peer apps, such as Zelle or Cash App, send money quickly. Payments sent through them are often hard or impossible to reverse, so send only to people you know and verify the name before you press send.

A prepaid card works only for the amount loaded. A credit card is a loan, and we study it in the next unit.

Overdraft happens when you spend more than your balance. Some banks cover the payment and charge a fee, and some decline the payment. Ask what your bank does, and consider alerts and a small cushion to avoid fees. Never write a check without money to cover it, since a bounced check brings fees and may bring legal trouble.

Protect yourself when paying. Use official websites and apps. Avoid public WiFi for banking. Check receipts and statements for errors. Federal law gives debit and credit card users some protection when fraud is reported quickly, so review statements often and report unauthorized charges at once.

Plan for business too. When you accept payments as a seller, keep records and follow the rules for taxes.

Your task: (1) Compare cash, debit, check and a payment app. (2) Explain overdraft and how to avoid it. (3) List four safe payment habits.""",
 script="""Welcome back. Listen, Proverbs 11:1 says, A false balance is abomination to the LORD: but a just weight is his delight. Honest, careful payment habits reflect honest character.

Now watch this. Cash is simple but can be lost and leaves no record. A debit card takes money straight from checking, so stolen numbers put your own money at risk. A check carries your account and routing numbers. ACH moves money between banks. Payment apps send money fast, and often cannot be reversed. Send only to people you know and verify the name.

A prepaid card works only for the amount loaded. A credit card is a loan, which we study next.

Overdraft means spending more than your balance. Know what your bank does, set alerts and keep a cushion. Never write a check without money to cover it.

Use official websites and apps. Avoid public WiFi for banking. Review statements often and report unauthorized charges at once.

Your task is to compare ways to pay, explain overdraft and list safe habits. Take the four question check.""" + CLOSE,
 quiz=[
 ("A card that takes money directly from your checking account is a:", ["Debit card", "Credit card", "Gift card only", "Store loan"], 0, "Debit uses your own deposited money."),
 ("Spending more than your account balance is called:", ["An overdraft", "A deposit", "A reconciliation", "A refund"], 0, "Overdraft means going below zero."),
 ("Payments sent through peer to peer apps are often:", ["Hard to reverse", "Always refundable", "Free of risk", "Guaranteed"], 0, "Send only to people you know."),
 ("A good habit for online banking is to:", ["Avoid public WiFi", "Share your PIN", "Ignore statements", "Use one weak password"], 0, "Public WiFi is less secure."),
 ]),
 dict(t="3.3 Fraud, Scams and Identity Theft", std="SS.912.FL",
 body="""Criminals target money, and the young are often targeted because they are new to finance. Proverbs 14:15 says, The simple believeth every word: but the prudent man looketh well to his going. Proverbs 22:3 adds, A prudent man foreseeth the evil, and hideth himself: but the simple pass on, and are punished. Caution is wisdom.

Identity theft happens when someone uses your personal information, such as your name, Social Security number, birth date or account numbers, to pretend to be you. Thieves may open accounts, make purchases or file false tax returns. Protect your Social Security number and share it only when required and verified.

Common scams include phishing, when an email, text or call pretends to be a bank or a company and asks you to click a link or give a code. Others include fake prize or lottery notices, fake job offers that ask for money or bank details, romance scams, fake charity appeals, tech support scams, fake check scams that ask you to deposit a check and send some back, and pressure from someone claiming to be a government agency. Warning signs include urgency, secrecy, a demand for gift cards, wire transfers or cryptocurrency, requests for passwords or codes, and promises of guaranteed returns.

Defend yourself. Do not click links in unexpected messages. Contact the company using a number you know is real. Use strong, different passwords and two step verification. Never give out one time codes. Check statements and your credit reports regularly. You can place a free credit freeze with the credit bureaus to block new accounts. Shred papers with personal data. Tell a trusted adult right away if you suspect a scam, since shame keeps victims quiet.

If you are a victim, act quickly. Contact your bank, change passwords, report to the Federal Trade Commission at IdentityTheft.gov or ReportFraud.ftc.gov, and file a police report if advised. Ephesians 4:28 reminds us to labour with honest hands, and Christians should never defraud others.

Your task: (1) Define identity theft. (2) List five warning signs of a scam. (3) Describe the steps to take if your information is stolen.""",
 script="""Welcome back. Listen, Proverbs 14:15 says, The simple believeth every word: but the prudent man looketh well to his going. Caution is wisdom.

Now watch this. Identity theft is when someone uses your name, Social Security number, birth date or account numbers to pretend to be you. Protect your Social Security number.

Common scams are phishing messages, fake prizes, fake job offers, romance scams, fake charities, tech support scams and fake check scams. Warning signs are urgency, secrecy, demands for gift cards, wire transfers or cryptocurrency, requests for passwords or codes, and guaranteed returns.

Defend yourself. Do not click links in unexpected messages. Call a number you know is real. Use strong different passwords and two step verification. Never share one time codes. Check statements and credit reports. Consider a free credit freeze. Shred papers. Tell a trusted adult right away.

If you are a victim, contact your bank, change passwords, report to the Federal Trade Commission at IdentityTheft.gov and file a police report if advised.

Your task is to define identity theft, list scam warning signs and describe recovery steps. Take the four question check.""" + CLOSE,
 quiz=[
 ("A message that pretends to be from a bank to trick you into giving information is:", ["Phishing", "Budgeting", "Saving", "Reconciling"], 0, "Phishing uses fake messages."),
 ("A common warning sign of a scam is:", ["Pressure to act right away", "A written contract you can study", "Time to think", "A known company number"], 0, "Scammers use urgency."),
 ("Where can you report identity theft to the federal government?", ["IdentityTheft.gov", "A social media comment", "A game chat", "A coupon site"], 0, "The Federal Trade Commission runs it."),
 ("A free credit freeze helps by:", ["Blocking new accounts in your name", "Raising your score", "Erasing debt", "Lowering taxes"], 0, "A freeze stops new credit from being opened."),
 ]),
 dict(t="3.4 Interest, Compounding and Inflation", std="SS.912.FL",
 body="""Interest is the price of using money. When you save, the bank pays you interest. When you borrow, you pay interest. Proverbs 13:11 says, Wealth gotten by vanity shall be diminished: but he that gathereth by labour shall increase. Steady growth beats get rich quick schemes.

Simple interest is calculated only on the original amount, called the principal. The formula is interest equals principal times rate times time. If you deposit 1,000 dollars at 5 percent simple interest for 3 years, you earn 1,000 times 0.05 times 3, which is 150 dollars.

Compound interest is calculated on the principal plus interest already earned. The same 1,000 dollars at 5 percent compounded yearly becomes about 1,050 after the first year, 1,102.50 after the second, and 1,157.63 after the third. Compounding speeds growth the longer money stays invested, which is why starting early matters so much. Albert Einstein is often credited with calling compound interest powerful, though the quote is not verified, so treat it as a popular saying and not a fact.

A handy shortcut is the rule of 72. Divide 72 by the annual interest rate to estimate the years needed to double money. At 6 percent, money doubles in about 72 divided by 6, or 12 years. At 9 percent, it doubles in about 8 years.

When comparing accounts, look at the annual percentage yield, or APY, which includes the effect of compounding, for savings. For loans, look at the annual percentage rate, or APR, the yearly cost of borrowing. Higher is better when saving and lower is better when borrowing.

Inflation is the general rise in prices over time. If prices rise 3 percent a year and your savings earn 1 percent, your buying power falls. This is one reason people invest for the long term, which we study in Unit 5.

Your task: (1) Calculate simple interest on 2,000 dollars at 4 percent for 5 years. (2) Explain why compounding rewards starting early. (3) Use the rule of 72 for a rate of 8 percent.""",
 script="""Welcome back. Listen, Proverbs 13:11 says, Wealth gotten by vanity shall be diminished: but he that gathereth by labour shall increase. Steady growth beats get rich quick schemes.

Now watch this. Interest is the price of using money. Simple interest uses only the principal. Interest equals principal times rate times time. A thousand dollars at 5 percent for 3 years earns 150 dollars.

Compound interest uses principal plus the interest already earned. That same thousand at 5 percent compounded yearly becomes about 1,157.63 after 3 years. The longer it stays, the faster it grows. Start early.

The rule of 72 divides 72 by the rate to estimate years to double. At 6 percent, about 12 years. At 9 percent, about 8 years.

For savings look at APY. For loans look at APR. Higher is better when saving. Lower is better when borrowing.

Inflation is the rise in prices over time. If prices rise 3 percent and savings earn 1 percent, your buying power falls.

Your task is to calculate simple interest, explain compounding and use the rule of 72. Take the four question check.""" + CLOSE,
 quiz=[
 ("Simple interest is calculated on:", ["Only the original principal", "Principal plus earned interest", "The tax rate", "Inflation"], 0, "Simple interest ignores earlier interest."),
 ("Interest earned on both principal and past interest is:", ["Compound interest", "Simple interest", "A fee", "A refund"], 0, "That is compounding."),
 ("Using the rule of 72, money at 6 percent doubles in about:", ["12 years", "6 years", "72 years", "3 years"], 0, "72 divided by 6 equals 12."),
 ("A general rise in prices over time is:", ["Inflation", "Deflation", "A deposit", "A budget"], 0, "Inflation reduces buying power."),
 ]),
 ],
 assess=dict(t="Assessment 3: Banking, Payments, Fraud and Interest",
 prompt="""Write a report of at least 250 words, with calculations, on banking and interest. Use complete sentences and label each part. Proverbs 14:15 says, The simple believeth every word: but the prudent man looketh well to his going.

Part 1: Compare a bank and a credit union. Describe checking, savings and a CD, and explain what FDIC and NCUA insurance protect.
Part 2: Compare cash, debit card, check and a payment app. Explain overdraft and how to avoid it, and list four safe payment habits.
Part 3: Define identity theft and phishing. List five warning signs of a scam, and describe the steps to take if your personal information is stolen.
Part 4: Calculate simple interest on 1,500 dollars at 4 percent for 3 years. Calculate the value of 1,000 dollars at 5 percent compounded yearly for 2 years. Use the rule of 72 for an 8 percent rate.
Part 5: Explain APY, APR and inflation. Apply Proverbs 13:11 and Proverbs 22:3 to wise money habits.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 20 points. Part 3: 20 points. Part 4: 20 points. Part 5: 15 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 3: The Prudent Man Looketh Well to His Going",
 prompt="""Write a post of at least 120 words that (1) describes a scam, fake offer or suspicious message that you or someone you know has seen, with no names, (2) explains in your own words how a person can protect personal information, (3) explains why starting to save early helps because of compound interest, and (4) connects your answer to Proverbs 14:15, Proverbs 22:3 or Proverbs 13:11. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why do scammers often use urgency? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("Which account usually pays interest and is meant for money you will not spend soon?", ["Savings account", "Checking account", "Prepaid card", "Debit card"], 0, "Savings accounts pay interest."),
 ("Federal credit unions are insured by the:", ["NCUA", "FDIC only", "IRS", "NASA"], 0, "The NCUA insures federal credit union deposits."),
 ("Standard FDIC coverage is up to how much per depositor, per institution, per ownership category?", ["250,000 dollars", "2,500 dollars", "25,000 dollars", "No limit"], 0, "The standard limit is 250,000 dollars."),
 ("A fee and possible penalty can follow when you:", ["Write a check without enough money", "Save regularly", "Read your statement", "Use a strong password"], 0, "A bounced check brings fees."),
 ("Which is a scam warning sign?", ["A demand to pay with gift cards", "A clear written contract", "Time to compare offers", "A company you called yourself"], 0, "Gift card demands are a common scam sign."),
 ("Simple interest on 1,000 dollars at 5 percent for 3 years is:", ["150 dollars", "50 dollars", "1,150 dollars", "500 dollars"], 0, "1,000 times 0.05 times 3 equals 150."),
 ("The rule of 72 estimates:", ["Years to double money", "Your tax bill", "Your credit score", "Monthly rent"], 0, "Divide 72 by the rate."),
 ("Proverbs 14:15 says the prudent man:", ["Looketh well to his going", "Believeth every word", "Passeth on", "Hides in fear"], 0, "Caution is wisdom."),
 ])
