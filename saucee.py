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
    def func(self):
            el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Username")
            el1.send_keys("standard_user")
            el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Password")
            el2.click()
            el2.send_keys("secret_sauce")
            el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-LOGIN")
            el3.click()
            el4 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"ADD TO CART\").instance(0)")
            el4.click()
            el5 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.ViewGroup\").instance(13)")
            el5.click()
            el6 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"CHECKOUT\")")
            el6.click()
            el7 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"CONTINUE\")")
            el7.click()
            el8 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-First Name")
            el8.click()
            el8.send_keys("adithya")
            el9 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Last Name")
            el9.click()
            el9.send_keys("sunil")
            el10 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-CONTINUE")
            el10.click()
            el11 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Zip/Postal Code")
            el11.click()
            el12 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-Zip/Postal Code")
            el12.click()
            el12.send_keys("668797")
            el13 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="test-CONTINUE")
            el13.click()
            actions = ActionChains(driver)
            actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            actions.w3c_actions.pointer_action.move_to_location(518, 2030)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.move_to_location(504, 552)
            actions.w3c_actions.pointer_action.release()
            actions.perform()

            el14 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"FINISH\")")
            el14.click()
obj=Saucelab()
obj.func()        