import json
import sys

def find_top_ten(tweet_file):

    hashtag_counts = {}

    with open(tweet_file, 'r') as tweets:

        for tweet in tweets:

            tweet = json.loads(tweet)

            for hashtags in tweet['entities']['hashtags']:
                hashtag =  hashtags['text']
                hashtag_counts[hashtag] = hashtag_counts.get(hashtag, 0) + 1

    sorted_hashtags = sorted(hashtag_counts,
                             key=hashtag_counts.get,
                             reverse=True)
    for key in sorted_hashtags[:10]:
        print key, hashtag_counts[key]

def main():

    tweet_file = sys.argv[1]

    # tweet_file = 'output_big.txt'
    # tweet_file = 'problem_1_submission.txt'

    find_top_ten(tweet_file)

if __name__ == '__main__':
    main()