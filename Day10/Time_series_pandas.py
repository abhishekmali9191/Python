# Time Series with Pandas
dates = pd.date_range(start='2024-01-01', periods=10, freq='D')
print(dates.dtype, dates,'\n')

#creating a time series with random data
data = np.random.randn(10)
time_series = pd.Series(data, index=dates)
print(time_series)

#access data for a specific date
print("Time series for : 2024/01/05",time_series['2024-01-05'])

#accessing data within a date range
print("Time series for range",time_series['2024-01-03':'2024-02-06'])

#boolean indexing to select dates based on a condition
print("With boolean indexing",time_series[time_series>0])

#create a time seiers with hourly frequency
hourly_dates = pd.date_range(start='2024-01-01', periods=24, freq='H')
hourly_data = np.random.randn(24)
hourly_series = pd.Series(hourly_data, index=hourly_dates)
print("COmplete hourly series : ",hourly_series)

#accesing data for a specific dates
print(hourly_series['2024-01-01 10:00:00'])

#accessing data within a date range
print(hourly_series['2024-01-01 10:00:00':'2024-01-01 15:00:00'])

#selecting data with in a range and with a condition
print(hourly_series[(hourly_series.index>='2024-01-01 10:00:00') & (hourly_series>0)])

#accessing data for a specific date
print(time_series.loc['2024-01-05'])

#access data for a multiple specific date
print(time_series.loc['2024-01-05': '2024-02-05'])

#Access data within a date range
print(time_series.loc['2024-01-03':'2024-02-06'])

#boolean indexing to select dates based on a condition
print(time_series.loc[time_series>0])

#accesss data for first position
print(time_series.iloc[0])

#access data for last position
print(time_series.iloc[-1])

#access data for the position from 2 to 5
print(time_series.iloc[2:5])

#Access data for a specific position
#print()



########################################################################
# OUTPUT
# datetime64[ns] DatetimeIndex(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04',
#                '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08',
#                '2024-01-09', '2024-01-10'],
#               dtype='datetime64[ns]', freq='D') 

# 2024-01-01   -0.800896
# 2024-01-02    0.490387
# 2024-01-03    0.050383
# 2024-01-04    0.473587
# 2024-01-05   -0.156716
# 2024-01-06   -0.064001
# 2024-01-07    0.543894
# 2024-01-08    0.926397
# 2024-01-09    1.217828
# 2024-01-10    1.202655
# Freq: D, dtype: float64
# Time series for : 2024/01/05 -0.1567155494165185
# Time series for range 2024-01-03    0.050383
# 2024-01-04    0.473587
# 2024-01-05   -0.156716
# 2024-01-06   -0.064001
# 2024-01-07    0.543894
# 2024-01-08    0.926397
# 2024-01-09    1.217828
# 2024-01-10    1.202655
# Freq: D, dtype: float64
# With boolean indexing 2024-01-02    0.490387
# 2024-01-03    0.050383
# 2024-01-04    0.473587
# 2024-01-07    0.543894
# 2024-01-08    0.926397
# 2024-01-09    1.217828
# 2024-01-10    1.202655
# dtype: float64
# COmplete hourly series :  2024-01-01 00:00:00    0.660973
# 2024-01-01 01:00:00    1.209941
# 2024-01-01 02:00:00    0.040527
# 2024-01-01 03:00:00    0.288176
# 2024-01-01 04:00:00    0.871131
# 2024-01-01 05:00:00    0.935007
# 2024-01-01 06:00:00    0.929704
# 2024-01-01 07:00:00   -0.094870
# 2024-01-01 08:00:00   -0.823347
# 2024-01-01 09:00:00    0.626179
# 2024-01-01 10:00:00    0.238125
# 2024-01-01 11:00:00    0.991560
# 2024-01-01 12:00:00   -0.250604
# 2024-01-01 13:00:00    0.240348
# 2024-01-01 14:00:00   -0.011986
# 2024-01-01 15:00:00    1.475126
# 2024-01-01 16:00:00   -1.396969
# 2024-01-01 17:00:00    1.131800
# 2024-01-01 18:00:00    0.918243
# 2024-01-01 19:00:00   -1.195937
# 2024-01-01 20:00:00    1.875485
# 2024-01-01 21:00:00   -1.615219
# 2024-01-01 22:00:00   -1.546902
# 2024-01-01 23:00:00   -0.021424
# Freq: H, dtype: float64
# 0.23812509364686332
# 2024-01-01 10:00:00    0.238125
# 2024-01-01 11:00:00    0.991560
# 2024-01-01 12:00:00   -0.250604
# 2024-01-01 13:00:00    0.240348
# 2024-01-01 14:00:00   -0.011986
# 2024-01-01 15:00:00    1.475126
# Freq: H, dtype: float64
# 2024-01-01 10:00:00    0.238125
# 2024-01-01 11:00:00    0.991560
# 2024-01-01 13:00:00    0.240348
# 2024-01-01 15:00:00    1.475126
# 2024-01-01 17:00:00    1.131800
# 2024-01-01 18:00:00    0.918243
# 2024-01-01 20:00:00    1.875485
# dtype: float64
# -0.1567155494165185
# 2024-01-05   -0.156716
# 2024-01-06   -0.064001
# 2024-01-07    0.543894
# 2024-01-08    0.926397
# 2024-01-09    1.217828
# 2024-01-10    1.202655
# Freq: D, dtype: float64
# 2024-01-03    0.050383
# 2024-01-04    0.473587
# 2024-01-05   -0.156716
# 2024-01-06   -0.064001
# 2024-01-07    0.543894
# 2024-01-08    0.926397
# 2024-01-09    1.217828
# 2024-01-10    1.202655
# Freq: D, dtype: float64
# 2024-01-02    0.490387
# 2024-01-03    0.050383
# 2024-01-04    0.473587
# 2024-01-07    0.543894
# 2024-01-08    0.926397
# 2024-01-09    1.217828
# 2024-01-10    1.202655
# dtype: float64
# -0.8008957057614414
# 1.2026548094187433
# 2024-01-03    0.050383
# 2024-01-04    0.473587
# 2024-01-05   -0.156716
# Freq: D, dtype: float64