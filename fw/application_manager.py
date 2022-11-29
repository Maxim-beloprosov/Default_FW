from fw.SQL.SQLBase import SQLBase
from fw.driverInstance import DriverInstance
from data.group_data import GroupData
from data.settings import Settings

from fw.api.api_base import APIBase


from fw.api.request.api_actions_in_request import ApiActionsInRequest

from fw.api.request.api_requests import ApiRequests
from fw.fw_base import FWBase

from fw.web.AnyPage import AnyPage
from fw.web.web_base import WebBase
from fw.work_with_email import WorkWithEmail
from fw.work_with_file import WorkWithFile
from fw.work_with_time import work_with_time


class MainPage:
    pass


class ApplicationManager:

    group_data = GroupData()
    settings = Settings()

    def __init__(self):
        self.driver_instance = DriverInstance()
        self.sql = SQLBase(self)
        self.fw_base = FWBase(self)
        self.api_base = APIBase(self)
        self.web_base = WebBase(self)
        self.time = work_with_time()
        self.mail = WorkWithEmail()
        self.work_with_file = WorkWithFile()

        self.web_any_page = AnyPage(self)
        self.web_main_page = MainPage(self)
