# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ### Feature extraction from a real file

# %%
import numpy as np 
import pandas as pd


# %%
df = pd.read_csv('../TextFiles/smsspamcollection.tsv', sep='\t')


# %%
df.head()


# %%
df.isnull().sum()


# %%
df['label'].value_counts()


# %%
from sklearn.model_selection import train_test_split


# %%
X = df['message']


# %%
y = df['label']


# %%
# creating train and test suit
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# %%
# Transform documents into feature vectors
from sklearn.feature_extraction.text import CountVectorizer


# %%
count_vect = CountVectorizer() # this module allows us to do all the transformations


# %%
X # we sill pass this to the count vectorizer and transform it.

# %% [markdown]
# ### Two steps to transform with the Count Vectorizer
# 
# 1-FIT VECTORIZER TO THE DATA (build a vocab, count the number of words...)
# 
# 2-TRANSFORM THE ORIGINAL TEXT MESSAGE --> VECTOR

# %%
# OPTION 1: Two steps (fit, transform)
# count_vect.fit(X_train) # build vocab, count nuber of words
# X_train_counts = count_vect.transform(X_train) # transform the text

# OPTION 2: All in one step (fit and transform)
X_train_counts = count_vect.fit_transform(X_train) # build vocab, count words and transforms


# %%
# this is a huge sparse matrix
X_train_counts # 3733 messages x 7082 unique words in those messages


# %%
X_train.shape


# %%
# we have the messages and the vocab count (see last step in 01-Feature-Extraction-from-Text2.ipynb)
X_train_counts.shape 


# %%



