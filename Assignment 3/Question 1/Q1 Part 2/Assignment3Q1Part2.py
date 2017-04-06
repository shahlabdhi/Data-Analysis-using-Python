
# coding: utf-8

# In[38]:

from pandas import Series, DataFrame
import pandas as pd
path='vehicle_collisions.csv'
df=pd.read_csv(path)


# In[39]:

df.head(5)


# In[40]:

df = df.drop(['UNIQUE KEY','DATE','TIME','ZIP CODE','LATITUDE','LONGITUDE','LOCATION','ON STREET NAME','CROSS STREET NAME','OFF STREET NAME','PERSONS INJURED','PERSONS KILLED','PEDESTRIANS INJURED','PEDESTRIANS KILLED','CYCLISTS INJURED','CYCLISTS KILLED','MOTORISTS INJURED','MOTORISTS KILLED','VEHICLE 1 FACTOR','VEHICLE 2 FACTOR','VEHICLE 3 FACTOR','VEHICLE 4 FACTOR','VEHICLE 5 FACTOR'], axis = 1)


# In[41]:

df1=df.drop(['VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE'], axis = 1)
df1.fillna('NYC', inplace=True)


# In[42]:

vehicles_df = df.drop(['BOROUGH'], axis = 1)


# In[43]:

vehicles_df = vehicles_df.count(axis=1)


# In[44]:

df = pd.concat([df1, vehicles_df], axis=1)

df.columns.values[1]='TOTAL'

df.head(5)


# In[28]:

df1 = DataFrame({})
df1['ONE_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='QUEENS')&(df['TOTAL']==1)].count()
df1['TWO_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='QUEENS')&(df['TOTAL']==2)].count()
df1['THREE_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='QUEENS')&(df['TOTAL']==3)].count()
df1['MORE_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='QUEENS')&((df['TOTAL']>3)|(df['TOTAL']==0))].count()
df1.head(5)


# In[29]:


df1.index.values[1]='QUEENS'

df1=df1.drop('BOROUGH')
df1.head(5)


# In[56]:

df2 = DataFrame({})
df2['ONE_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='BRONX')&(df['TOTAL']==1)].count()
df2['TWO_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='BRONX')&(df['TOTAL']==2)].count()
df2['THREE_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='BRONX')&(df['TOTAL']==3)].count()
df2['MORE_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='BRONX')&((df['TOTAL']>3)|(df['TOTAL']==0))].count()
df2.index.values[1]='BRONX'
df2=df2.drop('BOROUGH')


df3 = DataFrame({})
df3['ONE_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='BROOKLYN')&(df['TOTAL']==1)].count()
df3['TWO_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='BROOKLYN')&(df['TOTAL']==2)].count()
df3['THREE_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='BROOKLYN')&(df['TOTAL']==3)].count()
df3['MORE_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='BROOKLYN')&((df['TOTAL']>3)|(df['TOTAL']==0))].count()
df3.index.values[1]='BROOKLYN'
df3=df3.drop('BOROUGH')

df4 = DataFrame({})
df4['ONE_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='MANHATTAN')&(df['TOTAL']==1)].count()
df4['TWO_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='MANHATTAN')&(df['TOTAL']==2)].count()
df4['THREE_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='MANHATTAN')&(df['TOTAL']==3)].count()
df4['MORE_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='MANHATTAN')&((df['TOTAL']>3)|(df['TOTAL']==0))].count()
df4.index.values[1]='MANHATTAN'
df4=df4.drop('BOROUGH')

df5 = DataFrame({})
df5['ONE_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='STATEN ISLAND')&(df['TOTAL']==1)].count()
df5['TWO_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='STATEN ISLAND')&(df['TOTAL']==2)].count()
df5['THREE_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='STATEN ISLAND')&(df['TOTAL']==3)].count()
df5['MORE_VEHICLE_INVOLVED'] = df[(df['BOROUGH']=='STATEN ISLAND')&((df['TOTAL']>3)|(df['TOTAL']==0))].count()
df5.index.values[1]='STATEN ISLAND'
df5=df5.drop('BOROUGH')


# In[50]:

df2.head(5)


# In[51]:

df3.head(5)


# In[52]:

df4.head(5)


# In[57]:

df5.head(4)


# In[85]:

df6=pd.concat([df1,df2,df3,df4,df5])


# In[86]:

df6.head(4)


# In[17]:

by_borough.count()


# In[87]:


df6=df6.dropna(how='all')
df6.head(5)


# In[88]:


df6.to_csv('Q1Part2.csv', encoding='utf-8')


# In[ ]:



