#Assignment 2 same data with seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

months = ['January','February','March','April','May','June','July','August','September','October','November','December']
products =['Product A','Product B','Product C','Product D','Product E']
sales_data = np.random.randint(100,500,size=(12,5))
#print(sales_data)
df = pd.DataFrame(sales_data,columns=products, index=months)
print(df)
plt.figure(figsize=(20,8))
sns.lineplot(data=df)
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8,8))
sns.barplot(data=df, )
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
#plt.show()

plt.figure(figsize=(8,8))
sns.violinplot(data=df)
plt.title('Sales Data for a Year')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.show()

# ######################################################
# OUTPUT
#            Product A  Product B  Product C  Product D  Product E
# January          169        362        366        357        464
# February         396        222        426        301        182
# March            370        480        133        397        125
# April            413        289        290        246        310
# May              442        336        394        349        107
# June             452        227        161        256        220
# July             107        185        432        203        223
# August           335        154        407        274        314
# September        435        416        128        273        231
# October          331        154        153        125        369
# November         232        397        226        453        121
# December         184        325        451        442        409

# WARNING:matplotlib.legend:No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.
# WARNING:matplotlib.legend:No artists with labels found to put in legend.  Note that artists whose label start with an underscore are ignored when legend() is called with no argument.

