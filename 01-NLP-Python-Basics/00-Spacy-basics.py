# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import spacy


# %%
nlp = spacy.load('en_core_web_sm')


# %%
doc = nlp(u'Tesla is looking at buying U.S. startup for $6 million')


# %%
for token in doc:
    print(f"[Text: {token.text}, Type:  {token.pos_}, Position: {token.pos}]")


# %%
nlp.pipeline # module's pipelines


# %%
nlp.pipe_names


# %%
doc2 = nlp(u"Tesla isn't    looking into startups anymore.")


# %%
for token in doc2:
    print(token.text, token.pos_, token.dep_)


# %%
doc2[0].pos_


# %%
doc2[0].dep_


# %%
doc3 = nlp(u'Although commmonly attributed to John Lennon from his song "Beautiful Boy", the phrase "Life is what happens to us while we are making other plans" was written by cartoonist Allen Saunders and published in Reader\'s Digest in 1957, when Lennon was 17.')


# %%
life_quote =doc3[16:30]


# %%
print(life_quote)


# %%
type(life_quote)


# %%
type(doc3)


# %%
doc4 = nlp(u"This is the first sentence. This is another sentence. This is the last sentence.")


# %%
# getting everysentence, detected by ". "
for sentence in doc4.sents:
    print(sentence)


# %%
doc4[6]


# %%
doc4[6].is_sent_start # is the start of a sentence?


# %%



