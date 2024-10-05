#resampling data to a different frequency (e.g. weekly)
weekly_data = time_series.resample('W').mean()
print(weekly_data)

#calculating a 3 day moving average
rolling_mean = time_series.rolling(window=3).mean()
print(rolling_mean)

#adding a missing value
time_series['2024-01-04'] = np.nan
print(time_series)

# Forward filling missing values
filled_series = time_series.ffill()
print(filled_series)

# resample to weekly frequency
weekly_series = time_series.resample('W').mean()

# backward fill missing value
backward_filled_series = time_series.bfill()
print(backward_filled_series)

#interpolate missing values
interpolated_series = time_series.interpolate()
print(interpolated_series)

# detecting missing values
missing_values = time_series.isna()
print(missing_values)

# count missing values
missing_count = time_series.isna().sum()
print(missing_count)

# get indices of missing values
missing_indices = time_series[time_series.isna()].index[missing_values]
print(missing_indices)

# fill missing values with specific values
filled_series = time_series.fillna(0)
print(filled_series)

# drop missing values
dropped_series = time_series.dropna()
print(dropped_series)

# #################################################################################
# OUTPUT
# 2024-01-07    0.010509
# 2024-01-14    1.115627
# Freq: W-SUN, dtype: float64
# 2024-01-01         NaN
# 2024-01-02         NaN
# 2024-01-03   -0.086708
# 2024-01-04         NaN
# 2024-01-05         NaN
# 2024-01-06         NaN
# 2024-01-07    0.107726
# 2024-01-08    0.468763
# 2024-01-09    0.896040
# 2024-01-10    1.115627
# Freq: D, dtype: float64
# 2024-01-01   -0.800896
# 2024-01-02    0.490387
# 2024-01-03    0.050383
# 2024-01-04         NaN
# 2024-01-05   -0.156716
# 2024-01-06   -0.064001
# 2024-01-07    0.543894
# 2024-01-08    0.926397
# 2024-01-09    1.217828
# 2024-01-10    1.202655
# Freq: D, dtype: float64
# 2024-01-01   -0.800896
# 2024-01-02    0.490387
# 2024-01-03    0.050383
# 2024-01-04    0.050383
# 2024-01-05   -0.156716
# 2024-01-06   -0.064001
# 2024-01-07    0.543894
# 2024-01-08    0.926397
# 2024-01-09    1.217828
# 2024-01-10    1.202655
# Freq: D, dtype: float64
# 2024-01-01   -0.800896
# 2024-01-02    0.490387
# 2024-01-03    0.050383
# 2024-01-04   -0.156716
# 2024-01-05   -0.156716
# 2024-01-06   -0.064001
# 2024-01-07    0.543894
# 2024-01-08    0.926397
# 2024-01-09    1.217828
# 2024-01-10    1.202655
# Freq: D, dtype: float64
# 2024-01-01   -0.800896
# 2024-01-02    0.490387
# 2024-01-03    0.050383
# 2024-01-04   -0.053166
# 2024-01-05   -0.156716
# 2024-01-06   -0.064001
# 2024-01-07    0.543894
# 2024-01-08    0.926397
# 2024-01-09    1.217828
# 2024-01-10    1.202655
# Freq: D, dtype: float64
# 2024-01-01    False
# 2024-01-02    False
# 2024-01-03    False
# 2024-01-04     True
# 2024-01-05    False
# 2024-01-06    False
# 2024-01-07    False
# 2024-01-08    False
# 2024-01-09    False
# 2024-01-10    False
# Freq: D, dtype: bool
# 1