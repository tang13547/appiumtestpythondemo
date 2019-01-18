from appium import webdriver
from selenium.webdriver.common.by import By

import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.find_element(By.XPATH, '//android.view.ViewGroup/android.widget.Button[7]').click()
driver.find_element(By.XPATH, "//android.widget.Button[contains(@text,'5')]").click()
driver.find_element(By.ID, "com.android.calculator2:id/digit_9").click()
driver.find_element(By.ID, "com.android.calculator2:id/del").click()
driver.find_element(By.ID, "com.android.calculator2:id/op_add").click()
driver.find_element(By.ID, "com.android.calculator2:id/digit_6").click()
driver.find_element(By.ID, "com.android.calculator2:id/eq").click()
time.sleep(2)

result = driver.find_element(By.ID, "com.android.calculator2:id/formula").text

print("Getting result is:%s" %result)

driver.quit()