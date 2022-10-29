import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

t = 5

driver = webdriver.Chrome(executable_path='../../Downloads/Web_Test/chromedriver');
driver.get('https://demoqa.com/checkbox')


try:
    btn1 = driver.find_element(By.CLASS_NAME,"rct-checkbox")
    btn1.click()
    btn1.click()

except TimeoutException as ex:
    print(ex.msg)
    print("el elemento no esta disponible")
    driver.quit()

time.sleep(t)
driver.close()


driver.get('https://demoqa.com/upload-download')
driver.maximize_window()
time.sleep(t)
