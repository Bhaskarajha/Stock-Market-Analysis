# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:37:38 2019

@author: BHASKAR JHA
"""
'''import matplotlib
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline'''
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import matplotlib
%matplotlib inline
import seaborn as sns
import pandas_datareader.data as web
sns.set_style('whitegrid')
from datetime import datetime
from __future__ import division

techlist=['AAPL','GOOG','MSFT','AMZN','TSLA','NFLX','FB']
ls_key = 'Adj Close'

end=datetime.now()

start=datetime(end.year-1,end.month,end.day)
 
for stocks in techlist:
    globals()[stocks]=web.DataReader(stocks, 'yahoo',start,end)#from yahoo finance website 
    #i am taking the data

t=AAPL
a=GOOG
AAPL.describe()

#An adjusted closing price is a stock's closing price on any given day of trading
# that has been amended to include any distributions and corporate actions that occurred 
#at any time before the next day's open. The adjusted closing price is often used when examining
#historical returns or performing a detailed analysis of historical returns.



AAPL['Adj Close'].plot(legend=True,figsize=(10,4),color='blue')
GOOG['Adj Close'].plot(legend=True,figsize=(10,4),color='red')
MSFT['Adj Close'].plot(legend=True,figsize=(10,4),color='green')
AMZN['Adj Close'].plot(legend=True,figsize=(10,4),color='yellow')
TSLA['Adj Close'].plot(legend=True,figsize=(10,4),color='cyan')
NFLX['Adj Close'].plot(legend=True,figsize=(10,4),color='black')
FB['Adj Close'].plot(legend=True,figsize=(10,4),color='magenta')

AAPL['Volume'].plot(legend=True,figsize=(10,4),color='blue')
GOOG['Volume'].plot(legend=True,figsize=(10,4),color='red')
MSFT['Volume'].plot(legend=True,figsize=(10,4),color='green')
AMZN['Volume'].plot(legend=True,figsize=(10,4),color='yellow')
TSLA['Volume'].plot(legend=True,figsize=(10,4),color='black')
NFLX['Volume'].plot(legend=True,figsize=(10,4),color='cyan')
FB['Volume'].plot(legend=True,figsize=(10,4),color='magenta')


#make a list of moving average
ma_day=[10,20,30]
for ma in ma_day:
    column_name="MA for %s days" %(str(ma)) 
    MSFT[column_name]=np.roll(AAPL['Adj Close'],ma).mean


#i want graph for 10 days ,20 days , 30 days
MSFT[['Volume','MA for 10 days','MA for 20 days','MA for 30 days']].plot(subplots=False,figsize=(10,4))


#percent changes of adding and closing prices
#percent return of money
AAPL['DailyReturn']=AAPL['Adj Close'].pct_change()
AAPL['DailyReturn'].plot(figsize=(10,4),legend=True,linestyle='--',marker='o')
#how much percent return of exchange each day you will get ex .8%

sns.distplot(AAPL['DailyReturn'].dropna(),bins=100,color='purple')
#another way
AAPL['DailyReturn'].hist(bins=100)

#we want to analyze the return the stock in the list
#by building a new dataframe
closing_df=web.DataReader(techlist,'yahoo',start,end)['Adj Close']

t=closing_df.head()

techrets=closing_df.pct_change()
techrets.head()

sns.jointplot('GOOG','GOOG',techrets,kind='scatter',color='seagreen')
sns.jointplot('GOOG','AMZN',techrets,kind='scatter')
sns.jointplot('GOOG','NFLX',techrets,kind='scatter')
sns.jointplot('GOOG','FB',techrets,kind='scatter')
sns.jointplot('GOOG','TSLA',techrets,kind='scatter')
#use seaborn and pandas to use repeat comparision analysis for every possible stock
techrets.head()

sns.pairplot(techrets.dropna())


#this fig is for percent change in closing price
returns_fig=sns.PairGrid(techrets.dropna())
returns_fig.map_upper(plt.scatter,color='purple')
returns_fig.map_lower(sns.kdeplot,Cmap='cool_d')
returns_fig.map_diag(plt.hist,bins=30)

#for original closing price
returns_fig=sns.PairGrid(closing_df.dropna())
returns_fig.map_upper(plt.scatter,color='purple')
returns_fig.map_lower(sns.kdeplot,Cmap='cool_d')
returns_fig.map_diag(plt.hist,bins=30)


#find diagonal of histogram plot
#returns_fig.map_diag(plt.hist,bins=30)
#scatter_matrix(df, alpha=0.2, diagonal='hist')


#now for closing prices
#corelation b/w closing prices

#quick relation of daily return
#numerical value of daily return
sns.heatmap(techrets.dropna(),annot=True)

corr = techrets.dropna().corr()
#Plot figsize
fig, ax = plt.subplots(figsize=(10, 10))
#Generate Color Map, red & blue
colormap = sns.diverging_palette(220, 10, as_cmap=True)
#Generate Heat Map, allow annotations and place floats in map
sns.heatmap(corr, cmap=colormap, annot=True, fmt=".2f")
#Apply xticks
plt.xticks(range(len(corr.columns)), corr.columns);
#Apply yticks
plt.yticks(range(len(corr.columns)), corr.columns)
#show plot
plt.show()

#risk=amount of money we would expect to loose
#quantile=
#In statistics and probability quantiles are cut points dividing the range of a 
#probability distribution into continuous intervals with equal probabilities, or
# dividing the observations in a sample in the same way. There is one less quantile than
# the number of groups created. 
#Thus quartiles are the three cut points that will divide a dataset into four equal-sized groups.






