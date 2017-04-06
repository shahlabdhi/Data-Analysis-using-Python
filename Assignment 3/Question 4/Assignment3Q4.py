
# coding: utf-8

# In[6]:

from pandas import Series, DataFrame
import pandas as pd
path='movies_awards.csv'
df1=pd.read_csv(path,dtype='object')


# In[7]:

df1.head(5)


# In[8]:

type(df1['Awards'])


# In[11]:

df=df1.dropna()


# In[12]:

df['Awards Wins'] = df['Awards'].str.extract('(\d+ win)', expand=True)
df['Awards Nominated'] = df['Awards'].str.extract('(\d+ nomination)', expand=True)
df['Primetime Emmys Wins'] = df['Awards'].str.extract('(Won \d+ Primetime Emmy)', expand=True)
df['Primetime Emmys Nominations'] = df['Awards'].str.extract('(Nominated for \d+ Primetime Emmy)', expand=True)
df['Oscar Nominations'] = df['Awards'].str.extract('(Nominated for \d+ Oscar)', expand=True)
df['Oscar Wins'] = df['Awards'].str.extract('(Won \d+ Oscar)', expand=True)
df['Golden Globe Nominations'] = df['Awards'].str.extract('(Nominated for \d+ Golden Globe)', expand=True)
df['Golden Globe Wins'] = df['Awards'].str.extract('(Won \d+ Golden Globe)', expand=True)
df['BAFTA Nominations'] = df['Awards'].str.extract('(Nominated for \d+ BAFTA)', expand=True)
df['BAFTA Wins'] = df['Awards'].str.extract('(Won \d+ BAFTA)', expand=True)


# In[13]:

df['Awards Wins'] = df['Awards Wins'].str.extract('(\d+)')
df['Awards Nominated'] = df['Awards Nominated'].str.extract('(\d+)')
df['Oscar Nominations'] = df['Oscar Nominations'].str.extract('(\d+)')
df['Oscar Wins'] = df['Oscar Wins'].str.extract('(\d+)')
df['Primetime Emmys Nominations'] = df['Primetime Emmys Nominations'].str.extract('(\d+)')
df['Primetime Emmys Wins'] = df['Primetime Emmys Wins'].str.extract('(\d+)')
df['Golden Globe Nominations'] = df['Golden Globe Nominations'].str.extract('(\d+)')
df['Golden Globe Wins'] = df['Golden Globe Wins'].str.extract('(\d+)')
df['BAFTA Nominations'] = df['BAFTA Nominations'].str.extract('(\d+)')
df['BAFTA Wins'] = df['BAFTA Wins'].str.extract('(\d+)')


# In[14]:

df['Awards Wins'] = df['Awards Wins'].fillna(0)
df['Awards Nominated'] = df['Awards Nominated'].fillna(0)
df['Primetime Emmys Nominations'] = df['Primetime Emmys Nominations'].fillna(0)
df['Primetime Emmys Wins'] = df['Primetime Emmys Wins'].fillna(0)
df['Oscar Nominations'] = df['Oscar Nominations'].fillna(0)
df['Oscar Wins'] = df['Oscar Wins'].fillna(0)
df['Golden Globe Nominations'] = df['Golden Globe Nominations'].fillna(0)
df['Golden Globe Wins'] = df['Golden Globe Wins'].fillna(0)
df['BAFTA Nominations'] = df['BAFTA Nominations'].fillna(0)
df['BAFTA Wins'] = df['BAFTA Wins'].fillna(0)


# In[15]:

df['Awards Nominated'] = df['Awards Nominated'].astype(int)
df['Awards Wins'] = df['Awards Wins'].astype(int)
df['Oscar Nominations'] = df['Oscar Nominations'].astype(int)
df['Oscar Wins'] = df['Oscar Wins'].astype(int)
df['Primetime Emmys Nominations'] = df['Primetime Emmys Nominations'].astype(int)
df['Primetime Emmys Wins'] = df['Primetime Emmys Wins'].astype(int)
df['Golden Globe Nominations'] = df['Golden Globe Nominations'].astype(int)
df['Golden Globe Wins'] = df['Golden Globe Wins'].astype(int)
df['BAFTA Nominations'] = df['BAFTA Nominations'].astype(int)
df['BAFTA Wins'] = df['BAFTA Wins'].astype(int)


# In[16]:

df['Awards Nominated'] = df['Awards Nominated'] + df['Oscar Nominations'] + df['Primetime Emmys Nominations'] + df['Golden Globe Nominations'] + df['BAFTA Nominations']
df['Awards Wins'] = df['Awards Wins'] + df['Oscar Wins'] + df['Primetime Emmys Wins'] + df['Golden Globe Wins'] + df['BAFTA Wins']


# In[18]:

columns = ['Awards','Awards Nominations','Awards Wins','Oscar Nominations','Oscar Wins','Primetime Emmys Nominations','Primetime Emmys Wins','Golden Globe Nominations','Golden Globe Wins','BAFTA Nominations','BAFTA Wins']
df.head(5)


# In[19]:

df.to_csv('Q4_Part_1.csv',encoding='utf-8')


# In[ ]:



