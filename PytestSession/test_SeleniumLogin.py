from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest

driver = None


def setUp_module(module):
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.delete_all_cookies()
    driver.get("https://naveenautomationlabs.com/opencart/index.php?route=account/login")


def tearDown_module(module):
    print("Fuck off")


# def test_NALLoginLaunchUrl():
#     driver.get("https://naveenautomationlabs.com/opencart/index.php?route=account/login")
#     driver.implicitly_wait(30)
#     driver.find_element("//*[@id='top-links']/ul/li[2]/a").click()
#
#
# test_NALLoginLaunchUrl()()
setUp_module()
tearDown_module()