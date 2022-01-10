from selenium import webdriver
import time

try: 
    # link = "http://suninjuly.github.io/registration1.html" # тест1 должен проходить
    link = "http://suninjuly.github.io/registration2.html" # тест2 должен падать
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    inp1 = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
    inp1.send_keys('Test')
    inp2 = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
    inp2.send_keys('Test')
    inp3 = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
    inp3.send_keys('Test')
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




