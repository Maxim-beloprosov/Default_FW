import allure
from selenium.webdriver.common.by import By

from fw.web.tickets.tickets_base import TicketsBase


class Locator:
    fixed_panel_submit = (By.XPATH, '//div[@class="submit-fixed-panel submit-fixed-panel submit-fixed-panel_violet"]/button[2]')
    cke_contents = (By.XPATH, '//div[@class="ck ck-editor__main"]')


class TaskCreate(TicketsBase):

    def page_loaded(self):
        """
        Ждем появления элементов страницы
        """
        self.find_element(Locator.cke_contents)

    @allure.step('Нажать кнопку Создать')
    def click_button_to_create_task(self):
        self.click_element(Locator.fixed_panel_submit)
        self.manager.web_task_id.page_loaded()
        return self.manager.web_task_id



