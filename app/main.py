import tweepy

from authorization_tokens import *

# import random

# import pronouncing





consumer_key = api_key
consumer_secret = api_key_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


with open("already_tweeted.txt", 'r') as f:
    already_tweeted = [x.rstrip() for x in f]

about_tweets_list = ["arabic poetry", "arabic poems", "poetic lines", "poems" "sufi poetry"]
for term in about_tweets_list:
    search_results = api.search(q =f"{term}", lang = "en", tweet_mode="extended")

    for message in search_results:
        if hasattr(message, "retweeted_status"):
            tweet = message.retweeted_status.full_text
        else:
            tweet = message.full_text

        tweet = tweet + "by" + message.user.screen_name


        if "https:" in tweet:
            tweet = " ".join([i for i in tweet.split() if 'https:' not in i])

        if message.id not in already_tweeted:
            try:
                #api.update_status(tweet)
                print(message.id + ": " + tweet)
                already_tweeted.append(message.id)
            except:
                pass
        else:
            pass

with open("already_tweeted.txt", 'w+') as f:
    old_tweets = [x.rstrip() for x in f]
    f.write("\n")
    for i in already_tweeted:
        if i not in old_tweets:
            f.write(i + "\n")




print("Done.")
