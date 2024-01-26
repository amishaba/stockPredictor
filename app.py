import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import datetime as dt
import yfinance as yf 
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential 
from keras.layers import Dense, Dropout, LSTM
from keras.models import load_model
import streamlit as st 



print("starttt")
company = 'AAPL'
start = dt.datetime(2012,1,1)
end = dt.datetime(2022,1,1)

st.title('Stock Trend Prediction')

user_input=st.text_input('Enter Stock Ticker','AAPL')
#df= yf.download(company,start=start, end=end)
df= yf.download(user_input,start=start, end=end)

st.subheader('Data from 2010 - 2019')
st.write(df.describe())

st.subheader('Closing Price vs Time')
fig=plt.figure(figsize=(12,6))
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Closing Price vs Time with 100MA')
ma100=df.Close.rolling(100).mean()
fig=plt.figure(figsize=(12,6))
plt.plot(ma100)
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Closing Price vs Time with 100MA & 200MA')
ma100=df.Close.rolling(100).mean()
ma200=df.Close.rolling(200).mean()
fig=plt.figure(figsize=(12,6))
plt.plot(ma100)
plt.plot(ma200)
plt.plot(df.Close)
st.pyplot(fig)


#split into training and testing data
data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70) : int(len(df))])

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0,1))

data_training_array=scaler.fit_transform(data_training)



#LOAD MODEL
model=load_model('main/keras_model.keras')
#model=load_model('https://github.com/amishaba/stockPredictor/blob/main/keras_model.keras')


#tesing
past_100_days = data_training.tail(100)
final_df = pd.concat([past_100_days, data_testing], ignore_index=True)
input_data = scaler.fit_transform(final_df)

x_test=[]
y_test=[]

for i in range (100, input_data.shape[0]):
    x_test.append(input_data[i-100:i])
    y_test.append(input_data [ i , 0 ] )

x_test = np.array(x_test)
y_test = np.array(y_test)
y_predicted = model.predict(x_test)

scale_factor = 1/scaler.scale_[0]
y_predicted = y_predicted*scale_factor
y_test=y_test*scale_factor


#final plot
st.subheader('Predictions vs Original Price')
fig2 = plt.figure(figsize=(12,6))
plt.plot(y_test, 'b',label='Original Price')
plt.plot(y_predicted, 'r', label ='Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig2)

#streamlit run app.py
