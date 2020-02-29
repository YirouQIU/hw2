#!/usr/bin/env python
# coding: utf-8

# In[37]:


#1.Include a section with your name
#2.Create matrix A with size (3,5) containing random numbers 
import numpy as np
A = np.random.randint(0,100, size=(3, 5))
print (A)


# In[38]:


#3.Find the size and length of matrix A
A.size


# In[39]:


len(A)


# In[40]:


#4.Resize (crop/slice) matrix A to size (3,4)
A.resize((3,4))
print(A)


# In[42]:


#5.Resize (crop/slice) matrix A to size (3,4)
B=A.T
print(B)


# In[110]:


#6.Find the minimum value in column 1 of matrix B
print(B[::,1:2:])
print(B[::,0:1:].min())


# In[54]:


#7.Find the minimum and maximum values for the entire matrix A
print(A.min())


# In[56]:


print(A.max())


# In[63]:


#8.Create vector X (an array) with 4 random numbers
X=np.random.randint(0,100,4)
print(X)


# In[78]:


#9. Create a function and pass vector X and matrix A in it
def f(X,A):
    return np.dot(A,X.T)
#10.In the new function multiply vector X with matrix A and assign the result to D 
D=f(X,A)
print(D)


# In[87]:


#11.Create a complex number Z with absolute and real parts != 0
Z=8+6j
Z


# In[88]:


#12.Show its real and imaginary parts as well as it’s absolute value
Z.real


# In[89]:


Z.imag


# In[90]:


abs(Z)


# In[92]:


#13.Multiply result D with the absolute value of Z and record it to C
C=abs(Z)*D
print(C)


# In[96]:


#14.Convert matrix B from a matrix to a string and overwrite B
b=''
for i in range(0,B.shape[0]):
    for j in range(0,B.shape[1]-1):
        b+=str(B[i,j])+'\t'
    b+=str(B[i,-1])+'\n'
b


# In[98]:


str(B)


# In[109]:


#15.Display a text on the screen: ‘Name is done with HW2‘, but passs your ‘Name’ as a string variable
s = 'Yirou QIU'   
print("%s is done with HW2." % (s)) 

