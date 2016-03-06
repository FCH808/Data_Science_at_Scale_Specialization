import sys
import json
#import pprint
#import re

#sent_file = open("AFINN-111.txt")
#tweet_file = open("problem_1_submission.txt")




def score_tweets(sent_text, tweets_txt):
    sent_index = 0
    sent_dict = {}
    sent_dict =  make_sent_dict(sent_text)

    for line in tweets_txt.readlines():
        #print ""
        current_tweet_sent = sent_text.readline()

        current_tweet_sent = float(current_tweet_sent)

        #print "current_tweet_sent:", current_tweet_sent
        sent_index += 1
        temp_json_line = json.loads(line)
        if "delete" in temp_json_line.keys():
            #print "None"
            continue
        #pprint.pprint(temp_json_line["text"])
        temp = temp_json_line["text"].lower().encode('utf-8').strip().replace(",", " ").replace(r".", "").replace(":", "").split()

        word_count = len(temp)
        #print "Length:", word_count
        #print "Index:", sent_index
        #print "Sentiment Score", sent_text[sent_index]
        for word in temp:
            if word in sent_dict.keys():
                sent_dict[word] += current_tweet_sent/word_count
            else:
                sent_dict[word] = current_tweet_sent/word_count
            #print word
            #print current_tweet_sent/word_count

    for pair in sent_dict.items():
        print pair[0], pair[1]


        # score = 0
        # for sent_entry in sent_dict.items():
        #     try:
        #         #print temp_json_line['text'].lower().encode('utf-8')
        #         if sent_entry[0].lower() in temp_json_line['text'].lower().encode('utf-8'):
        #             score += sent_entry[1]
        #     except KeyError as err:
        #         #print "No Text in this Tweet", err
        #         break
        #
        # print score



## The following line of code strips all characters that I don't want in the text string
# clean_text =  re.sub(ur'[^\s\w_]+', u'', tweet_text, flags=re.UNICODE)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    score_tweets(sent_file, tweet_file)

if __name__ == '__main__':
    main()