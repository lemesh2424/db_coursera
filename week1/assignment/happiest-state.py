import json
import re
import sys

states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}

def main():
    mood_score = open(sys.argv[1])
    mood_scores = {}
    for mood in mood_score:
        word_set, score = mood.split("\t")
        mood_scores[word_set] = int(score)

    tweets = open(sys.argv[2])
    states_mood = {}
    for tweet in tweets:
        tweet_data = json.loads(tweet)
        if "text" in tweet_data:
            tweet_data["text"].encode('ascii', 'replace')
            text = tweet_data["text"]
            text = text.rstrip("\n")
            splitted_text = re.split(r"[\s.,?:!\n]+", text)
            score_of_mood = 0

            for word in splitted_text:
                if word in mood_scores:
                    score_of_mood = score_of_mood + mood_scores[word]

            user = tweet_data["user"]
            location = user["location"]

            for state in states.keys():
                if state in location or states[state] in location:
                    if state in states_mood:
                        states_mood[state] += score_of_mood
                    else:
                        states_mood[state] = score_of_mood

    happiest = ''
    for state in states_mood.keys():
        if happiest == '':
            happiest = state
        if states_mood[state] > states_mood[happiest]:
            happiest = state

    print(happiest)


if __name__ == '__main__':
    main()