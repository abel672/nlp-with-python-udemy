# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Perform standard imports
import spacy
nlp = spacy.load('en_core_web_sm')


# %%
from spacy.matcher import Matcher


# %%
matcher = Matcher(nlp.vocab) # loading our matcher


# %%
# SolarPower
pattern1 = [{'LOWER':'solarpower'}]
# Solar-power
pattern2 = [{'LOWER':'solar'},{'IS_PUNCT':True},{'LOWER':'power'}]
# Solar power
pattern3 = [{'LOWER':'solar'},{'LOWER':'power'}]


# %%
# creating matchers
matcher.add('SolarPower', None, pattern1, pattern2, pattern3)


# %%
doc = nlp(u"The Solar Power industry continues to grow as solar power increases. Solar-power is amazing.")


# %%
found_matches = matcher(doc)


# %%
print(found_matches)


# %%
for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id]     # get string representation
    span = doc[start:end]                       # get the matched span
    print(match_id, string_id, start, end, span.text)


# %%
# remove matcher
matcher.remove('SolarPower')


# %%



# %%
# solarPower SolarPower
pattern1 = [{'LOWER':'solarpowers'}]
# solar.power
pattern2 = [{'LOWER':'solar'},{'IS_PUNCT':True, 'OP':'*'},{'LOWER':'power'}]


# %%
matcher.add('SolarPower', None, pattern1, pattern2)


# %%
doc2 = nlp(u"Solar--power is solarpower yay!")


# %%
found_matches = matcher(doc2)


# %%
print(found_matches)


# %%



