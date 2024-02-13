#write same data on the excel all cells
import openpyxl
#file-workbook-sheet-row-column
file="D:\Datasets\ddtselenium.xlsx"
workbook=openpyxl.load_workbook(file)
sheet=workbook["Sheet1"]
for r in range(1,6):
    for c in range(1,5):
        sheet.cell(r,c).value="welcom"
workbook.save(file)