import allure
from selenium.webdriver.common.by import By

from fw.g1_web.tickets.request.g1_request_base import G1RequestBase


class Locator:
    block_select_region = (By.XPATH, '//*[@id="RegionId_chosen"]')
    input_text_global_search = (By.XPATH, '//div[@id="global_classificator_chosen"]//input')
    text_modal_window = (By.XPATH, '//div[@class="core_modal_text"]/div')
    waiting_list_user_for_change_normative = (By.XPATH, '//ul[@class="chosen-results"]/li[contains(@class, "active-result")]')
    result_modal_window_for_select_normative = (By.XPATH, '//ul[@class="chosen-results"]/li')

class G1RequestNew(G1RequestBase):

    @allure.step('Создать заявку выбирая все сущности норматива)')
    def g1_create_request_select_all_essence(self, job_type=None, description=None, approver=None, observer=None, date_start=None):
        # Проверяем, пришел ли Вид, если нет - назначаем его по дефолту
        if job_type is None:
            job_type = 'Тестовый_Тип_1'
        # Назначаем остальные сущности норматива из информации вида
        department = self.manager.group_data.service_template_g1[job_type]['department']
        category = self.manager.group_data.service_template_g1[job_type]['category']
        request_type = self.manager.group_data.service_template_g1[job_type]['type']
        # Переходим к созданию заявки
        self.manager.g1_web_any_page.g1_click_button_plus_request()
        # Заполняем все сущности норматива
        self.g1_set_department(department)
        self.g1_set_category(category)
        self.g1_set_request_type(request_type)
        self.g1_set_job_type(job_type)
        # Проверяем, пришло ли описание, если нет - назначаем его по дефолту
        if description is None:
            description = "TestDescription AutomationWebTests " + self.manager.time.get_date_time_Y_m_d_H_M_S()
        # Заполняем описание
        self.g1_fill_description(description)
        # Если пришел согласующий, добавляем его
        if approver is not None:
            self.g1_add_approver(approver)
        # Если пришел обозреватель, добавляем его
        if observer is not None:
            self.g1_add_observer(observer)
        # Если пришла дата старта, добавляем ее
        if date_start is not None:
            self.g1_fill_start_date(date_start)
        # Создаем заявку
        self.manager.g1_web_ticket_base.g1_click_button_create_or_save()
        return self.manager.g1_web_request_edit

    @allure.step('Создать заявку используя глобальный поиск')
    def g1_create_request_use_global_search(self, job_type=None, description=None, approver=None, observer=None, date_start=None):
        # Проверяем, пришел ли Вид, если нет - назначаем его по дефолту
        if job_type is None:
            job_type = 'Тестовый_Тип_1'
            # Назначаем остальные сущности норматива из информации вида
        department = self.manager.group_data.service_template_g1[job_type]['department']
        category = self.manager.group_data.service_template_g1[job_type]['category']
        request_type = self.manager.group_data.service_template_g1[job_type]['type']
        # Переходим к созданию заявки
        self.manager.g1_web_any_page.g1_click_button_plus_request()
        # Выбираем норматив, используя полный путь через глобальный поиск
        path_normative = department + ' → ' + category + ' → ' + request_type + ' → ' + job_type
        self.g1_select_need_normative_in_global_search(path_normative)
        # Проверяем, пришло ли описание, если нет - назначаем его по дефолту
        if description is None:
            description = "TestDescription AutomationWebTests " + self.manager.time.get_date_time_Y_m_d_H_M_S()
        # Заполняем описание
        self.g1_fill_description(description)
        # Если пришел согласующий, добавляем его
        if approver is not None:
            self.g1_add_approver(approver)
        # Если пришел обозреватель, добавляем его
        if observer is not None:
            self.g1_add_observer(observer)
        # Если пришла дата старта, добавляем ее
        if date_start is not None:
            self.g1_fill_start_date(date_start)
        # Создаем заявку
        self.manager.g1_web_ticket_base.g1_click_button_create_or_save()
        return self.manager.g1_web_request_edit

    @allure.step('Смена региона')
    def g1_change_region(self, region_text):
        # Нажимаем на блок регионов
        self.click_element(Locator.block_select_region)
        # Выбираем нужный регион
        need_region = (By.XPATH, f'//div[@id="RegionId_chosen"]//li[contains(text(), "{region_text}")]')
        self.move_to_element(need_region)
        self.click_element(need_region)
        # Ожидаем, пока регион будет выбран
        wait_select_region = (By.XPATH, f'//a[@class="chosen-single"]/span[contains(text(), "{region_text}")]')
        self.find_element(wait_select_region)
        return self

    @allure.step('Ввод текста в глобальный поиск')
    def g1_input_text_in_global_search(self, text):
        self.g1_page_loaded()
        self.click_element(Locator.input_text_global_search)
        self.send_keys(Locator.input_text_global_search, text)
        return self

    @allure.step('Выбор нужного норматива в глобальном поиске')
    def g1_select_need_normative_in_global_search(self, text):
        self.g1_input_text_in_global_search(text)
        self.find_elements(Locator.waiting_list_user_for_change_normative)
        normatives = self.find_elements(Locator.result_modal_window_for_select_normative)
        for i in range(1, len(normatives) + 1):
            need_normative = (By.XPATH, f'//ul[@class="chosen-results"]/li[{i}]')
            name_normative = self.get_tag_text(need_normative)
            if name_normative == text:
                self.move_to_element(need_normative)
                self.click_element(need_normative)
                break
        return self

    @allure.step('Возвращает текст примечания')
    def g1_get_text_note(self):
        return self.get_tag_text(Locator.text_modal_window)
