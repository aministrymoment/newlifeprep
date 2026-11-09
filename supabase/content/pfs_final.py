"""Personal Finance and Stewardship final module: final assessment (position 7) and final exam (quiz position 31)."""

FINAL_ASSESS = dict(t="Final Assessment: My Personal Financial Plan",
 prompt="""Create a complete personal financial plan in a report of at least 700 words. You may use your real situation or a realistic made up one. Do not include real account numbers, Social Security numbers, passwords or other private details, and ask a parent, guardian or teacher to review your plan. Include tables or lists for the numbers. Proverbs 16:3 says, Commit thy works unto the LORD, and thy thoughts shall be established.

Part 1: Stewardship and Goals. Explain what it means to be a steward. Write three SMART goals: one short term, one medium term and one long term.
Part 2: Income and Taxes. Describe your income sources or expected career, and calculate gross pay, estimated deductions and net pay for one month using realistic numbers. Name the forms you would receive and file.
Part 3: Monthly Budget. Build a zero based monthly budget that includes giving, saving, fixed expenses and variable expenses, and show that income minus expenses equals zero.
Part 4: Saving and Banking. Design a plan for a starter emergency fund and then three to six months of expenses. Choose the type of account and explain how you will protect your money from fraud.
Part 5: Credit and Debt. Explain how you will build and protect credit, and write a plan to avoid or pay off debt, including one loan example with principal, interest rate and term.
Part 6: Investing and Retirement. Explain risk, return and diversification, and describe how you would begin investing for the long term, including an employer match or IRA.
Part 7: Protection and Major Purchases. Choose the insurance you would need and explain why. Plan a major purchase such as a car, including the total cost of ownership.
Part 8: Giving, Legacy and Faith. Explain your plan for giving, apply at least three Scripture passages from the King James Version, and write a legacy statement.""",
 rubric="""100 points. Part 1, stewardship and goals: 10 points. Part 2, income and taxes: 10 points. Part 3, monthly budget: 15 points. Part 4, saving and banking: 10 points. Part 5, credit and debt: 15 points. Part 6, investing and retirement: 10 points. Part 7, protection and major purchases: 10 points. Part 8, giving, legacy and faith: 15 points. Grammar, conventions and accurate math: 5 points. A score of 70 or above is passing."""
)

FINAL_EXAM = [
 ("A person who manages what belongs to another is a:", ["Steward", "Debtor", "Landlord", "Beneficiary"], 0, "A steward manages for the owner."),
 ("Something required to live, such as basic food and shelter, is a:", ["Need", "Want", "Luxury", "Gift"], 0, "Needs are required for life."),
 ("Pay after taxes and deductions is called:", ["Net pay", "Gross pay", "Principal", "Profit"], 0, "Net pay is take home pay."),
 ("When spending is greater than income, a budget has a:", ["Deficit", "Surplus", "Dividend", "Premium"], 0, "A deficit means expenses exceed income."),
 ("Moving money to savings as soon as you are paid is called:", ["Paying yourself first", "Overdrafting", "Cosigning", "Refinancing"], 0, "Save before you spend."),
 ("Standard FDIC insurance covers deposits up to:", ["250,000 dollars per depositor, per institution, per ownership category", "2,500 dollars total", "Nothing", "1 million dollars always"], 0, "That is the standard coverage limit."),
 ("A warning sign of a scam is:", ["Pressure to pay with gift cards right away", "A written contract you can read", "Time to compare", "A call to a known number"], 0, "Urgency and odd payment methods signal fraud."),
 ("Interest calculated on principal plus past interest is:", ["Compound interest", "Simple interest", "A fee", "A tax"], 0, "That is compounding."),
 ("Paying only the minimum on a credit card balance usually:", ["Costs much more in interest", "Clears the debt fast", "Lowers the APR", "Raises your savings"], 0, "Interest keeps building."),
 ("The credit score factor with the greatest weight is:", ["Payment history", "Your address", "Your age", "Your job title"], 0, "Paying on time matters most."),
 ("The debt payoff method that targets the highest interest rate first is the:", ["Avalanche", "Snowball", "Minimum", "Balloon"], 0, "The avalanche saves the most interest."),
 ("Spreading money across many investments to reduce risk is:", ["Diversification", "Inflation", "Withholding", "Reconciliation"], 0, "Do not put all your eggs in one basket."),
 ("The amount you pay before insurance begins to pay is the:", ["Deductible", "Premium", "Copay only", "Dividend"], 0, "A deductible is paid first."),
 ("Revenue minus expenses equals:", ["Profit", "Principal", "Premium", "Penalty"], 0, "That is profit."),
 ("2 Corinthians 9:7 says God loveth a:", ["Cheerful giver", "Reluctant giver", "Hidden giver", "Silent giver"], 0, "God values a joyful heart."),
]
