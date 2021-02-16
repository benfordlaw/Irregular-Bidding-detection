#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df= pd.read_excel('WV_2020.xlsx')


# In[3]:


dff= df[['Extension']]


# In[4]:


dff


# In[5]:


dff2= dff.describe()


# In[6]:


dff2


# In[7]:


dff3= dff.mode()


# In[8]:


dff3


# In[ ]:




