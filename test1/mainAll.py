import unittest
from selenium import webdriver
import aksiSearch
import orderProductCase
import LogInTestCase

class SearchAndOrderTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_SearchAndOrder(self):

        #Load the fungsi search. .
        fungsiSearch = aksiSearch.AksiSearch(self.driver)

        #Load the fungsi order. .
        fungsiOrder = orderProductCase.Order(self.driver)

        #Load fungsi Login
        fungsiLogin = LogInTestCase.LoginTest(self.driver)




        #Menjalankan fungsi search
        fungsiSearch.SearchField()
        fungsiSearch.submitKey()
        fungsiSearch.pathLocation()
        fungsiSearch.print()

        products = fungsiSearch.getNameProduct()

        for product in products:
            print (product.text)



        assert fungsiSearch.NoResult(), "No results"

        #print(fungsiSearch.NoResult())



        #Menjalankan fungsi order dengan Login
            #pilih product
        fungsiOrder.pilihProduct()

            #addto chart
        fungsiOrder.AddToChart()

            #proses CheckOut
        fungsiOrder.CheckOut()

           #Login
             #Load fungsi Login
        fungsiLogin.test_Login()
        assert fungsiLogin.gagalLogin(), "Autentikasi gagal / gagal Login."

            #checkout setelah authentikasi
        fungsiOrder.AfterAuthenticationLogin()

            #agreement
        fungsiOrder.Agreement()

            #shipping
        fungsiOrder.Shipping()

            #payment
        fungsiOrder.Payment()

            #konfirmasi
        fungsiOrder.Confirmation()



    def tearDown(self):

        self.driver.close()

if __name__ == "__main__":

    unittest.main()
