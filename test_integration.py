import json
import unittest
import app

try:
    from .model import get_tweet_similar, preprocessText
except ImportError:
    from model import get_tweet_similar, preprocessText



class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def get_similar_tweets(self, text: str):
        return self.app.post('similar_tweets', headers={'Content-Type' 'applicationjson'}, data=json.dumps({'text' :text})).json

    def test_amount_tweets(self):
        self.assertEqual(len(self.get_similar_tweets('test')), 20)
        self.assertEqual(len(self.get_similar_tweets('this is a very long sentence for the test')), 20)

    def test_tweet_format(self):
        tweet = self.get_similar_tweets('test')[0]
        self.assertEqual(type(tweet['text']), str)
        self.assertEqual(type(tweet['link']), str)
        self.assertEqual(type(tweet['author']), str)


if __name__ == '__main__':
    unittest.main()