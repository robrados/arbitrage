import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class Driver(webdriver.Chrome):

    def __init__(self):
        super().__init__()
        #self.__webdriver = webdriver.Chrome()

    def func_xpath_click(self,sleep_start,sleep_end,func_xpath_url,func_xpath_string):
        self.implicitly_wait(1)
        timer = time.time()
        trial = 0
        while trial == 0:
            try:
                time.sleep(sleep_start)
                self.find_element_by_xpath(func_xpath_string).click()
                time.sleep(sleep_end)
                trial = 1
            except (WebDriverException, NoSuchElementException, OSError, ElementNotVisibleException):
                print("not clickable func")
                trial = 0
                time.sleep(1)
                if int(time.time() - timer) > 100:
                    self.get(func_xpath_url)
                    timer = time.time()

    def func_xpath_click_or_exit(self,sleep_start,sleep_end,func_xpath_url,func_xpath_string):
        self.implicitly_wait(1)
        timer = time.time()
        trial = 0
        while trial == 0:
            try:
                time.sleep(sleep_start)
                self.find_element_by_xpath(func_xpath_string).click()
                time.sleep(sleep_end)
                trial = 1
            except (WebDriverException, NoSuchElementException, OSError, ElementNotVisibleException):
                trial = 1
                time.sleep(sleep_end)
                
    def func_xpath_clear(self,sleep_start,sleep_end,func_xpath_url,func_xpath_string):
        self.implicitly_wait(1)
        timer = time.time()
        trial = 0
        while trial == 0:
            try:
                time.sleep(sleep_start)
                self.find_element_by_xpath(func_xpath_string).clear()
                time.sleep(sleep_end)
                trial = 1
            except (WebDriverException, NoSuchElementException, OSError, ElementNotVisibleException):
                print("not clickable func")
                trial = 0
                time.sleep(1)
                if int(time.time() - timer) > 100:
                    self.get(func_xpath_url)
                    timer = time.time()
                    
    def func_xpath_find_or_pass(self,time_passout,func_xpath_url,func_xpath_string):
        self.implicitly_wait(2)
        timer = time.time()
        global trial_global
        trial_local = 0
        while trial_local == 0:
            try:
                self.find_element_by_xpath(func_xpath_string)
                trial_local = 1
                time.sleep(1)
            except (NoSuchElementException, ElementNotVisibleException):
                trial_local = 0
                time.sleep(0.5)
                if int(time.time() - timer) > time_passout:
                    trial_global = 1
                    trial_local = 1
                    
    def func_xpath_find(self,sleep_start,sleep_end,func_xpath_url,func_xpath_string):
        self.implicitly_wait(2)
        timer = time.time()
        trial = 0
        while trial == 0:
            try:
                time.sleep(sleep_start)
                self.find_element_by_xpath(func_xpath_string)
                time.sleep(sleep_end)
                trial = 1
            except (NoSuchElementException, ElementNotVisibleException):
                trial = 0
                time.sleep(0.5)
                if int(time.time() - timer) > 100:
                    self.get(func_xpath_url)
                    timer = time.time()
                    
    def func_xpath_untilnotvisible(self,sleep_start,sleep_end,func_xpath_url,func_xpath_string):
        self.implicitly_wait(1)
        timer = time.time()
        trial = 0
        while trial == 0:
            try:
                time.sleep(sleep_start)
                self.find_element_by_xpath(func_xpath_string)
                trial = 0
                time.sleep(sleep_end)
                if int(time.time() - timer) > 100:
                    self.get(func_xpath_url)
                    timer = time.time()
            except (NoSuchElementException):
                trial = 1
                
    def func_xpath_sleep_click(self,sleeptime, func_xpath_url, func_xpath_string):
        self.implicitly_wait(1)
        timer = time.time()
        trial = 0
        while trial == 0:
            try:
                time.sleep(sleeptime)
                self.find_element_by_xpath(func_xpath_string).click()
                trial = 1
            except (WebDriverException, NoSuchElementException, OSError, ElementNotVisibleException):
                print("not clickable func")
                trial = 0
                time.sleep(1)
                if int(time.time() - timer) > 100:
                    self.get(func_xpath_url)
                    timer = time.time()
                    
    # Funktion mit non key worded variable list *args -> beliebig viele elemente ansteuerbar, falls gewisses element nicht sichtbar, ansonsten exit
    def func_xpath_if_visible_exit_else_click(self,func_xpath_visible,func_xpath_url,*args):
        timer = time.time()
        trial = 0
        while trial == 0:
            try:
                self.find_element_by_xpath(func_xpath_visible)
                trial = 1
            except (NoSuchElementException, ElementNotVisibleException):
                for i_func_xpath_if_visible_exit_else_click in args:
                    self.func_xpath_click(i_func_xpath_if_visible_exit_else_click,func_xpath_url)
                trial = 1
