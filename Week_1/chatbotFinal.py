import random

# variables containing txt arrays

file = open("stop-words.txt")
stopwords = file.readlines()
file2 = open("greetings.txt")
greet = file2.readlines()


# Removing stopwords from normal imput

def removeStopwords(message):
    for word in stopwords:
        next = word.strip()   s
        message = message.replace(" " + next + " ", " ")
    return message

#loop for chatbot interaction

while True:
    input = raw_input(">>>>>> ")
    filtered = removeStopwords(input)     #strips stopwords from imput, leaving everything else
    if greet in input :
        
        H= random.choice(file2)              #random response from list based of list
        print(H)
           
    else:
            print "I do not understand"     #prints if input doesn't match anything in lists