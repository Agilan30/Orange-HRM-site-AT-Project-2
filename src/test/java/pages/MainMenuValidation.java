import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class MainMenuValidation {
    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.get("https://www.orangehrm.com/");
        WebElement mainMenu = driver.findElement(By.id("MainMenu")); 
        String[] optionsToValidate = {
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
        };

        for (String option : optionsToValidate) {
            String optionXPath = "//ul[@id='mainMenu']//a[contains(text(), '" + option + "')]";
            WebElement optionElement = mainMenu.findElement(By.xpath(optionXPath));
            if (optionElement.isDisplayed()) {
                System.out.println(option + " is displayed.");
            } else {
                System.out.println(option + " is not displayed.");
            }
        }

        // Close the WebDriver
        driver.quit();
    }
}
