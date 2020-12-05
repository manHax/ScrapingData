import json
import csv
import tweepy
import re

def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):
    
    #create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #initialize Tweepy API
    api = tweepy.API(auth)
    
    #get the name of the spreadsheet we will write to
    fname = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))

    #open the spreadsheet we will write to
    with open('%s.csv' % (hashtag_phrase), 'w') as file:

        w = csv.writer(file)

        #write header row to spreadsheet
        w.writerow(['tweet_text'])
        #for each tweet matching our hashtags, write relevant info to the spreadsheet
        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', \
                                   lang="id", tweet_mode='extended').items(12):
            w.writerow([tweet.full_text.replace('\n',' ').encode('utf-8')])



if __name__ == '__main__':
    default_API = input("Use Your custom API? (y/n)")

    if (default_API=="y"):
        consumer_key = input('Consumer Key ')
        consumer_secret = input('Consumer Secret ')
        access_token = input('Access Token ')
        access_token_secret = input('Access Token Secret ')
        hashtag_phrase = input('Hashtag Phrase ')
    else:
        consumer_key = 'qwyIsgJIre1XJW7ziHpkg9T2E'
        consumer_secret = 'SbLbfddTx8zttvFSdZ5jawln6ph63IdsGyTwL8ssaefQKzo9Hs'
        access_token = '1346389309-6mQ8rMWRbRvsU1RguqFI5VgWMR0b2AnR7MDaxAb'
        access_token_secret = 'nqy5jp78PGXngTySe1ETqjsXntYJ2jm3LQ4G4wjxrqo6l'
        hashtag_phrase = input('Hashtag Phrase ')

    search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)
