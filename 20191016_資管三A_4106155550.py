#!/usr/bin/env python
# coding: utf-8

# In[2]:


score = int(input('請輸入成績:'))

if score > 90:
    print('優等')
elif score >= 80 and score <= 90:
    print('甲等')
elif score >= 70 and score < 80:
    print('乙等')
elif score >= 60 and score < 70:
    print('丙等')
else:
    print('丁等')


# ## 實作練習一

# ## 實作練習二

# In[3]:


x = int(input('請輸入正整數'))

sum = 0
i = 1
for n in range(x):
    sum = sum + i
    i = i + 1

print(sum, end=" ")


# ## 實作練習五

# In[4]:


n = int(input('請輸入正整數'))
output = []
for i in range(n+1):
    if i % 5 != 0:
        output.append(i)
print([i for i in output])


# ## 實作練習六

# In[6]:


n = int(input('請輸入正整數'))
output = n

if n == 1:
    print(n)
else:
    while(n>=2):
        output = output * (n-1)
        n = n-1
    print(output)


# In[ ]:




