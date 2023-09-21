package pages;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;

public class AdminPageTest {

    public static void main(String[] args) {
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.get("https://www.orangehrm.com/");
        WebElement pageTitle = driver.findElement(By.id("pageTitle")); 
        String titleText = pageTitle.getText();
        if (titleText.equals("OrangeHRM")) {
            System.out.println("Test Passed: The Admin Page title is 'OrangeHRM'.");
        } else {
            System.out.println("Test Failed: The Admin Page title is not 'OrangeHRM'.");
        }

        // Close the WebDriver
        driver.quit();
    }
}
