# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
npr = pd.read_csv('npr.csv')


# %%
from sklearn.feature_extraction.text import TfidfVectorizer


# %%
tfidf = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')


# %%
dtm = tfidf.fit_transform(npr['Article'])


# %%
dtm


# %%
from sklearn.decomposition import NMF


# %%
nmf_model = NMF(n_components=7, random_state=42)


# %%
# NMF works faster than LDA for this kind of document, because numpy data structure fits better for this kind of matrix types
nmf_model.fit(dtm) 


# %%
tfidf.get_feature_names()[2300]


# %%
# LDA: Words having highest probabilities belonging to a topic
# NMF: Words having highest coeficient values inside of the matrix
for index, topic in enumerate(nmf_model.components_):
    print(f"THE TOP 15 WORDS FOR TOPIC # {index}")
    print([tfidf.get_feature_names()[i] for i in topic.argsort()[-15:]])


# %%
topic_results = nmf_model.transform(dtm)


# %%
topic_results[0] # Coeficient values  (before with LDA it was percentages probabilities)


# %%
# getting the indes of the most respresentative target
topic_results[0].argmax()


# %%
# getting the highest from each topic
topic_results.argmax(axis=1)


# %%
npr['Topic'] = topic_results.argmax(axis=1)


# %%
npr.head()


# %%
# parsing with a dictionary
mytopic_dict = {0:'health',1:'election',2:'legis',3:'poli',4:'election',5:'music',6:'edu'}

npr['Topic Label'] = npr['Topic'].map(mytopic_dict)


# %%
npr.head()


# %%



