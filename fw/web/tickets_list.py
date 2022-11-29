import time

from selenium.webdriver.common.by import By
import allure
from fw.web.AnyPage import AnyPage


class Locator:
    subject_textarea = (By.CSS_SELECTOR, '[test_id="subject"] textarea')
    page_loaded = (By.CSS_SELECTOR, '[class="ticket-list-wrap ticket-list-wrap_fixed-scrollbar"]')
    create_task_todo = (By.XPATH, '//button[@test_id="create-task"]')
    create_request_todo = (By.XPATH, '//button[@test_id="create-request"]')
    create_phone_request_todo = (By.XPATH, '//button[@test_id="create-request-phone"]')
    search = (By.XPATH, '//div[@class="search-panel"]//input')
    first_ticket_in_list = (By.XPATH, '//div[@class="ticket-list-wrap__content ticket-list ps ps--active-x"]/a')
    filter = (By.XPATH, '//div[@class="search-panel__options"]/button[2]')
    filter_tab_all_open = (By.XPATH, '(//div[@class="dropdown-block sidebar-filter"]//div[@class="dropdown-block__control dropdown-block__control_blue"])[2]/*')
    filter_tab_type_open = (By.XPATH, '(//div[@class="dropdown-block sidebar-filter"]//div[@class="dropdown-block__control dropdown-block__control_blue"])[4]/*')
    filter_tab_status_open = (By.XPATH, '(//div[@class="dropdown-block sidebar-filter"]//div[@class="dropdown-block__control dropdown-block__control_blue"])[5]/*')
    filter_tab_create_date_open = (By.XPATH, '(//div[@class="dropdown-block sidebar-filter"]//div[@class="dropdown-block__control dropdown-block__control_blue"])[7]/*')
    filter_tab_begin_date_open = (By.XPATH, '(//div[@class="dropdown-block sidebar-filter"]//div[@class="dropdown-block__control dropdown-block__control_blue"])[8]/*')
    filter_tab_end_date_open = (By.XPATH, '(//div[@class="dropdown-block sidebar-filter"]//div[@class="dropdown-block__control dropdown-block__control_blue"])[9]/*')
    filter_tab_close_date_open = (By.XPATH, '(//div[@class="dropdown-block sidebar-filter"]//div[@class="dropdown-block__control dropdown-block__control_blue"])[10]/*')
    filter_tab_rating_open = (By.XPATH, '(//div[@class="dropdown-block sidebar-filter"]//div[@class="dropdown-block__control dropdown-block__control_blue"])[11]/*')
    filter_tab_initiator_open = (By.XPATH, '(//div[@class="dropdown-block sidebar-filter"]//div[@class="dropdown-block__control dropdown-block__control_blue"])[12]/*')
    filter_tab_contractor_open = (By.XPATH, '(//div[@class="dropdown-block sidebar-filter"]//div[@class="dropdown-block__control dropdown-block__control_blue"])[13]/*')
    filter_tab_responsibility_group_open = (By.XPATH, '(//div[@class="dropdown-block sidebar-filter"]//div[@class="dropdown-block__control dropdown-block__control_blue"])[14]/*')
    filter_tab_approvers_open = (By.XPATH, '(//div[@class="dropdown-block sidebar-filter"]//div[@class="dropdown-block__control dropdown-block__control_blue"])[16]/*')
    filter_reset_all = (By.XPATH, '//div[@class="sidebar-filter-result"]//button[1]')
    filter_mine = (By.XPATH, '//div[@test_id="filters-optAll-mine"]')
    filter_on_subordinates = (By.XPATH, '//div[@test_id="filters-optIAmContractor-delegated"]')
    filter_ticket_type_request = (By.XPATH, '//div[@test_id="filters-ticketTypes-Request"]')
    filter_ticket_type_task = (By.XPATH, '//div[@test_id="filters-ticketTypes-Task"]')
    filter_statuses_active = (By.XPATH, '//div[@test_id="filters-statuses-Active"]')
    filter_statuses_resolved = (By.XPATH, '//div[@test_id="filters-statuses-Resolved"]')
    filter_statuses_canceled = (By.XPATH, '//div[@test_id="filters-statuses-Canceled"]')
    filter_statuses_waiting = (By.XPATH, '//div[@test_id="filters-statuses-Waiting"]')
    filter_statuses_waiting_previous = (By.XPATH, '//div[@test_id="filters-statuses-WaitingPrevious"]')
    filter_statuses_agreement = (By.XPATH, '//div[@test_id="filters-statuses-Agreement"]')
    filter_statuses_rejected = (By.XPATH, '//div[@test_id="filters-statuses-Rejected"]')
    filter_statuses_show_all = (By.XPATH, '//div[@class="link-btn"]')
    filter_statuses_initiator_clarification = (By.XPATH, '//div[@test_id="filters-statuses-InitiatorClarification"]')
    filter_statuses_contractor_clarification = (By.XPATH, '//div[@test_id="filters-statuses-ContractorClarification"]')
    filter_statuses_closed = (By.XPATH, '//div[@test_id="filters-statuses-Closed"]')
    filter_create_date_picker = (By.XPATH, '//div[@test_id="filters-date-created"]')
    filter_tab_service_open = (By.XPATH, '(//div[@class="dropdown-block sidebar-filter"]//div[@class="dropdown-block__control dropdown-block__control_blue"])[6]/*')
    filter_tab_service_search = (By.XPATH, '//div[@test_id="`filters-services`"]//input')
    filter_tab_create_date_begin_date = (By.XPATH, '//div[@class="datepicker-container"]//input[@test_id="custom-input"][1]')
    filter_tab_create_date_end_date = (By.XPATH, '//div[@class="datepicker-container"]//input[@test_id="custom-input"][2]')
    filter_tab_create_date_button_ok = (By.XPATH, '//div[@class="datepicker-container"]//button[@class="button   button_blue button_medium "]')
    filter_tab_begin_date_picker = (By.XPATH, '//div[@test_id="filters-date-begin"]')
    filter_tab_begin_date_begin_date = (By.XPATH, '//div[@class="datepicker-container"]//input[@test_id="custom-input"][1]')
    filter_tab_begin_date_end_date = (By.XPATH, '//div[@class="datepicker-container"]//input[@test_id="custom-input"][2]')
    filter_tab_begin_date_button_ok = (By.XPATH, '//div[@class="datepicker-container"]//button[@class="button   button_blue button_medium "]')
    filter_tab_end_date_picker = (By.XPATH, '//div[@test_id="filters-date-end"]')
    filter_tab_end_date_begin_date = (By.XPATH, '//div[@class="datepicker-container"]//input[@test_id="custom-input"][1]')
    filter_tab_end_date_end_date = (By.XPATH, '//div[@class="datepicker-container"]//input[@test_id="custom-input"][2]')
    filter_tab_end_date_button_ok = (By.XPATH, '//div[@class="datepicker-container"]//button[@class="button   button_blue button_medium "]')
    filter_tab_closed_date_picker = (By.XPATH, '//div[@test_id="filters-date-closing"]')
    filter_tab_closed_date_begin_date = (By.XPATH, '//div[@class="datepicker-container"]//input[@test_id="custom-input"][1]')
    filter_tab_closed_date_end_date = (By.XPATH, '//div[@class="datepicker-container"]//input[@test_id="custom-input"][2]')
    filter_tab_closed_date_button_ok = (By.XPATH, '//div[@class="datepicker-container"]//button[@class="button   button_blue button_medium "]')
    filter_tab_rating_5 = (By.XPATH, '//div[@test_id="filters-rating-5"]')
    filter_tab_rating_4 = (By.XPATH, '//div[@test_id="filters-rating-4"]')
    filter_tab_rating_3 = (By.XPATH, '//div[@test_id="filters-rating-3"]')
    filter_tab_rating_2 = (By.XPATH, '//div[@test_id="filters-rating-2"]')
    filter_tab_rating_1 = (By.XPATH, '//div[@test_id="filters-rating-1"]')
    filter_tab_initiator_search = (By.XPATH, '//div[@test_id="`filters-initiator`"]//input')
    filter_tab_contractor_with_contractor = (By.XPATH, '//div[@test_id="filters-contractorStatus-withContractor"][1]')
    filter_tab_contractor_without_contractor = (By.XPATH, '//div[@test_id="filters-contractorStatus-withContractor"][2]')
    filter_tab_contractor_search = (By.XPATH, '//div[@test_id="filters-contractors"]//input')
    filter_tab_responsibility_group_search = (By.XPATH, '//div[@test_id="`filters-responsibilityGroup`"]//input')
    filter_tab_approvers_search = (By.XPATH, '//div[@test_id="`filters-optMyAgreements-approvers`"]//input')
    filter_close = (By.XPATH, '//div[@class="svg-effect-active svg-effect-active_darkGray svg-effect-active_enabled"]//*')


class TicketsList(AnyPage):

    def page_loaded(self):
        """
        Ждем появления элементов страницы
        """
        self.find_element(Locator.page_loaded)

    @allure.step('Нажимаем на кнопку Создать заявку')
    def button_to_create_request(self):
        self.click_element(Locator.create_request_todo)
        self.manager.web_request_create.page_loaded()
        return self.manager.web_request_create

    @allure.step('Нажимаем на кнопку Создать задачу')
    def button_to_create_task(self):
        self.click_element(Locator.create_task_todo)
        self.manager.web_task_create.page_loaded()
        return self.manager.web_task_create

    @allure.step('Нажимаем на кнопку Создать заявку по телефону')
    def button_to_create_phone_request(self):
        self.click_element(Locator.create_phone_request_todo)
        self.manager.web_request_create.page_loaded()
        return self.manager.web_request_create

    @allure.step('Вводим текст в поиске')
    def input_text_in_search(self, name_text):
        self.page_loaded()
        self.send_keys_slow(Locator.search, name_text, 100)
        return self

    @allure.step('Переходим в тикет с нужным описанием')
    def go_to_ticket_in_list(self, description_text):
        ticket_item_description = (By.XPATH, f'//a[@class="ticket-item ticket-list__item"]//div[contains(@class, "ticket-item__description")][contains(text(),"{description_text}")]')
        self.click_element(ticket_item_description)
        return self  # непонятно в какой класс переходить, т.к. может быть задача или заявка

    @allure.step('Нажимаем на кнопку фильтра')
    def button_to_open_filter(self):
        self.click_element(Locator.filter)
        return self

    @allure.step('Открыть вкладку фильтра')
    def open_filter_tab(self, tab):
        """

        Метод принимает на вход табы, которые следует открыть.
        Табы могут быть представлены в любом виде, например: 'all, type, status' или ['all', 'type', 'status'].

        """

        if 'all' in tab:
            self.click_element(Locator.filter_tab_all_open)
        if 'type' in tab:
            self.click_element(Locator.filter_tab_type_open)
        if 'status' in tab:
            self.click_element(Locator.filter_tab_status_open)
        if 'service' in tab:
            self.click_element(Locator.filter_tab_service_open)
        if 'create_date' in tab:
            self.click_element(Locator.filter_tab_create_date_open)
        if 'begin_date' in tab:
            self.click_element(Locator.filter_tab_begin_date_open)
        if 'end_date' in tab:
            self.click_element(Locator.filter_tab_end_date_open)
        if 'closed_date' in tab:
            self.click_element(Locator.filter_tab_close_date_open)
        if 'rating' in tab:
            self.scroll_to_element(Locator.filter_tab_rating_open)
            self.click_element(Locator.filter_tab_rating_open)
        if 'initiator' in tab:
            self.scroll_to_element(Locator.filter_tab_initiator_open)
            self.click_element(Locator.filter_tab_initiator_open)
        if 'contractor' in tab:
            self.scroll_to_element(Locator.filter_tab_contractor_open)
            self.click_element(Locator.filter_tab_contractor_open)
        if 'responsibility_group' in tab:
            self.scroll_to_element(Locator.filter_tab_responsibility_group_open)
            self.click_element(Locator.filter_tab_responsibility_group_open)
        if 'approvers' in tab:
            self.scroll_to_element(Locator.filter_tab_approvers_open)
            self.click_element(Locator.filter_tab_approvers_open)
        return self

    @allure.step('Нажать на кнопку "Сбросить всё" в фильтре')
    def button_filter_reset_all(self):
        self.click_element(Locator.filter_reset_all)
        return self

    @allure.step('Нажать на кнопку "На мне" на табе "Все" в фильтре')
    def button_filter_mine(self):
        time.sleep(1)
        self.click_element(Locator.filter_mine)
        return self

    @allure.step('Нажать на кнопку "На подчиненных" на табе "Все" в фильтре')
    def button_filter_on_subordinates(self):
        time.sleep(1)
        self.click_element(Locator.filter_on_subordinates)
        return self

    @allure.step('Нажать на кнопку "Заявка" на табе "Тип" в фильтре')
    def button_filter_ticket_type_request(self):
        time.sleep(1)
        self.click_element(Locator.filter_ticket_type_request)
        return self

    @allure.step('Нажать на кнопку "Задача" на табе "Тип" в фильтре')
    def button_filter_ticket_type_task(self):
        time.sleep(1)
        self.click_element(Locator.filter_ticket_type_task)
        return self

    @allure.step('Нажать на кнопку "В работе" на табе "Статус" в фильтре')
    def button_filter_statuses_active(self):
        time.sleep(1)
        self.click_element(Locator.filter_statuses_active)
        return self

    @allure.step('Нажать на кнопку "В проверке" на табе "Статус" в фильтре')
    def button_filter_statuses_resolved(self):
        time.sleep(1)
        self.click_element(Locator.filter_statuses_resolved)
        return self

    @allure.step('Нажать на кнопку "Отменено" на табе "Статус" в фильтре')
    def button_filter_statuses_canceled(self):
        time.sleep(1)
        self.click_element(Locator.filter_statuses_canceled)
        return self

    @allure.step('Нажать на кнопку "В ожидании" на табе "Статус" в фильтре')
    def button_filter_statuses_waiting(self):
        time.sleep(1)
        self.click_element(Locator.filter_statuses_waiting)
        return self

    @allure.step('Нажать на кнопку "В ожидании предшеств." на табе "Статус" в фильтре')
    def button_filter_statuses_waiting_previous(self):
        time.sleep(1)
        self.click_element(Locator.filter_statuses_waiting_previous)
        return self

    @allure.step('Нажать на кнопку "На согласовании" на табе "Статус" в фильтре')
    def button_filter_statuses_agreement(self):
        time.sleep(1)
        self.click_element(Locator.filter_statuses_agreement)
        return self

    @allure.step('Нажать на кнопку "Отклонено" на табе "Статус" в фильтре')
    def button_filter_statuses_rejected(self):
        time.sleep(1)
        self.click_element(Locator.filter_statuses_rejected)
        return self

    @allure.step('Нажать на кнопку "Отклонено" на табе "Статус" в фильтре')
    def button_filter_statuses_rejected(self):
        time.sleep(1)
        self.click_element(Locator.filter_statuses_rejected)
        return self

    @allure.step('Нажать на ссылку "Показать все" на табе "Статус" в фильтре')
    def button_filter_statuses_show_all(self):
        time.sleep(1)
        self.click_element(Locator.filter_statuses_show_all)
        return self

    @allure.step('Нажать на кнопку "На уточнении у иниц." на табе "Статус" в фильтре')
    def button_filter_statuses_initiator_clarification(self):
        time.sleep(1)
        self.click_element(Locator.filter_statuses_initiator_clarification)
        return self

    @allure.step('Нажать на кнопку "На уточнении у исп." на табе "Статус" в фильтре')
    def button_filter_statuses_contractor_clarification(self):
        time.sleep(1)
        self.click_element(Locator.filter_statuses_contractor_clarification)
        return self

    @allure.step('Нажать на кнопку "Закрыта" на табе "Статус" в фильтре')
    def button_filter_statuses_closed(self):
        time.sleep(1)
        self.click_element(Locator.filter_statuses_closed)
        return self

    @allure.step('Выбор услуги в фильтре на табе "Услуга"')
    def select_service_in_filter(self, name_text):
        time.sleep(1)
        self.send_keys_slow(Locator.filter_tab_service_search, name_text, 100)
        time.sleep(2)
        catalogue_item_name = (By.XPATH, f'//div[@test_id="`filters-services`"]//div[contains(text(), "{name_text}")]')
        self.move_to_element(catalogue_item_name)
        self.click_element(catalogue_item_name)
        return self

    @allure.step('Выбор даты создания в фильтре на табе "Дата создания"')
    def select_create_date_in_filter(self, begin_date, end_date):
        time.sleep(1)
        self.click_element(Locator.filter_create_date_picker)
        time.sleep(1)
        self.send_keys_slow(Locator.filter_tab_create_date_begin_date, begin_date, 100)
        self.send_keys_slow(Locator.filter_tab_create_date_end_date, end_date, 100)
        self.click_element(Locator.filter_tab_create_date_button_ok)
        return self

    @allure.step('Выбор даты начала в фильтре на табе "Дата начала"')
    def select_begin_date_in_filter(self, begin_date, end_date):
        time.sleep(1)
        self.click_element(Locator.filter_tab_begin_date_picker)
        time.sleep(1)
        self.send_keys_slow(Locator.filter_tab_begin_date_begin_date, begin_date, 100)
        self.send_keys_slow(Locator.filter_tab_begin_date_end_date, end_date, 100)
        self.click_element(Locator.filter_tab_begin_date_button_ok)
        return self

    @allure.step('Выбор даты окончания в фильтре на табе "Дата окончания"')
    def select_end_date_in_filter(self, begin_date, end_date):
        time.sleep(1)
        self.click_element(Locator.filter_tab_end_date_picker)
        time.sleep(1)
        self.send_keys_slow(Locator.filter_tab_end_date_begin_date, begin_date, 100)
        self.send_keys_slow(Locator.filter_tab_end_date_end_date, end_date, 100)
        self.click_element(Locator.filter_tab_end_date_button_ok)
        return self

    @allure.step('Выбор даты закрытия в фильтре на табе "Дата закрытия"')
    def select_closed_date_in_filter(self, begin_date, end_date):
        time.sleep(1)
        self.click_element(Locator.filter_tab_closed_date_picker)
        time.sleep(1)
        self.send_keys_slow(Locator.filter_tab_closed_date_begin_date, begin_date, 100)
        self.send_keys_slow(Locator.filter_tab_closed_date_end_date, end_date, 100)
        self.click_element(Locator.filter_tab_closed_date_button_ok)
        return self

    @allure.step('Нажать на кнопку с оценкой "5" на табе "Оценка" в фильтре')
    def button_filter_tab_rating_5(self):
        time.sleep(1)
        self.click_element(Locator.filter_tab_rating_5)
        return self

    @allure.step('Нажать на кнопку с оценкой "4" на табе "Оценка" в фильтре')
    def button_filter_tab_rating_4(self):
        time.sleep(1)
        self.click_element(Locator.filter_tab_rating_4)
        return self

    @allure.step('Нажать на кнопку с оценкой "3" на табе "Оценка" в фильтре')
    def button_filter_tab_rating_3(self):
        time.sleep(1)
        self.click_element(Locator.filter_tab_rating_3)
        return self

    @allure.step('Нажать на кнопку с оценкой "2" на табе "Оценка" в фильтре')
    def button_filter_tab_rating_2(self):
        time.sleep(1)
        self.click_element(Locator.filter_tab_rating_2)
        return self

    @allure.step('Нажать на кнопку с оценкой "1" на табе "Оценка" в фильтре')
    def button_filter_tab_rating_1(self):
        time.sleep(1)
        self.click_element(Locator.filter_tab_rating_1)
        return self

    @allure.step('Выбор нужного пользователя на табе "Инициатор" в фильтре')
    def select_user_in_tab_initiator_in_filter(self, name_text):
        time.sleep(1)
        self.send_keys_slow(Locator.filter_tab_initiator_search, name_text, 100)
        time.sleep(2)
        catalogue_item_name = (By.XPATH, f'//div[@test_id="`filters-initiator`"]//div[contains(text(), "{name_text}")]')
        self.move_to_element(catalogue_item_name)
        self.click_element(catalogue_item_name)
        return self

    @allure.step('Нажать на кнопку "С исполнителем" в фильтре на табе "Исполнитель"')
    def button_filter_tab_contractor_with_contractor(self):
        time.sleep(1)
        self.click_element(Locator.filter_tab_contractor_with_contractor)
        return self

    @allure.step('Нажать на кнопку "Без исполнителя" в фильтре на табе "Исполнитель"')
    def button_filter_tab_contractor_without_contractor(self):
        time.sleep(1)
        self.click_element(Locator.filter_tab_contractor_without_contractor)
        return self

    @allure.step('Выбор нужного пользователя на табе "Исполнитель" в фильтре')
    def select_user_in_tab_contractor_in_filter(self, name_text):
        time.sleep(1)
        self.send_keys_slow(Locator.filter_tab_contractor_search, name_text, 100)
        time.sleep(2)
        catalogue_item_name = (By.XPATH, f'//div[@test_id="filters-contractors"]//div[contains(text(), "{name_text}")]')
        self.move_to_element(catalogue_item_name)
        self.click_element(catalogue_item_name)
        return self

    @allure.step('Выбор нужной ГО на табе "Группа ответственности" в фильтре')
    def select_responsibility_group_in_filter(self, name_text):
        time.sleep(1)
        self.send_keys_slow(Locator.filter_tab_responsibility_group_search, name_text, 100)
        time.sleep(2)
        catalogue_item_name = (By.XPATH, f'//div[@test_id="`filters-responsibilityGroup`"]//div[contains(text(), "{name_text}")]')
        self.move_to_element(catalogue_item_name)
        self.click_element(catalogue_item_name)
        return self

    @allure.step('Выбор нужного пользователя на табе "Согласующие" в фильтре')
    def select_user_in_tab_approvers_in_filter(self, name_text):
        time.sleep(1)
        self.send_keys_slow(Locator.filter_tab_approvers_search, name_text, 100)
        time.sleep(2)
        catalogue_item_name = (By.XPATH, f'//div[@test_id="`filters-optMyAgreements-approvers`"]//div[contains(text(), "{name_text}")]')
        self.move_to_element(catalogue_item_name)
        self.click_element(catalogue_item_name)
        return self

    @allure.step('Закрыть окно фильтра')
    def button_filter_close(self):
        time.sleep(1)
        self.scroll_to_element(Locator.filter_close)
        self.click_element(Locator.filter_close)
        return self





