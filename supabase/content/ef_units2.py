"""Economics with Financial Literacy, Unit 2: The Economy and Consumers."""
from ef_units1 import CLOSE, S1, S2, S3

UNIT2 = dict(
 title="Unit 2: The Economy and Consumers",
 std=S2,
 topics=[
 dict(t="2.1 Measuring the Economy", std=S2,
 body="""Economists measure how well an economy is doing with a few key numbers. Gross domestic product, or GDP, is the total market value of all final goods and services produced within a country in a given year. Real GDP is adjusted for price changes so that we can compare years fairly. Economic growth means real GDP is rising over time, which usually means more jobs and rising living standards.

Inflation is a general rise in prices over time, which lowers the purchasing power of money. The Consumer Price Index, or CPI, tracks the price of a typical basket of goods and services that households buy. If inflation is three percent, something that cost one hundred dollars last year costs about one hundred three dollars this year, so savings sitting in cash buy less. Deflation, a general fall in prices, can also cause trouble.

The unemployment rate is the percent of people in the labor force who are actively looking for work but do not have a job. The labor force counts people who are working or looking, so students, retirees and people who have stopped looking are not counted as unemployed.

The business cycle is the repeating pattern of expansion (growth), peak, contraction (a recession if it is serious and lasting), and trough, followed by recovery. No one can predict the exact timing. Ecclesiastes 3:1 says, To every thing there is a season, and a time to every purpose under the heaven. Joseph's plan in Genesis 41 prepared Egypt for seven good years followed by seven lean years, a wise response to a cycle.

Worked example: if wages rise four percent but prices rise six percent, workers can buy less than before. Common mistake: judging a raise by dollars alone. Compare it to inflation.

Your task: (1) Define GDP, inflation, CPI and the unemployment rate. (2) Name the four phases of the business cycle. (3) Explain why a four percent raise may not be a gain when inflation is six percent.""",
 script="""Welcome back. Listen, to manage wisely you must know how to read the signs of the economy.

Gross domestic product, or GDP, is the total market value of final goods and services produced in a country in a year. When real GDP rises, the economy is growing. Inflation is a general rise in prices, which lowers what your money can buy. The Consumer Price Index tracks the cost of a typical basket of goods.

Now watch this. The unemployment rate is the percent of the labor force who are looking for work but do not have a job. The labor force counts people who are working or looking.

The business cycle moves through expansion, peak, contraction and trough, then recovery. A serious, lasting contraction is a recession. Ecclesiastes 3:1 says, To every thing there is a season, and a time to every purpose under the heaven. Joseph prepared Egypt for seven lean years in Genesis 41. That is wisdom.

If your wages rise four percent and prices rise six percent, you can buy less. Compare a raise with inflation.

Your task is to define GDP, inflation, CPI and unemployment, name the cycle phases and explain the raise example. Take the four question check.""" + CLOSE,
 quiz=[
 ("GDP is the market value of:", ["Final goods and services produced in a country in a year", "All money in banks", "Government debt", "Only exports"], 0, "GDP measures production."),
 ("Inflation is:", ["A general rise in prices", "A fall in prices", "A tax", "A rise in jobs"], 0, "It lowers purchasing power."),
 ("The unemployment rate counts people who:", ["Are looking for work but have no job", "Are retired", "Have stopped looking forever", "Are students only"], 0, "They are in the labor force and seeking work."),
 ("The phases of the business cycle include:", ["Expansion, peak, contraction and trough", "Spring and fall", "Buy and sell", "Tax and spend"], 0, "The cycle repeats."),
 ]),
 dict(t="2.2 Government, Taxes and Trade", std=S2,
 body="""Governments provide public goods such as roads, schools, courts, police and national defense, and pay for them mostly through taxes. Common taxes include income taxes, payroll taxes that fund Social Security and Medicare, sales taxes on purchases, and property taxes on land and buildings. A progressive tax takes a larger percent from higher incomes, a proportional tax takes the same percent from everyone, and a regressive tax takes a larger share of income from lower earners.

Florida does not have a state personal income tax. The state sales tax is six percent, and many counties add a local surtax, so the rate you pay depends on where you buy. Federal income tax still applies to Florida residents. When a government spends more than it collects in a year, it runs a deficit, and the total of past deficits is the national debt. Proverbs 22:7 reminds us that the borrower is servant to the lender, a lesson for nations as well as families.

Jesus taught that citizens have duties. Matthew 22:21 says, Render therefore unto Caesar the things which are Caesar's; and unto God the things that are God's. Paying taxes honestly is part of good citizenship.

Trade lets nations specialize. Comparative advantage means a nation or person should produce what they can make at the lowest opportunity cost and trade for the rest. Imports are goods bought from other countries, and exports are goods sold to them. A tariff is a tax on imports. Tariffs can protect some jobs, but they also raise prices for consumers, and other nations may respond with their own tariffs.

Worked example: a store charges a ten dollar item plus six percent sales tax, so the total is ten dollars and sixty cents. Common mistake: forgetting local surtax and taxes when budgeting.

Your task: (1) Name four kinds of taxes. (2) Explain progressive, proportional and regressive taxes. (3) Define comparative advantage and tariff.""",
 script="""Welcome back. Listen, government and trade touch your wallet every day.

Governments provide public goods like roads, courts and defense, and pay for them mostly with taxes. Income taxes, payroll taxes, sales taxes and property taxes are the common types. A progressive tax takes a larger percent from higher incomes. A proportional tax takes the same percent. A regressive tax takes a larger share from lower earners.

Now watch this. Florida has no state personal income tax. The state sales tax is six percent, and many counties add a surtax. Federal income tax still applies. When government spends more than it collects, it runs a deficit, and past deficits make up the national debt.

Matthew 22:21 says, Render therefore unto Caesar the things which are Caesar's; and unto God the things that are God's. Paying taxes honestly is good citizenship.

Trade lets nations specialize. Comparative advantage means producing what you make at the lowest opportunity cost and trading for the rest. A tariff is a tax on imports. It can protect some jobs but raises prices for consumers.

Your task is to name four taxes, explain the three tax types and define comparative advantage and tariff. Take the four question check.""" + CLOSE,
 quiz=[
 ("A tax that takes a larger percent from higher incomes is:", ["Progressive", "Regressive", "Proportional", "A tariff"], 0, "Progressive taxes rise with income."),
 ("Florida has no state:", ["Personal income tax", "Sales tax", "Property tax", "Roads"], 0, "Florida has no state personal income tax."),
 ("A tariff is a tax on:", ["Imports", "Wages", "Land", "Gifts"], 0, "It raises the price of imported goods."),
 ("Matthew 22:21 teaches us to render to Caesar:", ["The things which are Caesar's", "Nothing", "Only gifts", "Our faith"], 0, "Citizens owe honest taxes."),
 ]),
 dict(t="2.3 Income, Careers and Paychecks", std=S3,
 body="""Most people earn income by working. Human capital is the knowledge, skills and health that make a worker productive. On average, people with more education and training earn more and are less likely to be unemployed, though results vary by field. Choosing a career means weighing your gifts and calling, the demand for the work, the pay, the cost of training and the lifestyle you want. Scripture honors all honest work. Colossians 3:23 says, And whatsoever ye do, do it heartily, as to the Lord, and not unto men. 2 Thessalonians 3:10 says, For even when we were with you, this we commanded you, that if any would not work, neither should he eat.

Your gross pay is what you earn before deductions. Your net pay, or take home pay, is what you receive after deductions. Common deductions are federal income tax withholding, and FICA taxes. FICA includes Social Security at 6.2 percent and Medicare at 1.45 percent of wages, paid by the employee, and the employer pays a matching share. Florida has no state income tax to withhold. Workers may also pay for health insurance or retirement plans through payroll.

When you start a job you complete a Form W4 so your employer withholds the right amount of federal tax, and at the end of the year you receive a Form W2 that reports your wages and the taxes withheld. A pay stub shows the details. Check it for errors.

Workers earn income in several ways: wages, salary, tips, commissions, self employment and, later, interest and dividends. Employees and independent contractors are treated differently for taxes, and contractors pay both halves of the payroll taxes.

Worked example: a worker earns four hundred dollars gross. Social Security is 6.2 percent, which is 24.80 dollars, and Medicare is 1.45 percent, which is 5.80 dollars. Common mistake: budgeting from gross pay instead of net pay.

Your task: (1) Define gross pay, net pay and human capital. (2) Explain FICA. (3) Calculate the FICA taxes on a six hundred dollar paycheck.""",
 script="""Welcome back. Listen, work is a gift, and your paycheck tells a story you must learn to read.

Human capital is the knowledge, skills and health that make you productive. On average, more education and training lead to higher pay and steadier work. Colossians 3:23 says, And whatsoever ye do, do it heartily, as to the Lord, and not unto men. Second Thessalonians 3:10 says, if any would not work, neither should he eat.

Now watch this. Gross pay is what you earn before deductions. Net pay is what you take home. Deductions include federal income tax withholding and FICA. FICA is Social Security at 6.2 percent and Medicare at 1.45 percent of wages, and the employer pays a matching share. Florida has no state income tax to withhold.

When you start a job you fill out a Form W4. At year end you receive a Form W2 showing your wages and taxes withheld. Check your pay stub for errors.

Always budget from net pay, not gross pay.

Your task is to define gross pay, net pay and human capital, explain FICA and calculate FICA on a six hundred dollar paycheck. Take the four question check.""" + CLOSE,
 quiz=[
 ("Net pay is:", ["Pay after deductions", "Pay before taxes", "A bonus", "A loan"], 0, "It is your take home pay."),
 ("The employee share of Social Security tax is:", ["6.2 percent", "20 percent", "0.5 percent", "50 percent"], 0, "FICA includes 6.2 percent for Social Security."),
 ("Human capital is:", ["Knowledge, skills and health that make workers productive", "Money in a bank", "A kind of tax", "A machine"], 0, "Education and training raise productivity."),
 ("A Form W2 reports:", ["Wages and taxes withheld for the year", "Your budget", "Your grades", "Your savings"], 0, "Employers send it after the year ends."),
 ]),
 dict(t="2.4 Spending Wisely: Consumer Choices, Advertising and Contracts", std=S3,
 body="""Consumers make thousands of spending choices, and wise choices stretch every dollar. Begin with needs and wants. Needs are things required for life and work, such as food, shelter, clothing and transportation. Wants are things that are nice but not required. Comparison shopping means checking quality, price and reviews at several stores before you buy. Unit price, the price per ounce or per item, helps you compare different package sizes. Watch for total cost, including tax, shipping and fees.

Advertising is designed to persuade, not just to inform. Common techniques include celebrity endorsements, appeals to fear or popularity, limited time offers, bandwagon claims and free trials that start charging later. Ask: Who benefits if I buy this? Do I need it? Is the claim true? Proverbs 14:15 says, The simple believeth every word: but the prudent man looketh well to his going. Luke 14:28 says, For which of you, intending to build a tower, sitteth not down first, and counteth the cost, whether he have sufficient to finish it?

A contract is a legally binding agreement. Before signing any contract, read it fully, understand the fees, the length, and how to cancel, and ask for a copy. Warranties promise that a product will work for a stated time. Return policies vary by store, so check them before you buy. If you are treated unfairly, you can contact the seller, your state attorney general, or the Federal Trade Commission. In Florida, you may also contact the state Department of Agriculture and Consumer Services.

Be careful with subscriptions, buy now pay later plans and impulse buys. Waiting twenty four hours before a large purchase prevents many regrets.

Worked example: a twelve ounce box costs three dollars, and a twenty four ounce box costs five dollars. The unit prices are twenty five cents and about twenty one cents per ounce, so the larger box is a better value if you will use it. Common mistake: buying because something is on sale when you did not need it.

Your task: (1) Define unit price and comparison shopping. (2) Describe three advertising techniques. (3) List four things to check before signing a contract.""",
 script="""Welcome back. Listen, every dollar you spend is a decision, and wise decisions stretch your dollars.

Needs are things required for life and work. Wants are nice but not required. Comparison shop for quality, price and reviews. Use unit price, the price per ounce or per item, to compare package sizes. Include tax, shipping and fees in total cost.

Now watch this. Advertising is designed to persuade. Watch for celebrity endorsements, fear or popularity appeals, limited time offers and free trials that start charging later. Ask yourself whether you need it and whether the claim is true. Proverbs 14:15 says, The simple believeth every word: but the prudent man looketh well to his going.

Luke 14:28 says, For which of you, intending to build a tower, sitteth not down first, and counteth the cost, whether he have sufficient to finish it? Count the cost before you buy.

A contract is a legally binding agreement. Read it fully, understand the fees, the length and how to cancel, and get a copy. Wait twenty four hours before a large purchase.

Your task is to define unit price, describe three ad techniques and list four things to check before signing. Take the four question check.""" + CLOSE,
 quiz=[
 ("Unit price helps you compare:", ["Price per ounce or per item", "Store names", "Colors", "Brands only"], 0, "It shows the better value."),
 ("Luke 14:28 teaches us to:", ["Count the cost first", "Spend quickly", "Borrow freely", "Avoid all building"], 0, "Plan before you commit."),
 ("Before signing a contract you should:", ["Read it fully and understand fees and cancellation", "Sign quickly", "Skip the details", "Trust the salesperson only"], 0, "A contract is legally binding."),
 ("A limited time offer is meant to:", ["Create urgency to buy", "Lower taxes", "Teach economics", "Guarantee quality"], 0, "Pressure can lead to impulse buying."),
 ]),
 ],
 assess=dict(t="Assessment 2: The Economy and Consumers",
 prompt="""Write a report of at least 250 words on the economy and the consumer. Use complete sentences and label each part. Luke 14:28 says, For which of you, intending to build a tower, sitteth not down first, and counteth the cost, whether he have sufficient to finish it?

Part 1: Define GDP, inflation and the unemployment rate and describe the four phases of the business cycle.
Part 2: Explain four kinds of taxes and describe the difference between progressive, proportional and regressive taxes. Include what is true about Florida taxes.
Part 3: Explain comparative advantage and one effect of a tariff.
Part 4: Explain gross pay, net pay and FICA, and calculate the net pay for a sample paycheck of five hundred dollars after the two FICA taxes only.
Part 5: Describe three ways to spend wisely and explain how to protect yourself in a contract.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 20 points. Part 3: 15 points. Part 4: 20 points. Part 5: 20 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 2: Counting the Cost",
 prompt="""Write a post of at least 120 words that (1) describes a purchase teens often make because of advertising, (2) names one advertising technique used, (3) explains how you would count the cost before buying, and (4) connects your answer to Luke 14:28 or Proverbs 14:15. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why is it important to compare a raise with inflation?"""),
 unit_quiz=[
 ("A recession is a:", ["Serious, lasting contraction", "Period of growth", "Type of tax", "Bank loan"], 0, "It is a downturn in the business cycle."),
 ("The Consumer Price Index measures:", ["Changes in the price of a typical basket of goods", "Wages only", "Taxes", "Savings"], 0, "It tracks inflation."),
 ("A regressive tax:", ["Takes a larger share of income from lower earners", "Taxes only the rich", "Is always zero", "Is a tariff"], 0, "The burden is heavier on lower incomes."),
 ("A deficit occurs when government:", ["Spends more than it collects", "Collects more than it spends", "Cuts all taxes", "Prints a law"], 0, "The sum of deficits is the debt."),
 ("Comparative advantage means producing what you make at the lowest:", ["Opportunity cost", "Wage", "Tax", "Price"], 0, "Specialization and trade benefit both sides."),
 ("Social Security and Medicare taxes together are called:", ["FICA", "FDIC", "GDP", "CPI"], 0, "They appear on your pay stub."),
 ("Net pay is smaller than gross pay because of:", ["Deductions", "Bonuses", "Gifts", "Interest"], 0, "Taxes and other deductions are subtracted."),
 ("Before signing a contract, you should:", ["Read it fully", "Rush", "Ignore fees", "Skip cancellation terms"], 0, "A contract binds you legally."),
 ],
)
