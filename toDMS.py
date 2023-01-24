# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 10:43:48 2023

@author: 97798
"""
import pandas as pd
dat=pd.read_csv('stations_20.txt', sep = "\s+|\t+|\s+\t+|\t+\s+", index_col='sno')



def to_DMS(deg):
    d=deg.astype(int)
    df=deg.astype(float)
    print (d,df)
    mf=(df-d)*60
    m=mf.astype(int)
    sf=(mf-m)*60
    s=sf.astype(int)
  
    
    #s=int(int((deg-d)*60)-m)*60
    
    return (pd.concat([d,m,s], axis=1, keys=['d','m','s']))

lat=to_DMS(dat['lat'])
lon=to_DMS(dat['lon'])

stations=pd.concat([dat['station'],lat, lon], axis=1)
stations.to_csv('stations_20.csv',index=None, header=None)
