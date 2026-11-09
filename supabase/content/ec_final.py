"""Economics final module: final assessment (position 4) and final exam (quiz position 16)."""

FINAL_ASSESS = dict(t="Final Assessment: Economic Choices Report and Presentation",
 prompt="""Write an economics report of at least 500 words and prepare a short presentation of its main ideas. Choose one topic: (a) how supply and demand set the price of one real product in your community, such as gasoline, housing or groceries in South Florida; (b) the plan for a small business you could start, with its costs, prices and profit; (c) how inflation, interest rates or unemployment affect one family and what the Federal Reserve or Congress can do; (d) the effects of trade or a tariff on one product you use; or (e) a topic approved by your administrator. Write complete sentences and label each part. Proverbs 21:5 says, The thoughts of the diligent tend only to plenty; but of every one that is hasty only to want.

Part 1: Question and Thesis. State a clear question and a thesis about your topic.
Part 2: Sources. List at least three reliable sources, such as the Bureau of Labor Statistics, the Bureau of Economic Analysis, the Federal Reserve, a business or a news report, and tell how you judged each.
Part 3: The Report. Explain your topic with an introduction, at least three body paragraphs and a conclusion. Use at least four terms from this course, such as scarcity, opportunity cost, equilibrium, competition, GDP, inflation or comparative advantage, and show how each applies.
Part 4: Scripture Connection. Connect your topic to a passage of Scripture in the King James Version and explain the link.
Part 5: Personal Action Plan. Describe one step you will take to be a wise steward, such as a budget, a savings goal, a plan for credit or a career plan.
Part 6: Presentation Plan. Write a three part outline and an opening line for a three minute talk.""",
 rubric="""100 points. Part 1, question and thesis: 10 points. Part 2, sources: 10 points. Part 3, report content, accuracy and use of course terms: 40 points. Part 4, Scripture connection: 8 points. Part 5, personal action plan: 12 points. Part 6, presentation plan: 10 points. Grammar, conventions and respectful tone: 10 points. A score of 70 or above is passing."""
)

FINAL_EXAM = [
 ("Scarcity means:", ["Wants are unlimited but resources are limited", "Everyone is poor", "Goods are free", "Money has no value"], 0, "Scarcity is the basic economic problem."),
 ("The value of the next best alternative you give up is the:", ["Opportunity cost", "Equilibrium price", "Tariff", "Profit"], 0, "Every choice has an opportunity cost."),
 ("An economy in which individuals and businesses decide through voluntary trade is a:", ["Market economy", "Command economy", "Traditional economy", "Embargo"], 0, "Prices guide choices in a market economy."),
 ("When the price is above equilibrium, there is a:", ["Surplus", "Shortage", "Monopoly", "Deficit"], 0, "Sellers offer more than buyers want."),
 ("A market with a few large sellers, such as airlines, is an:", ["Oligopoly", "Monopoly", "Perfect competition", "Barter market"], 0, "An oligopoly has a few large firms."),
 ("Profit equals:", ["Total revenue minus total costs", "Total costs minus revenue", "Wages plus rent", "Taxes minus revenue"], 0, "A business earns profit when revenue is above costs."),
 ("Education and training increase a worker's:", ["Human capital", "Fixed costs", "Tariffs", "Deficit"], 0, "Human capital is the skill and knowledge of workers."),
 ("The Federal Reserve System was created in:", ["1913", "1776", "1933", "1865"], 0, "Congress passed the Federal Reserve Act in 1913."),
 ("The FDIC protects:", ["Bank deposits", "Stock prices", "Imports", "Business profits"], 0, "It insures deposits at member banks."),
 ("A good that everyone shares and no one can easily be kept from using is a:", ["Public good", "Private good", "Luxury", "Quota"], 0, "National defense is a public good."),
 ("GDP is the market value of:", ["All final goods and services produced in a country in a year", "Only exports", "Only government spending", "The national debt"], 0, "It is the main measure of national output."),
 ("To slow inflation, the Federal Reserve would usually:", ["Raise interest rates", "Lower interest rates", "Cut taxes", "Ban all imports"], 0, "Higher rates cool spending and borrowing."),
 ("A tax on imported goods is a:", ["Tariff", "Quota", "Embargo", "Deficit"], 0, "Tariffs raise the price of imports."),
 ("1,000 dollars at 5 percent simple interest for 3 years earns:", ["150 dollars", "50 dollars", "500 dollars", "1,157 dollars"], 0, "1,000 times 0.05 times 3 equals 150."),
 ("Proverbs 22:7 says, The rich ruleth over the poor, and the borrower is:", ["Servant to the lender", "Master of the bank", "Free of debt", "Rich in time"], 0, "Scripture warns that debt brings obligation."),
]
