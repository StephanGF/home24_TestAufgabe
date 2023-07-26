# -*- coding:utf-8 -*-
from config import config
import requests
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from datetime import datetime, timedelta

ts = TimeSeries(key=config.api_token)
data, meta_data = ts.get_daily('GOOGL', outputsize='compact')

endDate = datetime.now()
startDate = endDate - timedelta(days=8) #Why 8 day? Because without today`s day, and we need one more day.
print("\n\nSTART DATE: " + str(startDate.strftime('%b %d, %Y'))+ "\n")



daysArr = []
closeArr = []

for date_str, price_info in data.items():
	date = pd.to_datetime(date_str)
	if startDate <= date <= endDate:
		weekdays = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
		daysArr.append(weekdays[date.weekday()])
		closeArr.append(float(price_info['4. close']))

daysStr = ' \t'.join(daysArr)
closeStr = ' '.join([f"{c}" for c in closeArr])

ourSymbol = meta_data['2. Symbol']
print(f'Alphabet\n{ourSymbol},Currency: USD\nTime Period: {startDate.strftime("%b %d, %Y")} - {endDate.strftime("%b %d, %Y")}\n{daysStr}\n{closeStr}')