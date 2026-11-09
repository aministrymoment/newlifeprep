"""Economics, Unit 1: Foundations of Economics. Florida economics standards cited at strand level (SS.912.E.1 and SS.912.E.2); recheck exact wording at CPALMS."""
CLOSE = " Excellence, Faith, Purpose. I will see you in the next lesson."

UNIT1 = dict(
 title="Unit 1: Foundations of Economics",
 std="SS.912.E.1, SS.912.E.2",
 topics=[
 dict(t="1.1 Scarcity, Choice and Opportunity Cost", std="SS.912.E.1",
 body="""Economics is the study of how people, businesses and nations use limited resources to meet unlimited wants. The central problem is scarcity: there is never enough time, money or material to satisfy every want. Scarcity is not the same as poverty. Even the richest person has only twenty four hours in a day.

Economists sort resources into four kinds, called factors of production. Land means natural resources such as soil, water and minerals. Labor means the work people do with their minds and bodies. Capital means the tools, machines and buildings used to make other goods. Entrepreneurship means the skill of organizing the other three and taking the risk of starting a business.

Because of scarcity, every choice has a cost. The opportunity cost of a choice is the value of the next best thing you give up. If you spend Saturday working a shift for pay, the opportunity cost might be the football game you missed. Jesus taught this kind of careful thinking in Luke 14:28 when he said that a man who intends to build a tower first sits down and counts the cost. Joseph did the same in Genesis 41, when he planned during seven good years for seven years of famine.

Economists also use the idea of a trade off, which is what you give up, and marginal thinking, which means deciding one more unit at a time. Ask, is one more hour of study worth more to me than one more hour of work?

Your task: (1) Define scarcity and explain why it is not the same as poverty. (2) Name the four factors of production and give an example of each. (3) Describe one real choice you made this week and name its opportunity cost.""",
 script="""Welcome to Economics. I am Dr. Alex L. Jenkins Sr., and I am glad to walk with you through this course. Listen, economics is not just numbers on a chart. It is the study of how we make choices with what we have been given.

Now watch this. The big problem is scarcity. There is never enough time, money or material to satisfy every want. Scarcity is not poverty. Even a billionaire has only twenty four hours in a day.

Look at the four factors of production. Land, which means natural resources. Labor, the work people do. Capital, the tools, machines and buildings that help us make other things. And entrepreneurship, the skill and risk of putting it all together.

Because we cannot have everything, every choice has a cost. We call it opportunity cost, the value of the next best thing you give up. Jesus said in Luke 14:28 that a man building a tower first sits down and counts the cost. Joseph did that in Genesis 41 when he stored food in seven good years to prepare for seven lean ones.

Remember, a trade off is what you give up, and marginal thinking means deciding one more unit at a time.

Your task is to define scarcity, name the four factors of production, and describe one choice you made this week and its opportunity cost. Take the four question check.""" + CLOSE,
 quiz=[
 ("The basic economic problem of scarcity means:", ["Wants are unlimited but resources are limited", "Everyone is poor", "Money has no value", "Goods are free"], 0, "Scarcity is the gap between limited resources and unlimited wants."),
 ("Opportunity cost is:", ["The value of the next best choice you give up", "The price on the tag", "The tax on a purchase", "The cost of a loan"], 0, "Every choice gives up the next best alternative."),
 ("Which is an example of capital as a factor of production?", ["A delivery truck", "A river", "A worker's time", "A business idea"], 0, "Capital means tools, machines and buildings used to make other goods."),
 ("The factor of production that organizes the others and takes the risk is:", ["Entrepreneurship", "Land", "Labor", "Capital"], 0, "Entrepreneurs start and run businesses and bear the risk."),
 ]),
 dict(t="1.2 Economic Systems", std="SS.912.E.1",
 body="""Every nation must answer three basic questions: What goods and services will be produced? How will they be produced? Who will receive them? The way a society answers these questions is called its economic system.

In a traditional economy, customs and family roles decide, and people farm, hunt or craft as their parents did. In a command economy, the government decides what to produce, how much and at what price. The Soviet Union was a command economy, and it often suffered shortages and little innovation. In a market economy, individuals and businesses decide through voluntary trade, and prices guide the choices. Adam Smith, in The Wealth of Nations in 1776, taught that people pursuing their own interests in a free market are led as if by an invisible hand to serve the needs of others.

Most nations today have a mixed economy that blends private choice with some government direction. The United States is a mixed economy that leans strongly toward the market. It protects private property, allows profit and competition, and also provides public schools, roads, and rules against fraud.

A key feature of the market system is private property, the right to own and use what you earn. Another is the profit motive, the hope of gain that leads people to work, invent and take risks. Scripture honors honest work and ownership. Acts 4:32 to 35 describes believers who willingly shared with those in need, a voluntary act of love and not a government order.

Your task: (1) Name the three basic economic questions. (2) Compare a command economy and a market economy. (3) Explain why the United States is called a mixed economy.""",
 script="""Welcome back. Listen, before we study prices and profits, we have to understand the system we live in.

Every nation must answer three questions. What will be produced? How will it be produced? And who will get it? The way a society answers is its economic system.

Now look at the four types. A traditional economy follows custom and family roles. A command economy lets the government decide what to make, how much and at what price. The Soviet Union was a command economy, and it was known for shortages. A market economy lets individuals and businesses decide through voluntary trade, and prices send the signals. Adam Smith wrote in 1776 that people seeking their own interests in a free market are led as if by an invisible hand to serve others.

Watch this. Most nations are mixed. The United States leans toward the market, protects private property, allows profit and competition, and still provides public schools, roads and rules against fraud.

Remember Acts 4. Believers willingly shared with those in need. That was a gift from the heart, not an order from a ruler.

Your task is to name the three questions, compare command and market economies, and explain why we are called a mixed economy. Take the four question check.""" + CLOSE,
 quiz=[
 ("In a command economy, who decides what is produced?", ["The government", "Individual consumers", "Families by custom", "Foreign nations"], 0, "A command economy uses central government planning."),
 ("Adam Smith wrote The Wealth of Nations in:", ["1776", "1492", "1865", "1929"], 0, "Smith published it in 1776."),
 ("The United States economy is best described as:", ["A mixed economy leaning toward the market", "A pure command economy", "A traditional economy", "A barter economy only"], 0, "It blends private choice with some government direction."),
 ("Which is a basic feature of a market economy?", ["Private property and the profit motive", "Government sets every price", "No competition", "No ownership of land"], 0, "Ownership and the hope of gain drive market decisions."),
 ]),
 dict(t="1.3 Supply and Demand", std="SS.912.E.2",
 body="""A market is any place or system where buyers and sellers trade. Demand is the amount of a good that buyers are willing and able to buy at each price. The law of demand says that as the price rises, the quantity demanded falls, and as the price falls, the quantity demanded rises. Supply is the amount that sellers are willing to offer at each price. The law of supply says that as the price rises, the quantity supplied rises.

The price where the amount buyers want equals the amount sellers offer is the equilibrium price. If the price is set above it, a surplus appears, which means more is offered than buyers want. If the price is below it, a shortage appears, which means buyers want more than is offered.

Demand changes when something other than price changes: income, tastes, the price of related goods, the number of buyers, or expectations. If a hurricane warning is issued in South Florida, demand for water and plywood jumps, and the whole demand curve shifts right. Supply changes when the cost of making the good changes, such as wages, materials, technology or taxes. A freeze that ruins the orange crop shifts supply to the left and raises prices.

Proverbs 11:26 says that he who withholdeth corn, the people shall curse him: but blessing shall be upon the head of him that selleth it. Fair selling in a time of need is a moral matter as well as an economic one.

Your task: (1) State the laws of demand and supply. (2) Explain what happens when a price is above equilibrium. (3) Give one example of an event that shifts demand and one that shifts supply.""",
 script="""Welcome back. Listen, if you understand this lesson, you understand how prices are born.

A market is any place or system where buyers and sellers trade. Demand is how much buyers are willing and able to buy at each price. The law of demand says when the price goes up, the quantity demanded goes down. Supply is how much sellers are willing to offer. The law of supply says when the price goes up, the quantity supplied goes up.

Now watch this. Where the two meet is the equilibrium price. Set the price above it and you get a surplus, more offered than anyone wants. Set it below and you get a shortage, more wanted than is offered.

Look at how things shift. When income, tastes, the number of buyers or expectations change, demand shifts. A hurricane warning in South Florida sends demand for water and plywood soaring. When costs change, supply shifts. A freeze that ruins the orange crop cuts supply and raises prices.

Remember Proverbs 11:26. The one who withholds corn from the people is cursed, but blessing rests on the one who sells it fairly.

Your task is to state both laws, explain a surplus, and give one demand shift and one supply shift. Take the four question check.""" + CLOSE,
 quiz=[
 ("According to the law of demand, when the price of a good rises:", ["The quantity demanded falls", "The quantity demanded rises", "Supply disappears", "Nothing changes"], 0, "Price and quantity demanded move in opposite directions."),
 ("A surplus occurs when:", ["The price is above equilibrium", "The price is below equilibrium", "Buyers want more than is offered", "The price is zero"], 0, "At a high price, sellers offer more than buyers want."),
 ("Which event would shift the demand curve for bottled water to the right?", ["A hurricane warning", "A new water bottling machine", "A fall in wages at the bottler", "A tax cut for sellers"], 0, "A storm threat raises how much buyers want at every price."),
 ("The equilibrium price is where:", ["Quantity demanded equals quantity supplied", "The government sets the price", "Sellers earn no profit", "Demand is zero"], 0, "Equilibrium balances buyers and sellers."),
 ]),
 dict(t="1.4 Markets, Prices and Competition", std="SS.912.E.2",
 body="""Prices do three jobs in a market. They give information, because a high price signals that a good is scarce. They give an incentive, because a high price encourages sellers to make more and buyers to use less. And they ration, because they decide who gets a limited good.

Competition is the rivalry among sellers for the buyer's dollar. It pushes sellers to lower prices, raise quality and improve service. Economists describe four market structures. Perfect competition has many small sellers of the same product, such as farmers selling wheat. Monopolistic competition has many sellers of similar but different products, such as restaurants. An oligopoly has a few large sellers, such as airlines. A monopoly has one seller with no close substitutes, which can raise prices without fear of losing customers.

To protect competition, Congress passed the Sherman Antitrust Act in 1890, which banned efforts to create monopolies and fix prices. Government also uses price controls at times. A price ceiling is a maximum price, such as rent control, and it can cause shortages. A price floor is a minimum price, such as a minimum wage or a farm price support, and it can cause surpluses.

Honesty is a part of fair markets. Leviticus 19:35 and 36 commands, Just balances, just weights, a just ephah, and a just hin, shall ye have. Proverbs 20:10 says that divers weights, and divers measures, are both alike abomination to the LORD. Cheating a customer is sin, not just poor business.

Your task: (1) List the three jobs of prices. (2) Name and describe the four market structures. (3) Explain what a price ceiling and a price floor are, and give one effect of each.""",
 script="""Welcome back. Listen, prices are the language of the market, and today you will learn to read it.

Prices do three jobs. They give information, because a high price says a good is scarce. They give an incentive, because a high price tells sellers to make more and buyers to use less. And they ration, because they decide who gets a limited good.

Now look at competition. It is the rivalry among sellers for your dollar, and it pushes them to lower prices and raise quality. There are four market structures. Perfect competition has many small sellers of the same product, like farmers selling wheat. Monopolistic competition has many sellers of similar products, like restaurants. An oligopoly has a few big sellers, like airlines. A monopoly has one seller and no close substitute. In 1890 Congress passed the Sherman Antitrust Act to stop monopolies and price fixing.

Watch this. A price ceiling is a legal maximum, like rent control, and it can cause shortages. A price floor is a legal minimum, like a minimum wage, and it can cause surpluses.

Remember Leviticus 19:35 and 36. Just balances, just weights. Cheating a customer is sin, not just bad business.

Your task is to list the jobs of prices, name the four market structures, and explain ceilings and floors. Take the four question check.""" + CLOSE,
 quiz=[
 ("A market with only one seller and no close substitutes is a:", ["Monopoly", "Perfect competition", "Oligopoly", "Barter market"], 0, "A monopoly has a single seller."),
 ("A price ceiling is:", ["A legal maximum price", "A legal minimum price", "A tax on sellers", "The equilibrium price"], 0, "Rent control is a common example."),
 ("The Sherman Antitrust Act of 1890 was meant to:", ["Stop monopolies and price fixing", "Create a national bank", "Set the minimum wage", "Tax imports"], 0, "It protects competition."),
 ("Which is one job that prices do in a market?", ["Give information and incentives", "Set church doctrine", "Print money", "Choose a president"], 0, "Prices signal scarcity, motivate behavior and ration goods."),
 ]),
 ],
 assess=dict(t="Assessment 1: Foundations of Economics",
 prompt="""Write a report of at least 250 words on the foundations of economics. Use complete sentences and label each part. Luke 14:28 says, For which of you, intending to build a tower, sitteth not down first, and counteth the cost, whether he have sufficient to finish it?

Part 1: Define scarcity and explain how it forces people and nations to make choices.
Part 2: Name the four factors of production and give an example of each.
Part 3: Explain opportunity cost using a real choice that you or your family faced.
Part 4: Compare a command economy and a market economy and explain why the United States is a mixed economy.
Part 5: Explain how supply and demand set a price, and describe what happens when the price is too high or too low.""",
 rubric="""100 points. Part 1: 15 points. Part 2: 20 points. Part 3: 20 points. Part 4: 20 points. Part 5: 20 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 1: Counting the Cost",
 prompt="""Write a post of at least 120 words that (1) describes a time you had to choose between two good things and names the opportunity cost, (2) explains whether you think prices set by supply and demand are fair, and why, (3) tells one way a business owner can be honest in setting prices, and (4) connects your answer to Leviticus 19:35, which says, Ye shall do no unrighteousness in judgment, in meteyard, in weight, or in measure. Then write a respectful reply of at least 40 words to another student's post, or answer this question: Should government ever set a price ceiling during an emergency? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("Economics is the study of:", ["How people use limited resources to meet unlimited wants", "Only the stock market", "Only money", "Only government"], 0, "Scarcity is the foundation of economics."),
 ("Which is NOT a factor of production?", ["Profit", "Land", "Labor", "Capital"], 0, "The four factors are land, labor, capital and entrepreneurship."),
 ("If you give up a movie to work a shift, the movie is your:", ["Opportunity cost", "Profit", "Surplus", "Tariff"], 0, "It is the next best thing you gave up."),
 ("A market economy relies mainly on:", ["Voluntary trade and prices", "Government orders", "Tradition alone", "Foreign aid"], 0, "Individuals and businesses decide in a market."),
 ("When the price is below equilibrium, there is a:", ["Shortage", "Surplus", "Monopoly", "Tariff"], 0, "Buyers want more than sellers offer."),
 ("A frost destroys the orange crop. The supply curve for oranges:", ["Shifts left", "Shifts right", "Does not move", "Becomes a monopoly"], 0, "Less supply is offered at every price."),
 ("An oligopoly has:", ["A few large sellers", "One seller", "Thousands of identical sellers", "No sellers"], 0, "Airlines are a common example."),
 ("Who wrote that an invisible hand guides markets?", ["Adam Smith", "John Locke", "Thomas Jefferson", "Karl Marx"], 0, "Smith wrote The Wealth of Nations in 1776."),
 ])
