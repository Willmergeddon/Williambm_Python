import random
file = open("stop-words.txt")
stopwords = file.readlines()
#file2 = open("greetings.txt")
#greet = file2.readlines().len()

#H= random.choice(file2)



def removeStopwords(message):
    for word in stopwords:
        next = word.strip()
        message = message.replace(" " + next + " ", " ")
    return message


while True:
    input = raw_input(">>>>>> ")
    filtered = removeStopwords(input)
    print("your filtered word it:" + input)
