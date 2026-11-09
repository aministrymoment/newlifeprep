"""Economics, Unit 3: The National and Personal Economy. Florida economics standards cited at strand level (SS.912.E.3 and SS.912.FL); recheck exact wording at CPALMS."""
from ec_units1 import CLOSE

UNIT3 = dict(
 title="Unit 3: The National and Personal Economy",
 std="SS.912.E.3, SS.912.FL",
 topics=[
 dict(t="3.1 Measuring the Economy", std="SS.912.E.3",
 body="""To know whether an economy is healthy, economists measure it. The most common measure is gross domestic product, or GDP, which is the market value of all final goods and services produced within a country in one year. The Bureau of Economic Analysis reports it. Nominal GDP uses current prices, and real GDP adjusts for price changes so that years can be compared fairly. Economic growth means that real GDP rises over time.

The unemployment rate is the number of people who are jobless and actively looking for work, divided by the labor force, then multiplied by 100. The Bureau of Labor Statistics reports it. Frictional unemployment is short term, as people move between jobs. Structural unemployment happens when skills do not match available jobs. Cyclical unemployment rises when the economy slows.

Inflation is a general rise in prices, which lowers the buying power of money. The Consumer Price Index, the CPI, tracks the cost of a typical basket of goods and services. The Federal Reserve aims for inflation of about 2 percent a year.

Economies move through a business cycle with four phases: expansion, peak, contraction and trough. A long, deep contraction is called a depression. The Great Depression began after the stock market crash of 1929, and unemployment reached about 25 percent. Ecclesiastes 3:1 says, To every thing there is a season, and a time to every purpose under the heaven. A wise family and a wise nation prepare in good seasons for lean ones, as Joseph did.

Your task: (1) Define GDP and explain the difference between nominal and real GDP. (2) Tell how the unemployment rate is figured. (3) Name the four phases of the business cycle and describe what inflation does to a dollar.""",
 script="""Welcome back. Listen, a doctor takes your temperature before treating you, and an economist does the same with a nation.

The main measure is gross domestic product, GDP, the market value of all final goods and services produced inside a country in one year. Nominal GDP uses current prices. Real GDP adjusts for price changes so we can compare years fairly.

Now watch this. The unemployment rate is the number of people who are jobless and looking for work, divided by the labor force, times 100. Frictional unemployment is short term, as people change jobs. Structural unemployment is when skills do not match the jobs. Cyclical unemployment rises when the economy slows.

Look at inflation. It is a general rise in prices, which lowers what a dollar will buy. The Consumer Price Index tracks a typical basket of goods. The Federal Reserve aims for about 2 percent a year.

The business cycle has four phases: expansion, peak, contraction and trough. The Great Depression began after the crash of 1929, and unemployment reached about 25 percent.

Remember Ecclesiastes 3:1. To every thing there is a season. Prepare in the good seasons for the lean ones, as Joseph did.

Your task is to define GDP, explain the unemployment rate, and name the four phases of the cycle. Take the four question check.""" + CLOSE,
 quiz=[
 ("GDP measures:", ["The value of all final goods and services produced in a country in a year", "Only exports", "The national debt", "The number of workers"], 0, "GDP is the main measure of national output."),
 ("Real GDP differs from nominal GDP because real GDP:", ["Adjusts for changes in prices", "Ignores output", "Counts only imports", "Uses no data"], 0, "Real GDP removes the effect of inflation."),
 ("Inflation is:", ["A general rise in prices", "A fall in all prices", "A rise in wages only", "A type of tax"], 0, "Inflation lowers the buying power of money."),
 ("The four phases of the business cycle are expansion, peak, contraction and:", ["Trough", "Surplus", "Tariff", "Credit"], 0, "The low point is called the trough."),
 ]),
 dict(t="3.2 Fiscal and Monetary Policy", std="SS.912.E.3",
 body="""Government tries to keep the economy stable using two sets of tools. Fiscal policy is the use of government spending and taxation by Congress and the President. To fight a slowdown, government can cut taxes or increase spending, which puts more money in circulation. To cool inflation, it can raise taxes or cut spending. The English economist John Maynard Keynes argued during the Great Depression that government spending can lift a weak economy.

Every year Congress passes a federal budget. When spending is greater than revenue, there is a deficit. When revenue is greater than spending, there is a surplus. The national debt is the total of all past deficits, less any surpluses, that government still owes. Much federal spending is mandatory, such as Social Security and Medicare, some is discretionary, such as defense and education, and some pays interest on the debt.

Monetary policy is the use of the money supply and interest rates by the Federal Reserve. To stimulate the economy, the Fed lowers interest rates so that borrowing is cheaper. To slow inflation, it raises them. Fiscal policy is made by elected officials, while the Fed acts as an independent agency, so it can make hard choices without election pressure.

Scripture values wise planning. Proverbs 27:23 says, Be thou diligent to know the state of thy flocks, and look well to thy herds. Proverbs 6:6 says, Go to the ant, thou sluggard; consider her ways, and be wise. A family or a nation that saves and plans wisely stands stronger in hard times.

Your task: (1) Define fiscal policy and monetary policy and tell who makes each. (2) Explain the difference between a deficit and the national debt. (3) Tell what the Fed does to interest rates to slow inflation.""",
 script="""Welcome back. Listen, a nation cannot steer its economy with prayer alone. It needs tools, and there are two sets.

Fiscal policy is government spending and taxes, set by Congress and the President. To fight a slowdown, they can cut taxes or spend more. To cool inflation, they can raise taxes or cut spending. John Maynard Keynes argued in the Great Depression that government spending can lift a weak economy.

Now watch this. A deficit is when spending is greater than revenue in a year. A surplus is the reverse. The national debt is the total of past deficits, less surpluses, that government still owes. Do not confuse the two. A deficit is one year. The debt is the whole pile.

Monetary policy is the Federal Reserve using the money supply and interest rates. To stimulate, the Fed lowers rates so borrowing is cheaper. To slow inflation, it raises them. The Fed is independent, so it can make hard choices without election pressure.

Remember Proverbs 27:23, be diligent to know the state of thy flocks. And Proverbs 6:6, go to the ant, consider her ways, and be wise.

Your task is to define fiscal and monetary policy, explain deficit and debt, and tell what the Fed does to slow inflation. Take the four question check.""" + CLOSE,
 quiz=[
 ("Fiscal policy is made by:", ["Congress and the President", "The Federal Reserve", "State banks", "The Supreme Court"], 0, "It uses government spending and taxation."),
 ("A budget deficit occurs when:", ["Government spending is greater than revenue", "Revenue is greater than spending", "The Fed lowers rates", "Exports exceed imports"], 0, "A deficit is a one year shortfall."),
 ("To slow inflation, the Federal Reserve would usually:", ["Raise interest rates", "Lower interest rates", "Print more money", "Cut all taxes"], 0, "Higher rates make borrowing cost more and cool spending."),
 ("The national debt is:", ["The total that government owes from past deficits", "One year's deficit", "The trade surplus", "The Fed's profit"], 0, "The debt is the accumulated total."),
 ]),
 dict(t="3.3 Trade and the Global Economy", std="SS.912.E.3",
 body="""Nations trade because no nation has every resource or skill. Exports are goods and services sold to other countries, and imports are those bought from other countries. The idea of comparative advantage explains why trade helps everyone: a country or person should focus on the work that they do at the lowest opportunity cost, and trade for the rest. A lawyer who types faster than her assistant still hires the assistant, because her time is better used on legal work.

Governments sometimes limit trade. A tariff is a tax on imports. A quota is a limit on the amount of a good that may be imported. An embargo is a ban on trade with a country. Supporters say these protect jobs or national security, but critics say they raise prices for buyers and invite retaliation. Free trade agreements lower such barriers. The United States, Mexico and Canada trade under the United States Mexico Canada Agreement, which took effect in 2020 and replaced the North American Free Trade Agreement. The World Trade Organization, formed in 1995, helps settle trade disputes.

Different currencies trade at an exchange rate, the price of one currency in terms of another. When the dollar becomes stronger, imports get cheaper for Americans but exports get more costly for foreign buyers. South Florida is a gateway for trade with the Caribbean and Latin America, and the ports at Fort Lauderdale and Miami move goods in and out of the nation.

Trade is an old practice in Scripture. Proverbs 31:14 says of the virtuous woman, She is like the merchants' ships; she bringeth her food from afar. In 1 Kings 10, Solomon's wisdom and trade brought wealth and visitors from many lands.

Your task: (1) Define export, import and comparative advantage. (2) Describe a tariff and one argument for and against it. (3) Explain what a stronger dollar does to imports and exports.""",
 script="""Welcome back. Listen, the dinner on your table likely came from several countries. That is trade.

Exports are goods and services sold to other countries. Imports are those we buy from other countries. Now watch this. Comparative advantage is the reason trade helps everyone. Focus on the work you do at the lowest opportunity cost, and trade for the rest. A lawyer who types faster than her assistant still hires the assistant, because her time is better spent on legal work.

Governments sometimes limit trade. A tariff is a tax on imports. A quota limits the amount imported. An embargo bans trade with a country. Supporters say these protect jobs and security. Critics say they raise prices and invite retaliation. The United States, Mexico and Canada trade under the USMCA, which took effect in 2020 and replaced NAFTA. The World Trade Organization, formed in 1995, helps settle trade disputes.

Look at the exchange rate. It is the price of one currency in terms of another. A stronger dollar makes imports cheaper for us and our exports costlier for foreigners. South Florida is a gateway to the Caribbean and Latin America.

Remember Proverbs 31:14. She is like the merchants' ships. And 1 Kings 10 shows Solomon's wisdom drawing trade and visitors from many lands.

Your task is to define export, import and comparative advantage, describe a tariff, and explain a stronger dollar. Take the four question check.""" + CLOSE,
 quiz=[
 ("A tariff is:", ["A tax on imported goods", "A ban on all trade", "A limit on exports only", "A type of loan"], 0, "Tariffs raise the price of imports."),
 ("Comparative advantage means:", ["Doing the work you do at the lowest opportunity cost", "Having the most resources", "Never trading", "Owning the most land"], 0, "It explains why trade benefits both sides."),
 ("Goods sold to other countries are called:", ["Exports", "Imports", "Quotas", "Embargoes"], 0, "Exports leave the country."),
 ("The agreement that replaced NAFTA in 2020 is the:", ["United States Mexico Canada Agreement", "Sherman Act", "Federal Reserve Act", "Bill of Rights"], 0, "USMCA took effect in 2020."),
 ]),
 dict(t="3.4 Personal Finance and Stewardship", std="SS.912.FL",
 body="""A steward manages what belongs to another. Deuteronomy 8:18 says, Thou shalt remember the LORD thy God: for it is he that giveth thee power to get wealth. In the parable of the talents in Matthew 25, the master praised the servants who used his goods well, saying in verse 21, Well done, thou good and faithful servant. Good stewardship starts with a plan.

A budget is a plan for your income and spending. List your income, then your needs, wants, giving and savings. One common rule of thumb is to give first, then plan roughly half of income for needs, some for wants, and the rest for saving. Proverbs 3:9 says, Honour the LORD with thy substance, and with the firstfruits of all thine increase, and Malachi 3:10 speaks of bringing the tithes into the storehouse.

Saving builds security. An emergency fund of several months of expenses guards against a job loss or repair. Interest is the price of using money. Simple interest is figured on the starting amount only, so 1,000 dollars at 5 percent for 3 years earns 150 dollars. Compound interest is figured on the amount plus earlier interest, so the same money grows to about 1,157.63 dollars. The rule of 72 says that dividing 72 by the interest rate shows about how many years it takes to double, so at 6 percent it takes about 12 years.

Credit is borrowing with a promise to repay. The annual percentage rate, the APR, is the yearly cost of the loan. A credit score, usually between 300 and 850, shows how reliably you repay. Paying only the minimum on a credit card can leave you in debt for years. Proverbs 22:7 warns that the borrower is servant to the lender. Investing in stocks, bonds or funds may earn more over time, but carries risk, so diversify. Watch for scams that promise quick riches. Proverbs 21:5 says that the thoughts of the diligent tend only to plenty; but of every one that is hasty only to want.

Your task: (1) Build a sample monthly budget with income, giving, needs, wants and savings. (2) Explain the difference between simple and compound interest with the example given. (3) Name two ways to use credit wisely.""",
 script="""Welcome back. This is the lesson you will use every week of your life. Listen, a steward manages what belongs to another. Deuteronomy 8:18 says it is the LORD who gives us power to get wealth. In Matthew 25 the master said to the faithful servant, Well done, thou good and faithful servant.

Good stewardship starts with a plan. A budget is a plan for your income and spending. List your income, then giving, needs, wants and savings. Proverbs 3:9 says to honour the LORD with thy substance, and with the firstfruits of all thine increase.

Now watch this. Saving builds security. Keep an emergency fund of several months of expenses. Interest is the price of using money. Simple interest uses the starting amount only, so 1,000 dollars at 5 percent for 3 years earns 150 dollars. Compound interest grows on the interest too, and the same money becomes about 1,157 dollars and 63 cents. The rule of 72 says divide 72 by the rate to find the years to double. At 6 percent, about 12 years.

Look at credit. It is borrowing with a promise to repay. The APR is the yearly cost of the loan. A credit score, usually between 300 and 850, shows how reliably you repay. Paying only the minimum can keep you in debt for years. Proverbs 22:7 says the borrower is servant to the lender.

If you invest, diversify, and run from anyone promising quick riches. Proverbs 21:5 says haste leads only to want.

Your task is to build a sample budget, explain simple and compound interest, and name two ways to use credit wisely. Take the four question check.""" + CLOSE,
 quiz=[
 ("A budget is:", ["A plan for income and spending", "A type of loan", "A tax form", "A bank fee"], 0, "A budget lists income, giving, needs, wants and savings."),
 ("Simple interest on 1,000 dollars at 5 percent for 3 years is:", ["150 dollars", "50 dollars", "500 dollars", "1,157 dollars"], 0, "1,000 times 0.05 times 3 equals 150."),
 ("Compound interest differs from simple interest because it:", ["Earns interest on earlier interest", "Is always lower", "Is a tax", "Applies only to loans"], 0, "Compounding grows the balance faster."),
 ("Using the rule of 72, money at 6 percent doubles in about:", ["12 years", "6 years", "72 years", "36 years"], 0, "72 divided by 6 equals 12."),
 ]),
 ],
 assess=dict(t="Assessment 3: The National and Personal Economy",
 prompt="""Write a report of at least 250 words on the national and personal economy. Use complete sentences and label each part. Matthew 25:21 says, His lord said unto him, Well done, thou good and faithful servant: thou hast been faithful over a few things, I will make thee ruler over many things.

Part 1: Explain GDP, the unemployment rate and inflation, and tell what each shows about the economy.
Part 2: Describe the four phases of the business cycle and one way government can respond to a slowdown with fiscal policy and with monetary policy.
Part 3: Explain comparative advantage and one effect of a tariff.
Part 4: Create a sample monthly budget for a 1,500 dollar income that includes giving, needs, wants and savings, and explain your choices.
Part 5: Explain compound interest and two ways to avoid trouble with credit.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 20 points. Part 3: 15 points. Part 4: 25 points. Part 5: 15 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 3: Wise Stewards in Hard Times",
 prompt="""Write a post of at least 120 words that (1) tells how inflation or a recession could affect a family you know, (2) describes one habit of saving or giving that you will start, (3) explains whether you think trade with other countries helps or hurts American workers, and why, and (4) connects your answer to Proverbs 21:5, which says, The thoughts of the diligent tend only to plenty; but of every one that is hasty only to want. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Is borrowing money for college a wise decision? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("The unemployment rate is the share of the labor force that is:", ["Jobless and looking for work", "Retired", "In school", "Self employed"], 0, "It counts people who want work and cannot find it."),
 ("The Federal Reserve aims for inflation of about:", ["2 percent a year", "0 percent", "10 percent", "25 percent"], 0, "Two percent is the Fed's stated goal."),
 ("A national debt is the total of:", ["Past deficits less surpluses still owed", "One year's spending", "The trade surplus", "Bank deposits"], 0, "The debt accumulates over time."),
 ("To stimulate a weak economy, the Fed would usually:", ["Lower interest rates", "Raise interest rates", "Ban imports", "Raise the minimum wage"], 0, "Cheaper loans encourage spending and investment."),
 ("An embargo is:", ["A ban on trade with a country", "A tax on imports", "A limit on quantity", "A trade agreement"], 0, "It stops trade entirely."),
 ("A strong dollar tends to make imports:", ["Cheaper for Americans", "More costly for Americans", "Illegal", "Free"], 0, "Each dollar buys more foreign currency."),
 ("Compound interest earns interest on:", ["The principal and earlier interest", "The principal only", "Taxes", "Wages"], 0, "That is why compounding grows faster."),
 ("A credit score is usually a number between:", ["300 and 850", "1 and 10", "0 and 100", "1,000 and 5,000"], 0, "A higher score shows more reliable repayment."),
 ])
