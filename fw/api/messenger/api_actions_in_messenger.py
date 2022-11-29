import allure

from fw.api.messenger.api_messenger import ApiMessenger


class ActionsInMessenger(ApiMessenger):

    @allure.title('Создание персонального чата')
    def create_personal_chat(self, user_id):

        # Формируем тело запроса для создания персонального чата
        messenger_body = {
            'userId': user_id,
        }

        # Создаем персональный чат
        messenger = self.post_conversations_personal(messenger_body)

        return messenger

    @allure.title('Создание группового чата')
    def create_group_chat(self, users, name='AutomationApiTestChat'):

        # Формируем тело запроса для создания группового чата
        messenger_body = {
            'name': name + self.manager.time.get_date_time_Y_m_d_H_M_S(),
            'users': users,
        }

        # Создаем групповой чат
        messenger = self.post_conversations_group(messenger_body)

        return messenger

    @allure.title('Добавление пользователя в чат')
    def add_user_to_chat(self, users, messenger_id):

        # Формируем тело запроса для добавления пользователя в групповой чат
        messenger_body = {
            'users': users,
        }

        # Добавляем пользователя в чат
        self.post_conversations_id_participants(messenger_id, messenger_body)

        return

    @allure.title('Смена роли пользователя в чате')
    def change_user_role_in_chat(self, messenger_id, user_id, role='administrator'):

        # Формируем тело запроса для смены роли участника
        messenger_body = {
            'role': role,
        }

        # Меняем роль пользователя
        self.put_conversations_id_participants_userid_role(messenger_id, user_id, messenger_body)

        return

    @allure.title('Отправка сообщения')
    def send_content_to_chat(self, messenger_id, text_content=None):

        if text_content == None:
            # Подготовка данных для добавления текста в сообщении
            text_content = "Text AutomationApiTest " + self.manager.time.get_date_time_Y_m_d_H_M_S()

        # Формируем тело запроса для отправки сообщения
        content_body = {
            "content": text_content
        }

        # Отправляем сообщение
        content_send_text = self.post_conversations_id_messages(messenger_id, content_body)

        return content_send_text

    @allure.title('Список текстов из всех сообщений')
    def pull_content_list_chat(self, messenger_id, take=5, skip=0, up=True):

        # Получаем список сообщении
        content_list = self.get_conversations_id_messages(messenger_id, params={'take': take, 'skip': skip, 'up': up})

        # Формируем список текстов из всех сообщений
        content_list_texts = []
        for item in content_list:
            content_list_texts.append(item['content'])

        return content_list_texts

    @allure.title('Список id из всех сообщений')
    def pull_content_list_id(self, messenger_id, take=5, skip=0, up=True):

        # Получаем список сообщении
        content_list = self.get_conversations_id_messages(messenger_id, params={'take': take, 'skip': skip, 'up': up})

        # Формируем список текстов из всех сообщений
        content_list_id = []
        for item in content_list:
            content_list_id.append(item['id'])

        return content_list_id

    @allure.title('Редактирование сообщения')
    def change_content_text(self, messenger_id, text_id, text_content=None):

        if text_content == None:
            # Подготовка данных для добавления текста в сообщении
            text_content = "Text AutomationApiTest " + self.manager.time.get_date_time_Y_m_d_H_M_S()

        # Формируем тело запроса для отправки сообщения
        content_body = {
            "content": text_content
        }
        # Редактирование сообщения
        change_text = self.put_conversations_id_messages_messageId_content(messenger_id, text_id, content_body)

        return change_text

    @allure.title('Сравнение сообщении по id для редактирования сообщения')
    def compare_content_id(self, messenger_id, text_id, take=5, skip=0, up=True):

        # Получаем список сообщении
        content_list = self.get_conversations_id_messages(messenger_id, params={'take': take, 'skip': skip, 'up': up})

        text = []
        # Ищем редактируемое сообщение по id
        for item in content_list:
            # Сравниваем id сообщения из списка с id редактируемого сообщения
            if item['id'] == text_id:
                # Если проверка проходит, то добавляет текст из найденного сообщения
                text.append(item['content'])

        return text[0]

    @allure.title('Удаление сообщения в чате')
    def delete_content_text(self, messenger_id, text_id):
        # Удаляем сообщение
        content_text = self.delete_conversations_id_messages_messageId(messenger_id, text_id)

        return content_text