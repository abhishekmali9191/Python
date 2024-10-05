from scipy.interpolate import interp1d
import numpy as np

#konwing data points
x = np.array([0,1,2,3])
y = np.array([0,1,4,9])

#create a interpolate function
f = interp1d(x,y,kind = 'linear')

#interpolate a new value
new_x = 2.5
interpolated_value = f(new_x)
print(interpolated_value)  #interpolated value


# ################################################
# OUTPUT
# 6.5