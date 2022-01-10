from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    
    ch1 = browser.find_element_by_id('num1')
    x = ch1.text
    ch2 = browser.find_element_by_id('num2')
    y = ch2.text
    z = str(int(x) + int(y))

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(z)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
