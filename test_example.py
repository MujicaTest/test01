from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

service = Service('../../Downloads/Web_Test/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get('');
username = driver.find_element(By.ID, "user_email")
username.send_keys("")
time.sleep(1)
password = driver.find_element(By.ID, "user_password")
password.send_keys("")
time.sleep(1)

# enter to home
driver.find_element(By.NAME,'commit').click()

# enter to patient list

driver.find_element(By.CLASS_NAME,"dashboard-menu-item__btn-text").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "btn.btn--primary.table-header__add-patient").click()

# Adding the patients name
time.sleep(2)
patient_name = driver.find_element(By.XPATH,'//*[@id="patient_first_name"]')


# Adding last name

patient_Last_name = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/form/div[2]/input")

# Adding email

patient_email = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/form/div[3]/input')

# adding date of birth

patient_b1 = Select(driver.find_element(By.ID,'patient_birthday_1i'))

patient_b2 = Select(driver.find_element(By.ID,'patient_birthday_2i'))

patient_b3 = Select(driver.find_element(By.ID,'patient_birthday_3i'))


#filling the fields

patient_name.send_keys("Andres_test")
patient_Last_name.send_keys("Mujica_test")
patient_email.send_keys("andres.mujica+testautomated6@crisalix.com")
time.sleep(1)
patient_b1.select_by_visible_text("1989")
time.sleep(1)
patient_b2.select_by_visible_text("May")
time.sleep(1)
patient_b3.select_by_visible_text('17')
time.sleep(1)
#saving patient

driver.find_element(By.NAME, "commit").click()
time.sleep(1)
#Moving arround
#Moving to visualizations
driver.find_element(By.XPATH, "/html/body/div[1]/div/ul/li[2]/a").click()
time.sleep(1)
#Moving to Before and after
driver.find_element(By.XPATH, "/html/body/div[1]/div/ul/li[3]/a").click()
#Moving to edit profile
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[2]/a/span').click()
time.sleep(1)
#preconsultation form
#arreglar no sirve
#driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div[2]/div/a').click()

driver.find_element(By.CLASS_NAME,'user-info__edit-profile-text').click()

#editing profile

# Adding the patients name
time.sleep(2)
patient_name = driver.find_element(By.XPATH,'//*[@id="patient_first_name"]')
patient_name.clear()

# Adding last name

patient_Last_name = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/form/div[2]/input")
patient_Last_name.clear()
# Adding email

patient_email = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/form/div[3]/input')
patient_email.clear()
# adding date of birth

patient_b1 = Select(driver.find_element(By.ID,'patient_birthday_1i'))

patient_b2 = Select(driver.find_element(By.ID,'patient_birthday_2i'))

patient_b3 = Select(driver.find_element(By.ID,'patient_birthday_3i'))

time.sleep(1)

patient_name.send_keys("Andres")

patient_Last_name.send_keys("Test change")

patient_email.send_keys("andres.mujica+testauto@crisalix.com")
time.sleep(1)
patient_b1.select_by_visible_text("1952")
time.sleep(1)
patient_b2.select_by_visible_text("April")
time.sleep(1)
patient_b3.select_by_visible_text('12')
time.sleep(1)
driver.find_element(By.NAME, "commit").click()

