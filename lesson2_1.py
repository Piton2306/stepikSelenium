# # Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
from selenium import webdriver
import math
from time import sleep

link = 'http://suninjuly.github.io/get_attribute.html'


# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     x_element = browser.find_element_by_id('input_value')
#     x = x_element.text
#     y = calc(x)
#     button_text = browser.find_element_by_id('answer')
#     button_text.send_keys(y)
#     browser.find_element_by_id('robotCheckbox').click()
#     browser.find_element_by_id('robotsRule').click()
#     browser.find_element_by_css_selector("[type='submit']").click()
#
# finally:
#     sleep(5)
#     browser.close()

# Задание: поиск сокровища с помощью get_attribute
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    treasure = browser.find_element_by_id('treasure')
    treasure_num = treasure.get_attribute('valuex')
    y = calc(treasure_num)
    button_answer = browser.find_element_by_id('answer')
    button_answer.send_keys(y)
    robotCheckbox = browser.find_element_by_id('robotCheckbox')
    robotCheckbox.click()
    robotsRule = browser.find_element_by_id('robotsRule')
    robotsRule.click()
    submit = browser.find_element_by_css_selector("[type='submit']")
    submit.click()
finally:
    sleep(5)
    browser.quit()
