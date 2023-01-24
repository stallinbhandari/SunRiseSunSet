
clc
clear all
close all
%format longg
%% Method of Calculating Local Mean Time of Sunrise:

%In Nepal to obtain NST add 4*(86.25-lambda) mins or deduct
%4*(lambda-86.25) min as station is
%rad=(pi/180)
%coordinate input
%phi=27.7%27 42 00N
phi=27.696111111111112%ktm
lamda=85.360555555555550%85 22 12
%Nepal standard time(NST) Add value to longitude
%mins=4*(86.25-85.37)
mins=4*(86.25-85.360555555555550)%varanashi
hr_min = @(mins) [fix(mins/60) rem(mins,60)]
test = hr_min(mins)
dms = test(:,1)+test(:,2)/60
 
 
%angleInDegrees = dms2degrees(0 4.12)
%interpolation form given latitude phi1 and phi2
phi1=20
phi2=30

delphi=(phi2-phi1)
%INPUT t1

data=load('sunset.txt')
%time of sunset at 20 degree latitude 
t1=[data(:,2) data(:,3)]


 t1=t1(:,1)+t1(:,2)/60
 %INPUT t2
 %time of sunset at 30 degree latitude 
t2=[data(:,4) data(:,5)]
 t2=t2(:,1)+t2(:,2)/60

 delt=t2-t1
%Method of interpolation 
%diffin lat
delphi1=phi-20
 %phi1=6.583333+0.2597
%interpolation value
int=delphi1*(delt/10)
 %Add value to t1
 x=t1+int
 %x=degrees2dm(x)
 
 %Sunrise time at phi and lambda is
 sunsettime=x+dms
 sunsetindms=degrees2dms(sunsettime)
 second=sunsetindms(:,3)
 second=round(second)
 sunsetdmsround=[ sunsetindms(:,1) sunsetindms(:,2) second ]
 %inUTM
% utm1=(sunrisetime-(5+45/60))
% sunriseindmsutm=degrees2dms(utm1)
% %Twilight add 15 min to sunset
% twil=(0+15/60)
% twil1=utm1+twil

