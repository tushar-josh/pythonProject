import time
import pytest

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec

driver = webdriver.Chrome(executable_path='..\driver\chromedriver.exe')

driver.get('https://gn-test-46fc5.web.app/intelligence/estate-management/devices')

driver.maximize_window()


def waitfunction(path):
    wait = WebDriverWait(driver,100)
    wait.until(ec.presence_of_element_located((By.XPATH,path)))

def moveToEstateManagementPage():

    waitfunction('//div[@class="ant-layout-sider-trigger"]')
    nav_slider_btn = driver.find_element_by_xpath('//div[@class="ant-layout-sider-trigger"]')
    nav_slider_btn.click()

    assert driver.current_url == 'https://gn-test-46fc5.web.app/user/home'

    waitfunction('//*[text()="INTELLIGENCE"]')
    estate_option = driver.find_element_by_xpath('//*[text()="INTELLIGENCE"]')
    estate_option.click()

    waitfunction('''//span[@class='submenu-name    ' and text()="Estate Management"]''')
    driver.find_element_by_xpath('''//span[@class='submenu-name    ' and text()="Estate Management"]''').click()

    openDevicePanel()

def openDevicePanel():

    waitfunction('//*[text()="Devices"]')
    driver.find_element_by_xpath('//*[text()="Devices"]').click()

    waitfunction('//button')
    driver.find_element_by_xpath('//button').click()

    fillDeviceDetails()


def fillDeviceDetails():
    addDeviceDetail()


def addDeviceDetail():

    waitfunction('//div[@role="combobox" and @aria-controls="70528fd3-d46c-4207-ae4c-1708e88f36ff"]')
    makelist = Select(driver.find_element_by_xpath('//div[@role="combobox" and @aria-controls="70528fd3-d46c-4207-ae4c-1708e88f36ff"]'))

    makelist.select_by_index(0)



def test_logintest():
    email_box = driver.find_element_by_xpath("//input[@id='emailAddress']")
    passward_box = driver.find_element_by_xpath("//input[@id='password']")
    submit_btn = driver.find_element_by_xpath("//button[@type='submit']")

    email_box.send_keys("sobhagya.sharma@joshtechnologygroup.com")
    passward_box.send_keys("Sob@1507")
    submit_btn.click();

    moveToEstateManagementPage()








