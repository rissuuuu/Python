import pandas
from bokeh.charts import Scatter, output_file,show
data=pandas.DataFrame(columns=["X","Y"])
data["X"]=[1,2,3,4,5]
data["Y"]=[6,7,8,9,10]
print(data)