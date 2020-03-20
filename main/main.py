import sys
from selenium import webdriver
from time import sleep
from datetime import date

#search for the username and password.
sys.path.insert(0,'../resources/')
from secret import us, ps

class instagramBot:

    def __init__(self,username,password): 
        self.date = str(date.today())
        self.webdriver = webdriver.Chrome()
        self.webdriver.get('http://instagram.com')
        sleep(2)
     
        #logins
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(username)
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(password)
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]').click()
        sleep(4)            
        self.webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()


    #Profile functions
    def goToProfile(self):
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[4]/a').click()
        sleep(2)

    def goHome(self):
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a/svg/path').click()
        sleep(2)

    def getFollowers(self):
        self.goHome()
        sleep(2)
        self.goToProfile()
        sleep(2)
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        self.webdriver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button/svg/path').click()

    def getFollowing(self):
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
        self.webdriver.execute_script("window.scrollTo(0, 100)")
        sleep(2)
     
        try:
            try:
                self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]').click()
                #get the date and return it.
                return self.webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[2]/a/time').get_attribute('title')

            except:
                self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]').click()
                sleep(2)
                return self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[2]/div[2]/a/time').get_attribute('title')
        except:
            return '0000'

    #bot functions
    def getList(self):
        #gets all the usernames from the following and follower list
        last_height , height = 0, 1
        scroll_box = self.webdriver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div')

        while last_height != height:
            last_height = height
            height = self.webdriver.execute_script(""" 
                    arguments[0].scrollTo(0, arguments[0].scrollHeight);
                    return arguments[0].scrollHeight);
                    """, scroll_box)
            links = scroll_box.find_element_by_tag('a')
            names = [name.text for name in links if name.text != '']
        
        self.webdriver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button/svg').click()
        
        return names

    def createList(self,arr,listname):
        #saves every list given to a text file
        with open(str(listname)+".txt", "w") as output:
            output.write(str(arr))
    
    def getUnfollowers(self,following,followers):
        #gets a list about the people that you follow that does'nt follow you back.
        unflist = []

        for x in following:
            for y in followers:
                if not x.__eq__(y):
                    unflist.append(x)
        
        return unflist


    def posibleUnfollows(self,following):
        #gets a list about the peole that are not posting resently 
        posUnf = []
        for x in following:
            self.getProfile(x)
            sleep(2)
            pdate = self.getFirstPost()
            sleep(1)
            compDate = str(pdate)[:4]
            toDate = str(self.date)[:4]
            if not toDate.__eq__(compDate):
                posUnf.append(x)
    

nbot = instagramBot(us,ps)

nbot.getFollowers()
lfollowing = nbot.getList()

nbot.getFollowers()
lfollowers = nbot.getList()

lunfollowers = nbot.getUnfollowers(lfollowing,lfollowers)

nbot.createList(lunfollowers,'Unfollowers')
















