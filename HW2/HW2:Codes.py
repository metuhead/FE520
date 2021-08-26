#!/usr/bin/env python
# coding: utf-8

# # Q1

# In[ ]:


def Ball_Drop(Heights, drop_num=5):
    # modify this function

    
    total=0
    drop_num=drop_num*2

    for i in range(drop_num):
   
        total+=Heights
        if i%2==0:
            Heights=Heights/4


    return(total)


# # Q2

# In[ ]:


import string
import collections



def Get_Token(Given_str_1):
    # modify this function

    idoms = Given_str_1.split()
    reccur = collections.defaultdict(int)

    for idom in idoms:
        # remove punctuation
        for c in string.punctuation:
            idom = idom.replace(c, "")
        idom = idom.lower()
        reccur[idom] += 1

    return dict(reccur)


# # Q3

# In[ ]:


def Step_2_Fibo(Given_num, isIncrement=True):
    # modify this function
    
    li=[]
    count=0

    for item in range(33):
    
        if item>=2:
            fib=li[count]+li[count+1]
            count+=1
        else:
            fib=item
        
        li.append(fib)
 

    #print(li)

   
    if isIncrement is True:
        if Given_num  in  li:
            return(0)
        else:
            value=0
            for i in li:
                #value=0
                 if i-Given_num>0:
                    return(i-Given_num) 
                    break
                 value+=1
            #print(li[value])
    #if Increment== False:
    else:
        if Given_num in li:
            return(0)            
            
        else:
            value=0
            for i in li:
                if Given_num-i<0:
                    return(Given_num-li[value-1])
                    break
                value+=1

    
    
    
    
    


# # Q4

# In[ ]:


def identi_Substring(x):
    # modify this function
    
    length = len(x)
    if length == 0:
        print(0)

    count = 0

    i, j = 0, 1
    while j < length:
        if x[i] == x[j]:
            j += 1
        else:
            diff = j - i
            count += (diff * (diff + 1)) / 2
            i, j = j, j + 1

    value = length - i
    count=count + (value * (value + 1)) / 2
    return int(count)

    

