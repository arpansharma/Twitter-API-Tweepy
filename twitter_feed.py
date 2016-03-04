import tweepy

consumer_key = 'Your consumer key here'
consumer_secret = 'Your secret consumer key here'
access_token = 'Your access token here'
access_token_secret = 'Your secret access token here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
    print "\n"
