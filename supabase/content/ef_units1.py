"""Economics with Financial Literacy, Unit 1: Economic Foundations. Standards cited at strand level."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."
S1 = "NLPA Economics with Financial Literacy course outcomes, SS.912.E.1, SS.912.FL"
S2 = "NLPA Economics with Financial Literacy course outcomes, SS.912.E.2, SS.912.E.3"
S3 = "NLPA Economics with Financial Literacy course outcomes, SS.912.FL"

UNIT1 = dict(
 title="Unit 1: Economic Foundations",
 std=S1,
 topics=[
 dict(t="1.1 Scarcity, Choice and Incentives", std=S1,
 body="""Economics is the study of how people make choices when resources are limited. The basic problem is scarcity: wants are unlimited, but time, money, land, labor and tools are not. Because of scarcity, every person, family, business and nation must choose. Economists group resources into land (natural resources), labor (human work), capital (tools, buildings and machines) and entrepreneurship (the skill of organizing the other three to start a business and take risks).

Every choice has an opportunity cost, which is the value of the next best alternative you give up. If you spend Saturday working a job instead of resting, the rest is part of the cost. Thinking at the margin means weighing the extra benefit of one more unit against its extra cost. People also respond to incentives, which are rewards or penalties that influence behavior. A discount, a bonus, a tax or a fine can all change what people choose.

Scripture shows scarcity and wise planning. In Genesis 41:36 Joseph advised Pharaoh that the food shall be for store to the land against the seven years of famine, which shall be in the land of Egypt; that the land perish not through the famine. Joseph saved in the years of plenty so that the nation could eat in the years of want. Proverbs 21:5 says, The thoughts of the diligent tend only to plenteousness; but of every one that is hasty only to want.

Worked example: you have fifty dollars and can buy a pair of shoes or take a friend to a concert. If you choose the shoes, the opportunity cost is the concert. Common mistake: thinking that cost means only the price. Cost also includes what you give up.

Your task: (1) Define scarcity and opportunity cost. (2) Name the four kinds of resources with an example of each. (3) Describe a recent choice you made and its opportunity cost.""",
 script="""Welcome to Economics with Financial Literacy. I am Dr. Alex L. Jenkins Sr., and I am glad you are here. Listen, this course will help you understand how the economy works and how to manage your own money with wisdom.

Economics is the study of how people make choices when resources are limited. That limit is called scarcity. Our wants are unlimited, but our time, money and resources are not. So everyone must choose. The resources are land, labor, capital and entrepreneurship.

Now watch this. Every choice has an opportunity cost. That is the value of the next best thing you give up. If you spend fifty dollars on shoes, the concert you did not attend is your opportunity cost. Cost is more than the price. People also respond to incentives, which are rewards or penalties that change behavior.

Joseph understood scarcity. In Genesis 41:36 he told Pharaoh that the food shall be for store to the land against the seven years of famine. He saved in plenty so the nation could eat in want. Proverbs 21:5 says, The thoughts of the diligent tend only to plenteousness; but of every one that is hasty only to want.

Your task is to define scarcity and opportunity cost, name the four resources and describe a choice you made. Take the four question check.""" + CLOSE,
 quiz=[
 ("Scarcity means:", ["Wants are unlimited but resources are limited", "There is too much of everything", "Prices are low", "Money has no value"], 0, "Scarcity is the basic economic problem."),
 ("Opportunity cost is:", ["The value of the next best alternative you give up", "The price tag only", "A tax", "A kind of profit"], 0, "Every choice gives something up."),
 ("An incentive is:", ["A reward or penalty that influences behavior", "A kind of loan", "A government office", "A type of resource"], 0, "People respond to incentives."),
 ("Which is a capital resource?", ["A machine in a factory", "A forest", "A worker's time", "An idea only"], 0, "Capital means tools, buildings and machines."),
 ]),
 dict(t="1.2 Supply, Demand and Prices", std=S1,
 body="""In a market, buyers and sellers meet to trade. Demand is the amount of a good that buyers are willing and able to buy at different prices. The law of demand says that, other things equal, as the price rises, the quantity demanded falls. Supply is the amount that sellers are willing to offer at different prices. The law of supply says that as the price rises, the quantity supplied rises, because higher prices make selling more profitable.

Where the supply and demand curves cross is the equilibrium price, the price at which the amount buyers want equals the amount sellers offer. If the price is above equilibrium, a surplus appears and sellers lower prices. If the price is below equilibrium, a shortage appears and prices rise. This is how markets send signals without anyone giving orders.

Demand shifts when something other than price changes, such as income, tastes, the price of related goods, or the number of buyers. Supply shifts when costs, technology, or the number of sellers change. A bad harvest cuts supply and raises the price of food. A popular new phone raises demand.

Honest prices matter to God. Proverbs 11:1 says, A false balance is abomination to the LORD: but a just weight is his delight. Proverbs 11:26 adds, He that withholdeth corn, the people shall curse him: but blessing shall be upon the head of him that selleth it. Price gouging in an emergency and cheating customers are not honest dealing.

Worked example: a hurricane closes roads and bottled water becomes scarce. Supply falls, so the price tends to rise, which can attract more shipments. Common mistake: confusing a change in quantity demanded, caused by price, with a change in demand, caused by something else.

Your task: (1) State the laws of supply and demand. (2) Explain equilibrium, surplus and shortage. (3) Give an example of an event that shifts supply and one that shifts demand.""",
 script="""Welcome back. Listen, prices are the language of the market, and today you will learn to read it.

Demand is how much buyers are willing and able to buy at different prices. The law of demand says that as the price goes up, the quantity demanded goes down. Supply is how much sellers offer. The law of supply says that as the price goes up, sellers offer more.

Now watch this. Where supply and demand meet is the equilibrium price. Above it, there is a surplus and sellers lower prices. Below it, there is a shortage and prices rise. No one gives orders, yet the market sends signals.

Demand shifts when income, tastes or the number of buyers changes. Supply shifts when costs, technology or the number of sellers changes. A bad harvest cuts supply and raises food prices.

God cares about honest dealing. Proverbs 11:1 says, A false balance is abomination to the LORD: but a just weight is his delight. Cheating customers or taking cruel advantage in an emergency is not honest.

Your task is to state the two laws, explain equilibrium, surplus and shortage and give an example of a shift in supply and in demand. Take the four question check.""" + CLOSE,
 quiz=[
 ("The law of demand says that as price rises:", ["Quantity demanded falls", "Quantity demanded rises", "Supply disappears", "Income rises"], 0, "Buyers buy less at higher prices."),
 ("A surplus happens when the price is:", ["Above equilibrium", "Below equilibrium", "Equal to cost", "Zero"], 0, "Sellers have more than buyers want."),
 ("A bad harvest most directly causes:", ["A decrease in supply", "A decrease in demand", "A lower price", "A tax cut"], 0, "Less food is offered, so prices tend to rise."),
 ("Proverbs 11:1 calls God's delight:", ["A just weight", "A false balance", "A hidden price", "A large profit"], 0, "Honest dealing pleases God."),
 ]),
 dict(t="1.3 Economic Systems and Free Enterprise", std=S1,
 body="""Every society must answer three questions: What to produce? How to produce it? For whom to produce it? An economic system is the way a society answers them. In a traditional economy, custom and family roles decide. In a command economy, the government decides and owns most resources. In a market economy, millions of buyers and sellers decide through prices, and private people own property. Most nations use a mixed economy, in which markets do most of the work and government plays some role.

The United States is mainly a market economy with a role for government. Free enterprise rests on several ideas: private property rights, economic freedom, voluntary exchange, competition, and the profit motive. Profit is the reward for taking risks and serving customers well. Competition pushes businesses to improve quality and lower prices. Government sets the rules by enforcing contracts, protecting property, providing public goods such as roads and defense, and limiting fraud and unfair practices.

The Bible values work, ownership and fair dealing. Proverbs 14:23 says, In all labour there is profit: but the talk of the lips tendeth only to penury. Deuteronomy 8:18 says, But thou shalt remember the LORD thy God: for it is he that giveth thee power to get wealth. Christians receive business skill as a gift and use it with honesty and generosity, never through theft or oppression.

No system is perfect. Markets can fail when pollution, monopolies or false information harm others, and command systems often lack incentives and freedom. Citizens should weigh tradeoffs honestly.

Worked example: a family opens a bakery. They own the shop, set their own prices, and compete with other bakeries. If the bread is poor, customers leave. Common mistake: thinking that profit means cheating. Honest profit rewards service.

Your task: (1) Compare traditional, command, market and mixed economies. (2) List four features of free enterprise. (3) Explain one proper role of government in a market.""",
 script="""Welcome back. Listen, every nation has to answer three questions: what to produce, how to produce it and for whom.

A traditional economy follows custom. A command economy lets government decide and own most resources. A market economy lets buyers and sellers decide through prices, with private property. Most nations are mixed economies, with markets doing most of the work and government playing a role.

Now watch this. Free enterprise rests on private property, economic freedom, voluntary exchange, competition and the profit motive. Profit rewards risk and good service. Competition pushes businesses to improve quality and lower prices. Government sets the rules: enforcing contracts, protecting property, providing roads and defense and stopping fraud.

Scripture honors work and honest gain. Proverbs 14:23 says, In all labour there is profit: but the talk of the lips tendeth only to penury. Deuteronomy 8:18 says, it is he that giveth thee power to get wealth. We use that power with honesty and generosity.

No system is perfect. Pollution, monopolies and false information can harm people, and command systems often lack freedom and incentives.

Your task is to compare four systems, list four features of free enterprise and explain one role of government. Take the four question check.""" + CLOSE,
 quiz=[
 ("In a market economy, most decisions are made by:", ["Buyers and sellers through prices", "A single ruler", "Custom only", "Foreign nations"], 0, "Prices guide choices."),
 ("Most nations today have a:", ["Mixed economy", "Pure command economy", "Barter only", "No economy"], 0, "Markets and government work together."),
 ("Profit in free enterprise is the reward for:", ["Taking risks and serving customers", "Cheating", "Government gifts", "Avoiding work"], 0, "Honest profit rewards service."),
 ("Deuteronomy 8:18 says it is the LORD who gives:", ["Power to get wealth", "Prices", "Taxes", "Laws of supply"], 0, "Our abilities are gifts from God."),
 ]),
 dict(t="1.4 Money, Banking and the Federal Reserve", std=S1,
 body="""Money is anything widely accepted in exchange for goods and services. It does three jobs: a medium of exchange (you can buy things with it), a store of value (it keeps purchasing power over time), and a unit of account (it lets us compare prices). Before money, people used barter, trading goods directly, which required a double coincidence of wants. Money solves that problem. Good money is durable, portable, divisible, scarce and accepted by others. Today money includes coins, paper currency and bank deposits, and more payments are made by card and phone.

Banks take deposits and lend most of the money to borrowers, earning interest from loans and paying savers a smaller rate. This is how savings become loans for homes, cars and businesses. In the United States the Federal Deposit Insurance Corporation, or FDIC, insures deposits at member banks up to two hundred fifty thousand dollars per depositor, per bank, per ownership category.

The central bank of the United States is the Federal Reserve, created by Congress in 1913. It has a dual mandate: maximum employment and stable prices. Its main tool is influencing interest rates, especially the federal funds rate, and it also buys and sells government securities. When the Fed raises rates, borrowing costs more and spending tends to slow. When it lowers rates, borrowing is cheaper and spending tends to rise.

Scripture warns about honest money. Proverbs 22:1 says, A good name is rather to be chosen than great riches, and loving favour rather than silver and gold. Proverbs 16:11 says, A just weight and balance are the LORD'S: all the weights of the bag are his work. Money should be honest, and so should our dealing with it.

Worked example: you deposit one thousand dollars in a savings account at two percent interest. After one year you earn twenty dollars. Common mistake: keeping all savings in cash at home, where it earns nothing and can be lost.

Your task: (1) List the three functions of money. (2) Explain how banks turn savings into loans. (3) Describe the Federal Reserve's two goals.""",
 script="""Welcome back. Listen, money is a tool, and you should understand how it works.

Money is anything widely accepted in exchange. It does three jobs: a medium of exchange, a store of value and a unit of account. Before money people used barter, which was hard because you needed someone who wanted exactly what you had. Good money is durable, portable, divisible, scarce and accepted.

Now watch this. Banks take deposits and lend most of that money to borrowers. They earn interest on loans and pay savers a smaller rate. That is how savings become homes, cars and businesses. The FDIC insures deposits up to two hundred fifty thousand dollars per depositor, per bank, per ownership category.

The Federal Reserve is our central bank, created in 1913. Its goals are maximum employment and stable prices. When it raises interest rates, borrowing costs more and spending slows. When it lowers rates, borrowing is cheaper and spending tends to rise.

Proverbs 22:1 says, A good name is rather to be chosen than great riches. Proverbs 16:11 says, A just weight and balance are the LORD'S. Be honest with money.

Your task is to list the functions of money, explain how banks make loans and describe the Fed's goals. Take the four question check.""" + CLOSE,
 quiz=[
 ("Which is NOT a function of money?", ["Producing goods", "Medium of exchange", "Store of value", "Unit of account"], 0, "Money exchanges, stores and measures value."),
 ("The FDIC insures deposits up to:", ["$250,000 per depositor, per bank, per category", "$1,000", "$10 million", "Nothing"], 0, "Insured deposits are protected if a bank fails."),
 ("The Federal Reserve was created in:", ["1913", "1776", "1865", "1999"], 0, "Congress created it in 1913."),
 ("When the Fed raises interest rates, borrowing generally:", ["Becomes more expensive", "Becomes cheaper", "Stops completely", "Is free"], 0, "Higher rates raise the cost of loans."),
 ]),
 ],
 assess=dict(t="Assessment 1: Economic Foundations",
 prompt="""Write a report of at least 250 words on the foundations of economics. Use complete sentences and label each part. Proverbs 21:5 says, The thoughts of the diligent tend only to plenteousness; but of every one that is hasty only to want.

Part 1: Define scarcity, opportunity cost and incentives, and give an example of each from your own life.
Part 2: Explain the laws of supply and demand and describe equilibrium, surplus and shortage.
Part 3: Compare a market economy with a command economy and list four features of free enterprise.
Part 4: Explain the three functions of money, how banks make loans and the goals of the Federal Reserve.
Part 5: Explain how honest dealing, as taught in Proverbs 11:1, strengthens an economy.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 20 points. Part 3: 20 points. Part 4: 20 points. Part 5: 15 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 1: Wise Choices",
 prompt="""Write a post of at least 120 words that (1) describes a choice teens often make with limited money or time, (2) names the opportunity cost, (3) explains how an incentive could change the choice, and (4) connects your answer to Proverbs 21:5 or Genesis 41:36. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Why do honest prices matter to a community?"""),
 unit_quiz=[
 ("Scarcity forces people to:", ["Make choices", "Stop working", "Avoid markets", "Print money"], 0, "Limited resources require choices."),
 ("Opportunity cost is:", ["The next best alternative given up", "The sale price", "A kind of tax", "Profit"], 0, "Every choice has a cost."),
 ("Land, labor, capital and entrepreneurship are:", ["The four kinds of resources", "Four taxes", "Four banks", "Four prices"], 0, "These are the factors of production."),
 ("If the price is below equilibrium, there is a:", ["Shortage", "Surplus", "Tax", "Monopoly"], 0, "Buyers want more than sellers offer."),
 ("A mixed economy combines:", ["Markets and some government role", "Barter only", "Custom only", "No property"], 0, "Most nations are mixed."),
 ("Which is a proper role of government in a market?", ["Enforcing contracts and stopping fraud", "Setting every price", "Owning every business", "Banning competition"], 0, "Rules protect honest trade."),
 ("The Federal Reserve's goals are maximum employment and:", ["Stable prices", "Higher taxes", "Fewer banks", "Lower wages"], 0, "This is its dual mandate."),
 ("Proverbs 11:1 says God delights in:", ["A just weight", "A false balance", "A hidden fee", "A quick profit"], 0, "Honest dealing pleases God."),
 ],
)
