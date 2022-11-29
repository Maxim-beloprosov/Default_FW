import time
import allure
import pyperclip

from selenium.webdriver.common.by import By
from fw.web.AnyPage import AnyPage


class Locator:
    activity_subheader = (By.XPATH, '//div[@class="ck-body-wrapper"]')
    header_link = (By.XPATH, '//div[@class="header-link"]')
    empty_activity = (By.XPATH, '//div[@class ="activity-wrap__empty-text"]')
    button_read_all = (By.XPATH, '//div[@class="page-header__title-line"]//button[contains(@class, "head__read-all-btn")]')
    ticket_comment_iframe = (By.XPATH, '//div[@test_id="comment-create"]//p')
    cke_editable_themed_comment = (By.XPATH, '//body/p')
    send_comment = (By.XPATH, '//div[@class="comments"]//span[contains(text(),"Отправить")]')
    cancel_or_reject_or_appeal_description = (By.XPATH, '//div[@test_id="action-null-description"]/textarea')
    cke_1_contents = (By.XPATH, '//div[@id="cke_1_contents"]')
    cancel_or_reject_or_appeal_submit_btn = (By.CSS_SELECTOR, '[test_id="actionnullsubmit-btn"]')
    block_for_text_in_comment = (By.XPATH, '(//iframe)[1]')
    block_text_for_cancel = (By.XPATH, '//div[@test_id="action-Cancel-description"]/textarea')
    block_text_for_reject = (By.XPATH, '//div[@test_id="action-Reject-description"]/textarea')
    block_text_for_appeal = (By.XPATH, '//div[@test_id="action-Appeal-description"]/textarea')
    button_apply_cancel = (By.XPATH, '//button[@test_id="actionCancelsubmit-btn"]')
    button_apply_reject = (By.XPATH, '//button[@test_id="actionRejectsubmit-btn"]')
    button_apply_appeal = (By.XPATH, '//button[@test_id="actionAppealsubmit-btn"]')
    closed_description = (By.XPATH, '//div[@test_id="action-MarkAndClose-description"]/textarea')
    closed_submit_btn = (By.XPATH, '//button[@test_id="action-MarkAndClose-submit-btn"]')
    return_to_rework_description = (By.XPATH, '//div[@test_id="action-ReturnToRework-description"]/textarea')
    return_to_rework_submit_btn = (By.XPATH, '//button[@test_id="action-ReturnToRework-submit-btn"]')


class Activity(AnyPage):

    def page_loaded(self):
        self.find_element(Locator.activity_subheader)
        return self

    @allure.step('Нажать на кнопку Скопировать ссылку')
    def click_button_copy_link(self):
        self.click_element(Locator.header_link)
        actual_link = pyperclip.paste()
        time.sleep(0.5)
        return actual_link

    @allure.step('Возвращаем дату изменения тикета в Ленте Активности')
    def get_time_change_ticket_in_activity(self, ticket_number):
        # Получаем время изменения тикета
        block_time_create_ticket = (By.XPATH, f'//a[contains(text(),"{ticket_number}")]/../../../../..//div[@class="activity-item__date"]/div[1]')
        actual_time_change_ticket = self.get_tag_text(block_time_create_ticket)
        return actual_time_change_ticket

    @allure.step('Нажать на кнопку Отметить все как прочитанное')
    def click_button_read_all(self):
        self.page_loaded()
        self.click_element(Locator.button_read_all)
        self.find_element(Locator.empty_activity)
        return self

    @allure.step('Проверка, есть ли активности на странице')
    def check_is_there_activity_on_the_page(self):
        result = self.check_is_there_element_on_the_page(Locator.empty_activity)
        return result

    @allure.step('Возвращаем статус тикета из Ленты Активности')
    def get_status_ticket_from_activity(self, number_ticket):
        status_ticket_in_activity = (By.XPATH, f'//div[@class="feed-item-info"]//a[contains(text(),"{number_ticket}")]/..//div[contains(@class, "ticket-status__status")]')
        actual_status = self.get_tag_text(status_ticket_in_activity)
        return actual_status

    @allure.step('Нажать на номер нужного тикета')
    def click_number_with_need_ticket(self, ticket_number):
        button_ticket_with_need_number = (By.XPATH, f'//div[@class="feed-item-info"]//a[contains(text(),"{ticket_number}")]')
        self.scroll_to_element(button_ticket_with_need_number)
        self.click_element(button_ticket_with_need_number)
        return self

    @allure.step('Нажимаем на блок комментариев, чтобы отобразилось поле для ввода текста')
    def click_comments_block(self, number_ticket):
        # Ожидаем, пока страница загрузится
        self.page_loaded()
        block_comment = (By.XPATH, f'//div[@class="feed-item-info"]//a[contains(text(),"{number_ticket}")]/../../..//input[@test_id="comment-input"]')
        # Скроллим к полю блока комментариев
        self.scroll_to_element(block_comment)
        # Нажимаем на блок комментариев
        self.click_element(block_comment)
        return self

    @allure.step('Кнопка отправки комментария')
    def button_send_comment(self):
        self.click_element(Locator.send_comment)
        return self

    @allure.step('Отправить комментарий без адресата в Ленте Активности ')
    def send_comment_without_address_in_activity(self, number_ticket, comment_text):
        # Нажимаем на блок комментариев, чтобы раскрылось поле ввода
        self.click_comments_block(number_ticket)
        # Набираем текст в поле ввода
        self.fill_comment_without_delete_text(comment_text)
        # Отправляем комментарий
        self.button_send_comment()
        # Ждем, пока комментарий с нужным текстом появится
        locator_text_comment = (By.XPATH, f'//p[contains(text(),"{comment_text}")]')
        self.find_element(locator_text_comment)
        return self

    @allure.step('Выбрать адресата для комментария через написания @ в поле для текста')
    def select_address_user_for_comment_first(self, user):
        # Набираем текст в поле ввода
        self.fill_comment_with_delete_text('@')
        time.sleep(0.3)
        # Нажимаем на нужного пользователя
        block_user = (By.XPATH, f'//div[@class="mention-tooltip"]//div[contains(text(),"{user}")]')
        self.move_to_element(block_user)
        self.click_element(block_user)
        # Ожидаем, пока появится текст
        wait_text = (By.XPATH, f'//a[contains(text(), "@{user}")]')
        self.find_element(wait_text)
        return self

    @allure.step('Выбрать адресата для комментария через кнопку @ рядом со вложениями')
    def select_address_user_for_comment_second(self, number_ticket, surname_and_name_user):
        # Нажимаем на кнопку Упоминание
        self.button_address_user(number_ticket)
        # Нажимаем на нужного пользователя
        block_user = (By.XPATH, f'//div[@class="ticket-user__info"]/div[contains(text(),"{surname_and_name_user}")]')
        self.move_to_element(block_user)
        self.click_element(block_user)
        return self

    @allure.step('Ожидаем нужный комментарий в тикете')
    def waiting_the_need_comment_in_ticket(self, id_ticket, text_comment):
        # Получаем информацию о тикете с сервера (через API)
        information_comment_in_ticket = self.manager.api_actions_in_comment.get_list_comments(id_ticket)

        # Ждем момента, когда появится информация о нужном комментарии в тикете с сервера
        # Вводим счетчик времени, чтобы цикл не был бесконечным
        count_of_time = 0
        # Ожидаем, пока статус в тикете будет соответствовать ожидаемому
        while True:
            # Перебираем все комментарии
            for items in information_comment_in_ticket['items']:
                # Перебираем типы комментариев
                for contentParts in items['contentParts']:
                    # Проверяем, есть ли текст
                    if 'text' in contentParts:
                        # Проверяем, есть ли нужный нам текст комментария
                        if text_comment in contentParts['text']:
                            return self
            else:
                # Если нужного комментария нет, то ожидаем 1.5 секунды и снова запрашиваем информацию о тикете с сервера
                time.sleep(1.5)
                count_of_time = count_of_time + 2
                information_comment_in_ticket = self.manager.api_actions_in_comment.get_list_comments(id_ticket)
                # Проверяем, если общее время ожидания больше максимального времени ожидаемого, то прерываем все циклы
                if count_of_time == self.manager.settings.time_element_Wait:
                    raise

    @allure.step('Отправить комментарий с адресатом в Ленте Активности через написание @ в поле ввода текста')
    def send_comment_with_address_in_activity_first(self, number_ticket, id_ticket, comment_text, surname_and_name_user):
        # Нажимаем на блок комментариев, чтобы раскрылось поле ввода
        self.click_comments_block(number_ticket)
        # Выбираем адресата для комментария
        self.select_address_user_for_comment_first(surname_and_name_user)
        # Набираем текст в поле ввода
        self.fill_comment_without_delete_text(comment_text)
        # Отправляем комментарий
        self.button_send_comment()
        # Ожидаем, когда комментарий будет в информации тикета на сервере
        self.waiting_the_need_comment_in_ticket(id_ticket, comment_text)
        return self

    @allure.step('Отправить комментарий с адресатом в Ленте Активности через кнопку Упоминаний')
    def send_comment_with_address_in_activity_second(self,number_ticket, id_ticket, comment_text, surname_and_name_user):
        # Нажимаем на блок комментариев, чтобы раскрылось поле ввода
        self.click_comments_block(number_ticket)
        # Выбираем адресата для комментария
        self.select_address_user_for_comment_second(number_ticket, surname_and_name_user)
        # Набираем текст в поле ввода
        self.fill_comment_without_delete_text(comment_text)
        # Отправляем комментарий
        self.button_send_comment()
        # Ожидаем, когда комментарий будет в информации тикета на сервере
        self.waiting_the_need_comment_in_ticket(id_ticket, comment_text)
        return self

    @allure.step('Заполнение поля комментарий без удаления предыдущего текста')
    def fill_comment_without_delete_text(self, comment_text):
        time.sleep(0.3)
        # Вводим текст в поле комментария
        self.send_keys(Locator.ticket_comment_iframe, comment_text)
        return self

    @allure.step('Заполнение поля комментарий с удалением предыдущего текста')
    def fill_comment_with_delete_text(self, comment_text):
        time.sleep(0.3)
        # Вводим текст в поле комментария
        self.send_keys(Locator.ticket_comment_iframe, comment_text)
        return self

    @allure.step('Отправить комментарий в Ленте Активности')
    def send_comment_in_activity(self, number_ticket, id_ticket, comment_text):
        # Нажимаем на блок комментариев, чтобы раскрылось поле ввода
        self.click_comments_block(number_ticket)
        # Набираем текст в поле ввода
        self.fill_comment_without_delete_text(comment_text)
        # Отправляем комментарий
        self.button_send_comment()
        # Ожидаем, когда комментарий будет в информации тикета на сервере
        self.waiting_the_need_comment_in_ticket(id_ticket, comment_text)
        return self

    @allure.step('Нажать кнопку Вложения')
    def button_attachments(self, number_ticket):
        button_attachments = (By.XPATH, f'//div[@class="feed-item-info"]//a[contains(text(),"{number_ticket}")]/../../..//div[@class="toolbar toolbar_btn-blue"]/button[@data-manual="toolbar-file"]')
        self.click_element(button_attachments)
        return self

    @allure.step('Отправить комментарий cо вложениями в Ленте Активности')
    def send_comment_with_attachments_in_activity(self, number_ticket, id_ticket, comment_text, count_attachments):
        # Нажимаем на блок комментариев, чтобы раскрылось поле ввода
        self.click_comments_block(number_ticket)
        # Нажимаем на кнопку Вложения
        self.button_attachments(number_ticket)
        # Вводим цикл для добавления вложений
        for i in range(1, count_attachments + 1):
            # Задаем название вложения для поиска и выбора
            name_attachment = 'Тестовое фото №' + str(i)
            # Ищем нужное нам вложение
            self.search_attachment(number_ticket, name_attachment)
            # Выбираем нужное нам вложение
            self.select_attachment(name_attachment)
        self.click_button_attach(number_ticket)
        # Набираем текст в поле ввода
        self.fill_comment_without_delete_text(comment_text)
        # Отправляем комментарий
        self.button_send_comment()
        # Ожидаем, когда комментарий будет в информации тикета на сервере
        self.waiting_the_need_comment_in_ticket(id_ticket, comment_text)
        return self

    @allure.step('Выбор вложения')
    def select_attachment(self, name_attachment):
        need_attachment = (By.XPATH, f'//div[contains(text(),"{name_attachment}")]/../../../../../../../..//span[@class="checkmark checkmark_blue "]')
        self.move_to_element(need_attachment)
        self.click_element(need_attachment)
        return self

    @allure.step('Поиск вложения')
    def search_attachment(self, number_ticket, name_attachment):
        search_block = (By.XPATH, f'(//div[@class="feed-item-info"]//a[contains(text(),"{number_ticket}")]/../../..//input[@test_id="custom-input"])[1]')
        self.clear_and_send_keys(search_block, name_attachment)
        return self

    @allure.step('Нажать кнопку Прикрепить')
    def click_button_attach(self, number_ticket):
        button_attach = (By.XPATH, f'(//div[@class="feed-item-info"]//a[contains(text(),"{number_ticket}")]/../../..//div[@class="modal-attach-file__bottom-panel"]/button)[1]')
        self.click_element(button_attach)
        return self

    @allure.step('Нажать кнопку Упоминание (Адресат для комментария)')
    def button_address_user(self, number_ticket):
        button_address_user = (By.XPATH, f'//div[@class="feed-item-info"]//a[contains(text(),"{number_ticket}")]/../../..//div[@class="toolbar toolbar_btn-blue"]//div[@test_id="toolbar-mention"]')
        self.click_element(button_address_user)
        return self

    @allure.step('Получить последний комментарий в нужной заявке из Ленты Активности')
    def get_last_comment_in_activity(self, number_ticket):
        last_comment = (By.XPATH, f'(//a[contains(text(),"{number_ticket}")]/../../..//div[@class="feed-item-wrap__comments"]//p[@class="cke-text"])[1]')
        last_comment = self.get_tag_text(last_comment)
        return last_comment

    @allure.step('Проверка адресата в комментарии в Ленте Активности')
    def check_address_user_in_comment_in_activity(self, number_ticket, user):
        user = '@' + user['Surname'] + ' ' + user['Name']
        check_address_user = (By.XPATH, f'//a[contains(text(),"{number_ticket}")]/../..//a[contains(text(),"{user}")]')
        self.find_element(check_address_user)
        return self

    @allure.step('Ответить на комментарий')
    def answering_to_comment(self,id_ticket, comment, answer_text):
        # Нажимаем кнопку Ответить на комментарий с нужный текстом
        button_answer_to_comment = (By.XPATH, f'//p[contains(text(),"{comment}")]/../../../../..//button[@test_id="comment-response"]')
        self.click_element(button_answer_to_comment)
        # Вводим текст в поле комментария
        self.fill_comment_without_delete_text(answer_text)
        # Нажимаем кнопку Отправить
        self.button_send_comment()
        # Ожидаем, когда комментарий будет в информации тикета на сервере
        self.waiting_the_need_comment_in_ticket(id_ticket, answer_text)
        return self

    @allure.step('Навести курсор на кнопку действия с комментарием')
    def move_point_to_actions_with_comment(self, comment):
        button_actions = (By.XPATH, f'//p[contains(text(),"{comment}")]/../../../../..//div[@test_id="comment-more"]/button')
        self.move_to_element(button_actions)
        return self

    @allure.step('Нажать кнопку Прочитать комментарий')
    def click_button_read_to_comment(self, comment):
        # Наводим курсор на кнопку действий с комментарием
        self.move_point_to_actions_with_comment(comment)
        # Нажимаем кнопку Прочитать комментарий
        button_read_to_comment = (By.XPATH, f'//p[contains(text(),"{comment}")]/../../../../..//div[@test_id="comment-more"]/button//div[@test_id="read-comment"]')
        self.click_element(button_read_to_comment)
        return self

    @allure.step('Нажать кнопку Перейти к комментарию')
    def click_button_move_to_comment(self, comment):
        # Наводим курсор на кнопку действий с комментарием
        self.move_point_to_actions_with_comment(comment)
        # Нажимаем кнопку Перейти к комментарию
        button_move_to_comment = (By.XPATH, f'//p[contains(text(),"{comment}")]/../../../../..//div[@test_id="comment-more"]/button//div[@test_id="go-to-comment"]')
        self.scroll_to_element(button_move_to_comment)
        self.click_element(button_move_to_comment)
        self.move_to_last_page_in_browser()
        return self

    @allure.step('Получаем текст комментариев в нужном тикете')
    def get_text_comments_in_need_ticket(self, number_ticket):
        comments_in_ticket = (By.XPATH, f'//a[contains(text(),"{number_ticket}")]/../../..//div[@class="comments__list"]//p[@class="cke-text"]')
        count = len(self.find_elements(comments_in_ticket))
        list = []
        for i in range(1, count + 1):
            text_comments = (By.XPATH, f'(//a[contains(text(),"{number_ticket}")]/../../..//div[@class="comments__list"]//p[@class="cke-text"])[{i}]')
            text = self.get_tag_text(text_comments)
            list.append(text)
        return list

    @allure.step('Проверяем, есть ли нужный текст в списке')
    def check_is_there_need_text_in_list(self, list, text):
        if text in list:
            return False
        else:
            return True

    @allure.step('Перевести тикет в проверку')
    def send_ticket_for_resolve(self, type_and_number_a_ticket):
        action_resolve_btn = (By.XPATH, f'//a[contains(text(),"{type_and_number_a_ticket[1]}")]/../..//div[@test_id="Action-Resolve"]')
        self.scroll_to_element(action_resolve_btn)
        self.click_element(action_resolve_btn)
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        self.manager.web_tickets_base.waiting_the_correct_status(
            self.manager.group_data.Status_ticket['ENG']['В проверке'], type_and_number_a_ticket)
        # Обозначаем корректный статус тикета
        correct_status = self.manager.group_data.Status_ticket['project']['RUS']['В проверке']
        return correct_status

    @allure.step('Отменить тикет')
    def canceling_of_ticket(self, type_and_number_a_ticket):
        # Кнопка отмены тикета
        action_cancel_btn = (By.XPATH, f'//a[contains(text(),"{type_and_number_a_ticket[1]}")]/../..//div[@test_id="Action-Cancel"]')
        self.scroll_to_element(action_cancel_btn)
        self.click_element(action_cancel_btn)
        self.send_reason_and_cancel_ticket("TestReasonCanceled AutomationWebTests " + self.manager.time.get_date_time_Y_m_d_H_M_S())
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        self.manager.web_tickets_base.waiting_the_correct_status(self.manager.group_data.Status_ticket['ENG']['Отменено'], type_and_number_a_ticket)
        # Обозначаем корректный статус тикета
        if type_and_number_a_ticket[0] == 'Project' or type_and_number_a_ticket[0] == 'project':
            correct_status = self.manager.group_data.Status_ticket['project']['RUS']['Отменён']
        else:
            correct_status = self.manager.group_data.Status_ticket['request_and_task']['RUS']['Отменена']
        return correct_status

    @allure.step('Причина отмены, отклонения или апеллирования тикета')
    def reason_cancel_or_reject_or_appeal(self, text_reason):
        # Указываем причину
        self.click_element(Locator.cancel_or_reject_or_appeal_description)
        self.send_keys_slow(Locator.cancel_or_reject_or_appeal_description, text_reason, 100)
        # Кнопка подтверждения отмены, отклонения или апеллирования тикета
        self.click_element(Locator.cancel_or_reject_or_appeal_submit_btn)
        return self

    @allure.step('Заполнить причину и отменить тикет')
    def send_reason_and_cancel_ticket(self, text_reason):
        # Указываем причину
        self.click_element(Locator.block_text_for_cancel)
        self.send_keys_slow(Locator.block_text_for_cancel, text_reason, 100)
        # Кнопка подтверждения отмены, отклонения или апеллирования тикета
        self.click_element(Locator.button_apply_cancel)
        return self

    @allure.step('Заполнить причину и отклонить тикет')
    def send_reason_and_reject_ticket_from_activity(self, text_reason):
        # Указываем причину
        self.click_element(Locator.block_text_for_reject)
        self.send_keys_slow(Locator.block_text_for_reject, text_reason, 100)
        # Кнопка подтверждения отмены, отклонения или апеллирования тикета
        self.click_element(Locator.button_apply_reject)
        return self

    @allure.step('Вернуть тикет в работу')
    def comeback_a_ticket_in_work_from_activity(self, type_and_number_a_ticket):
        button_comeback_a_ticket_in_work = (By.XPATH, f'//a[contains(text(),"{type_and_number_a_ticket[1]}")]/../..//div[@test_id="Action-BackToWork"]')
        self.scroll_to_element(button_comeback_a_ticket_in_work)
        self.click_element(button_comeback_a_ticket_in_work)
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        self.manager.web_tickets_base.waiting_the_correct_status(
            self.manager.group_data.Status_ticket['ENG']['В работе'], type_and_number_a_ticket)
        # Обозначаем корректный статус тикета
        correct_status = self.manager.group_data.Status_ticket['request_and_task']['RUS']['В работе']
        return correct_status

    @allure.step('Нажимаем на кнопку Уточнения')
    def click_button_clarification(self, number_ticket):
        button_clarification = (By.XPATH, f'//a[contains(text(),"{number_ticket}")]/../../..//div[@class="toolbar__submit"]//div[@class="button__after-content"]/div[1]')
        self.click_element(button_clarification)
        return self

    @allure.step('Нажать кнопку Уточнить у инициатора')
    def button_ask_initiator_clarification(self, number_ticket):
        # Нажимаем на кнопку уточнения
        self.click_button_clarification(number_ticket)
        # Нажимаем Уточнить у инициатора
        ask_initiator = (By.XPATH, f'//a[contains(text(),"{number_ticket}")]/../../../../../../../../../../..//div[@test_id="comment-check-with-initiator"]')
        self.click_element(ask_initiator)
        return self

    @allure.step('Нажать кнопку Уточнить у исполнителя')
    def button_ask_contractor_clarification(self, number_ticket):
        # Нажимаем на кнопку уточнения
        self.click_button_clarification(number_ticket)
        # Нажимаем Уточнить у инициатора
        ask_contractor = (By.XPATH, f'//a[contains(text(),"{number_ticket}")]/../../../../../../../../../../..//div[@test_id="comment-check-with-contractor"]')
        self.click_element(ask_contractor)
        return self

    @allure.step('Задать уточнение инициатору из Ленты Активности')
    def ask_initiator_clarification_from_activity(self, type_and_number_a_ticket, comment_text=None):
        # Кликаем на блок комментариев, чтобы появилось поле для ввода текста
        self.click_comments_block(type_and_number_a_ticket[1])
        # Вводим текст в поле комментария
        if comment_text == None:
            comment_text = "TestClarificationForInitiator AutomationWebTests " + self.manager.time.get_date_time_Y_m_d_H_M_S()
        self.fill_comment_without_delete_text(comment_text)
        # Нажимаем кнопку Уточнить у инициатора
        self.button_ask_initiator_clarification(type_and_number_a_ticket[1])
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        self.manager.web_tickets_base.waiting_the_correct_status(
            self.manager.group_data.Status_ticket['ENG']['На уточнении у иниц.'], type_and_number_a_ticket)
        return self

    @allure.step('Задать уточнение исполнителю из Ленты Активности')
    def ask_contractor_clarification_from_activity(self, type_and_number_a_ticket, comment_text=None):
        # Кликаем на блок комментариев, чтобы появилось поле для ввода текста
        self.click_comments_block(type_and_number_a_ticket[1])
        # Вводим текст в поле комментария
        if comment_text == None:
            comment_text = "TestClarificationForContractor AutomationWebTests " + self.manager.time.get_date_time_Y_m_d_H_M_S()
        self.fill_comment_without_delete_text(comment_text)
        # Нажимаем кнопку Уточнить у инициатора
        self.button_ask_contractor_clarification(type_and_number_a_ticket[1])
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        self.manager.web_tickets_base.waiting_the_correct_status(
            self.manager.group_data.Status_ticket['ENG']['На уточнении у исп.'], type_and_number_a_ticket)
        return self

    @allure.step('Отклонить согласование')
    def reject_the_agreement_from_activity(self, type_and_number_a_ticket):
        reject_the_agreement = (By.XPATH, f'//a[contains(text(),"{type_and_number_a_ticket[1]}")]/../..//div[@test_id="Action-Reject"]')
        self.scroll_to_element(reject_the_agreement)
        # Нажимаем кнопку Отклонить
        self.click_element(reject_the_agreement)
        # Вводим текст причины и подтверждаем отклонение тикета
        self.send_reason_and_reject_ticket_from_activity("TestReasonRejected AutomationWebTests " + self.manager.time.get_date_time_Y_m_d_H_M_S())
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        self.manager.web_tickets_base.waiting_the_correct_status(self.manager.group_data.Status_ticket['ENG']['Отклонено'], type_and_number_a_ticket)
        # Обозначаем корректный статус тикета
        if type_and_number_a_ticket[0] == 'Project' or type_and_number_a_ticket[0] == 'project':
            correct_status = self.manager.group_data.Status_ticket['project']['RUS']['Отклонён']
        else:
            correct_status = self.manager.group_data.Status_ticket['request_and_task']['RUS']['Отклонена']
        return correct_status

    @allure.step('Принять согласование')
    def accept_the_agreement_from_activity(self, number_ticket):
        accept_the_agreement = (By.XPATH, f'//a[contains(text(),"{number_ticket}")]/../..//div[@test_id="Action-Approve"]')
        self.scroll_to_element(accept_the_agreement)
        self.click_element(accept_the_agreement)
        return self

    @allure.step('Делегировать согласование в Ленте Активности')
    def delegate_the_agreement_from_activity(self, number_a_ticket, user_name):
        button_delegate_the_agreement = (By.XPATH, f'//a[contains(text(),"{number_a_ticket}")]/../..//div[@test_id="Action-DelegateAgreement"]')
        self.scroll_to_element(button_delegate_the_agreement)
        # Нажимаем кнопку Делегировать согласование
        self.click_element(button_delegate_the_agreement)
        # Ищем нужного пользователя
        search_user_for_delegate = (By.XPATH, f'//div[@class="delegation__search"]/input')
        self.send_keys_slow(search_user_for_delegate, user_name, 100)
        # Выбираем нужного пользователя
        select_user = (By.XPATH, f'//div[contains(text(),"{user_name}")]/../..//div[@class="ticket-user__aftercontent"]')
        self.click_element(select_user)
        # Подтверждаем Делегирование согласования
        button_apply_delegate_the_agreement = (By.XPATH, f'//button[@test_id="action-DelegateAgreement-submit-btn"]')
        self.click_element(button_apply_delegate_the_agreement)
        return self
    @allure.step('Причина оценки работы тикета')
    def reason_rating_the_ticket_work(self, text_reason):
        # Указываем причину
        self.click_element(Locator.closed_description)
        self.send_keys_slow(Locator.closed_description, text_reason, 100)
        # Нажимаем кнопку подтверждения закрытия тикета
        self.click_element(Locator.closed_submit_btn)
        return self
    @allure.step('Закрыть тикет в Ленте Активности')
    def ticket_to_closed_from_activity(self, type_and_number_a_ticket, rating):
        # Переходим к кнопке действия "Закрыть"
        ticket_to_closed = (By.XPATH, f'//a[contains(text(),"{type_and_number_a_ticket[1]}")]/../..//div[@test_id="Action-Close"]')
        self.scroll_to_element(ticket_to_closed)
        # Нажимаем на кнопку действия "Закрыть"
        self.click_element(ticket_to_closed)
        reason = "Reason for closed " + self.manager.time.get_date_time_Y_m_d_H_M_S()
        # Если оценка от 1 до 4
        select_rating = (By.XPATH, f'//div[@class="rating-wrap__stars"]/div/div[{rating}]')
        if rating <= 4:
            self.click_element(select_rating)
            self.reason_rating_the_ticket_work(reason)
        else:
            self.click_element(select_rating)
            # Нажимаем кнопку подтверждения закрытия тикета
            self.click_element(Locator.closed_submit_btn)
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        self.manager.web_tickets_base.waiting_the_correct_status(self.manager.group_data.Status_ticket['ENG']['Закрыта'], type_and_number_a_ticket)
        # Обозначаем корректный статус тикета
        if type_and_number_a_ticket[0] == 'project' or type_and_number_a_ticket[0] == 'Project':
            correct_status = self.manager.group_data.Status_ticket['project']['RUS']['Закрыт']
        else:
            correct_status = self.manager.group_data.Status_ticket['request_and_task']['RUS']['Закрыта']
        return correct_status

    @allure.step('Апеллировать тикет в Ленте Активности')
    def appeal_a_ticket_from_activity(self, type_and_number_a_ticket):
        # Переходим к кнопке действия "Апеллировать"
        button_appeal_a_ticket = (By.XPATH, f'//a[contains(text(),"{type_and_number_a_ticket[1]}")]/../..//div[@test_id="Action-Appeal"]')
        self.scroll_to_element(button_appeal_a_ticket)
        # Нажимаем на кнопку действия "Апеллировать"
        self.click_element(button_appeal_a_ticket)
        reason = "TestReasonAppealing AutomationWebTests " + self.manager.time.get_date_time_Y_m_d_H_M_S()
        self.send_reason_and_appeal_ticket(reason)
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        self.manager.web_tickets_base.waiting_the_correct_status(
            self.manager.group_data.Status_ticket['ENG']['На согласовании'], type_and_number_a_ticket)
        # Обозначаем корректный статус тикета
        correct_status = 'На согласовании'
        return correct_status

    @allure.step('Заполнить причину и апеллировать тикет')
    def send_reason_and_appeal_ticket(self, text_reason):
        # Указываем причину
        self.click_element(Locator.block_text_for_appeal)
        self.send_keys_slow(Locator.block_text_for_appeal, text_reason, 100)
        # Кнопка подтверждения отмены, отклонения или апеллирования тикета
        self.click_element(Locator.button_apply_appeal)
        return self

    @allure.step('Назначить заявку на себя')
    def assign_request_to_me_from_activity(self, type_and_number_a_ticket, correct_contractor):
        self.page_loaded()
        # Переходим к кнопке действия "Апеллировать"
        assign_to_me = (By.XPATH, f'//a[contains(text(),"{type_and_number_a_ticket[1]}")]/../..//div[@test_id="Action-AssignToMe"]')
        self.scroll_to_element(assign_to_me)
        # Нажимаем на кнопку действия "Назначить на себя"
        self.click_element(assign_to_me)
        # Ожидаем, пока будет корректный исполнитель у заявки в апи и обновляем страницу
        self.manager.web_tickets_base.waiting_the_correct_contractor(correct_contractor, type_and_number_a_ticket)
        return self

    @allure.step('Отправить тикет на доработку')
    def ticket_to_overwork_from_activity(self, type_and_number_a_ticket):
        # Переходим к кнопке действия "На доработку"
        ticket_to_overwork = (By.XPATH, f'//a[contains(text(),"{type_and_number_a_ticket[1]}")]/../..//div[@test_id="Action-ReturnToRework"]')
        self.scroll_to_element(ticket_to_overwork)
        # Нажимаем на кнопку действия "На доработку"
        self.click_element(ticket_to_overwork)
        reason = "TestReasonBack AutomationWebTests " + self.manager.time.get_date_time_Y_m_d_H_M_S()
        self.reason_return_to_rework(reason)
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        self.manager.web_tickets_base.waiting_the_correct_status(
            self.manager.group_data.Status_ticket['ENG']['В работе'], type_and_number_a_ticket)
        # Обозначаем корректный статус тикета
        correct_status = 'В работе'
        return correct_status

    @allure.step('Причина возврата тикета на доработку')
    def reason_return_to_rework(self, text_reason):
        # Указываем причину
        self.click_element(Locator.return_to_rework_description)
        self.send_keys_slow(Locator.return_to_rework_description, text_reason, 100)
        # Кнопка подтверждения отмены тикета
        self.click_element(Locator.return_to_rework_submit_btn)
        return self

    @allure.step('Эскалировать заявку')
    def escalate_request_from_activity(self, type_and_number_a_ticket):
        self.page_loaded()
        # Переходим к кнопке действия "Эскалировать"
        button_escalate = (By.XPATH, f'//a[contains(text(),"{type_and_number_a_ticket[1]}")]/../..//div[@test_id="Action-Escalate"]')
        self.scroll_to_element(button_escalate)
        # Нажимаем на кнопку действия "Эскалировать"
        self.click_element(button_escalate)
        return self