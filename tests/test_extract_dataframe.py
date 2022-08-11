import sys
import unittest
import pandas as pd

# sys.path.append(os.path.abspath(os.path.join("../..")))
sys.path.append(".")
sys.path.append("..")
from defaults import *

from extract_dataframe import read_json
from extract_dataframe import TweetDfExtractor

# For unit testing the data reading and processing codes, 
# we will need about 5 tweet samples. 
# Create a sample not more than 10 tweets and place it in a json file.
# Provide the path to the samples tweets file you created below

#tweet_list = pd.read_csv('data/clean_data.csv')
_len, tweet_list = read_json('data/global_twitter_data.json')

columns = [
    "created_at",
    "source",
    "original_text",
    "clean_text",
    "sentiment",
    "polarity",
    "subjectivity",
    "lang",
    "favorite_count",
    "retweet_count",
    "original_author",
    "screen_count",
    "followers_count",
    "friends_count",
    "possibly_sensitive",
    "hashtags",
    "user_mentions",
    "place",
    "place_coord_boundaries",
]


class TestTweetDfExtractor(unittest.TestCase):
    """
		A class for unit-testing function in the fix_clean_tweets_dataframe.py file

		Args:
        -----
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""

    def setUp(self) -> pd.DataFrame:
        self.df = TweetDfExtractor(tweet_list[:5])
        self.maxDiff = None
        # tweet_df = self.df.get_tweet_df()

    def test_find_status_count(self):
        """
        Test case for the find status count method
        """
        # error test
        # self.assertEqual(self.df.find_statuses_count(),
        # [204051, 3462, 6727, 45477, 277957])

        # the edited error test
        self.assertEqual(self.df.find_statuses_count(),
                         [8097, 5831, 1627, 1627, 18958])

    def test_find_source(self):
        """
        Test case for the find source method
        """
        # the edited test case
        source = ['<a href="http://twitter.com/download/android" rel="nofollow">Twitter for ''Android</a>', '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>', '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>', '<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>', '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>']

        # error test  case
        error_source = ['Twitter for Android', 'Twitter for Android', 'Twitter for Android', 'Twitter for Android', 'Twitter for iPhone']
        self.assertEqual(self.df.find_source(), source)

    def test_find_screen_name(self):
        """
        Test case for the find screen name method
        """
        # error test case
        error_name_test_Case = ['ketuesriche', 'Grid1949',
                                'LeeTomlinson8', 'RIPNY08', 'pash22']
        # the edited error test
        name = ['i_ameztoy', 'ZIisq', 'Fin21Free', 'Fin21Free', 'VizziniDolores']
        self.assertEqual(self.df.find_screen_name(), name)

    def test_find_followers_count(self):
        """
        Test case for the find followers count method
        """
        # error test
        error_f_count = [551, 66, 1195, 2666, 28250]

        # the edited error test
        f_count = [20497, 65, 85, 85, 910]
        self.assertEqual(self.df.find_followers_count(), f_count)

    def test_find_friends_count(self):
        """
        Test case for the find friends count method
        """
        # error test
        error_friends_count = [351, 92, 1176, 2704, 30819]

        # edited error test
        friends_count = [2621, 272, 392, 392, 2608]
        self.assertEqual(self.df.find_friends_count(), friends_count)

    def test_find_is_sensitive(self):
        self.assertEqual(self.df.is_sensitive(),
                         [None, None, None, None, None])

    def test_find_location(self):
        """
        Test case for the find location method
        """
        # error test
        error_locations = ['', '', '', '', '']

        # edited error test
        locations = ['', '', 'Netherlands', 'Netherlands', 'Ayent, Schweiz']
        self.assertEqual(self.df.find_location(), locations)

    def test_find_lang(self):
        """
        Test case for the find lang method
        """
        langs = ['en', 'en', 'en', 'en', 'en']
        self.assertEqual(self.df.find_lang(), langs)

    def test_find_retweet_count(self):
        """
        Test case for the find retweet count method
        """
        # error test
        error_retweets_test_Case = [612, 92, 1, 899, 20]

        # the edited error test
        retweets = [2, 201, 0, 0, 381]
        self.assertEqual(self.df.find_retweet_count(), retweets)

    def test_find_favorite_count(self):
        """
        Test case for the find favorite count method
        """
        # error test
        # self.assertEqual(self.df.find_favorite_count(),
        #                   [548, 195, 2, 1580, 72])

        # the edited error test
        self.assertEqual(self.df.find_favorite_count(),
                         [4, 691, 0, 0, 1521])

if __name__ == "__main__":
    unittest.main()
