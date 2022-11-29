import os

import allure
from fw.g1_web.g1_any_page import G1AnyPage
from selenium.webdriver.common.by import By
import time

class Locator:
    description_text_in_frame = (By.XPATH, '//body/p')
    description_iframe = (By.XPATH, '//div[@id="cke_Description"]//iframe')
    all_observers = (By.XPATH, '//div[@class="ga_observers_block clearfix"]//div[@class="ga_user_inline"]')
    all_approvers = (By.XPATH, '//div[@class="ga_agreements_block clearfix"]//div[@class="ga_user_inline"]')
    all_attachments = (By.XPATH, '//div[@class="ga_attachment_block"]//li')
    date_start = (By.XPATH, '//input[@name="RequiredStartDate"]')
    button_create_or_save = (By.XPATH, '//div[@class="ga_save_panel"]//button[1]')
    button_copy_ticket = (By.XPATH, '//div[@class="ga_bid_copy ga_bid_copy_js tla"]')
    request_required_start_date = (By.XPATH, '//*[@id="is21"]//div/div/div/input[@name="RequiredStartDate"]')
    input_text_attachment_in_block_attachments = (By.XPATH, '//input[@id="fileupload"]')
    button_add_approvers = (By.XPATH, '//div[@class="ga_agreements_block clearfix"]//div[@class="ga_user_plus"]')
    button_add_observers = (By.XPATH, '//div[@class="ga_observers_block clearfix"]//div[@class="ga_user_plus"]')
    button_add_contractor = (By.XPATH, '//div[@class="ga_participant_block clearfix"]//div[@class="ga_user_plus"]')
    block_select_user = (By.XPATH, '//div[@id="get_user_request_chosen"]')
    input_text_for_add_user = (By.XPATH, '//div[@id="get_user_request_chosen"]//input')
    name_contactor = (By.XPATH, '//div[@class="ga_user_inline ga_contractor last"]//div[@class="ga_user_name"]')
    iframe_description = (By.XPATH, '//div[@class="ga_description"]//iframe ')
    block_initiator_and_contractor = (By.XPATH, '//div[@class="ga_participant_block clearfix"]/div')
    status_ticket = (By.XPATH, '//span[contains(@class, "ga_status")]')
    action_cancel_btn = (By.XPATH, '//button[@class="ga_bttn_status bttn_c"]')
    input_text_reason_for_cancel = (By.XPATH, '//div[@class="ga_info_modal_text"]//textarea')
    input_text_reason_for_reject = (By.XPATH, '//div[@class="ga_info_modal_text"]//iframe')
    button_apply_cancel = (By.XPATH, '//div[@class="ga_cancel_form"]/button')
    action_resolve_btn = (By.XPATH, '//button[@id="to_resolved"]')
    iframe_comment = (By.XPATH, '//div[@class="ga_comment_form"]//iframe')
    button_clarification_to_initiator = (By.XPATH, '//button[@class="ga_bttn bttn_fox ga_clarification_add"]')
    button_clarification_to_contractor = (By.XPATH, '//button[@class="ga_bttn bttn_yellow ga_clarification_add"]')
    g1_accept_the_agreement = (By.XPATH, '//div[@class="ga_change_status"]/button[@class="ga_bttn_status bttn_a"]')
    g1_reject_the_agreement = (By.XPATH, '//div[@class="ga_change_status"]/button[@class="ga_bttn_status bttn_d"]')


class G1TicketsBase(G1AnyPage):

    @allure.step('Нажать кнопку Сохранить/Создать')
    def g1_click_button_create_or_save(self):
        # Ожидаем, когда кнопка Сохранить/Создать будет активна
        self.g1_waiting_when_button_is_active(Locator.button_create_or_save)
        # Нажимаем на кнопку Сохранить/Создать
        self.click_element(Locator.button_create_or_save)
        # Ожидаем, что появится spinner на странице
        self.g1_page_loaded()
        return self

    @allure.step('Заполняем описание')
    def g1_fill_description(self, text):
        self.send_keys_in_frame(Locator.iframe_description, text)
        return self

    @allure.step('Переходим в тикет с нужным описанием')
    def g1_go_to_ticket_in_list_with_need_description(self, description_text):
        ticket_item_description = (By.XPATH, f'//div[@class="descr"]//a[contains(text(),"{description_text}")]')
        self.move_to_element(ticket_item_description)
        self.click_element(ticket_item_description)
        return self

    @allure.step('Возвращаем описание тикета')
    def g1_get_description(self):
        # Отображаем информацию из описания тикета
        frame = self.find_element(Locator.description_iframe)
        self.GetDriver().switch_to.frame(frame)
        description = self.get_tag_text(Locator.description_text_in_frame)
        self.GetDriver().switch_to.default_content()
        return description

    @allure.step('Изменить описание тикета')
    def g1_edit_description(self, description_text):
        self.clear_and_send_keys_in_frame(Locator.iframe_description, description_text)
        self.g1_click_button_create_or_save()
        return self

    @allure.step('Возвращаем обозревателей тикета')
    def g1_get_observers_in_ticket(self):
        self.g1_page_loaded()
        # Создаем список для будущих обозревателей
        list_observers = []
        # Получаем всех обозревателей
        count_observers = self.find_elements(Locator.all_observers)
        # Вычитаем 1 элемент, т.к. кнопка добавления обозревателей тоже учитывается выше
        count_observers = len(count_observers) - 1
        # Вводим цикл, чтобы пройтись по всем обозревателям
        for i in range(1, count_observers + 1):
            observer = (By.XPATH, f'(//div[@class="ga_observers_block clearfix"]//div[@class="ga_user_inline"])[{i}]')
            # Получаем имя обозревателя
            name_observer = self.get_tag_text(observer)
            # Добавляем имя обозревателя в список
            list_observers.append(name_observer)
        return list_observers

    @allure.step('Возвращаем согласующих тикета')
    def g1_get_approvers_in_ticket(self):
        self.g1_page_loaded()
        # Создаем список для будущих согласующих
        list_approvers = []
        # Получаем всех согласующих
        count_approvers = self.find_elements(Locator.all_approvers)
        # Вычитаем 1 элемент, т.к. кнопка добавления согласующих тоже учитывается выше
        count_approvers = len(count_approvers) - 1
        # Вводим цикл, чтобы пройтись по всем согласующим
        for i in range(1, count_approvers + 1):
            approver = (By.XPATH, f'//div[@class="ga_agreements_block clearfix"]//div[@class="ga_user_inline"][{i}]')
            # Получаем имя согласующего
            name_approver = self.get_tag_text(approver)
            # Добавляем имя согласующего в список
            list_approvers.append(name_approver)
        return list_approvers

    @allure.step('Возвращаем дату начала тикета')
    def g1_get_date_start_ticket(self):
        date_start = self.get_tag_attribute(Locator.date_start, 'value')
        return date_start

    @allure.step('Заполняем дату начала')
    def g1_fill_start_date(self, date_start):
        self.clear_and_send_keys(Locator.request_required_start_date, date_start)
        return self

    @allure.step('Добавить файл')
    def g1_add_attachment_in_ticket(self, name_attachment):
        path_to_project = os.path.join(self.get_project_root(), 'data', 'files_for_test', name_attachment)
        self.send_keys(Locator.input_text_attachment_in_block_attachments, path_to_project)
        return self

    @allure.step('Добавить файл через блок вложений')
    def g1_add_attachment_in_block_comments_in_ticket(self, name_attachment):
        self.click_element(By.XPATH, '//a[@id="cke_30"]')
        path_to_project = os.path.join(self.get_project_root(), 'data', 'files_for_test', name_attachment)
        self.send_keys(Locator.input_text_attachment_in_block_attachments, path_to_project)
        return self

    @allure.step('Возвращаем вложения тикета')
    def g1_get_attachments_in_ticket(self):
        self.g1_page_loaded()
        # Создаем список для будущих вложений
        list_attachments = []
        # Получаем всех вложений
        count_attachments = self.find_elements(Locator.all_attachments)
        # Вводим цикл, чтобы пройтись по всем вложениям
        for i in range(1, len(count_attachments) + 1):
            attachment = (By.XPATH, f'(//div[@class="ga_attachment_block"]//li)[{i}]/a')
            # Получаем имя вложения
            name_attachment = self.get_tag_text(attachment)
            # Добавляем имя вложения в список
            list_attachments.append(name_attachment)
        return list_attachments

    @allure.step('Добавить согласующего')
    def g1_add_approver(self, user_name):
        self.g1_page_loaded()
        # Нажимаем кнопку для добавления согласующего
        self.scroll_to_element(Locator.button_add_approvers)
        self.click_element(Locator.button_add_approvers)
        # Выбираем пользователя
        self.g1_select_user(user_name)
        # Ожидаем, пока появится добавленный пользователь
        find_add_approver = (By.XPATH, f'//div[@class="ga_agreements_block clearfix"]//div[contains(text(),"{user_name}")]')
        self.find_element(find_add_approver)
        return self

    @allure.step('Добавить обозревателя')
    def g1_add_observer(self, user_name):
        self.g1_page_loaded()
        # Нажимаем кнопку для добавления обозревателя
        self.scroll_to_element(Locator.button_add_observers)
        self.click_element(Locator.button_add_observers)
        # Выбираем пользователя
        self.g1_select_user(user_name)
        # Ожидаем, пока появится добавленный пользователь
        find_add_observer = (By.XPATH, f'//div[@class="ga_observers_block clearfix"]//div[contains(text(),"{user_name}")]')
        self.find_element(find_add_observer)
        return self

    @allure.step('Добавить исполнителя')
    def g1_add_contractor(self, user_name):
        self.g1_page_loaded()
        # Нажимаем кнопку для добавления исполнителя
        self.scroll_to_element(Locator.button_add_contractor)
        self.click_element(Locator.button_add_contractor)
        # Выбираем пользователя
        self.g1_select_user(user_name)
        # Ожидаем, пока появится добавленный пользователь
        find_add_contractor = (By.XPATH, f'//div[@class="ga_participant_block clearfix"]//div[contains(text(),"{user_name}")]')
        self.find_element(find_add_contractor)
        # Сохраняем заявку
        self.g1_click_button_create_or_save()
        return self

    @allure.step('Возвращаем исполнителя тикета')
    def g1_get_contractor(self):
        self.g1_page_loaded()
        actual_contractor = self.get_tag_text(Locator.name_contactor)
        return actual_contractor

    @allure.step('Выбираем нужного пользователя')
    def g1_select_user(self, user_name):
        time.sleep(0.5)
        # Нажимаем на блок выбора пользователя
        self.click_element(Locator.block_select_user)
        time.sleep(0.3)
        # Вводим имя нужного пользователя
        self.send_keys(Locator.input_text_for_add_user, user_name)
        # Выбираем нужного пользователя
        self.g1_select_need_user(user_name)
        return self

    @allure.step('Проверка, есть ли исполнитель')
    def g1_check_contractor(self):
        self.g1_page_loaded()
        # Получаем количество кружков в блоке инициатора и исполнителя (инициатор, исполнитель, назначение исполнителя, изменение исполнителя)
        elements = self.find_elements(Locator.block_initiator_and_contractor)
        # Если только 1 элемент, значит только в ткете есть только инициатор
        if len(elements) == 1:
            return False
        elif len(elements) == 2:
            # Если 2 кружка, проверяем, есть ли кнопка добавления исполнителя
            check_button_add_contractor = self.check_is_there_element_on_the_page(Locator.button_add_contractor)
            if check_button_add_contractor ==  True:
                return False
        # Если больше 3 элементов, значит есть как минимум инициатор и исполнитель
        else:
            return True

    @allure.step('Возвращаем статус тикета')
    def g1_get_status_ticket(self):
        self.g1_page_loaded()
        actual_status = self.get_tag_text(Locator.status_ticket)
        return actual_status

    @allure.step('Переходим в нужный тикет')
    def g1_go_to_need_ticket(self, type_ticket, number_ticket):
        url_ticket = self.g1_create_url_for_need_tickets(type_ticket, number_ticket)
        self.goto_page(url_ticket)
        return self

    @allure.step('Создаем ссылку на нужный тикет')
    def g1_create_url_for_need_tickets(self, type_ticket, number_ticket):
        if type_ticket == 'Request' or type_ticket == 'request':
            url_ticket = self.manager.g1_settings.GLOBAL[self.manager.g1_settings.branch]['main_page'] + f'Request/Edit/{number_ticket}'
            return url_ticket
        elif type_ticket == 'Task' or type_ticket == 'task':
            url_ticket = self.manager.g1_settings.GLOBAL[self.manager.g1_settings.branch]['main_page'] + f'Task/Edit/{number_ticket}'
            return url_ticket
        elif type_ticket == 'Project' or type_ticket == 'project':
            url_ticket = self.manager.g1_settings.GLOBAL[self.manager.g1_settings.branch]['main_page'] + f'Project/Edit/{number_ticket}'
            return url_ticket

    @allure.step('Отменить тикет')
    def g1_canceling_of_ticket(self):
        self.g1_page_loaded()
        # Кнопка отмены тикета
        self.scroll_to_element(Locator.action_cancel_btn)
        self.click_element(Locator.action_cancel_btn)
        reason = "TestReasonCanceled AutomationWebTests " + self.manager.time.get_date_time_Y_m_d_H_M_S()
        self.g1_send_reason_and_cancel_ticket(reason)
        # Обозначаем корректный статус тикета
        correct_status = self.manager.group_data.g1_Status_ticket['WEB']['Отменено']
        return correct_status

    @allure.step('Заполнить причину и отменить тикет')
    def g1_send_reason_and_cancel_ticket(self, text_reason):
        # Указываем причину
        self.send_keys(Locator.input_text_reason_for_cancel, text_reason)
        # Кнопка подтверждения отмены, отклонения или апеллирования тикета
        self.click_element(Locator.button_apply_cancel)
        return self

    @allure.step('Отправить тикет на проверку')
    def g1_send_ticket_for_resolve(self):
        self.g1_page_loaded()
        # Нажимаем на кнопку На проверку
        self.scroll_to_element(Locator.action_resolve_btn)
        self.click_element(Locator.action_resolve_btn)
        # Ожидаем, пока кнопка будет не активна, что будет означать, что она нажалась
        self.g1_waiting_when_button_is_not_active(Locator.action_resolve_btn)
        # Сохраняем заявку
        self.g1_click_button_create_or_save()
        # Обозначаем корректный статус тикета
        correct_status = self.manager.group_data.g1_Status_ticket['WEB']['Проверка выполнения']
        return correct_status

    @allure.step('Задать уточнение инициатору')
    def g1_ask_initiator_clarification(self, comment_text=None):
        if comment_text == None:
            comment_text = "Test Clarification " + self.manager.time.get_date_time_Y_m_d_H_M_S()
        # Вводим текст в поле комментария
        self.g1_fill_comment(comment_text)
        # Нажимаем кнопку Отправить уточнение инициатору
        self.click_element(Locator.button_clarification_to_initiator)
        self.g1_page_loaded()
        return self

    @allure.step('Задать уточнение исполнителю')
    def g1_ask_contractor_clarification(self, comment_text=None):
        if comment_text == None:
            comment_text = "Test Clarification " + self.manager.time.get_date_time_Y_m_d_H_M_S()
        # Вводим текст в поле комментария
        self.g1_fill_comment(comment_text)
        # Нажимаем кнопку Отправить уточнение инициатору
        self.click_element(Locator.button_clarification_to_contractor)
        self.g1_page_loaded()
        return self

    @allure.step('Заполнение поля комментарий')
    def g1_fill_comment(self, comment_text):
        # Ожидаем пока появится окно для ввода текста
        self.find_element(Locator.iframe_comment)
        # Скроллим к полю ввода текста
        self.scroll_to_element(Locator.iframe_comment)
        # Вводим текст в поле комментария
        self.send_keys_in_frame(Locator.iframe_comment, comment_text)
        return self

    @allure.step('Принять согласование')
    def g1_accept_the_agreement(self):
        self.g1_page_loaded()
        # Нажимаем на кнопку Согласовать
        self.scroll_to_element(Locator.g1_accept_the_agreement)
        self.click_element(Locator.g1_accept_the_agreement)
        # Ожидаем, пока кнопка будет не активна, что будет означать, что она нажалась
        self.g1_waiting_when_button_is_not_active(Locator.g1_accept_the_agreement)
        # Сохраняем заявку
        self.g1_click_button_create_or_save()
        return self

    @allure.step('Отклонить согласование')
    def g1_reject_the_agreement(self):
        self.g1_page_loaded()
        # Нажимаем кнопку Отклонить
        self.scroll_to_element(Locator.g1_reject_the_agreement)
        self.click_element(Locator.g1_reject_the_agreement)
        # Вводим текст причины и подтверждаем отклонение тикета
        reason = "TestReasonRejected AutomationWebTests " + self.manager.time.get_date_time_Y_m_d_H_M_S()
        self.g1_send_reason_and_reject_ticket(reason)
        # Обозначаем корректный статус тикета
        correct_status = self.manager.group_data.g1_Status_ticket['WEB']['Отклонена']
        return correct_status

    @allure.step('Заполнить причину и отклонить тикет')
    def g1_send_reason_and_reject_ticket(self, text_reason):
        # Указываем причину
        self.send_keys_in_frame(Locator.input_text_reason_for_reject, text_reason)
        # Кнопка подтверждения отмены, отклонения или апеллирования тикета
        self.click_element(Locator.button_apply_cancel)
        return self