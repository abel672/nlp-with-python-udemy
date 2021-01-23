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
# part 2: Vectorizing stories
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer


# %%
tokenizer = Tokenizer(filters=[])
tokenizer.fit_on_texts(vocab)


# %%
tokenizer.word_index


# %%
# tokenization for stories, questions and answers
train_story_text = []
train_question_text = []
train_answers = []


# %%
# separate each of them
for story, question, answer in train_data:
    train_story_text.append(story)
    train_question_text.append(question)
    train_answers.append(answer)


# %%
# turning each text's word into its matching word sequence (check tokenizer.word_index)
train_story_seq = tokenizer.texts_to_sequences(train_story_text)


# %%
len(train_story_seq)


# %%
len(train_story_text)


# %%
train_story_seq # story vector


# %%
# create method to vectorize stories, questions and answers (same steps as before)
def vectorize_stories(data, word_index=tokenizer.word_index, max_story_len=max_story_len, max_question_len=max_question_len):
    
    # STORIES = X
    X = []
    # QUESTIONS Xq
    Xq = []
    # Y CORRECT ANSWER (yes/no)
    Y = []
    
    for story, query, answer in data:
        
        # for each story
        # [23, 14, ...]
        x = [word_index[word.lower()] for word in story]
        xq = [word_index[word.lower()] for word in query]
        
        y = np.zeros(len(word_index)+1)
        
        y[word_index[answer]] = 1
        
        X.append(x)
        Xq.append(xq)
        Y.append(y)
    
    return (pad_sequences(X, maxlen=max_story_len), pad_sequences(Xq, maxlen=max_question_len), np.array(Y))


# %%
# now we have our data formatted (Vectorized) and we can use it to create our models
inputs_train, queries_train, answers_train = vectorize_stories(train_data)


# %%
inputs_test, queries_tests, answers_test = vectorize_stories(test_data)


# %%
inputs_test


# %%
answers_test


# %%
tokenizer.word_index['yes'] # position of the answer yes


# %%
tokenizer.word_index['no'] # position of the answer no


# %%
sum(answers_test) # here you can see the two previous indexes


# %%
sum(answers_test)[7]


# %%
sum(answers_test)[13]


# %%



