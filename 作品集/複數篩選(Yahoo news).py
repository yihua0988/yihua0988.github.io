# -*- coding: utf-8 -*-
"""
Yahoo News 搜尋多關鍵字 + 篩選 + 時間抓取
支援：
1. 滾動載入 + 點擊「更多新聞」
2. 分頁抓取
3. 篩選條件 any/all
4. 抓取文章發佈時間
"""

import os
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

# ===== 隱藏所有雜訊輸出 =====
os.environ['WDM_LOG_LEVEL'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['PYTHONWARNINGS'] = 'ignore'


def fetch_news(keyword, max_pages=5):
    """抓取 Yahoo News 搜尋結果，多頁抓取"""
    base_url = f"https://tw.news.yahoo.com/search?p={keyword}"

    # ---- Chrome 啟動設定 ----
    options = Options()
    options.add_argument("--headless=new")  # 新版 headless
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-webgl")  # 避免 WebGL 錯誤
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--log-level=3")  # 只顯示嚴重錯誤
    options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 隱藏 DevTools
    options.add_argument("--disable-logging")

    service = Service(executable_path="C:/chromedriver/chromedriver.exe")

    # ---- 建立瀏覽器 ----
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(base_url)
    time.sleep(2)

    print("開始模擬滾動 + 點擊更多新聞...")

    action = ActionChains(driver)
    all_news = []

    for page in range(max_pages):
        last_height = driver.execute_script("return document.body.scrollHeight")
        scroll_start = time.time()
        max_wait = 10

        while True:
            action.scroll_by_amount(0, 800).perform()
            time.sleep(0.5)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height > last_height:
                last_height = new_height
                scroll_start = time.time()
            elif time.time() - scroll_start > max_wait:
                break

        # 嘗試點擊「更多新聞」
        try:
            more_btn = driver.find_element(By.XPATH, '//button[contains(text(),"更多新聞")]')
            more_btn.click()
            time.sleep(2)
        except NoSuchElementException:
            break

    # 擷取新聞列表
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    news_items = soup.select("li div h3 a")
    results = []
    for a in news_items:
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

    print("正在使用 Selenium 開啟新聞搜尋頁，並模擬滾動 + 點擊更多新聞...")
    news_list = fetch_news(keyword, max_pages=10)
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
