import allure

from fw.api.api_base import APIBase

class ApiNotification(APIBase):

    @allure.step('Изменить (включить/отключить) подписку пользователя на уведомления. PUT /api/Notification/User/{id}')
    def put_notification_user_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Notification/User/{id}', body, params)