import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe")
browser.get(link)

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '10000 RUR')
    )
button = browser.find_element_by_id('book')
button.click()

x = browser.find_element_by_id('input_value').text
y = calc(x)

input2 = browser.find_element_by_id('answer')
input2.send_keys(y)

button1 = browser.find_element_by_id("solve")
button1.click()
