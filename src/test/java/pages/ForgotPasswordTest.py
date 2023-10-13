from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to chromedriver.exe
chrome_driver_path = "path_to_chromedriver.exe"

# Initialize Chrome browser
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

try:
    # Find the "Forgot Password" link and click it
    forgot_password_link = driver.find_element(By.LINK_TEXT, "Forgot Password")
    forgot_password_link.click()

    # Wait for the title to contain "Forgot Password"
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_contains("Forgot Password"))

    # Get the current page title
    page_title = driver.title

    # Check if the page title contains "Forgot Password"
    if "Forgot Password" in page_title:
        print("Forgot Password link is working. Test passed.")
    else:
        print("Forgot Password link is not working. Test failed.")

except Exception as e:
    print("Exception: " + str(e))

finally:
    # Close the browser
    driver.quit()
