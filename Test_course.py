import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='../../Downloads/Web_Test/chromedriver')
#driver2 = webdriver.Chrome(executable_path="../../Downloads/Web_Test/geckodriver")

driver.get('https://demoqa.com/text-box')
driver.maximize_window()
time.sleep(2)

name= driver.find_element(By.XPATH,"//input[contains(@id,'userName')]")
name.send_keys('Rodrigo')
time.sleep(2)
driver.find_element(By.XPATH,"//input[contains(@id,'userEmail')]").send_keys('Rodrigo@gmail.com')
time.sleep(2)
driver.execute_script('window.scrollTo(0,500)')
driver.close()