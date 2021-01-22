# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def read_file(filepath):
    with open(filepath) as f:
        str_text = f.read()
    
    return str_text


# %%
# read_file('moby_dick_four_chapters.txt')


# %%
import spacy


# %%
nlp = spacy.load('en', disable=['parser', 'tagger', 'ner'])


# %%
nlp.max_length = 1198623


# %%
def separate_punc(doc_text):
    return [token.text.lower() for token in nlp(doc_text) if token.text not in '\n\n \n\n\n!"-#$%&()--.*+,-/:;<=>?@[\\]^_`{|}~\t\n ']


# %%
d = read_file('moby_dick_four_chapters.txt')


# %%
tokens = separate_punc(d)


# %%
len(tokens) # words here


# %%
#25 words --> network predicts word #26


# %%
train_len = 25 + 1

text_sequences = []

for i in range(train_len, len(tokens)):
    seq = tokens[i-train_len:i]

    text_sequences.append(seq)


# %%
type(text_sequences)


# %%
# text_sequences[0]
# text_sequences[1] # sequences, each sequence is one token over (+1 beginign and end)

' '.join(text_sequences[0])


# %%
' '.join(text_sequences[1])


# %%
' '.join(text_sequences[2])


# %%
# format text sequence into a numerical sequence for keras
from keras.preprocessing.text import Tokenizer


# %%
tokenizer = Tokenizer()
tokenizer.fit_on_texts(text_sequences)


# %%
sequences = tokenizer.texts_to_sequences(text_sequences)


# %%
# now we have our converted numeric sequences
# sequences[0] 


# %%
# each number is actually a word (token)
# tokenizer.index_word


# %%
for i in sequences[0]:
    print(f"{i} : {tokenizer.index_word[i]}")


# %%
# see how many times words appears in our sequence
# tokenizer.word_counts


# %%
vocabulary_size = len(tokenizer.word_counts) # number of unique words in all this 4 chapters document that we got


# %%
type(sequences)


# %%
# turn the sequence into a numpy matrix format, to create a train split with it
import numpy as np


# %%
sequences = np.array(sequences)


# %%
sequences


# %%



