"""Entrepreneurship final module: final assessment (position 7) and final exam (quiz position 31)."""

FINAL_ASSESS = dict(t="Final Assessment: My Business Plan and Stewardship Reflection",
 prompt="""Create a business plan and reflection of at least 800 words in total. Use a sample or practice business only. Do not include real bank account numbers, Social Security numbers, passwords, home addresses, phone numbers or any private details about yourself, your family or other people. Share your plan with a parent, guardian or teacher for review before you present it to anyone. This plan is practice and general education, not legal, tax or financial advice, and you must not start a real business, sign a contract, borrow money or accept money without an adult.

Part 1: Executive Summary and Company Description. Name your business, state the idea, the mission and three values, and choose a legal structure with a reason. Note that real legal choices require professional advice.
Part 2: Market Analysis. Describe your target customer, five findings from research or interviews with at least ten possible customers, two direct and two indirect competitors, your value proposition and a four box SWOT.
Part 3: Marketing and Sales Plan. Describe the four Ps, your brand, an honest advertisement, a sales pitch and your customer service and refund policy.
Part 4: Operations and People Plan. Describe suppliers, inventory, quality and safety rules, a weekly checklist, online safety rules and the people you would need, including fair pay and child labor limits.
Part 5: Financial Plan. Using sample figures only, list startup costs, price your product with a markup, compute the break even point, forecast six months of revenue and profit, describe your cash flow, taxes you would set aside and a sensitivity check. Show your work.
Part 6: Risk, Giving and Growth. Name three risks with a response for each, describe a giving plan and explain one growth step you would take only after a successful pilot.
Part 7: Pitch. Write a two minute pitch that answers the six pitch questions.
Part 8: Faith and Reflection. Apply at least three Scripture passages from the King James Version, such as Proverbs 22:29, Luke 14:28, Colossians 3:23, Proverbs 3:9 or Matthew 25:14 to 30, to your plan, and explain what faithful stewardship means to you.""",
 rubric="""100 points. Part 1, summary and description: 10 points. Part 2, market analysis: 15 points. Part 3, marketing and sales: 15 points. Part 4, operations and people: 10 points. Part 5, financial plan: 20 points. Part 6, risk, giving and growth: 10 points. Part 7, pitch: 10 points. Part 8, faith and reflection: 5 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing. Deduct points if private information or real account numbers appear in the submission."""
)

FINAL_EXAM = [
 ("An entrepreneur is a person who:", ["Sees a need and organizes resources to meet it", "Avoids all risk", "Never serves customers", "Only works for others"], 0, "Entrepreneurs meet needs through business."),
 ("Proverbs 11:1 says a false balance is:", ["An abomination to the LORD", "A smart tool", "A good name", "A profit"], 0, "Honest weights please God."),
 ("A business structure that can protect an owner's personal property from many business debts is the:", ["LLC", "Sole proprietorship", "Hobby", "Gift"], 0, "LLC stands for limited liability company."),
 ("A target market is:", ["The specific group you serve best", "Everyone in the world", "Only family", "A tax"], 0, "Targeting helps you serve well."),
 ("A value proposition explains:", ["Why a customer should choose you", "Your home address", "Your tax bracket", "Your age"], 0, "It states the benefit you provide."),
 ("An item costs 20 dollars and you add a 50 percent markup. The price is:", ["30 dollars", "25 dollars", "40 dollars", "10 dollars"], 0, "50 percent of 20 is 10, so the price is 30."),
 ("Revenue of 900 dollars and expenses of 650 dollars give a profit of:", ["250 dollars", "1550 dollars", "650 dollars", "900 dollars"], 0, "900 minus 650 is 250."),
 ("Fixed costs 400 dollars, price 9 dollars and variable cost 4 dollars. Break even units are:", ["80", "44", "100", "400"], 0, "Margin is 5 and 400 divided by 5 is 80."),
 ("Romans 13:7 teaches us to:", ["Render to all their dues", "Hide income", "Avoid records", "Ignore the law"], 0, "Honest taxes are part of citizenship."),
 ("The first step in handling a complaint is to:", ["Listen without interrupting", "Argue", "Blame the customer", "Hang up"], 0, "Listening shows respect."),
 ("A student starting a real business should:", ["Involve a parent or guardian", "Hide it from adults", "Meet strangers alone", "Post a home address online"], 0, "Adult involvement protects young people."),
 ("Mark 10:43 and 44 teaches that the greatest leader is a:", ["Servant", "Boss only", "Critic", "Competitor"], 0, "Christian leadership is service."),
 ("Insurance transfers part of a risk to an insurer in exchange for a:", ["Premium", "Grant", "Tithe", "Dividend"], 0, "Premiums buy coverage."),
 ("A sensitivity check in a financial plan asks:", ["What happens if sales or costs change", "What your name is", "Who your friends are", "What color your logo is"], 0, "It tests assumptions."),
 ("In the parable of the talents in Matthew 25, the master praised servants who were:", ["Faithful with what they had", "Fearful and hidden", "Careless", "Proud"], 0, "Faithful stewardship is rewarded."),
]
