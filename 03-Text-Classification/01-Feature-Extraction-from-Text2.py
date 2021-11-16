# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
get_ipython().run_cell_magic('writefile', '1.txt', 'This is a story about cats\nour feline pets\nCats are furry animals')


# %%
get_ipython().run_cell_magic('writefile', '2.txt', 'This story is about surfing\nCatching waves is fun\nSurfing is a popular water sport')

# %% [markdown]
# ### Build a vocabulary
# 

# %%
vocab = {}
i = 1

with open('1.txt') as f:
    x = f.read().lower().split()

for word in x:
    if word in vocab:
        continue
    else:
        vocab[word] = i
        i+=1

print(vocab)


# %%
with open('2.txt') as f:
    x = f.read().lower().split()

for word in x:
    if word in vocab:
        continue
    else:
        vocab[word] = 1
        i+=1

print(vocab)

# %% [markdown]
# ### Feature extraction

# %%
# Create an empty vector with space for each word in the vocabulary:
one = ['1.txt']+[0]*len(vocab) # add a '0' for each word that is in the voc
one


# %%
# map the frequencies of each word across the text document (1.txt in this case)
with open('1.txt') as f:
    x = f.read().lower().split()

for word in x:
    one[vocab[word]]+=1

one


# %%
# Do the same for the second document
two = ['2.txt']+[0]*len(vocab)

with open('2.txt') as f:
    x = f.read().lower().split()

for word in x:
    two[vocab[word]]+=1


# %%
# compare the two vectors (VOCAB COUNT)
print(f'{one}\n{two}')


# %%



