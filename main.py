import unittest
from selenium import webdriver
#from utilities.BaseClass import BaseClass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestOne)
    suite.addTest(TestTwo)
    return suite

@unittest.skip
class TestOne(unittest.TestCase):

    def test1(self):
        self.driver = webdriver.Chrome('C:/Users/HARDPC/chrome webdrivers/chromedriver')
        self.driver.get("https://lambdatest.github.io/sample-todo-app/")
        self.driver.find_element(By.XPATH, "//input[@name='li1']").click()
        self.driver.find_element(By.XPATH, "//input[@name='li2']").click()
        element = self.driver.find_element(By.XPATH, "//*[@id='sampletodotext']")
        element.send_keys("Test")
        self.driver.find_element(By.XPATH, "//*[@id='addbutton']").click()
        #input("Press Enter to continue...")
        self.driver.quit()
        print("OK1")


@unittest.skip
class TestTwo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.driver.get("https://www.saucedemo.com/")


    def test_1(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='user-name']")))
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='password']")))
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='login-button']")))
        except:
            self.assertRaises("blad1")
        finally:
            login = self.driver.find_element(By.XPATH, "//*[@id='user-name']")
            login.send_keys("standard_user")
            passw = self.driver.find_element(By.XPATH, "//*[@id='password']")
            passw.send_keys("secret_sauce")
            self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()

        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[ @ id = 'add-to-cart-sauce-labs-bolt-t-shirt']")))
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a")))
        except:
            self.assertRaises("blad2")
        finally:
            self.driver.find_element(By.XPATH, "//*[ @ id = 'add-to-cart-sauce-labs-bolt-t-shirt']").click()
            self.driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()

        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='checkout']")))
        except:
            self.assertRaises("blad3")
        finally:
            self.driver.find_element(By.XPATH, "//*[@id='checkout']").click()

        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='first-name']")))
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='last-name']")))
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='postal-code']")))
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "// *[ @ id = 'continue']")))
        except:
            self.assertRaises("blad4")
        finally:
            name = self.driver.find_element(By.XPATH, "//*[@id='first-name']")
            lname = self.driver.find_element(By.XPATH, "//*[@id='last-name']")
            zipcode = self.driver.find_element(By.XPATH, "//*[@id='postal-code']")
            name.send_keys("Julon")
            lname.send_keys("sBarbariusz")
            zipcode.send_keys("20-202")
            self.driver.find_element(By.XPATH, "// *[ @ id = 'continue']").click()

        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='finish']")))
        except:
            self.assertRaises("blad5")
        finally:
            self.driver.find_element(By.XPATH, "//*[@id='finish']").click()

        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id='back-to-products']")))
        except:
            self.assertRaises("blad6")
        finally:
            self.driver.find_element(By.XPATH, "//*[@id='back-to-products']").click()

    def test_2(self):
        pass

    def tearDown(self):
        #input("Press Enter to continue...")
        self.driver.quit()
        #print("OK Test Two")


class TestThree(unittest.TestCase):

    def setUp(self):
        pass

    def test_1(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())