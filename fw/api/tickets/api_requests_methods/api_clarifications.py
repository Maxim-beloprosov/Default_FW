import allure

from fw.api.tickets.api_requests import ApiRequests


class ApiClarifications(ApiRequests):

    @allure.title('Задать уточнение инициатору')
    def ask_to_initiator_clarification(self, sync_token, request_id, clarification=None):

        if clarification == None:
            # Подготовка данных для уточнения инициатору
            clarification = "TestClarification AutomationApiTests" + self.manager.time.get_date_time_Y_m_d_H_M_S()

        # Формируем тело запроса для уточнения инициатору
        request_body = {
            "syncToken": sync_token,
            "contentParts": [
                {"type": "Text",
                 "text": clarification}
            ]
        }

        # Задаем уточнение инициатору
        request = self.manager.api_requests.put_requests_id_actions_clarifications_ask_initiator(request_id,
                                                                                             request_body)
        return request

    @allure.title('Задать уточнение исполнителю')
    def ask_to_contractor_clarification(self, sync_token, request_id, clarification=None):

        if clarification == None:
            # Подготовка данных для уточнения инициатору
            clarification = "TestClarification AutomationApiTests" + self.manager.time.get_date_time_Y_m_d_H_M_S()

        # Формируем тело запроса для уточнения инициатору
        request_body = {
            "syncToken": sync_token,
            "contentParts": [
                {"type": "Text",
                 "text": clarification}
            ]
        }

        # Задаем уточнение инициатору
        request = self.manager.api_requests.put_requests_id_actions_clarifications_ask_contractor(request_id,
                                                                                                 request_body)
        return request

    @allure.title('Инициатор отвечает на уточнение')
    def initiator_to_answer_clarification(self, sync_token, request_id, clarification_id):

        # Формируем тело запроса для ответа инициатором на уточнение
        request_body = {
            "syncToken": sync_token,
            "clarificationId": clarification_id,
            "contentParts": [
                {"type": "Text",
                 "text": "TestAnswer AutomationApiTests" + self.manager.time.get_date_time_Y_m_d_H_M_S()}
            ]
        }

        # Инициатором отвечаем на уточнение
        request = self.manager.api_requests.put_requests_id_actions_clarifications_initiator_answer(request_id,
                                                                                                  request_body)
        return request

    @allure.title('Исполнитель отвечает на уточнение')
    def contractor_to_answer_clarification(self, sync_token, request_id, clarification_id):

        # Формируем тело запроса для ответа исполнителем на уточнение
        request_body = {
            "syncToken": sync_token,
            "clarificationId": clarification_id,
            "contentParts": [
                {"type": "Text",
                 "text": "TestAnswer AutomationApiTests" + self.manager.time.get_date_time_Y_m_d_H_M_S()}
            ]
        }

        # Исполнителем отвечаем на уточнение
        request = self.manager.api_requests.put_requests_id_actions_clarifications_contractor_answer(request_id,
                                                                                                  request_body)
        return request

    @allure.title('Отменить уточнение')
    def cancel_clarifications(self, sync_token, request_id, clarification_id):

        # Формируем тело запроса для отмены уточнения
        request_body = {
            "syncToken": sync_token,
            "clarificationId": clarification_id
        }

        # Отменяем уточнение
        request = self.manager.api_requests.put_requests_id_actions_clarifications_cancel(request_id, request_body)
        return request