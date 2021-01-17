# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# %% [markdown]
# # Text Classification Assessment
# This assessment is very much like the Text Classification Project we just completed, and the dataset is very similar.
# 
# The **moviereviews2.tsv** dataset contains the text of 6000 movie reviews. 3000 are positive, 3000 are negative, and the text has been preprocessed as a tab-delimited file. As before, labels are given as `pos` and `neg`.
# 
# We've included 20 reviews that contain either `NaN` data, or have strings made up of whitespace.
# 
# For more information on this dataset visit http://ai.stanford.edu/~amaas/data/sentiment/
# %% [markdown]
# ### Task #1: Perform imports and load the dataset into a pandas DataFrame
# For this exercise you can load the dataset from `'../TextFiles/moviereviews2.tsv'`.

# %%
import pandas as pd

df = pd.read_csv('../TextFiles/moviereviews2.tsv', sep='\t')




# %%
df.head()


# %%
len(df)

# %% [markdown]
# ### Task #2: Check for missing values:

# %%
# Check for NaN values:
df.isnull().sum()


# %%
# Check for whitespace strings (it's OK if there aren't any!):
blanks = []

for i, label, review in df.itertuples():
    if type(review) == str:
        if review.isspace():
            blanks.append(i)


# %%
len(blanks)

# %% [markdown]
# ### Task #3: Remove NaN values:

# %%
df.dropna(inplace=True)


# %%
df.isnull().sum()

# %% [markdown]
# ### Task #4: Take a quick look at the `label` column:

# %%
df['label'].value_counts()

# %% [markdown]
# ### Task #5: Split the data into train & test sets:
# You may use whatever settings you like. To compare your results to the solution notebook, use `test_size=0.33, random_state=42`

# %%
from sklearn.model_selection import train_test_split

X = df['review']
y = df['label']


# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# %% [markdown]
# ### Task #6: Build a pipeline to vectorize the date, then train and fit a model
# You may use whatever model you like. To compare your results to the solution notebook, use `LinearSVC`.

# %%

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

text_clf = Pipeline([('tfidf', TfidfVectorizer()),
                    ('clf', LinearSVC())])


text_clf.fit(X_train, y_train)

# %% [markdown]
# ### Task #7: Run predictions and analyze the results

# %%
# Form a prediction set
predictions = text_clf.predict(X_test)


# %%
# Report the confusion matrix
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score


# %%
print(confusion_matrix(y_test, predictions))


# %%
# Print a classification report
print(classification_report(y_test, predictions))


# %%
# Print the overall accuracy
print(accuracy_score(y_test, predictions))

# %% [markdown]
# ## Great job!

