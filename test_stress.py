import unittest
import time

try:
    from .model import get_tweet_similar, preprocessText, load_model
except ImportError:
    from model import get_tweet_similar, preprocessText, load_model


class TestClassifier(unittest.TestCase):

	
    
    #stress test 1000 queries
	def test_f_stress_test(self):
		model =load_model()
		start=time.time()
		for i in range(1000):
			get_tweet_similar('test')
		end=time.time()
		print(end-start)
		self.assertGreater(60 , end-start)


 


if __name__ == '__main__':
    unittest.main()