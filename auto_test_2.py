from selenium import webdriver
import unittest

class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\korop\Desktop\Nauka programowania\chromedriver\chromedriver.exe")
    def test_demo_login(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/logowanie_etap_1.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Logowanie' == title


    def test_demo_konta(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/konta.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Konta' == title


    def test_demo_pulpit(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/pulpit.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Pulpit' == title

    def test_demo_przelew(self):
        driver = self.driver
        driver.get('https://demobank.jaktestowac.pl/przelew_nowy_zew.html')
        title = driver.title
        print(title)
        assert 'Demobank - Bankowość Internetowa - Przelew' == title

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

