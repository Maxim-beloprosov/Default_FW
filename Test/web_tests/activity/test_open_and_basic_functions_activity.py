import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Activity')
@allure.story('Переходы и основные действия в Ленте Активности')
class TestOpenAndBasicFunctionsActivity(WebBase):

    def setup_method(self):
        self.APP.web_any_page.open_main_page()
        self.APP.api_token.get_token('test_user09')

    correct_title_on_page_activity_feed = {
        'correct_title_rus': 'Лента активности',
        'correct_title_eng': 'Activity feed'
    }

    @allure.title('Переход к Ленте Активности сразу после авторизации')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_open_activity_after_authorization(self):
        self.APP.web_activity.page_loaded()
        # Получаем ссылку страницы после перехода
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'activity'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_activity_feed['correct_title_rus'] or actual_title == self.correct_title_on_page_activity_feed['correct_title_eng']

    @allure.title('Переход к Ленте Активности через левое боковое меню Master Layout')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_open_activity_left_menu(self):
        self.APP.web_activity.page_loaded()
        # Нажимаем на кнопку Лента Активности в левом боковом меню
        self.APP.web_any_page.click_activity()
        actual_link = self.APP.web_base.get_current_url()
        # Задаем ссылку, какая страница должна открыться
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'activity'
        # Получаем текст заголовка страницы
        actual_title = self.APP.web_any_page.get_text_title_on_page()
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link
        # Проверяем корректность заголовка страницы
        assert actual_title == self.correct_title_on_page_activity_feed['correct_title_rus'] or actual_title == self.correct_title_on_page_activity_feed['correct_title_eng']

    @allure.title('Проверка копирования ссылки Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    @pytest.mark.skip("Неверно отрабатывает копирование через pyperclip")
    def test_check_copy_link_activity(self):
        self.APP.web_activity.page_loaded()
        # Нажимаем кнопку скопировать ссылку
        actual_link = self.APP.web_activity.click_button_copy_link()
        # Задаем ссылку, которая должна быть скопирована
        correct_link = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page'] + 'activity'
        # Сравниваем 2 ссылки между собой
        assert actual_link == correct_link

    @allure.title('Проверка даты изменения тикета в Ленте Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_check_date_change_ticket_in_activity(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])
        # Выносим тип и номер тикета
        correct_info_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся инициатором
        self.APP.api_token.get_token('test_user09')
        # Запоминаем время отправки комментария
        correct_time_change_one = self.APP.time.get_time_now()
        # Переводим часы и минуты чисто в минут (1 час и 30 минут = 90 минут)
        correct_time_change_one = (int(correct_time_change_one[11:13]) * 60) + int(correct_time_change_one[14:16])
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(request['id'])
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Получаем дату изменения тикета из ленты активности
        actual_time_change = self.APP.web_activity.get_time_change_ticket_in_activity(correct_info_ticket[1])
        # Переводим часы и минуты чисто в минут (1 час и 30 минут = 90 минут)
        actual_time_change = (int(actual_time_change[0:2]) * 60) + int(actual_time_change[3:5])
        # Сравниваем информацию тикета ФР и ОР с помощью промежутка:
        # (от начала написания комментария до начала написания комментария + 2 минуты)
        assert correct_time_change_one <= actual_time_change <= (correct_time_change_one + 2)

    @allure.title('Отметить все действия как прочитанные')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_read_all_the_actions(self):
        # Создаем задачу
        task = self.create_task({"contractorId": 'test_user01'})
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(task['id'])
        # Авторизуемся исполнителем
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user01'])
        # Нажимаем на кнопку "Отметить все как прочитанное", чтобы Лента активности стала пустой
        self.APP.web_activity.click_button_read_all()
        # Проверяем, есть элемент "Нет непросмотренных активностей" на странице
        result_check = self.APP.web_activity.check_is_there_activity_on_the_page()
        # Если упал по тайм-ауту, значит нет элемента "Нет непросмотренных активностей" и следовательно, есть активности на странице
        assert result_check == True

    @allure.title('Отправить комментарий из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_send_comment_from_activity(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(request['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Отправляем комментарий
        comment_text = "TestComment AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_activity.send_comment_in_activity(type_and_number_a_ticket[1], request['id'], comment_text)
        # Переходим в нужный тикет
        self.APP.web_activity.click_number_with_need_ticket(type_and_number_a_ticket[1])
        # Возвращаем последний комментарий на странице тикета
        actual_text_comment = str(self.APP.web_tickets_base.get_last_comment_on_the_page())
        # Проверяем наличие нужного текста в последнем комментарии
        assert comment_text in actual_text_comment

    @allure.title('Отправить комментарий с адресатом из Ленты Активности через написания @ в поле для текста')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    def test_send_comment_with_address_user_from_activity_first(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(request['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Отправляем комментарий
        comment_text = "TestComment AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        address_user = self.APP.group_data.users['test_user01']['Surname'] + ' ' + self.APP.group_data.users['test_user01']['Name']
        self.APP.web_activity.send_comment_with_address_in_activity_first(type_and_number_a_ticket[1], request['id'], comment_text, address_user)
        # Переходим в нужный тикет
        self.APP.web_activity.click_number_with_need_ticket(type_and_number_a_ticket[1])
        # Возвращаем последний комментарий на странице тикета
        actual_text_comment = str(self.APP.web_tickets_base.get_last_comment_on_the_page())
        # Проверяем наличие нужного адресата в последнем комментарии
        assert address_user in actual_text_comment
        # Проверяем наличие нужного текста в последнем комментарии
        assert comment_text in actual_text_comment

    @allure.title('Отправить комментарий с адресатом из Ленты Активности через кнопку Упоминаний')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_send_comment_with_address_user_from_activity_second(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(request['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Отправляем комментарий
        comment_text = "TestComment AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        surname_and_name_address_user = self.users['test_user01']['Surname'] + ' ' + self.users['test_user01']['Name']
        self.APP.web_activity.send_comment_with_address_in_activity_second(type_and_number_a_ticket[1], request['id'], comment_text, surname_and_name_address_user)
        # Переходим в нужный тикет
        self.APP.web_activity.click_number_with_need_ticket(type_and_number_a_ticket[1])
        # Возвращаем последний комментарий на странице тикета
        actual_text_comment = self.APP.web_tickets_base.get_last_comment_on_the_page()
        # Проверяем наличие нужного адресата в последнем комментарии
        assert surname_and_name_address_user in actual_text_comment
        # Проверяем наличие нужного текста в последнем комментарии
        assert comment_text in actual_text_comment

    @allure.title('Проверка комментария от другого пользователя')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_check_comment_from_another_user(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        correct_comment = 'AutomationWebTest Comment ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_actions_in_comment.create_comment(request['id'], correct_comment)
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Проверяем комментарий от другого пользователя
        actual_comment = self.APP.web_activity.get_last_comment_in_activity(type_and_number_a_ticket[1])
        assert correct_comment == actual_comment

    @allure.title('Отправить комментарий с одним вложением из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_send_comment_with_one_attachment_from_activity(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(request['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Отправляем комментарий
        comment_text = "TestComment AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_activity.send_comment_with_attachments_in_activity(type_and_number_a_ticket[1], request['id'], comment_text, 1)
        # Переходим в нужный тикет
        self.APP.web_activity.click_number_with_need_ticket(type_and_number_a_ticket[1])
        # Возвращаем последний комментарий на странице тикета
        actual_text_comment = self.APP.web_tickets_base.get_last_comment_on_the_page()
        # Проверяем наличие нужного текста в последнем комментарии
        assert comment_text in actual_text_comment

    @allure.title('Отправить комментарий с двумя вложениями из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_send_comment_with_two_attachment_from_activity(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        self.APP.api_actions_in_comment.create_comment(request['id'])
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Отправляем комментарий
        comment_text = "TestComment AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_activity.send_comment_with_attachments_in_activity(type_and_number_a_ticket[1], request['id'], comment_text, 2)
        # Переходим в нужный тикет
        self.APP.web_activity.click_number_with_need_ticket(type_and_number_a_ticket[1])
        # Возвращаем последний комментарий на странице тикета
        actual_text_comment = self.APP.web_tickets_base.get_last_comment_on_the_page()
        # Проверяем наличие нужного текста в последнем комментарии
        assert comment_text in actual_text_comment

    @allure.title('Ответить на комментарий в Ленте Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_answering_to_comment_from_activity(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        comment = "TestComment AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_actions_in_comment.create_comment(request['id'], comment)
        # Выносим тип и номер тикета
        type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Отвечаем на комментарий
        answer_text = "TestAnswer AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_activity.answering_to_comment(request['id'], comment, answer_text)
        # Переходим в нужный тикет
        self.APP.web_activity.click_number_with_need_ticket(type_and_number_a_ticket[1])
        # Возвращаем последний комментарий на странице тикета
        actual_text_comment = self.APP.web_tickets_base.get_last_comment_on_the_page()
        # Проверяем наличие нужного текста в последнем комментарии
        assert answer_text in actual_text_comment

    @allure.title('Перейти к комментарию из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_move_to_comment_from_activity(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Пишем комментарий, чтобы заявка отобразилась в Ленте Активности
        comment = "TestComment AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_actions_in_comment.create_comment(request['id'], comment)
        # Выносим тип и номер тикета
        correct_type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим к комментарию в тикет
        self.APP.web_activity.click_button_move_to_comment(comment)
        # Получаем актуальный тип и номер тикета
        actual_type_and_number_a_ticket = self.APP.web_tickets_base.get_type_and_number_ticket()
        # Возвращаем последний комментарий на странице тикета
        actual_text_comment = self.APP.web_tickets_base.get_last_comment_on_the_page()
        # Сравниваем тип и номер тикета, туда ли мы перешли
        assert correct_type_and_number_a_ticket[1] == actual_type_and_number_a_ticket[1]
        # Перевожу в нижний регистр тип тикета (Task = task)
        assert (correct_type_and_number_a_ticket[0]).lower() == (actual_type_and_number_a_ticket[0]).lower()
        # Проверяем наличие нужного текста в последнем комментарии
        assert comment in actual_text_comment

    @allure.title('Прочитать комментарий из Ленты Активности')
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_read_to_comment_from_activity(self):
        # Создаем заявку
        request = self.create_request({"descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся участником ГО
        self.APP.api_token.get_token('test_user01')
        # Пишем первый комментарий, чтобы заявка отобразилась в Ленте Активности
        comment_first = "TestComment AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_actions_in_comment.create_comment(request['id'], comment_first)
        # Пишем второй комментарий, чтобы их было несколько
        comment_second = "TestComment AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_actions_in_comment.create_comment(request['id'], comment_second)
        # Выносим тип и номер тикета
        correct_type_and_number_a_ticket = [request['ticketType'], request['docNumber']]
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Читаем комментарий
        self.APP.web_activity.click_button_read_to_comment(comment_second)
        # Обновляем страницу, чтобы структура html обновилась
        self.APP.web_base.refresh_the_page()
        # Получаем текст комментариев в нужном тикете
        text_comments = self.APP.web_activity.get_text_comments_in_need_ticket(correct_type_and_number_a_ticket[1])
        # Проверяем, есть ли нужный нам комментарий (который прочитали) в списке комментариев в данный момент
        actual_result = self.APP.web_activity.check_is_there_need_text_in_list(text_comments, comment_second)
        assert actual_result