import allure

from fw.api.api_base import APIBase


class ApiTickets(APIBase):

    @allure.step('Список общего количества тикетов в каждой вкладке. POST /api/Tickets/Tabs/TotalCounts')
    def post_tickets_tabs_total_counts(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Tickets/Tabs/TotalCounts', body, params)

    @allure.step('Список задач, заявок, проектов POST /api/Tickets/Filter')
    def post_tickets_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Tickets/Filter', body, params)

    @allure.step('Вернуть доступ пользователя с разбивкой по участию к тикету и в списке тикетов. POST /Tickets/post_api_Tickets_id_Users_userId_AccessByParticipation')
    def  post_tickets_id_users_userId_access_by_participation(self, id, userId, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Tickets/{id}/Users/{userId}/AccessByParticipation', params)