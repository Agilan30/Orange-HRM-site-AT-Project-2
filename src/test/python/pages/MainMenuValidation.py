from selenium import webdriver

options_to_validate = [
    "Admin",
    "PIM",
    "Leave",
    "Time",
    "Recruitment",
    "My Info",
    "Performance",
    "Dashboard",
    "Directory",
    "Maintenance",
    "Buzz"
]

chrome_driver_path = "path/to/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.orangehrm.com/")
main_menu = driver.find_element_by_id("MainMenu")

for option in options_to_validate:
    option_xpath = f"//ul[@id='mainMenu']//a[contains(text(), '{option}')]"
    option_element = main_menu.find_element_by_xpath(option_xpath)
    if option_element.is_displayed():
        print(f"{option} is displayed.")
    else:
        print(f"{option} is not displayed.")

# Close the WebDriver
driver.quit()
