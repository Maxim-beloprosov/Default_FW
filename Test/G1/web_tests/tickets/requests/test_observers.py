from Test.G1.web_tests.g1_web_base import G1WebBase
import allure
import pytest

@allure.epic('G1')
@allure.feature('Web - Request')
@allure.story('Обозреватели в заявках')
class TestObserver(G1WebBase):

    @allure.title('Добавить обозревателя после создания заявки инициатором')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_add_observer_after_create_request_as_initiator(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Переходим в тикет
        self.APP.g1_web_ticket_base.g1_go_to_need_ticket('request', request['Id'])
        # Добавляем обозревателя
        correct_observer = 'user5 test'
        self.APP.g1_web_ticket_base.g1_add_observer(correct_observer)
        # Сохраняем заявку
        self.APP.g1_web_ticket_base.g1_click_button_create_or_save()
        # Получаем актуальных обозревателей
        actual_observers = self.APP.g1_web_ticket_base.g1_get_observers_in_ticket()
        # Проверяем количество обозревателей
        assert len(actual_observers) == 1
        # Проверяем конкретного обозревателя
        assert correct_observer in actual_observers

    @allure.title('Добавить обозревателя после создания заявки участником ГО')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_add_observer_after_create_request_as_responsibility_group_member(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Переходим в тикет
        self.APP.g1_web_ticket_base.g1_go_to_need_ticket('request', request['Id'])
        # Авторизуемся участником ГО
        self.APP.g1_web_any_page.g1_check_autorizated_user_and_loging_other_user_if_need('user2 test')
        # Добавляем обозревателя
        correct_observer = 'user5 test'
        self.APP.g1_web_ticket_base.g1_add_observer(correct_observer)
        # Сохраняем заявку
        self.APP.g1_web_ticket_base.g1_click_button_create_or_save()
        # Получаем актуальных обозревателей
        actual_observers = self.APP.g1_web_ticket_base.g1_get_observers_in_ticket()
        # Проверяем количество обозревателей
        assert len(actual_observers) == 1
        # Проверяем конкретного обозревателя
        assert correct_observer in actual_observers

    @allure.title('Добавить обозревателя после создания заявки исполнителем')
    @allure.description('Белопросов Максим')
    @pytest.mark.WebTest
    @pytest.mark.Gandiva1
    def test_add_observer_after_create_request_as_contractor(self):
        # Создаем заявку
        request = self.g1_create_request()
        # Переходим в тикет
        self.APP.g1_web_ticket_base.g1_go_to_need_ticket('request', request['Id'])
        # Авторизуемся участником ГО
        self.APP.g1_web_any_page.g1_check_autorizated_user_and_loging_other_user_if_need('user2 test')
        # Назначаем заявку на себя
        self.APP.g1_web_request_edit.g1_assign_request_to_me()
        # Добавляем обозревателя
        correct_observer = 'user5 test'
        self.APP.g1_web_ticket_base.g1_add_observer(correct_observer)
        # Сохраняем заявку
        self.APP.g1_web_ticket_base.g1_click_button_create_or_save()
        # Получаем актуальных обозревателей
        actual_observers = self.APP.g1_web_ticket_base.g1_get_observers_in_ticket()
        # Проверяем количество обозревателей
        assert len(actual_observers) == 1
        # Проверяем конкретного обозревателя
        assert correct_observer in actual_observers
