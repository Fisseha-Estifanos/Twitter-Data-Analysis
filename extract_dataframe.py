import json
import pandas as pd
import numpy as np
from textblob import TextBlob
from defaults import *


def read_json(json_file: str) -> list:
    """
    json file reader to open and read json files into a list
    Args:
    -----
    json_file: str - path of a json file

    Returns
    -------
    length of the json file and a list of json
    """

    tweets_data = []
    for tweets in open(json_file, 'r'):
        tweets_data.append(json.loads(tweets))
    return len(tweets_data), tweets_data

class TweetDfExtractor:
    """
    this function will parse tweets json into a pandas dataframe
    
    Return
    ------
    dataframe
    """
    def __init__(self, tweets_list):
        """
        The initializer for the TweetDf Extractor class
        """
        self.tweets_list = tweets_list

    def find_statuses_count(self)->list:
        """
        an example function
        """
        statuses_count = [x['user']['statuses_count']
                          for x in self.tweets_list]
        return statuses_count

    def find_full_text(self)->list:
        """
        a function to find and return full text of a twit from a dataframe
        """
        text = []
        for x in self.tweets_list:
            try:
                text.append(x['full_text'])
            except KeyError:
                #text.append(x['text'])
                text.append('NA')
        return text

    def find_sentiments(self, text)->list:
        """
        a function to find and return polarity and subjectivity of a twit
        """ 
        polarity = [TextBlob(x).polarity for x in text]
        subjectivity = [TextBlob(x).subjectivity for x in text]
        return (polarity, subjectivity)

    def find_created_time(self)->list:
        """
        a function to find and return the date the twit was created at
        """
        created_at = [x['created_at'] for x in self.tweets_list]
        return created_at

    def find_source(self)->list:
        """
        a function to find and return the source of a tweet
        """
        source = [x['source'] for x in self.tweets_list]
        return source

    def find_screen_name(self)->list:
        """
        a function to find and return the screen name from where the
        tweet originated
        """
        screen_name = [x['user']['screen_name'] for x in self.tweets_list]
        return screen_name

    def find_followers_count(self)->list:
        """
        function to find and return the follower count of a twitter
        """
        followers_count = [x['user']['followers_count'] for x in
                           self.tweets_list]
        return followers_count

    def find_friends_count(self)->list:
        """
        function to find and return the friends count of a twitter
        """
        friends_count = [x['user']['friends_count'] for x in self.tweets_list]
        return  friends_count

    def is_sensitive(self)->list:
        """
        try:
            is_sensitive = [x['possibly_sensitive'] for x in self.tweets_list]
        except KeyError:
            is_sensitive = None
        return is_sensitive
        """
        # function to find and return the possible sensitivity of a tweet
        is_sensitive = []
        for tweet in self.tweets_list:
            if 'possibly_sensitive' in tweet.keys():
                is_sensitive.append(tweet['possibly_sensitive'])
            else:
                is_sensitive.append(None)
        return is_sensitive

    def find_favorite_count(self)->list:
        """
        function to find and return the favorite count of a tweet
        """
        favorite_count = []
        for tweet in self.tweets_list:
            if 'retweeted_status' in tweet.keys():
                favorite_count.append(
                                tweet['retweeted_status']['favorite_count'])
            else:
                favorite_count.append(0)
        return favorite_count
    
    def find_retweet_count(self)->list:
        """
        function to find and return the retweet count of a tweet
        """
        retweet_count = []
        for tweet in self.tweets_list:
            if 'retweeted_status' in tweet.keys():
                retweet_count.append(
                                tweet['retweeted_status']['retweet_count'])
            else:
                retweet_count.append(0)
        return retweet_count

    def find_hashtags(self)->list:
        """
        function to find and return the hashtags of a tweet
        """
        hashtags = [x['entities']['hashtags'] for x in self.tweets_list]
        return hashtags

    def find_mentions(self)->list:
        """
        function to find and return the mentions of a tweet
        """
        mentions = [x['entities']['user_mentions'] for x in self.tweets_list]
        return mentions

    def find_location(self)->list:
        """
        function to find and return the location of a tweet
        """
        location = [x.get('user', {}).get('location', None) for x in
                    self.tweets_list]
        return location

    def find_lang(self) -> list:
        """
        function to find and return the language of a tweet
        """
        lang = [x['lang'] for x in self.tweets_list]
        return lang
    
    # TODO : make this method
    def find_authors(self) -> list:
        """
        function to find and return authors of tweets
        """
        authors = []
        for x in range(22000):
            authors.append(x)
        return authors

    def get_tweet_df(self, save: bool=False, save_as : str = 'processed_tweet_data', as_csv : bool = False) -> pd.DataFrame:
        """
        required columns to be generated
        """
        # added_column_Names = ['status_count', 'screen_name']
        selected_columns = ['created_at', 'source', 'original_text','polarity',
                   'subjectivity', 'lang', 'favorite_count', 'status_count',
                   'retweet_count', 'screen_name', 'original_author',
                   'followers_count','friends_count','possibly_sensitive',
                   'hashtags', 'user_mentions', 'place']
       
        created_at = self.find_created_time()
        source = self.find_source()
        text = self.find_full_text()
        polarity, subjectivity = self.find_sentiments(text)
        lang = self.find_lang()
        fav_count = self.find_favorite_count()
        status_count = self.find_statuses_count()
        retweet_count = self.find_retweet_count()
        screen_name = self.find_screen_name()
        author = self.find_screen_name()      
        followers_count = self.find_followers_count()
        friends_count = self.find_friends_count()
        sensitivity = self.is_sensitive()
        hashtags = self.find_hashtags()
        mentions = self.find_mentions()
        location = self.find_location()

        selected_data = [created_at, source, text, polarity, subjectivity, lang, fav_count, status_count, retweet_count, screen_name, author, followers_count, friends_count, sensitivity, hashtags, mentions, location]

        sel_data = {}
        for i in range(0, len(selected_columns), 1):
            sel_data[selected_columns[i]] = selected_data[i]

        final_dataframe = pd.DataFrame(data = sel_data)

        """print({len(status_count)}, {len(created_at)}, {len(source)},
               {len(text)}, {len(polarity)}, {len(subjectivity)},
               {len(fav_count)}, {len(retweet_count)}, {len(screen_name)},
               {len(followers_count)}, {len(friends_count)},
               {len(sensitivity)}, {len(hashtags)}, {len(mentions)},
               {len(location)}, {len(lang)}, {len(author)})"""

        """print(status_count, created_at, source,
               text, polarity, subjectivity,
               fav_count, retweet_count, screen_name,
               followers_count, friends_count,
               sensitivity, hashtags, mentions,
               location, lang, author)"""

        """print({type(status_count)}, {type(created_at)}, {type(source)},
                {type(text)}, {type(polarity)}, {type(subjectivity)},
                {type(fav_count)}, {type(retweet_count)}, {type(screen_name)},
                {type(followers_count)}, {type(friends_count)},
                {type(sensitivity)}, {type(hashtags)}, {type(mentions)},
                {type(location)}, {type(lang)}, {type(author)})"""

        if save:
            if as_csv:
                data_path = 'data/' + save_as + '.csv'
                final_dataframe.to_csv(data_path, index=False)
                print(f'File {save_as} successfully saved as {data_path}')
            else:
                data_path = 'data/' + save_as + '.json'
                final_dataframe.to_json(data_path, indent=4)
                print(f'File {save_as} successfully saved as {data_path}')
        return final_dataframe


if __name__ == "__main__":
    # required column to be generated you should be creative and add more features
    columns = ['created_at', 'source', 'original_text','clean_text', 'sentiment','polarity','subjectivity', 'lang', 'favorite_count', 'retweet_count', 
    'original_author', 'screen_count', 'followers_count','friends_count','possibly_sensitive', 'hashtags', 'user_mentions', 'place', 'place_coord_boundaries']
    
    # for the global data set
    _, global_tweet_list = read_json(global_data)
     # to make sure all the data is passe to he
    print(f"Total number of data: {_}")
    global_tweet = TweetDfExtractor(global_tweet_list)
    global_tweet_df = global_tweet.get_tweet_df(save= True, save_as='processed_global_tweet_data')
    print(global_tweet_df)

    """# for the african data set
    _, african_tweet_list = read_json(african_data)
     # to make sure all the data is passe to he
    print(f"Total number of data: {_}")
    african_tweet = TweetDfExtractor(african_tweet_list)
    african_tweet_df = african_tweet.get_tweet_df(save = True, save_as='processed_african_tweet_data') 
    print(african_tweet_df)"""

    # TODO : use all defined functions to generate a dataframe with the specified columns above
