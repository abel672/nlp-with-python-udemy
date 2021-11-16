# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import spacy


# %%
nlp = spacy.load('en_core_web_sm')


# %%
doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")


# %%
print(doc.text)


# %%
# get a token of the doc
print(doc[4])


# %%
# print the tag of a token
print(doc[4].tag_)


# %%
print(doc[4].pos_)


# %%
for token in doc:
    print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")


# %%
doc = nlp(u"I read books on NLP.")


# %%
word = doc[1]


# %%
word.text


# %%
token = word
print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")


# %%
# same word, different context
doc = nlp(u"I read a book on NLP.")
print(doc.text)


# %%
# the result also changes, due to the context is different
word = doc[1]

token = word
print(f"{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}")


# %%
doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")


# %%
POS_counts = doc.count_by(spacy.attrs.POS)


# %%
# number id of each token, and how many times it shows up
POS_counts


# %%
doc.vocab[84].text


# %%
doc[2]


# %%
doc[2].pos


# %%
doc[2].pos_


# %%
# POS Part-of-speech tags
for k, v in sorted(POS_counts.items()):
    print(f"{k}. {doc.vocab[k].text:{5}} {v}")


# %%
TAG_counts = doc.count_by(spacy.attrs.TAG)

# Fine Grained Tags
for k, v in sorted(TAG_counts.items()):
    print(f"{k}. {doc.vocab[k].text:{5}} {v}")


# %%
DEP_counts = doc.count_by(spacy.attrs.DEP)

# Sintactic Dependencies
for k, v in sorted(DEP_counts.items()):
    print(f"{k}. {doc.vocab[k].text:{5}} {v}")

# %% [markdown]
# ### TIPS:
# 
# ### to explain a specific tag
# spacy.explain(token.tag_)
# 
# ### to get the count of a specific attribute
# doc.count_by(spacy.attrs.POS)
# 
# doc.count_by(spacy.attrs.TAG)
# 
# doc.count_by(spacy.attrs.DEP)

# %%



