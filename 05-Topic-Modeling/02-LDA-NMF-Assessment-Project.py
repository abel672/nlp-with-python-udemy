# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# %% [markdown]
# # Topic Modeling Assessment Project
# 
# Welcome to your Topic Modeling Assessment! For this project you will be working with a dataset of over 400,000 quora questions that have no labeled cateogry, and attempting to find 20 cateogries to assign these questions to. The .csv file of these text questions can be found underneath the Topic-Modeling folder.
# 
# Remember you can always check the solutions notebook and video lecture for any questions.
# %% [markdown]
# #### Task: Import pandas and read in the quora_questions.csv file.

# %%
import pandas as pd


# %%
quora = pd.read_csv('quora_questions.csv')


# %%
quora.head()

# %% [markdown]
# # Preprocessing
# 
# #### Task: Use TF-IDF Vectorization to create a vectorized document term matrix. You may want to explore the max_df and min_df parameters.

# %%
from sklearn.feature_extraction.text import TfidfVectorizer


# %%
tfidf = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')


# %%
dtm = tfidf.fit_transform(quora['Question'])


# %%
dtm

# %% [markdown]
# # Non-negative Matrix Factorization
# 
# #### TASK: Using Scikit-Learn create an instance of NMF with 20 expected components. (Use random_state=42)..

# %%
from sklearn.decomposition import NMF


# %%
nmf_model = NMF(n_components=20, random_state=42)


# %%
nmf_model.fit(dtm)


# %%
nmf_model.components_[0].argsort()[-3:] # words indexes in topic  

# %% [markdown]
# #### TASK: Print our the top 15 most common words for each of the 20 topics.

# %%
print(tfidf.get_feature_names()[28463]) # tfidf possess all the words of vocabulary in a matrix by coordinates already by default.


# %%
for index, topic in enumerate(nmf_model.components_):
    print(f"THE TOP 15 WORDS FOR TOPIC # {index}")
    print([tfidf.get_feature_names()[i] for i in topic.argsort()[-15:]]) # we grab the word from the lib by topic index
    print('\n')

# %% [markdown]
# #### TASK: Add a new column to the original quora dataframe that labels each question into one of the 20 topic categories.

# %%
quora.head()


# %%
topic_results = nmf_model.transform(dtm) # topics results for each question (with NMF showed as coefients)


# %%
topic_results[0]


# %%
topic_results[0].argmax()


# %%
quora['Topic'] = topic_results.argmax(axis=1)


# %%
quora.head()

# %% [markdown]
# # Great job!

