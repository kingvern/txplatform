import json
import tablib

# json.text文件的格式： [{"a":1},{"a":2},{"a":3},{"a":4},{"a":5}]

# 获取ｊｓｏｎ数据
# with open('patent_list_with_pdf.json', 'r') as f:
#     rows = json.load(f)
#
# # 将json中的key作为header, 也可以自定义header（列名）
# # header=tuple([ i for i in rows[0].keys()])
# header = tuple(
#     {'pid', 'tio', 'abso', 'ago', 'pdt', 'pk', 'asc', 'tic', 'absc', 'lc', 'pd', 'ino', 'ad', 'ape', 'exo', 'tie',
#      'agc', 'pno', 'age', 'aso', 'lssc', 'vu', 'ase', 'pdfexist', 'debec', 'ine', 'exc', 'inc', 'apc', 'ano', 'apo',
#      'pns', 'ans', 'abse', 'debee', 'sfpns', 'ipc', 'debeo'})
#
# data = []
# # 循环里面的字典，将value作为数据写入进去
# for row in rows:
#     body = []
#     for v in row.values():
#         body.append(v)
#     data.append(tuple(body))

# data = tablib.Dataset(*data, headers=header)
#
# open('data.xls', 'wb').write(data.xls)
import pandas as pd

df = pd.read_json(r'patent_list_with_pdf_std.json', encoding='UTF-8')  # 如果文本里有汉字格式，此处需要设置encoding= 'UTF-8'，否则汉字会乱码
df.to_excel(r'patent_list_with_pdf_std.xlsx', index=False)
