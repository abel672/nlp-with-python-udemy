# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import nltk


# %%
nltk.download('vader_lexicon')


# %%
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# %%
sid = SentimentIntensityAnalyzer()


# %%
a = "This is a good movie"


# %%
sid.polarity_scores(a) # positive


# %%
a = "This was the best, most awesome movie EVER MADE!!!"


# %%
sid.polarity_scores(a) # super positive


# %%
a = "This was the WORST movie that has ever disgraced the screen."


# %%
sid.polarity_scores(a) # negative


# %%
# Sentiment Analysis with Amazon reviews
import pandas as pd


# %%
df = pd.read_csv('../TextFiles/amazonreviews.tsv', sep='\t')


# %%
df.head()


# %%
df['label'].value_counts() # count labels


# %%
df.dropna(inplace=True) # drop null


# %%
# check white spaces
blanks = []

for ind, label, review in df.itertuples():
    if type(review) == str:
        if review.isspace():
            blanks.append(ind)


# %%
blanks
# df.drop(blanks, inplace=True)


# %%
df.iloc[0]['review'] # first review


# %%
sid.polarity_scores(df.iloc[0]['review'])


# %%
# executing lambda Sentiment Analysis in all the reviews
# saving value in a new created column 'scores'
df['scores'] = df['review'].apply(lambda review: sid.polarity_scores(review))


# %%
df.head()


# %%
# getting every score.compund attribute and put it in a new column
df['compund'] = df['scores'].apply(lambda d: d['compound'])


# %%
df.head() # now we have the review compund score


# %%
# adding pos or neg tag according to compound value of the score
df['comp_score'] = df['compund'].apply(lambda score: 'pos' if score >= 0 else 'neg')


# %%
df.head() 


# %%
# checking the accuracy score of our current data frame
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# %%
accuracy_score(df['label'], df['comp_score'])


# %%
print(classification_report(df['label'], df['comp_score']))


# %%
print(confusion_matrix(df['label'], df['comp_score'])) # it should print something


# %%



