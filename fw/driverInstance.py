from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from data.settings import Settings


class DriverInstance:

    def __init__(self):
        self.settings = Settings

    driver = None

    def get_driver(self):
        options = webdriver.ChromeOptions()

        if self.settings.Browser['headless']:
            options.headless = True
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--window-size=1920,1080')
            options.add_argument('--disable-gpu')
        else:
            options.headless = False

        capabilities = DesiredCapabilities.CHROME
        capabilities['goog:loggingPrefs'] = {'browser': 'ALL',
                                             'performance': 'ALL',
                                             'server': 'ALL',
                                             'client': 'ALL'}

        if self.settings.Browser['Remote']:
            self.driver = webdriver.Remote(
                command_executor=self.settings.selenium_server,
                proxy=None,
                options=options,
                desired_capabilities=capabilities)
        else:
            self.driver = webdriver.Chrome(options=options, desired_capabilities=capabilities)

        if self.settings.Browser['headless'] is False:
            self.driver.maximize_window()
        return self.driver

    def stop_driver(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
