import time

import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - NotificationEmail')
@allure.story('E-mail уведомления. Задачи. Я согласующий.')
class TestApiNotificationTasksApprover(ApiBase):

    # Изначально логинимся под модератором
    def setup_method(self):
        self.APP.api_token.get_token('SystemOperator')

    test_data = [
        ({'emailNotices': [{'noticeId': 1201, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1201, 'isActive': False}]}, False,)
    ]

    @allure.title('Изменилось плановое время исполнения')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data)
    def test_notification_tasks_approver_change_planned_time(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'], set_notification)
        # Создаем задачу
        task = self.create_task({'approvers': ['test_user08']})
        # Меняем время окончания в задаче
        self.APP.api_actions_in_task.update_task(task['syncToken'], task['id'], {'endDate': self.APP.time.get_date_increased_x_days_json(2)},
                                                        params={'isModeratorMode': True})
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_02 = [
        ({'emailNotices': [{'noticeId': 1202, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1202, 'isActive': False}]}, False,)
    ]

    @allure.title('Изменилось плановое время согласования')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_02)
    def test_notification_tasks_approver_change_approve_time(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Создаем задачу
        task = self.create_task({'approvers': ['test_user08']})
        # Меняем плановое время
        self.APP.api_actions_in_task.change_planned_time_in_task(task['id'], {'plannedTimeOfApproval': 1000}, task['syncToken'])
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_03 = [
        ({'emailNotices': [{'noticeId': 1203, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1203, 'isActive': False}]}, False,)
    ]

    @allure.title('Изменилось плановое время уточнения')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_03)
    def test_notification_tasks_approver_change_clarification_time(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Создаем задачу
        task = self.create_task({'approvers': ['test_user08']})
        # Меняем плановое время
        self.APP.api_actions_in_task.change_planned_time_in_task(task['id'], {'plannedTimeOfApproval': 1000}, task['syncToken'], params={'isModeratorMode': True})
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_04 = [
        ({'emailNotices': [{'noticeId': 1216, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1216, 'isActive': False}]}, False,)
    ]

    @allure.title('Сменился исполнитель')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_04)
    def test_notification_tasks_contractor_change_contractor(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Создаем задачу
        task = self.create_task({'approvers': ['test_user08']})
        # Меняем исполнителя в задаче
        task = self.APP.api_actions_in_task.change_contractor_in_task(task['syncToken'], task['id'], self.users['test_user01']['user_id'],
                                                                      params={'isModeratorMode': True})
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_05 = [
        ({'emailNotices': [{'noticeId': 1220, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1220, 'isActive': False}]}, False,)
    ]

    @allure.title('Отправлено на согласование')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_05)
    def test_notification_tasks_approver_sent_to_approval(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Создаем задачу
        task = self.create_task({'approvers': ['test_user08']})
        # Логинимся под согласующим
        self.APP.api_token.get_token('test_user08')
        # Принимаем положительное решение по согласованию
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])
        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('SystemOperator')
        # Добавляем согласующего
        task = self.APP.api_actions_in_task.add_agreements_in_task(self.users['test_user01']['user_id'], task['syncToken'], task['id'], params={'isModeratorMode': True})
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_06 = [
        ({'emailNotices': [{'noticeId': 1221, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1221, 'isActive': False}]}, False,)
    ]

    @allure.title('Принято положительное решение по согласованию')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_06)
    def test_notification_tasks_approver_approval_positive(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Создаем задачу
        task = self.create_task({'approvers': ['test_user01', 'test_user08']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user08')
        # Положительно согласуем
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Положительно согласуем
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_07 = [
        ({'emailNotices': [{'noticeId': 1222, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1222, 'isActive': False}]}, False,)
    ]

    @allure.title('Принято отрицательное решение по согласованию')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_07)
    def test_notification_tasks_approver_approval_negative(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Создаем задачу
        task = self.create_task({'approvers': ['test_user01', 'test_user08']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user08')
        # Положительно согласуем
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Отклоняем заявку
        self.APP.api_actions_in_task.reject_task(task['syncTokne'], task['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_08 = [
        ({'emailNotices': [{'noticeId': 1223, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1223, 'isActive': False}]}, False,)
    ]

    @allure.title('Согласующий принял положительное решение по согласованию')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_08)
    def test_notification_tasks_approver_accepted_positive(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Создаем задачу
        task = self.create_task({'approvers': ['test_user01', 'test_user08']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Положительно согласуем
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_09 = [
        ({'emailNotices': [{'noticeId': 1224, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1224, 'isActive': False}]}, False,)
    ]

    @allure.title('Согласующий принял отрицательное решение по согласованию')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_09)
    def test_notification_tasks_approver_accepted_negative(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Создаем задачу
        task = self.create_task({'approvers': ['test_user01', 'test_user08']})
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
        ({'emailNotices': [{'noticeId': 1226, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1226, 'isActive': False}]}, False,)
    ]

    @allure.title('Вы остались последним согласующим')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_10)
    def test_notification_tasks_approver_you_last(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Создаем задачу
        task = self.create_task({'approvers': ['test_user01', 'test_user08']})
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user01')
        # Положительно согласуем
        task = self.APP.api_actions_in_task.approve_task(task['syncToken'], task['id'])
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_11 = [
        ({'emailNotices': [{'noticeId': 1225, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1225, 'isActive': False}]}, False,)
    ]

    @allure.title('Вы были назначены согласующим')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_11)
    def test_notification_tasks_approver_assigned_to_me(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Создаем задачу
        task = self.create_task()
        # Добавляем согласующего
        task = self.APP.api_actions_in_task.add_agreements_in_task(self.users['test_user08']['user_id'], task['syncToken'], task['id'])
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_12 = [
        ({'emailNotices': [{'noticeId': 1240, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1240, 'isActive': False}]}, False,)
    ]

    @allure.title('Добавлен обозреватель')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_12)
    def test_notification_tasks_approver_add_observer(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Создаем задачу
        task = self.create_task({'approvers': ['test_user08']})
        # Добавляем обозревателя
        task = self.APP.api_actions_in_task.refresh_observer_in_task(task['syncToken'], task['id'], self.users['test_user01']['user_id'])
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_13 = [
        ({'emailNotices': [{'noticeId': 1260, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1260, 'isActive': False}]}, False,)
    ]

    @allure.title('Оставлен общий(обычный) комментарий')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_13)
    def test_notification_tasks_approver_comment_common_added(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Создаем задачу
        task = self.create_task({'approvers': ['test_user08']})
        # Оставляем комментарий
        self.APP.api_actions_in_comment.create_comment(task['id'])
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list

    test_data_14 = [
        ({'emailNotices': [{'noticeId': 1261, 'isActive': True}]}, True,),
        ({'emailNotices': [{'noticeId': 1261, 'isActive': False}]}, False,)
    ]

    @allure.title('Оставлен персональный комментарий')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.EmailNotification
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_notification, expected_result", test_data_14)
    def test_notification_tasks_approver_comment_personal_added(self, set_notification, expected_result):
        # Включаем/выключаем подписку пользователя на уведомления
        self.APP.api_notification.put_notification_user_id(self.users['test_user08']['user_id'],
                                                           set_notification)
        # Создаем задачу
        task = self.create_task({'approvers': ['test_user08']})
        # Оставляем комментарий
        self.APP.api_actions_in_comment.create_comment_with_mention(self.users['test_user08']['user_id'], task['id'],
                                                                    addressee_type='Approver')
        # Проверяем, пришло ли письмо
        mail_in_list = self.APP.api_actions_in_notification_email.check_email_logs(self.users['test_user08']['Email'], task['docNumber'],
                                                                                   is_active=expected_result)
        assert mail_in_list


