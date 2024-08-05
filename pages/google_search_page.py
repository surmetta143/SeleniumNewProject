# pages/google_search_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GoogleSearchPage:
    URL = "http://localhost:63342/pythonProject/suresh.html?_ijt=9s6h735dt42jtveref9p84824r&_ij_reload=RELOAD_ON_SAVE"
    SEARCH_BOX = (By.NAME, "email")
    Password = (By.ID,"mobile")
    Home = (By.ID, "home")
    Career = (By.ID, "career")
    Contact = (By.ID, "contact")
    About = (By.ID, "about")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def setEmail(self, text):
        search_box = self.driver.find_element(*self.SEARCH_BOX)
        search_box.send_keys(text)
    def setPhone(self, text):
        search_box = self.driver.find_element(*self.Password)
        search_box.send_keys(text)
    def VerifyHomeButton(self, text):
        button = self.driver.find_element(*self.Home)
        return button.is_displayed()
    def VerifyCarrerButton(self, text):
        button = self.driver.find_element(*self.Career)
        return button.is_displayed()
    def VerifyContactButton(self, text):
        button = self.driver.find_element(*self.Contact)
        return button.is_displayed()
    def VerifyAboutButton(self, text):
        button = self.driver.find_element(*self.About)
        return button.is_displayed()

