# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 12:32:28 2022

@author: 97798
"""
import pandas as pd

from datetime import datetime
import math



dat=pd.read_csv('sun-rise-pac_2023.txt', sep = "\s+|\t+|\s+\t+|\t+\s+")

phiKTM=27.42
lambKTM=85.2212



phi_20=20
phi_30=30

#t20=pd.to_datetime("2023/01/01")
year=2023
month=1
day=1

# def sriset_time(h1,m1,h2,m2,phi,lamb):
#     print (h1,m1,h2,m2,phi,lamb)
#     #constants
#     lmtLamb=86.25
#     delLamb=lmtLamb-lamb
#     t_lamb=((24/360)*60)*delLamb
    
#     delPhi=phiKTM-20
    
    
#     # suffix 1 is for latitude 20 degrees and suffix 2 is for latitude 30 degrees
    
#     t1=pd.to_datetime(str(h1)+":"+str(m1))
    
#     t2=pd.to_datetime(str(h2)+":"+str(m2))
    
    
#     delt=t2-t1
#     delt_mins=int(delt.seconds/60)
    
#     #addition due to change in latitude 
#     t_phi=t1+pd.Timedelta(minutes=(delPhi*(delt_mins/(phi_30-phi_20))))
#     t_sriset=t_phi+pd.Timedelta(t_lamb)
#     sunriset=[t_sriset.hour,t_sriset.minute]
#     return (sunriset)
   

h_20=[dat['h']]
h_30=[dat['h.1']]
m_20=[dat['m']]
m_30=[dat['m.1']]



def delta_time(h1,m1,h2,m2,p1,l1):
    lmtLamb=86.25
    delLamb=lmtLamb-l1
    tLamb=delLamb*((24/360)*60)
   
    
    t1=pd.to_datetime("2023/01/01 "+h1.astype(str)+":"+m1.astype(str))
    
    t2=pd.to_datetime("2023/01/01 "+h2.astype(str)+":"+m2.astype(str))  
    
    delt=t2-t1
    return delt
    
    
    #delPhi=phiKTM-20
    #tPhi= delPhi*(0)
    #return([(h1+h2)/2,(m1+m2)/2,tLamb,delPhi])
            

# for a,b,c,d in zip(h_20,m_20,h_30,m_30):
#     sriset_time(a,b,c,d,phiKTM,lambKTM)
# #sriset=sriset_time(6,35,6,56,phiKTM,lambKTM)
# #dat['h_1']=dat['h']+dat['m']
dat["delt30-20"]=delta_time(dat['h'],dat['m'],dat['h.1'],dat['m.1'],phiKTM,lambKTM)



print(dat)



# dat["h_1"]=sriset_time(dat['h'],dat['m'],dat['h.1'],dat['m.1'],phiKTM,lambKTM)[0]
# dat["m_1"]=sriset_time(dat['h'],dat['m'],dat['h.1'],dat['m.1'],phiKTM,lambKTM)[1]
# dat["longitude"]=sriset_time(dat['h'],dat['m'],dat['h.1'],dat['m.1'],phiKTM,lambKTM)[2]
# dat["latitude"]=sriset_time(dat['h'],dat['m'],dat['h.1'],dat['m.1'],phiKTM,lambKTM)[3]
