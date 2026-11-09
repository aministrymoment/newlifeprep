"""Personal Finance and Stewardship, Unit 2: Budgeting, Saving and Giving. Florida financial literacy standards (SS.912.FL) cited at strand level; recheck exact benchmark codes at CPALMS."""
from pfs_units1 import CLOSE

UNIT2 = dict(
 title="Unit 2: Budgeting, Saving and Giving",
 std="SS.912.FL",
 topics=[
 dict(t="2.1 Building a Budget", std="SS.912.FL",
 body="""A budget is a plan for your money. It tells every dollar where to go before the month begins. Luke 14:28 says, For which of you, intending to build a tower, sitteth not down first, and counteth the cost, whether he have sufficient to finish it? A budget is how a steward counts the cost.

The basic idea is simple: income minus expenses. If expenses are greater than income, the budget has a deficit and the person goes into debt or runs out. If income is greater than expenses, there is a surplus that can be saved, given or invested. The goal is a plan in which the numbers balance.

Start by listing income. Use take home pay, not gross pay, and include gifts and part time work. Then list expenses in two groups. Fixed expenses stay about the same each month, such as rent, a car payment or insurance. Variable expenses change, such as food, gas, clothing and entertainment. Add giving and saving as expenses too, and place them near the top of the list.

A popular guideline is the 50, 30, 20 plan. About half of take home pay goes to needs, about thirty percent to wants, and about twenty percent to saving and paying down debt. Giving can be placed first, with the other percentages adjusted. It is a starting point and not a law. Families in high cost areas may need more for housing, and students may have very different numbers. A zero based budget gives every dollar a job so that income minus planned spending equals zero.

Review the budget every month. Compare planned amounts with actual spending and adjust. Involve your family, since a budget works best when everyone understands it. Proverbs 21:5 says, The thoughts of the diligent tend only to plenteousness.

Your task: (1) Define budget, deficit and surplus. (2) Give three fixed and three variable expenses. (3) Build a sample monthly budget for a part time worker earning 400 dollars.""",
 script="""Welcome back. Listen, Luke 14:28 says, For which of you, intending to build a tower, sitteth not down first, and counteth the cost, whether he have sufficient to finish it? A budget is how a steward counts the cost.

Now watch this. A budget is a plan for every dollar. Income minus expenses. If expenses are larger, you have a deficit. If income is larger, you have a surplus.

List income using take home pay. Then list expenses. Fixed expenses stay the same, like rent or insurance. Variable expenses change, like food, gas and fun. Put giving and saving near the top.

A guideline is 50, 30, 20. Half to needs, thirty percent to wants and twenty percent to saving and debt. It is a starting point, not a law. A zero based budget gives every dollar a job.

Review every month. Compare planned and actual and adjust. Involve your family.

Your task is to define budget terms, list fixed and variable expenses and build a sample budget. Take the four question check.""" + CLOSE,
 quiz=[
 ("When spending is greater than income, the budget has a:", ["Deficit", "Surplus", "Profit", "Refund"], 0, "A deficit means spending exceeds income."),
 ("Rent is usually an example of a:", ["Fixed expense", "Variable expense", "Income", "Tax credit"], 0, "Rent stays about the same each month."),
 ("In the 50, 30, 20 guideline, about 50 percent goes to:", ["Needs", "Wants", "Gifts only", "Entertainment"], 0, "Half of take home pay goes to needs."),
 ("A budget should be built from:", ["Take home pay", "Gross pay only", "Guesses about lottery wins", "Borrowed money"], 0, "Use the amount you actually receive."),
 ]),
 dict(t="2.2 Tracking Spending and Keeping Records", std="SS.912.FL",
 body="""A budget only works when it is compared with real spending. Proverbs 27:23 says, Be thou diligent to know the state of thy flocks, and look well to thy herds. In our day, knowing the state of your flocks means knowing where your money goes.

Tracking spending can be done in many ways. You can write purchases in a notebook, use a spreadsheet, use a bank or budgeting app, or use envelopes of cash for categories such as food and fun. Pick a method you will actually use. Many people are surprised to learn how small daily purchases add up. A four dollar drink each school day costs about seven hundred dollars in a school year.

Records protect you. Keep receipts for large purchases and returns, warranties for products, and bank statements for review. Keep tax records, such as Forms W2 and 1099, for as long as advised by the Internal Revenue Service or your tax preparer. Keep important papers in a safe place, such as a locked box or secure digital folder, with a backup. Important papers include a birth certificate, Social Security card, insurance policies, titles, contracts and wills. Keep sensitive documents private.

A personal balance sheet measures your wealth at one moment. Assets are things you own that have value, such as savings, a car or equipment. Liabilities are what you owe, such as loans or credit card balances. Net worth equals assets minus liabilities. A young person may have low or even negative net worth because of student loans, and the goal is for it to grow over time.

Make a monthly money meeting. Sit down for thirty minutes to check balances, pay bills on time, update the budget and set the next steps. Pay bills before their due dates to avoid late fees.

Your task: (1) Describe two ways to track spending. (2) List five records that should be kept. (3) Define asset, liability and net worth.""",
 script="""Welcome back. Listen, Proverbs 27:23 says, Be thou diligent to know the state of thy flocks, and look well to thy herds. Today that means knowing where your money goes.

Now watch this. Track spending in a notebook, a spreadsheet, an app or cash envelopes. Pick what you will use. Small purchases add up. A four dollar drink each school day costs about seven hundred dollars in a school year.

Keep records. Keep receipts for big purchases, warranties and bank statements. Keep tax forms such as the W2 and 1099 as advised. Store important papers safely, like a birth certificate, Social Security card, insurance policies, titles and contracts. Keep sensitive papers private.

A balance sheet shows wealth at one moment. Assets are what you own. Liabilities are what you owe. Net worth is assets minus liabilities. It may start low, and the goal is growth.

Hold a monthly money meeting. Check balances, pay bills on time and adjust the budget.

Your task is to describe tracking methods, list records and define net worth. Take the four question check.""" + CLOSE,
 quiz=[
 ("Things you own that have value are called:", ["Assets", "Liabilities", "Deductions", "Expenses"], 0, "Assets are valuable things you own."),
 ("Money that you owe is a:", ["Liability", "Asset", "Surplus", "Refund"], 0, "A liability is a debt or obligation."),
 ("Net worth is calculated as:", ["Assets minus liabilities", "Income plus tax", "Assets plus liabilities", "Gross pay minus net pay"], 0, "Subtract what you owe from what you own."),
 ("Proverbs 27:23 encourages a person to:", ["Know the state of his flocks", "Ignore his finances", "Borrow freely", "Hide his money"], 0, "Be diligent to know your financial condition."),
 ]),
 dict(t="2.3 Saving and the Emergency Fund", std="SS.912.FL",
 body="""Saving is setting aside money now for use later. Proverbs 6:6 to 8 sends us to a small teacher: Go to the ant, thou sluggard; consider her ways, and be wise: Which having no guide, overseer, or ruler, Provideth her meat in the summer, and gathereth her food in the harvest. Proverbs 21:20 says, There is treasure to be desired and oil in the dwelling of the wise; but a foolish man spendeth it up.

Joseph provides a larger example. In Genesis 41:36 he advised Pharaoh, And that food shall be for store to the land against the seven years of famine, which shall be in the land of Egypt; that the land perish not through the famine. Saving in good times protected a nation in hard times.

There are three main reasons to save. First, for emergencies, such as a medical bill, a car repair or a lost job. Second, for planned goals, such as a car, school or a trip. Third, for the long term, such as retirement. An emergency fund is money kept in a safe, easy to reach account for unexpected needs. A common guideline is to build a small starter fund first, such as one thousand dollars, and then work toward three to six months of basic living expenses.

The best way to save is to pay yourself first. Move money to savings as soon as you are paid, before you spend it, preferably by an automatic transfer. Small amounts add up, and starting early matters because of compound interest, which we study later. Keep savings in an insured account at a bank or credit union, not under the mattress. Use separate accounts or labels for different goals so that you can see progress.

Resist the urge to use the emergency fund for wants such as sales. If you use it, refill it.

Your task: (1) Give three reasons to save. (2) Explain pay yourself first. (3) Set a savings plan for a one thousand dollar starter emergency fund.""",
 script="""Welcome back. Listen, Proverbs 6:6 to 8 says, Go to the ant, thou sluggard; consider her ways, and be wise: Which having no guide, overseer, or ruler, Provideth her meat in the summer, and gathereth her food in the harvest. The ant saves in good times.

Now watch this. Joseph told Pharaoh in Genesis 41:36 that food should be for store against the seven years of famine. Saving in good times protected a nation.

Save for emergencies, for planned goals and for the long term. An emergency fund is money in a safe, reachable account. Start with a starter fund, like one thousand dollars, then build toward three to six months of basic expenses.

Pay yourself first. Move money to savings as soon as you are paid, ideally by an automatic transfer. Start early because of compound interest. Keep savings in an insured account. Use separate labels for different goals.

Do not use the emergency fund for sales. If you use it, refill it.

Your task is to give reasons to save, explain pay yourself first and make a plan for a starter fund. Take the four question check.""" + CLOSE,
 quiz=[
 ("Money set aside for unexpected needs is an:", ["Emergency fund", "Expense account", "Credit line", "Tax return"], 0, "An emergency fund covers surprises."),
 ("Paying yourself first means:", ["Moving money to savings when you are paid", "Spending before paying bills", "Taking a loan", "Skipping savings"], 0, "Save before you spend."),
 ("Who saved food in good years against a famine in Genesis 41?", ["Joseph", "Moses", "Samson", "Gideon"], 0, "Joseph advised storing food."),
 ("A common long term goal for the emergency fund is:", ["Three to six months of basic expenses", "One day of pay", "No savings", "Ten years of income"], 0, "That range is a widely used guideline."),
 ]),
 dict(t="2.4 Giving, Tithes and Generosity", std="SS.912.FL",
 body="""Giving is a central part of Christian stewardship. Deuteronomy 8:18 says, But thou shalt remember the LORD thy God: for it is he that giveth thee power to get wealth. Because God is the source, we honor Him with what He gives. Proverbs 3:9 and 10 say, Honour the LORD with thy substance, and with the firstfruits of all thine increase: So shall thy barns be filled with plenty, and thy presses shall burst out with new wine.

The tithe, which means a tenth, is taught in the Law. Malachi 3:10 says, Bring ye all the tithes into the storehouse, that there may be meat in mine house, and prove me now herewith, saith the LORD of hosts, if I will not open you the windows of heaven, and pour you out a blessing, that there shall not be room enough to receive it. Many churches teach the tithe as the starting place of giving, and offerings go beyond it. A believer who tithes places it in the budget first, as firstfruits, instead of giving what is left over.

The spirit of giving matters as much as the amount. 2 Corinthians 9:7 says, Every man according as he purposeth in his heart, so let him give; not grudgingly, or of necessity: for God loveth a cheerful giver. Plan your giving ahead of time and give with joy.

God also calls us to care for those in need. Proverbs 19:17 says, He that hath pity upon the poor lendeth unto the LORD; and that which he hath given will he pay him again. Ephesians 4:28 says we labour that we may have to give to him that needeth. Giving can include time, skills and food as well as money.

Wise giving also checks where gifts go. Give to your local church and to trusted ministries and charities. Be careful of appeals that pressure you or promise riches. Keep records of gifts for your own accounting, and ask the church or charity for a receipt for tax purposes where it applies.

Your task: (1) Define tithe and firstfruits. (2) Explain what 2 Corinthians 9:7 says about the attitude of giving. (3) Describe how you will include giving in your budget.""",
 script="""Welcome back. Listen, Proverbs 3:9 and 10 say, Honour the LORD with thy substance, and with the firstfruits of all thine increase: So shall thy barns be filled with plenty. Deuteronomy 8:18 reminds us that it is God who giveth thee power to get wealth.

Now watch this. The tithe means a tenth. Malachi 3:10 says, Bring ye all the tithes into the storehouse, that there may be meat in mine house, and prove me now herewith. Many churches teach the tithe as the starting place of giving, and offerings go beyond it. Give from the first, not from what is left.

Attitude matters. 2 Corinthians 9:7 says, Every man according as he purposeth in his heart, so let him give; not grudgingly, or of necessity: for God loveth a cheerful giver. Plan ahead and give with joy.

Care for the needy. Proverbs 19:17 says, He that hath pity upon the poor lendeth unto the LORD. Giving includes time, skills and food.

Be wise. Give to your church and trusted ministries. Beware of pressure and promises of riches. Keep records and ask for receipts.

Your task is to define tithe and firstfruits, explain cheerful giving and plan giving in your budget. Take the four question check.""" + CLOSE,
 quiz=[
 ("The word tithe means:", ["A tenth", "A half", "A fifth", "A hundredth"], 0, "A tithe is one tenth."),
 ("2 Corinthians 9:7 says God loves:", ["A cheerful giver", "A reluctant giver", "A silent giver", "A secret hoarder"], 0, "God values a joyful heart."),
 ("Giving the first part of increase to God is called giving:", ["Firstfruits", "Leftovers", "Interest", "Change"], 0, "Firstfruits honor God first."),
 ("Wise giving includes:", ["Giving to trusted churches and charities and keeping records", "Giving under pressure to anyone", "Never planning gifts", "Giving only what is left"], 0, "Be planned and careful."),
 ]),
 ],
 assess=dict(t="Assessment 2: Budgeting, Saving and Giving",
 prompt="""Write a report of at least 250 words, with sample work, on budgeting, saving and giving. Use complete sentences and label each part. Luke 14:28 says, For which of you, intending to build a tower, sitteth not down first, and counteth the cost, whether he have sufficient to finish it?

Part 1: Define budget, deficit, surplus, fixed expense and variable expense. Build a monthly budget for a part time worker who takes home 500 dollars, including giving and saving, and show that income minus expenses equals zero.
Part 2: Describe a method for tracking spending that you would use. List five records that should be kept and where you would keep them.
Part 3: Define asset, liability and net worth, and calculate net worth for someone with 1,200 dollars in assets and 400 dollars in liabilities.
Part 4: Explain why an emergency fund matters, what pay yourself first means, and make a savings plan for a 1,000 dollar starter fund. Use Proverbs 6:6 to 8 or Genesis 41:36.
Part 5: Define tithe and firstfruits, explain 2 Corinthians 9:7, and describe how you will give wisely.""",
 rubric="""100 points. Part 1: 25 points. Part 2: 15 points. Part 3: 15 points. Part 4: 20 points. Part 5: 20 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 2: Counting the Cost and Giving with Joy",
 prompt="""Write a post of at least 120 words that (1) describes a time when planning ahead helped you or someone you know, (2) explains in your own words why a budget helps a steward, (3) explains how a person can save and give at the same time, and (4) connects your answer to Luke 14:28, Proverbs 6:6 to 8, Malachi 3:10 or 2 Corinthians 9:7. Then write a respectful reply of at least 40 words to another student's post, or answer this question: What is one small spending habit you could change to save more? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("A plan that tells your money where to go is a:", ["Budget", "Loan", "Receipt", "Tax return"], 0, "That is the purpose of a budget."),
 ("A car payment that stays the same each month is a:", ["Fixed expense", "Variable expense", "Gift", "Asset"], 0, "Payments that do not change are fixed."),
 ("Assets minus liabilities equals:", ["Net worth", "Gross pay", "Interest", "Deficit"], 0, "That is the definition of net worth."),
 ("An emergency fund is meant for:", ["Unexpected needs", "Sales and wants", "Gifts only", "Entertainment"], 0, "It covers surprises like repairs or lost work."),
 ("The best way to build savings is to:", ["Pay yourself first by automatic transfer", "Save what is left, if any", "Wait until you are older", "Borrow to save"], 0, "Saving first makes it happen."),
 ("Proverbs 6:6 sends the sluggard to learn from:", ["The ant", "The lion", "The eagle", "The ox"], 0, "The ant gathers food in the harvest."),
 ("The tithe is:", ["A tenth", "A half", "A twentieth", "A bonus"], 0, "Tithe means tenth."),
 ("2 Corinthians 9:7 teaches that giving should be:", ["Cheerful and purposed in the heart", "Grudging", "Forced", "Hidden from God"], 0, "God loves a cheerful giver."),
 ])
