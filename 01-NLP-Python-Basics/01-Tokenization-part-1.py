# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import spacy
nlp = spacy.load('en_core_web_sm')


# %%
mystring = '"We\'re moving to L.A.!"'


# %%
print(mystring)


# %%
doc = nlp(mystring)


# %%
for token in doc:
    print(token.text)


# %%
doc2 = nlp(u"We're to help! Send snail-mail, email support@oursite.com or visit us at http://www.oursite.com!")


# %%
for t in doc2:
    print(t)


# %%
doc3 = nlp(u"A 5km NYC cab ride costs $10.30")


# %%
for t in doc3:
    print(t)


# %%
doc4 = nlp(u"Let's visit St. Louis in the U.S. next year.")


# %%
for t in doc4:
    print(t)


# %%
len(doc4)


# %%
len(doc4.vocab)


# %%
doc5 = nlp(u"It is better to give than receive")


# %%
doc5[0]


# %%
doc5[2:5]


# %%
doc6 = nlp(u'Apple to build a Hong Kong factory for $6 million')


# %%
for token in doc6:
    print(token.text, end=' | ')


# %%
# print entities found in the text
for entity in doc6.ents:
    print(entity)
    print(entity.label_)
    print(str(spacy.explain(entity.label_)))
    print('\n')


# %%
doc9 = nlp(u'Autonomous cars shift insurance liability toward manufacturers.')


# %%
for chunk in doc9.noun_chunks:
    print(chunk)


# %%



