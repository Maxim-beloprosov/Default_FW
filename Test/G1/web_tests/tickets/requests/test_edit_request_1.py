from Test.G1.web_tests.g1_web_base import G1WebBase
import allure
import pytest

@allure.epic('G1')
@allure.feature('Web - Request')
@allure.story('Редактирование заявок')
class TestEditRequest(G1WebBase):

    @allure.title('Назначить исполнителя в заявке')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_assign_contractor_in_request(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Переходим в тикет
        self.APP.g1_web_ticket_base.g1_go_to_need_ticket('request', request['Id'])
        # Назначаем исполнителя заявки
        correct_contractor = 'user2 test'
        self.APP.g1_web_ticket_base.g1_add_contractor(correct_contractor)
        # Возвращаем актуального исполнителя
        actual_contractor = self.APP.g1_web_ticket_base.g1_get_contractor()
        # Сравниваем исполнителей
        assert correct_contractor == actual_contractor

    @allure.title('Назначить заявку на себя')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_assign_request_to_me(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Переходим в тикет
        self.APP.g1_web_ticket_base.g1_go_to_need_ticket('request', request['Id'])
        # Назначаем заявку на себя
        correct_contractor = self.APP.g1_web_request_edit.g1_assign_request_to_me()
        # Возвращаем актуального исполнителя
        actual_contractor = self.APP.g1_web_ticket_base.g1_get_contractor()
        # Сравниваем исполнителей
        assert correct_contractor == actual_contractor

    @allure.title('Изменить норматив через выбор всех сущностей инициатором')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_change_normative_select_all_essence_as_initiator(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Переходим в тикет
        self.APP.g1_web_ticket_base.g1_go_to_need_ticket('request', request['Id'])
        # Изменяем норматив через выбор всех сущностей
        correct_job_type = 'Тестовый_Тип_3'
        self.APP.g1_web_request_edit.g1_change_normative_select_all_essence(correct_job_type)
        # Получаем актуальный норматив
        actual_department = self.APP.g1_web_request_base.g1_get_department()
        actual_category = self.APP.g1_web_request_base.g1_get_category()
        actual_request_type = self.APP.g1_web_request_base.g1_get_request_type()
        actual_job_type = self.APP.g1_web_request_base.g1_get_job_type()
        # Сравниваем сущности норматива
        assert self.APP.group_data.service_template_g1[correct_job_type]['department'] == actual_department
        assert self.APP.group_data.service_template_g1[correct_job_type]['category'] == actual_category
        assert self.APP.group_data.service_template_g1[correct_job_type]['type'] == actual_request_type
        assert correct_job_type == actual_job_type

    @allure.title('Изменить норматив через глобальный поиск инициатором')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_change_normative_use_global_search_as_initiator(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Переходим в тикет
        self.APP.g1_web_ticket_base.g1_go_to_need_ticket('request', request['Id'])
        # Изменяем норматив через глобальный поиск
        correct_job_type = 'Тестовый_Тип_3'
        self.APP.g1_web_request_edit.g1_change_normative_use_global_search(correct_job_type)
        # Получаем актуальный норматив
        actual_department = self.APP.g1_web_request_base.g1_get_department()
        actual_category = self.APP.g1_web_request_base.g1_get_category()
        actual_request_type = self.APP.g1_web_request_base.g1_get_request_type()
        actual_job_type = self.APP.g1_web_request_base.g1_get_job_type()
        # Сравниваем сущности норматива
        assert self.APP.group_data.service_template_g1[correct_job_type]['department'] == actual_department
        assert self.APP.group_data.service_template_g1[correct_job_type]['category'] == actual_category
        assert self.APP.group_data.service_template_g1[correct_job_type]['type'] == actual_request_type
        assert correct_job_type == actual_job_type

    @allure.title('Проверка удаления исполнителя при смене норматива')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_check_delete_contractor_when_change_normative(self):
        self.APP.g1_api_token.get_token('User6')  #TODO Когда будет один тип у названия пользователей исправить (передавать инициатора через переменную, тк он используется несколько раз)
        # Создаем заявку
        request = self.g1_create_request()
        # Авторизуемся участником ГО
        self.APP.g1_web_any_page.g1_check_autorizated_user_and_loging_other_user_if_need('user1 test')
        # Переходим в тикет
        self.APP.g1_web_ticket_base.g1_go_to_need_ticket('request', request['Id'])
        # Назначаем заявку на себя
        self.APP.g1_web_request_edit.g1_assign_request_to_me()
        # Авторизуемся инициатором
        self.APP.g1_web_any_page.g1_check_autorizated_user_and_loging_other_user_if_need('user6 test')
        # Изменяем норматив через глобальный поиск
        correct_job_type = 'Тип для тестирования(2)'
        self.APP.g1_web_request_edit.g1_change_normative_use_global_search(correct_job_type)
        # Получаем актуальный норматив
        actual_department = self.APP.g1_web_request_base.g1_get_department()
        actual_category = self.APP.g1_web_request_base.g1_get_category()
        actual_request_type = self.APP.g1_web_request_base.g1_get_request_type()
        actual_job_type = self.APP.g1_web_request_base.g1_get_job_type()
        # Проверяем, есть ли исполнитель
        check_contractor = self.APP.g1_web_ticket_base.g1_check_contractor()
        # Сравниваем сущности норматива
        assert self.APP.group_data.service_template_g1[correct_job_type]['department'] == actual_department
        assert self.APP.group_data.service_template_g1[correct_job_type]['category'] == actual_category
        assert self.APP.group_data.service_template_g1[correct_job_type]['type'] == actual_request_type
        assert correct_job_type == actual_job_type
        # Проверяем, что нет исполнителя (должно придти False)
        assert check_contractor == False

    @allure.title('Изменить описание заявки')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_edit_description_in_request(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Переходим в тикет
        self.APP.g1_web_ticket_base.g1_go_to_need_ticket('request', request['Id'])
        # Изменяем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.g1_web_ticket_base.g1_edit_description(correct_description)
        # Получаем описание тикета
        actual_description = self.APP.g1_web_ticket_base.g1_get_description()
        # Сравниваем два описания между собой
        assert correct_description == actual_description
