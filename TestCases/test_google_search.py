# tests/test_google_search.py
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.google_search_page import GoogleSearchPage
from TestData.data_reader import DataReader

# Set the path to your WebDriver executable



def test_google_search(driver):
    search_page = GoogleSearchPage(driver)
    search_page.load()
    driver.maximize_window()
    time.sleep(5)
    search_page.setEmail("suresh@gmail.com")
    time.sleep(5)
    search_page.setPhone("8985256492")
    time.sleep(5)
  
'''def test_button_homepage(driver):
    search_page = GoogleSearchPage(driver)
    search_page.load()
    assert search_page.VerifyHomeButton() == True , "not displayed"
    assert search_page.VerifyContactButton() == True , "not displayed"
    assert search_page.VerifyAboutButton() == True , "not displayed"
    assert search_page.VerifyCarrerButton() == True , "not displayed"




    time.sleep(10)'''

