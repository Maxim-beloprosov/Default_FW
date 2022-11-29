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

    @allure.title('Отменить заявку')
    def cancel_request(self, sync_token, request_id):
        # Подготовка данных отмены заявки
        reason_cancel = "TestReasonCanceled AutomationApiTests" + self.manager.time.get_date_time_Y_m_d_H_M_S()

        # Формируем тело запроса отмены заявки
        request_body = {
            "text": reason_cancel,
            "syncToken": sync_token
        }
        # Отменяем заявку
        request = self.manager.api_requests.put_requests_id_actions_cancel(request_id, request_body)
        return request

    @allure.title('Отклонить заявку')
    def reject_request(self, sync_token, request_id):

        # Подготовка данных для отклонения заявки
        reason = "TestReasonRejected AutomationApiTests" + self.manager.time.get_date_time_Y_m_d_H_M_S()

        # Формируем тело запроса для принятии отрицательного решения по согласованию
        request_body = {
            "syncToken": sync_token,
            'text': reason
        }

        # Принимаем отрицательное решение согласующим
        request = self.manager.api_requests.put_requests_id_actions_reject(request_id, request_body)
        return request

    @allure.title('Назначить заявку на себя')
    def assign_to_me(self, sync_token, request_id):

        # Формируем тело запроса для назначения заявки на себя
        request_body = {
            "syncToken": sync_token
        }

        # Назначаем заявку на себя
        request = self.manager.api_requests.put_requests_id_actions_assign_to_me(request_id, request_body)
        return request

    @allure.title('Апеллировать заявку')
    def appeal_request(self, sync_token, request_id):

        # Подготовка данных для апеллирования заявки
        reason = "TestReasonAppeal AutomationApiTests" + self.manager.time.get_date_time_Y_m_d_H_M_S()

        # Формируем тело запроса для апеллирования заявки
        request_body = {
            "syncToken": sync_token,
            'text': reason
        }

        # Апеллируем заявку
        request = self.manager.api_requests.put_requests_id_actions_appeal(request_id, request_body)
        return request

    @allure.title('Отправить заявку в проверку')
    def send_request_to_resolved(self, sync_token, request_id):

        # Формируем тело запроса для перевода заявки в проверку
        request_body = {
            "syncToken": sync_token
        }

        # Переводим заявку в проверку
        request = self.manager.api_requests.put_requests_id_actions_resolve(request_id, request_body)
        return request

    @allure.title('Возвращаем заявку на доработку')
    def comeback_ticket_to_overwork(self, sync_token, request_id):

        # Формируем тело запроса для возврата заявки на доработку
        request_body = {
            "text": "TestReasonComeBackInWork AutomationApiTests" + self.manager.time.get_date_time_Y_m_d_H_M_S(),
            "syncToken": sync_token
        }

        # Возвращаем заявку на доработку
        request = self.manager.api_requests.put_requests_id_actions_return_to_work(request_id, request_body)
        return request

    @allure.title('Возвращаем заявку в работу')
    def comeback_ticket_to_work(self, sync_token, request_id):

        # Формируем тело запроса для возврата заявки в работу
        request_body = {
            "syncToken": sync_token
        }

        # Возвращаем заявку в работу исполнителем
        request = self.manager.api_requests.put_requests_id_actions_back_to_work(request_id, request_body)
        return request

    @allure.title('Закрыть заявку')
    def close_request(self, sync_token, request_id, rating):

        # Подготовка данных для закрытия заявки
        reason = "TestReasonClosed WithRating " + str(
            rating) + " AutomationApiTests" + self.manager.time.get_date_time_Y_m_d_H_M_S()
        if rating == 5:
            # Формируем тело запроса закрытия заявки
            request_body = {
                "rating": rating,
                "syncToken": sync_token
            }
        else:
            # Формируем тело запроса закрытия заявки
            request_body = {
                "rating": rating,
                "text": reason,
                "syncToken": sync_token
            }

        # Закрываем заявку с нужной оценкой
        request = self.manager.api_requests.put_requests_id_actions_close(request_id, request_body)
        return request

    @allure.title('Взять заявку в работу')
    def take_request_for_work(self, sync_token, request_id):

        # Формируем тело запроса для взятия заявку в работу
        request_body = {
            "syncToken": sync_token
        }

        # Берем заявку в работу
        request = self.manager.api_requests.put_requests_id_actions_to_work(request_id, request_body)
        return request

    @allure.title('Проверить корректность счётчика фактического времени')
    def check_factual_time(self, request_counters, counter_type, expected_time):

        # Изначально задаём значение false
        flag = False

        # Проверяем корректность счётчика
        for item in request_counters:
            if item['type'] == counter_type:
                if item['adjustedTotalMinutes'] == expected_time:
                    flag = True

        return flag

    @allure.title('Проверить соответствие счётчика фактического времени пользователю')
    def check_equal_target_id(self, request_counters, counter_type, target_id):

        # Изначально задаём значение false
        flag = False

        # Проверяем корректность счётчика
        for item in request_counters:
            if item['type'] == counter_type:
                if item['targetId'] == target_id:
                    flag = True

        return flag

    @allure.title('Добавить дополнительное описание к заявке')
    def add_additional_descriptions_in_request(self, request_id, descriptions_mass={}):
        descriptions_body = {}
        # собираем тело
        if 'type' in descriptions_mass and 'text' in descriptions_mass:
            descriptions_body['contentParts'] = [{
                'type': descriptions_mass['type'],
                'text': descriptions_mass['text'],
            }]
        if 'type' in descriptions_mass and 'fileId' in descriptions_mass:
            descriptions_body['contentParts'] = [{
                'type': descriptions_mass['type'],
                'fileId': descriptions_mass['fileId']
            }]

        # Добавляем описание к заявке
        request = self.post_requests_id_description(request_id, descriptions_body)

        return request