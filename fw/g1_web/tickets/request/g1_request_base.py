import time

import allure
from selenium.webdriver.common.by import By

from fw.g1_web.tickets.g1_ticket_base import G1TicketsBase


class Locator:
    request_department = (By.XPATH, '//div[@id="Department_chosen"]')
    request_category = (By.XPATH, '//div[@id="Category_chosen"]')
    request_type = (By.XPATH, '//div[@id="RequestType_chosen"]')
    request_job_type = (By.XPATH, '//div[@id="JobType_chosen"]')
    text_department = (By.XPATH, '//div[@id="Department_chosen"]/a/span')
    text_category = (By.XPATH, '//div[@id="Category_chosen"]/a/span')
    text_request_type = (By.XPATH, '//div[@id="RequestType_chosen"]/a/span')
    text_job_type = (By.XPATH, '//div[@id="JobType_chosen"]/a/span')
    text_region = (By.XPATH, '//div[@class="ga_rtp_info"]/div[3]/div[@class="ga_rtp_info_val"]')

class G1RequestBase(G1TicketsBase):
    @allure.step('Установить "Отдел"')
    def g1_set_department(self, input_value_department):
        self.click_element(Locator.request_department)
        need_department = (By.XPATH, f'//div[@id="Department_chosen"]//li[contains(text(), "{input_value_department}")]')
        self.move_to_element(need_department)
        self.click_element(need_department)
        return self

    @allure.step('Установить "Категория"')
    def g1_set_category(self, input_value_category):
        self.click_element(Locator.request_category)
        need_category = (By.XPATH, f'//div[@id="Category_chosen"]//li[contains(text(), "{input_value_category}")]')
        self.move_to_element(need_category)
        self.click_element(need_category)
        return self

    @allure.step('Установить "Тип"')
    def g1_set_request_type(self, request_type):
        self.click_element(Locator.request_type)
        need_request_type = (By.XPATH, f'//div[@id="RequestType_chosen"]//li[contains(text(), "{request_type}")]')
        self.move_to_element(need_request_type)
        self.click_element(need_request_type)
        return self

    @allure.step('Установить "Вид"')
    def g1_set_job_type(self, job_type):
        self.click_element(Locator.request_job_type)
        need_job_type = (By.XPATH, f'//div[@id="JobType_chosen"]//li[contains(text(), "{job_type}")]')
        self.move_to_element(need_job_type)
        self.click_element(need_job_type)
        return self

    def g1_get_department(self):
        return self.get_tag_text(Locator.text_department)

    def g1_get_category(self):
        return self.get_tag_text(Locator.text_category)

    def g1_get_request_type(self):
        return self.get_tag_text(Locator.text_request_type)

    def g1_get_job_type(self):
        return self.get_tag_text(Locator.text_job_type)
    def g1_get_region(self):
        return self.get_tag_text(Locator.text_region)
