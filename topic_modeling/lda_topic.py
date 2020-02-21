import pandas as pd

# Importing and dataset selection
file_path = '/home/danielkmalungu/Documents/Project Startup/topic_modeling/million-headlines/abcnews-date-text.csv'
data = pd.read_csv(file_path,error_bad_lines=False)
data_text = data[['headline_text']]
data_text['index'] = data.index
documents = data_text

print(documents.head(5))

# Data Pre-processing
'''
the following are the activities Topic Modeling:
    1.Tokenization: Split the text into sentences and the sentences into words. Lowercase the words and remove punctuation.
    2.Words that have fewer than 3 characters are removed.
    3.All stopwords are removed.
    4.Words are lemmatized — words in third person are changed to first person and verbs in past and future tenses are changed into present.
    5.Words are stemmed — words are reduced to their root form.
'''
# Lording libraries
import gensim
from gensim.parsing.preprocessing import STOPWORDS
from gensim.utils import simple_preprocess
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import numpy as np 
np.random.seed(2020)
import nltk
nltk.download('wordnet')

#Function to perform lemmatize and stem
stemmer = PorterStemmer()
def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text,pos='v'))

def preprocess(text):
    result=[]
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result

# Preview documents after preprocessing
doc_sample =documents[documents['index']==4310].values[0][0]

print('original document: ')
words = []
for word in doc_sample.split(' '):
    words.append(word)

print(words)
print('\n\n tokenized and lemmatized document: ')
print(preprocess(doc_sample))

# Preprocessing headlines and saving the results
processed_doc = documents['headline_text'].map(preprocess)
print(processed_doc[:10])

# Bag of Words
# Creating a bag of words it contains a word and the frequency of that word
dictonary=gensim.corpora.Dictionary(processed_doc)
count = 0
for x,y in dictonary.iteritems():
    print(x,y)
    count += 1
    if count > 10:
        break

#Filtering words that don't fit the following requirements:
'''
1. less than 15 documents (absolute number)
2. more than 0.5 documents (fraction of total corpus size, not absolute number).
3. after the above two steps, keep only the first 100000 most frequent tokens.
'''
dictonary.filter_extremes(no_below=15, no_above=0.5,keep_n=100000)

#Gensim doc2bow
'''
For each document we create a dictionary reporting how manywords and how many times those words appear. 
Save this to ‘bow_corpus’, then check our selected document earlier.
'''

bow_do _4310 =bow_corpus[4310]
for i in range()