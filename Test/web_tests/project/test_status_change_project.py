import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Project')
@allure.story('Изменение статуса')
class TestStatusChangeProject(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.api_token.get_token('test_user09')

    @allure.title('Смена статуса в проекте с "Новая" на "В работе"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_project_from_new_to_work(self):
        # Переходим к созданию проекта
        self.APP.web_any_page.click_btn_create_project_plus_menu()
        # Заполняем название
        self.APP.web_tickets_base.fill_name("TestProject AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Добавляем руководителя проекта
        self.APP.web_tickets_base.add_contractor(self.APP.group_data.users['test_user01']['Surname'] + ' ' + self.APP.group_data.users['test_user01']['Name'])
        # Создаем проект
        self.APP.web_project_create.button_to_create_project()
        correct_status = 'В работе'
        # Получаем актуальный статус проекта
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса проекта
        assert correct_status == actual_status

    @allure.title('Смена статуса с "Новая" на "На согласовании"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_project_from_new_to_agreement(self):
        # Переходим к созданию проекта
        self.APP.web_any_page.click_btn_create_project_plus_menu()
        # Заполняем название
        self.APP.web_tickets_base.fill_name("TestProject AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Добавляем руководителя проекта
        self.APP.web_tickets_base.add_contractor(self.APP.group_data.users['test_user01']['Surname'] + ' ' + self.APP.group_data.users['test_user01']['Name'])
        # Добавляем согласующего
        self.APP.web_tickets_base.add_approver(self.APP.group_data.users['test_user05']['Surname'] + ' ' + self.APP.group_data.users['test_user05']['Name'])
        # Создаем проект
        self.APP.web_project_create.button_to_create_project()
        correct_status = 'На согласовании'
        # Получаем актуальный статус проекта
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса проекта
        assert correct_status == actual_status

    @allure.title('Смена статуса с "Новая" на "В ожидании + дата"')  # дата в формате 21 апр., 00:00
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.skip(reason='нет временных интервалов в созданном проекте пока, закомичены')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_project_from_new_to_waiting(self):
        # Переходим к созданию проекта
        self.APP.web_any_page.click_btn_create_project_plus_menu()
        # Заполняем название
        self.APP.web_tickets_base.fill_name("TestProject AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Добавляем руководителя проекта
        self.APP.web_tickets_base.add_contractor(self.APP.group_data.users['test_user01']['Surname'] + ' ' + self.APP.group_data.users['test_user01']['Name'])
        # Изменяем дату окончания
        self.APP.web_tickets_base.edit_end_date_in_task_or_project_when_create(self.APP.time.date_increased_x_days(10),
                                                                               '11')
        # Изменяем дату создания
        correct_date_start = self.APP.web_tickets_base.edit_start_date_in_task_or_project_when_create(
            self.APP.time.date_increased_x_days(7), '11')
        # Создаем проект
        self.APP.web_project_create.button_to_create_project()
        correct_status = 'В ожидании'
        # Получаем актуальный статус проекта
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса проекта
        assert correct_status == actual_status[0:10]
