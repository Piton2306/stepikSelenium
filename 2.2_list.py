# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from time import sleep
#
#
# def summa(a, b):
#     return str(int(a) + int(b))
#
#
# link = 'http://suninjuly.github.io/selects2.html'
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     num1 = browser.find_element_by_id('num1').text
#     num2 = browser.find_element_by_id('num2').text
#     select = Select(browser.find_element_by_id('dropdown'))
#     select.select_by_value(summa(num1, num2))
#     browser.find_element_by_css_selector("[type = 'submit']").click()
#     print(summa(num1, num2))
# finally:
#     sleep(5)
#     browser.quit()
#
# from selenium import webdriver
# import math
# from time import sleep
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# try:
#     browser = webdriver.Chrome()
#     link = "http://suninjuly.github.io/execute_script.html"
#     browser.get(link)
#     num_get = str(browser.find_element_by_id('input_value').text)
#     num = calc(num_get)
#     answer = browser.find_element_by_id('answer').send_keys(num)
#     robotCheckbox = browser.find_element_by_id('robotCheckbox').click()
#     button_robots = browser.find_element_by_id('robotsRule')
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button_robots)
#     button_robots.click()
#     submit =browser.find_element_by_css_selector("[type = 'submit']")
#     submit.click()
#
# finally:
#     sleep(5)
#     browser.quit()
import os
from selenium import webdriver
from time import sleep

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
print(current_dir)
print(file_path)
link = 'http://suninjuly.github.io/file_input.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector("[name = firstname]").send_keys('Имя')
    browser.find_element_by_css_selector("[name = lastname]").send_keys('Фамилия')
    browser.find_element_by_css_selector("[name = email]").send_keys('Емаил')
    browser.find_element_by_css_selector("[name = file]").send_keys(file_path)
    browser.find_element_by_css_selector("[type = submit]").click()
finally:
    sleep(5)
    browser.quit()
