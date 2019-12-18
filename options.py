from bs4 import BeautifulSoup
import urllib.request
from config import API_KEY
from alpha_vantage.timeseries import TimeSeries
import json
import datetime

def getEarningsHistoryHTML(stock):
    s = "https://www.nasdaq.com/market-activity/stocks/{}/earnings".format(stock)
    print(s)
    fp = urllib.request.urlopen(s)
    byteArr = fp.read()
    html = byteArr.decode("utf8")
    fp.close()
    return html

def getDate(quarterReport):
    return str(quarterReport.find_all_next("td")[1])[4:-5]

def getPastEarningsDates(stock):
    pastEarningsDates = []
    soup = BeautifulSoup(getEarningsHistoryHTML(stock), 'html.parser')
    table = soup.table.find_all('tr')
    for i in range(1, len(table)):
        quarterReport = table[i]
        date = getDate(quarterReport)
        pastEarningsDates.append(date)
    return pastEarningsDates

def get(stock):
    try:
        earningsMap = dict()
        dates = getPastEarningsDates(stock)
        for date in dates:
            data = getPastEarningsData(stock, date)
            earningsMap[date] = data
        print("DATA FOR __{}__".format(stock.upper()))
        print("Q DATE    | +/- %    | OPEN   | CLOSE")
        print("===================================")
        for date in earningsMap:
            print(date + ":", earningsMap[date])
    except:
        return "An error occurred."

def getPastEarningsData(stock, d):
    date = datetime.datetime.strptime(d, '%m/%d/%Y').strftime('%Y-%m-%d')
    ts = TimeSeries(key=API_KEY)
    stockJSON = ts.get_daily(symbol=stock, outputsize='full')[0]
    enumeratedJSON = list(enumerate(stockJSON))
    for index, elem in enumeratedJSON:
        if elem == date:
            prevDate = enumeratedJSON[index+1][1]
            prevDateClose = round(float(stockJSON[prevDate]["4. close"]), 2)
            nextDate = enumeratedJSON[index-1][1]
            nextDateClose = round(float(stockJSON[nextDate]["4. close"]), 2)
            percentChange = str(round((nextDateClose / prevDateClose - 1.0) * 100, 2)) + "%"
            return (percentChange, "$" + str(prevDateClose), "$" + str(nextDateClose))


