import numpy as np
import pandas as pd
import csv
from math import log10

#ctrl+/

class comparefactor: #group the stock into 5 portions, with the largest portion called Q1, and the smallest portion called Q5
    def _init_(self, year, portion): #self refers to the required factor
        return self

#historal data on nasdaq
aapl = pd.read_csv(r"AAPL.csv")
aapl['date_formatted'] = pd.to_datetime(aapl['Date'], format="%m/%d/%Y")
aapl = aapl.set_index("date_formatted")
aapl["Close/Last"] = aapl["Close/Last"].str.replace("$","", regex = True)
aapl["Open"] = aapl["Open"].str.replace("$","", regex = True)
aapl["High"] = aapl["High"].str.replace("$","", regex = True)
aapl["Low"] = aapl["Low"].str.replace("$","", regex = True)
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
firstdate.pop("Date")


onemonthreverse = []
for x in range(len(firstdateindex)-2):
        onemonthreverse.append(log10(aapl.iloc[firstdateindex[x],1]/aapl.iloc[firstdateindex[x]+21,1]))
onemonthreverse.extend([0,0])
firstdate1 = firstdate.copy()
firstdate1.loc[:,"1Mreverse"] = onemonthreverse

sixmonthmomentum = []
for x in range(len(firstdateindex)-5):
    sixmonthmomentum.append((firstdate.iloc[x+1,1]\
        -firstdate.iloc[x+5,1])/firstdate.iloc[x+5,1])
sixmonthmomentum.extend([0,0,0,0,0])
firstdate2 = firstdate1.copy()
firstdate2.loc[:,"6Mmomentum"] = sixmonthmomentum

twelvemonthmomentum = []
for x in range(len(firstdateindex)-11):
    twelvemonthmomentum.append((firstdate.iloc[x+1,1]\
        -firstdate.iloc[x+11,1])/firstdate.iloc[x+11,1])
twelvemonthmomentum.extend([0,0,0,0,0,0,0,0,0,0,0])
firstdate3 = firstdate2.copy()
firstdate3.loc[:,"12Mmomentum"] = twelvemonthmomentum

stockreturn = []
for x in range (len(aapl.index)-1):
    stockreturn.append((aapl.iloc[x,1]\
        -aapl.iloc[x+1,1])/aapl.iloc[x+1,1])
stockreturn.append(0)
aapl2 = aapl.copy()   
aapl2.loc[:,"return"] = stockreturn
sd = []
for x in range(len(monthlist)):
    sd.append( aapl2[monthlist[x]]["return"].std())
firstdate4 = firstdate3.copy()    
firstdate4.loc[:,"sd"] = sd

sdchange = []
for x in range(len(firstdate)-1):
    sdchange.append((firstdate4.iloc[x,firstdate4.columns.get_loc("sd")]\
        -firstdate4.iloc[x+1,firstdate4.columns.get_loc("sd")])/firstdate4.iloc[x+1,firstdate4.columns.get_loc("sd")])
sdchange.append(0)
firstdate5 = firstdate4.copy()
firstdate5.loc[:,"sdchange"] = sdchange

vibration = []
for x in range(len(monthlist)):
    vibration.append( (aapl[monthlist[x]]["High"].max()-aapl[monthlist[x]]["Low"].min())/\
       (aapl[monthlist[x]].iloc[-1,3]+aapl[monthlist[x]].iloc[1,1]) )
firstdate6 = firstdate5.copy()
firstdate6.loc[:,"vibration"] = vibration

analysisxls = pd.ExcelFile("AAPLF.xlsx")
basicdata = pd.read_excel(analysisxls,"finance")
columnname = []
for col in basicdata:
    columnname.append(col)
firstdate_basic = {}
for y in range (len(basicdata.columns)):
    firstdate_basic[columnname[y]] = []
    for z in range (len(basicdata.index)):
        for x in range (12):
            firstdate_basic[columnname[y]].append(basicdata.iloc[z,y])
firstdate_basic.pop("Unnamed: 0")
firstdate2 = pd.DataFrame(firstdate_basic)
firstdatereverse = firstdate2[::-1]
firstdatereverse = firstdatereverse.set_index(firstdate.index)

combinedate = pd.concat([firstdate6, firstdatereverse], axis = 1)
combinedate = combinedate.replace("- -","0")

combinedate = combinedate.astype(float)


combinedate["P/B ratio"] = combinedate["Open"]\
    /(combinedate["Total Stockholders Equity"]/combinedate["Weighted Average Shares Outstanding"])

print(combinedate)

        







    


# print(stock_dict[0].loc[stock_dict[0]["year"]== 2010,"EPS"])