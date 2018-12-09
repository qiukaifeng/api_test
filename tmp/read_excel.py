#1.导入xlrd
import xlrd

#2.打开excel（work_book）
excel=xlrd.open_workbook("../data/testcase.xlsx")

#3.指定工作表
sheet=excel.sheet_by_name("login")
#或者下面的方法
sheet=excel.sheet_by_index(0)

#4.读取信息
print(sheet.nrows)#有效数据行数
print(sheet.ncols)#有效数据列数

print(sheet.row_values(0))#打印第一行数据
print(sheet.row_values(1))#打印第二行数据

print(sheet.cell(0,0).value)#打印指定单元格


#1.打印所有注册模块的数据，不要标题行(方法1)
import xlrd
excel=xlrd.open_workbook("../data/testcase.xlsx")
sheet=excel.sheet_by_name("reg")
print(sheet.nrows)
print(sheet.ncols)
print(sheet.row_values(0))
print(sheet.row_values(1))
print(sheet.cell(1,0).value)#打印指定单元格

#方法2
sheet2=excel.sheet_by_name("reg")
for i in range(1,sheet2.nrows):
    print(sheet2.row_values(1))

