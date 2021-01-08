# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import nltk


# %%
from nltk.stem.porter import PorterStemmer


# %%
p_stemmer = PorterStemmer()


# %%
words = ['run', 'runner', 'ran', 'runs', 'easily', 'fairly', 'fairness']


# %%
for word in words:
    print(word + '------>' + p_stemmer.stem(word))


# %%
from nltk.stem.snowball import SnowballStemmer


# %%
s_stemmer = SnowballStemmer(language='english')


# %%
for word in words:
    print(word + ' ------> ' + s_stemmer.stem(word))


# %%
words = ['generous', 'generation', 'generously', 'generate']


# %%
for word in words:
    print (word + ' -------> ' + s_stemmer.stem(word))


# %%



