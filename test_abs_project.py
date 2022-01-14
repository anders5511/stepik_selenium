from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"  # тест1 должен проходить
        browser = webdriver.Chrome()
        browser.get(link)

        inp1 = browser.find_element_by_css_selector(
            'input[placeholder="Input your first name"]')
        inp1.send_keys('Test')
        inp2 = browser.find_element_by_css_selector(
            'input[placeholder="Input your last name"]')
        inp2.send_keys('Test')
        inp3 = browser.find_element_by_css_selector(
            'input[placeholder="Input your email"]')
        inp3.send_keys('Test')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 
            "Not message success registered")
        browser.quit()

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"  # тест2 не должен проходить
        browser = webdriver.Chrome()
        browser.get(link)

        inp1 = browser.find_element_by_css_selector(
            'input[placeholder="Input your first name"]')
        inp1.send_keys('Test')
        inp2 = browser.find_element_by_css_selector(
            'input[placeholder="Input your last name"]')
        inp2.send_keys('Test')
        inp3 = browser.find_element_by_css_selector(
            'input[placeholder="Input your email"]')
        inp3.send_keys('Test')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 
            "Not message success registered")
        browser.quit()

if __name__ == "__main__":
    unittest.main()
