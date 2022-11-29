import allure
from selenium.webdriver.common.by import By
import time

from fw.web.tickets.tickets_base import TicketsBase


class Locator:
    page_loaded = (By.XPATH, '//div[@class="async-wrapper-constructor-type-field-editor"]')
    append_description_open_editor = (By.CSS_SELECTOR, '[test_id="append-description-open-editor"]')
    append_description_submit_btn = (By.CSS_SELECTOR, '[test_id="append-description-submit-btn"]')
    contractors_activator = (By.XPATH, '//div[contains(@class, "dropdown-block contractor")]//div[@test_id="contractors-dropdown-activator"]')
    contractors_search_input = (By.CSS_SELECTOR, '[test_id="contractors-search"] input')
    action_cancel_btn = (By.CSS_SELECTOR, '[test_id="Action-Cancel"]')
    action_submit_btn = (By.CSS_SELECTOR, '[test_id="actionsubmit-btn"]')
    action_resolve_btn = (By.CSS_SELECTOR, '[test_id="Action-Resolve"]')
    assign_to_me = (By.CSS_SELECTOR, '[test_id="Action-AssignToMe"]')
    click_date_start_after_create = (By.XPATH, '//div[@class="dropdown-block time"]//div[@class="datepicker-date-activator"]')
    delete_date_start_after_create = (By.XPATH, '//div[@test_id="ticket-begin-date"]//div[@class="datepicker-date-activator__icon"]')
    input_date = (By.XPATH, '//div[@class="input-element"]/input[contains(@class, "date-time-picker__custom-input")]')
    input_hours = (By.XPATH, '//div[contains(@class, "input-element")]//input[@class="time__value"]')
    input_minutes = (By.XPATH, '//div[contains(@class, "input-element")]//input[@class="time__value time__value_minutes"]')
    apply_date = (By.XPATH, '(//div[@class="datepicker-container__content"]//div[@class="button__content"])[2]')
    block_comment = (By.XPATH, '//div[@class="comments"]//input')
    request_custom_fields_preloader = (By.XPATH, '//div[@class="request-custom-fields"]//div[contains(@class, "preloader")]')


class RequestId(TicketsBase):

    def page_loaded(self):
        """
        Ждем появления элементов страницы
        """
        self.find_element(Locator.page_loaded)

    @allure.step('Назначить заявку на себя')
    def assign_request_to_me(self, correct_contractor):
        self.page_loaded()
        self.scroll_to_element(Locator.assign_to_me)
        self.click_element(Locator.assign_to_me)
        # Ожидаем, пока будет корректный исполнитель у заявки в апи и обновляем страницу
        self.waiting_the_correct_contractor(correct_contractor)
        return self

    @allure.step('Изменить дату начала в заявке после создания')
    def edit_start_date_in_request_after_create(self, correct_date, correct_hours):
        # Раскрываем временные интервалы
        self.open_normative_time()
        time.sleep(0.5)
        # Нажимаем на дату начала
        self.click_element(Locator.click_date_start_after_create)
        # Заполняем дату
        self.clear_and_send_keys(Locator.input_date, correct_date)
        # Заполняем часы
        self.clear_and_send_keys(Locator.input_hours, correct_hours)
        # Заполняем минуты
        self.clear_and_send_keys(Locator.input_minutes, '00')
        correct_date_start = correct_date + ', ' + correct_hours + ':00'  # приводим к формату 08.09.2017 11:00
        # Нажимаем кнопку Применить
        self.click_element(Locator.apply_date)
        return correct_date_start

    @allure.step('Удалить дату начала в заявке после создания')
    def delete_start_date_in_request_after_create(self):
        # Раскрываем временные интервалы
        self.open_normative_time()
        time.sleep(0.5)
        # Удаляем дату начала
        self.move_to_element(Locator.delete_date_start_after_create)
        self.click_element(Locator.delete_date_start_after_create)
        return self

    @allure.step('Отправить комментарий')
    def send_comment(self, comment_text):
        self.waiting_for_item_not_display(Locator.request_custom_fields_preloader)
        self.click_element(Locator.block_comment)
        self.fill_comment(comment_text)
        self.button_send_comment()
        return self

