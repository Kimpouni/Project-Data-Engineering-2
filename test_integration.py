import json
import unittest
import app

import unittest
import os 
import requests

try:
    from .model import get_tweet_similar, preprocessText
except ImportError:
    from model import get_tweet_similar, preprocessText



class MyTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['NO_PROXY']='0.0.0.0'
        pass

    def test_interface(self):
        response = requests.get('http://localhost:5000')
        self.assertEqual(response.status_code,200)


    def test_amount_tweets(self):
        self.assertEqual(len(get_tweet_similar('testing with a long sentence, like a very very long sentence')), 20)


    def test_tweet_format(self):
        tweet = get_tweet_similar('test')[0]
        self.assertEqual(type(tweet['date']), str)
        self.assertEqual(type(tweet['text']), str)
        self.assertEqual(type(tweet['link']), str)
        self.assertEqual(type(tweet['author']), str)
        self.assertEqual(type(tweet['confidence']), float)


if __name__ == '__main__':
    unittest.main()