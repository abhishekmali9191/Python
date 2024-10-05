#Assignment 1 : ploting sales data for a year. Using matplotlib for creating line plots and bar charts and pie charts
import matplotlib.pyplot as plt
import numpy as np
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
products =['Product A','Product B','Product C','Product D','Product E']
sales_data = np.random.randint(100,500,size=(12,5))
print(sales_data)
plt.figure(figsize=(20,8))
plt.plot(months,sales_data,label = products)
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()

dataA = sales_data[:,0]
dataB = sales_data[:,1]
dataC = sales_data[:,2]
dataD = sales_data[:,3]
dataE = sales_data[:,4]



print('------------Bar Chart-------------')
plt.figure(figsize=(6,4))
plt.bar(months,dataA, width=0.8, label=products[0])
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.show()


plt.bar(months,dataB, width=0.8, label=products[1])
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.show()

plt.figure(figsize=(16,8))
plt.bar(months,dataC, width=0.8, label=products[2])
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.show()

plt.figure(figsize=(16,8))
plt.bar(months,dataD, width=0.8, label=products[3])
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.show()

plt.figure(figsize=(16,8))
plt.bar(months,dataE, width=0.8, label=products[4])
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.show()
# plt.bar(months,dataD, width=0.8, label=products[3])
# plt.bar(months,dataE, width=0.8, label=products[4])


# #########################################################
# OUTPUT
# [[312 369 209 379 302]
#  [112 469 181 204 450]
#  [207 262 203 292 166]
#  [291 217 314 159 307]
#  [199 356 199 158 418]
#  [192 335 199 443 125]
#  [425 279 342 403 220]
#  [442 283 251 402 416]
#  [328 236 264 230 318]
#  [420 497 336 312 177]
#  [456 476 222 296 114]
#  [266 480 235 214 131]]

# ------------Bar Chart-------------




