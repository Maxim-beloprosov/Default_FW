import allure

from fw.g1_api.g1_requests.g1_api_requests import G1ApiRequests


class G1ActionsInRequests(G1ApiRequests):

    @allure.title('Действия с заявкой, изменение её статуса.')
    def actions_in_request(self, id, last_modified_date, action_id, description=None, rating=None, user_id=None, group_id=None):

        request_body = {
            'LastModifiedDate': last_modified_date,
            'BidAction': action_id,
        }
        if description:
            request_body['Description'] = description
        if rating:
            request_body['Rating'] = rating
        if user_id:
            request_body['UserId'] = user_id
        if group_id:
            request_body['GroupId'] = group_id

        request = self.put_requests_id_action(id, request_body)
        return request

    @allure.title('Обновление исполнителя')
    def update_contractor_in_request(self, id, last_modified_date, contractor_id):

        request_body = {
            'LastModifiedDate': last_modified_date,
            'Contractor': {
                'Id': contractor_id
            }
        }
        request = self.put_requests_id_contractor(id, request_body)
        return request

    @allure.title('Добавление комментария к заявке')
    def add_comment_in_request(self, id, addressees_id=[], text='AutomationApiTest Comment'):

        request_body = {
            'Text': text,
            'Addressees': addressees_id
        }
        request = self.post_requests_id_comments(id, request_body)
        return request

    @allure.title('Добавление вопроса-уточнения в заявке')
    def add_clarification_question_in_request(self, id, clarification_type, text='AutomationApiTest ClarificationQuestion'):

        request_body = {
          'ClarificationType': clarification_type,
            'Text': text
        }
        request = self.post_requests_id_clarification_question(id, request_body)
        return request

    @allure.title('Добавление ответа на вопрос-уточнение в заявке')
    def add_clarification_answer_in_request(self, comment_id, text='AutomationApiTest ClarificationAnswer'):

        request_body = {
            'Text': text
        }
        request = self.post_requests_comments_id_clarification_answer(comment_id, request_body)
        return request

    @allure.title('Обновление обозревателей в заявке')
    def update_observers_in_request(self, request_id, last_modified_date, observers_id):
        """
        observers_id может быть в виде любой итерируемой коллекции
        например: observers_id=[123, 1321]
        """

        request_body = {
            'LastModifiedDate': last_modified_date,
            'Observers': [],
        }
        for id in observers_id:
            request_body['Observers'].append({'Id': id})
        request = self.put_requests_id_observers(request_id, request_body)
        return request

    @allure.title('Обновление инициатора в заявке')
    def update_initiatior_in_request(self, id, last_modified_date, user_id):

        request_body = {
            'LastModifiedDate': last_modified_date,
            'Person': {
                'Id': user_id
            }
        }
        request = self.put_requests_id_initiator(id, request_body)
        return request


    @allure.step('Добавить согласующего в заявку')
    def put_add_approver(self, request_id, last_modified_date, approver_id, params=None):

        body = {
            'LastModifiedDate': last_modified_date,
            'Approvers': []

        }
        for id in approver_id:
            body['Approvers'].append({'Id': 0, 'userId': id, "Status": 0, "IsUserAdded": True})

        add_approver = self.manager.g1_api_requests.put_requests_id_approvers(request_id, body)

        return add_approver

    @allure.story('Изменить дату начала заявки')
    def change_request_start_date(self, request_id, last_modified_date, required_start_date):

        body = {
            "LastModifiedDate": last_modified_date,
            "RequiredStartDate": required_start_date,
        }

        required = self.put_requests_id_required_start_date(request_id, body)

        return required

    @allure.step('Оценить и закрыть')
    def g1_rate_and_close_request(self, request_id, last_modified_date, rating):
        if rating == 5:
            body = {
                "LastModifiedDate": last_modified_date,
                "BidAction": self.manager.group_data.g1_tickets_actions['RUS']['Оценить и закрыть'],
                "Rating": rating
            }
        else:
            body = {
                "LastModifiedDate": last_modified_date,
                "BidAction": self.manager.group_data.g1_tickets_actions['RUS']['Оценить и закрыть'],
                "Rating": rating,
                "Description": "TestApiRating"
            }
        request = self.put_requests_id_action(request_id, body)

        return request