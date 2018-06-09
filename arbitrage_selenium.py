import csv, time, pandas as pd, matplotlib.pyplot as plt, numpy as np, keyboard, pyautogui, pyperclip, re, lxml

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from match import Match

url = "https://egb.com/play/simple_bets"

driver = webdriver.Chrome()
driver.maximize_window()

driver.get(url)

time.sleep(5)
matches = []

for i in range(1,20):
    p1 = driver.find_element_by_xpath("(//*[@class='table-bets__player1']/child::*[not(@src)])["+str(i)+"]").get_attribute("title")
    p2 = driver.find_element_by_xpath("(//*[@class='table-bets__player2']/child::*[not(@src)])["+str(i)+"]").get_attribute("title")
    m = Match(p1, p2)
    matches.append(m)

print("test print : " + matches[0].player2)

for m in matches:
    print(m)