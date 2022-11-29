import allure

from fw.api.request.api_requests import ApiRequests


class ApiActionsInRequest(ApiRequests):

    @allure.title('Согласовать заявку')
    def approve_request(self, sync_token, request_id):

        # Формируем тело запроса для согласования
        request_body = {
            "syncToken": sync_token
        }

        # Принимаем положительное решение согласующим
        request = self.manager.api_requests.put_requests_id_actions_approve(request_id, request_body)
        return request