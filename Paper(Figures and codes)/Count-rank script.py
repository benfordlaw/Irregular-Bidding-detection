#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df= pd.read_csv("WV-ashpalt items.csv")


# In[3]:


#overusage of 1,7,8,9 in the first test
df1= df.loc[df['firstdigit']==1]
df7= df.loc[df['firstdigit']==7]
df8= df.loc[df['firstdigit']==8]
df9= df.loc[df['firstdigit']==9]


# In[4]:


result = [df1, df7, df8, df9]
results = pd.concat(result)


# In[5]:


results


# In[6]:


year_count = results.groupby('Year').nunique()


# In[7]:


year_count.sort_values('Unnamed: 0')


# In[8]:


county_count = results.groupby('counties').nunique()


# In[9]:


county_count.sort_values('Unnamed: 0')


# In[10]:


company_count = results.groupby('Vendor Name').nunique()


# In[11]:


company_count.sort_values('Unnamed: 0')


# In[12]:


item_count = results.groupby('Item Description').nunique()


# In[13]:


item_count.sort_values('Unnamed: 0')


# In[14]:


dff= pd.read_csv("WV-ashpalt items.csv")


# In[15]:


dff


# In[16]:


#overusage of 0,4,5in the first test
dff0= dff.loc[dff['seconddigit']==0]
dff4= dff.loc[dff['seconddigit']==4]
dff5= dff.loc[dff['seconddigit']==5]


# In[17]:


dff


# In[ ]:





# In[18]:


df1


# In[19]:


dff= pd.read_csv("WV-ashpalt items.csv")


# In[20]:


#overusage of 0,4,5 in the first test
dff0= dff.loc[dff['firstdigit']==0]
dff4= dff.loc[dff['firstdigit']==4]
dff5= dff.loc[dff['firstdigit']==5]


# In[21]:


result2 = [dff0, dff4, dff5]
results2 = pd.concat(result2)


# In[22]:


results2


# In[23]:


year_count2 = results2.groupby('Year').nunique()
year_count2.sort_values('Unnamed: 0')


# In[24]:


county_count2 = results2.groupby('counties').nunique()
county_count2.sort_values('Unnamed: 0')


# In[25]:


company_count2 = results2.groupby('Vendor Name').nunique()
company_count2.sort_values('Unnamed: 0')


# In[26]:


item_count2 = results2.groupby('Item Description').nunique()
item_count2.sort_values('Unnamed: 0')


# In[27]:


#overusage of 1,7,8,9 in the first test
dff11= dff.loc[df['firsttwo']==11]
dff13= dff.loc[df['firsttwo']==13]
dff15= dff.loc[df['firsttwo']==15]
dff18= dff.loc[df['firsttwo']==18]
dff36= dff.loc[df['firsttwo']==36]
dff60= dff.loc[df['firsttwo']==60]
dff70= dff.loc[df['firsttwo']==70]
dff72= dff.loc[df['firsttwo']==72]
dff75= dff.loc[df['firsttwo']==75]
dff84= dff.loc[df['firsttwo']==84]
dff90= dff.loc[df['firsttwo']==90]


# In[28]:


result3 = [dff11, dff13, dff15, dff18, dff36, dff60, dff70, dff72, dff75, dff84, dff90]
results3 = pd.concat(result3)


# In[29]:


results3


# In[30]:


year_count3 = results3.groupby('Year').nunique()
year_count3.sort_values('Unnamed: 0')


# In[31]:


county_count3 = results3.groupby('counties').nunique()
county_count3.sort_values('Unnamed: 0')


# In[32]:


company_count3 = results3.groupby('Vendor Name').nunique()
company_count3.sort_values('Unnamed: 0')


# In[33]:


item_count3 = results3.groupby('Item Description').nunique()
item_count3.sort_values('Unnamed: 0')


# In[ ]:




