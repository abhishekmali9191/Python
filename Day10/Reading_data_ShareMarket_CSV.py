data = pd.read_csv(r'/content/WCHN.csv')

data.set_index('Date', inplace=True)
print(data.head())

data.isna()

split_index = int(0.8*len(data))
train_data = data.iloc[:split_index]
test_data = data.iloc[split_index:]

print(train_data)
print(test_data)
window_size = 3
forecast = train_data.rolling(window=window_size).mean().iloc[-len(test_data):]

print(forecast)

comparision = pd.DataFrame({'Actual':test_data['Close'], 'Forecast':forecast['Close']})
print(comparision)

# Calculate the mean absolute error as a simple evaluation
mae = np.mean(np.abs(comparision['Actual']-comparision['Forecast']))
print(mae)

# ##################################################################
# OUTPUT
#                  Open       High        Low      Close  Adj Close  Volume
# Date                                                                     
# 2017-12-21  30.900000  30.940001  30.809999  30.899000  29.856110    1600
# 2017-12-22  30.870001  30.870001  30.870001  30.870001  29.828089     500
# 2017-12-26  31.059999  31.059999  31.010000  31.039000  29.991385    4800
# 2017-12-27  30.709999  30.709999  30.690001  30.690001  29.654163    2500
# 2017-12-28  30.990000  30.990000  30.959999  30.962000  29.916985     600
# Open	High	Low	Close	Adj Close	Volume
# Date						
# 2017-12-21	False	False	False	False	False	False
# 2017-12-22	False	False	False	False	False	False
# 2017-12-26	False	False	False	False	False	False
# 2017-12-27	False	False	False	False	False	False
# 2017-12-28	False	False	False	False	False	False
# ...	...	...	...	...	...	...
# 2020-03-26	False	False	False	False	False	False
# 2020-03-27	False	False	False	False	False	False
# 2020-03-30	False	False	False	False	False	False
# 2020-03-31	False	False	False	False	False	False
# 2020-04-01	False	False	False	False	False	False
# 572 rows × 6 columns

