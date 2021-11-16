# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"phone" in text


# %%
# using reg exp
import re


# %%
pattern = "phone"


# %%
my_match = re.search(pattern, text)


# %%
my_match.span() # position of the found result


# %%
my_match.start()


# %%
my_match.end()


# %%
# another one
text = "my phone is a new phone"


# %%
match = re.search(pattern, text) # return the first matches


# %%
match.span()


# %%
all_matches = re.findall("phone", text) # return all matches


# %%
len(all_matches)


# %%
# get iteration of all the matches
for match in re.finditer("phone", text):
    print(match.span())


# %%
# reg expression pattern
text = "My telephone number is 777-555-1234"


# %%
pattern = r'\d\d\d-\d\d\d-\d\d\d\d'


# %%
phone_number = re.search(pattern, text)


# %%
phone_number


# %%
phone_number.group() # get value of the object


# %%
# pattern with quantifiers
pattern = r"\d{3}-\d{3}-\d{4}"


# %%
mymatch = re.search(pattern, text)


# %%
mymatch.group()


# %%



