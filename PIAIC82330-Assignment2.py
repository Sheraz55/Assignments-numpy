#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
x1=np.arange(1,13).reshape((6,2)) # task 1


# In[2]:


x2=np.arange(10,37).reshape(3,3,3)
dtype=np.float64


# In[3]:


x3 = np.arange(1, 100*10+1).reshape((100,10))
X3=x3[(x3%5 == 0) & (x3%7 == 0)]


# In[22]:


x4=np.arange(9).reshape(3,3)
x4[:,[0,1]]=x4[:,[1,0]]


# In[5]:


x5=np.zeros(20).reshape(4,5)


# In[6]:


x6=np.zeros(10)
x6[5]=10
x6[8]=20


# In[7]:


a = np.arange(4, dtype=np.int64)
x7 = np.zeros(4)
x7.dtype=np.int64


# In[8]:


x8=np.full(10,6).reshape(2,5)
x8.dtype=np.uint32


# In[53]:


x9=np.arange(1,101)
x9[x9%2==0]


# In[31]:


x10 = np.array([[3,3,3],[4,4,4],[5,5,5]])
X10= np.array([1,2,3])
y10=x10-(X10[0])
y10


# In[23]:


x11=np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
x11[x11%2==1] = -1


# In[52]:


x12 = np.array([1,2,3])
y12 = np.array([1,2,3])
np.concatenate((x12,y12),None)


# In[24]:


x13=  np.array([2, 6, 1, 9, 10, 3, 27])
X13=x13[(x13>5) & (x13<10)]


# In[11]:


x14=  np.arange(10,34)
np.split(x14.reshape(8,3),4)


# In[56]:


x15 = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
x15[[0, 1, 2], :] = x15[[1, 0, 2], :]


# In[26]:


x16 = np.array([[1], [2], [3]])
X16 = np.array([[2], [3], [4]])
np.hstack([x16,X16])


# In[32]:


x17 = np.arange(1,10*10+1).reshape((10,10))
np.where((x17%3 ==0)&(x17%5),"YES","NO")


# In[34]:


piaic = np.arange(100)
students = np.array([5,20,50,200,301,7001])
len(set(piaic)&set(students))


# In[46]:


X=np.arange(1,26).reshape(5,5)
W=X.copy()
W=X.T
b = 5
(W*X)+b


# In[51]:


x = np.arange(1,11)
x20=x*2+3-2
x20


# In[ ]:




