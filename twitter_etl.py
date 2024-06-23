import pandas as pd
from ntscraper import Nitter
import json
from datetime import datetime
import s3fs

def get_tweets(username, count):
    scraper = Nitter()
    try:
        tweets = scraper.get_tweets(username, mode='user', number=count)
        if 'tweets' in tweets:
            tweet_list = []
            for tweet in tweets['tweets']:
                data = [
                    tweet['user']['name'],
                    tweet['link'],
                    tweet['text'],
                    tweet['date'],
                    tweet['stats']['likes'],
                    tweet['stats']['comments'],
                    tweet['stats']['retweets']
                ]
                tweet_list.append(data)
            return tweet_list
        else:
            print(f"No tweets found for {username}")
            return []
    except Exception as e:
        print(f"An error occured while fetching tweets for {username}")
        return []

def run_twitter_etl():
    users = ['imVKohli', 'elonmusk', 'VancityReynolds']
    all_tweets = []

    for user in users:
        all_tweets += get_tweets(user, 200);

    df = pd.DataFrame(all_tweets, columns=['user', 'link', 'text', 'created_at', '#likes', '#comments', '#retweets'])

    df.to_csv("s3://twitter-airflow-etl-bucket/tweets_data.csv", index=False)

