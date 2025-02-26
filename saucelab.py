from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
import time
 
 
 
class Saucelab:
 
    cap = {
        "appium:deviceName": "Samsung",
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:app": "C:\\Users\\2022353\\Downloads\\sauce.apk",
        "appium:appWaitActivity": "com.swaglabsmobileapp.MainActivity"
}
 
    def initiate_Driver(self):
        #self.apppium_service = AppiumService()
        #global appium_service
       
        try:
            global driver
            driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(self.cap))
            driver.update_settings({"waitForIdleTimeout": 500})
        except TypeError:
            print("Error:Appium server not working ...")
 
    def login(self):
 
        driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='test-Username']").send_keys("standard_user")
        driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='test-Password']").send_keys("secret_sauce")
        driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='LOGIN']").click()
        time.sleep(5)
   
    def add_to_cart(self):
 
        count = len(driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@content-desc='test-Item title']"))
        for i in range(1,count+1):
            item = driver.find_element(AppiumBy.XPATH,"(//android.widget.TextView[@content-desc='test-Item title'])["+str(i)+"]").text
            print(item)
 
        driver.find_element(AppiumBy.XPATH, "(//android.view.ViewGroup[@content-desc='test-ADD TO CART'])[1]").click()
        time.sleep(3)
        driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-ADD TO CART']").click()
        time.sleep(3)
 
        #Navigate to cart page
        driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.widget.ImageView").click()
        time.sleep(3)
        remove_count = len(driver.find_elements(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-REMOVE']"))
        if remove_count == 2:
            print("Remove count is as expected.")
 
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(545, 1846)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(559, 774)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
 
        #click on checkout button
        driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-CHECKOUT']").click()
        time.sleep(3)
        print("checkout succesfull")
 
        driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='test-First Name']").send_keys("Adithya")
        driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='test-Last Name']").send_keys("Sunil")
        driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='test-Zip/Postal Code']").send_keys("686019")
        time.sleep(5)
 
        driver.find_element(AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='test-CONTINUE']").click()
        time.sleep(3)
 
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(518, 1910)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(518, 792)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
 
        el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-FINISH")
        el1.click()
        time.sleep(3)
        el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-BACK HOME")
        el2.click()
 
 
    def close_driver(self):
        driver.quit()
        print("Driver instance closed successfully")
        time.sleep(20)
 
obj = Saucelab()
obj.initiate_Driver()
obj.login()
obj.add_to_cart()
obj.close_driver()
 