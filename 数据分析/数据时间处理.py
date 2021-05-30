import xlwings as xw

def number():
    time = []
    for j in range(7):
        for i in range(1,81):
            time.append(i)

    print(time)

    sht = xw.Book().sheets('sheet1')  # 新增一个表格
    sht.range('A1').options(transpose=True).value = time

number()

