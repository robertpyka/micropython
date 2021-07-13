import unittest
from selenium import webdriver

class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\korop\Desktop\Nauka programowania\chromedriver\chromedriver.exe")
        print("Start test")
    #def test_pierwszy(self):

    def test_drugi(self):
        driver = self.driver
        driver.get('https://theuselessweb.com')
        title = driver.title
        print(title)
        assert 'The Useless Web' == title

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        print("Finish test")