# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import spacy
nlp = spacy.load('en_core_web_sm')


# %%
doc = nlp(u'This is the first sentence. This is another sentence. This is the last sentence.')


# %%
# generator: Generates and returns the sentence, instead of holding them in memory
for sent in doc.sents:
    print(sent)


# %%
# to grab a sentence by index, you may turn it into a list
list(doc.sents)[0]


# %%
type(list(doc.sents)[0])


# %%
doc = nlp(u'"Management is doing the right things; leadership is doing the right things." - Peter Drucker')


# %%
doc.text


# %%
for sent in doc.sents:
    print(sent)
    print('\n')


# %%
# ADD A SEGMENTATION RULE


# %%
# 1. Create a pipeline
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == ';':
            doc[token.i+1].is_sent_start = True
    return doc


# %%
# set the pipeline in nlp
nlp.add_pipe(set_custom_boundaries, before='parser')


# %%
nlp.pipe_names


# %%
# all the document, except last token
doc[:-1]


# %%
# create the same document again
doc4 = nlp(u'"Management is doing the right things; leadership is doing the right things." - Peter Drucker')


# %%
# test it
for sent in doc4.sents:
    print(sent)


# %%
# CHANGE SEGMENTATION RULE


# %%
# reloading the libary to reset behaviours
nlp = spacy.load('en_core_web_sm')


# %%
mystring = u"This is a sentence. This is another. \n\nThis is a \nthird sentence."


# %%
print(mystring)


# %%
doc = nlp(mystring)


# %%
for sentence in doc.sents:
    print(sentence)


# %%
from spacy.pipeline import SentenceSegmenter


# %%
# yield is like return, but without stopping the function execution
def split_on_newlines(doc):
    start = 0
    seen_newline = False

    for word in doc:
        if seen_newline:
            yield doc[start:word.i]
            start = word.i
            seen_newline = False
        elif word.text.startswith('\n'):
            seen_newline = True
    
    yield doc[start: ]


# %%
# creating new sentence segmenter
sbd = SentenceSegmenter(nlp.vocab, strategy=split_on_newlines)


# %%
# adding it as a new pipe
nlp.add_pipe(sbd)


# %%
doc = nlp(mystring)


# %%
# test that our new segment (function) works
for sentence in doc.sents:
    print(sentence)


# %%



