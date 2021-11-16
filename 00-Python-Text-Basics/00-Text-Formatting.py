# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
person = "Jose"


# %%
# before python 3.6
print("my name is {}".format(person))


# %%
# After python 3.6
print(f"my name is {person}")


# %%
d = {'a': 123, 'b': 456}


# %%
print(f"my number {d['a']}")


# %%
library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting in water alone', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]


# %%
library


# %%
for book in library:
    print(f"Author is {book[0]}")   


# %%
for author, topic, pages in library:
    print(f"{author:{10}} {topic:{30}} {pages:>{10}}")


# %%
from datetime import datetime


# %%
today = datetime(year=2020, month=1, day=12)


# %%
print(f"{today}")
#strftime.org
print(f"{today:%B, %d, %Y}")


# %%



