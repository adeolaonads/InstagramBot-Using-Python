#Testing Branches
#Testing Branches 2
#After the first fork from the real account

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create a bot using a class
class InstagramBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

# Adding a login method
    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher/')
        time.sleep(3)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        
 # Adding a like post method   
    def like_post(self,hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/' + hashtag + '/')

# Adding another method soon to the bot

ade = InstagramBot('Your email here', 'Your password here')
ade.login()
ade.like_post('instablog9ja')

