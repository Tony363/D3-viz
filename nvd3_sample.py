import pandas as pd
from nvd3 import multiBarChart

filepath = '/home/tony/Desktop/DV_homework/homework2/census.csv'
census = pd.read_csv(filepath,encoding='utf8')

output_file = open('multiBarChart.html','w')
chart = multiBarChart(width=500, height=400, x_axis_format=None)
chart.set_containerheader("<h2>US Population Census</h2>")
xdata = ['one', 'two', 'three', 'four']
ydata1 = [6, 12, 9, 16]
ydata2 = [8, 14, 7, 11]

chart.add_serie(name="Serie 1", y=ydata1, x=xdata)
chart.add_serie(name="Serie 2", y=ydata2, x=xdata)
chart.buildhtml()
output_file.write(chart.htmlcontent)
print(chart.htmlcontent)
output_file.close()