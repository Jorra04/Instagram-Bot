from selenium import webdriver
from time import sleep
from creds import pw
from creds import user

class InstaBot:
    def __init__(self, username, pw):
        chromePath = r"C:\Users\jorra\Downloads\chromedriver_win32\chromedriver.exe"
        self.driver = webdriver.Chrome(chromePath)
        self.driver.get("https://instagram.com")
        sleep(2)
        # self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)

        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)

        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()

        sleep(10)
        

InstaBot(user, pw)

