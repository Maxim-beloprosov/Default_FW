import time

import allure
import pytest
from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Ticket')
@allure.story('Фильтрация списка тикетов')
class TestApiTicketsFilter(ApiBase):

    @allure.title('Список тикетов во вкладке "На мне"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_tickets_is_contractor_tab(self):

        # Создание задачи
        created_task = self.create_task({'contractorId': 'test_user09'})

        # Фильтруем список тикетов
        tickets_list = self.APP.api_tickets_filtration.filter_tickets_by_tab_contractor(created_task['createdDate'], 10)

        # Перелогиниваемся на пользователя с правами модератора
        self.APP.api_token.get_token('SystemOperator')

        # Проверяем правильность фильтрации
        filter_result = self.filter_find_another_access_in_ticket(tickets_list['items'], 'ticketParticipations', 'Contractor',
                                                                  'test_user09')

        assert filter_result

    @allure.title('Список тикетов во вкладке "Мои согласования"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_tickets_is_approver_tab(self):

        # Создание задачи
        created_task = self.create_task({'approvers': ['test_user08']})

        # Переход на согласующего
        self.APP.api_token.get_token('test_user08')

        # Фильтруем список тикетов
        tickets_list = self.APP.api_tickets_filtration.filter_tickets_by_tab_my_agreements(created_task['createdDate'], 10)

        # Перелогиниваемся на пользователя с правами модератора
        self.APP.api_token.get_token('SystemOperator')

        # Проверяем правильность фильтрации
        filter_result = self.filter_find_another_access_in_ticket(tickets_list['items'], 'ticketParticipations', 'Approver', 'test_user08')

        assert filter_result

    @allure.title('Список тикетов во вкладке "Обозреваемые"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.NORMAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_tickets_is_observer_tab(self):

        # Создание задачи
        created_task = self.create_task({'observers': ['test_user08']})

        # Переход на обозревателя
        self.APP.api_token.get_token('test_user08')

        # Фильтруем список тикетов
        tickets_list = self.APP.api_tickets_filtration.filter_tickets_by_tab_observer(created_task['createdDate'], 10)

        # Перелогиниваемся на пользователя с правами модератора
        self.APP.api_token.get_token('SystemOperator')

        # Проверяем правильность фильтрации
        filter_result = self.filter_find_another_access_in_ticket(tickets_list['items'], 'ticketParticipations', 'Observer', 'test_user08')

        assert filter_result

    @allure.title('Список тикетов во вкладке "От меня"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_tickets_is_initiator_tab(self):

        # Создание задачи
        created_task = self.create_task()

        # Фильтруем список тикетов
        tickets_list = self.APP.api_tickets_filtration.filter_tickets_by_tab_from_me(created_task['createdDate'], 10)

        # Перелогиниваемся на пользователя с правами модератора
        self.APP.api_token.get_token('SystemOperator')

        # Проверяем правильность фильтрации
        filter_result = self.filter_find_another_access_in_ticket(tickets_list['items'], 'ticketParticipations', 'Initiator', 'test_user09')

        assert filter_result

    @allure.title('Список тикетов во вкладке "Избранное"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_tickets_my_favorites_tab(self):

        # Создание задачи
        created_task = self.create_task()

        # Добавляем задачу в избранное
        self.APP.api_actions_in_task.add_task_in_favourites(created_task)

        # Фильтруем список тикетов
        tickets_list = self.APP.api_tickets_filtration.filter_tickets_by_tab_favourites(created_task['createdDate'], 10)

        # Проверяем правильность фильтрации
        filter_result = self.filter_find_another_response_in_ticket(tickets_list['items'], 'isFavourite', True)

        assert filter_result

    @allure.title('Список тикетов во вкладке "На моих ГО"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_tickets_my_responsibility_groups(self):

        # Создаём заявку
        created_task = self.create_request()

        # Перелогиниваемся на участника ГО
        self.APP.api_token.get_token('test_user04')

        # Фильтруем список тикетов
        tickets_list = self.APP.api_tickets_filtration.filter_tickets_by_tab_on_my_responsibility_groups(created_task['createdDate'], 10)

        # Проверяем правильность фильтрации
        filter_result = self.filter_find_another_response_in_ticket(tickets_list['items'], 'responsibilityGroup', 'Группа_тестирования_№1')

        assert filter_result
