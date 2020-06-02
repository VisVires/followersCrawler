from credentials import username, password
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import seed
from random import randint

class InstaUnfollowers:
  def __init__(self, username, password):
    self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    self.driver.get('https://instagram.com')
    seed(1)
    val = randint(4, 6)
    time.sleep(val)
    usern= self.driver.find_element_by_xpath("//input[@name='username']")
    usern.send_keys(username)
    passw= self.driver.find_element_by_xpath("//input[@name='password']")
    passw.send_keys(password)
    passw.send_keys(Keys.ENTER)
    val = randint(4, 6)
    time.sleep(val)

    notNow= self.driver.find_element_by_xpath('//button[text()="Not Now"]')
    notNow.click()

    notNow2= self.driver.find_element_by_xpath('//button[text()="Not Now"]')
    notNow2.click()

    me = self.driver.find_element_by_xpath("//a[@href='/visviresvita/']")
    me.click()

    val = randint(3, 7)
    time.sleep(val)
    settings = self.driver.find_element_by_class_name('wpO6b ')
    settings.click()

    val = randint(3, 7)
    time.sleep(val)
    pAndS= self.driver.find_element_by_xpath('//button[text()="Privacy and Security"]')
    pAndS.click()

    val = randint(3, 7)
    time.sleep(val)
    info = self.driver.find_element_by_xpath("//a[@href='/accounts/access_tool/']")
    info.click()

    val = randint(3, 7)
    time.sleep(val)
    followers = self.driver.find_element_by_xpath("//a[@href='/accounts/access_tool/accounts_following_you']")
    followers.click()

    #val = randint(3, 7)
    #time.sleep(val)
    #following = self.driver.find_element_by_xpath("//a[@href='/accounts/access_tool/accounts_you_follow']")
    #following.click()

    exists = True

    val = randint(7, 10)
    time.sleep(val)

    while(exists):
    	print(exists)
    	viewMore = self.driver.find_element_by_xpath('//button[text()="View More"]')
    	if viewMore:
    		viewMore.click()
    	else:
    		exists = False
    		print(exists)
    	value = randint(2,6)
    	time.sleep(value)



bot = InstaUnfollowers(username, password)