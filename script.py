from selenium import webdriver
import time
from math import *

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    ch1 = browser.find_element_by_id('input_value')
    x = ch1.text
    y = str(log(abs(12*sin(int(x)))))

    browser.execute_script("window.scrollBy(0, 120);")

    inp = browser.find_element_by_id('answer')
    inp.send_keys(y)

    che = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    che.click()

    radio = browser.find_element_by_css_selector('[for="robotsRule"]')
    radio.click()

    button = browser.find_element_by_tag_name("button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
