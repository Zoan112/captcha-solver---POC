from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions() 
options.add_argument("--use-fake-ui-for-media-stream") #mic permission
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options = options)
driver.get("https://www.google.com/recaptcha/api2/demo") #open recaptcha page

#open voice recoginciton page
sr = driver.execute_script('''window.open("https://speech-to-text-demo.ng.bluemix.net/","_blank");''')
print(driver.window_handles)
driver.switch_to.window(window_name=driver.window_handles[-1])
print(sr)
print(driver.current_window_handle)
driver.implicitly_wait(20)

#accept cookies
'''
time.sleep(15) #wait for cookie dialog to pop-up
print("time is up")
elem = driver.find_elements_by_tag_name('iframe')   
print(elem)
driver.switch_to.frame(elem[2])#(elem[6])


driver.find_element_by_class_name('required').click()
'''
time.sleep(5)

#click the record button
root = driver.find_element_by_id('root')
root.find_element_by_xpath('//*[@id="root"]/div/div[6]/button[1]').click()

#wait
time.sleep(5)

#switch back to recaptcha page
driver.switch_to.window(window_name=driver.window_handles[0])
print(driver.current_window_handle)

frames = driver.find_elements_by_tag_name('iframe')
driver.switch_to.frame(frames[0])
driver.find_element_by_class_name('recaptcha-checkbox-border').click()
driver.implicitly_wait(10)

driver.switch_to.default_content()

driver.implicitly_wait(10)
driver.switch_to.frame(frames[2])
driver.find_element_by_xpath('//*[@id="recaptcha-audio-button"]').click()

driver.find_element_by_class_name('rc-audiochallenge-control').click() #play button

link = driver.find_element_by_tag_name('audio').get_attribute('src')
print(link)

input = driver.find_element_by_class_name('rc-audiochallenge-response-field')
input2 = input.find_element_by_tag_name('input')
input2 = driver.find_element_by_id("audio-response").send_keys('')
driver.implicitly_wait(10)
print('wait end')

#switch back to voice regoigntion and get text
driver.switch_to.window(window_name=driver.window_handles[-1])

#text box
time.sleep(5)
text =  driver.find_element_by_class_name('tab-panels').find_element_by_class_name('tab-panels--tab-content').find_element_by_css_selector('div[data-id="Text"]').find_element_by_tag_name('span').get_attribute('innerHTML')
print (text)

#switch back to recapatch
driver.switch_to.window(window_name=driver.window_handles[0])
print(driver.current_window_handle)

driver.switch_to.frame(frames[2])

input = driver.find_element_by_class_name('rc-audiochallenge-response-field')
input2 = input.find_element_by_tag_name('input')
input2 = driver.find_element_by_id("audio-response").send_keys(text)

#click verify and submit
driver.find_element_by_class_name('rc-footer').find_element_by_class_name('primary-controls').find_element_by_class_name('verify-button-holder').click()