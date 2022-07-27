from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)

driver.get("https://www.ncku.edu.tw/p/412-1000-24945.php?Lang=zh-tw")
print(driver.title)
html = driver.page_source
print(html)

driver.quit()
