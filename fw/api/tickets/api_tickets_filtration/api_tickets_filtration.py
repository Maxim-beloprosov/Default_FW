import time

import allure

from fw.api.tickets.api_tasks import ApiTasks


class FiltrationInTickets(ApiTasks):

    @allure.step('Фильтрация тикетов по табу "Все"')
    def filter_tickets_by_tab_all(self, expected_status_response, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации по "Все"
        filter_body = {
            "tabFilterType": "All",
            "allTabOptions": [
                expected_status_response
            ],
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets
        }

        # Фильтруем по "Все"
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "Статус"')
    def filter_tickets_by_tab_status(self, expected_status_response, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации по "Статус"
        filter_body = {
            "statuses": [
                expected_status_response
            ],
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets,
        }

        # Фильтруем по "Статус"
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "Тип"')
    def filter_tickets_by_tab_ticket_type(self, expected_ticket_type_response, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации по "Тип"
        filter_body = {
            "ticketTypes": [
                expected_ticket_type_response
            ],
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets
        }

        # Фильтруем по "Тип"
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "Исполнитель". Есть ли исполнитель.')
    def filter_tickets_by_tab_contractor_is_contractor(self, expected_contractor_response, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации по "Исполнитель"
        filter_body = {
            "isContractor": expected_contractor_response,
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets,
        }

        # Фильтруем по "Исполнитель"
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "Статус согласования"')
    def filter_tickets_by_tab_agreements_status(self, approver, expected_agreements_status_response, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации по "Статус согласования"
        filter_body = {
            "approverIds": [
                self.manager.group_data.users[approver]['user_id']
            ],
            "agreementStatuses": [
                expected_agreements_status_response
            ],
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets,
        }

        # Фильтруем по "Статус согласования"
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "Услуга"')
    def filter_tickets_by_tab_service(self, service_id, created_date, amount_filter_tickets,  time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации по "Услуга"
        filter_body = {
            "gandivaServiceIds": [
                service_id
            ],
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets,
        }

        # Фильтруем по "Услуга"
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "Дата создания"')
    def filter_tickets_by_tab_created_date(self, createdDateFrom, createdDateTo, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации по параметру "Дата создания"
        filter_body = {
            "createdDateFrom": createdDateFrom,
            "createdDateTo": createdDateTo,
            "take": amount_filter_tickets,
        }

        # Фильтруем по "Дата создания"
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "Дата начала"')
    def filter_tickets_by_tab_begin_date(self, beginDateFrom, beginDateTo, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации по параметру "Дата начала"
        filter_body = {
            "beginDateFrom": beginDateFrom,
            "beginDateTo": beginDateTo,
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets,
        }

        # Фильтруем по "Дата начала"
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "Дата окончания"')
    def filter_tickets_by_tab_end_date(self, endDateFrom, endDateTo, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации по параметру "Дата окончания"
        filter_body = {
            "endDateFrom": endDateFrom,
            "endDateTo": endDateTo,
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets,
        }

        # Фильтруем по "Дата окончания"
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "Дата закрытия"')
    def filter_tickets_by_tab_close_date(self, closingDateFrom, closingDateTo, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации по параметру "Дата закрытия"
        filter_body = {
            "closingDateFrom": closingDateFrom,
            "closingDateTo": closingDateTo,
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets,
        }

        # Фильтруем по "Дата закрытия"
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "Оценка"')
    def filter_tickets_by_tab_rating(self, rating, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации по параметру "Оценка"
        filter_body = {
            "ratings": rating,
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets,
        }

        # Фильтруем по "Оценка"
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "Инициатор"')
    def filter_tickets_by_tab_initiator(self, initiator, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации по параметру "Инициатор"
        filter_body = {
            "initiatorIds": [
                self.manager.group_data.users[initiator]['user_id']
            ],
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets,
        }

        # Фильтруем по "Инициатор"
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "Исполнитель". Id исполнителя.')
    def filter_tickets_by_tab_contractor_id_contractor(self, contractor, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации по id исполнителя
        filter_body = {
            "contractorIds": [
                self.manager.group_data.users[contractor]['user_id']
            ],
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets,
        }

        # Фильтруем по "Исполнитель"
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "Группа ответственности"')
    def filter_tickets_by_tab_responsibility_group(self, responsibility_group_id, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации по табу "Группа ответственности"
        filter_body = {
            "responsibilityGroupIds": [
                responsibility_group_id
            ],
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets,
        }

        # Фильтруем по "Группа ответственности"
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "Согласующий"')
    def filter_tickets_by_tab_approver(self, approver, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации по согласующим
        filter_body = {
            "approverIds": [
                self.manager.group_data.users[approver]['user_id']
            ],
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets,
        }

        # Фильтруем по "Согласующий"
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "На мне"')
    def filter_tickets_by_tab_contractor(self, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации
        filter_body = {
            "tabFilterType": "IAmContractor",
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets
        }

        # Фильтруем список тикетов
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "Мои согласования"')
    def filter_tickets_by_tab_my_agreements(self, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации
        filter_body = {
            "tabFilterType": "MyAgreements",
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets
        }

        # Фильтруем список тикетов
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "Я - обозреватель"')
    def filter_tickets_by_tab_observer(self, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации
        filter_body = {
            "tabFilterType": "MyObservers",
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets
        }

        # Фильтруем список тикетов
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "От меня"')
    def filter_tickets_by_tab_from_me(self, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации
        filter_body = {
            "tabFilterType": "IAmInitiator",
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets
        }

        # Фильтруем список тикетов
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "Избранное"')
    def filter_tickets_by_tab_favourites(self, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации
        filter_body = {
            "tabFilterType": "MyFavourites",
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets
        }

        # Фильтруем список тикетов
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets

    @allure.step('Фильтрация тикетов по табу "На моих ГО"')
    def filter_tickets_by_tab_on_my_responsibility_groups(self, created_date, amount_filter_tickets, time_sleep=5):
        # Созданный объект попадает в поисковую выборку примерно через 2-3 секунды.
        time.sleep(time_sleep)
        # Формируем тело для фильтрации
        filter_body = {
            "tabFilterType": "MyResponsibilityGroups",
            "createdDateFrom": self.manager.time.add_seconds_to_date_for_api_g2(created_date, -2),
            "take": amount_filter_tickets
        }

        # Фильтруем список тикетов
        filter_tickets = self.manager.api_tickets.post_tickets_filter(filter_body)

        return filter_tickets
