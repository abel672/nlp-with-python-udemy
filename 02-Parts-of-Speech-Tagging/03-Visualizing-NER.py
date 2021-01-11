# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import spacy


# %%
nlp = spacy.load('en_core_web_sm')


# %%
from spacy import displacy


# %%
doc = nlp(u"Over the last quarter Apple sold nearly 20 thousand iPods for a profit of $6 million."
        u"By contrast, Sony only sold 8 thousand Walkman music players")


# %%
displacy.render(doc, style='ent', jupyter=True)


# %%
# show line by line
for sent in doc.sents:
    displacy.render(nlp(sent.text), style='ent', jupyter=True)


# %%
# show only the entity PRODUCT
options = {'ents':['PRODUCT']}


# %%
displacy.render(doc, style='ent', jupyter=True, options=options)


# %%
# setting colors for entities
colors = {
    'ORG':'yellow',
    'PRODUCT': 'radial-gradient(yellow, red)', 
    'DATE': 'linear-gradient(90deg, purple, pink)'
}
options = {
    'ents':['PRODUCT', 'ORG', 'DATE'],
    'colors':colors
}


# %%
displacy.render(doc, style='ent', jupyter=True, options=options)


# %%
displacy.serve(doc, style='ent', options=options)


# %%



