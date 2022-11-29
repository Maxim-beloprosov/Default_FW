import time

import allure
from selenium.webdriver.common.by import By
from fw.g1_web.tickets.request.g1_request_base import G1RequestBase


class Locator:
    button_assign_to_me = (By.XPATH, '//button[@class="ga_bttn_status bttn_e"]/span')

class G1RequestEdit(G1RequestBase):
    @allure.step('Нажать на кнопку Назначить на себя')
    def g1_click_button_assign_to_me(self):
        self.g1_page_loaded()
        self.scroll_to_element(Locator.button_assign_to_me)
        self.click_element(Locator.button_assign_to_me)
        return self

    @allure.step('Назначить заявку на себя')
    def g1_assign_request_to_me(self):
        # Нажимаем кнопку Назначить на себя
        self.g1_click_button_assign_to_me()
        # Получаем авторизованного пользователя
        actual_user = self.g1_get_surname_and_name_autorizated_user()
        # Разбиваем и меняем местами ФИ, т.к. при назначении заявки на себя и до сохранении, сначала пишется имя, а потом уже фамилия (test user1)
        actual_user_comeback = actual_user.split(' ')
        actual_user_comeback = actual_user_comeback[1] + ' ' + actual_user_comeback[0]
        # Ожидаем, пока появится добавленный пользователь
        find_add_contractor = (By.XPATH, f'//div[@class="ga_participant_block clearfix"]//div[contains(text(),"{actual_user_comeback}")]')
        self.find_element(find_add_contractor)
        # Сохраняем заявку
        self.manager.g1_web_ticket_base.g1_click_button_create_or_save()
        return actual_user

    @allure.step('Изменить норматив через выбор всех сущностей')
    def g1_change_normative_select_all_essence(self, job_type):
        department = self.manager.group_data.service_template_g1[job_type]['department']
        category = self.manager.group_data.service_template_g1[job_type]['category']
        request_type = self.manager.group_data.service_template_g1[job_type]['type']
        # Заполняем все сущности норматива
        self.g1_set_department(department)
        self.g1_set_category(category)
        self.g1_set_request_type(request_type)
        self.g1_set_job_type(job_type)
        # Сохраняем заявку
        self.manager.g1_web_ticket_base.g1_click_button_create_or_save()
        return self

    @allure.step('Изменить норматив через глобальный поиск')
    def g1_change_normative_use_global_search(self, job_type):
        department = self.manager.group_data.service_template_g1[job_type]['department']
        category = self.manager.group_data.service_template_g1[job_type]['category']
        request_type = self.manager.group_data.service_template_g1[job_type]['type']
        # Выбираем норматив, используя полный путь через глобальный поиск
        path_normative = department + ' → ' + category + ' → ' + request_type + ' → ' + job_type
        self.manager.g1_web_request_new.g1_select_need_normative_in_global_search(path_normative)
        # Сохраняем заявку
        self.manager.g1_web_ticket_base.g1_click_button_create_or_save()
        return self
