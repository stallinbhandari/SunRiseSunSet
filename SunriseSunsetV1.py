# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 12:32:28 2022

@author: 97798
"""
import pandas as pd

from datetime import datetime
import os



dat_rise= pd.read_csv('sun-rise-pac_2023.txt', sep = "\s+|\t+|\s+\t+|\t+\s+")
dat_set= pd.read_csv('sun-set-pac_2023.txt', sep = "\s+|\t+|\s+\t+|\t+\s+")
#reading station files
file= open('stations.txt', 'r')
phiKTM=27.42
lambKTM=85.2212
f1=file.readlines()
stn={}
for lines in f1:
    rec=lines.strip().split()
    #print (rec[6])
    stn[rec[0]]=[int(rec[1])+int(rec[2])/60+int(rec[3])/3600, int(rec[4])+int(rec[5])/60+int(rec[6])/3600]

#Interpolating upper and lower latitudes
phi_20=20
phi_30=30

# #t20=pd.to_datetime("2023/01/01")
# year=2023
# month=1
# day=1

def sriset_time(dat,phi,lamb,event):
    
    h1=dat['h']
    h2=dat['h.1']
    m1=dat['m']
    m2=dat['m.1']

    #print (h1,m1,h2,m2,phi,lamb)
    #constants
    lmtLamb=86.25
    delLamb=lmtLamb-lamb
    t_lamb=((24/360))*delLamb
    #print (t_lamb)
    
    delPhi=phi-20
    # suffix 1 is for latitude 20 degrees and suffix 2 is for latitude 30 degrees
    #lets convert all units to hour so that we can do arithmetic operations easily
    time1=h1+m1/60
    time2=h2+m2/60
    # print (time1)
    
    #calculating rate change of time with each degree of latitude and adding the change to timea at 20 degree
    delt=time2-time1
    delt_mins=delt
    t_phi=delPhi*(delt_mins/(phi_30-phi_20)) #amount of time change from 20 degrees lat to phi lat
    #print ("thi si t_phi",t_phi)
    t_sriset=t_phi+t_lamb+time1 # time of sunrise or sunset at phi lat
    if event.upper()== "RISE":        
        t_twito=t_sriset-0.25 
        t_sriset= t_sriset.astype(str).str.split('.')
        t_twito=t_twito.astype(str).str.split('.')
        #h_m=pd.concat([t_sriset,t_twito], axis=1)       
        split_rise=pd.DataFrame(t_sriset.to_list(), columns=['hrise','mrise'])
        split_tFrom=pd.DataFrame(t_twito.to_list(), columns=['htFrom','mtFrom'])
        split_rise['mrise']=((split_rise['mrise'].str[:2]).astype(int)*.6).round(decimals=0).astype(int)
        split_tFrom['mtFrom']=((split_tFrom['mtFrom'].str[:2]).astype(int)*.6).round(decimals=0).astype(int)
        data=pd.concat([split_rise['hrise'],split_rise['mrise'],split_tFrom['htFrom'],split_tFrom['mtFrom']], axis=1)
    elif event.upper()=="SET":
        t_twito=t_sriset+0.25
        t_sriset= t_sriset.astype(str).str.split('.')
        t_twito=t_twito.astype(str).str.split('.')
        #h_m=pd.concat([t_sriset,t_twito], axis=1)       
        split_set=pd.DataFrame(t_sriset.to_list(), columns=['hset','mset'])
        split_tTo=pd.DataFrame(t_twito.to_list(), columns=['htTo','mtTo'])
        split_set['mset']=((split_set['mset'].str[:2]).astype(int)*.6).round(decimals=0).astype(int)
        split_tTo['mtTo']=((split_tTo['mtTo'].str[:2]).astype(int)*.6).round(decimals=0).astype(int)
        data=pd.concat([split_set['hset'],split_set['mset'],split_tTo['htTo'],split_tTo['mtTo']], axis=1)
    #converting the columns (series) of the panda dataframe to string and splitting with the decimal value

    
    
    
    
    # split_set=pd.DataFrame(dat_set['h2'].to_list(), columns=['hset','mset'])
    # #converting the two digits of hour values after decimal to minutes and again storing only the integer values 
    # split_rise['mrise']=((split_rise['mrise'].str[:2]).astype(int)*.6).round(decimals=0)#.astype(int)
    
    # split_set['mset']=((split_set['mset'].str[:2]).astype(int)*.6).round(decimals=0)#.astype(int)
    
    # #dat=pd.concat([dat,split], axis=1)
    # #dat1=pd.concat([dat_rise['Month'],dat_rise['Day'],split],axis=1)
    # dat1=pd.concat([dat_rise['Month'],dat_rise['Day'],split_rise,split_set], axis=1)
    # #writing the panda dataframe to a csv file without index and with defined columns only
    # #dat1.to_csv('SunriseSunset_2023_'+st+'.csv', sep=',',index=False, columns= ['Month', 'Day', 'hrise', 'mrise','hset','mset'])
    
   
    # #print (h_m)
    # return (h_m)
    return (data)

#looping through station coordinate and calling the sriset_time function of relevant arguments
for station in stn:
    st=station
    phi=stn[station][0]
    lamb=stn[station][1]
    #print (st, phi, lamb)
    
    
    #dat_rise["h1"],dat_rise["t2"]=sriset_time(dat_rise['h'],dat_rise['m'],dat_rise['h.1'],dat_rise['m.1'],phi,lamb)[0], sriset_time(dat_rise['h'],dat_rise['m'],dat_rise['h.1'],dat_rise['m.1'],phi,lamb)[1]
    #dat_set["h2"],dat_set["t4"]=sriset_time(dat_set['h'],dat_set['m'],dat_set['h.1'],dat_set['m.1'], phi, lamb)[0], sriset_time(dat_set['h'],dat_set['m'],dat_set['h.1'],dat_set['m.1'], phi, lamb)[1]
  
    # #splitting the above added columns to h and m columns 
    #print (sriset_time(dat_rise, phi, lamb,'rise'))
    sunrise_dat=sriset_time(dat_rise, phi, lamb,'rise')
    sunset_dat=sriset_time (dat_set,phi,lamb,'set')
    dat_print=pd.concat([dat_rise['Month'],dat_rise['Day'],sunrise_dat, sunset_dat['hset'],sunset_dat['mset'],sunset_dat['htTo'],sunset_dat['mtTo']],axis=1)
    
    print (st,'\n',dat_print)
    dat_print.to_csv('SunriseSunset_2023_'+st+'.csv', sep=',',index=False, columns= ['Month', 'Day','htFrom','mtFrom', 'hrise', 'mrise','hset','mset','htTo','mtTo'])
    
    


file.close()