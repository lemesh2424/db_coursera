import json
import sys
from collections import Counter


def main():
    tweets = open(sys.argv[1])
    hashtags = {}
    for tweet in tweets:
        tweet_data = json.loads(tweet)
        if "entities" in tweet_data:
            entities = tweet_data["entities"]
            hastags_per_tweet = entities["hashtags"]

            for hashtag in hastags_per_tweet:
                text = hashtag["text"]
                if text in hashtags.keys():
                    hashtags[text] += 1
                else:
                    hashtags[text] = 1

    sorted_hashtags = Counter(hashtags)
    top10 = sorted_hashtags.most_common(10)
    for top in top10:
        print(top[0] + " " + str(top[1]))


if __name__ == '__main__':
    main()