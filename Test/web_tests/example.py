import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - request')
@allure.story('Создание заявки')
class TestCreateRequest(WebBase):

    @allure.title('Создание заявки с выбором услуги из дерева')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_create_request_first(self):
        # Переходим к созданию заявки
        self.APP.web_any_page.click_btn_create_request_plus_menu()
        # Выбираем услугу
        self.APP.web_request_create.select_services_in_tree(self.APP.group_data.service_template['AutomationService Тестовый Тип 1']['name'])
        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_tickets_base.fill_description_in_ticket(correct_description)
        # Создаем заявку
        self.APP.web_request_create.button_to_create_request()
        # Переходим в список тикетов
        self.APP.web_any_page.click_tickets_left_menu()
        # Вводим в поиск описание созданной заявки
        self.APP.web_tickets_list.input_text_in_search(correct_description)
        # Переходим в тикет с нужным описанием
        self.APP.web_tickets_list.go_to_ticket_in_list(correct_description)
        # Сравниваем два описания между собой
        actual_description = self.APP.web_tickets_base.get_description_in_ticket()
        assert correct_description == actual_description