import json
import sys
import re


def main():
    tweets = open(sys.argv[1])
    words_count = 0
    words = {}
    for tweet in tweets:
        tweet_data = json.loads(tweet)
        if "text" in tweet_data:
            tweet_data["text"].encode('ascii', 'replace')
            text = tweet_data["text"]
            text = text.rstrip("\n")
            splitted_text = re.split(r"[\s.,?:!\n]+", text)

            words_count += len(splitted_text)

            for word in splitted_text:
                if word in words and word != '':
                    words[word] += 1
                elif word != '':
                    words[word] = 1

    for word in words.keys():
        print(word + " " + str(round(words[word] / words_count, 4)))


if __name__ == "__main__":
    main()