from selenium import webdriver
import time
import unittest


class TestsRegistration(unittest.TestCase):
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"

    def test_reg1(self):
        browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
        browser.get(self.link1)

        input1 = browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_css_selector('.first_block .third')
        input3.send_keys("Ivanov@gmail.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!",
                         "Text should be 'Поздравляем! Вы успешно зарегистировались!'")

    def test_reg2(self):
        browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
        browser.get(self.link2)

        input1 = browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_css_selector('.first_block .third')
        input3.send_keys("Ivanov@gmail.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!",
                         "Text should be 'Поздравляем! Вы успешно зарегистировались!'")


if __name__ == "__main__":
    unittest.main()
