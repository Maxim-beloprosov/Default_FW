import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Request')
@allure.story('Простые и сложные согласования"')
class TestApiAgreementsInTheRequest(ApiBase):

    @allure.title('Один согласующий, согласует положительно.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_first(self):
        # Создаем заявку с согласующим
        request = self.create_request({'approvers': ['test_Boss03']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_Boss03')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Два согласующих, один согласует.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_second(self):
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({'approvers': ['test_user01', 'test_user02']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Согласованная заявка переходит в статус "В работе"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_third(self):
        # Создаем заявку с согласующим
        request = self.create_request({'approvers': ['test_user01']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Один согласующий, отклоняет заявку.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_fourth(self):
        # Создаем заявку с согласующим
        request = self.create_request({'approvers': ['test_user01']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['Отклонено']

    @allure.title('Согласующие подчиненный и начальник. Подчиненный отклоняет.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_fifth(self):
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({'approvers': ['test_Boss01', 'test_Boss02']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_Boss01')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Согласующие подчиненный и начальник. Подчиненный отклоняет, начальник согласует.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_sixth(self):
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({'approvers': ['test_Boss01', 'test_Boss02']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_Boss01')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Перелогиниваемся на согласующего - начальника
        self.APP.api_token.get_token('test_Boss02')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Согласующий отклоняет, инициатор апеллирует.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_seventh(self):
        # Создаем заявку с согласующим
        request = self.create_request({'approvers': ['test_Boss01']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_Boss01')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user09')
        # Апеллируем
        request = self.APP.api_actions_in_request.appeal_request(request['syncToken'], request['id'])
        # Формируем список id всех согласующих
        approvers_id = self.list_id_all_approver(request)
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']
        assert self.APP.group_data.users['test_Boss02']['user_id'] in approvers_id

    @allure.title('Два равноправных согласующих. Первый согласует, второй отклоняет.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_eighth(self):
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({'approvers': ['test_user01', 'test_user02']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Перелогиниваемся на другого согласующего
        self.APP.api_token.get_token('test_user02')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['Отклонено']

    @allure.title('Два согласующих: подчиненный - начальник. подчиненный согласует, начальник отклоняет.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_ninth(self):
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({'approvers': ['test_Boss01', 'test_Boss02']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_Boss01')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Перелогиниваемся на начальника
        self.APP.api_token.get_token('test_Boss02')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['Отклонено']

    @allure.title('Два согласующих: подчиненный - начальник. подчиненный и начальник согласуют, добавляется подчиненный - он отклоняет')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_tenth(self):
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({'approvers': ['test_user01', 'test_Boss01']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Перелогиниваемся на начальника
        self.APP.api_token.get_token('test_Boss01')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_user02')
        # Перелогиниваемся на добавленного пользователя
        self.APP.api_token.get_token('test_user02')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['Отклонено']

    @allure.title('Проверка возможности согласования пользователей, не принимавших решение ранее при апелляции (При согласовании типа "подчиненный-начальник")')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_agreements_in_the_request_eleventh(self):
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({'approvers': ['test_user01', 'test_Boss01']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_Boss01')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user09')
        # Апеллируем
        request = self.APP.api_actions_in_request.appeal_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']
        assert len(request['agreements']) == 2
        assert self.APP.group_data.users['test_user01']['user_id'] in self.APP.api_change_request.get_list_id_all_approvers(request['agreements'])
        assert self.APP.api_change_request.get_user_agreement_status_in_request(request['agreements'],
                                                                                    self.APP.group_data.users['test_user01']['user_id']) == 'Pending'

    @allure.title('Согласующие подчиненный и начальник начальника. Подчиненный отклоняет, начальник согласует.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/17325', name='Back. ЗЯ. ЗД. Согл. Не работает иерархическое согласование с руководителем руководителя.')
    @pytest.mark.skip(reason='Иерархическое согласование с руководителем руководителя не работает.')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_api_agreements_in_the_request_twelfth(self):
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({'approvers': ['test_user01', 'test_Boss01']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Перелогиниваемся на согласующего - начальника
        self.APP.api_token.get_token('test_Boss02')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Согласующие: подчиненный и начальник, начальник начальника. Начальник отклоняет.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_thirteenth(self):
        # Создаем заявку с 3-мя согласующими
        request = self.create_request({'approvers': ['test_user01', 'test_Boss01', 'test_Boss02']})
        # Перелогиниваемся на начальника
        self.APP.api_token.get_token('test_Boss01')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']
        assert request['agreements'][0]['status'] == 'Pending'
        assert request['agreements'][1]['status'] == 'Rejected'
        assert request['agreements'][2]['status'] == 'RejectedByManager'

    @allure.title('Согласующие: подчиненный и начальник, начальник начальника. Начальник согласует.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_fourteenth(self):
        # Создаем заявку с 3-мя согласующими
        request = self.create_request({'approvers': ['test_user01', 'test_Boss01', 'test_Boss02']})
        # Перелогиниваемся на начальника
        self.APP.api_token.get_token('test_Boss01')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Повторное согласование, добавляется подчиненный, отклоняет.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_sixteenth(self):
        # Создаем заявку с согласующим
        request = self.create_request({'approvers': [ 'test_Boss01']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_Boss01')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_user01')
        # Перелогиниваемся на согласующего-подчиненного
        self.APP.api_token.get_token('test_user01')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['Отклонено']

    @allure.title('При смене норматива должны остаться согласующие, которые еще не приняли решение.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_seventeenth(self):
        # Логинимся под участником группы ответственности
        self.APP.api_token.get_token('test_user03')
        # Создаем заявку с согласующим
        request = self.create_request({'approvers': ['test_user01']})
        # Ищем нужную услугу
        services = self.APP.api_actions_in_service_catalog.search_service(self.APP.group_data.service_template['AutomationService Тестовый Тип 2']['name'])
        # Меняем услугу
        request = self.APP.api_change_request.change_service_in_request(request['syncToken'], request['id'], services["items"][0]['id'])
        # Формируем список id всех согласующих
        approvers_id = self.list_id_all_approver(request)
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']
        assert self.APP.group_data.users['test_user01']['user_id'] in approvers_id

    @allure.title('При смене норматива должны остаться согласующие, которые уже приняли решение.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_eighteenth(self):
        # Логинимся под участником группы ответственности
        self.APP.api_token.get_token('test_user03')
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({'approvers': ['test_user01', 'test_user02']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Перелогиниваемся обратно на инициатора
        self.APP.api_token.get_token('test_user03')
        # Ищем нужную услугу
        services = self.APP.api_actions_in_service_catalog.search_service(self.APP.group_data.service_template['AutomationService Тестовый Тип 2']['name'])
        # Меняем услугу
        request = self.APP.api_change_request.change_service_in_request(request['syncToken'], request['id'], services["items"][0]['id'])
        # Формируем список id всех согласующих
        approvers_id = self.list_id_all_approver(request)
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']
        assert self.APP.group_data.users['test_user01']['user_id'] in approvers_id

    @allure.title('Апеллирующий = начальнику того, кто отклонил.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_nineteenth(self):
        # Логинимся под участником начальником
        self.APP.api_token.get_token('test_Boss01')
        # Создаем заявку с согласующим
        request = self.create_request({'approvers': ['test_user01']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_Boss01')
        # Апеллируем
        request = self.APP.api_actions_in_request.appeal_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('4 согласующих, 1 отменил. Проверяем, что апелляция отработала корректно.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_twentieth(self):
        # Создаем заявку с 4-мя согласующими
        request = self.create_request({'approvers': ['test_user01', 'test_user05', 'test_user10', 'test_user14']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user05')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user09')
        # Апеллируем
        request = self.APP.api_actions_in_request.appeal_request(request['syncToken'], request['id'])
        # Формируем список id всех согласующих
        approvers_id = self.list_id_all_approver(request)
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']
        assert self.APP.group_data.users['test_user05']['user_id'] not in approvers_id
        assert self.APP.group_data.users['test_Boss02']['user_id'] in approvers_id

    @allure.title('Удаление согласующего при ответе на его запрос уточнения при повторном согласовании')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_twenty_first(self):
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({'approvers': ['test_user01', 'test_user05']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user05')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Перелогиниваемся на второго согласующего
        self.APP.api_token.get_token('test_user01')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Задаем вопрос-уточнение
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user09')
        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_Boss03')
        # Отвечаем на вопрос-уточнение
        request = self.APP.api_clarifications.initiator_to_answer_clarification(request['syncToken'], request['id'], request['clarifications'][0]['id'])
        # Формируем список id всех согласующих
        approvers_id = self.list_id_all_approver(request)
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']
        assert self.APP.group_data.users['test_user05']['user_id'] not in approvers_id
        assert self.APP.group_data.users['test_user01']['user_id'] not in approvers_id

    @allure.title('Согласующие: подчиненный и начальник, подчиненный задал вопрос иниц. и отклонил.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_twenty_second(self):
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({'approvers': ['test_user01', 'test_Boss01']})
        # Перелогиниваемся на согласующего-подчиненного
        self.APP.api_token.get_token('test_user01')
        # Задаем вопрос-уточнение
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Согласующие: подчиненный и начальник, подчиненный задал вопрос исп. и отклонил.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_twenty_third(self):
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({'approvers': ['test_user01', 'test_Boss01']})
        # Перелогиниваемся на согласующего-подчиненного
        self.APP.api_token.get_token('test_user01')
        # Задаем вопрос-уточнение
        request = self.APP.api_clarifications.ask_to_contractor_clarification(request['syncToken'], request['id'])
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']

    @allure.title('Согласующие: подчиненный и начальник, подчиненный задал вопрос исп., начальник согласовал.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_twenty_fourth(self):
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({'approvers': ['test_user01', 'test_Boss01']})
        # Перелогиниваемся на согласующего-подчиненного
        self.APP.api_token.get_token('test_user01')
        # Задаем вопрос-уточнение
        request = self.APP.api_clarifications.ask_to_contractor_clarification(request['syncToken'], request['id'])
        # Перелогиниваемся на согласующего-начальника
        self.APP.api_token.get_token('test_Boss01')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На уточнении у исп.']

    @allure.title(
        'Проверка возможности согласования пользователей, не принимавших решение ранее при апелляции (При равноправных согласующих)')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933', name='API.ЮЗ. Разные статусы у пользователя в разных микросервисах')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах.')
    def test_api_agreements_in_the_request_twenty_fifth(self):
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({'approvers': ['test_user01', 'test_user02']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user02')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user09')
        # Апеллируем
        request = self.APP.api_actions_in_request.appeal_request(request['syncToken'], request['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert request['ticketType'] == 'Request'
        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['На согласовании']
        assert len(request['agreements']) == 2
        assert request['agreements'][1]['approver']['id'] == self.APP.group_data.users['test_user01']['user_id']
        assert request['agreements'][1]['status'] == 'Pending'
