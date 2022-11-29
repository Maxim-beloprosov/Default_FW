import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Task')
@allure.story('Создание задачи')
class TestApiCreateTask(ApiBase):

    @allure.title('Создание задачи на себя')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_create_task(self):

        # Создаем задачу
        task = self.create_task()

        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']
        assert task['contractors'][0]['id'] == self.APP.group_data.users['test_user02']['user_id']

    @allure.title('Создание задачи с обозревателем')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_create_task_with_observer(self):

        # Создаем задачу
        task = self.create_task({"observers": ['test_user03']})

        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']
        assert task['contractors'][0]['id'] == self.APP.group_data.users['test_user02']['user_id']
        assert task["observers"][0]['id'] == self.APP.group_data.users['test_user03']['user_id']

    @allure.title('Создание задачи с cогласующим')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_create_task_with_approver(self):

        # Создаем задачу
        task = self.create_task({"approvers": ['test_user03']})

        # Сравниваем полученные значения с ожидаемыми
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']
        assert task['contractors'][0]['id'] == self.APP.group_data.users['test_user02']['user_id']
        assert task["agreements"][0]["approver"]['id'] == self.APP.group_data.users['test_user03']['user_id']

    @allure.title('Создание задачи без названия')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_create_task_without_subject(self):

        # Создаем задачу
        task = self.create_task({"subject": None})

        # Сравниваем полученные значения с ожидаемыми
        assert task['status'] == 400

    @allure.title('Создание задачи без описания')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_create_task_without_description(self):

        # Подготавливаем название
        subject = "AutomationApiTestTask " + self.APP.time.get_date_time_Y_m_d_H_M_S()

        # Id исполнителя
        contractor_id = self.APP.group_data.users['test_user02']['user_id']

        body = {
            "subject": subject,
            "contractorId": contractor_id
        }

        # Создаем задачу
        task = self.APP.api_tasks.post_tasks(body)

        # Сравниваем полученные значения с ожидаемыми
        assert task['status'] == 400

    @allure.title('Создание задачи без исполнителя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_create_task_without_contractor(self):

        # Подготавливаем название
        subject = "AutomationApiTestTask " + self.APP.time.get_date_time_Y_m_d_H_M_S()

        body = {
            "subject": subject,
            "descriptionContent": [{
                "type": 'Text',
                "text": "AutomationApiTestTask"
            }]
        }

        # Создаем задачу
        task = self.APP.api_tasks.post_tasks(body)

        # Сравниваем полученные значения с ожидаемыми
        assert task['status'] == 400

    @allure.title('Создание задачи с датой окончания раньше текущей даты')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_create_task_end_date_earlier_current_date(self):

        # Создаем задачу с датой окончания раньше текущей даты
        task = self.create_task({'endDate': self.APP.time.get_date_increased_x_days_json(-1)})

        # Сравниваем полученные значения с ожидаемыми
        assert task['status'] == 400

    @allure.title('Создание задачи с датой окончания раньше даты начала')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_create_task_end_date_earlier_begin_date(self):

        # Создаем задачу с датой окончания раньше даты начала
        task = self.create_task({'endDate': self.APP.time.get_date_increased_x_days_json(-1),
                                 'beginDate': self.APP.time.get_date_increased_x_days_json(1)})

        # Сравниваем полученные значения с ожидаемыми
        assert task['status'] == 400
