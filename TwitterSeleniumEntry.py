from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Firstly you must install chromedriver.exe on https://chromedriver.chromium.org/downloads
chromeDriverPath = ""   # Enter chromedriver.exe files path here

class Twitter:
    def __init__(self, username, password):

        # create a webriver options profile
        self.browserProfile = webdriver.ChromeOptions()
        # setting options
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages' : 'en,en_us'})
        self.browserProfile.add_experimental_option('excludeSwitches', ['enable-logging'])

        # attach the profile settings to web browser
        self.browser = webdriver.Chrome(executable_path=chromeDriverPath , chrome_options=self.browserProfile)

        self.username = username
        self.password = password

    def signIn(self):
        
        #twitter login screen link        
        self.browser.get("https://twitter.com/login") #twitter login screen lin
        time.sleep(2)

        # Input zone xpath's, it may been changed, check from site.
        usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)

        #button function and button xpath
        btnSubmit = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div")
        btnSubmit.submit()

        time.sleep(2)


print("Twitter Selenium Entry \n"+"-"*25)
userName = str(input("Username = "))
passWord = str(input("Password = "))

twitter = Twitter(userName, passWord)
twitter.signIn()
