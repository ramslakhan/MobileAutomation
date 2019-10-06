from time import sleep

from appium import webdriver


#desired Capabilities
desired_caps ={
  "deviceName": "RedmiNote6Pro",
  "platformName": "Android",
  "appPackage": "com.google.android.apps.maps",
  "appActivity": "com.google.android.maps.MapsActivity",
  "udid": "emulator-5554",
  "platformVersion": "7.1.1",
  "automationName": "UiAutomator2",
  "newCommandTimeout": "3600",
  "autoGrantPermissions ": "true",
  "noReset": "true",
  "fullReset": "false",
}

url = "http://127.0.0.1:4723/wd/hub"
driver = webdriver.Remote(url, desired_caps)
# driver.launch_app()
sleep(30)

driver.find_element_by_id("com.google.android.apps.maps:id/search_omnibox_text_box").click()
sleep(2)
driver.find_element_by_id('com.google.android.apps.maps:id/search_omnibox_edit_text').clear()
driver.find_element_by_id('com.google.android.apps.maps:id/search_omnibox_edit_text').send_keys("hyderabad")
driver.quit()