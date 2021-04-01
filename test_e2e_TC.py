import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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



def test_endtoend():

    '''LOcators'''
    close_btn = '//button[@class="_2KpZ6l _2doB4z"]'
    search = '//input[@name="q"]'
    submit = '//button[@type="submit"]'
    filter_mobile = '//a[@title="Mobiles"]'
    filter_samsung = "//div[text()='SAMSUNG']"
    #filter_assured = '//img[contains(@src,"www/linchpin/fk-cp-zion/img/fa_62673a.png")]/parent::div/parent::div/parent::label/input'
    filter_assured = '//section[@class="_2hbLCH _24gLJx"]//img[contains(@src,"www/linchpin/fk-cp-zion/img/fa_62673a.png")]/parent::div'
    phn_locators = '//div[@class="_4rR01T"]'
    phn_links = '//div[@class="_1AtVbE col-12-12"]//div[@class="_13oc-S"]//a'
    phn_price = '//div[@class="_30jeq3 _1_WHN1"]'

    '''Expected data'''
    phn = 'Samsung Galaxy S10'



    driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)


    Click_Element(driver,close_btn)
    Input_value(driver,search,phn)
    Click_Element(driver,submit)

    Click_Element(driver,filter_mobile)
    Click_Element(driver,filter_samsung)
    #Click_Element(filter_assured)
    time.sleep(2)

    driver.find_element_by_xpath("//label[@class='_2iDkf8 shbqsL']").click()
    #driver.execute_script("document.getElementsByClassName('_3U-Vxu')[0].click;")

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
        print("Mobile Name: " +Phone_Name[i])
        print("Link To Mobile: "+Link_Details[i])
        print("Price of the Phone: "+Price_details[i])
        print("----------------------------------------------------------------------------")



