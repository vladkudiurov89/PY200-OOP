# Открывает азвание листа в книге Эксель

import pandas as pd
file = "/home/vlad/Загрузки/Primer.xlsx"
x1 = pd.ExcelFile(file)
print(x1.sheet_names)

# from openpyxl import load_workbook
#
# wb = load_workbook('/home/vlad/Загрузки/Sur.xlsx')
# print(wb.get_sheet_names())


from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd

file = open(r'Primer.csv')
df = pd.read_csv(file)
print(df)



