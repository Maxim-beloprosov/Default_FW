import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Project')
@allure.story('Создание проекта')
class TestCreateProject(WebBase):

    @allure.title('Создание проекта')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_project(self):
        # Переходим к созданию проекта
        self.APP.web_any_page.click_btn_create_project_plus_menu()
        # Заполняем название
        self.APP.web_tickets_base.fill_name("TestProject AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_tickets_base.fill_description_in_ticket(correct_description)
        # Добавляем руководителя проекта
        self.APP.web_tickets_base.add_contractor(self.APP.group_data.users['test_user01']['Surname'] + ' ' + self.APP.group_data.users['test_user01']['Name'])
        # Создаем проект
        self.APP.web_project_create.button_to_create_project()
        # Переходим в список проектов
        self.APP.web_any_page.click_project_left_menu()
        # Вводим в поиск описание созданного проекта
        self.APP.web_project_list.input_text_in_search(correct_description)
        # Переходим в проект с нужным описанием
        self.APP.web_project_list.go_to_project_in_list(correct_description)
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Сравниваем два описания между собой
        actual_description = self.APP.web_tickets_base.get_description_in_ticket()
        assert correct_description == actual_description

    @allure.title('Создание проекта c обозревателем')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_project_with_observer(self):
        # Переходим к созданию проекта
        self.APP.web_any_page.click_btn_create_project_plus_menu()
        # Заполняем название
        self.APP.web_tickets_base.fill_name("TestProject AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Добавляем руководителя проекта
        self.APP.web_tickets_base.add_contractor(self.APP.group_data.users['test_user01']['Surname'] + ' ' + self.APP.group_data.users['test_user01']['Name'])
        # Добавляем обозревателя
        correct_observer = self.APP.group_data.users['test_user05']['Surname'] + ' ' + self.APP.group_data.users['test_user05']['Name']
        self.APP.web_tickets_base.add_observer(correct_observer)
        # Создаем проект
        self.APP.web_project_create.button_to_create_project()
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Получаем информацию о всех обозревателях
        list_observers = self.APP.web_tickets_base.get_observers_in_ticket()
        # Проверяем добавленного обозревателя
        assert len(list_observers) == 1
        assert correct_observer in list_observers

    @allure.title('Создание проекта c согласующим')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_project_with_approver(self):
        # Переходим к созданию проекта
        self.APP.web_any_page.click_btn_create_project_plus_menu()
        # Заполняем название
        self.APP.web_tickets_base.fill_name("TestProject AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Добавляем руководителя проекта
        self.APP.web_tickets_base.add_contractor(self.APP.group_data.users['test_user01']['Surname'] + ' ' + self.APP.group_data.users['test_user01']['Name'])
        # Добавляем согласующего
        correct_approver = self.APP.group_data.users['test_user05']['Surname'] + ' ' + self.APP.group_data.users['test_user05']['Name']
        self.APP.web_tickets_base.add_approver(correct_approver)
        # Создаем проект
        self.APP.web_project_create.button_to_create_project()
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Получаем информацию о всех согласующих
        list_approvers = self.APP.web_tickets_base.get_approvers_in_ticket()
        # Проверяем добавленного согласующего
        assert len(list_approvers) == 1
        assert correct_approver in list_approvers


    @allure.title('Создание проекта со вложением через боковое меню')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_project_with_attachment_first(self):
        # Переходим к созданию проекта
        self.APP.web_any_page.click_btn_create_project_plus_menu()
        # Заполняем название
        self.APP.web_tickets_base.fill_name("TestProject AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Добавляем вложение
        correct_attachment = 'Тестовое фото №1'
        self.APP.web_tickets_base.add_attachment_in_ticket(correct_attachment)
        # Добавляем руководителя проекта
        self.APP.web_tickets_base.add_contractor(self.APP.group_data.users['test_user01']['Surname'] + ' ' + self.APP.group_data.users['test_user01']['Name'])
        # Создаем проект
        self.APP.web_project_create.button_to_create_project()
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Получаем информацию о всех вложениях
        list_attachments = self.APP.web_tickets_base.get_attachments_in_ticket()
        # Проверяем добавленное вложение
        assert len(list_attachments) == 1
        assert correct_attachment in list_attachments

    @allure.title('Создание проекта со вложением в описании')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_project_with_attachment_second(self):
        # Переходим к созданию проекта
        self.APP.web_any_page.click_btn_create_project_plus_menu()
        # Заполняем название
        self.APP.web_tickets_base.fill_name("TestProject AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Добавляем вложение
        correct_attachment = 'Тестовое фото №2'
        self.APP.web_tickets_base.add_attachment_in_description(correct_attachment)
        # Добавляем руководителя проекта
        self.APP.web_tickets_base.add_contractor(self.APP.group_data.users['test_user01']['Surname'] + ' ' + self.APP.group_data.users['test_user01']['Name'])
        # Создаем проект
        self.APP.web_project_create.button_to_create_project()
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Получаем информацию о всех вложениях
        list_attachments = self.APP.web_tickets_base.get_attachments_in_ticket()
        # Проверяем добавленное вложение
        assert len(list_attachments) == 1
        assert correct_attachment in list_attachments

    @allure.title('Создание проекта с датой начала')
    @pytest.mark.skip(reason='нет временных интервалов в созданном проекте пока, закомичены')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_project_with_date_start(self):
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
        correct_date_start = self.APP.web_tickets_base.edit_start_date_in_task_or_project_when_create(self.APP.time.date_increased_x_days(7), '11')
        # Создаем проект
        self.APP.web_project_create.button_to_create_project()
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Получаем актуальную дату начала
        actual_date_start = self.APP.web_tickets_base.get_date_start_ticket()
        assert correct_date_start == actual_date_start

    @allure.title('Создание проекта с датой окончания')
    @pytest.mark.skip  # нет временных интервалов в созданном проекте пока, закомичены
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_create_project_with_date_end(self):
        # Переходим к созданию проекта
        self.APP.web_any_page.click_btn_create_project_plus_menu()
        # Заполняем название
        self.APP.web_tickets_base.fill_name("TestProject AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Заполняем описание
        self.APP.web_tickets_base.fill_description_in_ticket("TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S())
        # Добавляем руководителя проекта
        self.APP.web_tickets_base.add_contractor(self.APP.group_data.users['test_user01']['Surname'] + ' ' + self.APP.group_data.users['test_user01']['Name'])
        # Изменяем дату окончания
        correct_date_end = self.APP.web_tickets_base.edit_end_date_in_task_or_project_when_create(
            self.APP.time.date_increased_x_days(10), '11')
        # Создаем проект
        self.APP.web_project_create.button_to_create_project()
        # Раскрываем полную информацию о проекте
        self.APP.web_project_id.click_show_more()
        # Получаем актуальную дату начала
        actual_date_end = self.APP.web_tickets_base.get_date_end_ticket()
        assert correct_date_end == actual_date_end