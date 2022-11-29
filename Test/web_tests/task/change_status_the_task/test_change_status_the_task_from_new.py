import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Task')
@allure.story('Изменение статуса задачи из статуса "Новая"')
class TestChangeTheStatusFromNew(WebBase):

    @allure.title('Смена статуса с "Новая" на "В работе"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_change_status_in_task_from_new_to_work(self):
        # Создаем задачу
        self.create_task_in_web()
        correct_status = 'В работе'
        # Получаем актуальный статус задачи
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса задачи
        assert correct_status == actual_status

    @allure.title('Смена статуса с "Новая" на "На согласовании"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_change_status_in_task_from_new_to_agreement(self):
        # Переходим к созданию задачи
        self.APP.web_any_page.click_btn_create_task_left_menu()
        # Добавляем согласующего
        self.APP.web_tickets_base.add_approver(self.APP.group_data.users['test_user05']['Surname'] + ' ' + self.APP.group_data.users['test_user05']['Name'])
        # Заполняем название
        self.APP.web_tickets_base.fill_name("TestTask AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Добавляем исполнителя
        self.APP.web_tickets_base.add_contractor(self.APP.group_data.users['test_user01']['Surname'] + ' ' + self.APP.group_data.users['test_user01']['Name'])
        # Создаем задачу
        self.APP.web_task_create.click_button_to_create_task()
        correct_status = 'На согласовании'
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['ENG'][correct_status])
        # Сравниваем 2 статуса задачи
        assert correct_status == actual_status

    @allure.title('Смена статуса с "Новая" на "В ожидании + дата"')  # дата в формате 21 апр., 00:00
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_change_status_in_task_from_new_to_waiting(self):
        # Переходим к созданию задачи
        self.APP.web_any_page.click_btn_create_task_left_menu()
        # Заполняем название
        self.APP.web_tickets_base.fill_name("TestTask AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Добавляем исполнителя
        self.APP.web_tickets_base.add_contractor(self.APP.group_data.users['test_user01']['Surname'] + ' ' + self.APP.group_data.users['test_user01']['Name'])
        # Изменяем дату окончания
        self.APP.web_tickets_base.edit_end_date_in_task_or_project_when_create(self.APP.time.date_increased_x_days(10),
                                                                               '11')
        # Изменяем дату создания
        self.APP.web_tickets_base.edit_start_date_in_task_or_project_when_create(
            self.APP.time.date_increased_x_days(7), '11')
        # Создаем задачу
        self.APP.web_task_create.click_button_to_create_task()
        correct_status = 'В ожидании'
        # Получаем актуальный статус задачи
        actual_status = self.APP.web_tickets_base.get_status_ticket()
        # Сравниваем 2 статуса задачи
        assert correct_status == actual_status[0:10]
