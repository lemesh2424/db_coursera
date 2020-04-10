import sys
import json
import re


def main():
    mood_score = open(sys.argv[1])

    mood_scores = {}
    for line in mood_score:
        word_set, score = line.split("\t")
        mood_scores[word_set] = int(score)

    tweets = open(sys.argv[2])
    for tweet in tweets:
        tweet_data = json.loads(tweet)
        if "text" in tweet_data:
            tweet_text = tweet_data["text"]
            splitted_text = re.split(r"[\s\.,\?\:]+", tweet_text)
            score_of_mood = 0

            for word in splitted_text:
                if word in mood_scores:
                    score_of_mood = score_of_mood + mood_scores[word]

            print(score_of_mood)


if __name__ == '__main__':
    main()