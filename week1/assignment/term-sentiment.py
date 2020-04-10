import sys
import json
import re


def main():
    mood_score = open(sys.argv[1])

    mood_scores = {}  # initialize an empty dictionary
    for line in mood_score:
        word_set, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        mood_scores[word_set] = int(score)  # Convert the score to an integer.

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

            for word in splitted_text:
                if word not in mood_scores:
                    print(word + " " + str(score_of_mood))


if __name__ == '__main__':
    main()