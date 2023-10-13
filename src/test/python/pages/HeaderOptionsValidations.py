from selenium import webdriver

def validate_option(header, option_text):
    try:
        option = header.find_element_by_link_text(option_text)
        if option.is_displayed():
            print(f"{option_text} is displayed in the header.")
        else:
            print(f"{option_text} is NOT displayed in the header.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    chrome_driver_path = "path/to/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get("https://www.orangehrm.com/")
    
    header_css_selector = "your-header-css-selector"
    header = driver.find_element_by_css_selector(header_css_selector)
    
    options_to_validate = ["user management", "Job", "Organizations", "Qualifications", 
                           "Nationalities", "Corporate Banking", "Configuration"]
    
    for option_text in options_to_validate:
        validate_option(header, option_text)
    
    driver.quit()
