from selenium import webdriver
import time
from math import *

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    ch1 = browser.find_element_by_id('input_value')
    x = ch1.text
    y = str(log(abs(12 * sin(int(x)))))

    inp1 = browser.find_element_by_id('answer')
    inp1.send_keys(y)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    alert = browser.switch_to.alert  # переключаемся на всплывшее окно с ответом
    alert_text = alert.text.split(': ')[-1]  # текст в список. отделяем ответ
    print(alert_text)

    # попытка ввести ответ на степик автоматически)))
    browser1 = webdriver.Chrome()
    # browser1.get('https://stepik.org/catalog?auth=login')
    # login = browser1.find_element_by_name('login')
    # login.send_keys('shabazov@gmail.com')
    # password = browser1.find_element_by_name('password')
    # password.send_keys('Anders55')
    # button = browser1.find_element_by_class_name('sign-form__btn.button_with-loader')
    # button.click() # авторизация проходит

    # переход на заданный урок - не проходит (((
    # browser1.get('https://stepik.org/lesson/184253/step/4?unit=158843')
    # answer = browser1.find_element_by_id('ember1417')
    # answer.send_keys(alert_text)


finally:
    time.sleep(3)
    browser.quit()
    browser1.quit()
