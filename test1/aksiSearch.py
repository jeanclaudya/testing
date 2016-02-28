from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest


class BasePage(object):

    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class AksiSearch(BasePage):

    """Kelas ini merupakan kelas aksi search, semuah settingan buat serach ada disini"""

    #fungsi search field yang dipake, cari namanya dari inspect element
    def SearchField(self):
        driver = self.driver
        NameLocator = "search_query"
        self.search_field = driver.find_element_by_name(NameLocator)
        self.search_field.clear()

    #fungsi submit key digunakan untuk input keyword yang ingin di cari lalu submit
    def submitKey(self):
        #pada kasus ini inputkan key = "dress" untuk NORMAL TEST
        # sedangkan inputkan key = "lalalal" untuk NEGATIVE TEST
        key = "dress"
        self.search_field.send_keys(key)
        self.search_field.submit()

    #ini pathlokasi hasil nanti
    def pathLocation(self):
        self.products = self.driver.find_elements_by_xpath("//div[@class='right-block']/h5/a[@class='product-name']")

    #untuk mendaptkan nama product
    def getNameProduct(self):
        return self.products

    #print jumlah product
    def print(self):
        print ("Found " + str(len(self.products)) + " products:")

    #validasi kalau ternyata gak ada productnya ini buat cek error
    def NoResult(self):
        return "No results" not in self.driver.page_source