import allure

from fw.api.comments.api_comments import ApiComments


class ActionsInComment(ApiComments):

    @allure.title('Создание комментария')
    def create_comment(self, ticket_id, text=None, comment_mass={}, params=None):
        if text == None:
            text = 'AutomationApiTest Comment ' + self.manager.time.get_date_time_Y_m_d_H_M_S()

        # Формируем тело запроса для создания комментария
        comment_body = {
            'contentParts': [
                {
                    'type': 'Text',
                    'text': text,
                }
            ]
        }

        if 'type' in comment_mass:
            comment_body['contentParts'][0]['type'] = comment_mass['type']
        if 'text' in comment_mass:
            comment_body['contentParts'][0]['type'] = comment_mass['text']


        # Создаем комментарий
        comment = self.post_comments(comment_body, params={'ownerId': ticket_id})

        return comment

    @allure.title('Создание комментария с упоминанием')
    def create_comment_with_mention(self, addressees_id, ticket_id, addressee_type='Contractor', text='AutomationApiTest Comment'):

        # Формируем тело запроса для комментария
        request_body = {
            'contentParts': [
                {
                    'type': 'Mention',
                    'addresseeType': addressee_type,
                    'userId': addressees_id
                },
                {
                    'type': 'Text',
                    'text': text
                }],
        }

        # Оставляем комментарий
        comment = self.post_comments(request_body, params={'ownerId': ticket_id})

        return comment

    @allure.title('Редактирование комментария')
    def edit_comment(self, comment_id, type='Text', text='AutomationApiTest Comment!'):

        # Формируем тело запроса для редактирования комментария
        comment_body = {
            'contentParts': [
                {
                    'type': type,
                    'text': text,
                }
            ]
        }

        # Редактируем комментарий
        comment = self.put_comments_id(comment_id, comment_body)

        return comment

    @allure.title('Получение списка непрочитанных комментариев')
    def list_of_unread_comments(self, ownerTypes):

        # Подготовка тела запроса для получения списка непрочитанных комментариев
        comment_body = {
            'ownerTypes': ownerTypes,
            'skip': 0,
            'take': 10,
        }

        # Получаем список непрочитанных комментариев
        comment = self.post_comments_activity_tape(comment_body)

        return comment

    @allure.title('Создание комментария с вложением')
    def create_comment_with_attachment(self, ticket_id, fileId=None, params=None):

        # Формируем тело запроса для создания комментария
        comment_body = {
            'contentParts': [
                {
                    'type': 'Attachment',
                    'fileId': "62cc19b2d80491cde982ebc4",
                }
            ]
        }
        if fileId:
            comment_body['contentParts'][0]['fileId'] = fileId

        # Создаем комментарий
        comment = self.post_comments(comment_body, params={'ownerId': ticket_id})

        return comment

    @allure.title('Получить список комментариев')
    def get_list_comments(self, owner_id, created_date_from=None, created_date_to=None, skip=0, take=20, is_moderator_mode="false"):

        list_comments = self.get_comments(params={'ownerId': owner_id,
                                                  "createdDateFrom": created_date_from, "createdDateTo": created_date_to, "skip": skip, "take": take, "isModeratorMode": is_moderator_mode})
        return list_comments