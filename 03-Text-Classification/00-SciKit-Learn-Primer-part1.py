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
##### PART 2. Test the accuracy of the model, using the data set
from sklearn import metrics


# %%
predictions = lr_model.predict(X_test)


# %%
predictions # predictions of my model


# %%
y_test # true values


# %%
# test predictions and true values in a confusion matrix
print(metrics.confusion_matrix(y_test, predictions))


# %%
# you can make the confusion matrix simpler by adding labels
df = pd.DataFrame(metrics.confusion_matrix(y_test, predictions), index=['ham', 'spam'], columns=['ham', 'spam'])


# %%
df # confusion matrix data frame


# %%
# clasification report with the same data
print(metrics.classification_report(y_test, predictions)) 
# The model is good predicting 'ham' but not very good predicting 'spam' messages


# %%
# accuracy of my model
print(metrics.accuracy_score(y_test, predictions))

# %% [markdown]
# ### Creating another model

# %%
# Same steps as the previous model
from sklearn.naive_bayes import MultinomialNB

nb_model = MultinomialNB() # create model

nb_model.fit(X_train, y_train) #t rain model

# Test model part
predictions = nb_model.predict(X_test) # make a prediction with it

print(metrics.confusion_matrix(y_test, predictions)) # test the results


# %%
print(metrics.classification_report(y_test, predictions)) # this model can not predict any 'spam' at all

# %% [markdown]
# ### Creating another model

# %%
from sklearn.svm import SVC


# %%
svc_model = SVC(gamma='auto')

svc_model.fit(X_train, y_train)

predictions = svc_model.predict(X_test)

print(metrics.confusion_matrix(y_test, predictions))


# %%
print(metrics.classification_report(y_test, predictions))


# %%



