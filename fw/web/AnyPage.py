import time

import allure
from selenium.webdriver.common.by import By

from fw.web.web_base import WebBase


class Locator:
    user_avatar = (By.XPATH, '//a[@test_id="menu-current-user"]')
    profile_exit_btn = (By.XPATH, '//button[@test_id="profile-exit"]')
    profile_exit_submit_btn = (By.XPATH, '//button[@test_id="button-execute"]')
    menu_sidebar_catalogue = (By.XPATH, '//a[@test_id="menu-sidebar-catalogue"]')
    button_others_catalogue = (By.XPATH, '//a[@test_id="menu-sidebar-catalogue_catalogue_others"]')
    master_layout_sidebar_btn_create = (By.XPATH, '//button[@test_id="MASTER_LAYOUT_SIDEBAR_BTN_CREATE"]')
    master_layout_sidebar_menu_create_task = (By.XPATH, '//a[@test_id="MASTER_LAYOUT_SIDEBAR_MENU_CREATE_TASK"]')
    master_layout_sidebar_menu_create_request = (By.XPATH, '//a[@test_id="MASTER_LAYOUT_SIDEBAR_MENU_CREATE_REQUEST"]')
    master_layout_sidebar_menu_create_phone_request = (By.XPATH, '//a[@test_id = "MASTER_LAYOUT_SIDEBAR_MENU_TICKET_phoneRequest"]')
    master_layout_sidebar_menu_create_project = (By.XPATH, '//a[@test_id="MASTER_LAYOUT_SIDEBAR_MENU_CREATE_PROJECT"]')
    master_layout_sidebar_menu_create_access_list = (By.XPATH, '//a[@test_id="MASTER_LAYOUT_SIDEBAR_MENU_ACCESS_LISTS_PROJECT"]')
    menu_sidebar_tickets = (By.XPATH, '//a[@test_id="menu-sidebar-request"]')
    button_menu_task_create = (By.XPATH, '//a[@test_id="buttonmenu-task-create"]')
    button_menu_access_lists_create = (By.XPATH, '//a[@test_id="buttonmenu-access-lists-create"]')
    button_menu_request_create = (By.XPATH, '//a[@test_id="buttonmenu-request-create"]')
    button_menu_project_create = (By.XPATH, '//a[@test_id="buttonmenu-projects-create"]')
    menu_sidebar_project = (By.XPATH, '//a[@test_id="menu-sidebar-projects"]')
    menu_sidebar_messenger = (By.XPATH, '//a[@test_id = "menu-sidebar-messenger"]')
    menu_sidebar_access_lists = (By.XPATH, '//a[@test_id="menu-sidebar-access-lists"]')
    menu_sidebar_knowledge_base = (By.XPATH, '//a[@test_id = "menu-sidebar-knowledgebase"]')
    button_dashboard = (By.XPATH, '//a[@test_id="menu-sidebar-dashboard"]')
    button_activity = (By.XPATH, '//a[@test_id="menu-sidebar-activity"]')
    button_main_menu = (By.XPATH, '//div[@test_id="sandwich-menu"]')
    button_system_settings = (By.XPATH, '//a[@test_id="topmenu-system-settings"]')
    button_rights_and_roles = (By.XPATH, '//a[@test_id="topmenu-permissions-and-roles-users"]')
    button_services = (By.XPATH, '//a[@test_id="topmenu-services"]')
    button_responsibility_groups = (By.XPATH, '//a[@test_id="topmenu-responsibility-groups"]')
    button_templates_for_custom_fields = (By.XPATH, '//a[@test_id="topmenu-templates-additionals-fields"]')
    button_work_schedule = (By.XPATH, '//a[@test_id="topmenu-work-schedule-view"]')
    button_notifications_default = (By.XPATH, '//a[@test_id="topmenu-notifications"]')
    button_digest_default = (By.XPATH, '//a[@test_id="topmenu-notifications-default-digests"]')
    button_mail_notification_settings = (By.XPATH, '//a[@test_id="topmenu-notifications-email-setup"]')
    button_connecting_to_ad = (By.XPATH, '//a[@test_id="topmenu-control-ad-settings"]')
    button_search_users_in_ad = (By.XPATH, '//a[@test_id="topmenu-control-ad-sync"]')
    button_secret_keys = (By.XPATH, '//a[@test_id="topmenu-secret-keys"]')
    button_profile_autorizated_user = (By.XPATH, '//a[@test_id="profile-section"]')
    button_information_autorizated_user = (By.XPATH, '//a[@test_id="profile-information"]')
    button_notifications_autorizated_user = (By.XPATH, '//a[@test_id="profile-notifications"]')
    button_digests_autorizated_user = (By.XPATH, '//a[@test_id="profile-digests"]')
    button_work_schedule_autorizated_user = (By.XPATH, '//a[@test_id="profile-work-schedule"]')
    button_files_autorizated_user = (By.XPATH, '//a[@test_id="profile-files"]')
    button_devices_autorizated_user = (By.XPATH, '//a[@test_id = "profile-devices"]')
    button_settings_autorizated_user = (By.XPATH, '//a[@test_id="profile-settings"]')
    cancel_exit_the_profile = (By.XPATH, '//button[@test_id="button-cancel"]')
    language_system = (By.XPATH, '//div[@test_id="lang-btn"]')
    english_language = (By.XPATH, '//div[@test_id="lang-en"]')
    russian_language = (By.XPATH, '/div[@test_id="lang-ru"]')
    surname_and_name_autorizated_user = (By.XPATH, '//div[@class="menu-top-user__name"]')
    label_switch_moderator_mode = (By.XPATH, '//label[@class="switch"][1]')
    switch_moderator_mode = (By.XPATH, '//div[@id="moderpower__switch"]//div[@class="switch__hand false"]')
    title_on_page = (By.XPATH, '//h1')


class AnyPage(WebBase):

    @allure.step('Смена авторизованного пользователя')
    def change_user(self, user_login, user_password):
        """
        Данный метод не может вернуть экземплар класса
        :param user_login:
        :param user_password:
        :return:
        """
        time.sleep(2)
        current_url = self.get_current_url()
        self.exit_the_profile()
        self.click_exit_submit_btn()
        self.manager.web_login.login_log_pas(user_login, user_password)
        self.goto_page(current_url)
        time.sleep(2)

    @allure.step('Выход из профиля')
    def exit_the_profile(self):
        # Наводим курсор аватар пользователя
        self.move_to_element(Locator.user_avatar)
        # Кнопка выхода из профиля
        self.click_element(Locator.profile_exit_btn)
        return self

    @allure.step('Нажать кнопку подтверждения выхода из профиля')
    def click_exit_submit_btn(self):
        # Кнопка подтверждения выхода из профиля
        self.click_element(Locator.profile_exit_submit_btn)
        return self

    @allure.step('Нажать кнопку Пользовательские справочники')
    def click_others_catalogue_left_menu(self):
        # Наводим курсор на справочники в левом боковом меню
        self.move_to_element(Locator.menu_sidebar_catalogue)
        # Нажимаем на кнопку пользовательских справочников
        self.click_element(Locator.button_others_catalogue)
        self.manager.web_custom_field_dictionary.page_loaded()
        return self.manager.web_custom_field_dictionary

    @allure.step('Нажать кнопку Справочники')
    def click_catalogue_left_menu(self):
        self.click_element(Locator.menu_sidebar_catalogue)
        self.manager.web_catalogue.page_loaded()
        return self.manager.web_catalogue

    @allure.step('Нажать кнопку Тикеты')
    def click_tickets_left_menu(self):
        self.click_element(Locator.menu_sidebar_tickets)
        self.manager.web_tickets_list.page_loaded()
        return self.manager.web_tickets_list

    @allure.step('Нажать кнопку Проекты')
    def click_project_left_menu(self):
        self.click_element(Locator.menu_sidebar_project)
        self.manager.web_project_list.page_loaded()
        return self.manager.web_project_list

    @allure.step('Нажать кнопку Листы допуска')
    def click_access_lists_left_menu(self):
        self.click_element(Locator.menu_sidebar_access_lists)
        self.manager.web_access_lists.page_loaded()
        return self.manager.web_access_lists

    @allure.step('Нажать кнопку Чаты')
    def click_messenger_left_menu(self):
        self.click_element(Locator.menu_sidebar_messenger)
        self.manager.web_messenger.page_loaded()
        return self.manager.web_messenger

    @allure.step('Нажать кнопку База знаний')
    def click_knowledge_base_left_menu(self):
        self.click_element(Locator.menu_sidebar_knowledge_base)
        self.manager.web_messenger.page_loaded()
        return self.manager.web_messenger

    @allure.step('Переход к созданию листа допуска через кнопку листов допусков на главной странице')
    def click_btn_create_access_list_left_menu(self):
        # Наводим курсор на кнопку листов допусков на главной странице
        self.move_to_element(Locator.menu_sidebar_access_lists)
        # Нажимаем кнопку Создать
        self.click_element(Locator.master_layout_sidebar_menu_create_access_list)
        self.manager.web_access_list_create.page_loaded()
        return self.manager.web_access_list_create

    @allure.step('Переход к созданию задачи через "+" на главной странице')
    def click_btn_create_task_plus_menu(self):
        # Наводим курсор на кнопку "+" на главной странице
        self.move_to_element(Locator.master_layout_sidebar_btn_create)
        # Нажимаем кнопку Задачу
        self.click_element(Locator.button_menu_task_create)
        self.manager.web_task_create.page_loaded()
        return self.manager.web_task_create

    @allure.step('Переход к созданию задачи через кнопку тикетов на главной странице')
    def click_btn_create_task_left_menu(self):
        # Наводим курсор на кнопку тикетов на главной странице
        self.move_to_element(Locator.menu_sidebar_tickets)
        # Нажимаем кнопку Создать задачу
        self.click_element(Locator.master_layout_sidebar_menu_create_task)
        self.manager.web_task_create.page_loaded()
        return self.manager.web_task_create

    @allure.step('Переход к созданию заявки через "+" на главной странице')
    def click_btn_create_request_plus_menu(self):
        # Наводим курсор на кнопку "+" на главной странице
        self.move_to_element(Locator.master_layout_sidebar_btn_create)
        # Нажимаем кнопку Заявку
        self.click_element(Locator.button_menu_request_create)
        self.manager.web_request_create.page_loaded()
        return self.manager.web_request_create

    @allure.step('Переход к созданию заявки через кнопку тикетов на главной странице')
    def click_btn_create_request_left_menu(self):
        # Наводим курсор на кнопку тикетов на главной странице
        self.move_to_element(Locator.menu_sidebar_tickets)
        # Нажимаем кнопку Создать заявку
        self.click_element(Locator.master_layout_sidebar_menu_create_request)
        self.manager.web_request_create.page_loaded()
        return self.manager.web_request_create

    @allure.step('Переход к созданию заявки по телефону через кнопку тикетов на главной странице')
    def click_btn_create_phone_request_left_menu(self):
        # Наводим курсор на кнопку тикетов на главной странице
        self.move_to_element(Locator.menu_sidebar_tickets)
        # Нажимаем кнопку Создать заявку по телефону
        self.click_element(Locator.master_layout_sidebar_menu_create_phone_request)
        self.manager.web_request_create.page_loaded()
        return self.manager.web_request_create

    @allure.step('Переход к созданию проекта через "+" на главной странице')
    def click_btn_create_project_plus_menu(self):
        # Наводим курсор на кнопку "+" на главной странице
        self.move_to_element(Locator.master_layout_sidebar_btn_create)
        # Нажимаем кнопку Проект
        self.click_element(Locator.button_menu_project_create)
        self.manager.web_project_create.page_loaded()
        return self.manager.web_project_create

    @allure.step('Переход к созданию листа допуска через "+" на главной странице')
    def click_btn_create_access_lists_plus_menu(self):
        # Наводим курсор на кнопку "+" на главной странице
        self.move_to_element(Locator.master_layout_sidebar_btn_create)
        # Нажимаем кнопку Проект
        self.click_element(Locator.button_menu_access_lists_create)
        self.manager.web_access_list_create.page_loaded()
        return self.manager.web_access_list_create

    @allure.step('Переход к созданию проекта через кнопку проектов на главной странице')
    def click_btn_create_project_left_menu(self):
        # Наводим курсор на кнопку проектов на главной странице
        self.move_to_element(Locator.menu_sidebar_project)
        # Нажимаем кнопку Создать
        self.click_element(Locator.master_layout_sidebar_menu_create_project)
        self.manager.web_project_create.page_loaded()
        return self.manager.web_project_create

    @allure.step('Переход на страницу дашбордов')
    def click_dashboard(self):
        self.click_element(Locator.button_dashboard)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Переход в ленту активности')
    def click_activity(self):
        self.click_element(Locator.button_activity)
        self.manager.web_activity.page_loaded()
        return self.manager.web_activity

    @allure.step('Наводим курсор на главное меню')
    def move_to_main_menu(self):
        self.move_to_element(Locator.button_main_menu)
        return self

    @allure.step('Открыть системные настройки')
    def click_system_settings(self):
        self.move_to_main_menu()
        self.click_element(Locator.button_system_settings)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть права и роли')
    def click_rights_and_roles(self):
        self.move_to_main_menu()
        self.click_element(Locator.button_rights_and_roles)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть услуги')
    def click_services(self):
        self.move_to_main_menu()
        self.click_element(Locator.button_services)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть группы ответственности')
    def click_responsibility_groups(self):
        self.move_to_main_menu()
        self.click_element(Locator.button_responsibility_groups)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть шаблоны доп. полей')
    def click_templates_for_custom_fields(self):
        self.move_to_main_menu()
        self.click_element(Locator.button_templates_for_custom_fields)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть график работы')
    def click_work_schedule(self):
        self.move_to_main_menu()
        self.click_element(Locator.button_work_schedule)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть уведомления по умолчанию')
    def click_notifications_default(self):
        self.move_to_main_menu()
        self.click_element(Locator.button_notifications_default)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть дайджест по умолчанию')
    def click_digest_default(self):
        self.move_to_main_menu()
        self.click_element(Locator.button_digest_default)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть настройки почтовых уведомлений')
    def click_mail_notification_settings(self):
        self.move_to_main_menu()
        self.click_element(Locator.button_mail_notification_settings)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть подключение к AD')
    def click_connecting_to_ad(self):
        self.move_to_main_menu()
        self.click_element(Locator.button_connecting_to_ad)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть поиск пользователей по AD')
    def click_search_users_in_ad(self):
        self.move_to_main_menu()
        self.click_element(Locator.button_search_users_in_ad)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть секретные ключи')
    def click_secret_keys(self):
        self.move_to_main_menu()
        self.click_element(Locator.button_secret_keys)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Наводим курсор на аватар пользователя')
    def move_to_user_avatar(self):
        self.move_to_element(Locator.user_avatar)
        return self

    @allure.step('Открыть профиль авторизованного пользователя')
    def click_profile_autorizated_user(self):
        self.move_to_user_avatar()
        self.click_element(Locator.button_profile_autorizated_user)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть информацию о авторизованном пользователе')
    def click_information_autorizated_user(self):
        self.move_to_user_avatar()
        self.click_element(Locator.button_information_autorizated_user)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть уведомления авторизованного пользователя')
    def click_notifications_autorizated_user(self):
        self.move_to_user_avatar()
        self.click_element(Locator.button_notifications_autorizated_user)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть дайджесты авторизованного пользователя')
    def click_digests_autorizated_user(self):
        self.move_to_user_avatar()
        self.click_element(Locator.button_digests_autorizated_user)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть график работы авторизованного пользователя')
    def click_work_schedule_autorizated_user(self):
        self.move_to_user_avatar()
        self.click_element(Locator.button_work_schedule_autorizated_user)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть файлы авторизованного пользователя')
    def click_files_autorizated_user(self):
        self.move_to_user_avatar()
        self.click_element(Locator.button_files_autorizated_user)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть устройства авторизованного пользователя')
    def click_devices_autorizated_user(self):
        self.move_to_user_avatar()
        self.click_element(Locator.button_devices_autorizated_user)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Открыть настройки авторизованного пользователя')
    def click_settings_autorizated_user(self):
        self.move_to_user_avatar()
        self.click_element(Locator.button_settings_autorizated_user)
        return self
        # TODO добавить переход в нужный класс

    @allure.step('Отмена выхода из профиля')
    def click_cancel_exit_the_profile(self):
        self.click_element(Locator.cancel_exit_the_profile)
        return self

    @allure.step('Наводим курсор язык системы')
    def move_to_language_system(self):
        self.move_to_element(Locator.language_system)
        return self

    @allure.step('Выбор Английского языка')
    def select_english_language(self):
        self.move_to_language_system()
        self.click_element(Locator.english_language)
        return self

    @allure.step('Выбор Русского языка')
    def select_russian_language(self):
        self.move_to_language_system()
        self.click_element(Locator.russian_language)
        return self

    @allure.step('Получаем фамилию и имя авторизованного пользователя')
    def get_surname_and_name_autorizated_user(self):
        surname_and_name = self.get_tag_text(Locator.surname_and_name_autorizated_user)
        return surname_and_name

    @allure.step('Проверяем авторизованного пользователя, и заходим под другим пользователем, если они не совпадают')
    def check_autorizated_user_and_loging_other_user_if_need(self, user):
        # Получаем ФИ пользователя
        correct_surname_and_name = user['Surname'] + ' ' + user['Name']
        # Получаем ФИ авторизованного пользователя
        actual_surname_and_name = self.get_surname_and_name_autorizated_user()
        # Проверяем, равен ли авторизованный пользователь нужному
        if actual_surname_and_name != correct_surname_and_name:
            # Если нет - авторизуемся под нужным пользователем
            self.change_user(user['Login'], user['Password'])
        else:
            self.refresh_the_page()

    @allure.step('Получаем текст заголовка страницы')
    def get_text_title_on_page(self):
        text_title = self.get_tag_text(Locator.title_on_page)
        return text_title
