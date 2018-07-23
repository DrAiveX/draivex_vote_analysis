#! /usr/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
d=pd.read_csv("draivex.csv")
d=d.drop_duplicates(subset=['Name'])
data={}
for _,k,v in d[['Preferred Day of Week','Stream']].itertuples():
    x=data.get(k,None)
    if not x:
        data[k]=[v]
    else:
        x.append(v)
        data[k]=list(set(x))
print(data)
final=list(zip(*{k:len(v) for k,v in data.items()}.items()))
print(final)
Y1=np.array(final[1],dtype=np.float32)
b=final[0][np.array(final[1]).argmax()]
d.rename(columns={'Preferred Time Slot (1 - 1.5 hours)':'slot'},inplace=True)
dc=dict(d[d['Preferred Day of Week']==b]['slot'])
i=0
d3={}
for k,v in dc.items():
    x=v.split(';')
    for elem in x:
        d3[i]=elem
        i+=1
a=list(zip(*dict(Counter(list(zip(*d3.items()))[1])).items()))
plt.subplot(1,2,1)
plt.title("Forum Days")
plt.xlabel("Days of Weeks")
plt.ylabel("Comfortability")
plt.ylim(0,100)
plt.bar(final[0],(Y1/np.sum(Y1))*100)
plt.subplot(1,2,2)
plt.title("Time:")
plt.xlabel("Time Slots")
plt.ylabel("Comfortability")
plt.ylim(0,100)
Y2=np.array(a[1],dtype=np.float32)
plt.bar(a[0],(Y2/np.sum(Y2))*100)
plt.show()
