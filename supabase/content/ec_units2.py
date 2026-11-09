"""Economics, Unit 2: Business, Money and Government. Florida economics standards cited at strand level (SS.912.E.2 and SS.912.E.3); recheck exact wording at CPALMS."""
from ec_units1 import CLOSE

UNIT2 = dict(
 title="Unit 2: Business, Money and Government",
 std="SS.912.E.2, SS.912.E.3",
 topics=[
 dict(t="2.1 Business and Entrepreneurship", std="SS.912.E.2",
 body="""An entrepreneur sees a need, gathers land, labor and capital, and takes a risk to meet it. Businesses are the engines that turn ideas into goods and jobs. Proverbs 31:16 describes a woman who considereth a field, and buyeth it: with the fruit of her hands she planteth a vineyard. She is a model of wise enterprise.

Businesses take four common legal forms. A sole proprietorship has one owner who keeps all profit and bears all risk and debt. A partnership has two or more owners who share profit and responsibility. A corporation is a separate legal entity owned by stockholders, who are protected from personal liability for the company's debts. A limited liability company, called an LLC, blends the protection of a corporation with simpler rules. Many small businesses in Florida are LLCs.

Profit equals total revenue minus total costs. Revenue is the money a business takes in from sales. Costs include fixed costs, such as rent, which stay the same however much is sold, and variable costs, such as materials, which rise with output. A business that earns less than its costs takes a loss and may close.

Entrepreneurs face risk, but they also create jobs and bring new products. A business plan helps by stating the product, the customers, the competition, the costs and the way the owner will earn a profit. Proverbs 14:23 says that in all labour there is profit: but the talk of the lips tendeth only to penury.

Your task: (1) Name the four forms of business and one advantage of each. (2) Define profit, fixed cost and variable cost. (3) Describe a small business you could start and list what its business plan would need.""",
 script="""Welcome back. Listen, behind every job in your neighborhood is somebody who saw a need and took a risk.

An entrepreneur gathers land, labor and capital to meet a need. Proverbs 31:16 describes a woman who considered a field and bought it, and with the fruit of her hands planted a vineyard. That is wise enterprise.

Now watch this. There are four common forms of business. A sole proprietorship has one owner who keeps all the profit and all the risk. A partnership has two or more owners who share both. A corporation is a separate legal body owned by stockholders, who are not personally liable for its debts. And an LLC, a limited liability company, blends that protection with simpler rules.

Look at profit. Profit equals total revenue minus total costs. Fixed costs, like rent, stay the same however much you sell. Variable costs, like materials, rise as you make more. If costs beat revenue, that is a loss.

A business plan names the product, the customers, the competition, the costs and how you will earn a profit.

Your task is to name the four forms, define profit and the two kinds of cost, and sketch a small business. Take the four question check.""" + CLOSE,
 quiz=[
 ("Profit equals:", ["Total revenue minus total costs", "Total costs minus revenue", "Revenue plus costs", "Wages plus taxes"], 0, "A business earns profit when revenue is greater than costs."),
 ("Which business form protects owners from personal liability and is owned by stockholders?", ["Corporation", "Sole proprietorship", "Partnership with no agreement", "Barter group"], 0, "Corporate stockholders are not personally liable for company debts."),
 ("Monthly rent for a shop is an example of a:", ["Fixed cost", "Variable cost", "Revenue", "Subsidy"], 0, "Fixed costs do not change with the amount sold."),
 ("A sole proprietorship has:", ["One owner who bears all the risk", "Many stockholders", "Government owners", "No owner"], 0, "The owner keeps the profit and carries the debt."),
 ]),
 dict(t="2.2 Labor, Wages and Careers", std="SS.912.E.2",
 body="""Labor is the work people do in exchange for pay. Wages are set largely by supply and demand in the labor market. Jobs that need rare skills, long training or hard conditions usually pay more, because fewer workers can fill them. A worker can raise his or her pay by building human capital, which is the knowledge, skill and health a person brings to work. Education, training and experience are investments in human capital.

Specialization means focusing on one task, and the division of labor splits a big job among many workers. Together they raise productivity, which is the output per worker. Higher productivity makes higher wages possible. Colossians 3:23 teaches, And whatsoever ye do, do it heartily, as to the Lord, and not unto men. Proverbs 22:29 adds, Seest thou a man diligent in his business? he shall stand before kings.

Workers have some legal protections. The National Labor Relations Act of 1935 protects the right to form a labor union and to bargain together. The Fair Labor Standards Act of 1938 set the first federal minimum wage, required overtime pay at one and one half times the regular rate for work over forty hours in most jobs, and limited child labor. The federal minimum wage is 7.25 dollars an hour, and Florida's constitution sets a higher state minimum that rises on a schedule, so students should check the current rate with the Florida Department of Commerce.

Choosing a career means weighing pay, interest, training time and demand for the work. Technology changes jobs quickly, so lifelong learning matters.

Your task: (1) Define human capital and give two ways to build it. (2) Explain how specialization raises productivity. (3) Name one law that protects workers and tell what it does.""",
 script="""Welcome back. Listen, the most valuable thing you own is not in your wallet. It is in your mind and your hands.

Labor is the work people do for pay, and wages are set largely by supply and demand. Jobs that need rare skills or long training usually pay more, because fewer people can do them. That is why we talk about human capital, the knowledge, skill and health you bring to work. School, training and experience are investments in it.

Now watch this. Specialization means focusing on one task. The division of labor splits a big job among many workers. Together they raise productivity, the output per worker, and higher productivity makes higher wages possible.

Colossians 3:23 says, whatsoever ye do, do it heartily, as to the Lord. And Proverbs 22:29 says a diligent man shall stand before kings.

Look at the law. In 1935 the National Labor Relations Act protected the right to form unions. In 1938 the Fair Labor Standards Act set the first federal minimum wage, required overtime after forty hours, and limited child labor. Florida sets its own higher minimum, so always check the current rate.

Your task is to define human capital, explain specialization, and name a law that protects workers. Take the four question check.""" + CLOSE,
 quiz=[
 ("Human capital is:", ["The knowledge and skills a worker brings to a job", "A company's machines", "Money in a bank", "A tax on wages"], 0, "Education and training build human capital."),
 ("Productivity means:", ["Output per worker", "The number of workers", "The price of a good", "The size of a building"], 0, "Higher productivity allows higher wages."),
 ("The Fair Labor Standards Act of 1938 set the first:", ["Federal minimum wage", "Income tax", "National bank", "Tariff"], 0, "It also required overtime pay and limited child labor."),
 ("Overtime pay under federal law is generally owed after how many hours in a week?", ["Forty", "Thirty", "Fifty five", "Sixty"], 0, "Most covered workers earn time and a half after forty hours."),
 ]),
 dict(t="2.3 Money, Banking and the Federal Reserve", std="SS.912.E.3",
 body="""Before money, people used barter, trading goods directly. Barter fails when each person does not want what the other has. Money solves this by doing three jobs: it is a medium of exchange that everyone accepts, a unit of account that lets us measure value, and a store of value that holds worth over time. Good money is durable, portable, divisible, scarce and accepted. The United States dollar is fiat money, which means it has value because the government declares it legal tender and people trust it, not because it is backed by gold.

Banks take deposits and make loans. They pay interest to savers and charge a higher interest rate to borrowers, and the difference helps cover costs and earn profit. A bank keeps part of deposits on hand and lends the rest, which expands the money supply. After the bank failures of the Great Depression, Congress created the Federal Deposit Insurance Corporation, the FDIC, in 1933. It insures deposits up to 250,000 dollars per depositor, per insured bank, for each ownership category.

The nation's central bank is the Federal Reserve System, created in 1913. It has a Board of Governors of seven members in Washington, twelve regional banks, and the Federal Open Market Committee, which sets monetary policy. Its goals are maximum employment and stable prices. It guides the economy by buying and selling government securities, called open market operations, by setting the discount rate it charges banks, and by steering the federal funds rate.

Proverbs 22:7 warns, The rich ruleth over the poor, and the borrower is servant to the lender. Borrow with care.

Your task: (1) Name the three jobs of money. (2) Explain how a bank earns money on loans. (3) Describe two jobs of the Federal Reserve.""",
 script="""Welcome back. Listen, money is one of the greatest inventions in history, and few people can explain what it really is.

Before money there was barter, and barter breaks down when I do not want what you have. Money solves that with three jobs. It is a medium of exchange, a unit of account and a store of value. The dollar is fiat money. It has value because the government declares it legal tender and people trust it.

Now watch this. Banks take deposits and make loans. They pay savers a little interest and charge borrowers more, and the difference pays their costs and earns a profit. After the bank failures of the Great Depression, Congress created the FDIC in 1933. It insures deposits up to 250,000 dollars per depositor, per insured bank, for each ownership category.

Look at the Federal Reserve. Congress created it in 1913. It has a Board of Governors of seven members, twelve regional banks, and the Federal Open Market Committee. Its goals are maximum employment and stable prices. Its tools include open market operations, the discount rate, and steering the federal funds rate.

Remember Proverbs 22:7. The borrower is servant to the lender.

Your task is to name the three jobs of money, explain how banks earn from loans, and describe two jobs of the Fed. Take the four question check.""" + CLOSE,
 quiz=[
 ("Which is one of the three jobs of money?", ["Medium of exchange", "Source of taxes", "Form of government", "Type of loan"], 0, "Money is a medium of exchange, a unit of account and a store of value."),
 ("The FDIC was created in:", ["1933", "1776", "1913", "1971"], 0, "It was created after the bank failures of the Great Depression."),
 ("The Federal Reserve System was created in:", ["1913", "1863", "1933", "1987"], 0, "Congress passed the Federal Reserve Act in 1913."),
 ("Fiat money has value because:", ["The government declares it legal tender and people trust it", "It is made of gold", "It is rare", "It is printed in color"], 0, "The dollar is not backed by a metal."),
 ]),
 dict(t="2.4 The Role of Government in the Economy", std="SS.912.E.3",
 body="""Even in a market economy, government has important jobs. It protects property rights and enforces contracts, so people can trade with trust. It provides public goods, which are goods that everyone shares and that no one can easily be kept from using, such as national defense and lighthouses. Private firms will not provide them for profit because people can use them without paying, which is called the free rider problem.

Government also deals with externalities, which are side effects on people who did not take part in a transaction. Pollution from a factory is a negative externality, and government may set rules or fees. A vaccination or an education brings a positive externality, and government may support it. Government also regulates to protect consumers, keeps competition fair, and provides a safety net.

Governments pay for these services through taxes. The federal government collects mainly the income tax, made legal by the Sixteenth Amendment in 1913, and payroll taxes. Under the Federal Insurance Contributions Act, an employee pays 6.2 percent for Social Security and 1.45 percent for Medicare, and the employer pays the same amount. States and cities rely on sales taxes, property taxes and fees. Florida has no state personal income tax, and its sales tax is 6 percent at the state level, plus local additions in many counties.

A tax can be progressive, taking a larger share from higher incomes, proportional, taking the same share from all, or regressive, taking a larger share from lower incomes. In Nehemiah 5, the prophet confronted rich men who charged heavy interest and seized land, and he demanded that they restore what they had taken. Justice in economics matters to God.

Your task: (1) Define public good, free rider and externality. (2) Name three taxes and who collects each. (3) Explain the difference between a progressive and a regressive tax.""",
 script="""Welcome back. Listen, even a free market needs a referee.

Government protects property rights and enforces contracts, so people can trade with trust. It provides public goods, like national defense, that everyone shares and no one can easily be kept from using. Private firms will not provide them for profit because of the free rider problem. People can enjoy them without paying.

Now watch this. An externality is a side effect on someone who was not part of the deal. Pollution from a factory is a negative externality. A good education is a positive one.

Look at how government pays for its work. The federal government collects mainly the income tax, legal since the Sixteenth Amendment in 1913, and payroll taxes. An employee pays 6.2 percent for Social Security and 1.45 percent for Medicare, and the employer pays the same. States and cities depend on sales taxes, property taxes and fees. Florida has no state personal income tax, and its state sales tax is 6 percent, with local additions in many counties.

A progressive tax takes a larger share from higher incomes. A regressive tax takes a larger share from lower incomes.

In Nehemiah 5 the prophet demanded that rich men stop charging heavy interest and restore the land they seized. Justice matters to God.

Your task is to define public good, free rider and externality, name three taxes, and compare progressive and regressive taxes. Take the four question check.""" + CLOSE,
 quiz=[
 ("A good that everyone shares and no one can easily be kept from using is a:", ["Public good", "Luxury", "Private good", "Barter good"], 0, "National defense is a public good."),
 ("Factory pollution is an example of a:", ["Negative externality", "Public good", "Subsidy", "Tariff"], 0, "It harms people outside the transaction."),
 ("The Sixteenth Amendment made legal the:", ["Federal income tax", "Sales tax", "Property tax", "Tariff"], 0, "It was ratified in 1913."),
 ("Which statement about Florida is correct?", ["It has no state personal income tax", "It has the highest income tax", "It has no sales tax", "It taxes only imports"], 0, "Florida's constitution bars a state personal income tax."),
 ]),
 ],
 assess=dict(t="Assessment 2: Business, Money and Government",
 prompt="""Write a report of at least 250 words on business, money and government. Use complete sentences and label each part. Proverbs 22:7 says, The rich ruleth over the poor, and the borrower is servant to the lender.

Part 1: Describe a business you could start. Name its legal form, one fixed cost, one variable cost and how it would earn a profit.
Part 2: Explain how education and training build human capital and raise wages.
Part 3: Explain the three jobs of money and how banks and the FDIC protect savers.
Part 4: Describe two goals and two tools of the Federal Reserve.
Part 5: Explain one public good and one externality, and describe how a tax pays for government services.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 15 points. Part 3: 20 points. Part 4: 20 points. Part 5: 20 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 2: Work, Money and Justice",
 prompt="""Write a post of at least 120 words that (1) tells what career you would like to study for and what human capital you will need, (2) explains one way you will use banks wisely, (3) tells whether you think a business owner or government should do more to help workers, and why, and (4) connects your answer to Colossians 3:23, which says, And whatsoever ye do, do it heartily, as to the Lord, and not unto men. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Should the minimum wage be higher, lower or the same? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("A business owned by stockholders is a:", ["Corporation", "Sole proprietorship", "Partnership", "Cooperative of one"], 0, "Stockholders own shares of a corporation."),
 ("Which raises a worker's human capital?", ["Education and training", "A higher price on goods", "A tariff", "A bank loan"], 0, "Skills and knowledge raise productivity and pay."),
 ("Federal overtime pay is generally one and one half times the regular rate after:", ["Forty hours", "Twenty hours", "Sixty hours", "Eight hours"], 0, "The Fair Labor Standards Act sets this rule for most jobs."),
 ("Money that has value because a government declares it legal tender is:", ["Fiat money", "Barter", "Commodity money", "A bond"], 0, "The dollar is fiat money."),
 ("The FDIC insures deposits up to:", ["250,000 dollars per depositor, per bank, per ownership category", "1,000 dollars", "No limit", "10,000 dollars per account only"], 0, "The standard coverage amount is 250,000 dollars."),
 ("The Federal Reserve's two goals are:", ["Maximum employment and stable prices", "Higher taxes and lower wages", "Full trade and no banks", "More tariffs and fewer jobs"], 0, "Congress gave the Fed these goals."),
 ("A tax that takes a larger share of income from lower earners is:", ["Regressive", "Progressive", "Proportional", "Voluntary"], 0, "A regressive tax weighs more heavily on low incomes."),
 ("National defense is an example of a:", ["Public good", "Private good", "Negative externality", "Barter good"], 0, "Everyone shares it and no one can easily be kept from it."),
 ])
