from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from chromedriver_py import binary_path
from time import sleep
from datetime import datetime
import sys
import json


def openCoursesJson(n):
    with open('matakuliah.json') as f:
        datas = json.load(f)
        for data in datas['courses']:
            if (data['weekday'] == n):
                return data['link']


def chooseCourses():
    date = datetime.now()
    url = ""

    if date.weekday() == 1:
        # prak. pemrograman visual hari selasa
        url = openCoursesJson(1)
    elif date.weekday() == 3:
        # pemrograman visual hari kamis
        url = openCoursesJson(3)
    return url


def webDriverOptions():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument('window-size=1280,600')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
    )

    return options


def loginElearning(url, d, driver):
    print("Running loginElearning")
    driver.get(url)
    driver.find_element_by_xpath("//input[@name='username']").send_keys(
        d['username'])
    driver.find_element_by_xpath("//input[@name='password']").send_keys(
        d['password'])

    driver.find_element_by_xpath("//button[@type='submit']").click()


def doAttendance(driver):
    print("Running doAttendance")
    driver.find_element_by_xpath(
        "//a[contains(text(),'Submit attendance')]").click()
    if len(sys.argv) > 1:
        driver.find_element_by_xpath(
            "//input[@id='id_studentpassword']").send_keys(sys.argv[1])
    driver.find_element_by_xpath("//span[contains(.,'Hadir')]").click()
    driver.find_element_by_xpath("//input[@id='id_submitbutton']").click()


def printUser(name):
    print(f"{name['nama']} telah absen!")


url = chooseCourses()

# this is the main program
with open('akun.json') as f:
    data = json.load(f)
    for d in data['user']:
        # chromedriver options for headless mode
        print("Running, dont close!!")
        options = webDriverOptions()
        driver = webdriver.Chrome(executable_path=binary_path, options=options)

        # login
        loginElearning(url, d, driver)

        # to check if user already attendance or not
        try:
            doAttendance(driver)
            printUser(d)
        except NoSuchElementException:
            printUser(d)
            continue

        sleep(5)
        driver.close()
