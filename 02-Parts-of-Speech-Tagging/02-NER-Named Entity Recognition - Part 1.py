# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import spacy


# %%
nlp = spacy.load('en_core_web_sm')


# %%
def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text + ' - ' + ent.label_ + ' - ' + str(spacy.explain(ent.label_)))
    else:
        print('No entities found')


# %%
doc = nlp(u'Hi how are you?')


# %%
show_ents(doc)


# %%
doc = nlp(u'May I go to Washington, DC next May to see the Washington Monument?')


# %%
show_ents(doc)


# %%
doc = nlp(u"Can I please have 500 dollars of Mircrosoft stock?")


# %%
show_ents(doc)


# %%
doc = nlp(u"Tesla to build a U.K factory for $6 million")


# %%
show_ents(doc)


# %%
# adding a new entity label
from spacy.tokens import Span


# %%
ORG = doc.vocab.strings[u"ORG"]


# %%
ORG


# %%
# token location in the doc (Tesla)
start = 0
end = 1
# setup token in entity group
new_ent = Span(doc, start, end, label=ORG)


# %%
doc.ents = list(doc.ents) + [new_ent]


# %%
# test results
show_ents(doc)


# %%



