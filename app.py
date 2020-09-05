from tweepy import OAuthHandler
from tweepy import API
import config


auth = OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token,config.access_token_secret)
auth_api = API(auth)

#Add the user Id you want to get tweets 
user_id="realDonaldTrump"
#Add the number of tweets you want to get 
number_of_tweets= 20
#count: maximum allowed tweets count
#tweet_mode: extended to get the full text,it prevents a primary tweet longer than 140 characters from being truncated.
timeline = auth_api.user_timeline(user_id=user_id, count=number_of_tweets,tweet_mode="extended")
# Iterate and print tweets
textonly_tweets = [tweet.full_text for tweet in timeline]
print(*textonly_tweets, sep = "\n")
    



