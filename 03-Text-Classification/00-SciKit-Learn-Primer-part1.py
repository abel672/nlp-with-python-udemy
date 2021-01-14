# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import numpy as np
import pandas as pd


# %%
# data frame object
df = pd.read_csv('../TextFiles/smsspamcollection.tsv', sep='\t')


# %%
# show first five rows
df.head()


# %%
df.isnull()


# %%
df.isnull().sum()
# if you see a '1', it means the is a missing value


# %%
len(df)


# %%
# getting a column value
df['label']


# %%
# getting the unique values of this column
df['label'].unique()


# %%
# see how many values of each unique value do we have
df['label'].value_counts()


# %%
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.xscale('log')
bins = 1.15**(np.arange(0,50))
# histograms of the length column
plt.hist(df[df['label']=='ham']['length'], bins=bins, alpha=0.8)
plt.hist(df[df['label']=='spam']['length'], bins=bins, alpha=0.8)
plt.legend(('ham', 'spam'))
plt.show()


# %%
plt.xscale('log')
bins = 1.5**(np.arange(0, 15))
# histrograms of the punctuation column
plt.hist(df[df['label']=='ham']['punct'], bins=bins, alpha=0.8)
plt.hist(df[df['label']=='spam']['punct'], bins=bins, alpha=0.8)
plt.legend(('ham', 'spam'))
plt.show()

# %% [markdown]
# ### How to conduct a machine learning model with SciKit Lean

# %%
# 1. Split the data into a Train Set and a Test Set
from sklearn.model_selection import train_test_split


# %%
# X feature data
X = df[['length', 'punct']]
# y is our label
y = df['label']

# shift + tab shows the method's documentation 
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3, # 30% of the data goes to the Test Set
    random_state=42 # to get an specific test split (not really important)
)


# %%
# rows, columns
X_train.shape # training data for the features


# %%
# X_test.shape # test data
X_test


# %%
# y_test.shape
y_test # labels that corresponds with X_test


# %%
y_train.shape


# %%
# 2. Create and train a machine learning model

# We are going to train multiple moderns
# The extact process is similar regardless the model that you choose

from sklearn.linear_model import LogisticRegression


# %%
lr_model = LogisticRegression(solver='lbfgs')


# %%
# train our model
lr_model.fit(X_train, y_train) # once we run this, our model is ready to predict data


# %%



