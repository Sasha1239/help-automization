from enum import Enum

from selenium import webdriver
import time 

url: str = "http://suninjuly.github.io/simple_form_find_task.html"

xpath_pattern: str = "//input[@name='{input_type}']"

xpath_pattern2: str = "//div[@class='form-group' and child::label[text()='City:*']]/input[@name='firstname']"

# //div[@class='form-group' and child::label[contains(text(), '*')]]/input
class InputType(Enum):
    first_name: str = 'first_name'
    last_name: str = 'last_name'
    city: str = 'firstname'

    def __str__(self):
        return self.value

class InputName(Enum):
    city: str = 'City:*'
    first_name: str = 'First name'

try:
    browser = webdriver.Firefox()
    browser.get(url)

    # input1 = browser.find_element_by_tag_name("input[name=first_name]")
    input1 = browser.find_element_by_xpath(xpath_pattern.format(input_type=InputType.first_name))
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
