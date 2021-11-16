# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import spacy


# %%
nlp = spacy.load('en_core_web_lg')


# %%
nlp(u'The quick brown fox jumped').vector


# %%
nlp(u'The quick brown fox jumped').vector.shape # vector's dimension


# %%
nlp(u'fox').vector.shape


# %%
tokens = nlp(u'lion cat pet')


# %%
# similarities between tokens
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# %%
# different words in similar context may also have relationships
tokens = nlp(u'like love hate')


# %%
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# %%
nlp.vocab.vectors.shape # 684000 for every 300 dimension in each particular word vector


# %%
tokens = nlp(u'dog cat Abel')


# %%
# oov = Out Of Vocabulary
for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)


# %%
# calculate cosine similiarity
from scipy import spatial

cosine_similarity = lambda vec1, vec2: 1 - spatial.distance.cosine(vec1, vec2)


# %%
# grab some vectors
king = nlp.vocab['king'].vector
man = nlp.vocab['man'].vector
woman = nlp.vocab['woman'].vector


# %%
# king - man + woman ---> NEW_VECTOR similar Queen, princess, highness


# %%
new_vector = king - man + woman


# %%
computed_similarities = []

# FOR ALL WORDS IN MY VOCAB
for word in nlp.vocab:
    if word.has_vector:
        if word.is_lower:
            if word.is_alpha:
                similarity = cosine_similarity(new_vector, word.vector)
                computed_similarities.append((word, similarity))


# %%
# sort in descending order (-item) by similarity value (-item[1])
computed_similarities = sorted(computed_similarities, key=lambda item:-item[1])


# %%
# print first 10 items
print([t[0].text for t in computed_similarities[:10]])


# %%



