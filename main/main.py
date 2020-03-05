import sys
from selenium import webdriver
from time import sleep

#search for the username and password.
sys.path.insert(0,'../resources/')
from secret import us, ps

class instagramBot:

    def __init__(self,username,password):
        self.webdriver = webdriver.Chrome()
        self.webdriver.get('http://instagram.com')
        sleep(2)

        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[2]/p/a').click()
        sleep(4)

        #logins
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(username)
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]').click()
        sleep(2)
        self.webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()


    #Profile functions
    def goToProfile(self):
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[4]/a').click()
        sleep(2)

    def goHome(self):
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a/svg/path').click()
        sleep(2)

    def getfollowers(self):
        self.goHome()
        sleep(2)
        self.goToProfile()
        sleep(2)
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        self.webdriver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button/svg/path').click()

    def getfollowing(self):
        self.goHome()
        sleep(2)
        self.goToProfile()
        sleep(2)
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
        self.webdriver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button/svg/path').click()

    def getProfile(self,target):
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div/div/span[2]').sendKeys(target)
        sleep(1)
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]').click()

    def getFirstPost(self):
        #scroll down a little and select the first post
        pass

    def getDate(self):
        #return the year of the post 
        pass

    #bot functions
    def getList(self):
        #gets all the usernames from the following and follower list
        pass

    def createList(self,arr):
        #saves every list given to a text file
        pass
    
    def getUnfollowers(self,following,followers):
        #gets a list about the people that you follow that does'nt follow you back.
        pass

    def posibleUnfollows(self,following,followers):
        #gets a list about the peole that are not posting resently 
        pass


nbot = instagramBot(us,ps)












