import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Messenger')
@allure.story('Создание чатов, список чатов, редактирование чатов.')
class TestApiMessenger(ApiBase):

    @allure.title('Создание персонального чата с пользователем.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_api_messenger_personal_chat_create(self):
        # Создаем персональный чат
        messenger = self.APP.api_actions_in_messenger.create_personal_chat(self.APP.group_data.users['test_user01']['user_id'])
        # Получаем список чатов текущего пользователя
        messenger_list = self.APP.api_messenger.get_conversations()
        # Формируем список id всех чатов
        messenger_list_id = self.list_id_all_chat_for_user(messenger_list)
        # Получаем id всех участников чата
        messenger_participants_id = self.APP.api_messenger.get_conversations_id_participantids(messenger['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert messenger['id'] in messenger_list_id
        assert self.APP.group_data.users['test_user01']['user_id'] in messenger_participants_id

    @allure.title('Создание группового чата с пользователем.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_api_messenger_group_chat_create(self):
        # Создаем групповой чат
        messenger = self.APP.api_actions_in_messenger.create_group_chat([
                self.APP.group_data.users['test_user01']['user_id'],
                self.APP.group_data.users['test_user02']['user_id'],
            ])
        # Получаем список чатов текущего пользователя
        messenger_list = self.APP.api_messenger.get_conversations()
        # Формируем список id всех чатов
        messenger_list_id = self.list_id_all_chat_for_user(messenger_list)
        # Получаем id всех участников чата
        messenger_participants_id = self.APP.api_messenger.get_conversations_id_participantids(messenger['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert messenger['id'] in messenger_list_id
        assert self.APP.group_data.users['test_user01']['user_id'] in messenger_participants_id
        assert self.APP.group_data.users['test_user02']['user_id'] in messenger_participants_id
        assert self.APP.group_data.users['test_user09']['user_id'] in messenger_participants_id

    @allure.title('Добавление пользователя в групповой чат')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_api_messenger_group_chat_add_participant(self):
        # Создаем групповой чат
        messenger = self.APP.api_actions_in_messenger.create_group_chat([
            self.APP.group_data.users['test_user01']['user_id'],
            self.APP.group_data.users['test_user02']['user_id'],
        ])
        # Добавляем пользователя в чат
        self.APP.api_actions_in_messenger.add_user_to_chat([self.APP.group_data.users['test_user03']['user_id']], messenger['id'])
        # Получаем id всех участников чата
        messenger_participants_id = self.APP.api_messenger.get_conversations_id_participantids(messenger['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert self.APP.group_data.users['test_user03']['user_id'] in messenger_participants_id

    @allure.title('Удаление пользователя из группового чата')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.JenkinsTest
    def test_api_messenger_group_chat_delete_participant(self):
        # Создаем групповой чат
        messenger = self.APP.api_actions_in_messenger.create_group_chat([
            self.APP.group_data.users['test_user01']['user_id'],
            self.APP.group_data.users['test_user02']['user_id'],
        ])
        # Удаляем пользователя из чата
        self.APP.api_messenger.delete_conversations_id_participants(messenger['id'], params={'users': self.APP.group_data.users['test_user01']['user_id']})
        # Получаем id всех участников чата
        messenger_participants_id = self.APP.api_messenger.get_conversations_id_participantids(messenger['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert self.APP.group_data.users['test_user01']['user_id'] not in messenger_participants_id

    @allure.title('Смена роли пользователя на администратора чата')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_messenger_group_chat_change_role_participant(self):
        # Создаем групповой чат
        messenger = self.APP.api_actions_in_messenger.create_group_chat([
            self.APP.group_data.users['test_user01']['user_id'],
            self.APP.group_data.users['test_user02']['user_id'],
        ])
        # Меняем роль пользователя
        self.APP.api_actions_in_messenger.change_user_role_in_chat(messenger['id'], self.APP.group_data.users['test_user01']['user_id'])
        # Получаем id участников чата
        messenger_participants = self.APP.api_messenger.get_conversations_id_participants(messenger['id'])
        # Получаем роль пользователя в чате
        user_role = self.user_role_in_chat(messenger_participants, 'test_user01')
        # Сравниваем получаемые значения с ожидаемыми
        assert user_role == 'administrator'

    @allure.title('Удаление чата')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_messenger_delete_chat(self):
        # Создаем групповой чат
        messenger = self.APP.api_actions_in_messenger.create_group_chat([
            self.APP.group_data.users['test_user01']['user_id'],
            self.APP.group_data.users['test_user02']['user_id'],
        ])
        # Удаляем чат
        self.APP.api_messenger.delete_conversations_id(messenger['id'])
        # Получаем список чатов текущего пользователя
        messenger_list = self.APP.api_messenger.get_conversations()
        # Формируем список id всех чатов
        messenger_list_id = self.list_id_all_chat_for_user(messenger_list)
        # Сравниваем получаемые значения с ожидаемыми
        assert messenger['id'] not in messenger_list_id

    @allure.title('Пользователь покидает групповой чат.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_messenger_chat_leave(self):
        # Создаем групповой чат
        messenger = self.APP.api_actions_in_messenger.create_group_chat([
            self.APP.group_data.users['test_user01']['user_id'],
            self.APP.group_data.users['test_user02']['user_id'],
        ])
        # Покидаем чат
        self.APP.api_messenger.delete_conversations_id_participants_current(messenger['id'])
        # Получаем id участников чата
        messenger_participants = self.APP.api_messenger.get_conversations_id_participants(messenger['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert self.APP.group_data.users['test_user09']['user_id'] not in messenger_participants