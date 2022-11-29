import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Request')
@allure.story('Создание заявки')
class TestCreateRequest(WebBase):

    @allure.title('Создание заявки с выбором услуги из дерева')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_request_first(self):
        # Переходим к созданию заявки
        self.APP.web_any_page.click_btn_create_request_plus_menu()
        # Выбираем услугу
        self.APP.web_request_create.select_services_in_tree(self.APP.group_data.service_template['AutomationService Тестовый Тип 1']['name'])
        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_tickets_base.fill_description_in_ticket(correct_description)
        # Создаем заявку
        self.APP.web_request_create.button_to_create_request()
        # Переходим в список тикетов
        self.APP.web_any_page.click_tickets_left_menu()
        # Вводим в поиск описание созданной заявки
        self.APP.web_tickets_list.input_text_in_search(correct_description)
        # Переходим в тикет с нужным описанием
        self.APP.web_tickets_list.go_to_ticket_in_list(correct_description)
        # Сравниваем два описания между собой
        actual_description = self.APP.web_tickets_base.get_description_in_ticket()
        assert correct_description == actual_description

    @allure.title('Создание заявки с выбором услуги в поиске на странице')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_request_second(self):
        # Переходим к созданию заявки
        self.APP.web_any_page.click_btn_create_request_plus_menu()
        # Выбираем услугу
        self.APP.web_request_create.select_services_in_search_string(self.APP.group_data.service_template['AutomationService Тестовый Тип 1']['name'])
        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_tickets_base.fill_description_in_ticket(correct_description)
        # Создаем заявку
        self.APP.web_request_create.button_to_create_request()
        # Переходим в список тикетов
        self.APP.web_any_page.click_tickets_left_menu()
        # Вводим в поиск описание созданной заявки
        self.APP.web_tickets_list.input_text_in_search(correct_description)
        # Переходим в тикет с нужным описанием
        self.APP.web_tickets_list.go_to_ticket_in_list(correct_description)
        # Сравниваем два описания между собой
        actual_description = self.APP.web_tickets_base.get_description_in_ticket()
        assert correct_description == actual_description

    @allure.title('Создание заявки с обозревателем')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_request_with_observer_4(self):
        # Переходим к созданию заявки
        self.APP.web_any_page.click_btn_create_request_plus_menu()
        # Выбираем услугу
        self.APP.web_request_create.select_services_in_search_string(self.APP.group_data.service_template['AutomationService Тестовый Тип 1']['name'])
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Добавляем обозревателя
        correct_observer = self.APP.group_data.users['test_user05']['Surname'] + ' ' + self.APP.group_data.users['test_user05']['Name']
        self.APP.web_tickets_base.add_observer(correct_observer)
        # Создаем заявку
        self.APP.web_request_create.button_to_create_request()
        # Получаем информацию о всех обозревателях
        list_observers = self.APP.web_tickets_base.get_observers_in_ticket()
        # Проверяем добавленного обозревателя
        assert len(list_observers) == 1
        assert correct_observer in list_observers


    @allure.title('Создание заявки c согласующим')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_request_with_approver(self):
        # Переходим к созданию заявки
        self.APP.web_any_page.click_btn_create_request_plus_menu()
        # Выбираем услугу
        self.APP.web_request_create.select_services_in_search_string(self.APP.group_data.service_template['AutomationService Тестовый Тип 1']['name'])
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Добавляем согласующего
        correct_approver = self.APP.group_data.users['test_user05']['Surname'] + ' ' + self.APP.group_data.users['test_user05']['Name']
        self.APP.web_tickets_base.add_approver(correct_approver)
        # Создаем заявку
        self.APP.web_request_create.button_to_create_request()
        # Получаем информацию о всех согласующих
        list_approvers = self.APP.web_tickets_base.get_approvers_in_ticket()
        # Проверяем добавленного согласующего
        assert len(list_approvers) == 1
        assert correct_approver in list_approvers

    @allure.title('Создание заявки со вложением через боковое меню')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_request_with_attachment_first(self):
        # Переходим к созданию заявки
        self.APP.web_any_page.click_btn_create_request_plus_menu()
        # Выбираем услугу
        self.APP.web_request_create.select_services_in_search_string(self.APP.group_data.service_template['AutomationService Тестовый Тип 1']['name'])
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Добавляем вложение
        correct_attachment = 'Тестовое фото №1'
        self.APP.web_tickets_base.add_attachment_in_ticket(correct_attachment)
        # Создаем заявку
        self.APP.web_request_create.button_to_create_request()
        # Получаем информацию о всех вложениях
        list_attachments = self.APP.web_tickets_base.get_attachments_in_ticket()
        # Проверяем добавленное вложение
        assert len(list_attachments) == 1
        assert correct_attachment in list_attachments

    @allure.title('Создание заявки со вложением в описании')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_request_with_attachment_second(self):
        # Переходим к созданию заявки
        self.APP.web_any_page.click_btn_create_request_plus_menu()
        # Выбираем услугу
        self.APP.web_request_create.select_services_in_search_string(self.APP.group_data.service_template['AutomationService Тестовый Тип 1']['name'])
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Добавляем вложение
        correct_attachment = 'Тестовое фото №2'
        self.APP.web_tickets_base.add_attachment_in_description(correct_attachment)
        # Создаем заявку
        self.APP.web_request_create.button_to_create_request()
        # Получаем информацию о всех вложениях
        list_attachments = self.APP.web_tickets_base.get_attachments_in_ticket()
        # Проверяем добавленное вложение
        assert len(list_attachments) == 1
        assert correct_attachment in list_attachments

    @allure.title('Создание заявки с датой начала')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_request_with_date_start(self):
        # Переходим к созданию заявки
        self.APP.web_any_page.click_btn_create_request_plus_menu()
        # Выбираем услугу
        self.APP.web_request_create.select_services_in_search_string(self.APP.group_data.service_template['AutomationService Тестовый Тип 1']['name'])
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Изменяем дату создания
        correct_date_start = self.APP.web_request_create.edit_start_date_in_request_when_create(self.APP.time.date_increased_x_days(7), '11')
        # Создаем заявку
        self.APP.web_request_create.button_to_create_request()
        # Получаем актуальную дату начала
        actual_date_start = self.APP.web_tickets_base.get_date_start_ticket()
        # Сравниваем между собой 2 даты начала
        assert correct_date_start == actual_date_start

    @allure.title('Создание заявки по телефону с выбором услуги из дерева')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_phone_request_first(self):
        # Авторизуемся участником ГО
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user03'])
        # Переходим к созданию заявки по телефону
        self.APP.web_any_page.click_btn_create_phone_request_left_menu()
        # Выбираем услугу
        self.APP.web_request_create.select_services_in_tree(self.APP.group_data.service_template['AutomationService Тестовый Тип 12 Заявка по телефону']['name'])
        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_tickets_base.fill_description_in_ticket(correct_description)
        # Создаем заявку
        self.APP.web_request_create.button_to_create_request()
        correct_status = self.APP.group_data.Status_ticket['request_and_task']['RUS']['В проверке']
        # Переходим в список тикетов
        self.APP.web_any_page.click_tickets_left_menu()
        # Вводим в поиск описание созданной заявки
        self.APP.web_tickets_list.input_text_in_search(correct_description)
        # Переходим в тикет с нужным описанием
        self.APP.web_tickets_list.go_to_ticket_in_list(correct_description)
        # Получаем описание тикета
        actual_description = self.APP.web_tickets_base.get_description_in_ticket()
        # Получаем статус тикета
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем два описания между собой
        assert correct_description == actual_description
        # Сравниваем статусы между собой
        assert correct_status == actual_status

    @allure.title('Создание заявки по телефону с выбором услуги в поиске на странице')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_phone_request_second(self):
        # Авторизуемся участником ГО
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user03'])
        # Переходим к созданию заявки по телефону
        self.APP.web_any_page.click_btn_create_phone_request_left_menu()
        # Выбираем услугу
        self.APP.web_request_create.select_services_in_search_string(
            self.APP.group_data.service_template['AutomationService Тестовый Тип 12 Заявка по телефону']['name'])
        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_tickets_base.fill_description_in_ticket(correct_description)
        # Создаем заявку
        self.APP.web_request_create.button_to_create_request()
        correct_status = self.APP.group_data.Status_ticket['request_and_task']['RUS']['В проверке']
        # Переходим в список тикетов
        self.APP.web_any_page.click_tickets_left_menu()
        # Вводим в поиск описание созданной заявки
        self.APP.web_tickets_list.input_text_in_search(correct_description)
        # Переходим в тикет с нужным описанием
        self.APP.web_tickets_list.go_to_ticket_in_list(correct_description)
        # Получаем описание тикета
        actual_description = self.APP.web_tickets_base.get_description_in_ticket()
        # Получаем статус тикета
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем два описания между собой
        assert correct_description == actual_description
        # Сравниваем статусы между собой
        assert correct_status == actual_status

    @allure.title('Проверка на обязательность выбора услуги')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_check_mandatory_select_service(self):
        # Переходим к созданию заявки
        self.APP.web_any_page.click_btn_create_request_plus_menu()
        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_tickets_base.fill_description_in_ticket(correct_description)
        # Проверяем, активна ли кнопка создания тикета
        check_button = self.APP.web_tickets_base.check_active_or_not_active_button_create_ticket()
        # Ожидаем, что кнопка не активна
        assert check_button == False

    @allure.title('Проверка на обязательность заполнение доп полей')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.skip(reason='Кнопка создания тикетов активна, когда не заполнены обяз. доп. поля')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/20208')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_check_mandatory_fill_additional_fields(self):
        # Переходим к созданию заявки
        self.APP.web_any_page.click_btn_create_request_plus_menu()
        # Выбираем услугу
        self.APP.web_request_create.select_services_in_search_string(
            self.APP.group_data.service_template['AutomationService Тестовый Тип 12 Заявка по телефону']['name'])
        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_tickets_base.fill_description_in_ticket(correct_description)
        # Проверяем, активна ли кнопка создания тикета
        check_button = self.APP.web_tickets_base.check_active_or_not_active_button_create_ticket()
        # Ожидаем, что кнопка не активна
        assert check_button == False
