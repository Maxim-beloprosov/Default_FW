import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Messenger - Chatting')
@allure.story('Отправка сообщения, редактирование сообщения, удаления сообщения.')
class TestApiMessengerChatting(ApiBase):

    @allure.title('Отправка сообщения в персональном чате.')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_messenger_personal_chat_send_content(self):
        # Создаем персональный чат
        messenger = self.APP.api_actions_in_messenger.create_personal_chat(self.users['test_user01']['user_id'])
        # Создаем текст сообщения
        content_text = 'Text AutomationApiTest ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        # Отправляем сообщение в персональный чат
        content_send_text = self.APP.api_actions_in_messenger.send_content_to_chat(messenger['id'], content_text)
        # Формируем список текстов из всех сообщений с персонального чата
        content_list_texts = self.APP.api_actions_in_messenger.pull_content_list_chat(messenger['id'])

        # Проверяем наличие созданного текста сообщения в чате
        assert content_text in content_list_texts

    @allure.title('Отправка сообщения в групповом чате.')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_messenger_group_chat_send_content(self):
        # Создаем групповой чат
        messenger = self.APP.api_actions_in_messenger.create_group_chat([
            self.users['test_user01']['user_id'],
            self.users['test_user02']['user_id'],
        ])
        # Создаем текст сообщения
        content_text = 'Text AutomationApiTest ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        # Отправляем сообщение в групповой чат
        content_send_text = self.APP.api_actions_in_messenger.send_content_to_chat(messenger['id'], content_text)
        # Формируем список текстов из всех сообщений с группового чата
        content_list_texts = self.APP.api_actions_in_messenger.pull_content_list_chat(messenger['id'])

        # Проверяем наличие созданного текста сообщения в групповом чате
        assert content_text in content_list_texts
        # Проверяем количество созданных сообщении с ожидаемым (сообщение о создании группового чата + отправленные сообщения)
        assert len(content_list_texts) == 2

    @allure.title('Редактирование сообщения в персональном чате.')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_messenger_personal_chat_change_content(self):
        # Создаем персональный чат
        messenger = self.APP.api_actions_in_messenger.create_personal_chat(self.users['test_user01']['user_id'])

        # Создаем текст сообщения
        content_text = 'Text AutomationApiTest ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        # Отправляем сообщение в персональный чат
        content_send_text = self.APP.api_actions_in_messenger.send_content_to_chat(messenger['id'], content_text)

        # Создаем новый текст сообщения для редактирования
        content_new_text = 'New Text AutomationApiTest ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        # Редактируем сообщение в персональном чате
        content_send_new_text = self.APP.api_actions_in_messenger.change_content_text(messenger['id'], content_send_text['id'], content_new_text)

        # Проверяем изменение сообщения на новый текст
        assert content_new_text == self.APP.api_actions_in_messenger.compare_content_id(messenger['id'], content_send_text['id'])

    @allure.title('Редактирование сообщения в групповом чате.')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_messenger_group_chat_change_content(self):
        # Создаем групповой чат
        messenger = self.APP.api_actions_in_messenger.create_group_chat([
            self.users['test_user01']['user_id'],
            self.users['test_user02']['user_id'],
        ])

        # Создаем текст сообщения
        content_text = 'Text AutomationApiTest ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        # Отправляем сообщение в групповой чат
        content_send_text = self.APP.api_actions_in_messenger.send_content_to_chat(messenger['id'], content_text)

        # Создаем новый текст сообщения для редактирования
        content_new_text = 'New Text AutomationApiTest ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        # Редактируем сообщение в групповом чате
        content_send_new_text = self.APP.api_actions_in_messenger.change_content_text(messenger['id'], content_send_text['id'], content_new_text)

        # Проверяем изменение сообщения на новый текст
        assert content_new_text == self.APP.api_actions_in_messenger.compare_content_id(messenger['id'], content_send_text['id'])

    @allure.title('Удаление сообщения в персональном чате.')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_messenger_personal_chat_delete_content(self):
        # Создаем персональный чат
        messenger = self.APP.api_actions_in_messenger.create_personal_chat(self.users['test_user01']['user_id'])

        # Отправляем 2 сообщения в персональный чат, для проверки удаления необходимого сообщения
        content_send_text = []
        for i in range(2):
            value = self.APP.api_actions_in_messenger.send_content_to_chat(messenger['id'])
            content_send_text.append(value['id'])
        # Удаляем выбронное сообщение (1й по списку) в персональном чате
        content_delete_text = self.APP.api_actions_in_messenger.delete_content_text(messenger['id'], content_send_text[0])
        # Формируем список id из всех сообщении с персонального чата
        content_list_id = self.APP.api_actions_in_messenger.pull_content_list_id(messenger['id'])

        # Проверяем удаление выбронного текста (1й по списку)
        assert content_send_text[0] not in content_list_id

    @allure.title('Удаление сообщения в групповом чате.')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_messenger_group_chat_delete_content(self):
        # Создаем групповой чат
        messenger = self.APP.api_actions_in_messenger.create_group_chat([
            self.users['test_user01']['user_id'],
            self.users['test_user02']['user_id'],
        ])

        # Отправляем 2 сообщения в групповой чат, для проверки удаления необходимого сообщения
        content_send_text = []
        for i in range(2):
            value = self.APP.api_actions_in_messenger.send_content_to_chat(messenger['id'])
            content_send_text.append(value['id'])
        # Удаляем выбронное сообщение (1й по списку) в групповом чате
        content_delete_text = self.APP.api_actions_in_messenger.delete_content_text(messenger['id'], content_send_text[0])
        # Формируем список id из всех сообщении с группового чата
        content_list_id = self.APP.api_actions_in_messenger.pull_content_list_id(messenger['id'])

        # Проверяем удаление выбронного текста (1й по списку)
        assert content_send_text[0] not in content_list_id
        # Проверяем количество созданных сообщении с ожидаемым (сообщение о создании группового чата + отправленные сообщения)
        assert len(content_list_id) == 2