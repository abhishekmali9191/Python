#Assignment weather data with seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

day = [f'Day{i}' for i in range(1,21)]
temp = np.random.randint(15,30,size=(20))
humid = np.random.randint(50,90,size=(20))
print(temp)

df = pd.DataFrame({'Day':day,'Temperature':temp,'Humidity':humid})
print(df)
plt.figure(figsize=(20,8))
sns.lineplot(data=df)
plt.title('Temperature Data for a Month')
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.show()

sns.scatterplot(data=df)
plt.title('Temperature Data for a Month')
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.show()

plt.figure(figsize=(20,8))
sns.boxplot(x ='Humidity',y = 'Temperature',data=df)
plt.title('Temperature Data for a Month')
plt.xlabel('Humidity')
plt.ylabel('Temperature')
plt.show()

plt.figure(figsize=(20,8))
sns.histplot(data=df, x ='Day',y = 'Temperature' )
plt.title("Histo graph")
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.show()

# #######################################################
# OUTPUT
# [19 27 17 26 19 17 19 27 21 18 25 19 17 15 25 16 26 17 21 20]
#       Day  Temperature  Humidity
# 0    Day1           19        74
# 1    Day2           27        74
# 2    Day3           17        52
# 3    Day4           26        64
# 4    Day5           19        85
# 5    Day6           17        68
# 6    Day7           19        58
# 7    Day8           27        52
# 8    Day9           21        75
# 9   Day10           18        86
# 10  Day11           25        78
# 11  Day12           19        52
# 12  Day13           17        74
# 13  Day14           15        82
# 14  Day15           25        78
# 15  Day16           16        50
# 16  Day17           26        57
# 17  Day18           17        86
# 18  Day19           21        82
# 19  Day20           20        54



