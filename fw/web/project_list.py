from selenium.webdriver.common.by import By
import allure
from fw.web.AnyPage import AnyPage


class Locator:
    create_project_todo = (By.XPATH, '//button[@test_id="create-project"]')
    search = (By.XPATH, '//input[@test_id="custom-input"]')


class ProjectList(AnyPage):

    def page_loaded(self):
        """
        Ждем появления элементов страницы
        """
        self.find_element(Locator.search)

    @allure.step('Нажимаем на кнопку Создание проекта')
    def button_to_create_project(self):
        self.page_loaded()
        self.click_element(Locator.create_project_todo)
        self.manager.web_project_create.page_loaded()
        return self.manager.web_project_create

    @allure.step('Вводим текст в поиске')
    def input_text_in_search(self, name_text):
        self.page_loaded()
        self.send_keys_slow(Locator.search, name_text, 100)
        return self

    @allure.step('Переходим в проект с нужным описанием')
    def go_to_project_in_list(self, description_text):
        ticket_item_description = (By.XPATH, f'//a[@class="ticket-item ticket-list__item"]//div[contains(text(),"{description_text}")]')
        self.click_element(ticket_item_description)
        return self


