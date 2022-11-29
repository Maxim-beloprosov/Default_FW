import allure

from fw.api.tickets.api_requests import ApiRequests


class ApiChangeRequest(ApiRequests):

    @allure.step('Удалить дату начала')
    def delete_begin_date(self, sync_token, request_id):

        # Формируем тело запроса для удаления даты начала
        request_body = {
            "syncToken": sync_token,
            "beginDate": None
        }

        # Обновляем заявку, удаляя дату начала
        request = self.manager.api_requests.put_requests_id(request_id, request_body)
        return request

    @allure.step('Изменить дату начала')
    def change_begin_date(self, sync_token, request_id, delta):

        # Формируем тело запроса для указании даты начала
        request_body = {
            "beginDate": self.manager.time.get_date_increased_x_days_json(delta),
            "syncToken": sync_token
        }

        # Изменяем дату начала в заявке
        request = self.manager.api_requests.put_requests_id(request_id, request_body)
        return request

    @allure.step('Добавить согласующего')
    def add_approver(self, sync_token, request_id, approver):

        # Формируем тело запроса для добавлении согласующего
        request_body = {
            "approverId": self.manager.group_data.users[approver]['user_id'],
            "syncToken": sync_token
        }

        # Добавляем согласующего
        request = self.manager.api_requests.post_requests_id_agreements(request_id, request_body)
        return request

    @allure.step('Смена планового времени исполнения в заявке (с правами модератора)')
    def change_planned_time_execution(self, sync_token, request_id, time=1000):
        # Формируем тело запроса для изменения планового времени в заявке
        request_body = {
            'plannedTimeOfExecution': time,
            'syncToken': sync_token,
        }

        # Меняем плановое время
        request = self.put_requests_id_actions_change_planned_time(request_id, request_body,
                                                         params={'isModeratorMode': True})
        return request

    @allure.step('Смена планового времени согласования в заявке (с правами модератора)')
    def change_planned_time_approve(self, sync_token, request_id, time=1000):
        # Формируем тело запроса для изменения планового времени в заявке
        request_body = {
            'plannedTimeOfApproval': time,
            'syncToken': sync_token,
        }

        # Меняем плановое время
        request = self.put_requests_id_actions_change_planned_time(request_id, request_body,
                                                         params={'isModeratorMode': True})
        return request

    @allure.step('Смена планового времени уточнения в заявке (с правами модератора)')
    def change_planned_time_clarification(self, sync_token, request_id, time=1000):
        # Формируем тело запроса для изменения планового времени в заявке
        request_body = {
            'plannedTimeOfClarification': time,
            'syncToken': sync_token
        }

        # Меняем плановое время
        request = self.put_requests_id_actions_change_planned_time(request_id, request_body,
                                                         params={'isModeratorMode': True})
        return request

    @allure.step('Назначить исполнителя (модератором)')
    def set_contractor(self, sync_token, request_id, contractor_id):
        # Формируем тело запроса для назначения исполнителя
        request_body = {
            'contractorId': contractor_id,
            'syncToken': sync_token,
        }

        # Меняем исполнителя
        request = self.put_requests_id_actions_change_contractor(request_id, request_body,
                                                       params={'isModeratorMode': True})
        return request

    @allure.step('Сменить исполнителя (С правами модератора)')
    def change_contractor(self, sync_token, request_id, contractor):
        # Формируем тело запроса для смены исполнителя
        request_body = {
            'contractorId': self.manager.group_data.users[contractor]['user_id'],
            'syncToken': sync_token,
        }

        # Меняем исполнителя
        self.put_requests_id_actions_change_contractor(request_id, request_body,
                                                       params={'isModeratorMode': True})

    @allure.step('Сменить услугу в заявке (С правами модератора)')
    def change_service_in_request(self, sync_token, request_id, service_id):
        # Формируем тело запроса для смены услуги
        request_body = {
            'serviceId': service_id,
            'syncToken': sync_token,
        }

        # Меняем услугу
        request = self.put_requests_id_actions_change_gandiva_service(request_id, request_body,
                                                                      params={'isModeratorMode': True})

        return request

    @allure.step('Добавить обозревателя')
    def add_observer(self, user_id, sync_token, request_id, action='Add', params=None):
        # Формируем тело запроса для добавления обозревателя
        request_body = {
            'users': [{
                'id': user_id,
                'action': action,
            }],
            'syncToken': sync_token,
        }

        if params:
            # Добавляем обозревателя
            return self.put_requests_id_observers(request_id, request_body, params)
        else:
            return self.put_requests_id_observers(request_id, request_body)

    @allure.step('Смена трудоёмкости в заявке (с правами модератора)')
    def change_laboriousness(self, sync_token, request_id, time=1000):
        # Формируем тело запроса для изменения планового времени в заявке
        request_body = {
            'laboriousness': time,
            'syncToken': sync_token,
        }

        # Меняем плановое время
        request = self.put_requests_id_actions_change_planned_time(request_id, request_body,
                                                         params={'isModeratorMode': True})
        return request

    @allure.step('Добавить вложения в заявку')
    def add_attachments_in_request(self, request_id, file_id):
        # Формируем тело запроса
        request_body = {'fileids': file_id}

        # Добавляем вложения в заявку
        request = self.post_requests_id_add_attachments(request_id, request_body)

        return request

    @allure.step('Удалить вложения из заявки')
    def delete_attachments_from_request(self, request_id, attachment_id):

        # Формируем тело запроса
        request_body = {'attachmentIds': attachment_id}

        # Удаляем вложения
        request = self.post_requests_id_delete_attachments(request_id, request_body)

        return request

    @allure.step('Добавить описание к заявке')
    def add_descriptions_in_request(self, request_id, descriptions_mass={}):
        descriptions_body = {}

        # Собираем тело
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

    @allure.step('Добавить заявку в избранное')
    def add_request_in_favourites(self, request_id, sync_token):
        # Формируем тело запроса
        request_body = {'syncToken': sync_token}

        # Добавляем заявку в избранное
        request = self.post_requests_id_favourites(request_id, request_body)

        return request

    @allure.step('Добавить группу обозревателей')
    def add_observer_group(self, group_id, sync_token, request_id, action='Add', params=None):
        # Формируем тело запроса для добавления группы обозревателей
        request_body = {
            'groups': [{
                'id': group_id,
                'action': action,
            }],
            'syncToken': sync_token,
        }

        if params:
            # Добавляем обозревателей
            return self.put_requests_id_observers(request_id, request_body, params)
        else:
            return self.put_requests_id_observers(request_id, request_body)

    @allure.step('Эскалировать заявку')
    def escalate_request(self, request_id, sync_token):
        # Формируем тело запроса
        request_body = {'syncToken': sync_token}

        # Эскалируем заявку
        request = self.put_requests_id_actions_escalate(request_id, request_body)

        return request

    @allure.step('Получить Id групп обозревателей')
    def get_observer_groups_ids(self, request_observers_groups):
        observer_groups_ids = []
        for group in request_observers_groups:
            observer_groups_ids.append(group['id'])
        return observer_groups_ids

    @allure.step('Проверить наличие заявки в списке "Избранное"')
    def check_request_in_favourites(self, favourites_list, request_id):
        flag = False
        requests_ids = []
        for requests in favourites_list['items']:
            requests_ids.append(requests['id'])
            if request_id in requests_ids:
                flag = True
                break
        return flag

    @allure.step('Вернуть статус согласования согласующего по его id')
    def get_user_agreement_status_in_request(self, agreements, approver_id):
        for agreement in agreements:
            if agreement['approver']['id'] == approver_id:
                return agreement['status']

    @allure.step('Получить список id всех согласующих')
    def get_list_id_all_approvers(self, agreements):
        approvers_id_list = []
        for agreement in agreements:
            approvers_id_list.append(agreement['approver']['id'])
        return approvers_id_list
