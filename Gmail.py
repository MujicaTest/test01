import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('../../Downloads/Web_Test/chromedriver')  # Optional argument, if not specified will search path.

driver.get('https://sede.administracionespublicas.gob.es/pagina/index/directorio/icpplus')
driver.find_element(By.ID,'submit')

time.sleep(5)  # Let the user actually see something!

search_box = driver.find_element(By.NAME,'q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5)  # Let the user actually see something!

driver.quit()
