#!/usr/bin/env python
# coding: utf-8

# # Numpy Tutorials
# NumPy is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python
# 
# ### What is an array
# An array is a data structure that stores values of same data type. In Python, this is the main difference between arrays and lists. While python lists can contain values corresponding to different data types, arrays in python can only contain values corresponding to same data type

# In[2]:


import numpy as np


# In[3]:


my_lst = [1,2,3,4,5,6]


# In[4]:


arr = np.array(my_lst)


# In[5]:


arr


# In[6]:


type(arr)


# In[92]:


arr.shape


# In[38]:


## Multinested array
my_lst1=[1,2,3,4,5]
my_lst2=[2,3,4,5,6]
my_lst3=[9,7,6,8,9]

ar=np.array([my_lst1,my_lst2,my_lst3])


# In[50]:


ar


# In[52]:


type(ar)
ar.shape


# In[93]:


abc = np.array([1,2,3,4])
abc


# In[96]:


xyz = np.array([[[1,2,3],[4,5,6]],[[2,3,4],[5,6,7]]])
xyz


# In[41]:


arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr1


# In[94]:


arr1.shape


# In[101]:


ar.reshape(5, 3)


# ## Indexing

# In[43]:


## Accessing the elements in an array

arr2 = np.array([1,2,3,4,5])


# In[102]:


# as we know that array count starts with zero
arr2[0]


# In[45]:


ar


# In[54]:


ar[0:,:2]


# In[55]:


ar[1:,:2]


# In[56]:


ar[:,3:]


# In[57]:



arr


# In[59]:


arr[3:] = 100
arr


# In[76]:


## how to apply condition in eda

val = 2
arr<2


# In[78]:


arr[arr<3]


# In[114]:


arr4= np.arange(0,100, step= 4)
arr4


# In[111]:


np.linspace(1,10,20)


# In[109]:


## create array and reshape

x = np.arange(10,20)
x


# In[110]:


x.reshape(5,2)


# In[118]:


x1= np.arange(0,10).reshape(2,5)
x1


# In[119]:


x2= np.arange(10,20).reshape(2,5)
x2


# In[117]:


x1+x2


# In[116]:


x1*x2


# In[121]:


z = np.ones(8)
z


# In[130]:


np.ones((4,9,5), dtype=int)


# In[90]:


np.ones((2,5),dtype=int)


# In[91]:


## random distribution
np.random.rand(3,3)


# In[ ]:




