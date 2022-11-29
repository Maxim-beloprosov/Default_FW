import time

import allure

from fw.api.tickets.api_tickets import ApiTickets


class ActionsInTickets(ApiTickets):

    @allure.title('Получение кол-ва тикетов в разных вкладках')
    def get_counts(self, ticket_type, ticket_tab):

        tab = None
        if ticket_tab == "All":
            tab = 0
        elif ticket_tab == "IAmInitiator":
            tab = 1
        elif ticket_tab == "IAmContractor":
            tab = 2
        elif ticket_tab == "MyResponsibilityGroups":
            tab = 3
        elif ticket_tab == "MyAgreements":
            tab = 4
        elif ticket_tab == "MyObservers":
            tab = 5
        elif ticket_tab == "MyFavourites":
            tab = 6

        # Подготовка тела
        filter_body = {
            "ticketTypes": [
                ticket_type
            ]
        }

        # Вывод кол-ва всех созданных задач до создания новой:
        check_counts = self.manager.api_tickets.post_tickets_tabs_total_counts(filter_body)
        counts = check_counts[tab]['totalCount']

        return counts

    @allure.title('Проверка изменения кол-ва тиектов при создании нового')
    def check_counts(self, ticket_type, tab, old_counts):

        # Проверка, что кол-во тиектов изменилось при создании нового
        check = False

        for i in range(1, self.manager.settings.time_element_Wait):
            new_counts = self.get_counts(ticket_type, tab)
            if new_counts - old_counts == 1:
                check = True
                break
            else:
                time.sleep(0.5)

        return check

    @allure.title('Назначение исполнителя в заявке')
    def appoint_contractor(self, request_id, request_sync_token, contractor_id):

        # Назначение исполнителя
        appoint = self.manager.api_requests.put_requests_id_actions_change_contractor(request_id, {'contractorId': contractor_id, 'syncToken':
            request_sync_token})

        return appoint
