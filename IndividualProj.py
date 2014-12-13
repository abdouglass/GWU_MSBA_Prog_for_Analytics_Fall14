# -*- coding: utf-8 -*-
"""
Created on Tue Dec 02 20:33:45 2014

@author: abdouglass
"""

import wbdata
import pandas as pd
import datetime

 
#indicators
indicators = {'SE.SEC.NENR.MA' : 'SecondaryMale',
              'SE.SEC.NENR.FE' : 'SecondaryFemale',
              'SE.SEC.NENR' : 'Secondary',
              'SE.PRM.NENR.MA' : 'PrimaryMale',
              'SE.PRM.NENR.FE' : 'PrimaryFemale',
              'SE.PRM.NENR' : 'Primary',
              'SI.POV.NAGP' : 'Poverty',
              'SI.POV.GINI' : 'GINI'}


#get data from the world bank, take an average of years for each country, return df of average of years for indicators by country
def load_avg(start_yr, end_yr):
    years = (datetime.datetime(start_yr,1,1), datetime.datetime(end_yr,12,30))
    df = wbdata.get_dataframe(indicators, data_date=years)
    wb_df = df.unstack(level = 0)
    wb_mean = wb_df.mean()
    SecM = wb_mean['SecondaryMale']
    SecF = wb_mean['SecondaryFemale']
    Sec = wb_mean['Secondary']
    Prim = wb_mean['Primary']
    PrimM = wb_mean['PrimaryMale']
    PrimF = wb_mean['PrimaryFemale']
    Poverty = wb_mean['Poverty']
    Gini = wb_mean['GINI']
    mean_df = pd.DataFrame(Poverty, columns=['Poverty'])
    mean_df['Sec_M'] = SecM
    mean_df['Sec_F'] = SecF
    mean_df['Sec'] = Sec
    mean_df['Prim_M'] = PrimM
    mean_df['Prim_F'] = PrimF
    mean_df['Prim'] = Prim
    mean_df['Gini'] = Gini
    mean_df = mean_df.dropna(how='all')
    return mean_df    

til_2014 = load_avg(2005,2014)
til_2004 = load_avg(1995,2004)
til_1994 = load_avg(1985,1994)
til_1984 = load_avg(1975,1984)
til_1974 = load_avg(1965, 1974)
all_data = load_avg(1960,2014)


#remove rows with no data (no poverty, or none in any of the school fields), add year column so that multiple decades may be combined as needed in analysis
def has_data(dfYr, yr):
    df = dfYr.copy()
    df['lastYr'] = yr
    #df = df.fillna(0)   #replace NaN rows with 0
    df['school'] = pd.isnull(df['Sec_M']) * pd.isnull(df['Sec_F']) * pd.isnull(df['Sec']) * pd.isnull(df['Prim_M']) * pd.isnull(df['Prim_F']) * pd.isnull(df['Prim']) #only care that at least one column is available, thus creating new column that adds all school columns
    df = df.loc[df['school'] == False]   #removes entries without any school data available
    df['income'] = pd.isnull(df['Poverty']) * pd.isnull(df['Gini'])
    df = df.loc[df['income'] == False]    #removes entries without any poverty data available    
    df = df.drop('school',1)             #removes school column which was added to assist in determining which columns have any school data
    df = df.drop('income',1)
    return df


#additional ratios, as well as binary variables to assist in analysis and visualization
def addVar(dfX):
    df = dfX.copy()
    df['FM_Sec'] = df['Sec_F'] / df['Sec_M']
    df['FM_Prim'] = df['Prim_F'] / df['Prim_M']
    df['PrimSec'] = df['Sec'] / df['Prim']
    df['IncEqu'] = df['Gini'].apply(lambda x: True if x <= 30 else False)                #A 0 is perfect equality, 100 is perfect inequality.  Looking at all years the mean is 40, and the median is 39.  The minimum is 25.  Based on this, a cut off of 30 was used to signify a more equitable nation.
    df['EdSecEqu'] = df['FM_Sec'].apply(lambda x: True if x >= 0.95 else False)           #Looking at all years the mean is 94% and the median is 99-101% for primary/secondary.  Anything over 95% was considered to be postive for women
    df['EdPrimEqu'] = df['FM_Sec'].apply(lambda x: True if x >= 0.95 else False)         #Looking at all years the mean is 94% and the median is 99-101% for primary/secondary.  Anything over 95% was considered to be postive for women
    return df

df_all = addVar(has_data(all_data, 'All'))        
df_2014 = addVar(has_data(til_2014, '2014'))
df_2004 = addVar(has_data(til_2004, '2004'))
df_1994 = addVar(has_data(til_1994, '1994'))
df_1984 = addVar(has_data(til_1984, '1984'))
df_1974 = addVar(has_data(til_1974, '1974'))


#Determine which DFs aren't empty and export them to csv format.
df_list = [df_2014, df_2004, df_1994, df_1984, df_1974]
df_years = ['All','2014','2004','1994','1984','1974']
df_values = []
y = 0
for df in df_list:
    if df.empty == False:
        df.to_csv("WB_{0}.csv".format(df_years[y]))
        df_values.append(df)
    y += 1








