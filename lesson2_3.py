from selenium import webdriver
from time import sleep
from mymodule import calc

# link = 'http://suninjuly.github.io/alert_accept.html'


# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     browser.find_element_by_css_selector("[type='submit']").click()
#     confirm = browser.switch_to.alert
#     confirm.accept()
#     num_text = browser.find_element_by_id('input_value').text
#     num_result = calc(num_text)
#     print(num_result)
#     browser.find_element_by_id('answer').send_keys(num_result)
#     submit = browser.find_element_by_css_selector("[type = 'submit']").click()
# finally:
#     sleep(5)
#     browser.quit()


link = 'http://suninjuly.github.io/redirect_accept.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    trollface = browser.find_element_by_class_name('trollface').click()
    first_window = browser.window_handles[0]
    last_window = browser.window_handles[1]
    browser.switch_to.window(last_window)
    num = browser.find_element_by_id('input_value').text
    num_result = browser.find_element_by_id('answer').send_keys(calc(num))
    browser.find_element_by_css_selector("[type = 'submit']").click()
finally:
    sleep(20)
    browser.quit()