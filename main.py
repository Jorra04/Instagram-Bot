from selenium import webdriver
from time import sleep
from creds import pw
from creds import user

class InstaBot:
    def __init__(self, username, pw):
        chromePath = r"C:\Users\jorra\Downloads\chromedriver_win32\chromedriver.exe"
        self.driver = webdriver.Chrome(chromePath)
        self.driver.get("https://instagram.com")
        self.username = username
        sleep(2)
        # self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]").click()
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)

        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)

        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()

        sleep(4)

        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

        
        
    def get_unfollowers(self):
        self.driver.find_element_by_xpath("""//*[@id="react-root"]/section/div/div[1]/div/div[3]/div/div[2]/a/svg""")\
            .click()
        print("hello")

myBot = InstaBot(user, pw)
myBot.get_unfollowers()

