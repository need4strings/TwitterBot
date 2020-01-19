from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_tweet(self,hastag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hastag+'&src=typed_query')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)

            tweetLinks = [i.get_attribute('href')
            for i in bot.find_elements_by_xpath("//a[@dir='auto']")]
            filteredLinks = list(filter(lambda x: 'status' in x,tweetLinks))
            print(filteredLinks) 

            for link in filteredLinks :
                    bot.get(link)
                    time.sleep(5)
                    try:
                        bot.find_element_by_xpath("//div[@data-testid='like']").click()
                        time.sleep(10)
                    except Exception:
                        time.sleep(10)

tony = TwitterBot('username', 'password')

tony.login()
tony.like_tweet('gaming')