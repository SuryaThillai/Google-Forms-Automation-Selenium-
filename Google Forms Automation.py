from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
import time
from houseinfo import price,address,links,Houseinfo

web_driver_path = "/Users/surya/Documents/Chrome Driver/chromedriver"

serv = Service(web_driver_path)

options = ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=serv,options=options)

driver.get("https://forms.gle/wMtHT7ZFc7mubVLR7")

time.sleep(3)

info = Houseinfo()

for i in range(len(price)):

    address_entry = driver.find_elements(by=By.CSS_SELECTOR, value="div.Xb9hP input")[0]
    address_entry.send_keys(info.address[i])

    price_entry = driver.find_elements(by=By.CSS_SELECTOR, value="div.Xb9hP input")[1]
    price_entry.send_keys(info.price[i])

    link_entry = driver.find_elements(by=By.CSS_SELECTOR, value="div.Xb9hP input")[2]
    link_entry.send_keys(info.links[i])

    button = driver.find_element(by=By.CSS_SELECTOR, value="div.QvWxOd")
    button.click()

    time.sleep(3)

    driver.back()


