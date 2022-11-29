import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - NotificationEmail')
@allure.story('E-mail уведомления. Заявки. Я исполнитель.')
class TestApiNotificationRequestsContractor(ApiBase):

    # Изначально логинимся под модератором
    def setup_method(self):
        self.APP.api_token.get_token('SystemOperator')

    test_data = [
        ({'emailNotices': [{'noticeId': 101, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 101, 'isActive': False}]}, False,)
    ]

    @allure.title('Изменилось плановое время исполнения')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data)
    def test_notification_requests_contractor_change_planned_time(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку
        request = self.create_request()
        # Логинимся под исполнителем
        self.APP.api_token.get_token('test_user04')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Логинимся под модератором
        self.APP.api_token.get_token('SystemOperator')
        # Меняем плановое время
        self.APP.api_change_request.change_planned_time_execution(request['syncToken'], request['id'])
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_02 = [
        ({'emailNotices': [{'noticeId': 102, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 102, 'isActive': False}]}, False,)
    ]

    @allure.title('Изменилось плановое время согласования')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_02)
    def test_notification_requests_contractor_change_approve_time(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку
        request = self.create_request()
        # Логинимся под исполнителем
        self.APP.api_token.get_token('test_user04')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Логинимся под модератором
        self.APP.api_token.get_token('SystemOperator')
        # Меняем плановое время
        self.APP.api_change_request.change_planned_time_approve(request['syncToken'], request['id'])
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_03 = [
        ({'emailNotices': [{'noticeId': 103, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 103, 'isActive': False}]}, False,)
    ]

    @allure.title('Изменилось плановое время уточнения')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_03)
    def test_notification_requests_contractor_change_clarification_time(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку
        request = self.create_request()
        # Логинимся под исполнителем
        self.APP.api_token.get_token('test_user04')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Логинимся под модератором
        self.APP.api_token.get_token('SystemOperator')
        # Меняем плановое время
        self.APP.api_change_request.change_planned_time_clarification(request['syncToken'], request['id'])
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_04 = [
        ({'emailNotices': [{'noticeId': 115, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 115, 'isActive': False}]}, False,)
    ]

    @allure.title('Назначено на вас')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_04)
    def test_notification_requests_contractor_assigned_to_me(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку
        request = self.create_request()
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Назначаем исполнителя
        self.APP.api_change_request.set_contractor(request['syncToken'], request['id'], 'test_user04')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_05 = [
        ({'emailNotices': [{'noticeId': 116, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 116, 'isActive': False}]}, False,)
    ]

    @allure.title('Сменился исполнитель')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_05)
    def test_notification_requests_contractor_change_contractor(self, set_notification, expected_result):

        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку
        request = self.create_request()
        # Логинимся под исполнителем
        self.APP.api_token.get_token('test_user04')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Меняем исполнителя
        self.APP.api_change_request.change_contractor(request['syncToken'], request['id'], 'test_user01')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_06 = [
        ({'emailNotices': [{'noticeId': 117, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 117, 'isActive': False}]}, False,)
    ]

    @allure.title('Снято с вашей ответственности')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_06)
    def test_notification_requests_contractor_not_my_responsibility(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку
        request = self.create_request()
        # Логинимся под исполнителем
        self.APP.api_token.get_token('test_user04')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Логинимся под модератором
        self.APP.api_token.get_token('SystemOperator')
        # Ищем нужную услугу
        services = self.APP.api_actions_in_service_catalog.search_service(self.APP.group_data.service_template['AutomationService Тестовый Тип 4']['name'])
        # Меняем услугу
        request = self.APP.api_change_request.change_service_in_request(request['syncToken'], request['id'], services["items"][0]['id'])
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_07 = [
        ({'emailNotices': [{'noticeId': 120, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 120, 'isActive': False}]}, False,)
    ]

    @allure.title('Отправлено на согласование')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_07)
    def test_notification_requests_contractor_approval_sent(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку
        request = self.create_request()
        # Логинимся под исполнителем
        self.APP.api_token.get_token('test_user04')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_user02')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_08 = [
        ({'emailNotices': [{'noticeId': 121, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 121, 'isActive': False}]}, False,)
    ]

    @allure.title('Принято положительное решение по согласованию')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_08)
    def test_notification_requests_contractor_approval_accepted_positive(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку
        request = self.create_request()
        # Логинимся под исполнителем
        self.APP.api_token.get_token('test_user04')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_user02')
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user02')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_09 = [
        ({'emailNotices': [{'noticeId': 122, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 122, 'isActive': False}]}, False,)
    ]

    @allure.title('Принято отрицательное решение по согласованию')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_09)
    def test_notification_requests_contractor_approval_accepted_negative(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку
        request = self.create_request()
        # Логинимся под исполнителем
        self.APP.api_token.get_token('test_user04')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_user02')
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user02')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_10 = [
        ({'emailNotices': [{'noticeId': 123, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 123, 'isActive': False}]}, False,)
    ]

    @allure.title('Согласующий принял положительное решение по согласованию')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_10)
    def test_notification_requests_contractor_approver_accepted_positive(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку
        request = self.create_request()
        # Логинимся под исполнителем
        self.APP.api_token.get_token('test_user04')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_user02')
        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_user03')
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user02')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_11 = [
        ({'emailNotices': [{'noticeId': 124, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 124, 'isActive': False}]}, False,)
    ]

    @allure.title('Согласующий принял отрицательное решение по согласованию')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_11)
    def test_notification_requests_contractor_approver_accepted_negative(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку
        request = self.create_request()
        # Логинимся под исполнителем
        self.APP.api_token.get_token('test_user04')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_user02')
        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_user03')
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user02')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_12 = [
        ({'emailNotices': [{'noticeId': 140, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 140, 'isActive': False}]}, False,)
    ]

    @allure.title('Добавлен обозреватель')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_12)
    def test_notification_requests_contractor_added_observer(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку
        request = self.create_request()
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user04')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Добавляем обозревателя
        self.APP.api_change_request.add_observer(self.APP.group_data.users['test_user01']['user_id'], request['syncToken'], request['id'], params={'isModeratorMode': True})
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_13 = [
        ({'emailNotices': [{'noticeId': 151, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 151, 'isActive': False}]}, False,)
    ]

    @allure.title('Отклонена, вы являлись исполнителем')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_13)
    def test_notification_requests_contractor_to_rejected(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку
        request = self.create_request()
        # Логинимся под исполнителем
        self.APP.api_token.get_token('test_user04')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_user02')
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user02')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_14 = [
        ({'emailNotices': [{'noticeId': 160, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 160, 'isActive': False}]}, False,)
    ]

    @allure.title('Оставлен общий(обычный) комментарий')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_14)
    def test_notification_requests_contractor_comment_common_added(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку
        request = self.create_request()
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user04')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Оставляем комментарий
        self.APP.api_actions_in_comment.create_comment(request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_15 = [
        ({'emailNotices': [{'noticeId': 161, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 161, 'isActive': False}]}, False,)
    ]

    @allure.title('Оставлен персональный комментарий')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_15)
    def test_notification_requests_contractor_comment_personal_added(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку
        request = self.create_request()
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user04')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Оставляем комментарий
        self.APP.api_actions_in_comment.create_comment_with_mention(self.users['test_user08']['user_id'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list