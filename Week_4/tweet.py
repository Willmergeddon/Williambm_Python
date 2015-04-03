import twitter, datetime

#variables
#accesses twitter crentials and splits up keys and secrets

file = open("TwitterCredentials.txt")
cred = file.readline().strip().split(',')
sesh = open("Users/Will/Library/Application Support/Google/Chrome/Default/Current Session" )
lastSesh = sesh.read
api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],
		  access_token_key=cred[2],access_token_secret=cred[3])

print(api)
