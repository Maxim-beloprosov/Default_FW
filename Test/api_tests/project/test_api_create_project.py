import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Project')
@allure.story('Создание проекта')
class TestApiCreateProject(ApiBase):

    @allure.title('Создание проекта')
    @allure.description('Кантышев Николай')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_create_project(self):

        # Заносим данные для создания проекта
        project_name = 'ApiTest Create Project Auto ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        project_manager = 'test_user03'


        # Создаём проект
        project = self.create_project({"subject": project_name, "contractorId": project_manager})

        # Получаем ID руководителя (исполнителя) в созданном проекте
        project_manager_id = self.users[project_manager]['user_id']

        # Сравниваем значения созданного проекта с ожидаемыми значениями
        assert project['ticketType'] == 'Project'
        assert project['subject'] == project_name
        assert project['contractor']['id'] == project_manager_id


    @allure.title('Создание проекта с согласующим')
    @allure.description('Кантышев Николай')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_create_project_with_approver(self):

        # Заносим данные для создания проекта)
        approver = 'test_user04'

        # Создание проекта
        project = self.create_project({"approvers": [approver]})

        # Проверка значений созданного проекта с ожидаемыми значениями

        assert project['agreements'][0]['approver']['id'] == self.users[approver]['user_id']


    @allure.title('Создание проекта с несколькими согласующими')
    @allure.description('Кантышев Николай')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_create_project_with_several_approvers(self):

        # Заносим данные для создания проекта
        approver1 = 'test_user04'
        approver2 = 'test_user05'

        # Создаём проект
        project = self.create_project({"approvers": [approver1, approver2]})

        # Получение списка согласующих из проекта
        all_aprovers = self.APP.api_actions_in_project.get_all_approvers_in_project(project['agreements'])


        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert self.users[approver1]['user_id'] in all_aprovers
        assert self.users[approver2]['user_id'] in all_aprovers



    @allure.title('Создание проекта с обозревателем')
    @allure.description('Кантышев Николай')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_create_project_with_observer(self):

        # Заносим данные для создания проекта
        observer = 'test_user03'

        # Создаём проект
        project = self.create_project({"observers": [observer]})

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert project["observers"][0]['id'] == self.users[observer]['user_id']


    @allure.title('Создание проекта с несколькими обозревателями')
    @allure.description('Кантышев Николай')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_create_project_with_several_observers(self):

        observer1 = 'test_user03'
        observer2 = 'test_user05'

        # Создание проекта
        project = self.create_project({"observers": [observer1, observer2]})

        all_observers = self.APP.api_actions_in_project.get_all_observers_in_project(project['observers'])

        # Сравниваем значения созданного тикета с ожидаемыми значениями
        assert self.users[observer1]['user_id'] in all_observers
        assert self.users[observer2]['user_id'] in all_observers


    @allure.title('Создание проекта с заданным временем начала')
    @allure.description('Кантышев Николай')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_create_project_with_spec_start_time(self):

        # Заносим данные для создания проекта
        begin_date = self.APP.time.get_date_time_Y_m_d_H_M_S()

        # Создание проекта
        project = self.create_project({"beginDate": begin_date})

        # Занесение в переменную заданной даты и конвертация её в корректный для проверки формат
        project_check_date = self.APP.time.tickets_date(begin_date)

        # Сравниваем значения созданного тикета с ожидаемыми значениям
        assert project['beginDate'] == project_check_date


    @allure.title('Создание проекта с заданным временем окончания')
    @allure.description('Кантышев Николай')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_create_project_with_spec_end_time(self):

        # Заносим в переменную текущее время
        end_date = self.APP.time.get_date_time_Y_m_d_H_M_S()

        # Создание проекта с заданным временем окончания
        project = self.create_project({"endDate": end_date})

        # Занесение в переменную заданной даты и конвертация её в корректный для проверки формат
        project_check_date = self.APP.time.tickets_date(end_date)

        # Сравниваем значения созданного тикета с ожидаемыми значениям
        assert project['endDate'] == project_check_date
