import time
from threading import Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


'''LOcators'''
close_btn = '//button[@class="_2KpZ6l _2doB4z"]'
search = '//input[@name="q"]'
submit = '//button[@type="submit"]'
filter_mobile = '//a[@title="Mobiles"]'
filter_samsung = "//div[text()='SAMSUNG']"
filter_assured = '//section[@class="_2hbLCH _24gLJx"]//img[contains(@src,"www/linchpin/fk-cp-zion/img/fa_62673a.png")]/parent::div'
phn_locators = '//div[@class="_4rR01T"]'
phn_links = '//div[@class="_1AtVbE col-12-12"]//div[@class="_13oc-S"]//a'
phn_price = '//div[@class="_30jeq3 _1_WHN1"]'

'''Expected data'''
phn = 'Samsung Galaxy S10'


# This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
caps = [{
    'os_version': '10',
    'os': 'Windows',
    'browser': 'Firefox',
"browserstack.console" : "info",
    'browser_version': 'latest',
    'name': 'Parallel Test1',  # test name
    'build': 'Assignment_Interview_3'  # Your tests will be organized within this build
},
    {
        'os_version': 'Big Sur',
        'os': 'OS X',
        'browser': 'safari',
        'browser_version': 'latest',
"browserstack.console" : "info",
        'name': 'Parallel Test2',
        'build': 'Assignment_Interview_3'
    },
    {
    'os_version': '10',
    'os': 'Windows',
"browserstack.console" : "info",
    'browser': 'Edge',
    'browser_version': 'latest',
    'name': 'Parallel Test3',  # test name
    'build': 'Assignment_Interview_3'
    },
{
    'os_version': '10',
    'os': 'Windows',
"browserstack.console" : "info",
    'browser': 'Chrome',
    'browser_version': 'latest',
    'name': 'Parallel Test4',  # test name
    'build': 'Assignment_Interview_3'
    },
{
        'os_version': '10',
        'os': 'Windows',
        'browser': 'IE',
        'browser_version': 'latest',
        'name': 'Parallel Test5',
        "browserstack.console" : "info",
        'build': 'Assignment_Interview_3'
    }
]


# run_session function searches for 'BrowserStack' on google.com


logger = logging.getLogger(__name__)
filhandler = logging.FileHandler('logfile.log')
format = logging.Formatter("%(asctime)S :%(levelname)S:%(name)S:%(message)S")
filhandler.setFormatter(format)
logger.addHandler(filhandler)

def Click_Element(driver,locator):
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.XPATH, locator)))
    driver.find_element_by_xpath(locator).click()

def Input_value(driver,locator,Value):
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.XPATH, locator)))
    driver.find_element_by_xpath(locator).send_keys(Value)

def Get_text(driver,locator,Value):
    wait = WebDriverWait(driver, 20)
    wait.until(EC.presence_of_element_located((By.XPATH, locator)))
    text_val = driver.find_element_by_xpath(locator).text
    return text_val


def run_session(desired_cap):
    driver = webdriver.Remote(
        command_executor='https://kunalnevrekar1:NHzCyrFTKXS9AaXayE83@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=desired_cap)

    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    try:
        Click_Element(driver, close_btn)
        Input_value(driver, search, phn)
        Click_Element(driver, submit)

        Click_Element(driver, filter_mobile)
        Click_Element(driver, filter_samsung)
        # Click_Element(filter_assured)
        time.sleep(2)

        driver.find_element_by_xpath("//label[@class='_2iDkf8 shbqsL']").click()
        # driver.execute_script("document.getElementsByClassName('_3U-Vxu')[0].click;")

        time.sleep(4)
        All_phones = driver.find_elements_by_xpath(phn_locators)
        Phone_Name = []
        for ele in All_phones:
            name = ele.text
            Phone_Name.append(name)

        All_links = driver.find_elements_by_xpath(phn_links)
        Link_Details = []
        for ele in All_links:
            link = ele.get_attribute('href')
            Link_Details.append(link)

        All_price = driver.find_elements_by_xpath(phn_price)
        Price_details = []
        for ele in All_price:
            price = ele.text
            Price_details.append(price)

        for i in range(len(Price_details)):
            logger.info("Mobile Name: " + Phone_Name[i])
            logger.info("Link To Mobile: " + Link_Details[i])
            logger.info("Price of the Phone: " + Price_details[i])
            logger.info("----------------------------------------------------------------------------")

        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')

    except TimeoutException:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}')
    print(driver.title)
    driver.quit()


# The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session parallelly
for cap in caps:
    Thread(target=run_session, args=(cap,)).start()
