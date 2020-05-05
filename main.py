from selenium import webdriver
from time import sleep
from creds import pw, user, slider,groupName


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

        sleep(5)

        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(5)
        self.driver.find_element_by_class_name("xWeGp").click()
        sleep(5)
    def personal_dm(self):
        self.driver.find_element_by_xpath("//button[@type=\"button\"]").click()
        sleep(5)
        self.driver.find_element_by_xpath("//input[@name=\"queryBox\"]").send_keys(slider)
        sleep(5)
        self.driver.find_element_by_class_name("dCJp8 ").click()

        sleep(5)
        # self.driver.find_element_by_xpath("//button[@type=\"button\"]").click()
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/div/button").click()
        sleep(5)
        self.driver.find_element_by_xpath("//textarea[@placeholder=\"Message...\"]").send_keys("i turned myself into a bot.")

        sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Send')]").click()

    def dm_group(self):
        content = []
        content = self.driver.find_elements_by_xpath("//div[@class=\"        DPiy6           Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                              \"]")
        for i in content:
            print(i)
            sleep(5)
            i.click()
        # self.driver.find_element_by_xpath("//div[@class=\"        DPiy6           Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                              \"]").click()
        # sleep(5)
        # self.driver.find_element_by_xpath("//textarea[@placeholder=\"Message...\"]").send_keys("group message.")

        # sleep(5)
        # self.driver.find_element_by_xpath("//button[contains(text(), 'Send')]").click()
myBot = InstaBot(user, pw)
# myBot.dm_group()
myBot.personal_dm()

myBot.driver.quit()



