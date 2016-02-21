from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.icloud.com/"

driver = webdriver.Firefox()
driver.get(url)

driver.implicitly_wait(10)

username = driver.find_element_by_class_name("padding").find_element_by_class_name("field")
username.send_keys("email")
password = driver.find_element_by_xpath("//div[contains(@class, 'password')]")
password.send_keys("password") # think of a way to not store password in plain text

go = driver.find_element_by_xpath("//div[contains(@class, 'submit')]")
go.click()

driver.implicitly_wait(5)
driver.get(url+"#find")

driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
drop_down = driver.find_element_by_xpath("//div[contains(@class, 'focus')]/div[contains(@class, 'top-bar')]/div[contains(@title, 'devices')]")
drop_down.click()

iphone = driver.find_element_by_xpath("//div[contains(@class, 'list-picker')]/div/div/div/div/div[contains(@class, 'device-list-view')]")
driver.implicitly_wait(10)
iphone.click()

playsound = driver.find_element_by_xpath("//div/div/div/div/div/div/div[contains(@class, 'play-sound')]")
playsound.click()
