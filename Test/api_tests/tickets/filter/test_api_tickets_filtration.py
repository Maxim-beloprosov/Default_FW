import allure
import pytest
from Test.api_tests.api_base import ApiBase

@allure.feature('Api - Tickets')
@allure.story('Фильтрация тикетов')
class TestApiTickets(ApiBase):

    @allure.title('Фильтрация тикетов по табу "Все" по параметру "На мне"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_ticket_tab_all_on_me(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user05'})

        # Переход на пользователя исполнителя
        self.APP.api_token.get_token('test_user05')

        # Фильтрация по параметру "На мне"
        filter_on_me = self.APP.api_tickets_filtration.filter_tickets_by_tab_all('Mine', created_task['createdDate'], 5)

        # Проверка, является ли test_user05 во всех тикетах исполнителем.
        tickets_on_me = self.filter_find_another_id_response_in_ticket(filter_on_me['items'], 'contractor', self.users['test_user05']['user_id'])

        assert created_task['ticketType'] == 'Task'
        assert tickets_on_me

    @allure.title('Фильтрация тикетов по неопределённому параметру. Таб "Все"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_by_undefined_parameter_tab_all(self):

        # Фильтрация по неопределённому параметру
        filter_on_me = self.APP.api_tickets_filtration.filter_tickets_by_tab_all('Potato', '2000-10-10T00:00:00Z', 5)

        assert filter_on_me['status'] == 400

    @allure.title('Фильтрация тикетов по неопределённому параметру. Таб "Статус"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_by_undefined_parameter_tab_status(self):

        # Фильтрация по неопределённому параметру
        filter_on_me = self.APP.api_tickets_filtration.filter_tickets_by_tab_status('Potato', '2000-10-10T00:00:00Z', 5)

        assert filter_on_me['status'] == 400

    @allure.title('Фильтрация тикетов по неопределённому параметру. Таб "Тип"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_by_undefined_parameter_tab_type(self):

        # Фильтрация по неопределённому параметру
        filter_on_me = self.APP.api_tickets_filtration.filter_tickets_by_tab_ticket_type('Potato', '2000-10-10T00:00:00Z', 5)

        assert filter_on_me['status'] == 400

    @allure.title('Фильтрация тикетов по неопределённому параметру. Таб "Исполнитель"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_by_undefined_parameter_tab_contractor(self):

        # Фильтрация по неопределённому параметру
        filter_on_me = self.APP.api_tickets_filtration.filter_tickets_by_tab_contractor_is_contractor('Potato', '2000-10-10T00:00:00Z', 5)

        assert filter_on_me['status'] == 400

    @allure.title('Фильтрация тикетов по неопределённому параметру. Таб "Статус согласования"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_by_undefined_parameter_tab_agreement_status(self):

        # Фильтрация по неопределённому параметру
        filter_on_me = self.APP.api_tickets_filtration.filter_tickets_by_tab_agreements_status('test_user04', 'Potato', '2000-10-10T00:00:00Z', 5)

        assert filter_on_me['status'] == 400

    @allure.title('Фильтрация тикетов по неопределённому параметру. Таб "Услуга"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_by_undefined_parameter_tab_service(self):

        # Фильтрация по неопределённому параметру
        filter_on_me = self.APP.api_tickets_filtration.filter_tickets_by_tab_service('Potato', '2000-10-10T00:00:00Z', 5)

        assert filter_on_me['status'] == 400

    @allure.title('Фильтрация тикетов по неопределённому параметру. Таб "Дата создания"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_by_undefined_parameter_tab_created_date(self):

        # Фильтрация по неопределённому параметру
        filter_on_me = self.APP.api_tickets_filtration.filter_tickets_by_tab_created_date('Potato', 'Potato', 5)

        assert filter_on_me['status'] == 400

    @allure.title('Фильтрация тикетов по неопределённому параметру. Таб "Дата начала"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_by_undefined_parameter_tab_begin_date(self):

        # Фильтрация по неопределённому параметру
        filter_on_me = self.APP.api_tickets_filtration.filter_tickets_by_tab_begin_date('Potato', 'Potato', '2000-10-10T00:00:00Z', 5)

        assert filter_on_me['status'] == 400

    @allure.title('Фильтрация тикетов по неопределённому параметру. Таб "Дата окончания"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_by_undefined_parameter_tab_end_date(self):

        # Фильтрация по неопределённому параметру
        filter_on_me = self.APP.api_tickets_filtration.filter_tickets_by_tab_created_date('Potato', 'Potato', '2000-10-10T00:00:00Z', 5)

        assert filter_on_me['status'] == 400

    @allure.title('Фильтрация тикетов по неопределённому параметру. Таб "Дата окончания"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_by_undefined_parameter_tab_end_date(self):

        # Фильтрация по неопределённому параметру
        filter_on_me = self.APP.api_tickets_filtration.filter_tickets_by_tab_end_date('Potato', 'Potato', '2000-10-10T00:00:00Z', 5)

        assert filter_on_me['status'] == 400

    @allure.title('Фильтрация тикетов по неопределённому параметру. Таб "Дата закрытия"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_by_undefined_parameter_tab_close_date(self):

        # Фильтрация по неопределённому параметру
        filter_on_me = self.APP.api_tickets_filtration.filter_tickets_by_tab_close_date('Potato', 'Potato', '2000-10-10T00:00:00Z', 5)

        assert filter_on_me['status'] == 400

    params_rating = [
        ['Potato'],
        [4.345],
        [4/15],
        [1, 2, 3, 4, 5, 6],
    ]

    @allure.title('Негативная фильтрация тикетов. Таб "Оценка"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("array_test", params_rating)
    def test_api_filter_tickets_by_uncorrect_param_tab_rating(self, array_test):

        # Фильтрация по некорректным параметрам
        filter = self.APP.api_tickets_filtration.filter_tickets_by_tab_rating(array_test, '2000-10-10T00:00:00Z', 5)

        assert filter['status'] == 400

    @allure.title('Фильтрация тикетов по табу "Все" по параметру "На мне" c кол-вом -1')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_by_tab_all_on_me_with_negative_count(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user05'})

        # Переход на пользователя исполнителя
        self.APP.api_token.get_token('test_user05')

        # Фильтрация по параметру "На мне"
        filter_on_me = self.APP.api_tickets_filtration.filter_tickets_by_tab_all('Mine', '2000-10-10T00:00:00Z', -1)

        assert filter_on_me['status'] == 400

    @allure.title('Фильтрация тикетов по табу "Все" по параметру "На подчинённых"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_tab_all_on_my_subordinates(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_Boss02'})

        # Переход за пользователя-руководителя исполнителя BossThree
        self.APP.api_token.get_token('test_Boss03')

        # Фильтрация по параметру "На подчинённых"
        filter_on_my_subordinates = self.APP.api_tickets_filtration.filter_tickets_by_tab_all('Subordinates', created_task['createdDate'], 5)

        # Подготовка переменых для проверки правильности фильтрации
        list_my_subordinates_id = []

        # Получение id всех подчинённых
        for items in self.APP.api_users.get_users_profile_subordinate()['items']:
            list_my_subordinates_id.append(items['id'])

        # Проверка, что хотя бы один из подчинённых находится в тикете на любой роли или в ГО
        ticket_temp = None
        for items in filter_on_my_subordinates['items']:
            list_users_id = self.output_all_users_id_in_ticket(items['id'], items['ticketType'])
            result = list(set(list_my_subordinates_id) & set(list_users_id))
            if len(result) > 0:
                ticket_temp = True
            else:
                ticket_temp = False
                break

        assert created_task['ticketType'] == 'Task'
        assert ticket_temp

    @allure.title('Фильтрация тикетов по табу "Тип" по параметру "Заявка"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_request_tab_type_param_request(self):

        # Создание заявки
        created_request = self.create_tickets({}, ticket_type='request')

        # Фильтрация по параметру "Заявка"
        filter_request = self.APP.api_tickets_filtration.filter_tickets_by_tab_ticket_type('request', created_request['createdDate'], 5)

        # Проверка остались ли после фильтрации только Заявки
        tickets_type_request = self.filter_find_another_response_in_ticket(filter_request['items'], 'ticketType', 'request')

        assert created_request['ticketType'] == 'request'
        assert tickets_type_request

    @allure.title('Фильтрация тикетов по табу "Тип" по параметру "Задача"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_request_tab_type_param_task(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user09'})

        # Фильтрация по параметру "Заявка"
        filter_task = self.APP.api_tickets_filtration.filter_tickets_by_tab_ticket_type('Task', created_task['createdDate'], 5)

        # Проверка остались ли после фильтрации только Задачи
        tickets_type_task = self.filter_find_another_response_in_ticket(filter_task['items'], 'ticketType', 'Task')

        assert created_task['ticketType'] == 'Task'
        assert tickets_type_task

    @allure.title('Фильтрация тикетов по табу "Статус" по параметру "В работе"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_tab_status_param_active(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user09'})

        # Фильтрация по параметру "Закрыта"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_status(self.status_ticket['ENG']['В работе'], created_task['createdDate'], 5)

        # Проверка остались ли после фильтрации тикеты только в статусе "В работе"
        tickets_status_active = self.filter_find_another_response_in_ticket(filter_tickets['items'], 'status', self.status_ticket['ENG']['В работе'])

        assert created_task['ticketType'] == 'Task'
        assert tickets_status_active

    @allure.title('Фильтрация тикетов по табу "Статус" по параметру "В проверке"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933')
    def test_api_filter_tickets_tab_status_param_resolved(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user09', 'approvers': ['test_user05']})

        # Переход на пользователя-согласующего
        self.APP.api_token.get_token('test_user05')

        # Согласуем задачу
        agreement_task = self.APP.api_actions_in_task.approve_task(created_task['syncToken'], created_task['id'])

        # Переход на пользователя-инициатора
        self.APP.api_token.get_token('test_user09')

        # Отправка задачи на проверку
        resolved_task = self.APP.api_actions_in_task.resolve_task(agreement_task['syncToken'], agreement_task['id'])

        # Фильтрация по параметру "В проверке"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_status(self.status_ticket['ENG']['В проверке'],
                                                                                      created_task['createdDate'], 5)

        # Проверка остались ли после фильтрации тикеты только в статусе "В проверке"
        tickets_status_resolved = self.filter_find_another_response_in_ticket(filter_tickets['items'], 'status', self.status_ticket['ENG']['В проверке'])

        assert created_task['ticketType'] == 'Task'
        assert created_task['agreements'][0]['id'] == self.users['test_user05']['user_id']
        assert tickets_status_resolved

    @allure.title('Фильтрация тикетов по табу "Статус" по параметру "Отменено"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason="Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933")
    def test_api_filter_tickets_tab_status_param_canceled(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user09', 'approvers': ['test_user05']})

        # Отправка задачи в статус "Отменено"
        canceled_task = self.APP.api_actions_in_task.cancel_task(created_task['syncToken'], created_task['id'])

        # Фильтрация по параметру "Отменено"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_status(self.status_ticket['ENG']['Отменено'],
                                                                                      created_task['createdDate'], 5)

        # Проверка остались ли после фильтрации тикеты только в статусе "Отменено"
        tickets_status_canceled = self.filter_find_another_response_in_ticket(filter_tickets['items'], 'status', self.status_ticket['ENG']['Отменено'])

        assert created_task['ticketType'] == 'Task'
        assert created_task['agreements'][0]['id'] == self.users['test_user05']['user_id']
        assert tickets_status_canceled

    @allure.title('Фильтрация тикетов по табу "Статус" по параметру "В ожидании"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_tab_status_param_waiting(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user09', 'beginDate': 1})

        # Фильтрация по параметру "В ожидании"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_status(self.status_ticket['ENG']['В ожидании'],
                                                                                      created_task['createdDate'], 5)

        # Проверка остались ли после фильтрации тикеты только в статусе "В ожидании"
        tickets_status_waiting = self.filter_find_another_response_in_ticket(filter_tickets['items'], 'status', self.status_ticket['ENG']['В ожидании'])

        assert created_task['ticketType'] == 'Task'
        assert tickets_status_waiting

    @allure.title('Фильтрация тикетов по табу "Статус" по параметру "В ожидании предшественника"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Не меняется статус проекта при добавлении зависимой строчки проекта.')
    def test_api_filter_tickets_tab_status_param_waiting_previous(self):

        # Создание задачи #1
        created_task_one = self.create_task({'contractorId': 'test_user09'})

        # Создание задачи #2
        created_task_two = self.create_task({'contractorId': 'test_user09'})

        # Добавление задачи предшественника
        added_previous_task = self.APP.api_actions_in_task.add_previous_to_task(created_task_one['id'], created_task_two['id'])

        # Фильтрация по параметру "В ожидании предшественника"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_status(self.status_ticket['ENG']['В ожидании предшественника'], created_task_one['createdDate'], 5)

        # Проверка остались ли после фильтрации тикеты только в статусе "В ожидании предшественника"
        tickets_status_waiting_prev = self.filter_find_another_response_in_ticket(filter_tickets['items'], 'status', self.status_ticket['ENG']['В ожидании предшественника'])

        assert created_task_one['ticketType'] == 'Task'
        assert created_task_one['contractors'][0]['id'] == self.users['test_user09']['user_id']
        assert created_task_two['ticketType'] == 'Task'
        assert created_task_two['contractors'][0]['id'] == self.users['test_user09']['user_id']
        assert tickets_status_waiting_prev

    @allure.title('Фильтрация тикетов по табу "Статус" по параметру "Отклонено"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason="Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933")
    def test_api_filter_tickets_tab_status_param_rejected(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user09', 'approvers': ['test_user05']})

        # Переход за пользователя-согласующиего
        self.APP.api_token.get_token('test_user05')

        # Отклоняем задачу
        rejected_task = self.APP.api_actions_in_task.reject_task(created_task['syncToken'], created_task['id'])

        # Фильтрация по параметру "Отклонено"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_status(self.status_ticket['ENG']['Отклонено'], created_task['createdDate'], 5)

        # Проверка остались ли после фильтрации тикеты только в статусе "отклонено"
        tickets_status_rejected = self.filter_find_another_response_in_ticket(filter_tickets['items'], 'status', self.status_ticket['ENG']['Отклонено'])

        assert created_task['ticketType'] == 'Task'
        assert created_task['agreements'][0]['id'] == self.users['test_user05']['user_id']
        assert tickets_status_rejected

    @allure.title('Фильтрация тикетов по табу "Статус" по параметру "На согласовании"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason="Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933")
    def test_api_filter_tickets_tab_status_param_agreement(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user09', 'approvers': ['test_user05']})

        # Фильтрация по параметру "На согласовании"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_status(self.status_ticket['ENG']['На согласовании'],
                                                                                      created_task['createdDate'], 5)

        # Проверка остались ли после фильтрации тикеты только в статусе "На согласовании"
        tickets_status_agreement = self.filter_find_another_response_in_ticket(filter_tickets['items'], 'status', self.status_ticket['ENG']['На согласовании'])

        assert created_task['ticketType'] == 'Task'
        assert created_task['agreements'][0]['id'] == self.users['test_user05']['user_id']
        assert tickets_status_agreement

    @allure.title('Фильтрация тикетов по табу "Статус" по параметру "На уточнении у инициатора"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Нет возможности задавать вопрос-уточнение в проектах')
    def test_api_filter_tickets_tab_status_param_initiator_clarification(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user09', 'approvers': ['test_user05']})

        # Переход за пользователя-согласующего
        self.APP.api_token.get_token('test_user05')

        # Задаём вопрос-уточнение инициатору
        clarification_ticket = self.APP.api_actions_in_task.clarification_ask_to_initiator_in_task(created_task['syncToken'], created_task['id'])

        # Фильтрация по параметру "На уточнении у иниц."
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_status(self.status_ticket['ENG']['На уточнении у иниц.'],
                                                                                      created_task['createdDate'], 5)

        # Проверка остались ли после фильтрации тикеты только в статусе "На уточнении у иниц."
        tickets_status_clarification = self.filter_find_another_response_in_ticket(filter_tickets['items'], 'status', self.status_ticket['ENG']['На уточнении у иниц.'])

        assert created_task['ticketType'] == 'Task'
        assert created_task['agreements'][0]['id'] == self.users['test_user05']['user_id']
        assert tickets_status_clarification

    @allure.title('Фильтрация тикетов по табу "Статус" по параметру "На уточнении у исполнителя"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Нет возможности задавать вопрос-уточнение в проектах')
    def test_api_filter_tickets_tab_status_param_contractor_clarification(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user09', 'approvers': ['test_user05']})

        # Переход за пользователя-согласующего
        self.APP.api_token.get_token('test_user05')

        # Задаём вопрос-уточнение исполнителя
        clarification_ticket = self.APP.api_actions_in_task.clarification_ask_to_contractor_in_task(created_task['syncToken'], created_task['id'])

        # Фильтрация по параметру "На уточнении у исп."
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_status(self.status_ticket['ENG']['На уточнении у исп.'], created_task['createdDate'], 5)

        # Проверка остались ли после фильтрации тикеты только в статусе "На уточнении у исп."
        tickets_status_clarification = self.filter_find_another_response_in_ticket(filter_tickets['items'], 'status', self.status_ticket['ENG']['На уточнении у исп.'])

        assert created_task['ticketType'] == 'Task'
        assert created_task['agreements'][0]['id'] == self.users['test_user05']['user_id']
        assert tickets_status_clarification

    @allure.title('Фильтрация тикетов по табу "Статус" по параметру "Закрыта"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_tab_status_param_closed(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user08'})

        # Переходим за пользователя-исполнителя
        self.APP.api_token.get_token('test_user08')

        # Отправка задачи на проверку
        resolved_task = self.APP.api_actions_in_task.resolve_task(created_task['syncToken'], created_task['id'])

        # Переходим на пользователя-инициатора
        self.APP.api_token.get_token('test_user09')

        # Закрытие задачи
        close_task = self.APP.api_actions_in_task.close_task(5, resolved_task['syncToken'], resolved_task['id'])

        # Фильтрация по параметру "Закрыта"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_status(self.status_ticket['ENG']['Закрыта'], created_task['createdDate'], 5)

        # Проверка остались ли после фильтрации тикеты только в статусе "Закрыта"
        tickets_status_closed = self.filter_find_another_response_in_ticket(filter_tickets['items'], 'status', self.status_ticket['ENG']['Закрыта'])

        assert created_task['ticketType'] == 'Task'
        assert tickets_status_closed

    @allure.title('Фильтрация тикетов по табу "Услуга" с одной выбранной услугой')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_tab_service(self):

        # Создание заявки
        created_request = self.create_tickets({}, ticket_type='request')

        # Фильтрация по параметру "Услуга"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_service(created_request['gandivaService']['id'], created_request['createdDate'], 5)

        # Проверка остались ли после фильтрации тикеты только в с определённой услугой
        tickets_equal_id_service = self.filter_find_another_id_response_in_ticket(filter_tickets['items'], 'gandivaService', created_request['gandivaService']['id'])

        assert created_request['ticketType'] == 'request'
        assert tickets_equal_id_service

    @allure.title('Фильтрация тикетов по табу "Дата создания"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_tab_created_date(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user08'})

        # Подготовка переменных для фильтрации по дате
        createdDateFrom = self.APP.time.get_date_increased_x_days_json(-1)
        createdDateTo = self.APP.time.get_date_increased_x_days_json(1)

        # Фильтрация по параметру "Дата создания"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_created_date(createdDateFrom, createdDateTo, 5)

        # Проверка лежит ли "Дата создания" тикетов в промежутке +-1го дня.
        response_tickets_in_correct_datetime_range = self.filter_within_the_time_range(filter_tickets['items'], 'createdDate', createdDateFrom, createdDateTo)

        assert created_task['ticketType'] == 'Task'
        assert response_tickets_in_correct_datetime_range

    @allure.title('Фильтрация тикетов по табу "Дата начала"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_tab_begin_date(self):

        # Создание задачи
        created_task = self.create_task({"contractorId": 'test_user06', 'beginDate': 1, 'endDate': 2})

        # Подготовка переменных для фильтрации по дате
        beginDateFrom = self.APP.time.get_date_increased_x_days_json(-2)
        beginDateTo = self.APP.time.get_date_increased_x_days_json(2)

        # Фильтрация по параметру "Дата начала"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_begin_date(beginDateFrom, beginDateTo, created_task['createdDate'], 5)

        # Проверка лежат ли "Дата начала" тикетов в промежутке +-2х дней.
        response_tickets_in_correct_datetime_range = self.filter_within_the_time_range(filter_tickets['items'], 'beginDate', beginDateFrom, beginDateTo)

        assert created_task['ticketType'] == 'Task'
        assert response_tickets_in_correct_datetime_range

    @allure.title('Фильтрация тикетов по табу "Дата окончания"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_tab_end_date(self):

        # Создание задачи
        created_task = self.create_task({"contractorId": 'test_user06',  "endDate": 0.1})

        # Подготовка переменных для фильтрации по дате
        endDateFrom = self.APP.time.get_date_increased_x_days_json(-1)
        endDateTo = self.APP.time.get_date_increased_x_days_json(1)

        # Фильтрация по параметру "Дата окончания"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_end_date(endDateFrom, endDateTo, created_task['createdDate'], 5)

        # Проверка лежат ли "Дата окончания" тикетов в промежутке +-1 дня.
        response_tickets_in_correct_datetime_range = self.filter_within_the_time_range(filter_tickets['items'], 'endDate', endDateFrom, endDateTo)

        assert created_task['ticketType'] == 'Task'
        assert response_tickets_in_correct_datetime_range

    @allure.title('Фильтрация тикетов по табу "Дата закрытия"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_tab_close_date(self):

        # Создание задачи
        created_task = self.create_task({"contractorId": 'test_user08'})

        # Переходим за пользователя-исполнителя
        self.APP.api_token.get_token('test_user08')

        # Отправка задачи на проверку
        resolved_task = self.APP.api_actions_in_task.resolve_task(created_task['syncToken'], created_task['id'])

        # Переходим на пользователя-инициатора
        self.APP.api_token.get_token('test_user09')

        # Отправка задачи в статус "Закрыта"
        close_task = self.APP.api_actions_in_task.close_task(5, resolved_task['syncToken'], resolved_task['id'])

        # Подготовка переменных для фильтрации по параметру "Дата закрытия"
        closingDateFrom = self.APP.time.get_date_increased_x_days_json(-1)
        closingDateTo = self.APP.time.get_date_increased_x_days_json(1)

        # Фильтрация по параметру "Дата закрытия"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_close_date(closingDateFrom, closingDateTo, created_task['createdDate'], 5)

        # Проверка лежат ли "Дата закрытия" тикетов в промежутке +-1 дня
        response_tickets_in_correct_datetime_range = self.filter_within_the_time_range(filter_tickets['items'], 'closingFactualExecutionDate', closingDateFrom, closingDateTo)

        assert created_task['ticketType'] == 'Task'
        assert response_tickets_in_correct_datetime_range

    @allure.title('Фильтрация тикетов по табу "Оценка"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_tab_ratings(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user05'})

        # Переход на пользователя-исполнителя
        self.APP.api_token.get_token('test_user05')

        # Отправка задачи на проверку
        resolved_task = self.APP.api_actions_in_task.resolve_task(created_task['syncToken'], created_task['id'])

        # Переход на пользователя-инициатора
        self.APP.api_token.get_token('test_user09')

        # Закрытие задачи
        close_task = self.APP.api_actions_in_task.close_task(4, resolved_task['syncToken'], resolved_task['id'])

        # Фильтрация по параметру "Оценка"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_rating([4], created_task['createdDate'], 5)

        # Проверка остались ли после фильтрации тикеты только с "Оценкой" - 4
        response_rating_tickets_4 = self.filter_find_another_response_in_ticket(filter_tickets['items'], 'rating', 4)

        assert created_task['ticketType'] == 'Task'
        assert response_rating_tickets_4

    @allure.title('Фильтрация тикетов по табу "Инициатор"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_tab_initiator(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user05'})

        # Фильтрация по параметру "Инициатор"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_initiator('test_user09', created_task['createdDate'], 5)

        # Проверка, что после фильтрации все тикеты будут с инициатором test_user09
        response_initiator_in_ticket = self.filter_find_another_id_response_in_ticket(filter_tickets['items'], 'initiator', self.users['test_user09']['user_id'])

        assert created_task['ticketType'] == 'Task'
        assert response_initiator_in_ticket

    @allure.title('Фильтрация тикетов по табу "Исполнитель" по параметру "Без исполнителя"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_tab_contractor_without_contractor(self):

        # Создание заявки
        created_request = self.create_tickets({}, ticket_type='request')

        # Фильтрация по параметру "Без исполнителя"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_contractor_is_contractor(False, created_request['createdDate'], 5)

        # Проверка отсутствует ли поле с исполнителем в json фильтрации
        tickets_not_have_contractor = self.filter_response_not_have_element_in_json(filter_tickets['items'], 'contractor')

        assert created_request['ticketType'] == 'request'
        assert tickets_not_have_contractor

    @allure.title('Фильтрация тикетов по табу "Исполнитель" по параметру "С исполнителем"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_tab_contractor_with_contractor(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user05'})

        # Фильтрация по параметру "С исполнителем"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_contractor_is_contractor(True, created_task['createdDate'], 5)

        # Проверка присутствует ли поле с исполнителем в json фильтрации
        tickets_have_contractor = self.filter_response_have_element_in_json(filter_tickets['items'], 'contractor')

        assert created_task['ticketType'] == 'Task'
        assert tickets_have_contractor

    @allure.title('Фильтрация тикетов по табу "Исполнитель" по id исполнителя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_tab_contractor_by_contractor_id(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user05'})

        # Фильтрация по id исполнителя
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_contractor_id_contractor('test_user05', created_task['createdDate'], 5)

        # Проверка, что исполнитель с таким id присутствует в тикетах
        response_contractor_in_ticket = self.filter_find_another_id_response_in_ticket(filter_tickets['items'], 'contractor', self.users['test_user05']['user_id'])

        assert created_task['ticketType'] == 'Task'
        assert response_contractor_in_ticket

    @allure.title('Фильтрация тикетов по табу "Группа ответственности"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_tab_responsibility_group(self):

        # Создание заявки
        created_request = self.create_tickets({}, ticket_type='request')

        # Фильтрация по табу "Группа ответственности"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_responsibility_group(created_request['responsibilityGroup']['id'], created_request['createdDate'], 5)

        # Проверка, что все тикеты имеют нужную группу ответственности
        all_tickets_have_correct_responsibility_group = self.filter_correct_responsibility_group(filter_tickets['items'], created_request['responsibilityGroup']['id'])

        assert created_request['ticketType'] == 'request'
        assert all_tickets_have_correct_responsibility_group

    @allure.title('Фильтрация тикетов по табу "Согласующие"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason="Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933")
    def test_api_filter_tickets_tab_approver(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user05', 'approvers': ['test_user04']})

        # Фильтрация по согласующим
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_approver('test_user04', created_task['createdDate'], 5)

        # Проверка, что согласующий с таким id присутствует в тикете
        response_current_approver_in_tickets = self.filter_have_current_user_in_role_approver(filter_tickets['items'], 'test_user04')

        assert created_task['ticketType'] == 'Task'
        assert created_task['approvers'][0]['id'] == self.users['test_user04']['user_id']
        assert response_current_approver_in_tickets

    @allure.title('Фильтрация тикетов по табу "Статус согласования" по параметру "Ожидание принятия решений"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason="Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933")
    def test_api_filter_tickets_tab_agreement_statuse_param_pending(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user05', 'approvers': ['test_user04']})

        # Фильтрация по "Ожидание принятия решений"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_agreements_status('test_user04', 'Pending', created_task['createdDate'], 5)

        # Проверка, что все тикеты находяться в статусе согласования: "Ожидание принятия решения"
        response_all_tickets_in_agreement_statuse_pending = self.filter_find_approver_with_agreement_status(filter_tickets['items'], 'Pending', 'test_user04')

        assert created_task['ticketType'] == 'Task'
        assert created_task['agreements'][0]['approver']['id'] == self.users['test_user04']['user_id']
        assert response_all_tickets_in_agreement_statuse_pending

    @allure.title('Фильтрация тикетов по табу "Статус согласования" по параметру "На уточнении"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Нет возможности задать вопрос уточнение')
    def test_api_filter_tickets_tab_agreement_statuse_param_clarification(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user05', 'approvers': ['test_user04']})

        # Переход на пользователя-согласующего
        self.APP.api_token.get_token('test_user04')

        # Задание вопроса-уточнения инициатору
        clarification_task = self.APP.api_actions_in_task.clarification_ask_to_initiator_in_task(created_task['syncToken'], created_task['id'])

        # Фильтрация по "На уточнении"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_agreements_status('test_user04', 'Clarification', created_task['createdDate'], 5)

        # Проверка, что все тикеты находяться в статусе согласования: "На уточнении"
        response_all_tickets_in_agreement_status_clarification = self.filter_find_approver_with_agreement_status(filter_tickets['items'], 'Clarification', 'test_user04')

        assert created_task['ticketType'] == 'Task'
        assert created_task['agreements'][0]['approver']['id'] == self.users['test_user04']['user_id']
        assert response_all_tickets_in_agreement_status_clarification

    @allure.title('Фильтрация тикетов по табу "Статус согласования" по параметру "Согласовано"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason="Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933")
    def test_api_filter_tickets_tab_agreement_statuse_param_approved(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user05', 'approvers': ['test_user04']})

        # Переход на пользователя-согласующего
        self.APP.api_token.get_token('test_user04')

        # Согласовать задачу
        approved_task = self.APP.api_actions_in_task.approve_task(created_task['syncToken'], created_task['id'])

        # Фильтрация по "Согласовано"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_agreements_status('test_user04', 'Approved', created_task['createdDate'], 5)

        # Проверка, что все тикеты находяться в статусе согласования: "Согласовано"
        response_all_tickets_in_agreement_status_approved = self.filter_find_approver_with_agreement_status(
            filter_tickets['items'], 'Approved', 'test_user04')

        assert created_task['ticketType'] == 'Task'
        assert created_task['agreements'][0]['approver']['id'] == self.users['test_user04']['user_id']
        assert response_all_tickets_in_agreement_status_approved

    @allure.title('Фильтрация тикетов по табу "Статус согласования" по параметру "Согласовано руководителем"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason="Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933")
    def test_api_filter_tickets_tab_agreement_statuse_param_approved_by_manager(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user05', 'approvers': ['test_Boss02', 'test_Boss03']})

        # Переход на пользователя-согласующего, руководителя test_Boss02
        self.APP.api_token.get_token('test_Boss03')

        # Согласовать задачу
        approved_task = self.APP.api_actions_in_task.approve_task(created_task['syncToken'], created_task['id'])

        # Фильтрация по "Согласовано руководителем"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_agreements_status('test_Boss02', 'ApprovedByManager', created_task['createdDate'], 5)

        # Проверка, что все тикеты находяться в статусе согласования: "Согласовано руководителем"
        response_all_tickets_in_agreement_status_approved_by_manager = self.filter_find_approver_with_agreement_status(
            filter_tickets['items'], 'ApprovedByManager', 'test_Boss02')

        # Получаем список всех согласующих
        list_approvers = self.list_id_all_approver(created_task['agreements'])

        assert created_task['ticketType'] == 'Task'
        assert self.users['test_Boss02']['user_id'] in list_approvers
        assert self.users['test_Boss03']['user_id'] in list_approvers
        assert response_all_tickets_in_agreement_status_approved_by_manager

    @allure.title('Фильтрация тикетов по табу "Статус согласования" по параметру "Отклонено"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason="Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933")
    def test_api_filter_tickets_tab_agreement_statuse_param_rejected(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user05', 'approvers': ['test_user04']})

        # Переход на пользователя-согласующего
        self.APP.api_token.get_token('test_user04')

        # Отклоням задачу
        rejected_task = self.APP.api_actions_in_task.reject_task(created_task['syncToken'], created_task['id'])

        # Фильтрация по "Отклонено"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_agreements_status('test_user04', 'Rejected', created_task['createdDate'], 5)

        # Проверка, что все тикеты находяться в статусе согласования: "Отклонено"
        response_all_tickets_in_agreement_status_rejected = self.filter_find_approver_with_agreement_status(
            filter_tickets['items'], 'Rejected', 'test_user04')

        assert created_task['ticketType'] == 'Task'
        assert created_task['agreements'][0]['approver']['id'] == self.users['test_user04']['user_id']
        assert response_all_tickets_in_agreement_status_rejected

    @allure.title('Фильтрация тикетов по табу "Статус согласования" по параметру "Отклонено руководителем"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason="Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933")
    def test_api_filter_tickets_tab_agreement_statuse_param_rejected_by_manager(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user05', 'approvers': ['test_Boss02', 'test_Boss03']})

        # Переход на пользователя-согласующего, руководителя test_Boss02
        self.APP.api_token.get_token('test_Boss03')

        # Отклоням задачу
        rejected_task = self.APP.api_actions_in_task.reject_task(created_task['syncToken'], created_task['id'])

        # Фильтрация по "Отклонено руководителем"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_agreements_status('test_Boss02', 'RejectedByManager', created_task['createdDate'], 5)

        # Проверка, что все тикеты находяться в статусе согласования: "Отклонено руководителем"
        response_all_tickets_in_agreement_status_rejected_by_manager = self.filter_find_approver_with_agreement_status(
            filter_tickets['items'], 'RejectedByManager', 'test_Boss02')

        # Получаем список всех согласующих
        list_approvers = self.list_id_all_approver(created_task['agreements'])

        assert created_task['ticketType'] == 'Task'
        assert self.users['test_Boss02']['user_id'] in list_approvers
        assert self.users['test_Boss03']['user_id'] in list_approvers
        assert response_all_tickets_in_agreement_status_rejected_by_manager

    @allure.title('Фильтрация тикетов по табу "Статус согласования" по параметру "Отменено"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason="Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933")
    def test_api_filter_tickets_tab_agreement_statuse_param_canceled(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user05', 'approvers': ['test_user04', 'test_user06']})

        # переход на пользователя согласующего
        self.APP.api_token.get_token('test_user06')

        # Отклонить задачу за одного из согласующих
        rejected_task = self.APP.api_actions_in_task.reject_task(created_task['syncToken'], created_task['id'])

        # Фильтрация по "Отменено"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_agreements_status('test_user04', 'Canceled', created_task['createdDate'], 5)

        # Проверка, что во всех тикетах находяться пользователи в статусе согласования: "Отменено"
        response_all_tickets_in_agreement_status_canceled = self.filter_find_approver_with_agreement_status(
            filter_tickets['items'], 'Canceled', 'test_user04')

        # Получаем список всех согласующих
        list_approvers = self.list_id_all_approver(created_task['agreements'])

        assert created_task['ticketType'] == 'Task'
        assert self.users['test_user04']['user_id'] in list_approvers
        assert self.users['test_user06']['user_id'] in list_approvers
        assert response_all_tickets_in_agreement_status_canceled

    @allure.title('Фильтрация тикетов по табу "Статус согласования" по параметру "Делегировано"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason="Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933")
    def test_api_filter_tickets_tab_agreement_statuse_param_delegated_to_my_subordinates(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_Boss03', 'approvers': ['test_Boss02']})

        # Переходим на пользователя-согласующего
        self.APP.api_token.get_token('test_Boss02')

        # Делегирование задачи
        delegate_agreement_task = self.APP.api_actions_in_task.delegate_agreement_in_task(created_task['syncToken'], created_task['id'], 'test_user05')

        # Фильтрация по "Делегировано"
        filter_tickets = self.APP.api_tickets_filtration.filter_tickets_by_tab_agreements_status('test_Boss02', 'Delegated', created_task['createdDate'], 5)

        # Проверка, что все тикеты находяться в статусе согласования: "Делегировано"
        response_all_tickets_in_agreement_status_delegated = self.filter_find_approver_with_agreement_status(
            filter_tickets['items'], 'Delegated', 'test_Boss02')

        list_approvers = self.list_id_all_approver(delegate_agreement_task['agreements'])

        assert created_task['ticketType'] == 'Task'
        assert self.users['test_user05']['user_id'] in list_approvers
        assert self.users['test_Boss02']['user_id'] in list_approvers
        assert response_all_tickets_in_agreement_status_delegated

    @allure.title('Фильтрация тикетов без авторизации')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ApiTest
    def test_api_filter_tickets_with_non_authorization_in_gandiva(self):

        # Деавторизируемся
        self.APP.settings.Authorization = False

        # Фильтрация по параметру "На мне"
        filter_on_me = self.APP.api_tickets_filtration.filter_tickets_by_tab_all('Mine', '2000-10-10T00:00:00Z', 100)

        assert filter_on_me.status_code == 401

