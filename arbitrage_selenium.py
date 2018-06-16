from match import Match
from data import source, source_util
from scraper.SeleniumFunctions import *
import selenium

## start selenium session
driver = Driver()
driver.maximize_window()

__sources = source_util.get_sources()

for s in __sources:
    driver.get(s.url)

    time.sleep(5)
    matches = []
    config = ["ebg_config.json"]

    ## scraper

    p1 = driver.find_element_by_xpath("(//*[@class='table-bets__player1']/child::*[not(@src)])["+str(i)+"]").get_attribute("title")
    p2 = driver.find_element_by_xpath("(//*[@class='table-bets__player2']/child::*[not(@src)])["+str(i)+"]").get_attribute("title")
    q1 = driver.find_element_by_xpath("(//*[@class='table-bets__player1']/following-sibling::*/child::*)["+str(i)+"]").text
    q2 = driver.find_element_by_xpath("(//*[@class='table-bets__player2']/following-sibling::*/child::*)["+str(i)+"]").text
    m = Match(p1, p2, q1, q2)
    matches.append(m)

    print(Match)
    print("test print : " + matches[0].player2)

    driver.close()

    for m in matches:
        print(m)