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
# part 2: Create our data (X, y)
from keras.utils import to_categorical


# %%
sequences[:, :-1] # each row of words (features)


# %%
sequences[:,-1] # last word of each row (label)


# %%
X = sequences[:, :-1] # features


# %%
y = sequences[:,-1] # label


# %%
y = to_categorical(y, num_classes=vocabulary_size+1)


# %%
X.shape # (sequences, words per sequence)


# %%
seq_len = X.shape[1]


# %%
# Create our model with the data
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding # LSTM: For the sequences, Embedding: for the words


# %%
# function to create models
def create_model(vocabulary_size, seq_len):

    model = Sequential()

    model.add(Embedding(vocabulary_size, seq_len, input_length=seq_len))
    # LSTM layer chooses amount of neurons, recommended to have as amount a multiple of seq_len
    model.add(LSTM(seq_len*2, return_sequences=True)) # first param should be multiple of seq_len (Recomended)
    model.add(LSTM(seq_len*2))

    model.add(Dense(50, activation='relu'))
    model.add(Dense(vocabulary_size, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.summary()

    return model


# %%
model = create_model(vocabulary_size+1, seq_len) # creating our model


# %%
# training our model


# %%
# to save files for later and load them
from pickle import dump, load


# %%
model.fit(
    X, y,
    batch_size=128, # how many sequences do you want to pass at a time
    epochs=2, # number of tranings in the execution
    verbose=1 # output report
)


# %%
# saving our model
model.save('my_mobydick_model.h5')


# %%
# tokenizer from Keras with all the vocabsulary of the documents
dump(tokenizer,open('my_simpletokenizer','wb')) # saving our token


# %%
# part 3: Generate the next sequence of words by predictions
from keras.preprocessing.sequence import pad_sequences


# %%
def generate_text(model, tokenizer, seq_len, seed_text, num_gen_words):

    output_text = []

    input_text = seed_text

    for i in range(num_gen_words):

        # take input text and encode it to be a sequence
        encoded_text = tokenizer.texts_to_sequences([input_text])[0] 

        # pad the text: in case that is too long or too short, we adapt it   
        pad_encoded = pad_sequences([encoded_text], maxlen=seq_len, truncating='pre')

        #  predict the class probabilities for each word
        # this method will throw the entire vocabulary and asign a probability to the most likely next word
        pred_word_ind = model.predict_classes(pad_encoded, verbose=0)[0]
  
        # get the actual matched word
        pred_word = tokenizer.index_word[pred_word_ind]

        # add the predicted word in the original input text
        input_text += ' '+pred_word

        # adding the predicted word into the list
        output_text.append(pred_word)
    
    # return all the predicted words
    return ' '.join(output_text)


# %%
# text_sequences[0]


# %%
import random
random.seed(101)
random_pick = random.randint(0, len(text_sequences))


# %%
random_seed_text = text_sequences[random_pick]


# %%
random_seed_text


# %%
seed_text = ' '.join(random_seed_text)


# %%
seed_text


# %%
generate_text(model, tokenizer, seq_len, seed_text, num_gen_words=25)


# %%
# load example model with 60% accuracy
from keras.models import load_model


# %%
model = load_model('epochBIG.h5')


# %%
tokenizer = load(open('epochBIG', 'rb'))


# %%
generate_text(model, tokenizer, seq_len, seed_text, num_gen_words=25)


# %%


