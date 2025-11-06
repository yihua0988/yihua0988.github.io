"""
請洗資料並轉換幣別存入Excel
"""
import os
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Side, Font

# 假設匯率 1 USD = 135 JPY
exchange_rate = 135

# 以日圓為單位(資料內容)
data_in_yen = [
    [410932000000, 29758000000, 23452800000, 20429000000, 12001900000, None, None, None],  
    [100749000000, 88692000000, 66645000000, 59860000000, 27840000000, None, None, None],  
    [101487000000, 90826000000, 69150000000, 62241000000, 27970000000, None, None, None], 
    [70343000000, 62710000000, 48854000000, 41392000000, 18630000000, 15367000000, 13389000000, 8827000000],  
    [29442500000, 22408100000, 17035700000, 12123400000, 7984200000, 6121100000, 4584300000, 3245400000], 
    [11219200000, 6529400000, 4687100000, 5732200000, 2546000000, 2193200000, 1486900000, 748200000],  
    [29386000000, 22351600000, 16979200000, 12093700000, 7954500000, 6091500000, 4554700000, 3215700000],  
]

categories = ["營業額", "營業利益", "經常利益", "純利益", "股東權益", "總負債", "保留盈餘"]
years = ["2025", "2024", "2023", "2022", "2021", "2020", "2019", "2018"]

# 轉換為億 USD，缺失值用 "-"
data_in_usd = []
for row in data_in_yen:
    data_in_usd.append([round(value / exchange_rate / 100000000, 2) if value is not None else '-' for value in row])

# Excel 檔案路徑（程式資料夾）
script_folder = os.path.dirname(os.path.abspath(__file__))
xlsx_filename = os.path.join(script_folder, 'financial_data_usd.xlsx')

# 建立工作簿
wb = Workbook()
ws = wb.active
ws.title = "財務資料"

# 設定框線
thin_side = Side(style='thin')
thin_border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)

# 設定字型
default_font = Font(name='標楷體', size=14)
bold_font = Font(name='標楷體', size=14, bold=True)

# 寫入標題
ws.cell(row=1, column=1, value="西元年").border = thin_border
ws.cell(row=1, column=1).font = bold_font
ws.cell(row=1, column=1).alignment = Alignment(horizontal='center', vertical='center')

for col, year in enumerate(years, start=2):
    ws.cell(row=1, column=col, value=year).border = thin_border
    ws.cell(row=1, column=col).font = default_font
    ws.cell(row=1, column=col).alignment = Alignment(horizontal='center', vertical='center')

# 寫入科目與數字
for row_idx, category in enumerate(categories, start=2):
    # A 欄加粗字體
    ws.cell(row=row_idx, column=1, value=category).border = thin_border
    ws.cell(row=row_idx, column=1).font = bold_font
    ws.cell(row=row_idx, column=1).alignment = Alignment(horizontal='center', vertical='center')
    
    for col_idx, value in enumerate(data_in_usd[row_idx-2], start=2):
        ws.cell(row=row_idx, column=col_idx, value=value).border = thin_border
        ws.cell(row=row_idx, column=col_idx).font = default_font
        ws.cell(row=row_idx, column=col_idx).alignment = Alignment(horizontal='center', vertical='center')

# 最下面一列寫單位
unit_row = len(categories) + 2
ws.cell(row=unit_row, column=1, value="單位：億 USD").border = thin_border
ws.cell(row=unit_row, column=1).font = bold_font
ws.cell(row=unit_row, column=1).alignment = Alignment(horizontal='center', vertical='center')
for col in range(2, len(years)+2):
    ws.cell(row=unit_row, column=col).border = thin_border
    ws.cell(row=unit_row, column=col).font = default_font
    ws.cell(row=unit_row, column=col).alignment = Alignment(horizontal='center', vertical='center')

# 自動調整欄寬
for col in ws.columns:
    max_length = 0
    column = col[0].column_letter
    for cell in col:
        if cell.value:
            max_length = max(max_length, len(str(cell.value)))
    if column == 'A':
        ws.column_dimensions[column].width = int(max_length * 2.5)  # A欄放大1.5倍
    else:
        ws.column_dimensions[column].width = max_length + 4

# 儲存 Excel
wb.save(xlsx_filename)
print(f"Excel 文件已成功創建，存放在: {xlsx_filename}")
