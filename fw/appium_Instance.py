from data.settings import Settings
from appium.webdriver.appium_service import AppiumService
from appium import webdriver


class AppiumInstance:

    def __init__(self):
        self.settings = Settings

    appium_driver = None

    def get_Appium_Driver_Instance(self):
        if self.appium_driver is None:
            capabilities = {
                'platformName': self.settings.mobile_stand[self.settings.mobile_branch]['platformName'],
                'platformVersion': self.settings.mobile_stand[self.settings.mobile_branch]['platformVersion'],
                'app': self.settings.mobile_stand[self.settings.mobile_branch]['app'],
                'appPackage': self.settings.mobile_stand[self.settings.mobile_branch]['appPackage'],
                'appActivity': self.settings.mobile_stand[self.settings.mobile_branch]['appActivity'],
            }
            self.appium_driver = webdriver.Remote(self.settings.mobile_stand['appium_server'], desired_capabilities=capabilities)
            self.appium_driver.implicitly_wait(3)
        return self.appium_driver

    def stop_Test(self):
        if self.appium_driver is not None:
            self.appium_driver.quit()
            self.appium_driver = None
