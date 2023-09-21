import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class HeaderOptionsValidation {
    public static void main(String[] args) {
        
        System.setProperty("webdriver.chrome.driver", "path/to/chromedriver.exe");
        WebDriver driver = new ChromeDriver();
        driver.get("https://www.orangehrm.com/"); 
        WebElement header = driver.findElement(By.cssSelector("your-header-css-selector"));
    
        validateOption(header, "user management");
        validateOption(header, "Job");
        validateOption(header, "Organizations");
        validateOption(header, "Qualifications");
        validateOption(header, "Nationalities");
        validateOption(header, "Corporate Banking");
        validateOption(header, "Configuration");

        driver.quit();
    }
    
    
    private static void validateOption(WebElement header, String optionText) {
        WebElement option = header.findElement(By.linkText(optionText));
        if (option.isDisplayed()) {
            System.out.println(optionText + " is displayed in the header.");
        } else {
            System.out.println(optionText + " is NOT displayed in the header.");
        }
    }
}
