#!/usr/bin/env python
# coding: utf-8

# # Analyzing Data 

# ## Prison Helicopter Escapes

# We begin by importing some helper functions.

# In[39]:


from helper import *


# ## Get the Data

# Now, let's get the data from the [List of helicopter prison escapes](https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes) Wikipedia article.

# In[40]:


url = ('https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes')
data = data_from_url(url)


# In[41]:


index = 0
for row in data:
    data[index] = row[:-1]
    index += 1


# Let's print the first three rows

# In[42]:


for row in data[:3]:
    print(row)


# In[43]:


for row in data:
    date = fetch_year(row[0])
    row[0] = date


# In[44]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]


# In[45]:



years = []

for year in range(min_year, max_year + 1):
    years.append(year)


# In[46]:


attempts_per_year = []
for year in years:
    attempts_per_year.append([year, 0])
    


# In[47]:


for row in data:
    for year_attempt in attempts_per_year:
        year = year_attempt[0]
        if row[0] == year:
            year_attempt[1] += 1
            
print(attempts_per_year)    


# ## In which year did the most attempts at breaking out of prison with a helicopter occur?

# In[49]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)
print(attempts_per_year)


# The following code will present the amount of attempts by country in a table format

# In[48]:


countries_frequency = df["Country"].value_counts()

print_pretty_table(countries_frequency)


# In[ ]:




