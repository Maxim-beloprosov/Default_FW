import allure
import pytest
from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Task')
@allure.story('Редактирование задач')
class TestApiEditTask(ApiBase):

    @allure.title('Смена заголовка задачи')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_subject_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Меняем заголовок
        task['subject'] = 'AutomationApiTest Change Subject ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        # Обновляем задачу
        task = self.APP.api_tasks.put_tasks_id(task['id'], task)
        assert 'AutomationApiTest Change Subject' in task['subject']

    @allure.title('Смена даты начала задачи')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_begin_date_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Меняем дату начала
        task['beginDate'] = self.APP.time.get_date_increased_x_days_json(1)
        # Обновляем задачу
        task = self.APP.api_tasks.put_tasks_id(task['id'], task)
        assert task['status'] == self.APP.group_data.Status_ticket['ENG']['В ожидании']

    @allure.title('Смена даты окончания задачи')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_end_date_in_task(self):
        # Переменная с датой окончания
        end_date = self.APP.time.get_date_increased_x_days_json(1)
        # Создаем задачу с датой окончания
        task = self.create_task({'endDate': end_date})
        # Сохраняем дату окончания для проверки после создания задачи
        end_date_post_create = task['endDate']
        # Меняем дату окончания
        task['endDate'] = self.APP.time.get_date_increased_x_days_json(2)
        # Обновляем задачу
        task = self.APP.api_tasks.put_tasks_id(task['id'], task)
        assert task['endDate'] != end_date
        assert end_date == self.APP.time.convert_date_time_second(end_date_post_create)

    @allure.title('Смена трудоемкости в задаче')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_laboriousness_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Меняем трудоемкость задачи
        task['laboriousness'] = 600
        # Обновляем задачу
        task = self.APP.api_tasks.put_tasks_id(task['id'], task)
        assert task['laboriousness'] == 600

    @allure.title('Добавление блока описания в задаче')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_add_description_block_in_task(self):
        # Создаем задачу
        task = self.create_task()
        #Дата для описания
        date_time = self.APP.time.get_date_time_Y_m_d_H_M_S()
        # Добавляем описание к задаче
        task = self.APP.api_actions_in_task.add_additional_descriptions_in_task(task['id'], {'type': 'Text', 'text': 'AutomationApiTest Edit Text ' + date_time})
        assert 'AutomationApiTest Edit Text ' + date_time in task['contentParts'][0]['text']

    @allure.title('Добавление вложения в задачу')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_add_attachments_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Добавляем вложение
        task = self.APP.api_actions_in_task.add_attachments_in_task(task['id'], [self.APP.group_data.Attachments['Тестовое фото №1']['Id']])
        assert len(task['attachments']) > 0
        assert task['attachments'][0]['fileMetaData']['id'] == self.APP.group_data.Attachments['Тестовое фото №1']['Id']

    @allure.title('Добавление нескольких вложений в задачу')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_add_attachments_in_task_second(self):
        # Создаем задачу
        task = self.create_task()
        # Добавляем вложения
        task = self.APP.api_actions_in_task.add_attachments_in_task(task['id'], [self.APP.group_data.Attachments['Тестовое фото №1']['Id'], self.APP.group_data.Attachments['Тестовое фото №2']['id']])
        assert len(task['attachments']) > 1

    @allure.title('Удаление вложения из задачи')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_delete_attachments_from_task(self):
        # Создаем задачу
        task = self.create_task()
        # Добавляем вложение
        task = self.APP.api_actions_in_task.add_attachments_in_task(task['id'], [self.APP.group_data.Attachments['Тестовое фото №1']['Id']])
        #Удаляем вложение
        task = self.APP.api_actions_in_task.delete_attachments_from_task(task['id'], [task['attachments'][0]['id']])
        assert len(task['attachments']) == 0

    @allure.title('Удаление нескольких вложений из задачи')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_delete_attachments_from_task_second(self):
        # Создаем задачу
        task = self.create_task()
        # Добавляем вложения
        task = self.APP.api_actions_in_task.add_attachments_in_task(task['id'], [self.APP.group_data.Attachments['Тестовое фото №1']['Id'], self.APP.group_data.Attachments['Тестовое фото №2']['id']])
        # Удаляем вложения
        task = self.APP.api_actions_in_task.delete_attachments_from_task(task['id'], [task['attachments'][0]['id'], task['attachments'][1]['id']])
        assert len(task['attachments']) == 0

    @allure.title('Добавление блока описания с изображением в задачу')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_add_descriptions_block_with_picture_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Добавляем описание к задаче
        task = self.APP.api_actions_in_task.add_additional_descriptions_in_task(task['id'], {'type': 'Attachment', 'fileId': self.APP.group_data.Attachments['Тестовое фото №1']['Id']})
        assert task['contentParts'][0]['fileMetaData']['id'] == self.APP.group_data.Attachments['Тестовое фото №1']['Id']

    @allure.title('Добавление пустого блока описания.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_add_empty_description_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Добавляем пустое описание
        task = self.APP.api_actions_in_task.add_additional_descriptions_in_task(task['id'], {'type': 'Text', 'text': ''})
        assert task['status'] == 400

    @allure.title('Смена заголовка задачи на пустой.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_subject_to_empty_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Меняем заголовок
        task['subject'] = ''
        # Обновляем задачу
        task = self.APP.api_tasks.put_tasks_id(task['id'], task)
        assert task['status'] == 400

    @allure.title('Смена даты окончания задачи на > 10000 год')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_end_date_over_10000_in_task(self):
        # Переменная с датой окончания
        end_date = self.APP.time.get_date_increased_x_days_json(1)
        # Создаем задачу с датой окончания
        task = self.create_task({'endDate': end_date})
        # Сохраняем дату окончания для проверки после создания задачи
        end_date_post_create = task['endDate']
        # Меняем дату окончания
        task['endDate'] = '10000-09-20T15:33:41+03:00'
        # Обновляем задачу
        task = self.APP.api_tasks.put_tasks_id(task['id'], task)
        assert task['status'] == 400

    @allure.title('Смена даты начала задачи на > 10000')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_begin_date_over_10000_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Меняем дату начала
        task['beginDate'] = '10000-09-20T15:33:41+03:00'
        # Обновляем задачу
        task = self.APP.api_tasks.put_tasks_id(task['id'], task)
        assert task['status'] == 400

    @allure.title('Удалить исполнителя в задаче')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_delete_contractor_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Удаляем исполнителя
        task = self.APP.api_tasks.put_tasks_id_actions_clear_contractor(task['id'], body={'syncToken': task['syncToken']})
        assert task['status'] == 400

    @allure.title('Сменить инициатора на "пустого" в задаче')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_initiator_to_empty_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Меняем инициатора
        task = self.APP.api_tasks.put_tasks_id_actions_change_initiator(task['id'], body={'initiatorId': None, 'syncToken': task['syncToken']}, params={'isModeratorMode': True})
        assert task['status'] == 400

    @allure.title('Сменить исполнителя на "пустого" в задаче')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_contractor_to_empty_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Меняем исполнителя
        task = self.APP.api_tasks.put_tasks_id_actions_change_contractor(task['id'], body={'contractorId': None, 'syncToken': task['syncToken']})
        assert task['status'] == 400

    @allure.title('Сменить инициатора без прав модератора')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_initiator_without_permissions_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Меняем инициатора
        task = self.APP.api_tasks.put_tasks_id_actions_change_initiator(task['id'], body={'initiatorId': self.users['test_user03']['user_id'], 'syncToken': task['syncToken']})
        assert task.status_code == 403

    @allure.title('Сменить инициатора модератором без режима модератора')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_initiator_by_moderator_without_permissions_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # логинимся под модератором
        self.APP.api_token.get_token('SystemOperator')
        # Меняем инициатора
        task = self.APP.api_tasks.put_tasks_id_actions_change_initiator(task['id'], body={'initiatorId': self.users['test_user03']['user_id'],
                                                                                          'syncToken': task['syncToken']})
        assert task['status'] == 400

    @allure.title('Сменить исполнителя модератором без режима модератора')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_contractor_by_moderator_without_permissions_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')
        # Меняем исполнителя
        task = self.APP.api_tasks.put_tasks_id_actions_change_contractor(task['id'], body={'contractorId': self.users['test_user01']['user_id'], 'syncToken': task['syncToken']})
        assert task['status'] == 400

    @allure.title('Смена заголовка задачи без авторизации')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_subject_without_authorization_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Меняем заголовок
        task['subject'] = 'AutomationApiTest Change Subject ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        # Деавторизируемся
        self.APP.settings.Authorization = False
        # Обновляем задачу
        task = self.APP.api_tasks.put_tasks_id(task['id'], task)
        assert task.status_code == 401

    @allure.title('Смена даты начала задачи без авторизации')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_begin_date_without_authorization_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Меняем дату начала
        task['beginDate'] = self.APP.time.get_date_increased_x_days_json(1)
        # Деавторизируемся
        self.APP.settings.Authorization = False
        # Обновляем задачу
        task = self.APP.api_tasks.put_tasks_id(task['id'], task)
        assert task.status_code == 401

    @allure.title('Смена даты окончания задачи без авторизации')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_end_date_without_authorization_in_task(self):
        # Создаем задачу с датой окончания
        task = self.create_task({'endDate': self.APP.time.get_date_increased_x_days_json(1)})
        # Меняем дату окончания
        task['endDate'] = self.APP.time.get_date_increased_x_days_json(2)
        # Деавторизируемся
        self.APP.settings.Authorization = False
        # Обновляем задачу
        task = self.APP.api_tasks.put_tasks_id(task['id'], task)
        assert task.status_code == 401

    @allure.title('Смена трудоемкости в задаче без авторизации')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_laboriousness_without_authorization_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Меняем трудоемкость задачи
        task['laboriousness'] = 600
        # Деавторизируемся
        self.APP.settings.Authorization = False
        # Обновляем задачу
        task = self.APP.api_tasks.put_tasks_id(task['id'], task)
        assert task.status_code == 401

    @allure.title('Добавление блока описания в задаче без авторизации')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_add_description_block_without_authorization_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Дата для описания
        date_time = self.APP.time.get_date_time_Y_m_d_H_M_S()
        # Деавторизируемся
        self.APP.settings.Authorization = False
        # Добавляем описание к задаче
        task = self.APP.api_actions_in_task.add_additional_descriptions_in_task(task['id'],
                                                                                {'type': 'Text', 'text': 'AutomationApiTest Edit Text ' + date_time})
        assert task.status_code == 401

    @allure.title('Добавление вложения в задачу без авторизации')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_add_attachments_without_authorization_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Деавторизируемся
        self.APP.settings.Authorization = False
        # Добавляем вложение
        task = self.APP.api_actions_in_task.add_attachments_in_task(task['id'], self.APP.group_data.Attachments['Тестовое фото №1']['Id'])
        assert task.status_code == 401

    @allure.title('Удаление вложения из задачи без авторизации')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_delete_attachments_without_authorization_from_task(self):
        # Создаем задачу
        task = self.create_task()
        # Добавляем вложение
        task = self.APP.api_actions_in_task.add_attachments_in_task(task['id'], self.APP.group_data.Attachments['Тестовое фото №1']['Id'])
        # Деавторизируемся
        self.APP.settings.Authorization = False
        # Удаляем вложение
        task = self.APP.api_actions_in_task.delete_attachments_from_task(task['id'], [task['attachments'][0]['id']])
        assert task.status_code == 401

    @allure.title('Сменить инициатора без авторизации')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_initiator_without_authorization_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Деавторизируемся
        self.APP.settings.Authorization = False
        # Меняем инициатора
        task = self.APP.api_tasks.put_tasks_id_actions_change_initiator(task['id'], body={'initiatorId': self.users['test_user03']['user_id'],
                                                                                          'syncToken': task['syncToken']}, params={'isModeratorMode': True})
        assert task.status_code == 401

    @allure.title('Сменить исполнителя в задаче без авторизации')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_change_contractor_without_authorization_in_task(self):
        # Создаем задачу
        task = self.create_task()
        # Деавторизируемся
        self.APP.settings.Authorization = False
        # Меняем исполнителя
        task = self.APP.api_tasks.put_tasks_id_actions_change_contractor(task['id'], body={'contractorId': self.users['test_user01']['user_id'], 'syncToken': task['syncToken']})
        assert task.status_code == 401




