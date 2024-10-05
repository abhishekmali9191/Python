print("-----------Pie Chart---------------")
for i in range(12):
    plt.figure(figsize=(16,8))
    plt.pie(sales_data[i],labels=products,autopct='%1.2f%%')
    plt.title(f'Sales Data for  {months[i]}')
plt.show()

