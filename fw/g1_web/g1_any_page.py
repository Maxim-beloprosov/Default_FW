import time

import allure
from selenium.webdriver.common.by import By

from fw.g1_web.g1_web_base import G1WebBase


class Locator:
    button_plus_request = (By.XPATH, '//li[contains(@class, "Request plus")]')
    surname_and_name_autorizated_user = (By.XPATH, '//div[@class="h-user"]/a')
    button_change_user = (By.XPATH, '//div[@class="ga_impesonate_btn"]')
    block_select_for_change_user = (By.XPATH, '//div[@class="ga_impesonate"]//a[@class="chosen-single chosen-default"]')
    input_text_for_change_user = (By.XPATH, '//div[@class="ga_impesonate"]//div[@class="chosen-search"]/input')
    waiting_list_user_for_change_user = (By.XPATH, '//ul[@class="chosen-results"]/li[contains(@class, "active-result")]')
    button_apply_change_user = (By.XPATH, '//button[@class="ga_bttn bttn_blue ga_submit"]')
    button_requests = (By.XPATH, '//li[@class="item-nav Request active"]/span')
    tab_my_in_requests = (By.XPATH, '//a[@href="/RequestList/My"]')
    result_modal_window_for_change_user = (By.XPATH, '//ul[@class="chosen-results"]//li')
    loading_page = (By.XPATH, '//div[@class="spinner"]')


class G1AnyPage(G1WebBase):
    @allure.step('Ожидаем, когда загрузится страница')
    def g1_page_loaded(self):
        time.sleep(1)
        self.find_element(Locator.loading_page)

    @allure.step('Ожидаем, когда кнопка будет активна')
    def g1_waiting_when_button_is_active(self, locator):
        check = self.get_tag_attribute(locator, 'disabled')
        for i in range(1, 11):
            if check == 'true':
                time.sleep(1)
                check = self.get_tag_attribute(locator, 'disabled')
            else:
                return self

    @allure.step('Ожидаем, когда кнопка будет не активна')
    def g1_waiting_when_button_is_not_active(self, locator):
        check = self.get_tag_attribute(locator, 'disabled')
        for i in range(1, 11):
            if check == None:
                time.sleep(1)
                check = self.get_tag_attribute(locator, 'disabled')
            else:
                return self

    @allure.step('Нажать кнопку "+" (Создать заявку)')
    def g1_click_button_plus_request(self):
        self.g1_page_loaded()
        self.click_element(Locator.button_plus_request)
        return self.manager.g1_web_request_new

    @allure.step('Получаем фамилию и имя авторизованного пользователя')
    def g1_get_surname_and_name_autorizated_user(self):
        surname_and_name = self.get_tag_text(Locator.surname_and_name_autorizated_user)
        return surname_and_name

    @allure.step('Нажать кнопку Сменить пользователя')
    def g1_click_button_change_user(self):
        self.click_element(Locator.button_change_user)
        return self

    @allure.step('Выбираем пользователя для смены пользователя')
    def g1_change_user(self, user):
        # Нажимаем на кнопку Сменить пользователя
        self.g1_click_button_change_user()
        # Нажимаем на блок ввода текста для смены пользователя
        self.click_element(Locator.block_select_for_change_user)
        # Выбираем пользователя
        self.g1_search_and_select_need_user(user)
        # Нажимаем кнопку Изменить (Подтверждаем изменение пользователя)
        self.click_element(Locator.button_apply_change_user)
        return self

    @allure.step('Проверяем авторизованного пользователя, и заходим под другим пользователем, если они не совпадают')
    def g1_check_autorizated_user_and_loging_other_user_if_need(self, user):
        # Получаем фамилию и имя авторизованного пользователя
        actual_user = self.g1_get_surname_and_name_autorizated_user()
        # Проверяем, отличается ли авторизованный пользователь, от того, кем нужно авторизоваться
        if user != actual_user:
            # Если пользователя не совпадают, меняем пользователя
            self.g1_change_user(user)

    @allure.step('Нажать кнопку заявки')
    def g1_click_button_requests(self):
        self.click_element(Locator.button_requests)
        return self

    @allure.step('Нажать таб МОИ в заявках')
    def g1_click_button_tab_my_in_requests(self):
        self.g1_click_button_need_type_ticket_if_need('Request')
        self.click_element(Locator.tab_my_in_requests)
        return self

    @allure.step('Проверка какой тип тикета выбран')
    def g1_check_which_type_ticket_active(self, type_ticket):
        path_type_ticket = (By.XPATH, f'//li[contains(@class,"item-nav {type_ticket}")]')
        tag_elements = self.get_tag_attribute(path_type_ticket, 'class')
        if 'active' in tag_elements:
            return True
        else:
            return False

    @allure.step('Нажимаем на нужный тип тикета при необходимости')
    def g1_click_button_need_type_ticket_if_need(self, type_ticket):
        check_active_button_need_type_ticket = self.g1_check_which_type_ticket_active(type_ticket)
        if check_active_button_need_type_ticket == False:
            button_type_tickets = (By.XPATH, f'//li[@class="item-nav {type_ticket}"]')
            self.click_element(button_type_tickets)
        return self

    @allure.step('Формируем ФИ (фамилию и имя) из данных пользователя')
    def g1_shaping_surname_and_name(self, user):
        name_user = self.manager.group_data.g1_Status_ticket.g1_users[user]['SureName'] + self.manager.group_data.g1_Status_ticket.g1_users[user]['Name']
        return name_user

    @allure.step('Поиск и выбор нужного пользователя для смены пользователя')
    def g1_search_and_select_need_user(self, user):
        # Вводим фамилию и имя в поле ввода для текста
        self.send_keys(Locator.input_text_for_change_user, user)
        self.g1_select_need_user(user)
        return self

    @allure.step('Выбор нужного пользователя')
    def g1_select_need_user(self, user):
        # Ожидаем, пока появятся результаты поиска
        self.find_element(Locator.waiting_list_user_for_change_user)
        users = self.find_elements(Locator.result_modal_window_for_change_user)
        for i in range(1, len(users) + 1):
            need_user = (By.XPATH, f'//ul[@class="chosen-results"]//li[{i}]')
            name_user = self.get_tag_text(need_user)
            if name_user[0:len(user)] == user:
                self.move_to_element(need_user)
                self.click_element(need_user)
                return self