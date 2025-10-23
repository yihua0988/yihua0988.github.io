# -*- coding: utf-8 -*-
"""
利用selenium動態搜尋及requests靜態抓取在yahoo news，複數的關鍵字搜尋想要找的新聞
"""

import requests
from bs4 import BeautifulSoup
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def fetch_news(keyword):
    url = f"https://tw.news.yahoo.com/search?p={keyword}&fr=uh3_news_web"

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    service = Service(executable_path="C:/chromedriver/chromedriver.exe")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    time.sleep(2)

    print("開始模擬滑鼠滾輪向下滾動載入新聞...")

    action = ActionChains(driver)
    start_time = time.time()
    max_wait = 30 
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        action.scroll_by_amount(0, 300).perform()  
        time.sleep(0.5)  

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height > last_height:
            last_height = new_height
            start_time = time.time()  
        else:
            if time.time() - start_time > max_wait:
                break

    print("滾動結束，開始抓取新聞資料...")

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    news_items = soup.find_all("h3", class_="Mb(5px)")
    results = []
    for h3 in news_items:
        a = h3.find("a")
        if a and a.text.strip():
            title = a.text.strip()
            href = a.get("href", "")
            link = href if href.startswith("http") else "https://tw.news.yahoo.com" + href
            results.append({"title": title, "link": link, "time": ""})

    return results


def fetch_time_from_article(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/137.0.0.0 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.encoding = 'utf-8'
        if resp.status_code != 200:
            return "無法取得時間"
        soup = BeautifulSoup(resp.text, "html.parser")
        time_tag = soup.find("time")
        if time_tag and time_tag.text.strip():
            return time_tag.text.strip()
        else:
            return "無時間資料"
    except Exception as e:
        return f"抓取時間錯誤: {e}"


def match_title(title, filters, mode):
    if not filters:
        return True
    title_low = title.lower()
    if mode == "any":
        return any(f.lower() in title_low for f in filters)
    else:
        return all(f.lower() in title_low for f in filters)


def main():
    keyword = input("請輸入主要搜尋關鍵字：").strip()
    if not keyword:
        print("你沒有輸入關鍵字，程式結束。")
        return

    print("正在使用 Selenium 開啟新聞搜尋頁，並模擬滑動載入全部結果...")
    news_list = fetch_news(keyword)
    if not news_list:
        print("找不到任何新聞。")
        return
    print(f"已成功載入 {len(news_list)} 則新聞。")

    filter_keywords = []
    print("\n請輸入最多五個進一步篩選條件（按 Enter 跳過）：")
    for i in range(5):
        kw = input(f"篩選條件 {i+1}: ").strip()
        if kw:
            filter_keywords.append(kw)

    while True:
        mode = input("篩選模式（輸入 'any' 表示符合任一條件，'all' 表示符合全部條件，預設為 'any'）: ").strip().lower()
        if mode == "":
            mode = "any"
            break
        if mode in ("any", "all"):
            break
        print("輸入錯誤，請輸入 'any' 或 'all'，或直接按 Enter 使用預設 'any'。")

    filtered_news = [n for n in news_list if match_title(n["title"], filter_keywords, mode)]

    if not filtered_news:
        print("沒有找到符合條件的新聞。")
        return

    print(f"\n共找到 {len(filtered_news)} 則符合條件的新聞，開始抓取內文時間...")
    for news in filtered_news:
        news['time'] = fetch_time_from_article(news['link'])
        time.sleep(1)

    print("\n結果：")
    for idx, news in enumerate(filtered_news, 1):
        print(f"標題 {idx}: {news['title']}")
        print(f"連結: {news['link']}")
        print(f"時間: {news['time']}")
        print("-" * 40)


if __name__ == "__main__":
    main()
