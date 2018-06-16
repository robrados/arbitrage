from calculation.pattern_matching import Levenshtein
from scraper.SeleniumFunctions import *
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
from scraper import *

driver = webdriver.Chrome()
driver.get(r"https://egb.com/play/simple_bets")

time.sleep(5)

print(len(driver.find_elements_by_xpath(r"//*[@class='table-bets__player1']/child::*[not(@src)]")))

"""
list1 = ["asd","ghj","yx","qww","qqq"]
list2 = ["ghj","asd","yx","qqq","qww"]
listmatch = []

print(Levenshtein("hallo","alloh").levenshtein())

for i in list1:
    distance = []
    for j in list2:
        dist = Levenshtein(str(i),str(j)).levenshtein()
        distance.append(dist)
    listmatch.append(list2[distance.index(min(distance))])

print(list1)
print(listmatch)
"""

