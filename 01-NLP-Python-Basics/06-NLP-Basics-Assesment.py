# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# %% [markdown]
# # NLP Basics Assessment
# %% [markdown]
# For this assessment we'll be using the short story [_An Occurrence at Owl Creek Bridge_](https://en.wikipedia.org/wiki/An_Occurrence_at_Owl_Creek_Bridge) by Ambrose Bierce (1890). <br>The story is in the public domain; the text file was obtained from [Project Gutenberg](https://www.gutenberg.org/ebooks/375.txt.utf-8).

# %%
# RUN THIS CELL to perform standard imports:
import spacy
nlp = spacy.load('en_core_web_sm')

# %% [markdown]
# **1. Create a Doc object from the file `owlcreek.txt`**<br>
# > HINT: Use `with open('../TextFiles/owlcreek.txt') as f:`

# %%
# Enter your code here:
with open('../TextFiles/owlcreek.txt') as f:
    doc = nlp(f.read())


# %%
# Run this cell to verify it worked:

doc[:36]

# %% [markdown]
# **2. How many tokens are contained in the file?**

# %%
print(len(doc))

# %% [markdown]
# **3. How many sentences are contained in the file?**<br>HINT: You'll want to build a list first!

# %%
sentences = [sent for sent in doc.sents]


# %%
len(sentences)

# %% [markdown]
# **4. Print the second sentence in the document**<br> HINT: Indexing starts at zero, and the title counts as the first sentence.

# %%
print(sentences[2].text)

# %% [markdown]
# ** 5. For each token in the sentence above, print its `text`, `POS` tag, `dep` tag and `lemma`<br>
# CHALLENGE: Have values line up in columns in the print output.**

# %%
# NORMAL SOLUTION:
for token in sentences[2]:
    print(token.text, token.pos_, token.dep_, token.lemma_)


# %%
# CHALLENGE SOLUTION:
for token in sentences[2]:
    print(f'{token.text:{15}} {token.pos_:{5}} {token.dep_:{10}} {token.lemma_:{15}}')

# %% [markdown]
# **6. Write a matcher called 'Swimming' that finds both occurrences of the phrase "swimming vigorously" in the text**<br>
# HINT: You should include an `'IS_SPACE': True` pattern between the two words!

# %%
# Import the Matcher library:

from spacy.matcher import Matcher
matcher = Matcher(nlp.vocab)


# %%
# Create a pattern and add it to matcher:
pattern = [{'LOWER':'swimming'}, {'IS_SPACE': True, 'OP': '*'}, {'LOWER':'vigorously'}]

matcher.add('Swimming', None, pattern)


# %%
# Create a list of matches called "found_matches" and print the list:
found_matches = matcher(doc)

print(found_matches)

# %% [markdown]
# **7. Print the text surrounding each found match**

# %%
def surrounding_simple(start, end, doc):
    print(doc[start-10:end+10])


# %%
def surrounding_advanced(text, doc):
    for match_id, start, end in text:
        span = doc[start-10:end+10]
        print(span)


# %%
surrounding_simple(1274, 1277, doc)


# %%
surrounding_simple(3607, 3610, doc)

# %% [markdown]
# ### Extra Credit:
# ### Print the sentence that contains each found match

# %%
for sentence in sentences:
    if found_matches[0][1] < sentence.end:
        print(sentence)
        break

# each sentence has a start and end
# each match has also a start and end
# we just check which sentence has an end bigger than the match's start


# %%
for sentence in sentences:
    if found_matches[1][1] < sentence.end:
        print(sentence)
        break

# the same, with the second match

# %% [markdown]
# ### Great Job!

