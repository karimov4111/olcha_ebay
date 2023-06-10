import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.ebay.com/sch/i.html?_nkw=headphones&_sacat=0")
time.sleep(5)
past = driver.find_element(By.XPATH, "//h2[@class='srp-answer__title']")
driver.execute_script("arguments[0].scrollIntoView()", past)
time.sleep(5)
all_url=driver.find_elements(By.XPATH, "//ol/li/a[@class='pagination__item']")
link1=[]

for i in all_url[1:]:
    i.click()
    link1=driver.current_url
    time.sleep(5)
    past = driver.find_element(By.XPATH, "//h2[@class='srp-answer__title']")
    driver.execute_script("arguments[0].scrollIntoView()", past)
    driver.execute_script("window.scrollBy(0,-200)", "")
    time.sleep(5)


    
print(link1)
