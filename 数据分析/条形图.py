import matplotlib.pyplot as plt

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

waters = ('图书馆', '档案馆', '博物馆', '艺术馆、文化馆', '出版社', '影院')
buy_number = [25, 18, 179, 21, 238, 209]

plt.bar(waters, buy_number)
# plt.title('男性购买饮用水情况的调查结果')
plt.ylabel("数量（单位：个）")
plt.show()
