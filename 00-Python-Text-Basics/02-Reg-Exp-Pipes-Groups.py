# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
# using reg exp
import re


# %%
# reg expression pattern
text = "My telephone number is 777-555-1234"

# %%
# using groups
pattern = r"(\d{3})-(\d{3})-(\d{4})"

# %%
mymatch = re.search(pattern, text)


# %%
mymatch.group(1)


# %%
# pipe pattern
re.search(r"man|woman", "This man was here")


# %%
# while card
re.findall(r".at", "The cat in the hat sat")


# %%
# end with
re.findall(r"\d$", "This ends with a number 2")


# %%
# starts with
re.findall(r"^\d", "1 is the lonliest number")


# %%
phrase = "there are 3 numbers 34 inside 5 this sentence"


# %%
# exclusion
re.findall(r"[^\d]", phrase) # exclude any digit


# %%
# exclusion + inclusion
re.findall(r"[^\d]+", phrase) # include everyting that is not a digit


# %%
test_phrase = "This is a string! but it has punctuation. How to remove it?"


# %%
# exclude characters
re.findall(r"[^!.? ]+", test_phrase) # include everything that is not excluded


# %%
mylist = re.findall(r"[^!.? ]+", test_phrase) 
' '.join(mylist)


# %%
# get any number/alphanumerics separate with '-'
re.findall(r'[\w]+-[\w]+', text)


# %%



