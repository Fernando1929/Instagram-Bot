import sys
from selenium import webdriver
from time import sleep
from datetime import date

sys.path.insert(0,'../resources/') # search for the username and password.
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

    ###########################################Profile functions##########################################

    def goToProfile(self): #go to user profile
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a').click()
        sleep(2)

    def goHome(self):
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[1]/a/div/div/img').click()
        sleep(2)

    def getFollowers(self): #get people that follow you
        self.goHome()
        sleep(2)
        self.goToProfile()
        sleep(2)
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
       
    def getFollowing(self): #get people you follow
        self.goHome()
        sleep(2)
        self.goToProfile()
        sleep(2)
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()

    def getProfile(self,target): #look for a persons profile
        inbot.goHome()
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(target)
        sleep(2)
        self.webdriver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]').click()
    
    ###########################################Bot functions##############################################

    def getFirstPost(self): #scroll down a little and select the first post
        self.webdriver.execute_script("window.scrollTo(0, 100)")
        sleep(2)
     
        try: #get the date and return it.
            try: #single image
                self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]').click()
                sleep(4)
                time = self.webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[2]/a').find_element_by_tag_name('time').get_attribute('title')
                self.webdriver.find_element_by_xpath('/html/body/div[4]/div[3]/button').click()
                return time
            except: #multi image or video
                self.webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]').click()
                sleep(4)
                time = self.webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[2]/a').find_element_by_tag_name('time').get_attribute('title')
                self.webdriver.find_element_by_xpath('/html/body/div[4]/div[3]/button').click()
                return time
        except:
            return ''

    def getList(self): #gets all the usernames from the following and follower list
        sleep(2)
        last_height , height = 0, 1
        scroll_box = self.webdriver.find_element_by_xpath('/html/body/div[4]/div/div[2]')

        while last_height != height:
            last_height = height
            sleep(2)
            height = self.webdriver.execute_script(""" 
                    arguments[0].scrollTo(0, arguments[0].scrollHeight);
                    return arguments[0].scrollHeight;
                    """, scroll_box)

        links = scroll_box.find_elements_by_tag_name('a')
        name_list = [name.text for name in links if name.text != '']
        
        self.webdriver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()
        return name_list

    def createList(self,arr,listname): #saves every list given to a text file
        with open(str(listname)+".txt", "w") as output:
            output.write(str(arr))
    
    def getUnfollowers(self): #gets a list about the people that you follow that doesn't follow you back.
        unfollowers_list = []

        inbot.getFollowing()
        following = inbot.getList()

        inbot.getFollowers() 
        followers = inbot.getList()

        for x in following:
                if not followers.__contains__(x):
                    unfollowers_list.append(x)
        
        return unfollowers_list

    def getUnActiveFollowing(self): #gets a list about the peole that are not posting recently 
        inbot.getFollowing()
        following = inbot.getList()
        unactive_list = []
        for x in following:
            self.goHome()
            sleep(2)
            self.getProfile(x)
            sleep(2)
            postDate = self.getFirstPost()
            sleep(1)
            compDate = str(postDate)[-4:]
            todaysDate = str(self.date)[:4]
            if not todaysDate.__eq__(compDate):
                unactive_list.append(x,compDate)
        
        return unactive_list
        
    def exit(self):
        self.webdriver.__exit__()
        sys.exit()

    #################################################Testing#####################################################


inbot = instagramBot(us,ps)
#inbot.createList(inbot.getUnfollowers(),'Unfollowers') # to get unfollowers
#inbot.createList(inbot.getUnActiveFollowing(),'UnactiveAccounts') # to get unactive Accounts

















