#encoding=utf-8
import xlrd
import jieba

medi = xlrd.open_workbook('medicinal.xls')

#sheet_name=medi.sheet_names()[0]
sheet = medi.sheet_by_index(0)
#print(sheet)
rows = sheet.nrows  #工作表的行数
cols = sheet.ncols  #工作表的列数

names = []

#取第六列的所有信息
for row in range(rows):
    names.append(sheet.cell(row,5))
#print(names)

for m_name in names:
    m_list = jieba.cut(str(m_name))
    print(list(m_list))