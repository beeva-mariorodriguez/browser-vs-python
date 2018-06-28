#!/usr/bin/env python3

# install selenium 3
#   pip install selenium
# install chromedriver
#   sudo apt install chromium-chromedriver
#   or download from https://chromedriver.storage.googleapis.com/index.html?path=2.38/

import time
from selenium import webdriver

if __name__ == "__main__":
    opt = webdriver.ChromeOptions()
    opt.add_argument("no-first-run")
    opt.add_argument("disable-infobars")
    opt.add_argument("disable-extensions")
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.content_settings.exceptions.media_stream_camera.http://localhost:8080.setting": 1
      })
    browser = webdriver.Chrome(
        executable_path="/usr/lib/chromium-browser/chromedriver",
        options=opt)
    while True:
        browser.get('https://google.es/')
        time.sleep(10)
        browser.get('https://duckduckgo.com')
        time.sleep(10)
