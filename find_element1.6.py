# from selenium import webdriver
# find_element_by_id — поиск по уникальному атрибуту id элемента. Если ваши разработчики проставляют
# всем элементам в приложении уникальный id, то вам повезло, и вы чаще всего будет использовать этот метод,
# так как он наиболее стабильный;
# find_element_by_css_selector — поиск элемента с помощью правил на основе CSS. Это универсальный метод поиска,
# так как большинство веб-приложений использует CSS для вёрстки и задания оформления страницам.
# Если find_element_by_id вам не подходит из-за отсутствия id у элементов, то скорее всего вы
# будете использовать именно этот метод в ваших тестах;
# find_element_by_xpath — поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;
# find_element_by_name — поиск по атрибуту name элемента;
# find_element_by_tag_name — поиск элемента по названию тега элемента;
# find_element_by_class_name — поиск по значению атрибута class;
# find_element_by_link_text — поиск ссылки на странице по полному совпадению;
# find_element_by_partial_link_text — поиск ссылки на странице, если текст селектора совпадает с любой частью
# elementS = все одинаковые элементы
# текста ссылки.

# from selenium.webdriver.common.by import By
# By.ID – поиск по уникальному атрибуту id элемента;
# By.CSS_SELECTOR – поиск элементов с помощью правил на основе CSS;
# By.XPATH – поиск элементов с помощью языка запросов XPath;
# By.NAME – поиск по атрибуту name элемента;
# By.TAG_NAME – поиск по названию тега;
# By.CLASS_NAME – поиск по атрибуту class элемента;
# By.LINK_TEXT – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
# By.PARTIAL_LINK_TEXT – поиск ссылки по частичному совпадению текста.

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# class find_by:
#     def __init__(self, url):
#         self.url = url
#
#     def find(self):
#         browser = webdriver.Chrome()
#         browser.get(self.url)
#         button = browser.find_element_by_id("submit_button")
#         button.click()
#
#
#     def by(self):
#         browser = webdriver.Chrome()
#         browser.get(self.url)
#         button = browser.find_element(By.ID, 'submit_button')
#         button.click()
#         sleep(2)
#
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# # url = find_by(link)
# # find_by.by(url)
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element_by_id("submit_button")
#     button.click()
#     sleep(2)
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.ID, 'submit_button')
#     button.click()
#     sleep(2)
# finally:
#     sleep(5)
#     browser.close()
