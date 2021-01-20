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
dtm = cv.fit_transform(npr['Article'])


# %%
dtm


# %%
from sklearn.decomposition import LatentDirichletAllocation


# %%
LDA = LatentDirichletAllocation(n_components=7, random_state=42)


# %%
LDA.fit(dtm)


# %%
# Grab the vocabulary of words

# Grab the topics

# Grab the highest probability words per topic


