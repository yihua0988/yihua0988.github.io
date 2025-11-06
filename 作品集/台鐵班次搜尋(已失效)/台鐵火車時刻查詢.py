"""
利用openpyxl先開啟"台鐵車站代碼.pdf"尋找要出發及抵達的站代碼，再用requests抓取自行輸入的時間區間"自強號"班次及票價(有利用platform可以讓全部作業系統都是用這個程式)
"""
import requests
from bs4 import BeautifulSoup
import openpyxl
import os
import platform

pdf_path = "台鐵車站代碼.pdf"

def open_pdf(path):
    system = platform.system()
    try:
        if system == "Windows":
            os.startfile(path)
        elif system == "Darwin": 
            os.system(f"open '{path}'")
        else:  
            os.system(f"xdg-open '{path}'")
    except Exception as e:
        print(f"開啟PDF失敗: {e}")

open_pdf(pdf_path)

print("請用『台鐵車站代碼.pdf』尋找車站代碼並且複製貼上做搜尋")

url = "https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime"

start_station = input("請輸入起點站（例如 1000-臺北）: ")
end_station = input("請輸入終點站（例如 3300-臺中）: ")
ride_date = input("請輸入搭乘日期（格式 YYYY/MM/DD，例如 2025/06/13）: ")

post_data = {
    "startStation": start_station,
    "endStation": end_station,
    "transfer": "ONE",
    "rideDate": ride_date,
    "startOrEndTime": "true",
    "startTime": "00:00",
    "endTime": "23:59",
    "trainTypeList": "ALL",   
    "query": "查詢"
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime"
}

response = requests.post(url, data=post_data, headers=headers)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")

search_time_span = soup.select_one("div.text-right > span")
search_time = search_time_span.text.replace("查詢時間:", "") if search_time_span else ""

ride_date_input = soup.find("input", id="rideDate")
query_date = ride_date_input["value"] if ride_date_input else post_data["rideDate"]

table = soup.find("table", class_="itinerary-controls")
if not table:
    print("查無資料或表格未找到！")
    exit()

rows = table.find_all("tr")

header_cols = [th.get_text(strip=True).replace("\n", "") for th in rows[0].find_all("th")]
cols_to_remove = []
for col_name in ["詳細資訊", "訂票"]:
    if col_name in header_cols:
        cols_to_remove.append(header_cols.index(col_name))
clean_header = [col for i, col in enumerate(header_cols) if i not in cols_to_remove]

data = []
data.append(clean_header)

for row in rows[1:]:
    cols = [td.get_text(strip=True).replace("\n", "") for td in row.find_all("td")]
    if any("區間" in c for c in cols):
        continue
    if len(cols) == len(header_cols):
        clean_cols = [col for i, col in enumerate(cols) if i not in cols_to_remove]
        data.append(clean_cols)

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "台鐵時刻"

ws.append([f"查詢時間：{search_time}"])
ws.append([f"查詢日期：{query_date}"])
ws.append([f"{start_station} 到 {end_station}"])
ws.append([])

for row_data in data:
    ws.append(row_data)

ws.column_dimensions['A'].width = 45  # A欄 3倍寬 (預設約15)
ws.column_dimensions['D'].width = 22  # D欄 1.5倍寬 (預設約15)

excel_file = "TaiwanRailway_filtered.xlsx"
wb.save(excel_file)

print(f"Excel 檔案已儲存：{excel_file}")