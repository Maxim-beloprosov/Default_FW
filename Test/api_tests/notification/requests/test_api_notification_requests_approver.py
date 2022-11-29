import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - NotificationEmail')
@allure.story('E-mail уведомления. Заявки. Я согласующий.')
class TestApiNotificationRequestsApprover(ApiBase):

    # Изначально логинимся под модератором
    def setup_method(self):
        self.APP.api_token.get_token('SystemOperator')

    test_data = [
        ({'emailNotices': [{'noticeId': 201, 'isActive': True}, {'noticeId': 225, 'isActive': False}]}, True,),
        ({'emailNotices': [{'noticeId': 201, 'isActive': False}, {'noticeId': 225, 'isActive': False}]}, False,)
    ]

    @allure.title('Изменилось плановое время исполнения')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.EmailNotification
    @pytest.mark.parametrize("set_notification, expected_result", test_data)
    def test_notification_requests_approver_change_planned_time(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку с согласующим
        request = self.create_request({"approvers": ['test_user04']})
        # Логинимся под модератором
        self.APP.api_token.get_token('SystemOperator')
        # Меняем плановое время
        self.APP.api_change_request.change_planned_time_execution(request['syncToken'], request['id'])
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_02 = [
        ({'emailNotices': [{'noticeId': 202, 'isActive': True}, {'noticeId': 225, 'isActive': False}]}, True,),
        ({'emailNotices': [{'noticeId': 202, 'isActive': False}, {'noticeId': 225, 'isActive': False}]}, False,)
    ]

    @allure.title('Изменилось плановое время согласования')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.EmailNotification
    @pytest.mark.parametrize("set_notification, expected_result", test_data_02)
    def test_notification_requests_approver_change_approve_time(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку с согласующим
        request = self.create_request({"approvers": ['test_user04']})
        # Логинимся под модератором
        self.APP.api_token.get_token('SystemOperator')
        # Меняем плановое время
        self.APP.api_change_request.change_planned_time_approve(request['syncToken'], request['id'])
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_03 = [
        ({'emailNotices': [{'noticeId': 203, 'isActive': True}, {'noticeId': 225, 'isActive': False}]}, True,),
        ({'emailNotices': [{'noticeId': 203, 'isActive': False}, {'noticeId': 225, 'isActive': False}]}, False,)
    ]

    @allure.title('Изменилось плановое время уточнения')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.EmailNotification
    @pytest.mark.parametrize("set_notification, expected_result", test_data_03)
    def test_notification_requests_approver_change_clarification_time(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку с согласующим
        request = self.create_request({"approvers": ['test_user04']})
        # Логинимся под модератором
        self.APP.api_token.get_token('SystemOperator')
        # Меняем плановое время
        self.APP.api_change_request.change_planned_time_clarification(request['syncToken'], request['id'])
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_04 = [
        ({'emailNotices': [{'noticeId': 215, 'isActive': True}, {'noticeId': 225, 'isActive': False}]}, True,),
        ({'emailNotices': [{'noticeId': 215, 'isActive': False}, {'noticeId': 225, 'isActive': False}]}, False,)
    ]

    @allure.title('Назначен исполнитель')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.EmailNotification
    @pytest.mark.parametrize("set_notification, expected_result", test_data_04)
    def test_notification_requests_approver_contractor_assigned(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку с согласующим
        request = self.create_request({"approvers": ['test_user04']})
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Назначаем исполнителя
        self.APP.api_change_request.set_contractor(request['syncToken'], request['id'], 'test_user01')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_05 = [
        ({'emailNotices': [{'noticeId': 216, 'isActive': True}, {'noticeId': 225, 'isActive': False}]}, True,),
        ({'emailNotices': [{'noticeId': 216, 'isActive': False}, {'noticeId': 225, 'isActive': False}]}, False,)
    ]

    @allure.title('Сменился исполнитель')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.EmailNotification
    @pytest.mark.parametrize("set_notification, expected_result", test_data_05)
    def test_notification_requests_approver_contractor_changed(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку с согласующим
        request = self.create_request({"approvers": ['test_user04']})
        # Логинимся под исполнителем
        self.APP.api_token.get_token('test_user02')
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
        ({'emailNotices': [{'noticeId': 220, 'isActive': True}, {'noticeId': 225, 'isActive': False}]}, True,),
        ({'emailNotices': [{'noticeId': 220, 'isActive': False}, {'noticeId': 225, 'isActive': False}]}, False,)
    ]

    @allure.title('Отправлено на согласование')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.EmailNotification
    @pytest.mark.parametrize("set_notification, expected_result", test_data_06)
    def test_notification_requests_approver_approval_sent(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку с согласующим
        request = self.create_request({"approvers": ['test_user04']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user04')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_user02')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_07 = [
        ({'emailNotices': [{'noticeId': 221, 'isActive': True}, {'noticeId': 225, 'isActive': False}]}, True,),
        ({'emailNotices': [{'noticeId': 221, 'isActive': False}, {'noticeId': 225, 'isActive': False}]}, False,)
    ]

    @allure.title('Принято положительное решение по согласованию')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.EmailNotification
    @pytest.mark.parametrize("set_notification, expected_result", test_data_07)
    def test_notification_requests_approver_approval_accepted_positive(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({"approvers": ['test_user04', 'test_Boss01']})
        # Перелогиниваемся на согласующего - начальника
        self.APP.api_token.get_token('test_Boss01')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_08 = [
        ({'emailNotices': [{'noticeId': 222, 'isActive': True}, {'noticeId': 225, 'isActive': False}]}, True,),
        ({'emailNotices': [{'noticeId': 222, 'isActive': False}, {'noticeId': 225, 'isActive': False}]}, False,)
    ]

    @allure.title('Принято отрицательное решение по согласованию')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.EmailNotification
    @pytest.mark.parametrize("set_notification, expected_result", test_data_08)
    def test_notification_requests_approver_approval_accepted_negative(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({"approvers": ['test_user04', 'test_Boss01']})
        # Перелогиниваемся на согласующего - начальника
        self.APP.api_token.get_token('test_Boss01')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_09 = [
        ({'emailNotices': [{'noticeId': 223, 'isActive': True}, {'noticeId': 225, 'isActive': False}]}, True,),
        ({'emailNotices': [{'noticeId': 223, 'isActive': False}, {'noticeId': 225, 'isActive': False}]}, False,)
    ]

    @allure.title('Согласующий принял положительное решение по согласованию')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.EmailNotification
    @pytest.mark.parametrize("set_notification, expected_result", test_data_09)
    def test_notification_requests_approver_accepted_positive(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({"approvers": ['test_user04', 'test_user01']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_10 = [
        ({'emailNotices': [{'noticeId': 224, 'isActive': True}, {'noticeId': 225, 'isActive': False}]}, True,),
        ({'emailNotices': [{'noticeId': 224, 'isActive': False}, {'noticeId': 225, 'isActive': False}]}, False,)
    ]

    @allure.title('Согласующий принял отрицательное решение по согласованию')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.EmailNotification
    @pytest.mark.parametrize("set_notification, expected_result", test_data_10)
    def test_notification_requests_approver_accepted_negative(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку с 2-мя согласующими
        request = self.create_request({"approvers": ['test_user04', 'test_user01']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_11 = [
        ({'emailNotices': [{'noticeId': 225, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 225, 'isActive': False}]}, False,)
    ]

    @allure.title('Вы были назначены согласующим')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.EmailNotification
    @pytest.mark.parametrize("set_notification, expected_result", test_data_11)
    def test_notification_requests_approver_assigned_to_me(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку с согласующим
        request = self.create_request({"approvers": ['test_user04']})
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_12 = [
        ({'emailNotices': [{'noticeId': 226, 'isActive': True}, {'noticeId': 225, 'isActive': False}]}, True,),
        ({'emailNotices': [{'noticeId': 226, 'isActive': False}, {'noticeId': 225, 'isActive': False}]}, False,)
    ]

    @allure.title('Вы остались последним согласующим')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.EmailNotification
    @pytest.mark.parametrize("set_notification, expected_result", test_data_12)
    def test_notification_requests_approver_you_last(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку с 2- мя согласующими
        request = self.create_request({"approvers": ['test_user04', 'test_user01']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Согласуем заявку
        request = self.APP.api_actions_in_request.approve_request(request['syncToken'], request['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_13 = [
        ({'emailNotices': [{'noticeId': 240, 'isActive': True}, {'noticeId': 225, 'isActive': False}]}, True,),
        ({'emailNotices': [{'noticeId': 240, 'isActive': False}, {'noticeId': 225, 'isActive': False}]}, False,)
    ]

    @allure.title('Добавлен обозреватель')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.EmailNotification
    @pytest.mark.parametrize("set_notification, expected_result", test_data_13)
    def test_notification_requests_approver_add_observer(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку с согласующим
        request = self.create_request({"approvers": ['test_user04']})
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Добавляем обозревателя
        self.APP.api_change_request.add_observer(self.APP.group_data.users['test_user06']['user_id'], request['syncToken'], request['id'], params={'isModeratorMode': True})
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_14 = [
        ({'emailNotices': [{'noticeId': 260, 'isActive': True}, {'noticeId': 225, 'isActive': False}]}, True,),
        ({'emailNotices': [{'noticeId': 260, 'isActive': False}, {'noticeId': 225, 'isActive': False}]}, False,)
    ]

    @allure.title('Оставлен общий(обычный) комментарий')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.EmailNotification
    @pytest.mark.parametrize("set_notification, expected_result", test_data_14)
    def test_notification_requests_approver_comment_common_added(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку с согласующим
        request = self.create_request({"approvers": ['test_user04']})
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
        ({'emailNotices': [{'noticeId': 261, 'isActive': True}, {'noticeId': 225, 'isActive': False}]}, True,),
        ({'emailNotices': [{'noticeId': 261, 'isActive': False}, {'noticeId': 225, 'isActive': False}]}, False,)
    ]

    @allure.title('Оставлен персональный комментарий')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.EmailNotification
    @pytest.mark.parametrize("set_notification, expected_result", test_data_15)
    def test_notification_requests_approver_comment_personal_added(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку с согласующим
        request = self.create_request({"approvers": ['test_user04']})
        # Оставляем комментарий
        self.APP.api_actions_in_comment.create_comment_with_mention(self.users['test_user08']['user_id'], request['id'], addressee_type='Approver')
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list






