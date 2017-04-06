
# coding: utf-8

# In[1]:

from pandas import Series, DataFrame
import pandas as pd
path='cricket_matches.csv'
df=pd.read_csv(path)


# In[2]:

df.head(5)


# In[4]:

df1=pd.DataFrame()
df1=df[(df['home']==df['winner'])]


# In[5]:

df1


# In[15]:

pd.options.mode.chained_assignment = None
import numpy as np
df1['Total Score']=np.where((df1['home']==df1['innings1']), df1['innings1_runs'],df1['innings2_runs'])


# In[16]:

df1.head(5)


# In[25]:

by_team=df1.groupby('home')
df2=pd.DataFrame()
df2=(by_team.mean()['Total Score']).to_frame()
df2.head(5)


# In[26]:

df2.to_csv('Q3_Part1.csv', encoding='utf-8')


# In[ ]:



