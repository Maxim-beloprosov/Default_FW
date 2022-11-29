import allure

from fw.g1_api.tasks.g1_api_tasks import G1ApiTasks


class G1ActionsInTask(G1ApiTasks):

    @allure.step('Добавить согласующего в задачу')
    def g1_add_approver_in_task(self, task_id, approvers_id, last_modified_date):

        body = {
            "Approvers": [],
            "LastModifiedDate": last_modified_date
        }

        for id in approvers_id:
            body['Approvers'].append({'Id': id})

        task = self.put_tasks_id_approvers(task_id, body)

        return task

    @allure.step('Отправить задачу на проверку')
    def g1_resolve_task(self, task_id, last_modified_date):

        body = {
            "LastModifiedDate": last_modified_date,
            "BidAction": self.manager.group_data.g1_tickets_actions['RUS']['Отправить на проверку']
        }

        task = self.put_tasks_id_action(task_id, body)

        return task

    @allure.step('Изменить дату начала задачи')
    def g1_change_task_start_date(self, task_id, last_modified_date, begin_date):

        body = {
            "LastModifiedDate": last_modified_date,
            "StartDate": begin_date
        }

        task = self.put_tasks_id_required_date(task_id, body)

        return task

    @allure.step('Согласовать задачу')
    def g1_approve_task(self, task_id, last_modified_date):

        body = {
            "LastModifiedDate": last_modified_date,
            "BidAction": self.manager.group_data.g1_tickets_actions['RUS']['Согласовать']
        }

        task = self.put_tasks_id_action(task_id, body)

        return task

    @allure.step('Отклонить задачу')
    def g1_reject_task(self, task_id, last_modified_date):

        body = {
            "LastModifiedDate": last_modified_date,
            "BidAction": self.manager.group_data.g1_tickets_actions['RUS']['Отклонить']
        }

        task = self.put_tasks_id_action(task_id, body)

        return task

    @allure.step('Вернуть на доработку')
    def g1_back_task_to_work(self, task_id, last_modified_date):
        body = {
            "LastModifiedDate": last_modified_date,
            "BidAction": self.manager.group_data.g1_tickets_actions['RUS']['Вернуть на доработку'],
            "Description": "TestApi"
        }

        task = self.put_tasks_id_action(task_id, body)

        return task

    @allure.step('Оценить и закрыть')
    def g1_rate_and_close_task(self, task_id, last_modified_date, rating):
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
                "Description": "TestApi"
            }
        task = self.put_tasks_id_action(task_id, body)

        return task

    @allure.step('Отменить задачу')
    def g1_cancel_task(self, task_id, last_modified_date):
        body = {
            "LastModifiedDate": last_modified_date,
            "BidAction": self.manager.group_data.g1_tickets_actions['RUS']['Отменить заявку'],
        }

        task = self.put_tasks_id_action(task_id, body)

        return task

    @allure.step('Редактировать заголовок задачи')
    def g1_edit_subject_in_task(self, task_id, last_modified_date, text):
        body = {
            'LastModifiedDate': last_modified_date,
            'Subject': text,
        }

        task = self.put_tasks_id_subject(task_id, body)

        return task

    @allure.step('Изменить дату окончания задачи')
    def g1_change_end_date_in_task(self, task_id, last_modified_date, end_date):
        body = {
            'LastModifiedDate': last_modified_date,
            'EndDate': end_date
        }

        task = self.put_tasks_id_required_date(task_id, body)

        return task

    @allure.step('Изменить описание в задаче')
    def g1_edit_description_in_task(self, task_id, last_modified_date, description):
        body = {
            'LastModifiedDate': last_modified_date,
            'Description': description
        }

        task = self.put_tasks_id_description(task_id, body)

        return task

    @allure.step('Изменить хэштеги в задаче')
    def g1_edit_hashtags_in_task(self, task_id, last_modified_date, hashtags):
        """Хэштеги отдавать в виде списка"""
        body = {
            'LastModifiedDate': last_modified_date,
            'HashTags': hashtags
        }

        task = self.put_tasks_id_hashtags(task_id, body)

        return task

    @allure.step('Изменить исполнителя в задаче')
    def g1_change_contractor_in_task(self, task_id, last_modified_date, contractor_id):
        body = {
            'LastModifiedDate': last_modified_date,
            'Contractor': {'Id': contractor_id}
        }

        task = self.put_tasks_id_contractor(task_id, body)

        return task

    @allure.step('Добавить комментарий к задаче')
    def g1_add_comment_in_task(self, task_id, text, addressees, parent_comment_id=None):
        body = {
            'ParentCommentId': parent_comment_id,
            'Text': text,
            'Addressees': addressees
        }

        comment = self.post_tasks_id_comments(task_id, body)

        return comment

    @allure.step('Список Id всех адресатов комментария')
    def g1_list_all_addreesses_comment_in_task(self, addressees):
        adressees_id = []
        for i in addressees:
            adressees_id.append(i['User']['Id'])
        return adressees_id

    @allure.step('Добавление обозревателей в залдачу')
    def g1_add_observers_in_task(self, task_id, last_modified_date, observers_id):
        body = {
            'LastModifiedDate': last_modified_date
        }
        if type(observers_id) == int:
            body['Observers'] = [{'Id': observers_id}]
        else:
            body['Observers'] = []
            for observer in observers_id:
                body['Observers'].append({'Id': observer})

        task = self.put_tasks_id_observers(task_id, body)

        return task

    @allure.step('Список Id всех обозревателей задачи')
    def g1_list_all_observers_in_task(self, observers):
        observers_id = []
        for i in observers:
            observers_id.append((i['Id']))
        return observers_id

    @allure.step('Добавление вложенной заявки к задаче')
    def g1_add_subrequest_in_task(self, task_id, request_id, last_modified_date):
        params = {'lastModifiedDate': last_modified_date}
        task = self.put_tasks_id_sub_requests_request_id(task_id, request_id, params=params)
        return task

    @allure.step('Добавление вложенной задачи к задаче')
    def g1_add_subtask_in_task(self, task_id, sub_task_id, last_modified_date):
        params = {'lastModifiedDate': last_modified_date}
        task = self.put_tasks_id_sub_task_id(task_id, sub_task_id, params=params)
        return task

    @allure.step('Получить статус согласующего в задаче')
    def g1_get_approver_status_in_task(self, task_approvers, approver_login):
        for approver in task_approvers:
            if approver['Login'] == approver_login:
                return approver['Status']
