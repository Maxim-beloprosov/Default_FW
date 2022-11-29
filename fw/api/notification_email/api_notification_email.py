import allure

from fw.api.api_base import APIBase

class ApiNotificationEmail(APIBase):

    @allure.step('Лог по отправке писем, включает в себя разные данные по письмам. POST /api/NotificationEmailLogs/Mails')
    def post_notification_email_logs_mails(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/NotificationEmailLogs/Mails', body, params)