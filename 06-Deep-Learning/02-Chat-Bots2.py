# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pickle
import numpy as np


# %%
with open('train_qa.txt', 'rb') as f:
    train_data = pickle.load(f)


# %%
with open('test_qa.txt', 'rb') as f:
    test_data = pickle.load(f)


# %%
type(test_data)


# %%
type(train_data)


# %%
len(train_data)


# %%
len(test_data)


# %%
train_data[0] # train data sentences followed with a questin and an answer


# %%
# story
' '.join(train_data[0][0])


# %%
# question
' '.join(train_data[0][1])


# %%
# answer
train_data[0][2]


# %%
# create a vocabulary
all_data = test_data + train_data


# %%
len(all_data)


# %%
set(train_data[0][0]) # turn list into a set


# %%
vocab = set()

for story, question, answer in all_data:
    # unite all sets into one set (it organize values and remove repeated ones)
    # https://www.programiz.com/python-programming/methods/set/union
    vocab = vocab.union(set(story))
    vocab = vocab.union(set(question))


# %%
vocab.add('no')


# %%
vocab.add('yes')


# %%
# set of all the possible vocab words
vocab


# %%
vocab_len = len(vocab) + 1 # (+ 1 is the placeholder that we will use later on, by deffect is 0)


# %%
vocab_len


# %%
# LONGEST STORY
# the all stories length
all_story_lens = [len(data[0]) for data in all_data]


# %%
max_story_len = max(all_story_lens) # get the max length


# %%
# LONGEST QUESTION
# get max question length too
all_question_lens = [len(data[1]) for data in all_data]
max_question_len = max(all_question_lens)


# %%
max_question_len


# %%



