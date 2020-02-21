# Importing module 
import pandas as pd 
import os
import matplotlib.pyplot as plt

# Reading data into python
path = './papers.csv'
papers = pd.read_csv(path)

# Droping colunms that don't add value to our dataset
print('All the colunms that make the dataset: \n',papers.columns)

papers = papers.drop(['id','event_type','pdf_name'],axis=1)

print('The new colunms in the dataset: \n',papers.columns)

############## Preprocessing #################
# Removing Punctutation/lower case
'''
Removing punchuation makes and  make sure all the sentencess are in lower care
'''
# Importing the regular expressing library
import re

#removing punctuation
papers['paper_text'] = papers['paper_text'].map(lambda x:re.sub('[,\.!?]', '', x))

#Coveting to lowercase
papers['paper_text'] = papers['paper_text'].map(lambda x: x.lower())

# Printing sample preprocessed data 
papers['paper_text'].head()

############ Exploratory Analysis ##############
# importing the word cloud library
from wordcloud import WordCloud

#Joining the diffrent  processed titles together
long_string = ','.join(list(papers['paper_text'].values))

#creating a wordcloud object
wc_obj = WordCloud(background_color='white',max_words=5000,contour_width=3,contour_color='rainbow',
                   width=600,height=400)

#generating a wordcloud
wc_obj.generate(long_string)

#visualizing the word cound
wc_obj.to_image()
plt.show()

############## prepare text for LDA analysis  ##########
'''
Transforming the textual data in a format that will serve as an input for training LDA
step 1: Convert the document into a simple vector representation (Bag of Words BOW)
step 2: Convert the list of titles into list of vectors all with equal length to the vocabulary
'''
#Importing library with countvectorizer method
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import seaborn as sbn

# Function
def plot_10_most_common_words(count_data,count_vectorizer):
    words = count_vectorizer.get_feature_names()
    total_counts=np.zeros(len(words))
    for t in count_data:
        total_counts+=t.toarray()[0]
        
    count_dict = (zip(words,total_counts))
    count_dict=sorted(count_dict,key=lambda x:x[1],reverse=True)[0:10]
    words = [w[0] for w in count_dict]
    counts=[w[1] for w in count_dict]
    x_pos = np.arange(len(words))
    
    plt.figure(2,figsize=(15,15/1.6180))
    plt.subplot(title='10 Most common words')
    sbn.set_context('notebook',font_scale=1.25,rc={'lines.linewidth':2.5})
    sbn.barplot(x_pos,counts,palette='husl')
    plt.xticks(x_pos,words,rotation=90)
    plt.xlabel('Words')
    plt.ylabel('counts')
    plt.show()

# Initialise the count vectorizer with english stop word
c_v=CountVectorizer(stop_words='english')

#Fitting and Transforn the the processed title
c_d=c_v.fit_transform(papers['paper_text'])

# Visualise the 10 most common words
plot_10_most_common_words(count_data=c_d,count_vectorizer=c_v)


# LDA model trainig and results visualization
import warnings
warnings.simplefilter('ignore',DeprecationWarning)

#Loading LDA model for sklearn
from sklearn.decomposition import LatentDirichletAllocation as LDA

def print_topics(model,count_vectorizer,n_top_words):
    words=count_vectorizer.get_feature_names()
    for topic_idx, topic in enumerate(model.components_):
        print('\n Topic #%d: '% topic_idx)
        print(''.join([words[i] for i in topic.argsort()[:-n_top_words -1:-1]]))
# Tweak the two parameters below
number_topics = 5
number_words = 10

# Create and Fit the LDA model
lda = LDA(n_components=number_topics,n_jobs=-1)
lda.fit(count_data)

# Print the topics fount by the LDA Model
print('Topics Found via LDA: ')
print(lda,count_vectorizer,number_words)
print(CountVectorizer)