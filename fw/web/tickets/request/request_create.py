from selenium.webdriver.common.by import By
import allure
import time

from fw.web.tickets.tickets_base import TicketsBase


class Locator:
    cke_contents = (By.XPATH, '//div[@class="ck ck-editor__main"]')
    button_tree_services = (By.CSS_SELECTOR, '[test_id="service-tree-btn"]')
    search_services_on_the_page = (By.CSS_SELECTOR, '[test_id="select-request-service"] input')
    search_services_in_tree = (By.XPATH, '//div[@class="popup-service__search"]/input')
    apply_services = (By.CSS_SELECTOR, '[test_id="apply-service"]')
    fixed_panel_submit = (By.CSS_SELECTOR, '[test_id="fixed-panel-submit"]')
    contractors_rgs = (By.XPATH, '//div[@class ="contractors"]/div[4]')
    list_services = (By.XPATH, '//div[@class="result__list"]')
    click_date_start_when_create = (By.XPATH, '//div[@data-manual="create-request-begin-date"]')
    input_date = (By.XPATH, '//div[@class="input-element"]/input[contains(@class, "date-time-picker__custom-input")]')
    input_hours = (By.XPATH, '//div[contains(@class, "input-element")]//input[@class="time__value"]')
    input_minutes = (By.XPATH, '//div[contains(@class, "input-element")]//input[@class="time__value time__value_minutes"]')
    apply_date = (By.XPATH, '(//div[@class="datepicker-container__content"]//div[@class="button__content"])[2]')


class RequestCreate(TicketsBase):

    def page_loaded(self):
        """
        Ждем появления элементов страницы
        """
        self.find_element(Locator.cke_contents)

    @allure.step('Выбор услуги из дерева при создании заявки')
    def select_services_in_tree(self, name_text):
        self.page_loaded()
        # Переходим в дерево услуг
        self.click_element(Locator.button_tree_services)
        # Ищем услугу
        self.send_keys_slow(Locator.search_services_in_tree, name_text, 100)
        # Выбираем услугу
        catalogue_item_name = (By.XPATH, f'//li[@test_id="service-tree-branch"]//p[contains(text(),"{name_text}")]')
        self.click_element(catalogue_item_name)
        # Применяем услугу
        self.click_element(Locator.apply_services)
        # Ждем появления элементов страницы
        self.find_element(Locator.contractors_rgs)

    @allure.step('Выбор услуги в поисковой строке на странице')
    def select_services_in_search_string(self, name_text):
        self.page_loaded()
        # Ищем услугу
        self.send_keys_slow(Locator.search_services_on_the_page, name_text, 100)
        catalogue_item_name = (By.XPATH, f'//div[@class="result__list"]//div[contains(text(),"{name_text}")]')
        # Перемещаемся к услуге, т.к. анимация не сразу отрисовывает результат поиска
        self.move_to_element(catalogue_item_name)
        # Выбираем услугу
        self.click_element(catalogue_item_name)
        # Ждем появления элементов страницы
        self.find_element(Locator.contractors_rgs)

    @allure.step('Нажать кнопку Создать')
    def button_to_create_request(self):
        self.click_element(Locator.fixed_panel_submit)
        self.manager.web_request_id.page_loaded()
        return self.manager.web_request_id

    @allure.step('Изменить дату начала в заявке при создании')
    def edit_start_date_in_request_when_create(self, correct_date, correct_hours):
        self.page_loaded()
        # Нажимаем на дату начала
        self.click_element(Locator.click_date_start_when_create)
        # Заполняем дату
        self.clear_and_send_keys(Locator.input_date, correct_date)
        # Заполняем время
        self.clear_and_send_keys(Locator.input_hours, correct_hours)
        self.clear_and_send_keys(Locator.input_minutes, '00')

        correct_date_start = correct_date + ', ' + correct_hours + ':00'  # приводим к формату 08.09.2017 11:00
        # Нажимаем кнопку Применить
        self.click_element(Locator.apply_date)
        return correct_date_start
