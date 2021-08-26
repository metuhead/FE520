
# HW 4

#1.1

#Importing modules
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from numpy import mean
from numpy.core.defchararray import count
from statistics import stdev


#Reading the csv file
file_csv=pd.read_csv("/Users/metuhead/Desktop/FE 520-Python/HW4/Homework4_Dataset/res_purchase_2014.csv")
file_csv
#Showing Amount column in csv file
file_csv["Amount"]


# Replacing and splitting unwanted charachters in the column
df_Amount=file_csv["Amount"].map(lambda x: str(x).replace("(","-").replace("$","").strip(")").strip("zero").strip(" "))
#df_Amount=file_csv["Amount"].map(lambda x: str(x).strip("$"))
df_Amount=pd.to_numeric(df_Amount)

#df_Amount=df_Amount.astype(float)

# Calculating sum of Amount column
df_Amount.sum()

#1.2

# displaying Amount and Vendor columns
file_csv[["Amount","Vendor"]]


# Filtering the Amount column by WW GRAINGER vendor
df_GRAINGER=df_Amount[file_csv["Vendor"] =="WW GRAINGER"]

#sum of the Amount spent in WW GRAINGER
df_GRAINGER.sum()


#1.3

# Filtering the Amount column by WW SUPERCENTER vendor
df_SUPERCENTER=df_Amount[file_csv["Vendor"]=="WM SUPERCENTER"]

#sum of the Amount spent in WW SUPERCENTER
df_SUPERCENTER.sum()


#1.4
# displaying Amount and MCC columns
file_csv[["Amount","Merchant Category Code (MCC)"]]
# Filtering the Amount column by  MCC column where MCC is Grocery Stores
df_GROCERY=df_Amount[file_csv["Merchant Category Code (MCC)"]== "GROCERY STORES,AND SUPERMARKETS"]
df_GROCERY

#sum of the Amount spent in Grocery Stores
df_GROCERY.sum()



#########  Q2

#Q1
df_Balancesheet= pd.read_excel("/Users/metuhead/Desktop/FE 520-Python/HW4/Homework4_Dataset/Energy.xlsx")

df_Ratings=  pd.read_excel("/Users/metuhead/Desktop/FE 520-Python/HW4/Homework4_Dataset/EnergyRating.xlsx")

#displaying Energy dataframe
df_Balancesheet


#Q2
#filling all na with zeros for Energy
df_Balancesheet=df_Balancesheet.fillna(0)
df_Balancesheet

# Replacing all nan  with 0
df_Balancesheet=df_Balancesheet.replace(0,np.nan)
df_Balancesheet
df_Ratings

#filling all na with zeros for Ratings
df_Ratings=df_Ratings.fillna(0)
df_Ratings

# Replacing all nan values with 0
df_Ratings= df_Ratings.replace(0,np.nan)
df_Ratings

#Getting number of rows and col in Balance sheet dataframe
df_Balancesheet.shape

# Calculating 90% of the column numbers as threshold
tresh= 844*0.9
tresh

#Dropping columns including more than 90% zero or missing value
df_Balancesheet=df_Balancesheet.dropna(axis=1,thresh=759.6)
df_Balancesheet

#Getting number of rows and columns in Rating dataframe
df_Ratings.shape
# # Calculating 90% of the column numbers as threshold
tresh1=2522*0.9
tresh1
#print the results
print(df_Ratings.shape, tresh1)

#Dropping columns including more than 90% zero or missing value
df_Ratings=df_Ratings.dropna(axis=1,thresh=2269.8)
df_Ratings

#Q3
##Replacing NaN values with mean
df_Balancesheet=df_Balancesheet.replace("NaN",df_Balancesheet.mean())
# or this one df_Balancesheet=df_Balancesheet.fillna(df_Balancesheet.mean())

df_Ratings=df_Ratings.replace("NaN",df_Ratings.mean())
# or this one  df_Ratings=df_Ratings.fillna(df_Ratings.mean())


#Selecting numerical parts

num_df_Balancesheet=df_Balancesheet.select_dtypes([np.number])
num_df_Ratings=df_Ratings.select_dtypes([np.number])
num_df_Ratings
num_df_Balancesheet



#Q4

## defining a function to normalize the table



def norm(x):

  x_new= (x-x.min())/(x.max()-x.min())

  return x_new


#Normalizing the table for both Balancesheet and Ratings

num_df_Balancesheet=num_df_Balancesheet.apply(norm)
#num_df_Balancesheet
num_df_Ratings=num_df_Ratings.apply(norm)
num_df_Ratings





#Q5

# Creating separate dataframe includes:
##[’Current Assets - Other - Total’, ’Current Assets - Total’]

des_cur=num_df_Balancesheet[["Current Assets - Other - Total"]]
des_cur_tot = num_df_Balancesheet[["Current Assets - Total"]]

#Stacking the dataframes
des_stack_cur_tot=des_cur_tot.stack() 
des_stack=des_cur.stack()

#Creating lists which inludes length, mean, stdev, min of the variable
s1=[len(des_stack),mean(des_stack),stdev(des_stack),min(des_stack),max(des_stack)]
s2=[len(des_stack_cur_tot),mean(des_stack_cur_tot),stdev(des_stack_cur_tot),min(des_stack_cur_tot),max(des_stack_cur_tot)]

#Converting lists into Series
S1=pd.Series(s1)
S2=pd.Series(s2)

#Concate series and creating a dataframe
pd.concat([S1,S2],axis=1)







##Q6 
#Reading and sorting the new balance sheet
df_NewBalancesheet=pd.read_excel("/Users/metuhead/Desktop/FE 520-Python/HW4/Homework4_Dataset/Energy.xlsx")
df_NewBalancesheet=df_NewBalancesheet[["Current Assets - Other - Total","Current Assets - Total","Other Long-term Assets","Assets Netting & Other Adjustments"]]

#Creating correlation matrix for new balance sheet
df_NewBalancesheet.corr()  



### Q7


##Split the Company name column and get the last word
df_Balancesheet["Name"]=df_Balancesheet["Company Name"].str.split().str[-1]

df_Balancesheet

### Q8


# Merging two datasets based on ’datadate’ and ’Global CompanyKey’

Matched=pd.merge(df_Ratings,df_Balancesheet,how="inner",on=["Data Date","Global Company Key"])
#display new dataframe
Matched

# Q9

# Creating a key and values for ratings and corresponding values
credit={"AAA": 0,"AA+": 1,"AA":2,"AA-":3,"A+":4,"A":5,"A-":6,"BBB+":7,"BBB":8,"BBB-":9,"BB+":10,"BB":11,"others":12,"":12}

# Mapping through all ratings and assigning numbers

Matched["Rate"]=Matched["S&P Domestic Long Term Issuer Credit Rating"].map(credit)

# display Matched dataframe

Matched


#Q10


#Filtering Matched dataframe with Name equals"CO"
df_frequency=Matched[Matched["Name"]=="CO"]
# Creating histogram for the distribution of the data
df_frequency["Rate"].hist()



