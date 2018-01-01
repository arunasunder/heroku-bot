# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "9kkN1jMQXQaLDjiS5V5gowvvj"
consumer_secret = "McWZRtCItskC8NOXmAQfhyfDsVAxvPSy8rC9veyd4EHYenMDyh"
access_token = "942922975849926656-fEMaRVfEs4SjRDw6aZ5nhCxyex0J0Ou"
access_token_secret = "qyxZGGu1IWBdkdd5P17B6Rjn71XRpX3NoBK8hXJJQllUW"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(
        "Can't stop. Won't stop. Chatting! This is Tweet #%s!" %
        tweet_number)


# Create a function that calls the TweetOut function every minute
counter = 0

# Infinitely loop
while(True):

    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)

    # Once tweeted, wait 60 seconds before doing anything else
    time.sleep(60)

    # Add 1 to the counter prior to re-running the loop
    counter = counter + 1
