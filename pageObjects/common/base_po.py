from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class BasePo:
    driver = None

    @classmethod
    def browser_launch(cls):
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Maximizes the Chrome window
        # Initialize the WebDriver using ChromeDriverManager to automate ChromeDriver setup
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        cls.driver.implicitly_wait(10)  # Adjust the timeout as needed for finding elements

    @classmethod
    def close_browser(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
