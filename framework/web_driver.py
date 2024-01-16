from selenium import webdriver

class WebDriver:
    def __init__(self, browser="chrome"):
        # Initialize a web driver based on the specified browser
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

    def get(self, url):
        # Open a specified URL in the web browser
        self.driver.get(url)

    def close(self):
        # Close the web browser
        self.driver.quit()
