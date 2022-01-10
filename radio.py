from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/math.html'
    br = webdriver.Chrome()
    br.get(link)

    x_element = br.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    inp = br.find_element_by_id('answer')
    inp.send_keys(y)

    #option1 = br.find_element_by_css_selector("[for='robotCheckbox']")
    #option1.click()

    #option2 = br.find_element_by_css_selector("[value='robots']")
    #option2.click()

    #button = br.find_element_by_css_selector('button.btn')
    #button.click()

    people_radio = br.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

finally:
    time.sleep(10)
    br.quit()
