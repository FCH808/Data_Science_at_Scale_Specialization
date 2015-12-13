import sys
import json
from tweet_sentiment import score_tweet, build_dict

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


def find_happiest_state(sentiment_file, tweet_file):

    sentiment_dict = build_dict(sentiment_file)

    state_sentiment = {}

    with open(tweet_file, 'r') as tweets:

        for tweet in tweets:

            tweet = json.loads(tweet)

            # Coursera grader raises KeyError, wrap in try/except block
            try:
                if tweet['place'] != None:
                    if tweet['place']['country'] == 'United States':
                        tweet_state = tweet['place']['full_name'].split()[-1]
                        if tweet_state in states.keys():
                            # print tweet_state
                            # print tweet['text']
                            current_score = score_tweet(tweet['text'], sentiment_dict)

                            # First item is the running count, second is the avg score
                            old_count_and_score = state_sentiment.get(tweet_state, [0, 0])
                            weighted_old_score = old_count_and_score[0]*old_count_and_score[1]

                            updated_count = old_count_and_score[0] + 1

                            updated_score = (weighted_old_score + current_score) / updated_count

                            state_sentiment[tweet_state] = [updated_count, updated_score]
            except KeyError as e:
                pass


        # Sort by score (second number in the list of values)
        sorted_states =  sorted(state_sentiment.iteritems(),
                                key=lambda (k,v): (v[1], k),
                                reverse=True)

        # Print out the score of the first entry.
        # Use an OrderedDict next time. ;)
        print sorted_states[1][0]

def main():

    sentiment_file = sys.argv[1]
    tweet_file = sys.argv[2]
    # sentiment_file = 'AFINN-111.txt'
    #
    # tweet_file = 'output_big.txt'
    # tweet_file = 'test.txt'

    find_happiest_state(sentiment_file, tweet_file)

if __name__ == '__main__':
    main()