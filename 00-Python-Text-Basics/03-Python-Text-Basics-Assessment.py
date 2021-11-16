# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# %% [markdown]
# # Python Text Basics Assessment
# 
# Welcome to your assessment! Complete the tasks described in bold below by typing the relevant code in the cells.<br>
# You can compare your answers to the Solutions notebook provided in this folder.
# %% [markdown]
# ## f-Strings
# #### 1. Print an f-string that displays `NLP stands for Natural Language Processing` using the variables provided.

# %%
abbr = 'NLP'
full_text = 'Natural Language Processing'

# Enter your code here:
print(f'{abbr} stands for {full_text}')

# %% [markdown]
# ## Files
# #### 2. Create a file in the current working directory called `contacts.txt` by running the cell below:

# %%
get_ipython().run_cell_magic('writefile', 'contacts.txt', 'Hello, this is a contacts file')

# %% [markdown]
# #### 3. Open the file and use .read() to save the contents of the file to a string called `fields`.  Make sure the file is closed at the end.

# %%
# Write your code here:
with open('contacts.txt') as contacts:
    fields = contacts.read()


# %%
# Run fields to see the contents of contacts.txt:
fields

# %% [markdown]
# ## Working with PDF Files
# #### 4. Use PyPDF2 to open the file `Business_Proposal.pdf`. Extract the text of page 2.

# %%
# Perform import
import PyPDF2

# Open the file as a binary object
file = open('Business_Proposal.pdf', 'rb')

# Use PyPDF2 to read the text of the file
pdf_reader = PyPDF2.PdfFileReader(file)


# Get the text from page 2 (CHALLENGE: Do this in one step!)
page_two_text = pdf_reader.getPage(1).extractText()

# Close the file
file.close()

# Print the contents of page_two_text
print(page_two_text)

# %% [markdown]
# #### 5. Open the file `contacts.txt` in append mode. Add the text of page 2 from above to `contacts.txt`.
# 
# #### CHALLENGE: See if you can remove the word "AUTHORS:"

# %%
# Simple Solution:
with open('contacts.txt', 'a+') as file:
    # remove AUTHORS (see also another way in the next cell)
    cleaned_text = page_two_text.replace("AUTHORS:", "")
    file.write(cleaned_text)
    file.seek(0)
    print(file.read())



# %%
# CHALLENGE Solution (re-run the %%writefile cell above to obtain an unmodified contacts.txt file):
with open('contacts.txt', 'a+') as contacts:
    contacts.write(page_two_text[8:])
    contacts.seek(0)
    print(contacts.read())


# %% [markdown]
# ## Regular Expressions
# #### 6. Using the `page_two_text` variable created above, extract any email addresses that were contained in the file `Business_Proposal.pdf`.

# %%
import re

# Enter your regex pattern here. This may take several tries!
# pattern = r"\w{1,}@\w{1,}.\w{3}" # abel's solution
pattern = r"[\w]+@[\w]+.\w{3}" # author's solution

re.findall(pattern, page_two_text)

# %% [markdown]
# ### Great job!

