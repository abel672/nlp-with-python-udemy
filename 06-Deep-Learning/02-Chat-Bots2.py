# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

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

# %% [markdown]
# ## Setting up Vocabulary of all words

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
max_story_len


# %%
# LONGEST QUESTION
# get max question length too
all_question_lens = [len(data[1]) for data in all_data]
max_question_len = max(all_question_lens)


# %%
max_question_len

# %% [markdown]
# ## Vectorizing the Data

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
#     train_answers.append(answer)


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
inputs_test, queries_test, answers_test = vectorize_stories(test_data)


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
# part 3: Build the Neural Network
    # Input Encoder M
    # Input Encoder C
    # Question Encoder
# Complete the Network


# %%
from keras.models import Sequential,Model


# %%
from keras.layers.embeddings import Embedding


# %%
from keras.layers import Input,Activation,Dense,Permute,Dropout,add,dot,concatenate,LSTM


# %%
# PLACEHOLDERS shape=(max_story_len, batch_size): They will receive input later based on stories and questinos
# We will pass this to our encoders
input_sequence = Input((max_story_len,))
question = Input((max_question_len,))


# %%
# Create input encoders
# 1. Define vocabulary size (voca_len)
vocab_size = len(vocab) + 1


# %%
# INPUT ENCODER M: Get embedded to a sequence of vectors
input_encoder_m = Sequential()
input_encoder_m.add(Embedding(input_dim=vocab_size, output_dim=64))
# when bigger is the value, longer is the training
input_encoder_m.add(Dropout(0.5)) # 50% of the neurons will be turned off, that helps with over feeding

# OUTPUT
# (samples, story_maxlen, embedding_dim)


# %%
# INPUT ENCODER C
input_encoder_c = Sequential()
input_encoder_c.add(Embedding(input_dim=vocab_size, output_dim=max_question_len))
input_encoder_c.add(Dropout(0.5))

# OUTPUT
# (samples, story_maxlen, max_question_len)


# %%
# QUESTION ENCODER
question_encoder = Sequential()
question_encoder.add(Embedding(input_dim=vocab_size,output_dim=64,input_length=max_question_len))
question_encoder.add(Dropout(0.3))

# OUTPUT
# (samples, query_maxlen, embedding_dim)


# %%
#  ENCODED <--- ENCODER(INPUT)
input_encoded_m = input_encoder_m(input_sequence)
input_encoded_c = input_encoder_c(input_sequence)
question_encoded = question_encoder(question)


# %%
# Use a dot product to compute the match between the first input vector sequence and the query


# %%
# dot product computed match for the first input vector sequence and the query
match = dot([input_encoded_m, question_encoded], axes=(2,2))
match = Activation('softmax')(match)


# %%
# add this match matrix with the second input vector sequence
response = add([match, input_encoded_c])
response = Permute((2,1))(response) # to have an output of examples by querie max len, by story max len


# %%
# concatenate match matrix with the question vector sequence (Concatenate response with question)
answer = concatenate([response, question_encoded])


# %%
answer # The None is the batch_size that we did not define yet


# %%
# BUILD OUR MODEL: Reduce our answer with our current Neural Network


# %%
answer = LSTM(32)(answer)


# %%
answer = Dropout(0.5)(answer)
# this outputs something in the form of samples by the vocab size 
# we should only see a marking for YES or NO, everything else is just a bunch of 0.
# Just as we did when we vectorized the answers
answer = Dense(vocab_size)(answer) # (samples, vocab_size) # YES/NO 0000


# %%
# output the probability distribution over the vocabulary
# turn YES and NO into 0 and 1
answer = Activation('softmax')(answer)


# %%
# build the final model: Passing the PLACEHOLDERS
model = Model([input_sequence, question], answer)


# %%
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])


# %%
model.summary()


# %%
# Part 4: Fit/Train the network (the model)


# %%
history = model.fit(
    [inputs_train, queries_train],
    answers_train,
    batch_size=32, # smaller batch sizes with longer trained epochs slightly get better results
    epochs=10, validation_data=([inputs_test, queries_test], answers_test))


# %%
# Plotting out our training history


# %%
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
print(history.history.keys())


# %%
# summarize history for accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


# %%
# save this model
# model.save('mybrandnewmodel.h5')


# %%
# load model
model.load_weights('chatbot_10.h5')


# %%
pred_results = model.predict(([inputs_test, queries_test]))


# %%
test_data[0][0]


# %%
test_data[0][1]


# %%
test_data[0][2]


# %%
pred_results.shape # ([stories, questions, answer], vocab_words+1)


# %%
pred_results[0] # probability of every single vocab word


# %%
# get the max probability
val_max = np.argmax(pred_results[0])


# %%
# tokenizer.word_index
# np.argmax(pred_results[0])


# %%
# take the word from our vocabulary
for key, val in tokenizer.word_index.items():
    if val == val_max:
        k = key


# %%
k # this should be 'no', there is a mistake somewhere...


# %%
pred_results[0][val_max] 

# %% [markdown]
# ## Test our model

# %%
# This is our the vocabulary that our model knows, we can only use these words to ask questions to the model.
vocab


# %%
# Creating stories
my_story = "John left the kitchen . Sandra dropped the football in the garden ."


# %%
my_story.split()


# %%
my_question = "Is the football in the garden ?"


# %%
my_question.split()


# %%
mydata = [(my_story.split(), my_question.split(), 'yes')]


# %%
mydata


# %%
# vectorize data
my_story, my_ques, my_ans = vectorize_stories(mydata)


# %%
# my_story
# my_ques
# my_ans


# %%
# predict data with the model
pred_results = model.predict(([my_story, my_ques]))


# %%
# get the max value of the predicted results
val_max = np.argmax(pred_results[0])


# %%
for key, val in tokenizer.word_index.items():
    if val == val_max:
        k = key


# %%
k # this should be yes, there is a mistake somewhere...


# %%
pred_results[0][val_max]


# %%



