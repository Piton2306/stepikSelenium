# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/wait1.html")
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")

# try:
#     browser.implicitly_wait(5)
#     button = browser.find_element_by_id("verify")
#     button.click()
#     message = browser.find_element_by_id("verify_message")
#     assert "successful" in message.text
#     print('Выполнено')
#     browser.quit()
# except Exception:
#     print('Ошибка')
#     browser.quit()
# from selenium import webdriver
#
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://suninjuly.github.io/wait2.html')
# button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, 'verify')))
# button.click()
# message = browser.find_element_by_id(("verify_message"))
# assert "successful" in message.text
# browser.quit()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lesson2_3 import calc

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)
price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
browser.find_element_by_id('book').click()
num = browser.find_element_by_id('input_value').text
num_result = calc(num)
browser.find_element_by_id('answer').send_keys(num_result)
browser.find_element_by_id('solve').click()

