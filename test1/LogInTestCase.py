from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
import unittest



class BasePage(object):

    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):

        self.driver = driver

class LoginTest(BasePage):

    def test_Login(self):
        driver =  self.driver
        #masuk ke halaman login
        #driver.find_element_by_xpath("driver.find_elements_by_xpath").click()

        #login
        self.emailField    = driver.find_element_by_name("email")
        self.passwordField = driver.find_element_by_name("passwd")


        #input data
        email ="jeanclaudyawp@gmail.com"
        password = "lupabanget"

        self.emailField.send_keys(email)
        self.passwordField.send_keys(password)

        #klik button sign in
        self.driver.find_element_by_id("SubmitLogin").click()

    def gagalLogin(self):

        return "Authentication failed." not in self.driver.page_source

    def tearDown(self):
        self.driver.quit()

