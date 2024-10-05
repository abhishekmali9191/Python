import plotly.graph_objects as go
import numpy as np

months = ['January','February','March','April','May','June','July','August','September','October','November','December']
sales = np.random.randint(100,500,size=(12))

#line plot
line_fig=go.Figure()
line_fig.add_trace(go.Scatter(x=months,y=sales,mode='lines+markers',name='Sales'))
line_fig.update_layout(title='Sales Data for a Year',xaxis_title='Months',yaxis_title='Sales')
line_fig.write_image(r'/content/sample_data/line_plot.png')
line_fig.show()

#bar chart
bar_fig = go.Figure()
bar_fig.add_trace(go.Bar(x=months,y=sales,name='Sales'))
bar_fig.update_layout(title='Sales Data for a Year',xaxis_title='Months',yaxis_title='Sales')
bar_fig.show()
bar_fig.write_image(r'/content/sample_data/bar_chart.png')

#pie chart
pie_fig = go.Figure(data=go.Pie(labels=months,values=sales))
pie_fig.update_layout(title='Sales Data for a Year')
pie_fig.show()
pie_fig.write_image(r'/content/sample_data/pie_chart.png')

