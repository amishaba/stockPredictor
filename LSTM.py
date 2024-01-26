import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import datetime as dt
import yfinance as yf 

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential 
from keras.layers import Dense, Dropout, LSTM


print("starttt")
company = 'AAPL'
start = dt.datetime(2012,1,1)
end = dt.datetime(2022,1,1)


#data = web.DataReader(company, 'yahoo',start,end)
df= yf.download(company,start=start, end=end)

df= df.reset_index()
df= df.drop(['Date', 'Adj Close'], axis=1)
print(str(df.head()))

print(plt.plot(df.Close))