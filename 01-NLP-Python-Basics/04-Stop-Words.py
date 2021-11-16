# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import spacy


# %%
nlp = spacy.load('en_core_web_sm')


# %%
print(nlp.Defaults.stop_words)


# %%
len(nlp.Defaults.stop_words)


# %%
nlp.vocab['mistery'].is_stop


# %%
# add custom stop word to the set
nlp.Defaults.stop_words.add('btw')


# %%
nlp.vocab['btw'].is_stop = True


# %%
len(nlp.Defaults.stop_words)


# %%
nlp.vocab['btw'].is_stop


# %%
# remove stop word from the set
nlp.Defaults.stop_words.remove('beyond')


# %%
nlp.vocab['beyond'].is_stop = False


# %%
nlp.vocab['beyond'].is_stop


# %%



