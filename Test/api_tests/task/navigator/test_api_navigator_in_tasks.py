import time

import allure
import pytest
from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Task')
@allure.story('Счётчики в задачах')
class TestApiNavigatorInTasks(ApiBase):

    def setup_method(self):
        self.APP.api_token.get_token('SystemOperator')

    @allure.title('Создание задачи с установленным плановым временем')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='При смене даты окончания, не приходит новое плановое время исполнения https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/19611')
    def test_api_create_task_with_planned_time_execution(self):

        # Создание задачи
        created_task = self.create_task({'endDate': 1, 'beginDate': self.APP.time.get_date_time_for_api_g2_hours(-3)})

        # Определяем кол-во минут в временном промежутке
        total_minutes = int(abs(self.APP.time.determinate_time_interval_between_dates(created_task['beginDate'], created_task['endDate']) / 60))

        assert created_task['navigator']['execution']['plannedTime'] == total_minutes
        assert created_task['navigator']['execution']['timeNavigatorStatus'] == 'Active'
        assert created_task['navigator']['agreement']['timeNavigatorStatus'] == 'Stopped'
        assert created_task['navigator']['clarification']['timeNavigatorStatus'] == 'Stopped'

    @allure.title('Изменение планового времени исполнения в задачах')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='При смене даты окончания, не приходит новое плановое время исполнения https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/19611')
    def test_api_change_execution_planned_time(self):

        # Создание задачи
        created_task = self.create_task({'beginDate': -1, 'endDate': 1})

        # Устанавливаем новую дату окончания задачи
        new_end_date_in_task = self.APP.api_actions_in_task.update_task(created_task['syncToken'], created_task['id'], {'endDate': 3})

        # Определяем кол-во минут в временном промежутке
        total_minutes = int(abs(self.APP.time.determinate_time_interval_between_dates(new_end_date_in_task['beginDate'], new_end_date_in_task['endDate']) / 60))

        assert new_end_date_in_task['navigator']['execution']['plannedTime'] == total_minutes
        assert new_end_date_in_task['navigator']['execution']['timeNavigatorStatus'] == 'Active'
        assert new_end_date_in_task['navigator']['agreement']['timeNavigatorStatus'] == 'Stopped'
        assert new_end_date_in_task['navigator']['clarification']['timeNavigatorStatus'] == 'Stopped'

    @allure.title('Проверка работы счётчика фактического времени исполнения в задачах')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_checking_work_execution_factual_time(self):

        # Создание задачи
        created_task = self.create_task({'beginDate': -1, 'endDate': 1})

        # Ожидание смены счётчика времени исполнения
        time.sleep(61)

        # Получаем информацию по задаче
        task = self.APP.api_tasks.get_tasks_id(created_task['id'])

        assert self.APP.api_actions_in_task.checking_the_equality_params_in_counters(task['counters'], 'type', {'Execution': 1, 'ContractorExecution': 1})

    @allure.title('Изменение планового времени согласования в задачах (отсутствует согласующий)')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Не обновляется плавовое время согласования без добавления согласующего https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/19610')
    def test_api_change_approval_planned_time_without_approver(self):

        # Создание задачи
        created_task = self.create_task({})

        # Изменяем плановое время согласования
        change_approval_time = self.APP.api_actions_in_task.change_planned_time_in_task(created_task['id'], {'plannedTimeOfApproval': 1}, created_task['syncToken'])

        assert change_approval_time['plannedTimeOfApproval'] == 1
        assert change_approval_time['navigator']['agreement']['timeNavigatorStatus'] == 'Stopped'

    @allure.title('Ввод планового времени согласования больше чем возможно в задачах')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_approval_planned_time_with_very_high_time(self):

        # Создание задачи
        created_task = self.create_task({})

        # Изменяем плановое время согласования
        change_approval_time = self.APP.api_actions_in_task.change_planned_time_in_task(created_task['id'], {'plannedTimeOfApproval': 2147483648}, created_task['syncToken'])

        assert change_approval_time['status'] == 400

    @allure.title('Ввод планового времени согласования меньше чем возможно в задачах')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_approval_planned_time_with_very_low_time(self):

        # Создание задачи
        created_task = self.create_task({})

        # Изменяем плановое время согласования
        change_approval_time = self.APP.api_actions_in_task.change_planned_time_in_task(created_task['id'], {'plannedTimeOfApproval': -2147483649}, created_task['syncToken'])

        assert change_approval_time['status'] == 400

    @allure.title('Изменение планового времени согласования в задачах (есть согласующий)')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Не обновляется плавовое время согласования без добавления согласующего https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/19610')
    def test_api_change_approval_planned_time_with_approver(self):

        # Создание задачи
        created_task = self.create_task({'approvers': ['test_user04']})

        # Изменяем плановое время согласования
        change_approval_time = self.APP.api_actions_in_task.change_planned_time_in_task(created_task['id'], {'plannedTimeOfApproval': 1}, created_task['syncToken'])

        assert change_approval_time['plannedTimeOfApproval'] == 1
        assert change_approval_time['navigator']['execution']['timeNavigatorStatus'] == 'Stopped'
        assert change_approval_time['navigator']['agreement']['timeNavigatorStatus'] == 'Active'
        assert change_approval_time['navigator']['clarification']['timeNavigatorStatus'] == 'Stopped'

    @allure.title('Проверка работы счётчика фактического времени согласования в задачах (Один согласующий)')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933')
    def test_api_checking_work_approval_planned_time_with_one_approver(self):

        # Создание задачи
        created_task = self.create_task({'beginDate': -1, 'endDate': 1})

        # Добавляем согласующего
        add_approver = self.APP.api_actions_in_task.add_agreements_in_task(self.users['test_user04']['user_id'], created_task['syncToken'], created_task['id'])

        # Изменяем плановое время согласования
        change_approval_time = self.APP.api_actions_in_task.change_planned_time_in_task(created_task['id'], {'plannedTimeOfApproval': 1}, add_approver['syncToken'])

        # Ожидание смены счётчика времени согласования
        time.sleep(61)

        # Получаем информацию по задаче
        task = self.APP.api_tasks.get_tasks_id(created_task['id'])

        assert self.APP.api_actions_in_task.checking_the_equality_params_in_counters(task['counters'], 'type', {'TotalAgreement': 1, 'AgreementLevel': 1})

    @allure.title('Проверка работы счётчика фактического времени согласования в задачах с добавлением согласующего во время создания задачи')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933')
    def test_api_checking_work_approval_planned_time_with_added_one_approver_during_task_creating(self):

        # Создание задачи
        created_task = self.create_task({'beginDate': -1, 'endDate': 1, 'approvers': ['test_user04']})

        # Изменяем плановое время согласования
        change_approval_time = self.APP.api_actions_in_task.change_planned_time_in_task(created_task['id'], {'plannedTimeOfApproval': 1}, created_task['syncToken'])

        # Ожидание смены счётчика времени согласования
        time.sleep(61)

        # Получаем информацию по задаче
        task = self.APP.api_tasks.get_tasks_id(created_task['id'])

        assert task['plannedTimeOfApproval'] == 1
        assert self.APP.api_actions_in_task.checking_the_equality_params_in_counters(task['counters'], 'type', {'PendingAgreement': 1})
        assert change_approval_time['navigator']['execution']['timeNavigatorStatus'] == 'Stopped'
        assert change_approval_time['navigator']['agreement']['timeNavigatorStatus'] == 'Active'
        assert change_approval_time['navigator']['clarification']['timeNavigatorStatus'] == 'Stopped'

    @allure.title('Проверка работы счётчика фактического времени согласования в задачах (Пара согласующих)')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933')
    def test_api_checking_work_approval_planned_time_with_two_approvers(self):

        # Создание задачи
        created_task = self.create_task({'beginDate': -1, 'endDate': 1, 'approvers': ['test_user01', 'test_user02']})

        # Изменяем плановое время согласования
        change_approval_time = self.APP.api_actions_in_task.change_planned_time_in_task(created_task['id'], {'plannedTimeOfApproval': 1}, created_task['syncToken'])

        # Ожидание смены счётчика времени согласования
        time.sleep(61)

        # Получаем информацию по задаче
        task = self.APP.api_tasks.get_tasks_id(created_task['id'])

        assert task['plannedTimeOfApproval'] == 1
        assert self.APP.api_actions_in_task.checking_the_equality_params_in_counters(task['counters'], 'type', {'PendingAgreement': 1})

    @allure.title('Изменение планового времени уточнения в задачах')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_clarification_planned_time(self):

        # Создание задачи
        created_task = self.create_task({})

        # Изменяем плановое время уточнения
        change_clarification_time = self.APP.api_actions_in_task.change_planned_time_in_task(created_task['id'], {'plannedTimeOfClarification': 1}, created_task['syncToken'])

        assert change_clarification_time['plannedTimeOfClarification'] == 1
        assert change_clarification_time['navigator']['agreement']['timeNavigatorStatus'] == 'Stopped'

    @allure.title('Изменение планового времени оценки задачи')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_feedback_planned_time(self):

        # Создание задачи
        created_task = self.create_task({})

        # Переходим на пользователя-исполнителя
        self.APP.api_token.get_token('test_user02')

        # Отправляем задачу в статус "На проверке"
        resolved_task = self.APP.api_actions_in_task.resolve_task(created_task['syncToken'], created_task['id'])

        # Переходим на пользователя с правами модератора
        self.APP.api_token.get_token('SystemOperator')

        # Изменяем плановое время оценки
        change_feedback_time = self.APP.api_actions_in_task.change_planned_time_in_task(created_task['id'], {'plannedTimeOfFeedback': 1}, resolved_task['syncToken'])

        assert change_feedback_time['plannedTimeOfFeedback'] == 1
        assert change_feedback_time['navigator']['execution']['timeNavigatorStatus'] == 'Stopped'
        assert change_feedback_time['navigator']['agreement']['timeNavigatorStatus'] == 'Stopped'
        assert change_feedback_time['navigator']['clarification']['timeNavigatorStatus'] == 'Stopped'

    @allure.title('Проверка работы счётчика фактического времени оценки задач')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_checking_work_factual_time_feedback(self):

        # Создание задачи
        created_task = self.create_task({})

        # Переходим на пользователя-исполнителя
        self.APP.api_token.get_token('test_user02')

        # Отправляем задачу в статус "На проверке"
        resolved_task = self.APP.api_actions_in_task.resolve_task(created_task['syncToken'], created_task['id'])

        # Переходим на пользователя с правами модератора
        self.APP.api_token.get_token('SystemOperator')

        # Изменяем плановое время оценки
        change_feedback_time = self.APP.api_actions_in_task.change_planned_time_in_task(created_task['id'], {'plannedTimeOfFeedback': 1}, resolved_task['syncToken'])

        # Ожидание смены счётчика времени оценки
        time.sleep(61)

        # Получаем информацию по задаче
        task = self.APP.api_tasks.get_tasks_id(created_task['id'])

        assert task['plannedTimeOfFeedback'] == 1
        assert self.APP.api_actions_in_task.checking_the_equality_params_in_counters(task['counters'], 'type', {'Feedback': 1})

    @allure.title('Смена даты начала')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_begin_date(self):

        # Создание задачи
        created_task = self.create_task({})

        # Устанавливаем новую дату начала
        new_date = self.APP.time.get_date_time_for_api_g2(-1)

        # Смена даты начала
        new_begin_date = self.APP.api_actions_in_task.update_task(created_task['syncToken'], created_task['id'], {'beginDate': new_date})

        assert new_begin_date['beginDate'] == new_date

    @allure.title('Создание задачи c текстом в дате начала')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_create_task_with_string_in_begin_date(self):

        # Создание задачи
        created_task = self.create_task({'endDate': 1, 'beginDate': 'Potato'})

        assert created_task['status'] == 400

    @allure.title('Смена даты начала на текст')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_begin_date_to_string_in_task(self):

        # Создание задачи
        created_task = self.create_task({'endDate': 1, 'beginDate': -1})

        # Смена даты начала
        new_begin_date = self.APP.api_actions_in_task.update_task(created_task['syncToken'], created_task['id'], {'beginDate': 'Potato'})

        assert new_begin_date['status'] == 400

    @allure.title('Смена даты начала пользоватем, не учавствующим в задаче')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_begin_date_in_task_user_not_in_task(self):

        # Создание задачи
        created_task = self.create_task({'endDate': 1, 'beginDate': -1})

        # Переходим на пользователя не находящегося в задаче
        self.APP.api_token.get_token('test_user01')

        # Смена даты начала
        new_begin_date = self.APP.api_actions_in_task.update_task(created_task['syncToken'], created_task['id'], {'beginDate': -1})

        assert new_begin_date['status'] == 403

    @allure.title('Смена даты начала без авторизации')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_begin_date_in_task_without_authorization(self):

        # Создание задачи
        created_task = self.create_task({'endDate': 1, 'beginDate': -1})

        # Убираем авторизацию
        self.APP.settings.Authorization = False

        # Смена даты начала
        new_begin_date = self.APP.api_actions_in_task.update_task(created_task['syncToken'], created_task['id'], {'beginDate': -1})

        assert new_begin_date.status_code == 401

    @allure.title('Смена даты окончания')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_end_date(self):

        # Создание задачи
        created_task = self.create_task({})

        # Устанавливаем новую дату окончания
        new_date = self.APP.time.get_date_time_for_api_g2(+1)

        # Смена даты окончания
        new_end_date = self.APP.api_actions_in_task.update_task(created_task['syncToken'], created_task['id'], {'endDate': new_date})

        assert new_end_date['endDate'] == new_date

    @allure.title('Создание задачи c текстом в дате окончания')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_create_task_with_string_in_end_date(self):

        # Создание задачи
        created_task = self.create_task({'endDate': 'Potato', 'beginDate': self.APP.time.get_date_time_for_api_g2_hours(-3)})

        assert created_task['status'] == 400

    @allure.title('Смена даты окончания на текст')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_end_date_to_string_in_task(self):

        # Создание задачи
        created_task = self.create_task({'endDate': 1, 'beginDate': -1})

        # Смена даты окончания
        new_end_date = self.APP.api_actions_in_task.update_task(created_task['syncToken'], created_task['id'], {'endDate': 'Potato'})

        assert new_end_date['status'] == 400

    @allure.title('Создание задачи c большим значением в дате окончания')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_create_task_with_very_high_end_date(self):

        # Создание задачи
        created_task = self.create_task({'endDate': '10000-02-18T00:00:00Z', 'beginDate': -1})

        assert created_task['status'] == 400

    @allure.title('Смена даты окончания на большое значение')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_end_date_to_very_high_in_task(self):

        # Создание задачи
        created_task = self.create_task({'endDate': 1, 'beginDate': -1})

        # Смена даты окончания
        new_end_date = self.APP.api_actions_in_task.update_task(created_task['syncToken'], created_task['id'], {'endDate': '10000-01-01T00:00:00Z'})

        assert new_end_date['status'] == 400

    @allure.title('Смена даты окончания пользоватем, не учавствующим в задаче')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_end_date_in_task_user_not_in_task(self):

        # Создание задачи
        created_task = self.create_task({'endDate': 1, 'beginDate': -1})

        # Переходим на пользователя не находящегося в задаче
        self.APP.api_token.get_token('test_user01')

        # Смена даты начала
        new_end_date = self.APP.api_actions_in_task.update_task(created_task['syncToken'], created_task['id'], {'endDate': 2})

        assert new_end_date['status'] == 403

    @allure.title('Смена даты окончания без авторизации')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_change_end_date_in_task_without_authorization(self):

        # Создание задачи
        created_task = self.create_task({'endDate': 1, 'beginDate': -1})

        # Убираем авторизацию
        self.APP.settings.Authorization = False

        # Смена даты окончания
        new_end_date = self.APP.api_actions_in_task.update_task(created_task['syncToken'], created_task['id'], {'endDate': 2})

        assert new_end_date.status_code == 401
