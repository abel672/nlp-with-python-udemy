# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import PyPDF2


# %%
# read binary mode
myfile = open('US_Declaration.pdf', 'rb')


# %%
pdf_reader = PyPDF2.PdfFileReader(myfile)


# %%
pdf_reader.numPages


# %%
page_one = pdf_reader.getPage(0)


# %%
mytext = page_one.extractText()


# %%
myfile.close()


# %%
print(mytext)


# %%
# adding a page into the pdf
f = open('US_Declaration.pdf', 'rb')


# %%
pdf_reader = PyPDF2.PdfFileReader(f)


# %%
first_page = pdf_reader.getPage(0)


# %%
pdf_writer = PyPDF2.PdfFileWriter()


# %%
pdf_writer.addPage(first_page)


# %%
# write binary (to write pdf files)
pdf_output = open('MY_BRAND_NEW.pdf', 'wb')


# %%
pdf_writer.write(pdf_output)


# %%
pdf_output.close()


# %%
f.close()


# %%



# %%
# read the new created pdf
brand_new = open('MY_BRAND_NEW.pdf', 'rb')

pdf_reader = PyPDF2.PdfFileReader(brand_new)


# %%
pdf_reader.numPages


# %%
# grabing all the text from a pdf file
f = open('US_Declaration.pdf', 'rb')

pdf_text = [] # create an empty list

pdf_reader = PyPDF2.PdfFileReader(f)

for p in range(pdf_reader.numPages):

    page = pdf_reader.getPage(p)

    pdf_text.append(page.extractText())

f.close()


# %%
pdf_text


# %%
len(pdf_text)


# %%
# printing all the pages
for page in pdf_text:
    print(page)
    print('\t')
    print('\t')
    print('\t')
    print('\t')
    print('\t')


# %%



