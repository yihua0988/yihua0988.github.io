"""
利用requests找出在pchome網站上更符合自己需求的商品，並存成Excel
最多抓取 100 頁，Excel 存到桌面
"""
import requests
import time
import os
import pandas as pd

# 取得桌面路徑
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
output_folder = os.path.join(desktop, "pchome_results")
os.makedirs(output_folder, exist_ok=True)

# 顯示目前工作目錄
print("程式執行工作目錄：", os.getcwd())
print("Excel 將存放在：", output_folder)

# 使用者輸入
search_term = input("請輸入搜尋關鍵字：").strip()
filter_keyword = input("請輸入需篩選的品名關鍵字（可空白）：").strip()
min_price = input("請輸入最低價格（可空白）：").strip()
max_price = input("請輸入最高價格（可空白）：").strip()

min_price = int(min_price) if min_price.isdigit() else 0
max_price = int(max_price) if max_price.isdigit() else float("inf")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Referer": "https://24h.pchome.com.tw/"
}

base_url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results"
page = 1
total_products = 0
matched_products = 0
max_pages = 100  # 最多抓 100 頁

all_products = []

while page <= max_pages:
    params = {
        "q": search_term,
        "page": page,
        "sort": "rnk/dc"
    }

    response = requests.get(base_url, headers=headers, params=params)

    # 嘗試解析 JSON
    try:
        data = response.json()
    except requests.exceptions.JSONDecodeError:
        print("❌ 回傳不是 JSON，可能是網頁錯誤或被擋住")
        break
    products = data.get("prods", [])
    if not products:
        print(f"\n🔚 第 {page} 頁沒有商品，結束抓取")
        break

    print(f"\n第 {page} 頁，共 {len(products)} 件商品")
    for product in products:
        name = product.get("name", "")
        price = product.get("price", 0)
        pid = product.get("Id", "")
        link = f"https://24h.pchome.com.tw/prod/{pid}"

        if filter_keyword and filter_keyword not in name:
            continue
        if not (min_price <= price <= max_price):
            continue

        # 將商品資訊存入 list
        all_products.append({
            "商品名稱": name,
            "價格": price,
            "連結": link
        })

        print(f"商品名稱: {name}")
        print(f"價格: {price} 元")
        print(f"連結: {link}")
        print("-" * 40)
        matched_products += 1

    total_products += len(products)
    page += 1
    time.sleep(1)  # 避免頻繁請求被封

print("\n🔹 抓取結束")

# 將結果存成 Excel
if all_products:
    df = pd.DataFrame(all_products)
    filename = os.path.join(output_folder, f"pchome_{search_term}.xlsx")
    df.to_excel(filename, index=False)
    print(f"✅ 已將符合條件的商品存成 Excel：{filename}")
else:
    print("⚠️ 沒有符合條件的商品，不產生 Excel")

print(f"\n共搜尋到 {total_products} 件商品，符合條件的有 {matched_products} 件。")
