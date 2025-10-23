"""
利用requests找出在pchome網站上更符合自己需求的商品
"""
import requests
import time

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

while True:
    params = {
        "q": search_term,
        "page": page,
        "sort": "rnk/dc"
    }

    response = requests.get(base_url, headers=headers, params=params)
    data = response.json()

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

        print(f"商品名稱: {name}")
        print(f"價格: {price} 元")
        print(f"連結: {link}")
        print("-" * 40)
        matched_products += 1

    total_products += len(products)
    page += 1
    time.sleep(1)
    
print(f"\n共搜尋到 {total_products} 件商品，符合條件的有 {matched_products} 件。")
