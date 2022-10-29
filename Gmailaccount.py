from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('../../Downloads/Web_Test/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('https://mail.google.com/mail/u/0/');
#username = driver.find_element(By.ID, "user_email")
#username.send_keys("andres.mujica@crisalix.com")
time.sleep(1)