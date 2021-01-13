# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# %% [markdown]
# # Parts of Speech Assessment
# %% [markdown]
# For this assessment we'll be using the short story [The Tale of Peter Rabbit](https://en.wikipedia.org/wiki/The_Tale_of_Peter_Rabbit) by Beatrix Potter (1902). <br>The story is in the public domain; the text file was obtained from [Project Gutenberg](https://www.gutenberg.org/ebooks/14838.txt.utf-8).

# %%
# RUN THIS CELL to perform standard imports:
import spacy
nlp = spacy.load('en_core_web_sm')
from spacy import displacy

# %% [markdown]
# **1. Create a Doc object from the file `peterrabbit.txt`**<br>
# > HINT: Use `with open('../TextFiles/peterrabbit.txt') as f:`

# %%
with open('../TextFiles/peterrabbit.txt') as f:
    doc = nlp(f.read())
    print(doc)

# %% [markdown]
# **2. For every token in the third sentence, print the token text, the POS tag, the fine-grained TAG tag, and the description of the fine-grained tag.**

# %%
# Enter your code here:
for token in list(doc.sents)[3]:
    print(f'{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {spacy.explain(token.tag_)}')

# %% [markdown]
# **3. Provide a frequency list of POS tags from the entire document**

# %%
POS_counts = doc.count_by(spacy.attrs.POS)
POS_counts

for k, v in sorted(POS_counts.items()):
    print(f'{k}. {doc.vocab[k].text:{10}}: {v}')

# %% [markdown]
# **4. CHALLENGE: What percentage of tokens are nouns?**<br>
# HINT: the attribute ID for 'NOUN' is 92

# %%
# Teacher Solution
print(len(doc)) # words in the document
print(POS_counts[92]) # words that are NOUN in the document


# %%
# POS = Part Of Speech, it contains all tags (NOUN, VERB, NUM, ...)
result = 100 * POS_counts[92] / len(doc)
print(f'{round(result, 2)}%')


# %%
# MY SOLUTION
all_tokens = 0
noun_tokens = 0
for k, v in sorted(POS_counts.items()):
    if (doc.vocab[k] == 92):
        noun_tokens = v
        print(f'Noun Token: {k}, {v}')
    all_tokens += v

result = (noun_tokens * 100) / all_tokens

print(f'{noun_tokens}/{all_tokens} = {round(result, 2)}%')

# %% [markdown]
# **5. Display the Dependency Parse for the third sentence**

# %%
# Teacher Solution
displacy.render(list(doc.sents)[3], style='dep', jupyter=True)


# %%
# MY SOLUTION
index = 0
for sent in doc.sents:
    if(index == 3):
        displacy.render(sent, style='dep', jupyter=True, options={'distance': 150})
        break
    index += 1

# %% [markdown]
# **6. Show the first two named entities from Beatrix Potter's *The Tale of Peter Rabbit* **

# %%
# Teacher Solution
for ent in doc.ents[:2]:
    print(ent.text + ' - ' + ent.label_ + ' - ' + str(spacy.explain(ent.label_)))


# %%
# My solution
for ent in list(doc.sents)[0].ents:
    print(ent.text + ' - ' + ent.label_ + ' - ' + str(spacy.explain(ent.label_)))

# %% [markdown]
# **7. How many sentences are contained in *The Tale of Peter Rabbit*?**

# %%
len(list(doc.sents))

# %% [markdown]
# **8. CHALLENGE: How many sentences contain named entities?**

# %%
# Teacher Solution
list_of_sents = [nlp(sent.text) for sent in doc.sents]
list_of_nent = [doc for doc in list_of_sents if doc.ents] # return sentence that contains entities in its doc
len(list_of_nent)


# %%
# My Solution
def count_sent_named_entities(doc):
    counter = 0
    # iterate over each sentence
    for sent in doc.sents:
        if sent.ents:
            counter += 1
    print(counter)

# 49


# %%
count_sent_named_entities(doc)

# %% [markdown]
# **9. CHALLENGE: Display the named entity visualization for `list_of_sents[0]` from the previous problem**

# %%
# Teacher Solution
displacy.render(list_of_sents[0], style='ent', jupyter=True)


# %%
# MY SOLUTION
displacy.render(nlp(list(doc.sents)[0].text), style='ent', jupyter=True)

# %% [markdown]
# ### Great Job!

