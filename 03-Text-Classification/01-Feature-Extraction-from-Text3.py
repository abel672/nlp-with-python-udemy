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
X # we will pass this to the count vectorizer and transform it.

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
# Part 2: Tfid Transformation and Clasification
from sklearn.feature_extraction.text import TfidfTransformer


# %%
tfidf_transformer = TfidfTransformer()


# %%
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)


# %%
X_train_tfidf.shape # not just counter: term frequency * inverse document's frequency


# %%
# Counter Vectorization and Tfid Transformation into one step
from sklearn.feature_extraction.text import TfidfVectorizer


# %%
vectorizer = TfidfVectorizer()


# %%
X_train_tfidf = vectorizer.fit_transform(X_train)


# %%
# Step 3. Clasification: train a clasifier
from sklearn.svm import LinearSVC


# %%
clf = LinearSVC()


# %%
clf.fit(X_train_tfidf, y_train) # our traininig set has been vectorized into a full vocabulary

# %% [markdown]
# ### To perform an analysis in our test set, we have to do all the same procedures as the training set

# %%
# Perform Vectozization, Tfid Transformation and Clasification in one single pipeline
from sklearn.pipeline import Pipeline


# %%
# pipeline with Vectorization, Tfid Transformation and Clasification
text_clf = Pipeline([('tfidf', TfidfVectorizer()), ('clf', LinearSVC())]) 


# %%
text_clf.fit(X_train, y_train)


# %%
predictions = text_clf.predict(X_test) # creating our model with all the training data


# %%
from sklearn.metrics import confusion_matrix, classification_report


# %%
print(confusion_matrix(y_test, predictions)) # very good results


# %%
print(classification_report(y_test, predictions)) # very good results


# %%
from sklearn import metrics


# %%
metrics.accuracy_score(y_test, predictions) # 99% score


# %%
# using our successed model to predict another message
text_clf.predict(["Congratinations! You've been selected as a winner. TEXT WON to 44255 congratulations free entry to contest."])


# %%
text_clf.predict(["Dear Marty, how are you?. We are going to do ski this weekend. Would you like to join us?"])


# %%



