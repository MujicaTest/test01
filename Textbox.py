import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webelement import WebElement

t = 5

driver = webdriver.Chrome(executable_path='../../Downloads/Web_Test/chromedriver');
driver.get('https://demoqa.com/checkbox')



#driver.find_element(By.CLASS_NAME,"rct-checkbox").click()
btn1 = driver.find_element(By.CLASS_NAME,"rct-checkbox")
btn1.click()
btn1.click()

time.sleep(t)
driver.close()
