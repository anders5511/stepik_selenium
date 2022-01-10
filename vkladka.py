from selenium import webdriver
import time
from math import *

def calc(x):
    return str(log(abs(12*sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    btn = browser.find_element_by_class_name('trollface.btn.btn-primary')
    btn.click()

    new_window = browser.window_handles[1] # запоминаем новую(текущую) вкладку
    first_window = browser.window_handles[0] # запоминаем старую вкладку
    browser.switch_to.window(new_window) # переключаемся на новую вкладку
    
    ch = browser.find_element_by_id('input_value')
    x = calc(ch.text)
    
    inp = browser.find_element_by_css_selector('input.form-control')
    inp.send_keys(x)

    button = browser.find_element_by_class_name('btn.btn-primary')
    button.click()

    alert = browser.switch_to.alert  # переключаемся на всплывшее окно с ответом
    alert_text = alert.text.split(': ')[-1]  # текст в список. отделяем ответ
    print(alert_text)

finally:
    #time.sleep(3)
    browser.quit()