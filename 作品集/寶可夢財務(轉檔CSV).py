"""
另用python程式轉化資料為csv
"""
import csv

# 假設的匯率 1 USD = 135 JPY
exchange_rate = 135

# 以日圓為單位
data_in_yen = [
    [410932000000, 29758000000, 23452800000, 20429000000, 12001900000, None, None, None],  
    [100749000000, 88692000000, 66645000000, 59860000000, 27840000000, None, None, None],  
    [101487000000, 90826000000, 69150000000, 62241000000, 27970000000, None, None, None], 
    [70343000000, 62710000000, 48854000000, 41392000000, 18630000000, 15367000000, 13389000000, 8827000000],  
    [29442500000, 22408100000, 17035700000, 12123400000, 7984200000, 6121100000, 4584300000, 3245400000], 
    [11219200000, 6529400000, 4687100000, 5732200000, 2546000000, 2193200000, 1486900000, 748200000],  
    [29386000000, 22351600000, 16979200000, 12093700000, 7954500000, 6091500000, 4554700000, 3215700000],  
]

# 轉換為美金
data_in_usd = []
for row in data_in_yen:
    # 除以匯率後將單位從「萬」轉換為「億」，即除以 10000
    data_in_usd.append([round(value / exchange_rate / 100000000, 2) if value is not None else '-' for value in row])

csv_filename = r'D:\專案\financial_data_usd.csv'

categories = ["營業額", "營業利益", "經常利益", "純利益", "股東權益", "總負債", "保留盈餘"]
years = ["2025", "2024", "2023", "2022", "2021", "2020", "2019", "2018"]

with open(csv_filename, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(["科目"] + years)
    for i, category in enumerate(categories):
        writer.writerow([category] + data_in_usd[i])

print(f"CSV 文件已經成功創建，並存儲在 {csv_filename}。")
