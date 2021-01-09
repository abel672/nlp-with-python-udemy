# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Perform standard imports
import spacy
nlp = spacy.load('en_core_web_sm')

# %%
# Part 2
from spacy.matcher import PhraseMatcher


# %%
matcher = PhraseMatcher(nlp.vocab)


# %%
with open('../TextFiles/reaganomics.txt', encoding='cp1252') as f:
    doc3 = nlp(f.read())


# %%
phrase_list = ['voodoo economics', 'supply-sides economics', 'tickle-down economics', 'free-market economics']


# %%
phrase_patterns = [nlp(text) for text in phrase_list] # create patterns for phrases


# %%
phrase_patterns


# %%
matcher.add('EconMatcher', None, *phrase_patterns) # creating matcher


# %%
found_matches = matcher(doc3)


# %%
found_matches


# %%
for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id]     # get string representation
    span = doc3[start:end]                      # get the matched span
    print(match_id, string_id, start, end, span.text)


# %%



