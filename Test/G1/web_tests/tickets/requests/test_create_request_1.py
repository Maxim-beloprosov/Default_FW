from Test.G1.web_tests.g1_web_base import G1WebBase
import allure
import pytest

@allure.epic('G1')
@allure.feature('Web - Request')
@allure.story('Создание заявок')
class TestCreateRequest(G1WebBase):

    '''
    Осталось перенести 2 теста из файла
    4.Создание заявки(дополнительные поля, заполнение)
    5.Создание заявки(дополнительные поля, заполнение)
    '''

    @allure.title('Создание заявки с выбором всех сущностей норматива')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_create_request_first(self):
        # Задаем данные для выбора норматива
        job_type = 'Тестовый_Тип_1'
        department = self.APP.group_data.service_template_g1[job_type]['department']
        category = self.APP.group_data.service_template_g1[job_type]['category']
        request_type = self.APP.group_data.service_template_g1[job_type]['type']
        # Переходим к созданию заявки
        self.APP.g1_web_any_page.g1_click_button_plus_request()
        # Заполняем норматив (Отдел, категория, тип и вид)
        self.APP.g1_web_request_new.g1_set_department(department)
        self.APP.g1_web_request_new.g1_set_category(category)
        self.APP.g1_web_request_new.g1_set_request_type(request_type)
        self.APP.g1_web_request_new.g1_set_job_type(job_type)
        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.g1_web_ticket_base.g1_fill_description(correct_description)
        # Нажимаем кнопку Сохранить для создания заявки
        self.APP.g1_web_ticket_base.g1_click_button_create_or_save()
        # Переходим в заявке, в таб МОИ
        self.APP.g1_web_any_page.g1_click_button_tab_my_in_requests()
        # Переходим в тикет с нужным описанием
        self.APP.g1_web_ticket_base.g1_go_to_ticket_in_list_with_need_description(correct_description)
        # Получаем описание тикета
        actual_description = self.APP.g1_web_ticket_base.g1_get_description()
        # Сравниваем два описания между собой
        assert correct_description == actual_description
        assert department == self.APP.g1_web_request_edit.g1_get_department()
        assert category == self.APP.g1_web_request_edit.g1_get_category()
        assert request_type == self.APP.g1_web_request_edit.g1_get_request_type()
        assert job_type == self.APP.g1_web_request_edit.g1_get_job_type()


    @allure.title('Создание заявки с выбором норматива через глобальный поиск')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_create_request_second(self):
        # Задаем данные для выбора норматива
        job_type = 'Тестовый_Тип_1'
        department = self.APP.group_data.service_template_g1[job_type]['department']
        category = self.APP.group_data.service_template_g1[job_type]['category']
        request_type = self.APP.group_data.service_template_g1[job_type]['type']
        # Переходим к созданию заявки
        self.APP.g1_web_any_page.g1_click_button_plus_request()
        # Заполняем норматив через глобальный поиск
        path_normative = department + ' → ' + category + ' → ' + request_type + ' → ' + job_type
        self.APP.g1_web_request_new.g1_select_need_normative_in_global_search(path_normative)
        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.g1_web_ticket_base.g1_fill_description(correct_description)
        # Нажимаем кнопку Сохранить для создания заявки
        self.APP.g1_web_ticket_base.g1_click_button_create_or_save()
        # Переходим в заявке, в таб МОИ
        self.APP.g1_web_any_page.g1_click_button_tab_my_in_requests()
        # Переходим в тикет с нужным описанием
        self.APP.g1_web_ticket_base.g1_go_to_ticket_in_list_with_need_description(correct_description)
        # Получаем описание тикета
        actual_description = self.APP.g1_web_ticket_base.g1_get_description()
        # Сравниваем два описания между собой
        assert correct_description == actual_description
        # Сравниваем актуальный норматив с ранее заданным
        assert department == self.APP.g1_web_request_edit.g1_get_department()
        assert category == self.APP.g1_web_request_edit.g1_get_category()
        assert request_type == self.APP.g1_web_request_edit.g1_get_request_type()
        assert job_type == self.APP.g1_web_request_edit.g1_get_job_type()

    @allure.title('Создание заявки с обозревателем')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_create_request_with_observer_2(self):
        # Задаем данные для выбора норматива
        job_type = 'Тестовый_Тип_1'
        department = self.APP.group_data.service_template_g1[job_type]['department']
        category = self.APP.group_data.service_template_g1[job_type]['category']
        request_type = self.APP.group_data.service_template_g1[job_type]['type']
        # Переходим к созданию заявки
        self.APP.g1_web_any_page.g1_click_button_plus_request()
        # Заполняем норматив через глобальный поиск
        self.APP.g1_web_any_page.g1_click_button_plus_request()
        path_normative = department + ' → ' + category + ' → ' + request_type + ' → ' + job_type
        self.APP.g1_web_request_new.g1_select_need_normative_in_global_search(path_normative)
        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.g1_web_ticket_base.g1_fill_description(correct_description)
        # Добавляем обозревателя
        correct_observer = 'user5 test'
        self.APP.g1_web_ticket_base.g1_add_observer(correct_observer)
        # Нажимаем кнопку Сохранить для создания заявки
        self.APP.g1_web_ticket_base.g1_click_button_create_or_save()
        # Переходим в заявке, в таб МОИ
        self.APP.g1_web_any_page.g1_click_button_tab_my_in_requests()
        # Переходим в тикет с нужным описанием
        self.APP.g1_web_ticket_base.g1_go_to_ticket_in_list_with_need_description(correct_description)
        # Получаем описание тикета
        actual_description = self.APP.g1_web_ticket_base.g1_get_description()
        # Получаем обозревателя заявки
        actual_observers = self.APP.g1_web_ticket_base.g1_get_observers_in_ticket()
        # Сравниваем два описания между собой
        assert correct_description == actual_description
        # Сравниваем актуальный норматив с ранее заданным
        assert department == self.APP.g1_web_request_edit.g1_get_department()
        assert category == self.APP.g1_web_request_edit.g1_get_category()
        assert request_type == self.APP.g1_web_request_edit.g1_get_request_type()
        assert job_type == self.APP.g1_web_request_edit.g1_get_job_type()
        # Проверяем количество обозреваталей
        assert len(actual_observers) == 1
        # Проверяем конкретного обозревателя
        assert correct_observer in actual_observers

    @allure.title('Создание заявки с согласующим')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_create_request_with_approver(self):
        # Задаем данные для выбора норматива
        job_type = 'Тестовый_Тип_1'
        department = self.APP.group_data.service_template_g1[job_type]['department']
        category = self.APP.group_data.service_template_g1[job_type]['category']
        request_type = self.APP.group_data.service_template_g1[job_type]['type']
        # Переходим к созданию заявки
        self.APP.g1_web_any_page.g1_click_button_plus_request()
        # Заполняем норматив через глобальный поиск
        path_normative = department + ' → ' + category + ' → ' + request_type + ' → ' + job_type
        self.APP.g1_web_request_new.g1_select_need_normative_in_global_search(path_normative)
        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.g1_web_ticket_base.g1_fill_description(correct_description)
        # Добавляем согласующего
        correct_approver = 'user5 test'
        self.APP.g1_web_ticket_base.g1_add_approver(correct_approver)
        # Нажимаем кнопку Сохранить для создания заявки
        self.APP.g1_web_ticket_base.g1_click_button_create_or_save()
        # Переходим в заявке, в таб МОИ
        self.APP.g1_web_any_page.g1_click_button_tab_my_in_requests()
        # Переходим в тикет с нужным описанием
        self.APP.g1_web_ticket_base.g1_go_to_ticket_in_list_with_need_description(correct_description)
        # Получаем описание тикета
        actual_description = self.APP.g1_web_ticket_base.g1_get_description()
        # Получаем согласующего заявки
        actual_approvers = self.APP.g1_web_ticket_base.g1_get_approvers_in_ticket()
        # Сравниваем два описания между собой
        assert correct_description == actual_description
        # Сравниваем актуальный норматив с ранее заданным
        assert department == self.APP.g1_web_request_edit.g1_get_department()
        assert category == self.APP.g1_web_request_edit.g1_get_category()
        assert request_type == self.APP.g1_web_request_edit.g1_get_request_type()
        assert job_type == self.APP.g1_web_request_edit.g1_get_job_type()
        # Проверяем количество согласующих
        assert len(actual_approvers) == 1
        # Проверяем конкретного согласующего
        assert correct_approver in actual_approvers

    @allure.title('Создание заявки с обяз. согласующим и обозревателем')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_create_request_with_mandatory_approver_and_observer(self):
        # Задаем данные для выбора норматива
        job_type = 'Тип для тестирования(2)'
        department = self.APP.group_data.service_template_g1[job_type]['department']
        category = self.APP.group_data.service_template_g1[job_type]['category']
        request_type = self.APP.group_data.service_template_g1[job_type]['type']
        correct_approver = 'Boss1 test'  # Пока нет информации о нормативах в group data
        correct_observer = 'Boss2 test'  # Пока нет информации о нормативах в group data
        # Переходим к созданию заявки
        self.APP.g1_web_any_page.g1_click_button_plus_request()
        # Заполняем норматив через глобальный поиск
        path_normative = department + ' → ' + category + ' → ' + request_type + ' → ' + job_type
        self.APP.g1_web_request_new.g1_select_need_normative_in_global_search(path_normative)
        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.g1_web_ticket_base.g1_fill_description(correct_description)
        # Нажимаем кнопку Сохранить для создания заявки
        self.APP.g1_web_ticket_base.g1_click_button_create_or_save()
        # Переходим в заявке, в таб МОИ
        self.APP.g1_web_any_page.g1_click_button_tab_my_in_requests()
        # Переходим в тикет с нужным описанием
        self.APP.g1_web_ticket_base.g1_go_to_ticket_in_list_with_need_description(correct_description)
        # Получаем согласующего заявки
        actual_approvers = self.APP.g1_web_ticket_base.g1_get_approvers_in_ticket()
        # Получаем обозревателя заявки
        actual_observers = self.APP.g1_web_ticket_base.g1_get_observers_in_ticket()
        # Сравниваем актуальный норматив с ранее заданным
        assert department == self.APP.g1_web_request_edit.g1_get_department()
        assert category == self.APP.g1_web_request_edit.g1_get_category()
        assert request_type == self.APP.g1_web_request_edit.g1_get_request_type()
        assert job_type == self.APP.g1_web_request_edit.g1_get_job_type()
        # Проверяем количество согласующих
        assert len(actual_approvers) == 1
        # Проверяем конкретного согласующего
        assert correct_approver in actual_approvers
        # Проверяем количество обозреваталей
        assert len(actual_observers) == 1
        # Проверяем конкретного обозревателя
        assert correct_observer in actual_observers

    @allure.title('Создание заявки со вложением через блок вложений')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_create_request_with_attachment_first(self):
        # Задаем данные для выбора норматива
        job_type = 'Тестовый_Тип_1'
        department = self.APP.group_data.service_template_g1[job_type]['department']
        category = self.APP.group_data.service_template_g1[job_type]['category']
        request_type = self.APP.group_data.service_template_g1[job_type]['type']
        # Переходим к созданию заявки
        self.APP.g1_web_any_page.g1_click_button_plus_request()
        # Заполняем норматив через глобальный поиск
        path_normative = department + ' → ' + category + ' → ' + request_type + ' → ' + job_type
        self.APP.g1_web_request_new.g1_select_need_normative_in_global_search(path_normative)
        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.g1_web_ticket_base.g1_fill_description(correct_description)
        # Добавляем вложение через блок вложений
        correct_attachment = 'TestApiFile.jpg'
        self.APP.g1_web_ticket_base.g1_add_attachment_in_ticket(correct_attachment)
        # Нажимаем кнопку Сохранить для создания заявки
        self.APP.g1_web_ticket_base.g1_click_button_create_or_save()
        # Переходим в заявке, в таб МОИ
        self.APP.g1_web_any_page.g1_click_button_tab_my_in_requests()
        # Переходим в тикет с нужным описанием
        self.APP.g1_web_ticket_base.g1_go_to_ticket_in_list_with_need_description(correct_description)
        # Получаем описание тикета
        actual_description = self.APP.g1_web_ticket_base.g1_get_description()
        # Получаем вложения тикета
        actual_attachments = self.APP.g1_web_ticket_base.g1_get_attachments_in_ticket()
        # Сравниваем два описания между собой
        assert correct_description == actual_description
        # Сравниваем актуальный норматив с ранее заданным
        assert department == self.APP.g1_web_request_edit.g1_get_department()
        assert category == self.APP.g1_web_request_edit.g1_get_category()
        assert request_type == self.APP.g1_web_request_edit.g1_get_request_type()
        assert job_type == self.APP.g1_web_request_edit.g1_get_job_type()
        # Проверяем количество вложений
        assert len(actual_attachments) == 1
        # Проверяем конкретное вложение
        assert correct_attachment in actual_attachments

    @allure.title('Создание заявки с датой начала')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_create_request_with_date_start(self):
        # Задаем данные для выбора норматива
        job_type = 'Тестовый_Тип_1'
        department = self.APP.group_data.service_template_g1[job_type]['department']
        category = self.APP.group_data.service_template_g1[job_type]['category']
        request_type = self.APP.group_data.service_template_g1[job_type]['type']
        # Переходим к созданию заявки
        self.APP.g1_web_any_page.g1_click_button_plus_request()
        # Заполняем норматив через глобальный поиск
        path_normative = department + ' → ' + category + ' → ' + request_type + ' → ' + job_type
        self.APP.g1_web_request_new.g1_select_need_normative_in_global_search(path_normative)
        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.g1_web_ticket_base.g1_fill_description(correct_description)
        # Добавляем дату начала
        correct_date_start = self.APP.time.date_increased_x_days(2)
        self.APP.g1_web_ticket_base.g1_fill_start_date(correct_date_start)
        # Нажимаем кнопку Сохранить для создания заявки
        self.APP.g1_web_ticket_base.g1_click_button_create_or_save()
        # Переходим в заявке, в таб МОИ
        self.APP.g1_web_any_page.g1_click_button_tab_my_in_requests()
        # Переходим в тикет с нужным описанием
        self.APP.g1_web_ticket_base.g1_go_to_ticket_in_list_with_need_description(correct_description)
        # Получаем описание тикета
        actual_description = self.APP.g1_web_ticket_base.g1_get_description()
        # Получаем дату начала тикета
        actual_date_start = self.APP.g1_web_ticket_base.g1_get_date_start_ticket()
        # Сравниваем два описания между собой
        assert correct_description == actual_description
        # Сравниваем актуальный норматив с ранее заданным
        assert department == self.APP.g1_web_request_edit.g1_get_department()
        assert category == self.APP.g1_web_request_edit.g1_get_category()
        assert request_type == self.APP.g1_web_request_edit.g1_get_request_type()
        assert job_type == self.APP.g1_web_request_edit.g1_get_job_type()
        # Проверяем дату начала
        assert correct_date_start == actual_date_start

    @allure.title('Проверка примечания в нормативе')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_check_note_in_normative(self):
        # Задаем данные для выбора норматива
        job_type = 'Тестовый_Тип_3'
        department = self.APP.group_data.service_template_g1[job_type]['department']
        category = self.APP.group_data.service_template_g1[job_type]['category']
        request_type = self.APP.group_data.service_template_g1[job_type]['type']
        # Переходим к созданию заявки
        self.APP.g1_web_any_page.g1_click_button_plus_request()
        # Заполняем норматив через глобальный поиск
        path_normative = department + ' → ' + category + ' → ' + request_type + ' → ' + job_type
        self.APP.g1_web_request_new.g1_select_need_normative_in_global_search(path_normative)
        # Получаем текст модального окна
        actual_note = self.APP.g1_web_request_new.g1_get_text_note()
        correct_note = self.APP.group_data.service_template_g1['Тестовый_Тип_3']['note']
        assert correct_note == actual_note

    @allure.title('Проверка региона после создания заявки, не меняя регион до создания')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_check_region_after_create_request_first(self):
        # Задаем данные для выбора норматива
        job_type = 'Тестовый_Тип_1'
        department = self.APP.group_data.service_template_g1[job_type]['department']
        category = self.APP.group_data.service_template_g1[job_type]['category']
        request_type = self.APP.group_data.service_template_g1[job_type]['type']
        correct_region = self.APP.group_data.g1_users['User1']['Region']
        # Переходим к созданию заявки
        self.APP.g1_web_any_page.g1_click_button_plus_request()
        # Заполняем норматив через глобальный поиск
        path_normative = department + ' → ' + category + ' → ' + request_type + ' → ' + job_type
        self.APP.g1_web_request_new.g1_select_need_normative_in_global_search(path_normative)
        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.g1_web_ticket_base.g1_fill_description(correct_description)
        # Нажимаем кнопку Сохранить для создания заявки
        self.APP.g1_web_ticket_base.g1_click_button_create_or_save()
        # Переходим в заявке, в таб МОИ
        self.APP.g1_web_any_page.g1_click_button_tab_my_in_requests()
        # Переходим в тикет с нужным описанием
        self.APP.g1_web_ticket_base.g1_go_to_ticket_in_list_with_need_description(correct_description)
        # Получаем описание тикета
        actual_description = self.APP.g1_web_ticket_base.g1_get_description()
        # Получаем регион тикета
        actual_region = self.APP.g1_web_request_base.g1_get_region()
        # Сравниваем два описания между собой
        assert correct_description == actual_description
        # Сравниваем актуальный норматив с ранее заданным
        assert department == self.APP.g1_web_request_edit.g1_get_department()
        assert category == self.APP.g1_web_request_edit.g1_get_category()
        assert request_type == self.APP.g1_web_request_edit.g1_get_request_type()
        assert job_type == self.APP.g1_web_request_edit.g1_get_job_type()
        # Сравниваем два региона между собой
        assert correct_region == actual_region

    @allure.title('Проверка региона после создания заявки, поменяв регион до создания')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_check_region_after_create_request_second(self):
        # Задаем данные для выбора норматива
        job_type = 'Тестовый_Тип_1'
        department = self.APP.group_data.service_template_g1[job_type]['department']
        category = self.APP.group_data.service_template_g1[job_type]['category']
        request_type = self.APP.group_data.service_template_g1[job_type]['type']
        correct_region = 'Астрахань'
        # Переходим к созданию заявки
        self.APP.g1_web_any_page.g1_click_button_plus_request()
        # Заполняем норматив через глобальный поиск
        path_normative = department + ' → ' + category + ' → ' + request_type + ' → ' + job_type
        self.APP.g1_web_request_new.g1_select_need_normative_in_global_search(path_normative)
        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.g1_web_ticket_base.g1_fill_description(correct_description)
        # Меняем регион
        self.APP.g1_web_request_new.g1_change_region(correct_region)
        # Нажимаем кнопку Сохранить для создания заявки
        self.APP.g1_web_ticket_base.g1_click_button_create_or_save()
        # Переходим в заявке, в таб МОИ
        self.APP.g1_web_any_page.g1_click_button_tab_my_in_requests()
        # Переходим в тикет с нужным описанием
        self.APP.g1_web_ticket_base.g1_go_to_ticket_in_list_with_need_description(correct_description)
        # Получаем описание тикета
        actual_description = self.APP.g1_web_ticket_base.g1_get_description()
        # Получаем регион тикета
        actual_region = self.APP.g1_web_request_base.g1_get_region()
        # Сравниваем два описания между собой
        assert correct_description == actual_description
        # Сравниваем актуальный норматив с ранее заданным
        assert department == self.APP.g1_web_request_edit.g1_get_department()
        assert category == self.APP.g1_web_request_edit.g1_get_category()
        assert request_type == self.APP.g1_web_request_edit.g1_get_request_type()
        assert job_type == self.APP.g1_web_request_edit.g1_get_job_type()
        # Сравниваем два региона между собой
        assert correct_region == actual_region