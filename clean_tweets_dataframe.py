import re
import pandas as pd
from defaults import *

class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')
        
    def drop_unwanted_column(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        unwanted_rows = self.df[self.df['retweet_count'] == 'retweet_count' ].index
        self.df.drop(unwanted_rows , inplace=True)
        self.df = self.df[self.df['polarity'] != 'polarity']
        return df

    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        """
        self.df.drop_duplicates(subset='original_text', inplace=True)
        return df

    def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        """
        self.df['created_at'] = pd.to_datetime(self.df['created_at'], errors='coerce')
        return df
    
    def convert_to_numbers(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        self.df['id'] = pd.to_numeric(self.df['id'], errors='coerce')
        self.df['subjectivity'] = pd.to_numeric(self.df['subjectivity'],
                                                errors='coerce')
        self.df['listed_count'] = pd.to_numeric(self.df['listed_count'],
                                                errors='coerce')
        self.df['retweet_count'] = pd.to_numeric(self.df['retweet_count'],
                                                 errors='coerce')
        self.df['friends_count'] = pd.to_numeric(self.df['friends_count'],
                                                 errors='coerce')
        self.df['favorite_count'] = pd.to_numeric(self.df['favorite_count'],
                                                  errors='coerce')
        self.df['statuses_count'] = pd.to_numeric(self.df['statuses_count'],
                                                  errors='coerce')
        self.df['followers_count'] = pd.to_numeric(self.df['followers_count'],
                                                   errors='coerce')
        self.df['polarity'] = pd.to_numeric(self.df['polarity'],
                                            errors='coerce')
        return df
    
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        """
        self.df.query("lang == 'en'", inplace=True)
        return df

    def drop_nulls(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        drop nulls
        """
        self.df = self.df.dropna(axis=0, how='any', inplace=False)
        return df

    def find_hashtags(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Method to find hashtags from tweets
        This function will extract hashtags
        """
        self.df = re.findall('(#[A-Za-z]+[A-Za-z0-9-_]+)', df) 
        return df

    def text_category(self, series: pd.Series) -> list:
        """
        function that return positive, negative or neutral based on polarity
        """
        polarities = []
        for pol in series:
            if pol >= 0.00000000001:
                polarities.append("positive")
            elif pol == 0.00000000000:
                polarities.append("neutral")
            elif pol <= -0.00000000001:
                polarities.append("negative")
            else:
                polarities.append('UNK')
        return polarities
    
    def fill_missing(self, df: pd.DataFrame, column: str, value):
        """
        fill null values of a specific column with the provided value
        """

        df[column] = df[column].fillna(value)

        return df

    def replace_empty_string(self, df:pd.DataFrame, column: str, value: str):
        """
        replace empty strings in a specific column with the provided value
        """

        df[column] = df[column].apply(lambda x: value if x == "" else x)

        return df

    def remove_characters(self, df: pd.DataFrame, column: str):
        """
        removes non-alphanumeric characters with the exception of underscore hyphen and space
        from the specified column
        """

        df[column] = df[column].apply(lambda text: re.sub("[^a-zA-Z0-9\s_-]", "", text))

        return df

    def extract_device_name(self, source: str):
        """
        returns device name from source text
        """
        res = re.split('<|>', source)[2].strip()
        return 

if __name__ == "__main__":
    """
    read the twitter dataset and Pass the data to the Clean_Tweets
    class
    """
    global_tweet_df = pd.read_json(global_data, lines=True)
    global_cleaner = Clean_Tweets(global_tweet_df)
    
    african_tweet_df = pd.read_json(african_data, lines=True)
    african_cleaner = Clean_Tweets(african_tweet_df)
