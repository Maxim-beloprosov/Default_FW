import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Comments')
@allure.story('Создание комментария, редактирование комментария, просмотр комментариев')
class TestApiComment(ApiBase):

    test_data = ['Request', 'Task', 'Project']

    @allure.title('Создание комментария к тикету.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('ticket_type', test_data)
    def test_api_comment_create_comment_in_the_ticket(self, ticket_type):
        ticket = self.create_tickets({"observers": ['test_user03']}, ticket_type=ticket_type)
        # Перелогиниваемся на обозревателя
        self.APP.api_token.get_token('test_user03')
        # Текст для коммента и проверки
        text = 'AutomationApiTest Comment ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        # Создаем комментарий
        comment = self.APP.api_actions_in_comment.create_comment(ticket['id'], text=text)
        # Сравниваем получаемые значения с ожидаемыми
        assert comment['ownerId'] == ticket['id']
        assert comment['author']['id'] == self.APP.group_data.users['test_user03']['user_id']
        assert comment['contentParts'][0]['type'] == 'Text'
        assert comment['contentParts'][0]['text'] == text

    @allure.title('Редактирование пользовательского комментария.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('ticket_type', test_data)
    def test_api_comment_edit_comment_in_the_ticket(self, ticket_type):
        ticket = self.create_tickets({"observers": ['test_user03']}, ticket_type=ticket_type)
        # Перелогиниваемся на обозревателя
        self.APP.api_token.get_token('test_user03')
        # Создаем комментарий
        comment = self.APP.api_actions_in_comment.create_comment(ticket['id'])
        # Редактируем комментарий
        comment = self.APP.api_actions_in_comment.edit_comment(comment['id'])
        #Сравниваем получаемые значения с ожидаемыми
        assert comment['contentParts'][0]['type'] == 'Text'
        assert comment['contentParts'][0]['text'] == 'AutomationApiTest Comment!'

    @allure.title('Удаление пользовательского комментария в тикете.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('ticket_type', test_data)
    def test_api_comment_delete_comment_in_the_ticket(self, ticket_type):
        ticket = self.create_tickets({"observers": ['test_user03']}, ticket_type=ticket_type)
        # Перелогиниваемся на обозревателя
        self.APP.api_token.get_token('test_user03')
        # Создаем комментарий
        comment = self.APP.api_actions_in_comment.create_comment(ticket['id'])
        # Удаляем комментарий
        comment = self.APP.api_comments.delete_comments_id(comment['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert comment['deletedBy']['id'] == self.users['test_user03']['user_id']

    @allure.title('Прочитать комментарий в тикете.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('ticket_type', test_data)
    def test_api_comment_read_comment_in_the_ticket(self, ticket_type):
        ticket = self.create_tickets({"observers": ['test_user03']}, ticket_type=ticket_type)
        # Перелогиниваемся на обозревателя
        self.APP.api_token.get_token('test_user03')
        # Создаем комментарий
        comment = self.APP.api_actions_in_comment.create_comment(ticket['id'])
        # Перелогиваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Читаем комментарий
        self.APP.api_comments.post_comments_id_read(comment['id'])
        # Получаем список комментариев тикета
        comment_list = self.APP.api_actions_in_comment.list_of_unread_comments([ticket_type])
        # Сравниваем получаемые значения с ожидаемыми.
        assert self.comment_in_the_list_of_unread_comments(comment_list, comment['id'])

    @allure.title('Прочитать все комментарии')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_comment_read_all_comments(self):
        # Создаем задачу с обозревателем
        task = self.create_task({"observers": ['test_user03']})
        # Перелогиниваемся на обозревателя
        self.APP.api_token.get_token('test_user03')
        # Создаем комментарий
        self.APP.api_actions_in_comment.create_comment(task['id'])
        # Перелогиваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Читаем все комментарии
        self.APP.api_comments.post_comments_read_all()
        # Получаем список непрочитанных комментариев
        comment_list = self.APP.api_actions_in_comment.list_of_unread_comments(['Request', 'Task', 'Project'])
        # Сравниваем получаемые значения с ожидаемыми
        assert comment_list['items'] == []

    @allure.title('Создание персонального комментария в тикете с упоминанием.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('ticket_type', test_data)
    def test_api_comment_create_personal_comment_in_the_ticket_with_mention(self, ticket_type):
        ticket = self.create_tickets({"observers": ['test_user03']}, ticket_type=ticket_type)
        # Перелогиниваемся на обозревателя
        self.APP.api_token.get_token('test_user03')
        # Создаем комментарий
        comment = self.APP.api_actions_in_comment.create_comment_with_mention(self.APP.group_data.users['test_user03']['user_id'], ticket['id'], addressee_type='User')
        # Сравниваем получаемые значения с ожидаемыми
        assert comment['ownerId'] == ticket['id']
        assert comment['author']['id'] == self.APP.group_data.users['test_user03']['user_id']
        assert comment['contentParts'][0]['type'] == 'Mention'

    @allure.title('Создание комментария с вложением к тикету.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('ticket_type', test_data)
    def test_api_comment_create_comment_with_attachment_in_the_ticket(self, ticket_type):
        ticket = self.create_tickets({"observers": ['test_user03']}, ticket_type=ticket_type)
        # Перелогиниваемся на обозревателя
        self.APP.api_token.get_token('test_user03')
        # Создаем комментарий
        comment = self.APP.api_actions_in_comment.create_comment_with_attachment(ticket['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert comment['ownerId'] == ticket['id']
        assert comment['author']['id'] == self.APP.group_data.users['test_user03']['user_id']
        assert comment['contentParts'][0]['type'] == 'Attachment'

    @allure.title('Создание комментария с изображением к тикету.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('ticket_type', test_data)
    def test_api_comment_create_comment_with_picture_in_the_ticket(self, ticket_type):
        # Создаем тикет с обозревателем
        ticket = self.create_tickets({"observers": ['test_user01']}, ticket_type=ticket_type)
        # Перелогиниваемся на обозревателя
        self.APP.api_token.get_token('test_user01')
        # Создаем комментарий
        comment = self.APP.api_actions_in_comment.create_comment_with_attachment(ticket['id'], fileId=self.APP.group_data.Attachments['Тестовое фото №1']['Id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert comment['ownerId'] == ticket['id']
        assert comment['author']['id'] == self.APP.group_data.users['test_user01']['user_id']
        assert comment['contentParts'][0]['type'] == 'Attachment'

    @allure.title('Создание пустого комментария к тикету.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/20468', name='API. КМ. Имеется возможность создать пустой комментарий.')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('ticket_type', test_data)
    @pytest.mark.skip(reason='Имеется возможность создать пустой комментарий.')
    def test_api_comment_create_empty_comment_in_the_ticket(self, ticket_type):
        ticket = self.create_tickets({"observers": ['test_user03']}, ticket_type=ticket_type)
        # Перелогиниваемся на обозревателя
        self.APP.api_token.get_token('test_user03')
        # Создаем комментарий
        comment = self.APP.api_actions_in_comment.create_comment(ticket['id'], text='')
        assert comment['status'] == 400

    @allure.title('Создание комментария к тикету без авторизации.')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('ticket_type', test_data)
    def test_api_comment_create_comment_without_authorization_in_the_ticket(self, ticket_type):
        ticket = self.create_tickets(ticket_type=ticket_type)
        # Деавторизируемся
        self.APP.settings.Authorization = False
        # Создаем комментарий
        comment = self.APP.api_actions_in_comment.create_comment(ticket['id'])
        assert comment.status_code == 401