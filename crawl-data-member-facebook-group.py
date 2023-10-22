from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 1. Khai bao bien browser
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 2. Mở thử một trang web
browser.get("http://facebook.com")

# 2a. Điền thông tin vào ô user và pass
txtUser = browser.find_element(By.ID, "email")
txtUser.send_keys("[your_mail]")

txtPass = browser.find_element(By.ID, "pass")
txtPass.send_keys("[your_password]")

# 2b. Submit form
txtPass.send_keys(Keys.ENTER)


# 3. Dừng chương trình 5 giây
sleep(5)

# 4. Đóng trình duyệt

browser.get("https://www.facebook.com/groups/400575940667899/members")


sleep(10)
comment_list = browser.find_elements(By.XPATH, "//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f']")

for comment in comment_list:
    print(comment.text)

browser.close()
