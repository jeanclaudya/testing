import unittest


class BasePage(object):

    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):

        self.driver = driver


class Order(BasePage):


    def pilihProduct(self):
        #pilih product
         product = "Printed Dress"
         self.driver.find_element_by_link_text(product).click()
         print("Pilih dress  ---- OK")

    def AddToChart(self):
        self.driver.find_element_by_xpath(".//*[@id='add_to_cart']/button").click()
        print("Add to chart product ---- OK")

    def CheckOut(self):
        self.driver.find_element_by_xpath(".//*[@id='layer_cart']/div[1]/div[2]/div[4]/a/span").click()
        print("Process Checkout ---- OK")

        #prosess checkout detail
        self.driver.find_element_by_xpath("//*[@id='center_column']/p[2]/a[1]/span").click()
        print("Process Checkout Summary ---- OK")

    def AfterAuthenticationLogin(self):
        #proses checkout 2 setelah authentikasi
        self.driver.find_element_by_xpath(".//*[@id='center_column']/form/p/button").click()
        print("Process Checkout dengan detail Address ---- OK")

    def Agreement(self):
        self.driver.find_element_by_id("cgv").click()
        print("Checklist Box Agrement ---- OK")

    def Shipping(self):
        self.driver.find_element_by_xpath(".//*[@id='form']/p/button").click()
        print("Shipping Checkout ---- OK")

    def Payment(self):
        #pilihan payment dengan bank transfer
        self.driver.find_element_by_xpath(".//*[@id='HOOK_PAYMENT']/div[1]/div/p/a").click()
        print("Pilihan payment dengan bank transfer ---- OK")

    def Confirmation(self):
        self.driver.find_element_by_xpath(".//*[@id='cart_navigation']/button").click()
        print("Konfirmasi Akhir Checkout ---- OK")


    def tearDown(self):

        self.driver.close()

