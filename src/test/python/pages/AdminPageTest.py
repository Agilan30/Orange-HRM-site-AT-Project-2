from selenium import webdriver

# Set the path to the chromedriver executable
chrome_driver_path = "path/to/chromedriver.exe"

# Create a new Chrome browser instance
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Navigate to the specified URL
driver.get("https://www.orangehrm.com/")

# Find the element with id "pageTitle"
page_title_element = driver.find_element_by_id("pageTitle")

# Get the text of the element
title_text = page_title_element.text

# Check if the title text is equal to "OrangeHRM"
if title_text == "OrangeHRM":
    print("Test Passed: The Admin Page title is 'OrangeHRM'.")
else:
    print("Test Failed: The Admin Page title is not 'OrangeHRM'.")

# Close the WebDriver
driver.quit()
