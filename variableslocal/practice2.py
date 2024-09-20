import xlrd loc = ("path of file")
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)
print(sheet.cell_value(____ ,____))