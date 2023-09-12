from selenium import webdriver
from selenium.webdriver.common.by import By


def login(user, pw, url):
    """Login to FamilySearch"""
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # Use Incognito Mode
    browser = webdriver.Chrome()
    browser.implicitly_wait(2.5)
    browser.get(url)
    username = browser.find_element(By.ID, 'userName')
    username.click()  # Put cursor in userName element
    username.send_keys(user)  # Enter username
    password = browser.find_element(By.ID, 'password')
    password.click()  # Put cursor in password element
    password.send_keys(pw)  # Enter password
    browser.find_element(By.ID, 'privateComputerLabel').click()
    browser.find_element(By.ID, 'login').click()
    # browser.find_element(By.CLASS_NAME, 'icon-zoom-out zoom-out').click()
    return browser

