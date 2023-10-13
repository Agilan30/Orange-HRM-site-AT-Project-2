from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Setup:
    def __init__(self):
        self.driver = None

    def setup(self):
        service = Service('/path/to/chromedriver')  # Specify the path to your chromedriver executable
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def close_driver(self):
        # You may need to modify the locator strategy based on the HTML structure of the page
        # For example, using class name: By.CLASS_NAME, 'class-name'
        # Using ID: By.ID, 'element-id'
        # Using CSS selector: By.CSS_SELECTOR, 'css-selector'
        # Using XPath: By.XPATH, 'xpath'
        # Example usage: WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'element-id')))
        # Replace 'element-id' with the appropriate ID of the element you want to wait for
        # You can also use other expected_conditions methods for different conditions
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'element-id')))
        dashboard_page = DashboardPage(self.driver)
        # Call the logout method from DashboardPage class
        # dashboard_page.do_logout()
        self.driver.close()

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    # def do_logout(self):
    #     # Implement the logout functionality here
    #     pass

# Usage
setup_instance = Setup()
setup_instance.setup()
# Perform actions on the page using the driver
# setup_instance.close_driver()  # Call this method when you want to close the browser
