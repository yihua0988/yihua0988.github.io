# -*- coding: utf-8 -*-
"""
利用requests抓取中油json當週油價，以及用datetime顯示今天日期，再用PyQt5設計桌面UI做顯示(可自行放"啟動"資料夾做一個開機程式顯示當週油價)
"""
import sys
import requests
import urllib3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import re
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class DesktopWidget(QWidget):
    def __init__(self):
        super().__init__()
        # 設定為無邊框、工具視窗，且永遠在最前面
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background-color: rgba(255, 255, 255, 200); border: 1px solid #888;")

        self.initUI()
        self.resize(int(380 * 0.66), int(160 * 0.66))
        self.update_data()  # 啟動時抓一次

        # 右上角定位
        screen_width = self.screen().size().width()
        self.move(screen_width - self.width() - 20, 20)

    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 10, 15, 10)
        self.setLayout(main_layout)

        title_layout = QHBoxLayout()
        self.label_title = QLabel("今日油價")
        self.label_title.setFont(QFont("Microsoft JhengHei", 16, QFont.Bold))
        self.label_title.setStyleSheet("color: #333333;")
        self.label_date = QLabel(datetime.today().strftime("%Y-%m-%d"))
        self.label_date.setFont(QFont("Microsoft JhengHei", 10))
        self.label_date.setStyleSheet("color: #555555;")
        title_layout.addWidget(self.label_title)
        title_layout.addWidget(self.label_date)
        title_layout.addStretch()
        main_layout.addLayout(title_layout)

        self.label_updown = QLabel("")
        self.label_updown.setFont(QFont("Microsoft JhengHei", 12, QFont.Bold))
        main_layout.addWidget(self.label_updown)

        self.label_price = QLabel("")
        self.label_price.setFont(QFont("Microsoft JhengHei", 11))
        main_layout.addWidget(self.label_price)

        self.label_time = QLabel("")
        self.label_time.setFont(QFont("Microsoft JhengHei", 9))
        main_layout.addWidget(self.label_time)

    def update_data(self):
        self.label_date.setText(datetime.today().strftime("%Y-%m-%d"))
        try:
            r = requests.get(
                "https://www.cpc.com.tw/GetOilPriceJson.aspx?type=TodayOilPriceString",
                timeout=10,
                verify=False
            )
            r.raise_for_status()
            data = r.json()

            self.label_time.setText(f"更新時間：{data.get('PriceUpdate', '未知')}")

            # 漲跌顯示紅綠文字
            updown_html = data.get('UpOrDown_Html', '')
            match = re.search(r'調(漲|降).*?<i>([\d.]+)</i>', updown_html)
            if match:
                direction, rate = match.group(1), float(match.group(2))
                color = "red" if direction == "漲" else "green"
                self.label_updown.setStyleSheet(f"color: {color}; font-weight: bold;")
                self.label_updown.setText(f"本週油價：{direction} {rate:.1f} 元")
            else:
                self.label_updown.setText("本週油價：無變動")
                self.label_updown.setStyleSheet("color: gray;")

            price_texts = [
                f"92無鉛：{data.get('sPrice1', '-')} 元",
                f"95無鉛：{data.get('sPrice2', '-')} 元",
                f"98無鉛：{data.get('sPrice3', '-')} 元",
                f"酒精汽油：{data.get('sPrice4', '-')} 元",
                f"超級柴油：{data.get('sPrice5', '-')} 元",
                f"液化石油氣：{data.get('sPrice6', '-')} 元",
            ]
            self.label_price.setText("\n".join(price_texts))

        except Exception as e:
            print("Fetch error:", e)
            self.label_title.setText("⚠️ 油價更新失敗")
            self.label_price.setText("請檢查網路連線或稍後再試")
            self.label_updown.setText("")
            self.label_time.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = DesktopWidget()
    w.show()
    sys.exit(app.exec_())
