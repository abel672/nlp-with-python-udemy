# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd


# %%
df = pd.read_csv('../TextFiles/moviereviews.tsv', sep='\t')


# %%
df.head()


# %%
df.dropna(inplace=True) # removing null values


# %%
# checking white spaces
blanks = []

for ind, label, review in df.itertuples():
    if type(review) == str:
        if review.isspace():
            blanks.append(ind)


# %%
blanks


# %%
# removing white spaces
df.drop(blanks, inplace=True)


# %%
# checking our label counts
df['label'].value_counts()


# %%
# Start Sentiment Analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# %%
sid = SentimentIntensityAnalyzer()


# %%
df['scores'] = df['review'].apply(lambda review: sid.polarity_scores(review))


# %%
df['compound'] = df['scores'].apply(lambda d: d['compound'])


# %%
df.head()


# %%
df['comp_score'] = df['compound'].apply(lambda score: 'pos' if score >= 0 else 'neg')


# %%
df.head()


# %%
# compare label and score through all the data frame
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix


# %%
print(confusion_matrix(df['label'], df['comp_score']))


# %%
print(classification_report(df['label'], df['comp_score']))


# %%
print(accuracy_score(df['label'], df['comp_score']))


# %%



