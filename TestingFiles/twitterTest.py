import tweepy
import twitter_credentials as tc
import json
auth = tweepy.OAuthHandler(tc.CONSUMER_KEY, tc.CONSUMER_SECRET)
auth.set_access_token(tc.ACCESS_TOKEN, tc.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

slug = 'Senators'
owner = 'CSPAN'

def get_userinfo(name):
	# get all user data via a Tweepy API call
	user = api.get_user(screen_name = name)
	# create row data as a list
	'''
	user_info = [ name,
				user.name,
				user.description,
				user.followers_count,
				user.friends_count,
				user.created_at,
				user.location ]
	'''
	user_info = {
		'name': name,
		'userName': user.name,
		'Description': user.description,
		'followersCount': user.followers_count,
		'friendsCount':user.friends_count,
		'CreatedAt':user.created_at,
		'Location':user.location

	}
	# send that one row back
	return user_info

def get_all_tweet(name):
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print ("getting tweets before %s" % (oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print ("...%s tweets downloaded so far" % (len(alltweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = {name: [{'time': tweet.created_at, 'text': tweet.text} for tweet in alltweets]}
	return outtweets

# Main
if __name__ == '__main__':
    members = []
        # without this you only get the first 20 list members
    for page in tweepy.Cursor(api.list_members, owner, slug).items():
        members.append(page)
    memberlist = [ m.screen_name for m in members ]
    '''
    for name in memberlist:
        print(get_userinfo(name)["name"])
    '''
    print(get_all_tweet(memberlist[0]))
    output = {}
    for member in memberlist:
        output[member] = get_all_tweet(member)[member]
    with open('twitTest.json', 'w') as outfile:
        json.dump(output, outfile, default=str)
    #print(members)
