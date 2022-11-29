import time

from selenium.webdriver.common.by import By
import allure


from fw.web.tickets.tickets_base import TicketsBase


class Locator:
    cke_contents = (By.XPATH, '//*[@class="constructor-create-task"]')
    fixed_panel_submit = (By.XPATH, '//button[2][contains(@test_id, "fixed-panel-submit")]')
    contractors_add_btn = (By.XPATH, '//button[@test_id="contractors-add-btn"]')
    contractors_search_input = (By.XPATH, '//div[@test_id="anchor"]//input')


class ProjectCreate(TicketsBase):

    def page_loaded(self):
        """
        Ждем появления элементов страницы
        """
        self.find_element(Locator.cke_contents)

    @allure.step('Нажать кнопку Создать')
    def button_to_create_project(self):
        self.click_element(Locator.fixed_panel_submit)
        self.manager.web_project_id.page_loaded()
        return self.manager.web_project_id

