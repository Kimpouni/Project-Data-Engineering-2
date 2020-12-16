import unittest

try:
    from .model import get_tweet_similar, preprocessText
except ImportError:
    from model import get_tweet_similar, preprocessText


class TestClassifier(unittest.TestCase):
    
    def test_obama(self):
        self.assertRegex(
            get_tweet_similar('Obama')[0]['text'],
            'Obama')
        print("Testing Obama as a query \n")
        print("First result :"+get_tweet_similar('Obama')[0]['text']+"\n")


    def test_hillary(self):
        self.assertRegex(
            get_tweet_similar('Hillary')[0]['text'],
            'Hillary')
        print("Testing Hillary as a query \n")
        print("First result :"+get_tweet_similar('Hillary')[0]['text']+"\n")

 


if __name__ == '__main__':
    unittest.main()