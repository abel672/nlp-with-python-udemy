# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd


# %%
npr = pd.read_csv('npr.csv')


# %%
npr.head()


# %%
len(npr['Article'])


# %%
npr['Article'][4000]


# %%
from sklearn.feature_extraction.text import CountVectorizer


# %%
cv = CountVectorizer(
    max_df=0.9, # document frequency: very common terms along the documents
    min_df=2, # Minimal document frequency for a word in this count vectorizer has to be 2 documents
    # the terms has to be minimal in 2 documents to be detected in this count vector
    stop_words='english' # remove english stop words (a, the, for, ...)
)


# %%
dtm = cv.fit_transform(npr['Article']) # turning data frame into a sparse matrix document


# %%
dtm # document x word


# %%
from sklearn.decomposition import LatentDirichletAllocation


# %%
LDA = LatentDirichletAllocation(n_components=7, random_state=42)


# %%
LDA.fit(dtm) # LDA model


# %%
# Grab the vocabulary of words


# %%
len(cv.get_feature_names())


# %%
type(cv.get_feature_names())


# %%
import random

random_word_id = random.randint(0, 54777)

cv.get_feature_names()[random_word_id]


# %%
# Grab the topics


# %%
len(LDA.components_)


# %%
type(LDA.components_)


# %%
LDA.components_.shape #(topics, words)


# %%
LDA.components_ # all the topics and words


# %%
single_topic = LDA.components_[0] # grabing one topic


# %%
single_topic.argsort() # indexes from lowest to highest value

# %% [markdown]
# ### Example

# %%
import numpy as np


# %%
arr = np.array([10, 200, 1])


# %%
arr


# %%
arr.argsort() # indexes from lowest to hieghest value


# %%
# ARGSORT ---> INDEX POSITIONS SORTED FROM LEAST ---> GREATEST
# TOP 10 VALUES
single_topic.argsort()[-10:] # last 10 values of .argsort()


# %%
top_twenty_words = single_topic.argsort()[-20:]


# %%
# twenty most used words in the selected topic
for index in top_twenty_words:
    print(cv.get_feature_names()[index])


# %%
# Grab the highest probability words per topic
for i,topic in enumerate(LDA.components_):
    print(f"THE TOP 15 WORDS FOR TOPIC #{i}")
    print([cv.get_feature_names()[index] for index in topic.argsort()[-15:]])
    print('\n')
    print('\n')


# %%
# documents belonging to a particular topic
topic_results = LDA.transform(dtm)


# %%
topic_results.shape


# %%
topic_results[0]


# %%
# show percentage relation from the first document with every topic
topic_results[0].round(2)


# %%
# grab the index of the highest probability (percentage)
topic_results[0].argmax()


# %%
npr['Topic'] = topic_results.argmax(axis=1) # topest topic in each document


# %%
npr


# %%



