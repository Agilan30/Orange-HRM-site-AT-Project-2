package pages;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

import java.util.List;

public class DashboardPage {
    @FindBy(className = "oxd-userdropdown-tab")
    public WebElement btnProfileTab;
    @FindBy(partialLinkText = "Logout")
    public WebElement logOutLink;
    @FindBy(className = "oxd-main-menu-item--name")
    public List<WebElement> menus;

    public DashboardPage(WebDriver driver) {

        PageFactory.initElements(driver, this);
    }

   options_to_validate = ["user management", "Job", "Organizations", "Qualifications", "Nationalities", "Corporate Banking", "Configuration"]

# Locate the header element (you should use the appropriate HTML selector)
header_element = driver.find_element_by_css_selector('header')  # Replace with the actual selector

# Extract the text from the header element
header_text = header_element.text

# Check if each option is present in the header text
for option in options_to_validate:
    if option.lower() in header_text.lower():
        print(f"Option '{option}' is displayed in the header.")
    else:
        print(f"Option '{option}' is NOT displayed in the header.")

# Close the web driver
driver.quit()
In this code:

You need to specify the path to your web driver executable (e.g., ChromeDriver) in the executable_path parameter when creating the webdriver instance.

Replace 'https://example.com' with the actual URL of the webpage you want to test.

Use the appropriate HTML selector to locate the header element. In this example, I've used the placeholder 'header' for demonstration purposes. You should replace it with the actual CSS selector that matches the header element on your webpage.

The script extracts the text from the header element and checks if each option is present in the header text. It performs a case-insensitive comparison to ensure flexibility.

Finally, the web driver is closed.

Make sure to customize the code according to your specific webpage's structure and the testing framework you are using.






}
