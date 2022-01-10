from selenium import webdriver
import time
import os
import pyperclip

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    first = browser.find_element_by_name('firstname')
    first.send_keys('Test')
    last = browser.find_element_by_name('lastname')
    last.send_keys('Test')
    email = browser.find_element_by_name('email')
    email.send_keys('Test')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'files.txt')           # добавляем к этому пути имя файла 
    
    form = browser.find_element_by_id('file')
    #form.click() делать не нужно, просто вставляем путь в кнопку
    form.send_keys(file_path)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()    

    alert = browser.switch_to.alert # переключаемся на всплывшее окно с ответом
    alert_text = alert.text.split(': ')[-1] # текст в список. отделяем ответ
    print(alert_text)

    pyperclip.copy(alert_text) # вставляем в буфер обмена!!!

finally:
    #time.sleep(10)
    browser.quit()

