
# coding: utf-8

# In[29]:

from pandas import Series, DataFrame
import pandas as pd
path='employee_compensation.csv'
df=pd.read_csv(path)


# In[2]:

df.head(5)


# In[33]:

df1 = pd.DataFrame()


# In[67]:

df1=df.groupby(['Year','Employee Identifier','Job Family']).agg({'Total Benefits':'mean',
                                      'Total Compensation': 'mean',
                                      'Overtime': 'sum',
                                      'Salaries':'sum'})
df1.head(5)


# In[68]:

df2 = pd.DataFrame()


# In[69]:

df2=df1[df1['Overtime']>df1['Salaries']*0.05]
df2.shape


# In[81]:

df2.head(5)


# In[82]:

pd.options.mode.chained_assignment = None
df2['Percentage']=(df2['Total Benefits']/df2['Total Compensation'])*100


# In[85]:

df2.reset_index().head(5)


# In[101]:

df3=pd.DataFrame()


# In[113]:

import numpy as np
df3= df2.reset_index().groupby(['Job Family','Year'])
type(df3)


# In[119]:

test=df3.aggregate(np.sum)
del test['Employee Identifier']
del test['Overtime']
del test['Salaries']
test.head(5)


# In[120]:

test.to_csv('Q2Part2.csv',encoding='utf-8')


# In[ ]:



