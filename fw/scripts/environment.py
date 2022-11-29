import os
import sys

from fw.fw_base import FWBase


class Environment(FWBase):

    def update_environment(self, web=False):
        """
        Метод формирования текста для записи в файл окружения
        :param web:
        :return:
        """
        text = ''
        text += f"Python.Version={sys.version}\n"
        text += f'Stand={self.manager.settings.branch}\n'
        text += f"URL={self.manager.settings.GLOBAL[self.manager.settings.branch]['main_page']}\n"
        text += f"API={self.manager.api_base.get_base_url()}\n"

        if web:
            text += f'Browser={self.manager.settings.Browser["Name"]}\n'
            text += f'Headless={self.manager.settings.Browser["headless"]}\n'
            text += f'Remote={self.manager.settings.Browser["Remote"]}\n'
            if self.manager.settings.Browser["Remote"]:
                text += f'Selenium Server={self.manager.settings.selenium_server}\n'
        return text

    def update_environment_file(self, web):
        """
        Метод перезаписи данный в файл окружения для allure-results
        :param web:
        :return:
        """
        try:
            text = self.update_environment(web)
            if os.path.exists(os.path.join(self.manager.api_users.get_project_root(), 'allure-results')) is False:
                os.mkdir(os.path.join(self.manager.api_users.get_project_root(), 'allure-results'))

            path = os.path.join(self.manager.api_users.get_project_root(), 'allure-results', 'environment.properties')

            with open(path, 'w', newline='') as file:
                file.write(text)
        except:
            pass
