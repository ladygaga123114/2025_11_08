import os
from playwright.sync_api import sync_playwright

def get_html_path(filename: str) -> str:
    """返回HTML文件的絕對路徑"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(current_dir, filename)
    return f"file://{html_path}"

def main():
    # 這裡指定要開啟的 HTML 檔案名稱
    html_filename = "waiting_demo.html"  # 你可以改成其他檔名
    path = get_html_path(html_filename)
    with sync_playwright() as p:
        # 啟動瀏覽器
        browser = p.chromium.launch(headless=False, slow_mo=500)

        # 打開新頁面
        page = browser.new_page()

        page.goto(path)

        page.wait_for_timeout(3000)  # 等待3秒以觀察效果

        browser.close()

if __name__ == "__main__":
    main()