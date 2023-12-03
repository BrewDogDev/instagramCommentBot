from time import sleep
from selenium import webdriver
import random
from names import names

from selenium.webdriver.common.action_chains import ActionChains

email = "" #used to login
password = "" #used to login
postToComment = "" #url of post

browser = webdriver.Chrome()
browser.implicitly_wait(5)

def loginGoTran():
    browser.get('https://www.instagram.com/')

    try:
        username_input = browser.find_element_by_name("username")
        username_input.send_keys(email)

        password_input = browser.find_element_by_name("password")
        password_input.send_keys(password)


        login_link = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
        login_link.click()
        sleep(6)
    except:
        print("already logged in")
    
    browser.get(postToComment)

random.shuffle(names)
loginGoTran()
for name in names:
    try:
        comment_box = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
        comment_button = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]')

        comment_box.click()
        actions = ActionChains(browser)
        actions.send_keys("@"+name)
        actions.perform()
        comment_button.click()
        sleep(4)
    except:
        sleep(2)
        loginGoTran()


