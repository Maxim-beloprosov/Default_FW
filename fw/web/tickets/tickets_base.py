from selenium.webdriver.common.by import By
import allure
from fw.web.AnyPage import AnyPage
import time


class Locator:
    ticket_description_iframe = (By.XPATH, '//div[@test_id="ticket-description"]//iframe')
    ticket_comment_iframe = (By.XPATH, '//div[@class="comments__editor"]//iframe')
    input_text_description = (By.XPATH, '//div[@test_id="ticket-description"]//p')
    input_text_additional_description = (By.XPATH, '//div[@test_id="append-description-editor"]//p')
    edit_text_description = (By.XPATH, '//div[@test_id="cke-description-edit"]//p')
    input_text_comment = (By.XPATH, '//div[@test_id="comment-create"]//p')
    cke_contents = (By.XPATH, '//*[@id="cke_1_contents"]')
    approvers_add_btn = (By.XPATH, '//button[@test_id="approvers-add-btn"]')
    observers_add_btn = (By.XPATH, '//button[@test_id="observers-group-add-btn"]')
    observers_search_input = (By.XPATH, '//div[@test_id="observers-group-dropdown-content"]//input')
    approvers_search_input = (By.XPATH, '//div[@test_id="approvers-dropdown-content"]//input')
    attachment_search_input = (By.XPATH, '(//div[@class="modal-attach-file"]//input[@test_id="custom-input"])[2]')
    attachment_search_input_in_description = (By.XPATH, '//div[@class="ticket__content"]//div[@class="modal-attach-file__search"]//input')
    attach_file = (By.XPATH, '(//div[@class="modal-attach-file__bottom-panel"]/button)[2]')
    attach_file_in_description = (By.XPATH, '//div[contains(@class, "toolbar")]//div[@class="modal-attach-file__bottom-panel"]/button')
    attachment_add_btn = (By.XPATH, '//button[@test_id="add-attachment"]')
    attachment_add_btn_in_description = (By.XPATH, '//button[@test_id="toolbar-file"]')
    append_description_open_editor = (By.XPATH, '//button[@test_id="append-description-open-editor"]')
    append_description_editor_iframe = (By.XPATH, '//div[@test_id="append-description-editor"]//iframe')
    edit_description_editor_iframe = (By.XPATH, '//div[@test_id="cke-description-edit"]//iframe')
    append_description_submit_btn = (By.XPATH, '//button[@test_id="append-description-submit-btn"]')
    action_cancel_btn = (By.XPATH, '//div[@test_id="Action-Cancel"]')
    return_to_rework_description = (By.XPATH, '//div[@test_id="action-ReturnToRework-description"]/textarea')
    return_to_rework_submit_btn = (By.XPATH, '//button[@test_id="action-ReturnToRework-submit-btn"]')
    block_text_for_cancel = (By.XPATH, '//div[@test_id="action-Cancel-description"]/textarea')
    block_text_for_reject = (By.XPATH, '//div[@test_id="action-Reject-description"]/textarea')
    block_text_for_appeal = (By.XPATH, '//div[@test_id="action-Appeal-description"]/textarea')
    button_apply_cancel = (By.XPATH, '//button[@test_id="actionCancelsubmit-btn"]')
    button_apply_reject = (By.XPATH, '//button[@test_id="actionRejectsubmit-btn"]')
    button_apply_appeal = (By.XPATH, '//button[@test_id="actionAppealsubmit-btn"]')
    closed_description = (By.XPATH, '//div[@test_id="action-MarkAndClose-description"]/textarea')
    closed_submit_btn = (By.XPATH, '//button[@test_id="action-MarkAndClose-submit-btn"]')
    action_resolve_btn = (By.XPATH, '//div[@test_id="Action-Resolve"]')
    contractors_add_btn = (By.XPATH, '//button[@test_id="contractors-add-btn"]')
    contractors_search_input = (By.XPATH, '//div[@test_id="anchor"]//input')
    contractors_activator_in_request = (By.XPATH, '//section[@class="sidebar-ticket ticket-sidebar__wrap border"]/div[4]//div[@class="user-avatar"]')
    contractors_activator_in_task = (By.XPATH, '//section[@class="sidebar-ticket ticket-sidebar__wrap border"]/div[3]//div[@class="user-avatar"]')
    # Пока временные нормативы в проектах закомичены, путь у задач и проектов разный к исполнителю. Как вернут временные нормативы в проекты, пути будут одинаковые
    contractors_activator_in_projects = (By.XPATH, '(//section[@class="sidebar-ticket ticket-sidebar__wrap border"]//div[@class="user-avatar"])[1]')
    button_edit_contractor = (By.XPATH, '//div[@test_id="-dropdown-content"]//div[@class="action"]')
    accept_the_agreement = (By.XPATH, '//div[@test_id="Action-Approve"] ')
    reject_the_agreement = (By.XPATH, '//div[@test_id="Action-Reject"]')
    button_comeback_a_ticket_in_work = (By.XPATH, '//div[@test_id="Action-BackToWork"]')
    button_take_a_ticket_in_work = (By.XPATH, '//div[@test_id="Action-ToWork"]')
    button_appeal_a_ticket = (By.XPATH, '//div[contains(text(),"Апеллировать")]')
    ticket_to_overwork = (By.XPATH, '//div[@test_id="Action-ReturnToRework"] ')
    ticket_to_closed = (By.XPATH, '//div[@test_id="Action-Close"]')
    button_save_additional_description = (By.XPATH, '//button[@test_id="cke-description-edit-submit"]')
    subject_textarea = (By.XPATH, '//div[@test_id="subject"]/textarea')
    description_text = (By.XPATH, '//div[@test_id="ticket-description"]')
    contractor_ticket = (By.XPATH, '//div[@class="member"][1]//div[@test_id="contractors-dropdown-activator"]//div[@class="member__name"]')
    status_ticket = (By.XPATH, '//div[@class="ticket__info"]/div/div')
    click_date_start_when_create = (By.XPATH, '(//div[@class="datepicker-date-activator"])[1]')
    click_date_end_when_create = (By.XPATH, '(//div[@class="datepicker-date-activator"])[2]')
    click_date_start_after_create = (By.XPATH, '//div[@test_id="ticket-begin-date"]')
    click_date_end_after_create = (By.XPATH, '//div[@class="dropdown-block__content"]/div/div[3]//div[@class="calendar"]')
    input_date = (By.XPATH, '//div[@class="input-element"]//input[@test_id="custom-input"]')
    input_hours = (By.XPATH, '(//div[@class="time-wrap time-wrap_gray time-wrap_middle time-universal-control"]//input)[1]')
    input_minutes = (By.XPATH, '(//div[@class="time-wrap time-wrap_gray time-wrap_middle time-universal-control"]//input)[2]')
    apply_date = (By.XPATH, '//div[@class="date-time-picker__buttons"]//button[@class="button   button_violet button_medium "]')
    date_start = (By.XPATH, '(//div[contains(@class, "time")]//div[@class="time__text"]/..//div[contains(@class, "datepicker-date-activator__text")])[1]')
    date_end = (By.XPATH, '(//div[contains(@class, "time")]//div[@class="time__text"]/..//div[contains(@class, "datepicker-date-activator__text")])[2]')
    date_create = (By.XPATH, '//div[@class="ticket__times"]/div')
    open_normative_time = (By.XPATH, '//div[@class="dropdown-block time"]//div[contains(@class, "dropdown-block__control")]')
    send_comment = (By.XPATH, '//div[@class="comments"]//div[@class="toolbar__submit"]/button')
    button_clarification = (By.XPATH, '//div[@class="toolbar__submit"]//div[@class="button__after-content"]/div[1]')
    ask_initiator = (By.XPATH, '//span[contains(text()," Уточнить у инициатора ")]')
    ask_contractor = (By.XPATH, '//span[contains(text()," Уточнить у исполнителя ")]')
    block_comment = (By.XPATH, '//input[@test_id="comment-input"]')
    button_cancel_the_clarification = (By.XPATH, '//div[@test_id="cancelToClarification"]')
    modal_attach_file_loaded = (By.XPATH, '(//div[@class="popup"]//div[contains(@class, "modal-attach-file__loaded")])[2]')
    all_observers = (By.XPATH, '//div[@test_id="observers-group-dropdown-activator"]/../../../..//div[@class="member-wrap member__item"]')
    all_approvers = (By.XPATH, '//div[@class="member"]//div[@class="agreement"]')
    all_attachments = (By.XPATH, '//div[@class="drop-zone__content"]//div[@class="file"]//div[@class="file-info__title"]')
    all_descriptions = (By.XPATH, '//div[@class="cke-supreme description"]//div[@class="cke-supreme__content"]')
    button_approver_avatar = (By.XPATH, '//div[@class="agreement"]//div[@test_id="-dropdown-activator"]')
    button_approver_delete = (By.XPATH, '//div[@class="action__text action__text_black"]')
    block_time = (By.XPATH, '//div[@class="dropdown-block__control dropdown-block__control_violet"]//*')
    name_responsibility_groups = (By.XPATH, '//div[@class="rg"]//span')
    fixed_panel_submit = (By.XPATH, '//button[@test_id="fixed-panel-submit"]')

class TicketsBase(AnyPage):

    @allure.step('Заполнение поля описания')
    def fill_description_in_ticket(self, description_text):
        self.clear_and_send_keys(Locator.input_text_description, description_text)
        return self

    @allure.step('Добавление согласующего')
    def add_approver(self, user_name):
        # Кнопка добавления согласующего в тикетах
        self.scroll_to_element(Locator.approvers_add_btn)
        self.click_element(Locator.approvers_add_btn)
        # Поиск согласующего для добавления
        self.send_keys_slow(Locator.approvers_search_input, user_name, 100)
        # Выбор пользователя из списка
        locator_approver = (By.XPATH, f"//div[contains(@class, 'result')]//div[contains(@class, 'item__name')][contains(text(), '{user_name}')]")
        self.move_to_element(locator_approver)  # т.к. есть похожие пользователи, переходим к нужному, чтобы точно можно было на него нажать
        self.click_element(locator_approver)
        return self

    @allure.step('Проверка согласующего')
    def check_approver(self, user_name):
        check_user_in_approver = (By.XPATH, f'//div[@class="agreement"]//div[contains(text(), "{user_name}")]')
        self.find_element(check_user_in_approver)
        return self

    @allure.step('Добавление обозревателя')
    def add_observer(self, user_name):
        # Кнопка добавления обозревателя в тикетах
        self.scroll_to_element(Locator.observers_add_btn)
        self.click_element(Locator.observers_add_btn)
        # Поиск обозревателя для добавления
        self.send_keys_slow(Locator.observers_search_input, user_name, 100)
        # Выбор пользователя из списка
        locator_observer = (By.XPATH, f"//div[contains(@class, 'result')]//div[@class='wrapper__item']//div[contains(text(), '{user_name}')]")
        self.move_to_element(locator_observer)  # т.к. есть похожие пользователи, переходим к нужному, чтобы точно можно было на него нажать
        self.click_element(locator_observer)
        return self

    @allure.step('Проверка обозревателя')
    def check_observer(self, user_name):
        check_user_in_observer = (By.XPATH, f'//div[@class="member-wrapper"]//div[contains(text(), "{user_name}")]')
        self.find_element(check_user_in_observer)
        return self

    @allure.step('Добавить дополнительное описание')
    def add_additional_description(self, information_text):
        # Ожидаем, пока появится последний элемент на странице
        self.manager.web_request_id.page_loaded()
        time.sleep(1)
        # Кнопка добавления дополнительного описания
        self.click_element(Locator.append_description_open_editor)
        # Вводим текст в поле "описание"
        self.clear_and_send_keys(Locator.input_text_additional_description, information_text)
        # Кнопка добавления дополнилнительного описания
        self.click_element(Locator.append_description_submit_btn)
        check_additional_description = (By.XPATH, f'//div[@test_id="ticket-description"]//p[contains(text(),"{information_text}")]')
        self.find_element(check_additional_description)
        return self

    @allure.step('Редактирование дополнительного описания')
    def edit_additional_description(self, number_additional_description, information_text):
        # Кнопка изменения дополнительного описания
        button_edit_additional_description = (By.XPATH, f'//button[@test_id="edit-description-{number_additional_description}"]')
        self.scroll_to_element(button_edit_additional_description)
        self.click_element(button_edit_additional_description)
        # Вводим текст в поле "описание"
        self.clear_and_send_keys(Locator.edit_text_description, information_text)
        # Кнопка сохранения дополнительного описания
        self.click_element(Locator.button_save_additional_description)
        check_additional_description = (By.XPATH, f'//div[@test_id="ticket-description"]//p[contains(text(),"{information_text}")]')
        self.find_element(check_additional_description)
        return self

    @allure.step('Отменить тикет')
    def canceling_of_ticket(self):
        # Кнопка отмены тикета
        self.scroll_to_element(Locator.action_cancel_btn)
        self.click_element(Locator.action_cancel_btn)
        reason = "TestReasonCanceled AutomationWebTests " + self.manager.time.get_date_time_Y_m_d_H_M_S()
        self.send_reason_and_cancel_ticket(reason)
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        type_and_number_a_ticket = self.waiting_the_correct_status(self.manager.group_data.Status_ticket['ENG']['Отменено'])
        # Обозначаем корректный статус тикета
        if type_and_number_a_ticket[0] == 'projects':
            correct_status = self.manager.group_data.Status_ticket['project']['RUS']['Отменён']
        else:
            correct_status = self.manager.group_data.Status_ticket['request_and_task']['RUS']['Отменена']
        return correct_status

    @allure.step('Заполнить причину и отменить тикет')
    def send_reason_and_cancel_ticket(self, text_reason):
        # Указываем причину
        self.click_element(Locator.block_text_for_cancel)
        self.send_keys_slow(Locator.block_text_for_cancel, text_reason, 100)
        # Кнопка подтверждения отмены тикета
        self.click_element(Locator.button_apply_cancel)
        return self

    @allure.step('Заполнить причину и отклонить тикет')
    def send_reason_and_reject_ticket(self, text_reason):
        # Указываем причину
        self.click_element(Locator.block_text_for_reject)
        self.send_keys_slow(Locator.block_text_for_reject, text_reason, 100)
        # Кнопка подтверждения отмены, отклонения или апеллирования тикета
        self.click_element(Locator.button_apply_reject)
        return self

    @allure.step('Заполнить причину и апеллировать тикет')
    def send_reason_and_appeal_ticket(self, text_reason):
        # Указываем причину
        self.click_element(Locator.block_text_for_appeal)
        self.send_keys_slow(Locator.block_text_for_appeal, text_reason, 100)
        # Кнопка подтверждения отмены, отклонения или апеллирования тикета
        self.click_element(Locator.button_apply_appeal)
        return self

    @allure.step('Нажать кнопку перевести в проверку')
    def click_btn_ticket_for_resolve(self):
        self.scroll_to_element(Locator.action_resolve_btn)
        self.click_element(Locator.action_resolve_btn)
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        self.waiting_the_correct_status(
            self.manager.group_data.Status_ticket['ENG']['В проверке'])
        # Обозначаем корректный статус тикета
        correct_status = self.manager.group_data.Status_ticket['request_and_task']['RUS']['В проверке']
        return correct_status

    @allure.step('Принять согласование')
    def accept_the_agreement(self):
        self.scroll_to_element(Locator.accept_the_agreement)
        self.click_element(Locator.accept_the_agreement)
        #hours = self.manager.time.get_time_now()  Пока закомментировал, тк падает тест иногда, либо не успевает придти комментарий, либо время не совпадает
        #date = 'сегодня, ' + hours[11:15]
        #self.find_comment_with_date_on_the_page('Положительное решение по согласованию.', date)
        return self

    @allure.step('Отклонить согласование')
    def reject_the_agreement(self):
        self.scroll_to_element(Locator.reject_the_agreement)
        # Нажимаем кнопку Отклонить
        self.click_element(Locator.reject_the_agreement)
        # Вводим текст причины и подтверждаем отклонение тикета
        reason = "TestReasonRejected AutomationWebTests " + self.manager.time.get_date_time_Y_m_d_H_M_S()
        self.send_reason_and_reject_ticket(reason)
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        type_and_number_a_ticket = self.waiting_the_correct_status(
            self.manager.group_data.Status_ticket['ENG']['Отклонено'])
        # Обозначаем корректный статус тикета
        if type_and_number_a_ticket[0] == 'projects':
            correct_status = self.manager.group_data.Status_ticket['project']['RUS']['Отклонён']
        else:
            correct_status = self.manager.group_data.Status_ticket['request_and_task']['RUS']['Отклонена']
        return correct_status

    @allure.step('Вернуть тикет в работу')
    def comeback_a_ticket_in_work(self):
        self.scroll_to_element(Locator.button_comeback_a_ticket_in_work)
        self.click_element(Locator.button_comeback_a_ticket_in_work)
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        self.waiting_the_correct_status(
            self.manager.group_data.Status_ticket['ENG']['В работе'])
        # Обозначаем корректный статус тикета
        correct_status = self.manager.group_data.Status_ticket['request_and_task']['RUS']['В работе']
        return correct_status

    @allure.step('Взять тикет в работу')
    def take_a_ticket_in_work(self):
        self.scroll_to_element(Locator.button_take_a_ticket_in_work)
        self.click_element(Locator.button_take_a_ticket_in_work)
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        self.waiting_the_correct_status(
            self.manager.group_data.Status_ticket['ENG']['В работе'])
        # Обозначаем корректный статус тикета
        correct_status = self.manager.group_data.Status_ticket['request_and_task']['RUS']['В работе']
        return correct_status

    @allure.step('Апеллировать тикет')
    def appeal_a_ticket(self):
        self.scroll_to_element(Locator.button_appeal_a_ticket)
        self.click_element(Locator.button_appeal_a_ticket)
        reason = "TestReasonAppealing AutomationWebTests " + self.manager.time.get_date_time_Y_m_d_H_M_S()
        self.send_reason_and_appeal_ticket(reason)
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        self.waiting_the_correct_status(
            self.manager.group_data.Status_ticket['ENG']['На согласовании'])
        # Обозначаем корректный статус тикета
        correct_status = self.manager.group_data.Status_ticket['request_and_task']['RUS']['На согласовании']
        return correct_status

    @allure.step('Отправить тикет на доработку')
    def ticket_to_overwork(self):
        self.scroll_to_element(Locator.ticket_to_overwork)
        self.click_element(Locator.ticket_to_overwork)
        reason = "TestReasonBack AutomationWebTests " + self.manager.time.get_date_time_Y_m_d_H_M_S()
        self.reason_return_to_rework(reason)
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        self.waiting_the_correct_status(
            self.manager.group_data.Status_ticket['ENG']['В работе'])
        # Обозначаем корректный статус тикета
        correct_status = self.manager.group_data.Status_ticket['request_and_task']['RUS']['В работе']
        return correct_status

    @allure.step('Причина возврата тикета на доработку')
    def reason_return_to_rework(self, text_reason):
        # Указываем причину
        self.click_element(Locator.return_to_rework_description)
        self.send_keys_slow(Locator.return_to_rework_description, text_reason, 100)
        # Кнопка подтверждения отмены тикета
        self.click_element(Locator.return_to_rework_submit_btn)
        return self

    @allure.step('Причина оценки работы тикета')
    def reason_rating_the_ticket_work(self, text_reason):
        # Указываем причину
        self.click_element(Locator.closed_description)
        self.send_keys_slow(Locator.closed_description, text_reason, 100)
        # Нажимаем кнопку подтверждения закрытия тикета
        self.click_element(Locator.closed_submit_btn)
        return self

    @allure.step('Закрыть тикет')
    def ticket_to_closed(self, rating):
        # Переходим к кнопке действия "Закрыть"
        self.scroll_to_element(Locator.ticket_to_closed)
        # Нажимаем на кнопку действия "Закрыть"
        self.click_element(Locator.ticket_to_closed)
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
        type_and_number_a_ticket = self.waiting_the_correct_status(
            self.manager.group_data.Status_ticket['ENG']['Закрыта'])
        # Обозначаем корректный статус тикета
        if type_and_number_a_ticket[0] == 'projects':
            correct_status = self.manager.group_data.Status_ticket['project']['RUS']['Закрыт']
        else:
            correct_status = self.manager.group_data.Status_ticket['request_and_task']['RUS']['Закрыта']
        return correct_status

    @allure.step('Возвращаем описание тикета')
    def get_description_in_ticket(self):
        # Отображаем информацию из описания тикета
        description = self.get_tag_text(Locator.description_text)
        return description

    @allure.step('Добавление исполнителя')
    def add_contractor(self, correct_contractor):
        # Кнопка добавления исполнителя в тикете
        self.scroll_to_element(Locator.contractors_add_btn)
        self.click_element(Locator.contractors_add_btn)
        # Поиск пользователя для добавления
        self.send_keys_slow(Locator.contractors_search_input, correct_contractor, 100)
        # Выбор пользователя из списка
        locator = (By.XPATH, f'//div[contains(@class, "result")][contains(@class, "result_shown")]//div[contains(text(), "{correct_contractor}")]')
        self.find_element(locator)
        time.sleep(0.5)
        self.click_element(locator)
        return correct_contractor

    @allure.step('Изменение исполнителя')
    def changing_contractor(self, correct_contractor):
        information_ticket = self.get_type_and_number_ticket()
        if information_ticket[0] == 'request':
            # Нажимаем на аватар исполнителя
            self.click_element(Locator.contractors_activator_in_request)
        elif information_ticket[0] == 'task':
            # Нажимаем на аватар исполнителя
            self.click_element(Locator.contractors_activator_in_task)
        elif information_ticket[0] == 'projects':
            # Нажимаем на аватар исполнителя
            self.click_element(Locator.contractors_activator_in_projects)
        # Нажимаем на кнопку Изменить
        self.click_element(Locator.button_edit_contractor)
        # Поиск пользователя для добавления
        self.send_keys_slow(Locator.contractors_search_input, correct_contractor, 100)
        # Выбор пользователя из списка
        locator_contractor = (By.XPATH, f"//div[contains(@class, 'item__name')][contains(text(), '{correct_contractor}')]")
        self.find_element(locator_contractor)
        self.click_element(locator_contractor)
        self.waiting_the_correct_contractor(correct_contractor)
        return correct_contractor

    @allure.step('Заполнение поля название')
    def fill_name(self, name_text):
        self.clear_and_send_keys(Locator.subject_textarea, name_text)
        return self

    @allure.step('Возвращаем статус тикета')
    def get_status_ticket(self):
        actual_status = self.get_tag_text(Locator.status_ticket)
        return actual_status

    @allure.step('Возвращаем исполнителя тикета')
    def get_contractor_ticket(self):
        # Отображаем исполнителя тикета
        contractor_ticket = self.get_tag_text(Locator.contractor_ticket)
        return contractor_ticket

    @allure.step('Добавление вложения в тикете')
    def add_attachment_in_ticket(self, attachment_name):
        # Кнопка добавления вложения в тикетах
        self.scroll_to_element(Locator.attachment_add_btn)
        self.click_element(Locator.attachment_add_btn)
        # Поиск файла для добавления
        self.find_element(Locator.modal_attach_file_loaded)
        self.send_keys_slow(Locator.attachment_search_input, attachment_name, 100)
        # Выбор файла из списка
        locator_attachment = (By.XPATH, f'//div[@class="modal-attach-file__file"]//div[contains(text(), "{attachment_name}")]')
        self.click_element(locator_attachment)
        # Нажимаем кнопку Прикрепить
        self.click_element(Locator.attach_file)
        return self

    @allure.step('Возвращаем вложения тикета')
    def get_attachments_in_ticket(self):
        list_attachments = []
        count_attachments = self.find_elements(Locator.all_attachments)
        for i in range(1, len(count_attachments) + 1):
            attachment = (By.XPATH, f'(//div[@class="drop-zone__content"]//div[@class="file"]//div[@class="file-info__title"])[{i}]')
            name_attachment = self.get_tag_text(attachment)
            list_attachments.append(name_attachment)
        return list_attachments

    @allure.step('Добавление вложения в описании заявки')
    def add_attachment_in_description(self, attachment_name):
        # Кнопка добавления вложения в описании тикета
        self.scroll_to_element(Locator.attachment_add_btn_in_description)
        self.click_element(Locator.attachment_add_btn_in_description)
        # Поиск файла для добавления
        self.send_keys_slow(Locator.attachment_search_input_in_description, attachment_name, 100)
        # Выбор файла из списка
        locator_attachment = (
        By.XPATH, f'//div[@class="modal-attach-file__file"]//div[contains(text(), "{attachment_name}")]')
        self.click_element(locator_attachment)
        # Нажимаем кнопку Прикрепить
        self.click_element(Locator.attach_file_in_description)
        return self

    @allure.step('Изменить дату начала в задаче или проекте при создании')
    def edit_start_date_in_task_or_project_when_create(self, correct_date, correct_hours):
        # Нажимаем на дату начала
        self.scroll_to_element(Locator.click_date_start_when_create)
        self.click_element(Locator.click_date_start_when_create)
        # Заполняем дату
        self.clear_and_send_keys(Locator.input_date, correct_date)
        # Заполняем часы
        self.clear_and_send_keys(Locator.input_hours, correct_hours)
        # Заполняем минуты
        minutes = '00'
        self.clear_and_send_keys(Locator.input_minutes, minutes)
        correct_date_start = correct_date + ', ' + correct_hours + ':' + minutes  # приводим к формату 08.09.2017 11:00
        # Нажимаем кнопку Применить
        self.click_element(Locator.apply_date)
        return correct_date_start

    @allure.step('Изменить дату окончания в задаче или проекте при создании')
    def edit_end_date_in_task_or_project_when_create(self, correct_date, correct_hours):
        # Нажимаем на дату окончания
        self.scroll_to_element(Locator.click_date_end_when_create)
        self.click_element(Locator.click_date_end_when_create)
        # Заполняем дату
        self.clear_and_send_keys(Locator.input_date, correct_date)
        # Заполняем время
        self.clear_and_send_keys(Locator.input_hours, correct_hours)
        # Заполняем минуты
        minutes = '00'
        self.clear_and_send_keys(Locator.input_minutes, minutes)
        correct_date_end = correct_date + ', ' + correct_hours + ':' + minutes  # приводим к формату 08.09.2017 11:00
        # Нажимаем кнопку Применить
        self.click_element(Locator.apply_date)
        return correct_date_end

    @allure.step('Изменить дату начала в задаче или проекте после создания')
    def edit_start_date_in_task_or_project_after_create(self, correct_date, correct_hours):
        # Расскрываем блок времени
        self.click_element(Locator.block_time)
        time.sleep(1)
        # Нажимаем на дату начала
        self.click_element(Locator.click_date_start_after_create)
        time.sleep(1)
        # Заполняем дату
        self.clear_and_send_keys(Locator.input_date, correct_date)
        time.sleep(1)
        # Заполняем время
        self.clear_and_send_keys(Locator.input_hours, correct_hours)
        time.sleep(1)
        correct_date_start = correct_date + ', ' + correct_hours + ':00'  # приводим к формату 08.09.2017 11:00
        # Нажимаем кнопку Применить
        self.click_element(Locator.apply_date)
        return correct_date_start

    @allure.step('Изменить дату окончания в задаче или проекте после создания')
    def edit_end_date_in_task_or_project_after_create(self, correct_date, correct_hours):
        # Нажимаем на дату окончания
        self.click_element(Locator.click_date_end_after_create)
        # Заполняем дату
        self.clear_and_send_keys(Locator.input_date, correct_date)
        # Заполняем время
        self.clear_and_send_keys(Locator.input_hours, correct_hours)
        correct_date_end = correct_date + ', ' + correct_hours + ':00'  # приводим к формату 08.09.2017 11:00
        # Нажимаем кнопку Применить
        self.click_element(Locator.apply_date)
        return correct_date_end

    @allure.step('Перевод даты "20 апр., 11:00" в формат "20.04.2022, 11:00')
    def conversion_date_to_correct_format(self, date):
        elements_date = date.split(" ")
        actual_month = elements_date[1]
        months = ['янв.,', 'февр.,', 'мар.,', 'апр.,', 'мая,', 'июня,', 'июля,', 'авг.,', 'сент.,', 'окт.,', 'нояб.,', 'дек.,']
        for i in range(0, len(months)):
            if months[i] == actual_month:
                actual_date = elements_date[0] + '.' + ('0' + str(i+1)) + '.2022, ' + elements_date[-1]  # 08.09.2017, 11:00
                return actual_date

    @allure.step('Возвращаем дату начала тикета')
    def get_date_start_ticket(self):
        # Раскрываем временные нормативы
        self.open_normative_time()
        # Отображаем дату начала тикета
        actual_date_start = self.get_tag_text(Locator.date_start)
        return actual_date_start

    @allure.step('Возвращаем дату создания тикета из самого тикета')
    def get_date_create_ticket_in_ticket(self):
        # Отображаем дату создания тикета
        date_create = self.get_tag_text(Locator.date_create)
        # Разделяем дату создания на список
        elements_date_create = date_create.split(" ")
        # Возвращаю дату создания тикета в формате 15 июня, 13:06
        return elements_date_create[1:]

    @allure.step('Возвращаем дату окончания тикета')
    def get_date_end_ticket(self):
        # Раскрываем временные нормативы
        self.open_normative_time()
        # Отображаем дату окончания тикета
        actual_date_end = self.get_tag_text(Locator.date_end)
        return actual_date_end

    @allure.step('Раскрываем временные нормативы')
    def open_normative_time(self):
        self.click_element(Locator.open_normative_time)
        time.sleep(0.5)
        return self

    @allure.step('Нажимаем на блок комментариев, чтобы отобразилось поле для ввода текста')
    def click_comments_block(self):
        # Ждем пока прогрузится последний элемент на странице
        self.manager.web_request_id.page_loaded()
        time.sleep(5)
        # Скроллим к полю блока комментариев
        self.scroll_to_element(Locator.block_comment)
        # Нажимаем на блок комментариев
        self.click_element(Locator.block_comment)
        return self

    @allure.step('Заполнение поля комментарий')
    def fill_comment(self, comment_text):
        # Скроллим к полю ввода текста
        self.scroll_to_element(Locator.input_text_comment)
        # Вводим текст в поле комментария
        self.clear_and_send_keys(Locator.input_text_comment, comment_text)
        return self

    @allure.step('Кнопка отправки комментария')
    def button_send_comment(self):
        self.click_element(Locator.send_comment)
        return self

    @allure.step('Отправить комментарий')
    def send_comment(self, comment_text):
        # Нажимаем на блок комментариев, чтобы появилось поле для ввода текста
        self.click_comments_block()
        # Заполняем текст для комментария
        self.fill_comment(comment_text)
        # Отправляем комментарий
        self.button_send_comment()
        # Ждем, пока комментарий с нужным текстом появится
        locator_text_comment = (By.XPATH, f'//*[text()="{comment_text}"]')
        self.find_element(locator_text_comment)
        return self

    @allure.step('Нажимаем на кнопку Уточнения')
    def click_button_clarification(self):
        self.click_element(Locator.button_clarification)
        return self

    @allure.step('Нажать кнопку Уточнить у инициатора')
    def button_ask_initiator_clarification(self):
        # Нажимаем на кнопку уточнения
        self.click_button_clarification()
        # Нажимаем Уточнить у инициатора
        self.click_element(Locator.ask_initiator)
        return self

    @allure.step('Нажать кнопку Уточнить у исполнителя')
    def button_ask_contractor_clarification(self):
        # Нажимаем на кнопку уточнения
        self.click_button_clarification()
        # Нажимаем Уточнить у исполнителя
        self.click_element(Locator.ask_contractor)
        return self

    @allure.step('Задать уточнение инициатору')
    def ask_initiator_clarification(self, comment_text=None):
        if comment_text == None:
            comment_text = "TestClarificationForInitiator " + self.manager.time.get_date_time_Y_m_d_H_M_S()
        # Кликаем на блок комментариев, чтобы появилось поле для ввода текста
        self.click_comments_block()
        # Вводим текст в поле комментария
        self.fill_comment(comment_text)
        # Нажимаем кнопку Уточнить у инициатора
        self.button_ask_initiator_clarification()
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        self.waiting_the_correct_status(
            self.manager.group_data.Status_ticket['ENG']['На уточнении у иниц.'])
        # Ждем, пока комментарий с нужным текстом появится
        locator_text_comment = (By.XPATH, f'//*[text()="{comment_text}"]')
        self.find_element(locator_text_comment)
        return comment_text

    @allure.step('Задать уточнение исполнителю')
    def ask_contractor_clarification(self, comment_text):
        # Кликаем на блок комментариев, чтобы появилось поле для ввода текста
        self.click_comments_block()
        # Вводим текст в поле комментария
        self.fill_comment(comment_text)
        # Нажимаем кнопку Уточнить у исполнителя
        self.button_ask_contractor_clarification()
        # Ожидаем, пока будет корректный статус у заявки в апи и обновляем страницу
        self.waiting_the_correct_status(
            self.manager.group_data.Status_ticket['ENG']['На уточнении у исп.'])
        # Ждем, пока комментарий с нужным текстом появится
        locator_text_comment = (By.XPATH, f'//*[text()="{comment_text}"]')
        self.find_element(locator_text_comment)
        return comment_text

    @allure.step('Ответить на комментарий')
    def answering_to_comment(self, clarification_text, answer_text=None):
        # Нажимаем кнопку Ответить на комментарий с нужный текстом
        button_answer_to_comment = (By.XPATH, f'//*[text()="{clarification_text}"]/../../../../..//button[@data-manual="comment-response"]')
        self.click_element(button_answer_to_comment)
        # Вводим текст в поле комментария
        if answer_text == None:
            answer_text = "TestAnswer AutomationWebTests " + self.manager.time.get_date_time_Y_m_d_H_M_S()
        self.fill_comment(answer_text)
        # Нажимаем кнопку Отправить
        self.button_send_comment()
        # Ждем, пока комментарий с нужным текстом появится
        locator_text_comment = (By.XPATH, f'//*[text()="{answer_text}"]')
        self.find_element(locator_text_comment)
        return self

    @allure.step('Нажимаем кнопку Действия с комментарием')
    def actions_with_comment(self, clarification_text):
        button_actions_with_comment = (By.XPATH, f'//*[text()="{clarification_text}"]/../../../../..//div[@test_id="comment-more"]/button')
        self.scroll_to_element(button_actions_with_comment)
        self.move_to_element(button_actions_with_comment)
        return self

    @allure.step('Отменить уточнение')
    def cancel_the_clarification(self, clarification_text):
        # Нажимаем кнопку Действия с комментарием
        self.actions_with_comment(clarification_text)
        # Нажимаем Отменить уточнение
        self.click_element(Locator.button_cancel_the_clarification)
        return self

    @allure.step('Ищем комментарий c датой на странице')
    def find_comment_with_date_on_the_page(self, text_comment, date):
        comment_with_date = (By.XPATH, f'//*[text()="{text_comment}"]/../../../../div/*[contains(text(),"{date}")]')
        self.find_element(comment_with_date)
        return self

    @allure.step('Возвращаем последний комментарий на странице тикета')
    def get_last_comment_on_the_page(self):
        last_comment = (By.XPATH, f'(//div[@class="comments__list"]//div[@class="cke-supreme__content"])[1]')
        text_last_comment = self.get_tag_text(last_comment)
        return text_last_comment

    @allure.step('Получаем номер и тип тикета')
    def get_type_and_number_ticket(self):
        count_of_time = 0
        while True:
            url = self.get_current_url()
            if 'tickets' in url or 'projects' in url:
                # Разделяю ссылку в список через /
                number_ticket = url.split('/')
                # Задаю значение тип тикета  (request, task, project)
                type_ticket = number_ticket[-2]
                # Разделяю последнее значение из списка через ?
                number_ticket = number_ticket[-1].split('?')
                # Задаю значение номер тикета (3000000)
                number_ticket = number_ticket[0]
                return type_ticket, number_ticket
            else:
                count_of_time += 1
                time.sleep(0.8)
                if count_of_time == self.manager.settings.time_element_Wait:
                    raise

    @allure.step('Ожидаем, пока будет корректный статус у тикета в апи и отправляем тип и номер тикета')
    def waiting_the_correct_status(self, correct_status, type_and_number_a_ticket=None):
        if type_and_number_a_ticket == None:
            # Получаем тип и номер тикета
            type_and_number_a_ticket = self.get_type_and_number_ticket()  # Приходит в формате ('type_ticket', 'number_ticket')
            # Получаем информацию о тикете с сервера (через API)
            information_ticket = self.get_information_a_ticket_from_api(type_and_number_a_ticket)
        else:
            # Получаем информацию о тикете с сервера (через API)
            information_ticket = self.get_information_a_ticket_from_api(type_and_number_a_ticket)
        # Вводим счетчик времени, чтобы цикл не был бесконечным
        count_of_time = 0
        # Ожидаем, пока статус в тикете будет соответствовать ожидаемому
        while True:
            if information_ticket['status'] == correct_status:
                # Если статус тикета равен ожидаемому, то перезагружаем страницу и заканчиваем цикл
                self.refresh_the_page()
                break
            else:
                # Если статус тикета НЕ РАВЕН ожидаемому, то ожидаем 1 секунду и снова запрашиваем информацию о тикете с сервера
                time.sleep(3)
                count_of_time += 3
                information_ticket = self.get_information_a_ticket_from_api(type_and_number_a_ticket)
                if count_of_time == self.manager.settings.time_element_Wait:
                    raise
        return type_and_number_a_ticket

    @allure.step('Ждем актуального статуса от сервера и получаем статус тикета с WEB')
    def waiting_and_check_status_ticket(self, status):
        self.waiting_the_correct_status(status)
        status_ticket = self.get_status_ticket()
        return status_ticket

    @allure.step('Получаем информацию о тикете с сервера по номеру (через API)')
    def get_information_a_ticket_from_api(self, type_and_number_a_ticket):
        # Авторизуемся пользователем, у которого есть права модератора
        self.manager.api_token.get_token('test_api_user')
        if type_and_number_a_ticket[0] == 'request' or type_and_number_a_ticket[0] == 'Request':
            information_ticket = self.manager.api_requests.get_requests_document_number(type_and_number_a_ticket[1], 'isModeratorMode=true')
            return information_ticket
        elif type_and_number_a_ticket[0] == 'task' or type_and_number_a_ticket[0] == 'Task':
            information_ticket = self.manager.api_tasks.get_tasks_document_number(type_and_number_a_ticket[1],
                                                                                  'isModeratorMode=true')
            return information_ticket
        elif type_and_number_a_ticket[0] == 'projects' or type_and_number_a_ticket[0] == 'Projects' or type_and_number_a_ticket[0] == 'Project' or type_and_number_a_ticket[0] == 'project':
            information_ticket = self.manager.api_projects.get_projects_document_number(type_and_number_a_ticket[1], 'isModeratorMode=true')
            return information_ticket


    @allure.step('Ожидаем, пока будет корректный исполнитель у тикета в апи')
    def waiting_the_correct_contractor(self, correct_contractor, type_and_number_a_ticket=None):
        if type_and_number_a_ticket == None:
            # Получаем номер тикета
            type_and_number_a_ticket = self.get_type_and_number_ticket()  # Приходит в формате ('type_ticket', 'number_ticket')

        # Получаем информацию о тикете с сервера (через API)
        information_ticket = self.get_information_a_ticket_from_api(type_and_number_a_ticket)

        # Ждем момента, когда появится информация о исполнителе в информации о тикете с сервера
        count_of_time = 0
        while True and count_of_time < self.manager.settings.time_element_Wait:
            if "contractor" in information_ticket or "contractors" in information_ticket:
                break
            else:
                information_ticket = self.get_information_a_ticket_from_api(type_and_number_a_ticket)
                time.sleep(3)
                count_of_time += 3
                if count_of_time == self.manager.settings.time_element_Wait:
                    raise

        # Складываем фамилию и имя
        if type_and_number_a_ticket[0] == 'Task' or type_and_number_a_ticket[0] == 'task':
            actual_contractor = information_ticket['contractors'][0]['surname'] + ' ' + information_ticket['contractors'][0][
                'name']
        else:
            actual_contractor = information_ticket['contractor']['surname'] + ' ' + information_ticket['contractor']['name']

        # Вводим счетчик времени, чтобы цикл не был бесконечным
        count_of_time = 0

        # Ожидаем, пока исполнитель в тикете будет соответствовать ожидаемому
        while True and count_of_time < self.manager.settings.time_element_Wait:
            if actual_contractor == correct_contractor:
                # Если исполнитель тикета равен ожидаемому, то перезагружаем страницу и заканчиваем цикл
                self.refresh_the_page()
                break
            else:
                # Если исполнительно тикета НЕ РАВЕН ожидаемому, то ожидаем 1 секунду и снова запрашиваем информацию о тикете с сервера
                time.sleep(3)
                count_of_time += 3
                if type_and_number_a_ticket[0] == 'Task' or type_and_number_a_ticket[0] == 'task':
                    information_ticket = self.get_information_a_ticket_from_api(type_and_number_a_ticket)
                    actual_contractor = information_ticket['contractors'][0]['surname'] + ' ' + \
                                        information_ticket['contractors'][0]['name']
                else:
                    information_ticket = self.get_information_a_ticket_from_api(type_and_number_a_ticket)
                    actual_contractor = information_ticket['contractor']['surname'] + ' ' + \
                                        information_ticket['contractor']['name']
                if count_of_time == self.manager.settings.time_element_Wait:
                    raise
        return self

    @allure.step('Возвращаем обозревателей тикета')
    def get_observers_in_ticket(self):
        list_observers = []
        time.sleep(0.5)
        count_observers = self.find_elements(Locator.all_observers)
        for i in range(1, len(count_observers) + 1):
            observer = (By.XPATH, f'(//div[@test_id="observers-group-dropdown-activator"]/../../../..//div[@class="member-wrap member__item"])[{i}]')
            name_observer = self.get_tag_text(observer)
            list_observers.append(name_observer)
        return list_observers

    @allure.step('Возвращаем согласующих тикета')
    def get_approvers_in_ticket(self):
        list_approvers = []
        time.sleep(0.5)
        count_approvers = self.find_elements(Locator.all_approvers)
        for i in range(1, len(count_approvers) + 1):
            approver = (By.XPATH, f'(//div[@class="member"]//div[@class="agreement"])[{i}]')
            name_approver = self.get_tag_text(approver)
            list_approvers.append(name_approver)
        return list_approvers

    @allure.step('Возвращаем дополнительные описания тикета')
    def get_additional_descriptions_in_ticket(self):
        list_additional_descriptions = []
        time.sleep(0.5)
        count_additional_descriptions = self.find_elements(Locator.all_descriptions)
        for i in range(1, len(count_additional_descriptions) + 1):
            additional_description = (By.XPATH, f'(//div[@class="cke-supreme description"]//div[@class="cke-supreme__content"])[{i}]')
            text_additional_description = self.get_tag_text(additional_description)
            list_additional_descriptions.append(text_additional_description)
        return list_additional_descriptions

    @allure.step('Создаем ссылку на нужный тикет')
    def create_url_for_need_tickets(self, type_ticket, number_ticket):
        if type_ticket == 'Request':
            url_ticket = self.manager.settings.GLOBAL[self.manager.settings.branch]['main_page'] + f'tickets/request/{number_ticket}'
            return url_ticket
        elif type_ticket == 'Task':
            url_ticket = self.manager.settings.GLOBAL[self.manager.settings.branch]['main_page'] + f'tickets/task/{number_ticket}'
            return url_ticket
        elif type_ticket == 'Project':
            url_ticket = self.manager.settings.GLOBAL[self.manager.settings.branch]['main_page'] + f'projects/{number_ticket}'
            return url_ticket

    @allure.step('Переходим в нужный тикет')
    def go_to_need_ticket(self, type_ticket, number_ticket):
        url_ticket = self.create_url_for_need_tickets(type_ticket, number_ticket)
        self.goto_page(url_ticket)
        return self

    @allure.step('Возвращаем группу ответственности в заявке')
    def get_actual_responsibility_groups_in_request(self):
        name_responsibility_groups = self.get_tag_text(Locator.name_responsibility_groups)
        return name_responsibility_groups

    @allure.step('Проверка, активна ли кнопка создания тикета')
    def check_active_or_not_active_button_create_ticket(self):
        # Получаем теги кнопки создания тикета
        tag_elements = self.get_tag_attribute(Locator.fixed_panel_submit, 'class')
        if 'button_readonly' in tag_elements:
            return False
        else:
            return True