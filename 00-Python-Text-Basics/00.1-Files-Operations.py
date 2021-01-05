# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%



# %%
get_ipython().run_cell_magic('writefile', 'test.txt', 'Hello, this is a quick test file.\nThis is the second line of the file.')


# %%
myfile = open('whoops.txt')


# %%
pwd


# %%
myfile = open('test.txt')


# %%
myfile

# %% [markdown]
# Alternatively, to grab files from any location on your computer, simply pass in the entire file path.
# 
# For Windows you need to use double \ so python doesn't treat the second \ as an escape character, a file path is in the form:
# 
#     myfile = open("C:\\Users\\YourUserName\\Home\\Folder\\myfile.txt")
# 
# For MacOS and Linux you use slashes in the opposite direction:
# 
#     myfile = open("/Users/YourUserName/Folder/myfile.txt")

# %%
myfile.read()


# %%
myfile.read()


# %%
myfile.seek(0) # restarting the cursor of the file to the beggining


# %%
myfile.read()


# %%
myfile.seek(0)


# %%
content = myfile.read()


# %%
content


# %%
print(content)


# %%
myfile.close()


# %%
###### readlines
myfile = open('test.txt')


# %%
myfile.readlines() # read each line into an array


# %%
myfile.seek(0)


# %%
mylines = myfile.readlines()


# %%
for line in mylines:
    print(line.split()[0])


# %%
#### write files
myfile = open('test.txt', 'w+')


# %%
myfile.read()


# %%
myfile.write('My brand new text')


# %%
myfile.seek(0)


# %%
myfile.read()


# %%
myfile.close()


# %%
#### append to a file
myfile = open('whoops.txt', 'a+')


# %%
myfile.write('MY FIRST LINE IN A+ OPENING')


# %%
myfile.close()


# %%
newfile = open('whoops.txt')


# %%
newfile.read()


# %%
newfile.write('try to write something with only read permissions')


# %%
newfile.close()


# %%
myfile = open('whoops.txt', mode='a+')


# %%
myfile.write('This is an added line, because I used a+ mode')


# %%
myfile.seek(0)


# %%
myfile.read()


# %%
myfile.write('\nThis is a real new line, on the next line')


# %%
myfile.seek(0)


# %%
myfile.read()


# %%
myfile.seek(0)


# %%
print(myfile.read())


# %%
myfile.close()


# %%
# this will close the file automatically for you
with open('whoops.txt', 'r') as mynewfile:
    myvariable = mynewfile.readlines()


# %%
myvariable


# %%



