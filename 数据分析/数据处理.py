import pandas as pd
import matplotlib.pyplot as plt

path = 'C:\\Users\\lim\\Desktop\\数据.xlsx'
data = pd.DataFrame(pd.read_excel(path))
# print(data.info())

s = data.city.value_counts()[0:6]
# print(s)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
# print(data.describe(),'\n')
plt.clf()
s.plot.barh()
plt.show()
