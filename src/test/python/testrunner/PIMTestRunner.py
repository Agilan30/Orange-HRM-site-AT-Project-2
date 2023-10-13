import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import faker
import random
import utils

class PIMTestRunner:

    def __init__(self, driver):
        self.driver = driver
        self.dashboard_page = DashboardPage(driver)
        self.login_page = LoginPage(driver)
        self.pim_page = PIMPage(driver)

    def do_login_with_invalid_creds(self):
        self.login_page = LoginPage(self.driver)
        message_actual = self.login_page.do_login_with_invalid_creds("admin", "wrong password")
        message_expected = "Invalid credentials"
        assert message_expected in message_actual
        time.sleep(1.5)

    def do_login(self):
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        user_object = utils.load_json_file("./src/test/resources/Admin.json")
        username = user_object.get("username")
        password = user_object.get("password")
        self.login_page.do_login(username, password)

        # Assertion
        header_text = self.driver.find_element_by_tag_name("h6").text
        header_expected = "Dashboard"
        assert header_text == header_expected
        time.sleep(1.5)
        self.dashboard_page.menus[1].click()
        time.sleep(1.5)

    def create_employee_without_username(self):
        self.pim_page = PIMPage(self.driver)
        time.sleep(1.5)
        self.pim_page.button[1].click()
        fake = faker.Faker()
        firstname = fake.first_name()
        lastname = fake.last_name()
        employee_id = random.randint(10000, 99999)
        password = "Agilan@123"
        time.sleep(1.5)
        self.pim_page.create_employee_without_username(firstname, lastname, employee_id, password)

        # Assertion
        header_actual = self.driver.find_elements_by_class_name("oxd-text")[15].text
        header_expected = "Required"
        assert header_expected in header_actual
        self.driver.refresh()

    def create_employee1(self):
        self.pim_page = PIMPage(self.driver)
        fake = faker.Faker()
        firstname = fake.first_name()
        lastname = fake.last_name()
        employee_id = random.randint(10000, 99999)
        username = "Agilan3001" + str(random.randint(1000, 9999))
        password = "Agilan@123"
        time.sleep(1.5)
        self.pim_page.create_employee(firstname, lastname, employee_id, username, password)

        # Assertion
        header_actual = self.driver.find_elements_by_class_name("orangehrm-main-title")[0].text
        header_expected = "Personal Details"
        if header_expected in header_actual:
            utils.add_json_array(firstname, lastname, employee_id, username, password)
        self.driver.find_elements_by_class_name("oxd-topbar-body-nav-tab-item")[2].click()
        time.sleep(1.5)

    def create_employee2(self):
        self.pim_page = PIMPage(self.driver)
        fake = faker.Faker()
        firstname = fake.first_name()
        lastname = fake.last_name()
        employee_id = random.randint(10000, 99999)
        username = "Hema2000" + str(random.randint(1000, 9999))
        password = "Hema@456"
        time.sleep(1.5)
        self.pim_page.create_employee(firstname, lastname, employee_id, username, password)

        # Assertion
        header_actual = self.driver.find_elements_by_class_name("orangehrm-main-title")[0].text
        header_expected = "Personal Details"
        if header_expected in header_actual:
            utils.add_json_array(firstname, lastname, employee_id, username, password)
        time.sleep(1)

    def search_employee_by_invalid_name(self):
        self.pim_page = PIMPage(self.driver)
        self.dashboard_page.menus[1].click()
        fake = faker.Faker()
        name = fake.first_name()
        employee_name = name
        self.pim_page.search_employee_by_invalid_name(employee_name)
        time.sleep(1.5)

        # Assertion
        message_actual = self.driver.find_elements_by_class_name("oxd-text--span")[11].text
        message_expected = "No Records Found"
        assert message_expected == message_actual
        time.sleep(1)

    def search_employee_by_name(self):
        user_object = utils.load_json_file_containing_array("./src/test/resources/Employee.json", 0)
        employee_first_name = user_object.get("firstname")
        employee_last_name = user_object.get("lastname")
        employee_name = employee_first_name + " " + employee_last_name

        self.pim_page.txt_search_emp_name[1].send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
        self.pim_page.search_employee_by_valid_name(employee_name)
        time.sleep(1.5)

        # Assertion
        message_actual = self.driver.find_elements_by_class_name("oxd-text--span")[11].text
        message_expected = "Record Found"
        assert message_expected in message_actual
        time.sleep(1)

    def update_employee_by_id(self):
        emp_id = random.randint(10000, 99999)
        random_employee_id = str(emp_id)
        utils.update_json_object("./src/test/resources/Employee.json", "employeeId", random_employee_id, 0)
        utils.do_scroll(self.driver, 300)
        self.pim_page.update_employee_by_id(random_employee_id)
        time.sleep(1.5)

        # Assertion
        header_actual = self.driver.find_elements_by_class_name("orangehrm-main-title")[0].text
        header_expected = "Personal Details"
        assert header_expected in header_actual

    def search_employee_by_id(self):
        self.dashboard_page.menus[1].click()
        user_object = utils.load_json_file_containing_array("./src/test/resources/Employee.json", 0)
        employee_id = user_object.get("employeeId")
        self.pim_page.search_employee_by_valid_id(employee_id)
        time.sleep(1.5)
        utils.do_scroll(self.driver, 500)

        # Assertion
        message_actual = self.driver.find_elements_by_class_name("oxd-text--span")[11].text
        message_expected = "Record Found"
        assert message_expected in message_actual
        time.sleep(1)

    def log_out(self):
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.do_logout()
        self.driver.close()

