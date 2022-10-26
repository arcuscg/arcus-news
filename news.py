#!/usr/bin/env python3

import os
import tweepy

client = tweepy.Client(
    consumer_key=os.getenv["CONSUMER_KEY"],
    consumer_secret=os.getenv["CONSUMER_SECRET"],
    access_token=os.getenv["ACCESS_TOKEN"],
    access_token_secret=os.getenv["ACCESS_TOKEN_SECRET"],
)

topics = [
    "#infosec",
    "#cybersecurity",
    "#cve"
]

for single_topic in topics:
    selected = client.search_recent_tweets("#cybersecurity",max_results=100,tweet_fields="public_metrics", user_auth=True)
    print(f"Displaying tweets for {single_topic}\n---")
    for tweet in selected[0]:
        print(tweet.id, tweet.public_metrics)