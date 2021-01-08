# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import spacy
nlp = spacy.load('en_core_web_sm')

# %%
# tokenization part 2
from spacy import displacy


# %%
doc = nlp(u"Apple is going to build a U.K. factory for $6 million.")


# %%
displacy.render(doc, style='dep', jupyter=True, options={'distance': 110})


# %%
doc = nlp(u"Over the last quarter Apple sold nearly 20 thousand iPods for a profit of $6 million.")


# %%
displacy.render(doc, style='ent', jupyter=True)


# %%
doc = nlp(u"This is a sentence")
displacy.serve(doc, style='dep')


# %%



