import allure

from fw.api.api_base import APIBase


class ApiNodes(APIBase):

    @allure.step('Добавление предшественника. POST /api/TicketRelation/Tickets/{id}/AddPrevious')
    def post_add_previous_to_task(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/TicketRelation/Tickets/{id}/AddPrevious', body, params)