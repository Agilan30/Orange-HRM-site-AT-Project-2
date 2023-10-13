import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages import DashboardPage, LoginPage, EmployeeInfoPage
from utils import Utils
import json

class EmployeeTestRunner(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='path/to/chromedriver')  # Provide path to chromedriver executable
        self.driver.get("your_website_url")  # Replace with your website URL
        self.driver.maximize_window()

    def test_login_with_second_users(self):
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
        user_object = Utils.load_json_file_containing_array("./src/test/resources/Employee.json", 1)
        username = user_object.get("username")
        password = user_object.get("password")
        login_page.do_login(username, password)
        time.sleep(1.5)

        # Assertion
        header_text = self.driver.find_element(By.TAG_NAME, "h6").text
        header_expected = "Dashboard"
        self.assertEqual(header_text, header_expected)
        time.sleep(1.5)

    def test_update_user_information(self):
        employee_info_page = EmployeeInfoPage(self.driver)
        employee_info_page.user_menu[2].click()
        Utils.do_scroll(self.driver, 500)
        employee_info_page.select_gender()
        time.sleep(1)
        Utils.do_scroll(self.driver, 500)
        employee_info_page.select_blood_type()
        time.sleep(1)
        self.driver.refresh()
        employee_info_page.select_contact()
        time.sleep(1)

        # Assertion
        header_text = self.driver.find_element(By.TAG_NAME, "h6").text
        header_expected = "PIM"
        self.assertEqual(header_text, header_expected)
        time.sleep(1)

    def test_logout(self):
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.do_logout()
        self.driver.close()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
