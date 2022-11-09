from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

#for element (best for text element) - serch by name
class BasePageElement(object):
    def __set__(self,obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
        lambda driver: driver.find_element(By.NAME,self.locator))
        driver.find_element(By.NAME,self.locator).clear()
        driver.find_element(By.NAME,self.locator).send_keys(value)

    def __get__(self, obj  , owner):
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")