import selenium
from selenium import webdriver
from ConfigParser import SafeConfigParser

def login(driver):
    config = SafeConfigParser()
    config.read('config.ini')

    username = driver.find_element_by_class_name("padding").find_element_by_class_name("field")
    username.send_keys(config.get('apple-account', 'email'))
    password = driver.find_element_by_xpath("//div[contains(@class, 'password')]")
    password.send_keys(config.get('apple-account', 'password'))
    go = driver.find_element_by_xpath("//div[contains(@class, 'submit')]")
    go.click()

def findDevice(driver):
    driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))

    drop_down_xpath = ("//div[contains(@class, 'focus')]/div[contains(@class, "
                        "'top-bar')]/div[contains(@title, 'devices')]")
    drop_down = driver.find_element_by_xpath(drop_down_xpath)
    drop_down.click()

    my_device_xpath = ("//div[contains(@class, 'list-picker')]/div/div/div"
                        "/div/div[contains(@class, 'device-list-view')]")
    iphone = driver.find_element_by_xpath(my_device_xpath)
    return iphone
    

url = "https://www.icloud.com/"

driver = webdriver.Firefox()
driver.get(url)
driver.implicitly_wait(10)

login(driver)

driver.implicitly_wait(5)
driver.get(url+"#find")

iphone = findDevice(driver)
driver.implicitly_wait(10)
iphone.click()

play_sound_xpath = ("//div/div/div/div/div/div/"
                    "div[contains(@class, 'play-sound')]")
playsound = driver.find_element_by_xpath(play_sound_xpath)
playsound.click()
