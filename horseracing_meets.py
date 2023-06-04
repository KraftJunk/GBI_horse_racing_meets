
import selenium
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

##Need to install driver on your machine for your version of chrome
service = Service("C:\\Users\S00162960\Downloads\chromedriver_win32\chromedriver.exe")


def get_driver():
    #options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=automationControlled")

    driver = webdriver.Chrome(options=options,service=service)
    driver.get("https://www.attheraces.com/racecards")
    return driver

def clean_text(text):
    #extract only racecard name
    output=text.split(" ")[0]
    return output

## Our main function that will log into FCC and return the quote we want
def main():
    global IE_races
    global uk_races
    uk_races=[]
    IE_races = []
    driver = get_driver()
    race_0 = driver.find_element(by=By.XPATH,value="//*[@id='fixtures-grouped-by-meeting']/div[1]/div[1]/section/div[1]/a/h2")
    uk_races.append(clean_text(race_0.text))
    race_1 = driver.find_element(by=By.XPATH,value="//*[@id='fixtures-grouped-by-meeting']/div[1]/div[2]/section/div[1]/a/h2")
    uk_races.append(clean_text(race_1.text))
    print(uk_races)
    try:
        race_2 = driver.find_element(by=By.XPATH,value="//*[@id='fixtures-grouped-by-meeting']/div[1]/div[3]/section/div[1]/a/h2")
        uk_races.append(clean_text(race_2.text))
    except selenium.common.exceptions.NoSuchElementException as error:
        print("no more uk races")
    try:
        race_3 = driver.find_element(by=By.XPATH,value="//*[@id='fixtures-grouped-by-meeting']/div[1]/div[4]/section/div[1]/a/h2")
        uk_races.append(clean_text(race_3.text))
    except selenium.common.exceptions.NoSuchElementException:
        print("no more uk races")
    try:
        race_4 = driver.find_element(by=By.XPATH,value="//*[@id='fixtures-grouped-by-meeting']/div[1]/div[5]/section/div[1]/a/h2")
        uk_races.append(clean_text(race_4.text))
    except selenium.common.exceptions.NoSuchElementException as error:
        print("no more uk races")
    try:
        race_5 = driver.find_element(by=By.XPATH,value="//*[@id='fixtures-grouped-by-meeting']/div[1]/div[6]/section/div[1]/a/h2")
        uk_races.append(clean_text(race_5.text))
    except selenium.common.exceptions.NoSuchElementException as error:
        print("no more uk races")
    try:
        race_6 = driver.find_element(by=By.XPATH,value="//*[@id='fixtures-grouped-by-meeting']/div[1]/div[7]/section/div[1]/a/h2")
        uk_races.append(clean_text(race_6.text))
    except selenium.common.exceptions.NoSuchElementException as error:
        print("no more uk races")
    try:
        race_7 = driver.find_element(by=By.XPATH,value="//*[@id='fixtures-grouped-by-meeting']/div[1]/div[8]/section/div[1]/a/h2")
        uk_races.append(clean_text(race_7.text))
    except selenium.common.exceptions.NoSuchElementException as error:
        print("no more uk races")
    try:
        race_8 = driver.find_element(by=By.XPATH,value="//*[@id='fixtures-grouped-by-meeting']/div[1]/div[9]/section/div[1]/a/h2")
        uk_races.append(clean_text(race_8.text))
    except selenium.common.exceptions.NoSuchElementException as error:
        print("no more uk races")
    try:
        race_9 = driver.find_element(by=By.XPATH,value="//*[@id='fixtures-grouped-by-meeting']/div[1]/div[10]/section/div[1]/a/h2")
        uk_races.append(clean_text(race_9.text))
    except selenium.common.exceptions.NoSuchElementException as error:
        print("no more uk races")
##IRISH RACES
    try:
        IE_race_0 = driver.find_element(by=By.XPATH,
                                        value="//*[@id='fixtures-grouped-by-meeting']/div[2]/div[1]/section/div[1]/a/h2")
        IE_races.append(clean_text(IE_race_0.text))
    except selenium.common.exceptions.NoSuchElementException as error:
        print("no more IE races")
    try:
        IE_race_1 = driver.find_element(by=By.XPATH,
                                        value="//*[@id='fixtures-grouped-by-meeting']/div[2]/div[2]/section/div[1]/a/h2")
        IE_races.append(clean_text(IE_race_1.text))
    except selenium.common.exceptions.NoSuchElementException as error:
        print("no more IE races")
    try:
        IE_race_2 = driver.find_element(by=By.XPATH,
                                        value="//*[@id='fixtures-grouped-by-meeting']/div[2]/div[3]/section/div[1]/a/h2")
        IE_races.append(clean_text(IE_race_2.text))
    except selenium.common.exceptions.NoSuchElementException as error:
        print("no more IE races")
    try:
        IE_race_3 = driver.find_element(by=By.XPATH,
                                        value="//*[@id='fixtures-grouped-by-meeting']/div[2]/div[4]/section/div[1]/a/h2")
        IE_races.append(clean_text(IE_race_3.text))
    except selenium.common.exceptions.NoSuchElementException as error:
        print("no more IE races")

def save():
    now = datetime.now()
    day_month = now.strftime("%d%m")
    with open("horseracing"+day_month+".txt", "w") as f:
        f.write(str(uk_races+IE_races))


print(main())
print(save())

