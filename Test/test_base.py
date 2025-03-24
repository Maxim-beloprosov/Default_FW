import allure

from fw.application_manager import ApplicationManager


class TestBase:

    APP = ApplicationManager()

    def setup_class(self):
        self.main_page = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page']

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def teardown_class(self):
        pass

