from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.python.org/")
print(driver.title)
time.sleep(5)
driver.get("https://www.udemy.com/")
time.sleep(5)
print(driver.title)
driver.back()
time.sleep(5)
print(driver.title)
driver.forward()
time.sleep(5)
print(driver.title)


