import numpy as np
import pandas as pd
import csv
from math import log10


aapl = pd.read_csv(r"AAPL.csv")
aapl['date_formatted'] = pd.to_datetime(aapl['Date'], format="%m/%d/%Y")
aapl = aapl.set_index("date_formatted")
aapl["Close/Last"] = aapl["Close/Last"].str.replace("$","")
aapl["Open"] = aapl["Open"].str.replace("$","")
aapl["High"] = aapl["High"].str.replace("$","")
aapl["Low"] = aapl["Low"].str.replace("$","")
aapl = aapl.astype({'Close/Last':"float"})
aapl = aapl.astype({"Open":"float"})
aapl = aapl.astype({"High":"float"})
aapl = aapl.astype({"Low":"float"})
datelist = []
monthlist = []
for x in range (2013,2023):
    for k in range(1,13):
        if k >9:
            datelist.append (str(x)+"-"+str(k)+"-"+"01")
            monthlist.append (str(x)+"-"+str(k))
        else:
            datelist.append (str(x)+"-"+"0"+str(k)+"-""01")
            monthlist.append (str(x)+"-"+"0"+str(k))
datelist.reverse()     

firstdateindex = aapl.index.get_indexer(datelist, method ='nearest')
firstdateindex = firstdateindex.tolist()
firstdate = aapl.iloc[firstdateindex,:]


onemonthreverse = []
for x in range(len(firstdateindex)-2):
        onemonthreverse.append(log10(aapl.iloc[firstdateindex[x],1]/aapl.iloc[firstdateindex[x]+21,1]))
onemonthreverse.extend([0,0])
firstdate.loc[:,"1Mreverse"] = onemonthreverse

sixmonthmomentum = []
for x in range(len(firstdateindex)-5):
    sixmonthmomentum.append((firstdate.iloc[x+1,1]\
        -firstdate.iloc[x+5,1])/firstdate.iloc[x+5,1])
sixmonthmomentum.extend([0,0,0,0,0])
firstdate.loc[:,"6Mmomentum"] = sixmonthmomentum

twelvemonthmomentum = []
for x in range(len(firstdateindex)-11):
    twelvemonthmomentum.append((firstdate.iloc[x+1,1]\
        -firstdate.iloc[x+11,1])/firstdate.iloc[x+11,1])
twelvemonthmomentum.extend([0,0,0,0,0,0,0,0,0,0,0])
firstdate.loc[:,"12Mmomentum"] = twelvemonthmomentum

stockreturn = []
for x in range (len(aapl.index)-1):
    stockreturn.append((aapl.iloc[x,1]\
        -aapl.iloc[x+1,1])/aapl.iloc[x+1,1])
stockreturn.append(0)   
aapl.loc[:,"return"] = stockreturn
sd = []
for x in range(len(monthlist)):
    sd.append( aapl[monthlist[x]]["return"].std())
firstdate.loc[:,"sd"] = sd

sdchange = []
for x in range(len(firstdate)-1):
    sdchange.append((firstdate.iloc[x,firstdate.columns.get_loc("sd")]\
        -firstdate.iloc[x+1,firstdate.columns.get_loc("sd")])/firstdate.iloc[x+1,firstdate.columns.get_loc("sd")])
sdchange.append(0)
firstdate.loc[:,"sdchange"] = sdchange

vibration = []
for x in range(len(monthlist)):
    vibration.append( (aapl[monthlist[x]]["High"].max()-aapl[monthlist[x]]["Low"].min())/\
       (aapl[monthlist[x]].iloc[-1,3]+aapl[monthlist[x]].iloc[1,1]) )
firstdate.loc[:,"vibration"] = vibration

print(firstdate)