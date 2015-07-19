import twitter
import json
import threading
import sys, os

lastID = 0

api = twitter.Api(consumer_key="C6f3rWK0UNotmJxdPea76SeBi",
	consumer_secret="2ZOxtXNiAuEDi9fipkPuX13PyZMk3Ng29HJ1O0wKmNUiuffWl9",
	access_token_key="188154178-DhxcvmWQoAUwckXYdsh1JIxkjKHTRGPZW8pxaTd6",
	access_token_secret="MWTc71f1A5DESsb3nQ9zg5RCmJXlv5U8sVO2HqAIBikgn")

# with open("lastTime.txt", "rb") as f:
# 	for line in f:
# 		lastSavedTime = int(line)
# 		print lastSavedTime

def searchTweets():
	global lastID
	search = api.GetSearch(term='#gamergate', count=20, since_id=lastID)

	if lastID == 0:
		for s in search:
			print s.id
			print '@' + s.user.screen_name + ": " + s.text
			text = s.text
			with open('twitterdata.txt', 'a') as f:
				f.write('@' + s.user.screen_name + ": ")
				f.write(text.encode('utf-8'))
				f.write('\n')
				f.write('----------')
				f.write('\n')

		lastID = search[len(search)-1].id
		print lastID

	else:
		for s in search:
			print '@' + s.user.screen_name + ": " + s.text
			text = s.text
			with open('twitterdata.txt', 'a') as f:
				f.write('@' + s.user.screen_name + ": ")
				f.write(text.encode('utf-8'))
				f.write('\n')
				f.write('----------')
				f.write('\n')
		lastID = search[len(search)-1].id
		print lastID

	startTimer(5.0)


def startTimer(time):

	print "starting timer..."
	t = threading.Timer(time, searchTweets)
	t.start()



searchTweets()