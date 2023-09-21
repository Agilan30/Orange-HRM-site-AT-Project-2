# Web Automation on OrangeHRM Website with Selenium TestNG

## What is Automation?

Automation is the process of using software tools and scripts to perform tasks that would typically be done manually by a human. In the context of software testing, automation involves using tools to execute test cases and compare the actual results with the expected results automatically.

## Why we use Selenium TestNG for Automation?

Selenium is a popular open-source testing tool widely used for automating web browsers. It allows developers and testers to automate web-based applications' testing across multiple browsers and platforms. Selenium provides a set of APIs to interact with web elements and manipulate their properties and behaviors, making it an ideal tool for automating UI tests.

TestNG is a testing framework for Java that is designed to be more flexible and powerful than JUnit. It supports a wide range of testing functionalities, including unit, integration, and end-to-end testing, as well as parallel execution, data-driven testing, and reporting. TestNG is often used with Selenium to create robust and scalable test automation framework.

## Technology used:
- Selenium Webdriver
- TestNG Framework
- Java
- Gradle
- Intellij idea
- Allure

## How to run this project

- Clone this project
- Hit the following command into the terminal:
 ```gradle clean test```
 
- For generating Allure Report use these commands:
```allure generate allure-results --clean -o allure-report``` and
```allure serve allure-results```

## Scenerio:

- Login to orange hrm demo site: https://opensource-demo.orangehrmlive.com/
- Reset Password through Forgot Password Link.
- Now validate the title of the Admin page as "OrangeHRM"
- Then validate if the options - User Management, Job, Organization, Qualifications, Nationalities, Corporate Banking, Configurations are displayed on the header of the web page.
- Then validate the Main Menu of the Orange HRM site.
- Check if all the options - Admin, PIM, Leave, Time, Recruitment, My Info, Performance, Dashboard, Directory, Maintenance, Buzz are displayed.
- Now logout from admin and login with the 2nd user from your JSON list


## Test case check list based on the Scenerio:

- Admin Login with Invalid credential. 
- Forgot Password Validation.
- Reset Password Link.
- New Password validation
- Admin Page title validation.
- Header validation of web page.
- Main Menu validation.


![A2](https://user-images.githubusercontent.com/123433625/221358808-8c67c1a2-769e-4ed4-b0a2-0f49e2b8e7a1.jpg)





