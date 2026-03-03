ham_words=0
ham_messages=0
spam_words=0
spam_messages=0
spam_exclamation=0

file = open("SMSSpamCollection.txt", encoding="utf-8")

for line in file:
    line = line.strip()
    if not line:
        continue

    typ, text = line.split("\t", 1)
    words = text.split()

    if typ == "ham":
        ham_messages += 1
        ham_words += len(words)

    elif typ == "spam":
        spam_messages += 1
        spam_words += len(words)
        if text.endswith("!"):
            spam_exclamation += 1


average_ham=ham_words/ham_messages
average_spam=spam_words/spam_messages
print ("Average number of words in ham:",average_ham)
print ("Average number of words in spam:",average_spam)
print("Number of spam messages ending with '!':", spam_exclamation)