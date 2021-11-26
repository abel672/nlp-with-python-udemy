# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# %% [markdown]
# # Sentiment Analysis Assessment - Solution
# 
# ## Task #1: Perform vector arithmetic on your own words
# Write code that evaluates vector arithmetic on your own set of related words. The goal is to come as close to an expected word as possible. Please feel free to share success stories in the Q&A Forum for this section!

# %%
# Import spaCy and load the language library. Remember to use a larger model!
import spacy


# %%
nlp = spacy.load('en_core_web_lg')


# %%
# Choose the words you wish to compare, and obtain their vectors
fighter = nlp.vocab['fighter'].vector 
villain = nlp.vocab['villain'].vector 
hero = nlp.vocab['hero'].vector 


# %%
# Import spatial and define a cosine_similarity function
from scipy import spatial

cosine_similarity = lambda x, y: 1 - spatial.distance.cosine(x, y)


# %%
# Write an expression for vector arithmetic
# For example: new_vector = word1 - word2 + word3
new_vector = fighter - villain + hero


# %%
new_vector.shape


# %%
# List the top ten closest vectors in the vocabulary to the result of the expression above

computed_similarities = []

for word in nlp.vocab:
    if word.has_vector:
        if word.is_lower:
            if word.is_alpha:
                similarity = cosine_similarity(new_vector, word.vector)
                computed_similarities.append((word, similarity))


# %%
# print(computed_similarities[0])

# sorting by similarity
computed_similarities = sorted(computed_similarities, key=lambda item:-item[1])

ten_closest_words = [t[0].text for t in computed_similarities[:10]]
print(ten_closest_words)

# %% [markdown]
# #### CHALLENGE: Write a function that takes in 3 strings, performs a-b+c arithmetic, and returns a top-ten result

# %%
def vector_math(a,b,c):
    word1 = nlp.vocab[a].vector
    word2 = nlp.vocab[b].vector
    word3 = nlp.vocab[c].vector

    new_vector = word1 + word2 - word3
    computed_similarities = []

    for word in nlp.vocab:
        if word.has_vector:
            if word.is_lower:
                if word.is_alpha:
                    similarity = cosine_similarity(new_vector, word.vector)
                    computed_similarities.append((word, similarity))
    
    # sort
    computed_similarities = sorted(computed_similarities, key=lambda item: -item[1])

    return [t[0].text for t in computed_similarities[:10]]    


# %%
# Test the function on known words:
vector_math('king','man','woman')

# %% [markdown]
# ## Task #2: Perform VADER Sentiment Analysis on your own review
# Write code that returns a set of SentimentIntensityAnalyzer polarity scores based on your own written review.

# %%
# Import SentimentIntensityAnalyzer and create an sid object

# import nltk
# nltk.download('vader_lexicon') # if you downloaded vader already you can skip this

from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()


# %%
# Write a review as one continuous string (multiple sentences are ok)
review = 'I really like this course of NLP!!. Is super cool, the content is very well explained.'


# %%
# Obtain the sid scores for your review
sid.polarity_scores(review)

# %% [markdown]
# ### CHALLENGE: Write a function that takes in a review and returns a score of "Positive", "Negative" or "Neutral"

# %%
def review_rating(string):
    get_value = lambda score: 'Positive' if score['compound'] > 0 else 'Negative' if score['compound'] < 0 else 'Neutral'

    return get_value(sid.polarity_scores(review))


# %%
# Test the function on your review above:
review_rating(review)

# %% [markdown]
# ## Great job!

