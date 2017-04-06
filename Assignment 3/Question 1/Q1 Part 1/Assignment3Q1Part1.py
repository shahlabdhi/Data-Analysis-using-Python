
# coding: utf-8

# In[38]:

from pandas import Series, DataFrame
import pandas as pd
path='vehicle_collisions.csv'
df=pd.read_csv(path,parse_dates=['DATE'], usecols=[0,1,3])


# In[39]:

df.head(5)


# In[40]:

df.shape


# In[45]:

df=df.fillna('NYC')


# In[46]:

df.head(5)


# In[56]:

pd.options.mode.chained_assignment = None
yr = df[df.DATE.dt.year == 2016]


# In[57]:

yr['Month'] = yr['DATE'].dt.strftime('%b')


# In[58]:

NYC = yr['UNIQUE KEY'].groupby(yr['Month']).count()


# In[53]:

NYC.index = pd.CategoricalIndex(NYC.index, 
                               categories=['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'], 
                               sorted=True)
NYC = NYC.sort_index()
Manhattan = yr['UNIQUE KEY'][Year['BOROUGH'] == "MANHATTAN"].groupby(yr['Month']).count()
Manhattan.index = pd.CategoricalIndex(Manhattan.index, 
                               categories=['Jan', 'Feb', 'Mar', 'Apr','May','Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec'], 
                               sorted=True)
Manhattan = Manhattan.sort_index()


# In[54]:

Columns = ["Month", "Manhattan", "NYC", "Percentage"]
dataFrame = pd.DataFrame({'Month' : NYC.index, 'Manhattan' : Manhattan, 'NYC' : NYC, 'Percentage' : Manhattan / NYC})


# In[55]:

dataFrame[Columns].to_csv('Q1Part1.csv', index=False, encoding='utf-8')


# In[ ]:



