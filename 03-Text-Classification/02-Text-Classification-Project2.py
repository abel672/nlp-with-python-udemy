# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd


# %%
df = pd.read_csv("../TextFiles/moviereviews.tsv", sep='\t')


# %%
df.head()


# %%
len(df)


# %%
# print(df['review'][2]) # checking review number 2

# %% [markdown]
# ### Part 1: Clean our data

# %%
# checking missing values
df.isnull().sum()


# %%
# removing null values for our data frame
df.dropna(inplace=True)


# %%
# cleaned
df.isnull().sum()


# %%
# databases sometimes put an empty / blank string instead of null values
mystring = 'hello'
empty = ' '


# %%
mystring.isspace()


# %%
empty.isspace()


# %%
# how to check in a df
blanks = []

# (index, label, review text)
for i, lb, rv in df.itertuples():
    if rv.isspace():
        blanks.append(i)


# %%
# index positions of all the empty white spaces in the reviews
blanks


# %%
# cleaning the df from all those index positions
df.drop(blanks, inplace=True)


# %%
len(df) # cleaned

# %% [markdown]
# #### Part 2: Train our data

# %%
from sklearn.model_selection import train_test_split


# %%
X = df['review']


# %%
y = df['label']


# %%
# creating training sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# %%
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC


# %%
# Vectorization, Tfid Transformation and Clasification
text_clf = Pipeline([('tfidf', TfidfVectorizer()),
                    ('clf', LinearSVC())])


# %%
text_clf.fit(X_train, y_train) # training our model


# %%
predictions = text_clf.predict(X_test) # creating our model


# %%
# testing it
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score


# %%
print(confusion_matrix(y_test, predictions)) # confusion matrix


# %%
print(classification_report(y_test, predictions)) # classification predictions


# %%
print(accuracy_score(y_test, predictions)) # accuracy score (percentage)


# %%



