from markov_twitter import get_api
api = get_api()

tweets = api.GetUserTimeline(screen_name='KarlTheFog', count=200)

bad_char = u'\u2026'
tweets_text = [tweet.text.encode('utf-8') for tweet in tweets]
# for tweet in tweets_text:
#     if bad_char in tweet:
#         tweets_text.remove(tweet)
#     else:
        # print tweet
print "\n".join(tweets_text)