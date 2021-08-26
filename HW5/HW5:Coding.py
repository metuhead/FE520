#!/usr/bin/env python
# coding: utf-8

# # Q1

# In[ ]:


#Importing necessary packages
import pandas as pd
import numpy as np
from datetime import datetime


# In[ ]:


#Importing dataset

df_Energy=pd.read_excel("/Users/metuhead/Desktop/FE 520-Python/Assignments/HW5/Assignment5_data/Energy.xlsx")


# In[ ]:


#Showing dataset
df_Energy


# In[ ]:


#Creating a function to split the dataset

def split(EndYear,StartYear=2012):
    
    import pandas as pd
    import numpy as np
    from datetime import datetime

    #Importing dataset
    df_Energy=pd.read_excel("/Users/metuhead/Desktop/FE 520-Python/Assignments/HW5/Assignment5_data/Energy.xlsx")

    
 
    # Only selecting columns form "Accumulated Other Comprehensive Income (Loss)" to 
    # "Selling, General and Administrative Expenses"]

    df_Selected=df_Energy.loc[:,"Accumulated Other Comprehensive Income (Loss)": "Selling, General and Administrative Expenses"]
    #df_Selected
    # Creating a data frame only includes  columns
    df_Dates=df_Energy.loc[:,"Data Date":"Fiscal Year"]
    #df_Dates
    
    # Joining df_Selected and df_Dates
    df_new=df_Dates.join(df_Selected)
    #df_new


    
    
    if EndYear==None:
        
        Test=df_new[df_new["Fiscal Year"]==StartYear]
        
        Train=df_new[df_new["Fiscal Year"]!=StartYear]
    
    elif EndYear != None:
        
        Test= df_new[(df_new["Fiscal Year"] >= StartYear) & (df_new["Fiscal Year"] <= EndYear)]
        
        Train=df_new[~((df_new["Fiscal Year"] >= StartYear) & (df_new["Fiscal Year"] <= EndYear))]
        
        
    
    
    return(Test, Train)


# In[ ]:


split(2013)


# # Q2

# In[ ]:



#Importing necessary packages

import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import datetime


# In[ ]:


#Importing data
df=pd.read_csv("/Users/metuhead/Desktop/FE 520-Python/Assignments/HW5/Assignment5_data/HW5_Q2_data.csv")


# In[ ]:


#Creating a time period for date index only including business days
period=pd.bdate_range(start='1/3/1990',end='11/1/1993',freq='B')

num=0
for date in period:
    if str(date)[0:-9] != str(df["Date"][num]):
        holiday=[str(date)[0:-9]]
        break
    num = num + 1


# In[ ]:


#Creating  a new time period 
df_new= pd.bdate_range(start='1/3/1990', end='11/1/1993', holidays=holiday, freq='C', weekmask='Mon Tue Wed Thu Fri')


#Excluding the column  date 

df_data=df.drop(columns='Date')

#Adding the column date which is created previously

df_data["dates"]=df_new


# In[ ]:


##Modifiying the data
#Filling na with 0 value and replacing all zeros with NaN
fil_data=df_data.fillna(0)
fil_data=fil_data.replace({0:np.nan})

#Dropping colums whose values include more than 50% na
fil_data=fil_data.dropna(axis=1,thresh=fil_data.shape[1]*0.5)

#Resampling the data by BM and getting the mean of the resampled data
df_monthly=fil_data.resample("BM",on="dates").mean()
#Taking average of each row, and calculating montly return 
df_monthly["average"]=df_monthly.mean(axis=1)


# In[ ]:


#Calculating the returns between months and append 

huc=[0]
plc=0

for income in df_monthly["average"]:
    if plc>0:
        difference=income-df_monthly["average"][plc-1]
        huc.append(difference)
    plc=plc+1

    
#Now adding the difference in returns to df_monthly
df_monthly["difference"]=huc


# In[ ]:


#Finding the Mean Reversion and Momentum periods in data frame

hucre=["start"]
x=1

for difference in df_monthly["difference"]:
    if(df_monthly["difference"][x+1]>0 and df_monthly["difference"][x]>0):
        hucre.append("mmt")
    elif(df_monthly["difference"][x]>0 and df_monthly["difference"][x-1]>0):
         hucre.append("mmt")
    elif(df_monthly["difference"][x+1]<0 and df_monthly["difference"][x]<0):
        hucre.append("mmt")
    elif(df_monthly["difference"][x]<0 and df_monthly["difference"][x-1]<0):
        hucre.append("mmt")
    else:
        hucre.append("Reversion")

    x=x+1

    if x== len(df_monthly["difference"])-1:

        if(df_monthly["difference"][x]>0 and df_monthly["difference"][x-1]>0):
            hucre.append("mmt")
        elif(df_monthly["difference"][x]<0 and df_monthly["difference"][x-1]<0):
            hucre.append("mmt")
        else:
            hucre.append("Reversion")

        break


# In[ ]:


#Changes in returns are added to the hucre
df_monthly["strat"] = hucre

#Finding the strategy change in months
now=1

logchange=["start"]

for stra in df_monthly["strat"]:
    if str(df_monthly["strat"][now]) != str(df_monthly["strat"][now-1]):
        alterstring="difference "+df_monthly["strat"][now-1]+" to"+df_monthly["strat"][now];
        logchange.append(alterstring);
    else:

        logchange.append("same")
    
    now=now+1

    if now==len(df_monthly["strat"]):
        break

#Changes in returns are added to the df_monthly 

df_monthly["newstrat"]=logchange

#To easily see the newstrat 
strat_rever=df_monthly["newstrat"][::-1]


# In[ ]:


#Q2.1

plc=0
num=0

for i in strat_rever:
    
    if str(strat_rever[plc]) != "same":
        
        print(df_monthly["newstrat"].iloc[[len(df_monthly["strat"])-plc-1]])
        num=num+1
    
    plc=plc+1
    
    
    if num==2:
        break


# In[ ]:


#Q2.2

summ=0
num=0
plc=0

for stra in df_monthly["strat"]:
    
    if str(stra)=="mmt":
        
        summ=summ+df_monthly["average"][plc]
        
        num=num+1
    
    plc=plc+1
    

print("Momentum strategy return summation", summ)

print("Momentum strategy months", num)

print("Momentum strategy average return", summ*1/num)


# In[ ]:


#Q2.3
summ=0
num=0
plc=0


for stra in df_monthly["strat"]:
    
    if str(stra)=="Reversion":
        
        summ=summ+df_monthly["average"][plc]
        
        num=num+1
        
    plc=plc+1
    
    
print("Mean Reversion return summation", summ)

print("Mean Reversion strategy months", num)

print("Mean Reversion strategy average return", summ*1/num)

        


# # Q3

# In[ ]:


import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import linear_model
from sklearn import preprocessing
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import linear_model
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, r2_score


# In[ ]:


#Q3.1
#Load the data

diabets_df=datasets.load_diabetes()


# In[ ]:


#Show the data
diabets_df


# In[ ]:


#Q3.2

#Randomly split the data into training set (80%) and testing set (20%).
new_df= diabets_df.data[:,np.newaxis,2]

varx_test=new_df[-20:]
varx_train=new_df[:-20]

vary_test=diabets_df.target[-20:]
vary_train=diabets_df.target[:-20]


# In[ ]:


# Q3.3
# Creating  a linear regression model

lm=linear_model.LinearRegression()

lm.fit(varx_train,vary_train)


model_y= lm.predict(varx_test)

model_y


# In[ ]:


# Showing coefficients and Finding residuals and r square

coef=lm.coef_

ms_error=mean_squared_error(vary_test,model_y)

r_square=r2_score(vary_test,model_y)

print(coef)
print(ms_error)
print(r_square)



# In[ ]:


#Q3.4

#Fitting and validating  linear regression models on the whole data set.

fold=10

new_lm=lm.fit(varx_train,vary_train)

rang=list(range(1,11))

for results in rang:
    
    result=cross_val_score(new_lm,varx_train, vary_train,cv=10)
    print(result)
    
    

