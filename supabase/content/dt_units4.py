"""Digital Technology and Computer Applications, Unit 4: The Internet, Networks and Cybersecurity. Florida standards cited at strand level (SC.912.CS)."""
from dt_units1 import CLOSE

UNIT4 = dict(
 title="Unit 4: The Internet, Networks and Cybersecurity",
 std="Florida computer science and digital literacy course standards",
 topics=[
 dict(t="4.1 How the Internet Works", std="Florida computer science and digital literacy course standards",
 body="""The internet is a worldwide network of networks that connects billions of devices. Psalm 19:4 says of God's creation, Their line is gone out through all the earth, and their words to the end of the world. The internet now carries words, sounds and pictures to the ends of the earth, and it can be used to spread the gospel as well as to spread harm.

The internet is not the same thing as the World Wide Web. The internet is the infrastructure, made of cables, towers, satellites, routers and servers. The web is a service that runs on the internet. It is a system of pages and files you view with a browser. Email, video calls and online games also use the internet.

Here is how it works. A client is a device that asks for information, such as your phone or laptop. A server is a computer that stores information and sends it when asked. Your internet service provider, or ISP, connects you to the wider internet. Every device has an IP address, a number that identifies it so data knows where to go. Because numbers are hard to remember, the Domain Name System, or DNS, works like a phone book, turning a name like newlifeprep.org into the number of the right server.

A web address is called a URL. It includes the protocol, the domain name and the path to a page. The protocol HTTP is the set of rules for sending web pages. HTTPS adds encryption, which scrambles data so others cannot read it, and the lock symbol in the browser shows a secure connection. Look for HTTPS before entering passwords or payment information.

Data does not travel in one piece. It is broken into small packets, sent along different routes and put back together at the destination. Routers decide the path for each packet. This design lets the internet keep working even if part of it fails.

Your task: (1) Explain the difference between the internet and the web. (2) Explain what DNS does. (3) Explain why HTTPS matters.""",
 script="""Welcome back. Listen, Psalm 19:4 says, Their line is gone out through all the earth, and their words to the end of the world. The internet now carries words to the ends of the earth, and we can use it to spread the gospel.

Now watch this. The internet is a worldwide network of networks. It is the infrastructure of cables, towers, satellites, routers and servers. The web is a service that runs on it, a system of pages you view with a browser. Email and video calls use the internet too.

A client asks for information. A server stores it and sends it. Your ISP connects you to the internet. Every device has an IP address. DNS works like a phone book, turning a name like newlifeprep.org into the number of the right server.

A URL is a web address. HTTP is the set of rules for web pages. HTTPS adds encryption. Look for the lock before entering passwords or payments.

Data is broken into packets, sent along different routes and put back together. Routers choose the path.

Your task is to explain the internet and the web, DNS and HTTPS. Take the four question check.""" + CLOSE,
 quiz=[
 ("The Domain Name System works like:", ["A phone book for web names", "A printer", "A battery", "A virus"], 0, "DNS turns names into numbers."),
 ("A device that asks for information is a:", ["Client", "Server", "Router", "Packet"], 0, "Clients request; servers respond."),
 ("HTTPS differs from HTTP because it:", ["Encrypts the connection", "Is slower by design", "Has no address", "Removes the web"], 0, "HTTPS scrambles data in transit."),
 ("Data travels across the internet in small pieces called:", ["Packets", "Folders", "Passwords", "Pixels"], 0, "Packets are reassembled at the destination."),
 ]),
 dict(t="4.2 Networks, WiFi and Devices", std="Florida computer science and digital literacy course standards",
 body="""A network is a group of connected devices that share information and resources. Ecclesiastes 4:12 says, a threefold cord is not quickly broken. Connected people and connected devices can do more together than apart.

Networks are described by size. A local area network, or LAN, covers a small area such as a home, a school or a church building. A wide area network, or WAN, covers a large area, and the internet is the largest WAN. A personal area network, such as Bluetooth between a phone and earbuds, covers a very short range.

Know the equipment. A modem connects your network to your internet service provider. A router directs traffic between devices and the internet, and often includes WiFi. A switch connects wired devices in a local network. An access point extends WiFi coverage. A network interface card lets a device connect. Ethernet is the wired connection, usually faster and more stable. WiFi is the wireless connection, which is convenient but shared and easier to intercept.

Bandwidth is how much data can be sent at once, often measured in megabits per second. More devices using a connection means less for each. A weak signal, distance and walls can slow WiFi.

The Internet of Things, or IoT, is the growing group of everyday objects connected to the internet, such as cameras, doorbells, speakers, thermostats and watches. They are convenient but can be a security risk if left with default passwords or out of date software.

Secure your network. Change the default router name and password. Use the strongest encryption available, such as WPA3 or WPA2. Keep the router firmware updated. Create a guest network for visitors. Turn off features you do not use. On public WiFi, avoid sensitive tasks, or use a trusted virtual private network, or VPN, which encrypts your traffic. Confirm the network name with the owner, since criminals create fake hotspots with believable names.

Your task: (1) Compare a LAN and a WAN. (2) Name the jobs of a modem and a router. (3) List four ways to secure a home network.""",
 script="""Welcome back. Listen, Ecclesiastes 4:12 says, a threefold cord is not quickly broken. Connected people and connected devices can do more together.

Now watch this. A network is a group of connected devices that share information. A LAN covers a small area like a home, school or church. A WAN covers a large area, and the internet is the largest one. Bluetooth is a personal area network.

A modem connects your network to your ISP. A router directs traffic and often provides WiFi. A switch connects wired devices. Ethernet is wired and usually faster and steadier. WiFi is wireless and convenient, but easier to intercept.

Bandwidth is how much data can be sent at once. More devices mean less for each.

The Internet of Things includes cameras, doorbells, speakers and watches. Change their default passwords and keep them updated.

Secure your network. Change the router name and password. Use WPA3 or WPA2. Update the router. Use a guest network. On public WiFi, avoid sensitive tasks or use a trusted VPN. Confirm the network name, since fake hotspots exist.

Your task is to compare LAN and WAN, name the jobs of a modem and router and list ways to secure a home network. Take the four question check.""" + CLOSE,
 quiz=[
 ("A network that covers a home or a church building is a:", ["LAN", "WAN", "DNS", "URL"], 0, "A local area network is small in size."),
 ("The device that directs traffic between your devices and the internet is a:", ["Router", "Monitor", "Mouse", "Speaker"], 0, "Routers direct network traffic."),
 ("A good first step to secure a new router is to:", ["Change the default password", "Leave the default password", "Turn off updates", "Share the password publicly"], 0, "Default passwords are widely known."),
 ("A VPN is used to:", ["Encrypt your traffic on a network", "Print documents", "Increase screen size", "Delete viruses by itself"], 0, "A VPN protects traffic on untrusted networks."),
 ]),
 dict(t="4.3 Cybersecurity: Threats and Defenses", std="Florida computer science and digital literacy course standards",
 body="""Cybersecurity is the practice of protecting devices, networks and information from attack. Nehemiah 4:9 says, Nevertheless we made our prayer unto our God, and set a watch against them day and night. Nehemiah prayed and posted guards while rebuilding the wall. We also pray and stay watchful. Churches, schools and families are targets, and Proverbs 22:3 reminds us that a prudent man foreseeth the evil.

Know the threats. Malware is harmful software. A virus attaches to files and spreads when they are opened. A worm spreads by itself across networks. A trojan pretends to be useful software. Spyware secretly watches your activity. Ransomware locks your files and demands payment. Adware shows unwanted advertisements.

Social engineering tricks people instead of machines. Phishing uses fake emails, texts or websites to steal passwords or money. Look for urgent threats, unknown senders, spelling errors, mismatched links and requests for passwords or gift cards. Do not click, and report it. Scams also include fake prizes, fake tech support and messages from a friend whose account was hacked. Attackers often impersonate a pastor or leader to request money, so confirm by another method.

Build layers of defense. Install updates, since they fix known weaknesses. Use antivirus software and a firewall, which filters traffic coming into and out of a network. Use strong, unique passwords with multifactor authentication. Download software only from official stores and trusted sites. Do not plug in unknown USB drives. Encrypt sensitive files and devices, and lock your screen. Limit who has administrator access, giving people only the access they need. Back up your files regularly, and keep a copy offline, so ransomware cannot destroy every copy.

If something goes wrong, act quickly. Disconnect from the network, tell a trusted adult or the person in charge of technology, change passwords from a clean device, run a scan and report fraud to the right authorities. Do not pay a ransom without expert advice. Learn from what happened and improve your defenses.

Your task: (1) Define malware, ransomware and phishing. (2) List five layers of defense. (3) Describe what to do if you think your device has been hacked.""",
 script="""Welcome back. Listen, Nehemiah 4:9 says, Nevertheless we made our prayer unto our God, and set a watch against them day and night. Nehemiah prayed and posted guards. We pray and stay watchful.

Now watch this. Cybersecurity protects devices, networks and information from attack. Malware is harmful software. A virus attaches to files. A worm spreads by itself. A trojan pretends to be useful. Spyware watches you. Ransomware locks your files and demands payment.

Social engineering tricks people. Phishing uses fake emails, texts or websites. Look for urgent threats, unknown senders, spelling errors, mismatched links and requests for passwords or gift cards. Attackers often pretend to be a pastor or leader asking for money. Confirm by another method.

Build layers. Install updates. Use antivirus and a firewall. Use strong passwords with multifactor authentication. Download from official stores. Do not plug in unknown USB drives. Encrypt sensitive files. Limit administrator access. Keep backups, including one offline copy.

If something goes wrong, disconnect, tell a trusted adult, change passwords from a clean device, scan and report fraud.

Your task is to define malware, ransomware and phishing, list defenses and describe what to do after a hack. Take the four question check.""" + CLOSE,
 quiz=[
 ("Malware that locks your files and demands payment is:", ["Ransomware", "Adware", "A firewall", "A router"], 0, "Ransomware holds files hostage."),
 ("Fake messages that trick people into giving passwords are called:", ["Phishing", "Backup", "Streaming", "Booting"], 0, "Phishing uses deception."),
 ("A firewall:", ["Filters network traffic", "Prints pages", "Cleans the screen", "Increases RAM"], 0, "It blocks unwanted traffic."),
 ("An important reason to install software updates is to:", ["Fix known security weaknesses", "Make files disappear", "Remove all passwords", "Slow the device"], 0, "Updates patch vulnerabilities."),
 ]),
 dict(t="4.4 Research, Evaluating Sources and Responsible Use of AI Tools", std="Florida computer science and digital literacy course standards",
 body="""Everyone can publish online, so not everything found there is true. 1 Thessalonians 5:21 says, Prove all things; hold fast that which is good. Good researchers test what they read before they trust or share it.

Search with skill. Choose specific keywords instead of whole questions. Put exact phrases in quotation marks. Narrow results by site type or date. Try different words if the first search fails. Remember that the first result is not always the best, and some top results are paid advertisements. Use library databases, government sites and academic sources for school research.

Evaluate each source with five questions. Who is the author or publisher, and are they qualified? Is the information accurate, supported by evidence and confirmed by other reliable sources? What is the purpose, whether to inform, teach, sell, persuade or entertain? Is it current enough for the topic? Is it relevant to your question? Be careful with sites that have no author, no sources, a strong emotional tone or a strong sales goal. Use lateral reading: leave the page and check what other reliable sources say about the source itself. Misinformation is false information shared without intent to deceive, and disinformation is false information spread on purpose. Pause before sharing, and check headlines, dates and images, since photos can be edited or taken out of context.

Artificial intelligence tools can answer questions, summarize text, help with ideas and write code. Used wisely, they are like a tutor or assistant. But AI can be wrong, can invent facts or sources, and can reflect bias. Always check important facts with reliable sources. Do not enter private information such as full names, addresses, passwords or school records into tools you do not control. Do not present AI work as your own, and follow your teacher's rules about when AI help is allowed. If AI helps you, say how, and make sure your final work shows your own understanding. Proverbs 12:22 says, Lying lips are abomination to the LORD: but they that deal truly are his delight.

Your task: (1) List five questions for evaluating a source. (2) Explain the difference between misinformation and disinformation. (3) Describe three rules for using AI tools honestly.""",
 script="""Welcome back. Listen, 1 Thessalonians 5:21 says, Prove all things; hold fast that which is good. Good researchers test what they read.

Now watch this. Search with skill. Use specific keywords. Put exact phrases in quotation marks. Remember that some top results are paid advertisements.

Evaluate every source. Who is the author and are they qualified? Is it accurate and supported by evidence? What is the purpose, to inform, sell or persuade? Is it current? Is it relevant? Use lateral reading, which means leaving the page to see what other reliable sources say about it.

Misinformation is false information shared without intent to deceive. Disinformation is false information spread on purpose. Pause before sharing. Photos can be edited or taken out of context.

AI tools can be like a tutor or assistant. But AI can be wrong, can invent facts and sources and can reflect bias. Check important facts. Do not enter private information. Do not present AI work as your own. Follow your teacher's rules. If AI helps you, say how, and make sure the final work shows your own understanding. Proverbs 12:22 says, they that deal truly are his delight.

Your task is to list source questions, compare misinformation and disinformation and describe honest AI use. Take the four question check.""" + CLOSE,
 quiz=[
 ("False information spread on purpose is called:", ["Disinformation", "Backup", "A cookie", "A router"], 0, "Disinformation is deliberate."),
 ("Putting words in quotation marks in a search finds:", ["That exact phrase", "Only images", "Nothing", "Random pages"], 0, "Quotation marks search for exact phrases."),
 ("AI tools can sometimes:", ["Give wrong answers and invent sources", "Never be wrong", "Replace all checking", "Know your password"], 0, "AI output must be verified."),
 ("Lateral reading means:", ["Checking what other sources say about a source", "Reading sideways", "Reading faster", "Skipping the author"], 0, "It tests the credibility of a source."),
 ]),
 ],
 assess=dict(t="Assessment 4: The Internet, Networks and Cybersecurity",
 prompt="""Write a report of at least 250 words on the internet and online security. Use complete sentences and label each part. Nehemiah 4:9 says, Nevertheless we made our prayer unto our God, and set a watch against them day and night.

Part 1: Explain the difference between the internet and the World Wide Web. Define client, server, ISP, IP address, DNS, URL and HTTPS, and explain how data travels in packets.
Part 2: Compare a LAN and a WAN. Name the jobs of a modem, a router and a switch. List five steps to secure a home or church network.
Part 3: Define malware, virus, ransomware, spyware and phishing. Describe five warning signs of a phishing message.
Part 4: Describe five layers of defense for a computer or a church office, and explain what to do if a device is hacked.
Part 5: List five questions for evaluating a source, explain misinformation and disinformation, and give three rules for honest use of AI tools. Apply 1 Thessalonians 5:21 and Proverbs 12:22.""",
 rubric="""100 points. Part 1: 20 points. Part 2: 20 points. Part 3: 20 points. Part 4: 15 points. Part 5: 20 points. Complete sentences and conventions: 5 points. A score of 70 or above is passing."""),
 disc=dict(t="Discussion 4: Prove All Things",
 prompt="""Write a post of at least 120 words that (1) describes a time when you saw or received false or suspicious information online, with no names, (2) explains in your own words how you decide whether a source can be trusted, (3) explains how a church or family can protect itself from online scams, and (4) connects your answer to 1 Thessalonians 5:21, Nehemiah 4:9, Proverbs 22:3 or Proverbs 12:22. Then write a respectful reply of at least 40 words to another student's post, or answer this question: How can a believer use AI tools without being dishonest? Keep your tone kind and respectful of other views."""),
 unit_quiz=[
 ("The internet differs from the web because the internet is:", ["The infrastructure the web runs on", "Only a browser", "Only email", "A search engine"], 0, "The web is one service on the internet."),
 ("A number that identifies a device on a network is an:", ["IP address", "Email subject", "Font", "Folder"], 0, "IP addresses route data."),
 ("A secure website address begins with:", ["HTTPS", "HTTP only", "FTP only", "None of these"], 0, "HTTPS encrypts traffic."),
 ("A router:", ["Directs traffic between devices and the internet", "Stores your photos only", "Blocks all sound", "Prints pages"], 0, "Routers direct network traffic."),
 ("Which is a sign of phishing?", ["An urgent request for your password from an unknown sender", "A letter you expected from your teacher", "A calendar reminder you set", "A song"], 0, "Urgent requests for passwords are warning signs."),
 ("Backups help defeat ransomware because:", ["You can restore files without paying", "They remove all viruses", "They speed up WiFi", "They stop updates"], 0, "A clean backup restores your data."),
 ("1 Thessalonians 5:21 tells us to:", ["Prove all things; hold fast that which is good", "Believe everything", "Avoid all learning", "Share rumors"], 0, "Test information before trusting it."),
 ("When using an AI tool for school, you should:", ["Check facts and follow your teacher's rules", "Enter your passwords", "Submit its work as your own", "Trust it without checking"], 0, "Verify and be honest."),
 ])
