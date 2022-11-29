import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - NotificationEmail')
@allure.story('E-mail уведомления. Заявки. Я обозреватель.')
class TestApiNotificationRequestsObserver(ApiBase):

    # Изначально логинимся под модератором
    def setup_method(self):
        self.APP.api_token.get_token('SystemOperator')

    test_data = [
        ({'emailNotices': [{'noticeId': 301, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 301, 'isActive': False}]}, False,)
    ]

    @allure.title('Изменилось плановое время исполнения')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data)
    def test_notification_requests_observer_change_planned_time(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user04']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user08')
        # Создаем заявку с обозревателем
        request = self.create_request({'observers': ['test_user04']})
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Меняем плановое время
        self.APP.api_change_request.change_planned_time_execution(request['syncToken'], request['id'])
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user04']['Email'], request['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list