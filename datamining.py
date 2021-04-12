#import the library 
import pandas as pd
import numpy as np

#create the data frame of the bufftail
file=pd.DataFrame({'BuffTail':[10,1,37,5,12]})


#create the data frame of the garden bee
file1=pd.DataFrame({'Garden bee':[8,3,19,6,4]})


#create the data frame of the red tail
file2=pd.DataFrame({'Red tail':[18,9,1,2,4]})


#create the data frame of the honey bee
file3=pd.DataFrame({'Honeybee':[12,13,16,9,10]})


#create the data frame of the carder bee
file4=pd.DataFrame({'Carder bee':[8,27,6,32,23]})


#joining of all the data frame 

result=file.join(file1,lsuffix='file',rsuffix='file1')
a=result.join(file2,lsuffix='result',rsuffix='file2')
b=a.join(file3,lsuffix='a',rsuffix='file3')
c=b.join(file4,lsuffix='b',rsuffix='file4')
print(c)

#assigning the plant name to the rows
c.index=['Thistle', 'Vipers Bugloss', 'Golden Rain','Yellow Alfalfa','blackberry']
print(c)

#making the matrix object from the original data
matrix=c.values
print(matrix)

#display the data for the blackberry only
dis=c.loc['blackberry']
print(dis)

#display the data for the golden rain and yellow alfalfa
tag=c.loc[c.index.isin(['Golden Rain','Yellow Alfalfa'])]
print(tag)

#dispaly data for the redtail bee
pos=c.loc[:,'Red tail']
print(pos)

#sort the bufftail column in decreasing order
p=c.sort_values(by='BuffTail',ascending=0)
print(p)