# from selenium import webdriver
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     value1 = 'body > div > form > div:nth-child(1) > input'
#     value2 = 'last_name'
#     value3 = 'city'
#     value4 = 'country'
#
#     input1 = browser.find_element_by_tag_name(value1)
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name(value2)
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name(value3)
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id(value4)
#     input4.send_keys("Russia")
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла
from selenium import webdriver
import math
from time import sleep

# link = 'http://suninjuly.github.io/find_link_text'
# browser = webdriver.Chrome()
# browser.get(link)
# b = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e) * 10000)))
# b.click()
#
# value1 = 'body > div > form > div:nth-child(1) > input'
# value2 = 'last_name'
# value3 = 'city'
# value4 = 'country'
# input1 = browser.find_element_by_tag_name(value1)
# input1.send_keys("Ivan")
# input2 = browser.find_element_by_name(value2)
# input2.send_keys("Petrov")
# input3 = browser.find_element_by_class_name(value3)
# input3.send_keys("Smolensk")
# input4 = browser.find_element_by_id(value4)
# input4.send_keys("Russia")
# button = browser.find_element_by_css_selector("button.btn")
# button.click()
# sleep(10)
# browser.quit()
from selenium import webdriver
import time

# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     value = 1
#     elements = browser.find_elements_by_tag_name('input')*value
#     for element in elements:
#         element.send_keys("мой ответ")
#
#
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

# try:
#     browser = webdriver.Chrome()
#     browser.get('http://suninjuly.github.io/find_xpath_form')
#     value =1
#     elements = browser.find_elements_by_tag_name('input') * value
#     for element in elements:
#         element.send_keys("мой ответ")
#     button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

from selenium import webdriver
import time

try:
    # link = "http://suninjuly.github.io/registration2.html"
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    element = browser.find_element_by_css_selector('.first_block .first')
    element.send_keys('Имя')
    time.sleep(2)
    element = browser.find_element_by_css_selector('.first_block .second')
    element.send_keys('Фамилия')
    time.sleep(2)
    element = browser.find_element_by_css_selector('.first_block .third')
    element.send_keys('Mail')
    time.sleep(2)
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
'first_block'
# try:
#     browser = webdriver.Chrome()
#     browser.get('http://suninjuly.github.io/registration2.html')
#     value = 1
#     elements = browser.find_elements_by_css_selector('.first_block input')
#     for element in elements:
#         element.send_keys("мой ответ")
#         time.sleep(2)
#     # Отправляем заполненную форму
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element_by_tag_name("h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#     print(welcome_text)


