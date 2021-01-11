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
# part two
doc = nlp(u"Our company created a brand new vacuum cleaner."
            u"This new vacuum-cleaner is the best in show.")


# %%
show_ents(doc)


# %%
from spacy.matcher import PhraseMatcher


# %%
matcher = PhraseMatcher(nlp.vocab)


# %%
phrase_list = ['vacuum cleaner', 'vacuum-cleaner']


# %%
phrase_patterns = [nlp(text) for text in phrase_list]


# %%
# creating a product phrase matcher
matcher.add('newproduct', None, *phrase_patterns)


# %%
found_matches = matcher(doc)


# %%
found_matches


# %%
from spacy.tokens import Span


# %%
# Creating NER for Products
PROD = doc.vocab.strings[u"PRODUCT"]


# %%
found_matches


# %%
# extracting the new found Product entities int the doc with our NER and matcher
new_ents = [Span(doc, match[1], match[2], label=PROD) for match in found_matches]


# %%
# adding out new product entities to our doc entities
doc.ents = list(doc.ents) + new_ents


# %%
show_ents(doc)


# %%
doc = nlp(u"Originally I paid $29.95 for this car toy, but now it is marked down by 10 dollars.")


# %%
# getting just the MONEY entities from our document
len([ent for ent in doc.ents if ent.label_ == "MONEY"])


# %%



