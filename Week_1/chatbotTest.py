import random
file = open("stop-words.txt")
stopwords = file.readlines()
f2 = ["It has been a long time.","It’s been too long.","What have you been up to all these years?","It’s always a pleasure to see you.","How long has it been?","What’s new?","What’s good?","What’s up?","Good to see you.",",How are things (with you)?","Hello","How are you?", "How’re you?","How are you doing?","How ya doin?","How’s it going?","Long time no see.","Hi"]





def removeStopwords(message):
    for word in stopwords:
        next = word.strip()
        message = message.replace(" " + next + " ", " ")
    return message


while True:
    input = raw_input(">>>>>> ")
    filtered = removeStopwords(input)
    if input in greet:
        H= random.choice(file)
        print(H)
           
        
    else:
            print "I do not understand" 