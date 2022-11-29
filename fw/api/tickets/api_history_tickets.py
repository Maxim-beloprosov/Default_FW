import allure

from fw.api.api_base import APIBase


class ApiHistoryTickets(APIBase):

    @allure.step('/api/HistoryTicket/Tickets/{id}')
    def post_history_ticket_tickets_id(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/HistoryTicket/Tickets/{id}', body, params)
