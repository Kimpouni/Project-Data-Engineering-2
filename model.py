import multiprocessing
import re
from os import path
import pandas as pd
from gensim.models.doc2vec import TaggedDocument, Doc2Vec
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import re
from nltk.corpus import stopwords
from nltk.corpus import words
import string
import unidecode
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer 
tk = TweetTokenizer() 
  
lemmatizer = WordNetLemmatizer() 


# IMPORT DATA
data = pd.read_csv( 'data/tweets.csv')

# Drop duplicates
data = data.drop_duplicates(subset=['id'])

data = data.reset_index().drop(columns=['index', 'id', 'Unnamed: 0'])
data.head()

#init
ps = PorterStemmer()

def preprocessText(corpus):
    
    # Lower
    corpus = corpus.lower()

    # Remove pictures
    regex = r'pic\.twitter\.com.*'
    corpus.replace('\n','').strip()
    corpus.replace(u'\u2018',"'").replace(u'\u2019',"'")
    corpus= re.sub("https*\S+", " ", corpus)
    
    corpus = re.sub(regex, '', corpus, 0, re.MULTILINE)
    corpus = re.sub(r'[^\w\s]', '', (corpus))
    preprocessed = list()
    stopset = stopwords.words('english') + list(string.punctuation)
    
    # remove stop words and punctuations from string.
    # word_tokenize is used to tokenize the input corpus in word tokens.
    corpus = " ".join([i for i in word_tokenize(corpus) if i not in stopset])
    tok_doc = word_tokenize("".join(corpus))    
    stemmed_doc = [ps.stem(word) for word in tok_doc]
    lemma = [lemmatizer.lemmatize(word) for word in stemmed_doc]
    preprocessed.append(" ".join(lemma))
    
    return preprocessed

def preprocessList(listText):
    preprocessed = list()
    for text in listText:
        preprocList = preprocessText(text)
        preprocessed.append(preprocList)
    return preprocessed

def get_tweet_similar(user_text):
    model = Doc2Vec.load("model")
    tokens = tk.tokenize(preprocessText(user_text)[0])
    vector = model.infer_vector(tokens)
    

    result = []
    for tweet_id, confidence in model.docvecs.most_similar([vector], topn=20):
        tweet = data.iloc[tweet_id].to_dict()
        result.append({**tweet, 'confidence': confidence, 'retweet': bool(tweet['retweet'])})

    return result

def main():
    # get tokens
    preprocessed = []
    data.loc[:, 'tokens'] = preprocessList(data.text)
    

    sentences = []
    for ind in data.index:
        tweet_tokens = tk.tokenize(data['tokens'][ind])
        sentences.append(TaggedDocument(tweet_tokens, [ind]))

   

    #MODEL
    model = Doc2Vec(
        documents=sentences,
        min_count=1,  
        max_vocab_size=None,
        window=50,  # the # of words before and after to be used as context
        size=300,  # is the dimensionality of the feature vector
        workers=multiprocessing.cpu_count(),
        iter=200  # number of iterations (epochs) over the corpus)
    )

    model.save("model")






    