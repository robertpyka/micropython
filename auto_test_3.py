from selenium import webdriver
import unittest,time


class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(
            executable_path=r"C:\Users\korop\Desktop\Nauka programowania\chromedriver\chromedriver.exe")

    def test_demo_login(self):
        driver = self.driver
        tested_page = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(f'{tested_page}')
        title = driver.title
        print(f"Actual title:  {title}")
        self.assertEqual('Demobank - Bankowość Internetowa - Logowanie', title)

    def test_demo_konta(self):
        driver = self.driver
        tested_page = 'https://demobank.jaktestowac.pl/konta.html'
        driver.get(tested_page)
        title = driver.title
        print(f"Actual title:  {title}")
        self.assertEqual('Demobank - Bankowość Internetowa - Konta', title)

    def test_demo_pulpit(self):
        driver = self.driver
        tested_page = 'https://demobank.jaktestowac.pl/pulpit.html'
        driver.get(tested_page)
        title = driver.title
        print(f"Actual title:  {title}")
        self.assertEqual('Demobank - Bankowość Internetowa - Pulpit', title)

    def test_demo_przelew(self):
        driver = self.driver
        tested_page = 'https://demobank.jaktestowac.pl/przelew_nowy_zew.html'
        driver.get(tested_page)
        title = driver.title
        print(f"Actual title:  {title}")
        self.assertEqual('Demobank - Bankowość Internetowa - Przelew', title)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


class LoginPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(
            executable_path=r"C:\Users\korop\Desktop\Nauka programowania\chromedriver\chromedriver.exe")

    def test_CheckTitle(self):
        driver = self.driver
        tested_page = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(f'{tested_page}')
        title = driver.find_element_by_xpath('//*[@class="wborder"]')
        print(title.text)
        self.assertEqual('Wersja demonstracyjna serwisu demobank', title.text)

    def test_button_login_disable_enable(self):
        driver = self.driver
        tested_page = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(f'{tested_page}')
        button_next = driver.find_element_by_xpath('//*[@id="login_next"]')
        print(f"Button property should be true and is :{button_next.get_property('disabled')}")
        self.assertEqual(True, button_next.get_property('disabled'),
                         f'Expected state of "dalej" button: True , differ from actual: {button_next.get_property("disabled")} , for page url: {tested_page}')
        login_form_input = driver.find_element_by_xpath('//*[@id="login_id"]')
        login_form_input.clear()
        login_form_input.send_keys("1234567")
        self.assertEqual(True, button_next.get_property('disabled'),
                         f'Expected state of "dalej" button: True , differ from actual: {button_next.get_property("disabled")} , for page url: {tested_page}')
        login_form_input.send_keys("a")
        self.assertEqual(False, button_next.get_property('disabled'),
                         f'Expected state of "dalej" button: False , differ from actual: {button_next.get_property("disabled")} , for page url: {tested_page}')

    def test_display_error_message_when_user_submit_less_than_8_signs(self):
        driver = self.driver
        url = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(url)
        login_form_input_element = driver.find_element_by_xpath('//*[@id="login_id"]')
        login_text = '1234567'
        login_form_input_element.send_keys(login_text)
        hint_button_element = driver.find_element_by_xpath(
            '//*[@id="login_id_container"]//*[@class="i-hint-white tooltip widget-info"]')
        hint_button_element.click()
        warning_message_element = driver.find_element_by_xpath('//*[@class="error"]')
        warning_message_text = warning_message_element.text
        self.assertEqual('identyfikator ma min. 8 znaków', warning_message_text,
                         f'Expected warning message differ from actual one for url: {url}')

    def test_after_login_next_page_available(self):
        driver = self.driver
        tested_page = 'https://demobank.jaktestowac.pl/logowanie_etap_1.html'
        driver.get(f'{tested_page}')
        button_next = driver.find_element_by_xpath('//*[@id="login_next"]')
        button_next.click()
        time.sleep(3)
        password_input = driver.find_element_by_xpath('//*[@id = "login_password"]')
        self.assertEqual(False, password_input.get_property("disabled"),
                         f'Page not loaded properly')

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
