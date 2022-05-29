import requests
import json
import pprint

# exchange data from a date start=YYYYMMDD
start_date="2021-01-01"

# exchange data till a date end= YYYYMMDD
end_date="2022-05-20"

# base currency or reference currency valcode= usd – символьний код валюти
valcode="USD"

# required currency for plot sort=exchangedate – назва поля по якому виконується сортування (exchangedate/
# r030/сс/rate)
sort="exchangedate"

# order= desc - метод сортування (desc – за спаданням, asc – за зростанням)
order="desc"

# json- формат надання інформації, якщо цей параметр не зазначено, то XML
fdata="json"

# api url for request 
url = f'https://bank.gov.ua/NBU_Exchange/exchange_site?start={start_date}&end={end_date}&valcode={valcode}&sort={sort}&order={order}&{fdata}'
response = requests.get(url)

# retrive response in json format
data = response.json()

pprint.pprint(data["rate"])

rates=[]
# extract dates and rates from each item of dictionary or json in the above created list
for i,j in data["rates"].items():
      rates.append([i,j[out_curr]])
print(rates)

# create an data frame
import pandas as pd
df=pd.DataFrame(rates)
# define column names explicitely
df.columns=["date","rate"]
df