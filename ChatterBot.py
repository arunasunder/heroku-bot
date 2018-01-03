# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "gmNxN1oGO0x7hZ2S3aZleASHp"
consumer_secret = "KHZh1DlxV95aeOHWRvF4c4xNfBrVyk1Hg1hhMyZTP0hxIM8Nk0"
access_token = "106801026-nj9pKRBBbDBCfgC5LJIe0iLDfcCMTyaQ3pT7v0Vt"
access_token_secret = "TJG5kuuafGXG7GMAuHMoGx2ynMRUcr2A6SEgsg0hwvXvl"

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
