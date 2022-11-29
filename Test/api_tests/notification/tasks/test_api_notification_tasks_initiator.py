import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - NotificationEmail')
@allure.story('E-mail уведомления. Задачи. Я инициатор.')
class TestApiNotificationTasksInitiator(ApiBase):

    # Изначально логинимся под модератором
    def setup_method(self):
        self.APP.api_token.get_token('SystemOperator')

    test_data = [
        ({'emailNotices': [{'noticeId': 1001, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1001, 'isActive': False}]}, False,)
    ]

    @allure.title('Изменилось плановое время исполнения')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data)
    def test_notification_tasks_initiator_change_planned_time(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'], set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем задачу
        task = self.create_task()
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Меняем время окончания в задаче
        task = self.APP.api_actions_in_task.update_task(task['syncToken'], task['id'], {'endDate': self.APP.time.get_date_increased_x_days_json(2)}, params={'isModeratorMode': True})
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_02 = [
        ({'emailNotices': [{'noticeId': 1002, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1002, 'isActive': False}]}, False,)
    ]

    @allure.title('Изменилось плановое время согласования')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_02)
    def test_notification_tasks_initiator_change_approve_time(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем задачу
        task = self.create_task()
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Меняем плановое время
        self.APP.api_actions_in_task.change_planned_time_in_task(task['id'], {'plannedTimeOfApproval': 1000}, task['syncToken'], params={'isModeratorMode': True})
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_03 = [
        ({'emailNotices': [{'noticeId': 1003, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1003, 'isActive': False}]}, False,)
    ]

    @allure.title('Изменилось плановое время уточнения')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_03)
    def test_notification_tasks_initiator_change_clarification_time(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем задачу
        task = self.create_task()
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Меняем плановое время
        self.APP.api_actions_in_task.change_planned_time_in_task(task['id'], {'plannedTimeOfClarification': 1000}, task['syncToken'], params={'isModeratorMode': True})
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_04 = [
        ({'emailNotices': [{'noticeId': 1016, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1016, 'isActive': False}]}, False,)
    ]

    @allure.title('Сменился исполнитель')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_04)
    def test_notification_tasks_initiator_change_contractor(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем задачу
        task = self.create_task()
        # Логинимся под модератором
        self.APP.api_token.get_token('SystemOperator')
        # Меняем исполнителя
        self.APP.api_actions_in_task.change_contractor_in_task(task['syncToken'], task['id'], self.APP.group_data.users['test_user03']['user_id'], params={'isModeratorMode': True})
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_05 = [
        ({'emailNotices': [{'noticeId': 1020, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1020, 'isActive': False}]}, False,)
    ]

    @allure.title('Отправлено на согласование')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_05)
    def test_notification_tasks_initiator_approval_sent(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем задачу
        task = self.create_task()
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Добавляем согласующего
        request = self.APP.api_actions_in_task.add_agreements_in_task(self.APP.group_data.users['test_user03']['user_id'], task['syncToken'], task['id'], params={'isModetatorMode': True})
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_06 = [
        ({'emailNotices': [{'noticeId': 1021, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1021, 'isActive': False}]}, False,)
    ]

    @allure.title('Принято положительное решение по согласованию')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_06)
    def test_notification_tasks_initiator_approval_accepted_positive(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем задачу с согласующим
        task = self.create_task({'approvers': ['tes_user01']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Согласуем задачу
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_07 = [
        ({'emailNotices': [{'noticeId': 1022, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1022, 'isActive': False}]}, False,)
    ]

    @allure.title('Принято отрицательное решение по согласованию')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_07)
    def test_notification_tasks_initiator_approval_accepted_negative(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем задачу с согласующим
        task = self.create_task({'approvers': ['test_user01']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Отклоняем заявку
        task = self.APP.api_actions_in_task.reject_task(task['syncToken'], task['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_08 = [
        ({'emailNotices': [{'noticeId': 1023, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1023, 'isActive': False}]}, False,)
    ]

    @allure.title('Согласующий принял положительное решение по согласованию')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_08)
    def test_notification_tasks_initiator_approver_accepted_positive(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем задачу с 2-мя согласующими
        task = self.create_task({'approvers': ['test_user01', 'test_user03']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Согласуем задачу
        task = self.APP.api_actions_in_task.approve_task(task['syncToken', task['id']])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_09 = [
        ({'emailNotices': [{'noticeId': 1024, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1024, 'isActive': False}]}, False,)
    ]

    @allure.title('Согласующий принял отрицательное решение по согласованию')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_09)
    def test_notification_tasks_initiator_approver_accepted_negative(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем задачу с 2-мя согласующими
        task = self.create_task({'approvers': ['test_user01', 'test_user03']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Отклоняем задачу
        task = self.APP.api_actions_in_task.reject_task(task['syncToken'], task['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_10 = [
        ({'emailNotices': [{'noticeId': 1040, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1040, 'isActive': False}]}, False,)
    ]

    @allure.title('Добавлен обозреватель')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_10)
    def test_notification_tasks_initiator_added_observer(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем задачу
        task = self.create_task()
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Добавляем обозревателя
        task = self.APP.api_actions_in_task.refresh_observer_in_task(task['syncToken'], task['id'], self.APP.group_data.users['test_user01']['user_id'], params={'isModeratorMode': True})
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_11 = [
        ({'emailNotices': [{'noticeId': 1050, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1050, 'isActive': False}]}, False,)
    ]

    @allure.title('Проверка выполнения, требуется оценка')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_11)
    def test_notification_tasks_initiator_to_resolved(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем задачу
        task = self.create_task()
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Отправляем задачу на проверку
        task = self.APP.api_actions_in_task.resolve_task(task['syncToken'], task['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_12 = [
        ({'emailNotices': [{'noticeId': 1060, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1060, 'isActive': False}]}, False,)
    ]

    @allure.title('Оставлен общий(обычный) комментарий')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_12)
    def test_notification_tasks_initiator_comment_common_added(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем задачу
        task = self.create_task()
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Оставляем комментарий
        self.APP.api_actions_in_comment.create_comment(task['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_13 = [
        ({'emailNotices': [{'noticeId': 1061, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1061, 'isActive': False}]}, False,)
    ]

    @allure.title('Оставлен персональный комментарий')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_13)
    def test_notification_tasks_initiator_comment_personal_added(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Перелогиниваемся на пользователя
        self.APP.api_token.get_token('test_user08')
        # Создаем задачу
        task = self.create_task()
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Оставляем комментарий
        self.APP.api_actions_in_comment.create_comment_with_mention(self.users['test_user08']['user_id'], task['id'],
                                                                    addressee_type='Initiator')
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

