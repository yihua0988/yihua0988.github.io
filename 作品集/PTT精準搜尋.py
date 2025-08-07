import logging
logging.basicConfig(level=logging.INFO)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from datetime import datetime
import time
import os
import re
import requests
from PIL import Image
import matplotlib.pyplot as plt

def parse_push(push_str):
    try:
        if push_str == '爆':
            return 100, 100, 0
        elif push_str.startswith('X'):
            val = -int(push_str[1:])
            return val, 0, abs(val)
        elif push_str.isdigit():
            val = int(push_str)
            return val, val, 0
        else:
            return 0, 0, 0
    except:
        return 0, 0, 0

def download_image(img_url, save_folder, filename):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        r = requests.get(img_url, stream=True, timeout=10, headers=headers)
        if r.status_code == 200:
            filepath = os.path.join(save_folder, filename)
            with open(filepath, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
            print(f"下載完成: {filename}")
            return filepath
        else:
            print(f"下載失敗，狀態碼: {r.status_code} - {img_url}")
    except:
        pass
    return None

def show_image_spyder(filepath, title=None):
    try:
        img = Image.open(filepath)
        plt.imshow(img)
        plt.axis('off')
        if title:
            try:
                plt.title(title)
            except:
                pass
        plt.show()
        print(f"在Spyder內顯示圖片: {filepath}")
    except Exception as e:
        print(f"顯示圖片失敗: {e}")

def extract_image_urls_from_text(text):
    pattern = r'(https?://[^\s]+?\.(?:jpg|jpeg|png|gif))'
    urls = re.findall(pattern, text, flags=re.IGNORECASE)
    return list(set(urls))

def main():
    board = input("請輸入看板名稱（例如 NBA）：").strip()
    main_keyword = input("請輸入主要搜尋關鍵字：").strip()
    if not main_keyword:
        print("請至少輸入一個主要搜尋關鍵字！")
        return
    filter_input = input("如需進一步篩選標題，請輸入其他關鍵字（空格分隔，可跳過）：").strip()
    keywords = [main_keyword] + filter_input.split() if filter_input else [main_keyword]

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service("C:/chromedriver/chromedriver.exe") 
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(f"https://www.ptt.cc/bbs/{board}/index.html")
        try:
            WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, '//button[text()="我同意，我已年滿十八歲"]'))
            ).click()
            print("已通過年齡驗證頁面")
        except TimeoutException:
            pass

        base_url = f"https://www.ptt.cc/bbs/{board}/search?page={{}}&q={keywords[0]}"
        print(f"開始搜尋看板 {board} ，關鍵字: {keywords[0]}")

        articles = []
        max_pages = 10

        for page_num in range(1, max_pages + 1):
            url = base_url.format(page_num)
            driver.get(url)
            time.sleep(1)

            entries = driver.find_elements(By.CSS_SELECTOR, "div.r-ent")
            if not entries:
                print(f"第{page_num}頁無文章，結束搜尋。")
                break

            for entry in entries:
                try:
                    title_elem = entry.find_element(By.CSS_SELECTOR, "div.title a")
                    title_text = title_elem.text.strip()
                    href = title_elem.get_attribute("href")
                except NoSuchElementException:
                    continue

                if len(keywords) > 1:
                    title_lower = title_text.lower()
                    if not all(k.lower() in title_lower for k in keywords[1:]):
                        continue

                author = entry.find_element(By.CSS_SELECTOR, "div.meta div.author").text
                push_str = entry.find_element(By.CSS_SELECTOR, "div.nrec").text
                push_num, push_up, push_down = parse_push(push_str)

                driver.execute_script("window.open(arguments[0]);", href)
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(1)

                try:
                    meta_lines = driver.find_elements(By.CSS_SELECTOR, "div.article-metaline")
                    article_time = "無法取得時間"
                    for line in meta_lines:
                        tag = line.find_element(By.CLASS_NAME, "article-meta-tag").text
                        if tag == "時間":
                            raw_time = line.find_element(By.CLASS_NAME, "article-meta-value").text
                            dt = datetime.strptime(raw_time, "%a %b %d %H:%M:%S %Y")
                            article_time = dt.strftime("%Y-%m-%d %H:%M:%S")
                            break
                except:
                    article_time = "無法取得時間"

                try:
                    main_content = driver.find_element(By.ID, "main-content").text
                    lines = main_content.split('\n')
                    content_lines = []
                    for line in lines:
                        line = line.strip()
                        if any(x in line for x in ["作者", "標題", "時間", "發信站", "看板"]):
                            continue
                        if line.startswith('推') or line.startswith('噓') or line.startswith('→'):
                            continue
                        if line.startswith('--'):
                            break
                        if line:
                            content_lines.append(line)
                    content_preview = ''.join(content_lines)[:200]
                except Exception:
                    content_preview = ""

                images = extract_image_urls_from_text(main_content)

                driver.close()
                driver.switch_to.window(driver.window_handles[0])

                articles.append({
                    "title": title_text,
                    "author": author,
                    "link": href,
                    "push": push_num,
                    "push_up": push_up,
                    "push_down": push_down,
                    "time": article_time,
                    "content_preview": content_preview,
                    "images": images  
                })

            print(f"已完成第 {page_num} 頁搜尋，累積文章數：{len(articles)}")

    finally:
        driver.quit()

    if not articles:
        print("沒有符合條件的文章。")
        return

    print(f"\n符合條件的文章共 {len(articles)} 篇：\n")
    for idx, art in enumerate(articles, 1):
        print(f"文章 {idx}:")
        print(f"標題: {art['title']}")
        print(f"作者: {art['author']}")
        print(f"連結: {art['link']}")
        print(f"時間: {art['time']}")
        print(f"點擊率 (推噓數): {art['push']}")
        print(f"好評推: {art['push_up']}, 差評噓: {art['push_down']}")
        print(f"內文摘要（前200字）: {art['content_preview']}")
        print(f"內文中圖片數量: {len(art['images'])}")
        print("-" * 40)

    save_folder = os.path.join("downloaded_images", board)
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    for idx, art in enumerate(articles, 1):
        if not art["images"]:
            continue
        print(f"\n文章 {idx} 《{art['title']}》 下載圖片中...")
        for img_idx, img_url in enumerate(art["images"][:3], 1):  
            ext = img_url.split('.')[-1].split('?')[0]
            safe_title = ''.join(c if c.isalnum() else '_' for c in art['title'][:10])
            filename = f"{safe_title}_{idx}_{img_idx}.{ext}"
            filepath = download_image(img_url, save_folder, filename)
            if filepath:
                try:
                    img = Image.open(filepath)
                    plt.imshow(img)
                    plt.axis('off')
                    plt.title(f"文章 {idx}：《{art['title']}》圖片 {img_idx}")
                    plt.show()
                    print(f"在Spyder內顯示圖片: {filepath}")
                except Exception as e:
                    print(f"顯示圖片失敗: {e}")
                time.sleep(1)

if __name__ == "__main__":
    main()