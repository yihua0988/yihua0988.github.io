# -*- coding: utf-8 -*-
"""
PTT 精準搜尋（三瀏覽器通用 + 自動 driver 下載）
功能：
 - 支援 Chrome / Edge / Firefox（webdriver_manager 自動安裝 driver）
 - 取得：看板、主要關鍵字、進階篩選、年份、完整時間/列表日期、標題、作者、連結
 - 儲存到當前資料夾 PTT搜尋紀錄.xlsx（若已存在則追加）
"""
import os
import sys
import time
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

sys.stderr = open(os.devnull, 'w')
def get_driver():
    # Chrome
    try:
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--log-level=3")  
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        print("✅ 使用 Chrome 瀏覽器")
        return driver
    except Exception as e:
        print("❌ Chrome 啟動失敗：", e)

    # Edge
    try:
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless=new")
        edge_options.add_argument("--disable-gpu")
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")
        edge_options.add_argument("--log-level=3")
        edge_options.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
        print("✅ 使用 Edge 瀏覽器")
        return driver
    except Exception as e:
        print("❌ Edge 啟動失敗：", e)

    # Firefox
    try:
        # 隱藏 geckodriver 和 selenium 的錯誤訊息
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")       
        firefox_options.log.level = "fatal"             

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=firefox_options
        )
        print("✅ 使用 Firefox 瀏覽器")
        return driver

    except Exception as e:
            print("❌ Firefox 啟動失敗：", e)

    raise RuntimeError("⚠️ 找不到任何可用的瀏覽器 Driver。請確認系統有安裝 Chrome、Edge 或 Firefox。")

def extract_full_time_from_article(driver, article_url):
    """嘗試從文章中抓取完整發文時間與年份"""
    try:
        driver.execute_script("window.open(arguments[0], '_blank');", article_url)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)

        meta_lines = driver.find_elements(By.CSS_SELECTOR, "div.article-metaline")
        for line in meta_lines:
            try:
                tag = line.find_element(By.CLASS_NAME, "article-meta-tag").text.strip()
                if tag == "時間":
                    raw_time = line.find_element(By.CLASS_NAME, "article-meta-value").text.strip()
                    try:
                        dt = datetime.strptime(raw_time, "%a %b %d %H:%M:%S %Y")
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        return dt.strftime("%Y-%m-%d %H:%M:%S"), dt.year
                    except ValueError:
                        # 無法解析時間格式，回傳原字串
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])
                        return raw_time, None
            except:
                continue

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return None, None

    except Exception:
        # 若出錯，確保關閉分頁
        try:
            if len(driver.window_handles) > 1:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
        except:
            pass
        return None, None

def crawl_ptt(board, main_keyword, extra_keywords, max_pages=5):
    driver = get_driver()
    base_url = f"https://www.ptt.cc/bbs/{board}/search?q={main_keyword}"
    driver.get(base_url)
    time.sleep(1)

    # 通過年齡驗證頁面
    try:
        if "over18" in driver.current_url:
            try:
                driver.find_element(By.NAME, "yes").click()
            except:
                try:
                    driver.find_element(By.XPATH, '//button[text()="我同意，我已年滿十八歲"]').click()
                except:
                    pass
            time.sleep(1)
    except:
        pass

    records = []
    page = 1
    while page <= max_pages:
        print(f"📄 正在爬取第 {page} 頁...")
        time.sleep(1)

        entries = driver.find_elements(By.CSS_SELECTOR, "div.r-ent")
        if not entries:
            break

        for ent in entries:
            try:
                title_elem = ent.find_element(By.CSS_SELECTOR, "div.title")
                links = title_elem.find_elements(By.TAG_NAME, "a")
                if not links:
                    continue
                title = links[0].text.strip()
                href = links[0].get_attribute("href")
                author = ent.find_element(By.CSS_SELECTOR, "div.meta div.author").text.strip()
                date_text = ent.find_element(By.CSS_SELECTOR, "div.meta div.date").text.strip()  # e.g. 11/06

                # 關鍵字過濾
                if extra_keywords:
                    if not all(k.lower() in title.lower() for k in extra_keywords):
                        continue

                # 抓完整時間
                full_time, year = extract_full_time_from_article(driver, href)

                # 若抓不到完整時間，用列表日期補年份
                if not full_time:
                    try:
                        m, d = date_text.strip().split("/")
                        m, d = int(m), int(d)
                        now = datetime.now()
                        if (m, d) > (now.month, now.day):
                            guessed_year = now.year - 1
                        else:
                            guessed_year = now.year
                        full_time = f"{guessed_year}-{m:02d}-{d:02d}"
                        year = guessed_year
                    except:
                        full_time = date_text
                        year = datetime.now().year

                records.append({
                    "看板": board,
                    "主要關鍵字": main_keyword,
                    "進階篩選": " ".join(extra_keywords),
                    "年份": year,
                    "完整時間或列表日期": full_time,
                    "標題": title,
                    "作者": author,
                    "連結": href
                })
            except Exception:
                continue

        # 上頁連結
        try:
            prev_link = driver.find_element(By.LINK_TEXT, "‹ 上頁")
            href = prev_link.get_attribute("href")
            if not href:
                break
            driver.get(href)
            page += 1
        except:
            break

    driver.quit()
    return records

def save_to_excel(records, filename="PTT搜尋紀錄.xlsx"):
    if not records:
        print("⚠️ 沒有資料可儲存。")
        return

    df = pd.DataFrame(records)
    save_path = os.path.join(os.getcwd(), filename)
    if os.path.exists(save_path):
        try:
            old_df = pd.read_excel(save_path)
            df = pd.concat([old_df, df], ignore_index=True)
        except Exception as e:
            print("讀取舊檔失敗：", e)
    df.to_excel(save_path, index=False)
    print(f"✅ 已儲存至 {save_path}")

def main():
    board = input("請輸入看板名稱（例如 NBA）：").strip()
    main_keyword = input("請輸入主要搜尋關鍵字：").strip()
    extra_input = input("如需進一步篩選標題，請輸入其他關鍵字（空格分隔，可跳過）：").strip()
    extra_keywords = extra_input.split() if extra_input else []

    print(f"\n開始搜尋 看板={board}，主要關鍵字={main_keyword}，進階篩選={' '.join(extra_keywords)}\n")
    records = crawl_ptt(board, main_keyword, extra_keywords)
    print(f"\n共擷取到 {len(records)} 筆資料。")
    save_to_excel(records)


if __name__ == "__main__":
    main()
