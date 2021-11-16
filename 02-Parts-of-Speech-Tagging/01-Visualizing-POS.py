# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import spacy


# %%
nlp = spacy.load('en_core_web_sm')


# %%
doc = nlp(u"The quick brown fox jumped over the lazy dog.")


# %%
from spacy import displacy


# %%
displacy.render(doc, style='dep', jupyter=True)


# %%
options = {'distance': 110, 'compact':'True','color':'yellow','bg':'#09a3d5','font':'Times'}


# %%
displacy.render(doc, style='dep', jupyter=True, options=options)


# %%
doc2 = nlp(u"This is a sentence. This is another sentence, possibly longer than the other.")


# %%
spans = list(doc2.sents)
# spans = [sent for sent in doc2.sents]
spans


# %%
displacy.serve(spans, style='dep', options=options)


# %%



