# Open https://the-internet.herokuapp.com/login

# Please automate next test cases:
# 1. Login with valid creds (tomsmith/SuperSecretPassword!) and assert you successfully logged in
# 2. Login with invalid creds and check validation error
# 3. Logout from app and assert you successfully logged out

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestLoginForm(unittest.TestCase):
    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("headless")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        # self.driver = webdriver.Chrome()
        self.test_data = {
            'valid_data': ['tomsmith', 'SuperSecretPassword!'],
            'invalid_data': ['11111', '22222!']
        }

    def common_login_steps(self, credentials):
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/login')
        driver.find_element(By.ID, 'username').send_keys(credentials[0])
        driver.find_element(By.ID, 'password').send_keys(credentials[1])
        driver.find_element(By.CSS_SELECTOR, '#login > button').click()
        return driver

    def test_valid_credentials(self):
        driver = self.common_login_steps(self.test_data['valid_data'])
        self.assertTrue(driver.find_element(By.ID, 'flash').is_displayed())

    def test_invalid_credentials(self):
        driver = self.common_login_steps(self.test_data['invalid_data'])
        self.assertEqual(driver.find_element(By.ID, 'flash').get_attribute('class'), 'flash error')

    def test_login_logout_flow(self):
        driver = self.common_login_steps(self.test_data['valid_data'])
        driver.find_element(By.CSS_SELECTOR, '#content > div > a').click()
        self.assertEqual(driver.find_element(By.ID, 'flash').get_attribute('class'), 'flash success')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
