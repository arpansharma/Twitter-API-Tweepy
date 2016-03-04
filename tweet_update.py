import tweepy

CONSUMER_KEY = 'Your consumer key here'
CONSUMER_SECRET = 'Your secret consumer key here'
ACCESS_TOKEN = 'Your access token here'
ACCESS_TOKEN_SECRET = 'Your secret access token here'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

status = "Testing Twitter API :)"
api.update_status(status=status)
