#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_csv("auto_data.csv")
df


# In[4]:


df.info()


# In[6]:


df.head()


# In[10]:


df.tail(5)


# In[15]:


import pandas as pd

correlation_var = df.corr()

print(correlation_var)


# In[17]:


import pandas as pd
mean=df.mean()
print(mean)


# In[7]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("auto_data.csv")
numeric_columns = ['mpg', 'cylinders', 'displacement', 'weight', 'acceleration']
mean_value=df[numeric_columns].mean()
plt.figure(figsize=(10,6))
sns.violinplot(data=df[numeric_columns],palette='Set3')
plt.title("Violinplot of Numeric_Columns")
plt.show()







# In[7]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("auto_data.csv")
numeric_columns = ['mpg', 'cylinders', 'displacement', 'weight', 'acceleration']
mean_value=df[numeric_columns].mean()

sns.boxplot(data=df[numeric_columns],palette='Set3')
plt.title('Box Plot of Numeric Columns')
plt.show()


# In[8]:


import matplotlib.pyplot as plt
numeric_columns = ['mpg', 'cylinders', 'displacement', 'weight', 'acceleration']
mean_value=df[numeric_columns].mean()
plt.figure(figsize=(10,6))
mean_value.plot(kind='bar' , color='blue')
plt.xlabel('columns')
plt.ylabel('mean')
plt.title('Mean Values of Numeric Columns')
plt.show()


# In[5]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("auto_data.csv")
numeric_columns = ['mpg', 'cylinders', 'displacement', 'weight', 'acceleration']
mean_value=df[numeric_columns].mean()
plt.figure(figsize=(10,6))
mean_value.plot(kind='line',color='blue')
plt.title("Lineplot of Mean_value")
plt.show()


# In[15]:


import seaborn as sns
pair_columns=['mpg','origin','weight']
sns.pairplot(data=df[pair_columns],hue='origin',height=4)
plt.title("pairplot of pair_columns")
plt.grid(True)
plt.show()


# In[31]:


import pandas as pd
df['horsepower']=pd.to_numeric(df['horsepower'],errors='coerce')
filtered_df=df[(df['acceleration']>15)&(df['horsepower']<170)]
names=filtered_df['name']
print(names)


# In[44]:


import pandas as pd
df=pd.read_csv("auto_data.csv")
count=df.groupby("cylinders").size()
print(count)


# In[50]:


import pandas as pd
df=pd.read_csv("auto_data.csv")
vehical_count=df.groupby('model_year').size()
print(vehical_count)

