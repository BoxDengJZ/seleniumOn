import time

from selenium import webdriver

drive = webdriver.Chrome()
drive.implicitly_wait(15)
drive.maximize_window()
drive.get("https://twitter.com/Google")
for _ in range(15):
    time.sleep(2)
    drive.execute_script("window.scrollTo(0, document.body.scrollHeight)")
