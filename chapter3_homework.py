from selenium import webdriver
import unittest,time

class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(
            executable_path=r"C:\Users\korop\Desktop\Nauka programowania\chromedriver\chromedriver.exe")

    def test_check_remind_login(self):
        driver = self.driver
        test_page = "https://demobank.jaktestowac.pl/logowanie_etap_1.html"
        driver.get(test_page)
        remind_button = driver.find_element_by_xpath(('//*[@id="ident_rem"]'))
        remind_button.click()
        time.sleep(1)
        remind_popup = driver.find_element_by_xpath('//*[@class="shadowbox-content contact-popup"]')
        self.assertEqual("ta funkcja jest niedostępna",remind_popup.text)

    def test_login_to_account(self):
        driver = self.driver
        test_page = "https://demobank.jaktestowac.pl/logowanie_etap_2.html"
        driver.get(test_page)
        login_input = driver.find_element_by_xpath('//*[@id="login_id"]')
        login_input.send_keys('asdfghjk')
        password_input = driver.find_element_by_xpath('//*[@id="login_password"]')
        password_input.send_keys("12345678")
        button_login = driver.find_element_by_xpath(('//*[@id="login_next"]'))
        button_login.click()
        time.sleep(2)
        name_surname = driver.find_element_by_xpath('//*[@id="user_name"]')
        self.assertEqual("Jan Demobankowy",name_surname.text)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()