import allure
import pytest
from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Task')
@allure.story('Согласование задачи')
class TestApiTheTaskAgreements(ApiBase):

    @allure.title('Положительное согласование задачи с одним согласующим')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933')
    def test_api_task_approve_with_one_approver(self):

        # Создаем задачу
        task = self.create_task({"contractorId": 'test_user06', "approvers": ['test_Boss03']})

        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token(user_name='test_Boss03')

        # Согласование данных согласующим
        task_approve = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])

        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task_approve['ticketType'] == 'Task'
        assert task_approve['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Положительное согласование задачи одним из согласующих')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933')
    def test_api_task_approve_one_of_two_approvers(self):

        # Создаем задачу
        task = self.create_task({"contractorId": 'test_user06', "approvers": ['test_user05', 'test_user07']})

        # Перелогиниваемся на 1-го согласующего
        self.APP.api_token.get_token(user_name='test_user05')

        # Согласование данных согласующим
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])

        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title("Пользователь принимает отрицательное согласование задачи, начальник принимает положительное.")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933')
    def test_api_task_approve_after_reject(self):

        # Создаем задачу
        task = self.create_task({"contractorId": 'test_user06', "approvers": ['test_Boss02', 'test_user05']})

        # Перелогиниваемся на согласующего пользователя
        self.APP.api_token.get_token(user_name='test_user05')

        # Отклонение задачи пользователем
        task = self.APP.api_actions_in_task.reject_task(task['syncToken'], task['id'])

        # Перелогиниваемся на начальника начальника
        self.APP.api_token.get_token(user_name='test_Boss02')

        # Согласующий согласовывает задачу
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])

        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Несколько согласующих, все принимают положительное согласование')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933')
    def test_api_task_all_approve(self):

        # Создаем задачу
        task = self.create_task({"contractorId": 'test_user06', "approvers": ['test_user05', 'test_user07']})

        # Перелогиниваемся на 1-го согласующего
        self.APP.api_token.get_token(user_name='test_user05')

        # Согласование задачи 1-ым согласующим
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])

        # Перелогиниваемся на 2-го согласующего
        self.APP.api_token.get_token(user_name='test_user07')

        # Согласование задачи 2-ым согласующим
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])

        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title("Начальник принимает отрицательное согласование при наличии подчиненного в согласующих")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933')
    def test_api_boss_reject_with_user(self):

        # Создаем задачу
        task = self.create_task({"contractorId": 'test_user06', "approvers": ['test_Boss03', 'test_user07']})

        # Перелогиниваемся на начальника
        self.APP.api_token.get_token(user_name='test_Boss03')

        # Отклонение задачи начальником
        task = self.APP.api_actions_in_task.reject_task(task['syncToken'], task['id'])

        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['Отклонено']

    @allure.title("Положительное согласование начальником при наличии подчиненного в согласующих")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933')
    def test_api_boss_approve_with_approver(self):

        # Создаем задачу
        task = self.create_task({"contractorId": 'test_user06', "approvers": ['test_Boss03', 'test_user07']})

        # Перелогиниваемся на начальника
        self.APP.api_token.get_token(user_name='test_Boss03')

        # Согласование задачи начальником
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])

        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Возврат в работу при апелляции руководителем согласующего = инициатору')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Нет возможности апеллировать задачу если руководитель согласующего = инициатору. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/19406')
    def test_api_return_to_work_on_appeal_if_manager_equal_initiator(self):

        # Переход на пользователя-инициатора test_Boss03
        self.APP.api_token.get_token("test_Boss03")

        # Создание задачи
        created_task = self.create_tickets({'contractorId': 'test_user08', 'approvers': ['test_Boss02']})

        # Переход на пользователя-согласующего test_Boss02
        self.APP.api_token.get_token("test_Boss02")

        # Отклонение задачи согласующим
        rejected_task = self.APP.api_actions_in_task.reject_task(created_task['syncToken'], created_task['id'])

        # Переход на пользователя-инициатора test_Boss03
        self.APP.api_token.get_token("test_Boss03")

        # Апеллирование задачи
        appealed_task = self.APP.api_actions_in_task.appeal_task(rejected_task['syncToken'], created_task['id'])

        assert appealed_task['ticketType'] == 'Task'
        assert appealed_task['status'] == self.status_ticket['ENG']['В работе']
        assert len(appealed_task['agreements']) == 0

    @allure.title('Проверка что при апелляции выбирается именно тот, кто отклонил заявку, делаем 4 согласующих и только 1 из них отклонил заявку')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_right_selected_approver_on_appeal(self):

        # Создание задачи
        created_task = self.create_tickets(
            {'contractorId': 'test_user09', 'approvers': ['test_user01', 'test_user02', 'test_user03', 'test_user04']})

        # Переход на пользователя-согласующего
        self.APP.api_token.get_token('test_user01')

        # Отклонение задачи согласующим
        rejected_task = self.APP.api_actions_in_task.reject_task(created_task['syncToken'], created_task['id'])

        # Переход на пользователя-инициатора
        self.APP.api_token.get_token('test_user09')

        # Апеллирование задачи
        appealed_task = self.APP.api_actions_in_task.appeal_task(rejected_task['syncToken'], created_task['id'])

        # Получение списка id всех согласующих
        approvers_id = self.list_id_all_approver(appealed_task['agreements'])

        assert appealed_task['ticketType'] == 'Task'
        assert self.users['test_user01']['user_id'] not in approvers_id
        assert self.users['test_Boss01']['user_id'] in approvers_id

    @allure.title('Отклонение задачи согласующим не дожидаясь ответа на вопрос-уточнение от инициатора')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_approver_rejected_without_answer_on_clarification(self):

        # Создание задачи
        created_task = self.create_tickets({'contractorId': 'test_user09', 'approvers': ['test_user01']}, ticket_type="Task")

        # Переход за пользователя-согласующего
        self.APP.api_token.get_token('test_user01')

        # Задаём вопрос-уточнение инициатору
        ask_initiator_task = self.APP.api_actions_in_task.clarification_ask_to_initiator_in_task(created_task['syncToken'], created_task['id'])

        # Отклонение задачи согласующим
        rejected_task = self.APP.api_actions_in_task.reject_task(ask_initiator_task['syncToken'], created_task['id'])

        assert rejected_task['ticketType'] == 'Task'
        assert rejected_task['status'] == self.status_ticket['ENG']['Отклонено']

    @allure.title('Добавление согласующего инициатором в задачу со статусом "В ожидании"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_add_approver_by_initiator_to_task_with_status_waiting(self):

        # Создание задачи
        created_task = self.create_tickets({'contractorId': 'test_user09'})

        # Перевод задачи из статуса "В работе" в статус "В ожидании"
        created_task_waiting = self.APP.api_actions_in_task.update_task(created_task['syncToken'], created_task['id'], {'beginDate': 2})

        # Добавление согласующего
        added_approver_to_task = self.APP.api_actions_in_task.add_agreements_in_task(self.users['test_user04']['user_id'], created_task_waiting['syncToken'], created_task_waiting['id'])

        assert added_approver_to_task['ticketType'] == 'Task'
        assert added_approver_to_task['status'] == self.status_ticket['ENG']['На согласовании']
        assert added_approver_to_task['agreements'][0]['approver']['id'] == self.users['test_user04']['user_id']

    @allure.title('Добавлении согласующего исполнителем')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_add_approver_by_contractor(self):

        # Создание задачи
        created_task = self.create_tickets({'contractorId': 'test_Boss03'})

        # Переход на пользователя-исполнителя
        self.APP.api_token.get_token('test_Boss03')

        # Добавление согласующего
        added_approver_to_task = self.APP.api_actions_in_task.add_agreements_in_task(self.users['test_user05']['user_id'], created_task['syncToken'], created_task['id'])

        assert added_approver_to_task['ticketType'] == 'Task'
        assert added_approver_to_task['status'] == self.status_ticket['ENG']['На согласовании']
        assert added_approver_to_task['agreements'][0]['approver']['id'] == self.users['test_user05']['user_id']

    @allure.title('Добавлении согласующего во время создания задачи')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_add_approver_while_creating_task(self):

        # Создание задачи
        created_task = self.create_tickets({'contractorId': 'test_user09', 'approvers': ['test_user05']})

        assert created_task['ticketType'] == 'Task'
        assert created_task['status'] == self.status_ticket['ENG']['На согласовании']
        assert created_task['agreements'][0]['approver']['id'] == self.users['test_user05']['user_id']

    @allure.title('Добавление одного и того же согласующего дважды')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_add_approver_twice(self):

        # Создаем задачу
        task = self.create_task({'approvers': ['test_user05']})

        # Добавляем согласующего 2 раз
        task = self.APP.api_actions_in_task.add_agreements_in_task(self.APP.group_data.users['test_user05']['user_id'], task['syncToken'], task['id'])

        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']
        assert len(task['agreements']) == 1

    @allure.title('Согласующий отказывает, инициатор апеллирует')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_reject_appeal(self):

        # Создаем задачу
        task = self.create_task({'approvers': ['test_user05']})

        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user05')

        # Согласующий отклоняет задачу
        task = self.APP.api_actions_in_task.reject_task(task['syncToken'], task['id'])

        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user09')

        # Инициатор аппелирует
        task = self.APP.api_actions_in_task.appeal_task(task['syncToken'], task['id'])

        # Получаем список всех согласующих
        approvers_id = self.list_id_all_approver(task['agreements'])

        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']
        assert self.APP.group_data.users['test_Boss02']['user_id'] in approvers_id

    @allure.title('Первый согласующий согласовывает, второй отклоняет')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_reject_after_agree(self):

        # Создаем задачу
        task = self.create_task({'approvers': ['test_user05', 'test_user06']})

        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user05')

        # Согласуем задачу
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])

        # Перелогиниваемся на второго согласующего
        self.APP.api_token.get_token('test_user06')

        # Согласующий отклоняет задачу
        task = self.APP.api_actions_in_task.reject_task(task['syncToken'], task['id'])

        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['Отклонено']

    @allure.title('Подчинённый согласовывает, начальник отклоняет')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_subordinate_agree_manger_reject(self):

        # Создаем задачу
        task = self.create_task({'approvers': ['test_user07', 'test_Boss03']})

        # Перелогиниваемся на подчинённого
        self.APP.api_token.get_token('test_user07')

        # Согласуем задачу
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])

        # Перелогиниваемся на начальника
        self.APP.api_token.get_token('test_Boss03')

        # Согласующий отклоняет задачу
        task = self.APP.api_actions_in_task.reject_task(task['syncToken'], task['id'])

        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['Отклонено']

    @allure.title('подчинённый согласовывает, начальник согласовывает, добавляют подчинённого он отклоняет')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_first_subordinate_agree_manger_agree_second_subordinate_reject(self):

        # Создаем задачу
        task = self.create_task({'approvers': ['test_user07', 'test_Boss03']})

        # Перелогиниваемся на подчинённого
        self.APP.api_token.get_token('test_user07')

        # Согласуем задачу
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])

        # Перелогиниваемся на начальника
        self.APP.api_token.get_token('test_Boss03')

        # Согласуем задачу
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])

        # Добавляем подчинённого в согласующих
        task = self.APP.api_actions_in_task.add_agreements_in_task(self.APP.group_data.users['test_Boss02']['user_id'], task['syncToken'], task['id'])

        # Перелогиниваемся на второго подчинённого
        self.APP.api_token.get_token('test_Boss02')

        # Согласующий отклоняет задачу
        task = self.APP.api_actions_in_task.reject_task(task['syncToken'], task['id'])

        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['Отклонено']

    @allure.title(
        'При апелляции вернуть возможность согласовать/отклонить заявку пользователям, которые не принимали решения ранее')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_after_reject(self):

        # Создаем задачу
        task = task = self.create_task({'approvers': ['test_user07', 'test_user04', 'test_user02']})

        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user07')

        # Согласующий отклоняет задачу
        task = self.APP.api_actions_in_task.reject_task(task['syncToken'], task['id'])

        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user09')

        # Инициатор аппелирует
        task = self.APP.api_actions_in_task.appeal_task(task['syncToken'], task['id'])

        # Получаем список всех согласующих
        approvers_id = self.list_id_all_approver(task['agreements'])

        # Сравниваем значения получаемой задачи с ожидаемыми значениями
        assert task['ticketType'] == 'Task'
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']
        assert task['agreements'][1]['status'] == 'Pending'
        assert self.APP.group_data.users['test_Boss03']['user_id'] in approvers_id
        assert self.users['test_user04']['user_id'] in approvers_id
        assert self.APP.group_data.users['test_user07']['user_id'] not in approvers_id

    @allure.title('Добавление пользователя в согласующие с неизвестным id')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_add_approver_with_undefined_approver_id(self):

        # Создаем задачу
        created_task = self.create_task({})

        # Добавляем несуществующего согласующего
        add_aprover = self.APP.api_tasks.post_tasks_id_agreements(created_task['id'], {'approverId': '3fa85f64-5717-4562-b3fc-2c963f66afa6', 'syncToken': created_task['syncToken']})

        assert add_aprover['status'] == 404

    @allure.title('Редактирование чужой задачи')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_add_approver_with_undefined_approver_id(self):

        # Создаем задачу
        created_task = self.create_task({})

        # Переходим на пользователя не присутствующего в задаче
        self.APP.api_token.get_token('test_user01')

        update_task = self.APP.api_actions_in_task.update_task(created_task['syncToken'], created_task['id'], {'title': 'New title task'})

        assert update_task['status'] == 403

