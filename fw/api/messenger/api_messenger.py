import allure

from fw.api.api_base import APIBase


class ApiMessenger(APIBase):

    @allure.step('Создает персональный чат с пользователем. POST /api/Conversations/personal')
    def post_conversations_personal(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Conversations/personal', body, params)

    @allure.step('Возвращает список чатов текущего пользователя. GET /api/Conversations/')
    def get_conversations(self, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Conversations/', params)

    @allure.step('Создает групповой чат с пользователем. POST /api/Conversations/group')
    def post_conversations_group(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Conversations/group', body, params)

    @allure.step('Возвращает список пользователей чата. GET /api/Conversations/{id}/participants')
    def get_conversations_id_participants(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Conversations/{id}/participants', params)

    @allure.step('Добавляет пользователей к чату. POST /api/Conversations/{id}/participants')
    def post_conversations_id_participants(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Conversations/{id}/participants', body, params)

    @allure.step('Исключает пользователей из чата. DELETE /api/Conversations/{id}/participants')
    def delete_conversations_id_participants(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/Conversations/{id}/participants', params=params)

    @allure.step('Изменяет роль участника. PUT /api/Conversations/{id}/participants/{userid}/role')
    def put_conversations_id_participants_userid_role(self, id, userid, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Conversations/{id}/participants/{userid}/role', body, params)

    @allure.step('Возвращает список идентификаторов пользователей чата. GET /api/Conversations/{id}/participantids')
    def get_conversations_id_participantids(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Conversations/{id}/participantids', params)

    @allure.step('Удаляет чат. DELETE /api/Conversations/{id}')
    def delete_conversations_id(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/Conversations/{id}', params)

    @allure.step('Пользователь покидает чат. DELETE /api/Conversations/{id}/participants/current')
    def delete_conversations_id_participants_current(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/Conversations/{id}/participants/current', params)

    @allure.step('Возвращает количество чатов с непрочитанными сообщениями. GET /api/Conversationse/unreaded/count')
    def get_conversations_unread_count(self, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Conversations/unreaded/count', params)

    @allure.step('Поиск по всем сообщениям. GET /api/Conversations/search/messages/')
    def get_conversations_search_messages(self, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Conversations/search/messages/', params)

    @allure.step('Поиск по чатам. GET /api/Conversations/search/сonversations/')
    def get_conversations_search_сonversations(self, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Conversations/search/сonversations/', params)

    @allure.step('Изменяет наименование чата. PUT /api/Conversations/{id}/name')
    def put_conversations_id_name(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Conversations/{id}/name', body, params)

    # Chatting. Общение в чате
    @allure.step('Возращает переписку в группе. GET /api/Conversations/{id}/messages')
    def get_conversations_id_messages(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Conversations/{id}/messages', params)

    @allure.step('Создает текстовое сообщение в чате. POST /api/Conversations/{id}/messages')
    def post_conversations_id_messages(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Conversations/{id}/messages', body, params)

    @allure.step('Пересылает текстовые сообщения в другой чат. POST /api/Conversations/{id}/forward')
    def post_conversations_id_forward(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Conversations/{id}/forward', body, params)

    @allure.step('Удаляет сообщение. DELETE /api/Conversations/{id}/messages/{messageId}')
    def delete_conversations_id_messages_messageId(self, id, messageId, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/Conversations/{id}/messages/{messageId}', params)

    @allure.step('Удаляет несколько сообщений. DELETE /api/Conversations/{id}/messages/')
    def delete_conversations_id_messages(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/Conversations/{id}/messages/', params)

    @allure.step('Изменяет текстовое сообщение. PUT /api/Conversations/{id}/messages/{messageId}/content')
    def put_conversations_id_messages_messageId_content(self, id, messageId, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Conversations/{id}/messages/{messageId}/content', body, params)