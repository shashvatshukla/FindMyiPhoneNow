from selenium import webdriver
import selenium
url = "https://www.icloud.com/"

driver = webdriver.Firefox()
driver.get(url)

driver.implicitly_wait(10)

#username = driver.find_element_by_name("div#sc1929.atv4.sc-view.sc-text-field-view.username.signin-field.prewebkit538.text-field.sc-huge-size")
username = driver.find_element_by_id("sc1931")
username.send_keys("email id")
password = driver.find_element_by_id("sc1940")
password.send_keys("password") # think of a way to not store password in plain text
#form = driver.find_element_by_id("sc1921")
#password.submit()
#form.submit()
#password.send_keys(Keys.RETURN) 

go = driver.find_element_by_id("sc1950")
go.click()

driver.implicitly_wait(5)

#find = driver.find_element_by_id("sc2331")
#find.click()
driver.get(url+"#find")

driver.implicitly_wait(20)
#frame = driver.find_element_by_id("sc3009")
#driver.switch_to.frame(frame)
driver.switch_to_frame("find")
devices = driver.find_element_by_id("sc1807")

#devices = driver.find_element_by_id("sc2194-label")

devices.click()
iphone = driver.find_element_by_class_name("atv4.find-me.sc-view.sc-list-item-view.device-list-item-view.st.st-devLstItm.sc-collection-item.even.has-icon.sel.sc-regular-size")
#iphone = driver.find_element_by_id("2496-0")
#iphone = driver.find_element_by_id("sc2506")
driver.implicitly_wait(10)
iphone.click()

playsound = driver.find_element_by_id("sc2790")
#playsound = driver.find_element_by_id("sc2205-label")
playsound.click()
