"""Economics with Financial Literacy final module."""
FOCUS = ("Economics with Financial Literacy is a one semester course that meets the Florida requirement for economics with financial literacy. Students learn how scarcity, choice, incentives, supply and demand, and prices work, how economic systems, money, banking and the Federal Reserve shape daily life, and how GDP, inflation, unemployment and the business cycle describe the economy. Students then study taxes, trade, careers, paychecks, and wise consumer choices. The financial literacy unit covers budgeting, saving, emergency funds, banking, credit, debt, credit scores, compound interest, investing, risk, insurance, taxes, fraud protection and giving. Students practice the biblical principles of honesty, diligence, planning and stewardship from the King James Version. The course ends with a final personal finance plan and a final exam. Excellence, Faith, Purpose.")

FINAL_ASSESS = dict(t="Final Assessment: My Personal Financial Plan",
 prompt="""Create a personal financial plan of at least 600 words and prepare a short presentation of its main ideas. Use complete sentences and label each part. Use sample numbers only and do not share private financial details. Proverbs 21:5 says, The thoughts of the diligent tend only to plenteousness; but of every one that is hasty only to want.

Part 1: Economic foundations. Explain scarcity, opportunity cost and supply and demand, using one example from your own life.
Part 2: The economy. Explain GDP, inflation, unemployment and the business cycle, and tell how inflation affects savings.
Part 3: Career and income. Choose a career, describe the training it needs and calculate a sample net monthly income after FICA taxes of 6.2 and 1.45 percent and an estimated income tax withholding that you state.
Part 4: Budget. Build a monthly budget with giving, saving, fixed and variable expenses.
Part 5: Credit and debt. Explain APR, credit scores and your plan to avoid unnecessary debt, with reference to Romans 13:8 or Proverbs 22:7.
Part 6: Saving and investing. Set one short term and one long term goal, use the rule of 72 to estimate doubling time and explain diversification.
Part 7: Protection. Explain insurance and three ways to avoid fraud.
Part 8: Faith and giving. Apply at least three Scriptures from the King James Version and describe your giving plan.
Part 9: Presentation plan. List five main points you would share in a three minute talk.""",
 rubric="""100 points. Part 1: 10 points. Part 2: 10 points. Part 3: 10 points. Part 4: 15 points. Part 5: 10 points. Part 6: 15 points. Part 7: 10 points. Part 8: 10 points. Part 9: 5 points. Grammar, conventions and accuracy of calculations: 5 points. A score of 70 or above is passing.""")

FINAL_EXAM = [
 ("Scarcity means:", ["Wants are unlimited but resources are limited", "Prices are too high", "Money is worthless", "Markets do not exist"], 0, "Scarcity is the basic economic problem."),
 ("Opportunity cost is:", ["The value of the next best alternative given up", "The sticker price", "A tax", "Profit"], 0, "Every choice gives something up."),
 ("The law of demand says that as price rises:", ["Quantity demanded falls", "Quantity demanded rises", "Supply stops", "Wages rise"], 0, "Buyers buy less at higher prices."),
 ("A shortage occurs when the price is:", ["Below equilibrium", "Above equilibrium", "At equilibrium", "Zero tax"], 0, "Buyers want more than sellers offer."),
 ("Most nations today have a:", ["Mixed economy", "Pure command economy", "Barter system only", "Traditional system only"], 0, "Markets and government both play a role."),
 ("The Federal Reserve has the goals of maximum employment and:", ["Stable prices", "Higher taxes", "Fewer banks", "Lower wages"], 0, "This is its dual mandate."),
 ("Inflation is:", ["A general rise in prices", "A fall in prices", "A rise in jobs", "A kind of tax"], 0, "It reduces purchasing power."),
 ("Florida has no state:", ["Personal income tax", "Sales tax", "Property tax", "Court system"], 0, "Federal income tax still applies."),
 ("The employee share of FICA includes Social Security at 6.2 percent and Medicare at:", ["1.45 percent", "10 percent", "0.1 percent", "25 percent"], 0, "Employers pay a matching share."),
 ("Net pay is:", ["Pay after deductions", "Pay before taxes", "A bonus", "A loan"], 0, "Budget from net pay."),
 ("Unit price helps you compare:", ["Price per ounce or per item", "Store hours", "Brand colors", "Coupons only"], 0, "It shows the better value."),
 ("A credit score usually ranges from:", ["300 to 850", "1 to 10", "0 to 100", "500 to 5000"], 0, "Higher scores earn better terms."),
 ("By the rule of 72, money at 8 percent doubles in about:", ["9 years", "2 years", "18 years", "72 years"], 0, "72 divided by 8 is 9."),
 ("Romans 13:8 says:", ["Owe no man any thing, but to love one another", "Borrow freely", "Spend quickly", "Trust in riches"], 0, "Debt is a serious commitment."),
 ("2 Corinthians 9:7 says God loveth:", ["A cheerful giver", "A quick spender", "A hidden saver", "A proud lender"], 0, "Giving should come from the heart."),
]
