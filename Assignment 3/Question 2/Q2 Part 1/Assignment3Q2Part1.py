
# coding: utf-8

# In[1]:

from pandas import Series, DataFrame
import pandas as pd
path='employee_compensation.csv'
df=pd.read_csv(path)


# In[2]:

df.head(5)


# In[2]:

by_org = df.groupby(['Organization Group','Department'])
by_org


# In[3]:

df1=pd.DataFrame()


# In[4]:

df1=(by_org.mean()['Total Compensation']).to_frame()


# In[18]:

df1


# In[20]:

df1.to_csv('Q2_Part1.csv', encoding='utf-8')


# In[19]:

type(df1)

