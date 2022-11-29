from pathlib import Path

import allure


class FWBase:

    def __init__(self, ApplicationManager):
        self.manager = ApplicationManager

    def get_project_root(self):
        """Returns project root folder."""
        return Path(__file__).parent.parent

    # Прослойка логирования, если элемент логов выключен то его значение зануляем.
    def request_logs(self, request_type=None, url=None, headers=None, body=None, status_code=None, response=None):
        if self.manager.settings.log_lvl['API']['request_type'] is False: request_type=''
        if self.manager.settings.log_lvl['API']['url'] is False: url=''
        if self.manager.settings.log_lvl['API']['headers'] is False: headers=''
        if self.manager.settings.log_lvl['API']['body'] is False: body=''
        if self.manager.settings.log_lvl['API']['status_code'] is False: status_code=''
        if self.manager.settings.log_lvl['API']['response'] is False: response=''

        self.request(request_type, url, headers, body, status_code, response)

    @allure.step('test')
    def request(self, request_type=None, url=None, headers=None, body=None, status_code=None, response=None):
        pass

