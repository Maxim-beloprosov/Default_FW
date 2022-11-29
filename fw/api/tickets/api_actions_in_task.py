import allure

from fw.api.tickets.api_tasks import ApiTasks


class ActionsInTask(ApiTasks):

    @allure.title('Согласовать задачу')
    def approve_task(self, synctoken, task_id):

        # Формируем тело запроса для согласования задачи
        task_body = {
            'syncToken': synctoken
        }

        # Согласуем задачу
        task = self.put_tasks_id_actions_approve(task_id, task_body)

        return task

    @allure.title('Отклонить задачу')
    def reject_task(self, synctoken, task_id, text='AutomationApiTest Reject'):

        # Формируем тело запроса для отклонения
        task_body = {
            'text': text,
            'syncToken': synctoken,
        }

        # Отклоняем задачу
        task = self.put_tasks_id_actions_reject(task_id, task_body)

        return task

    @allure.title('Задать вопрос-уточнение инициатору')
    def clarification_ask_to_initiator_in_task(self, synctoken, task_id, type='Text', text='AutomationApiTest Question'):

        # Формируем тело запроса для вопроса-уточнения
        task_body = {
            'contentParts': [
                {
                    'type': type,
                    'text': text,
                }
            ],
            'syncToken': synctoken,
        }

        # Задаем вопрос-уточнение
        task = self.put_tasks_id_actions_clarifications_ask_initiator(task_id, task_body)

        return task

    @allure.title('Задать вопрос-уточнение исполнителю')
    def clarification_ask_to_contractor_in_task(self, synctoken, task_id, type='Text', text='AutomationApiTest Question'):

        # Формируем тело запроса для вопроса-уточнения
        task_body = {
            'contentParts': [
                {
                    'type': type,
                    'text': text,
                }
            ],
            'syncToken': synctoken,
        }

        # Задаем вопрос-уточнение
        task = self.put_tasks_id_actions_clarifications_ask_contractor(task_id, task_body)

        return task

    @allure.title('Ответ на вопрос-уточнение исполнителю')
    def clarification_contractor_answer_in_task(self, clarification_id, synctoken, task_id, type='Text', text='AutomationApiTest Answer'):

        # Формируем тело запроса для ответа на вопрос-уточнение
        task_body = {
            'clarificationId': clarification_id,
            'contentParts': [
                {
                    'type': type,
                    'text': text,
                }
            ],
            'syncToken': synctoken,
        }

        # Отвечаем на вопрос-уточнение инициатора
        task = self.put_tasks_id_actions_clarifications_contractor_answer(task_id, task_body)

        return task

    @allure.title('Отменить вопрос-уточнение инициатору')
    def cancel_initiator_clarification_in_task(self, clarification_id, synctoken, task_id):

        # Формируем тело запроса для отмены вопроса-уточнения
        task_body = {
            'clarificationId': clarification_id,
            'syncToken': synctoken,
        }

        # Отменяем вопрос уточнение
        task = self.put_tasks_id_actions_clarifications_cancel(task_id, task_body)

        return task

    @allure.title('Ответ на вопрос-уточнение инициатору')
    def clarification_initiator_answer_in_task(self, clarification_id, synctoken, task_id, type='Text', text='AutomationApiTest Answer'):

        # Формируем тело запроса для ответа на вопрос-уточнение
        task_body = {
            'clarificationId': clarification_id,
            'contentParts': [
                {
                    'type': type,
                    'text': text,
                }
            ],
            'syncToken': synctoken,
        }

        # Отвечаем на вопрос-уточнение инициатора
        task = self.put_tasks_id_actions_clarifications_initiator_answer(task_id, task_body)

        return task

    @allure.title('Апеллировать задачу')
    def appeal_task(self, synctoken, task_id, text='AutomationApiTest Appeal'):

        # Формируем тело запроса для апелляции
        task_body = {
            'text': text,
            'syncToken': synctoken,
        }

        # Производим апелляцию
        task = self.put_tasks_id_actions_appeal(task_id, task_body)

        return task

    @allure.title('Отправить задачу в проверку')
    def resolve_task(self, synctoken, task_id):

        # Формируем тело запроса для отправки задачи на проверку
        task_body = {
            "syncToken": synctoken,
        }

        # Отправляем задачу на проверку
        task = self.put_tasks_id_actions_resolve(task_id, task_body)

        return task

    @allure.title('Вернуть задачу на доработку')
    def return_task_to_rework(self, synctoken, task_id, text='AutomationApiTest Resolved to Work'):

        # Формируем тело запроса для отправки задачи на доработку
        task_body = {
            'text': text,
            'syncToken': synctoken,
        }

        # Отправляем задачу на доработку
        task = self.put_tasks_id_actions_return_to_rework(task_id, task_body)

        return task

    @allure.title('Закрыть задачу')
    def close_task(self, rating, synctoken, task_id, text='AutomationApiTest Closed'):

        if rating == 5:
            # Формируем тело запроса для закрытия задачи
            task_body = {
                'rating': rating,
                'syncToken': synctoken,
            }
        else:
            # Формируем тело запроса для закрытия задачи
            task_body = {
                'rating': rating,
                'text': text,
                'syncToken': synctoken,
            }

        # Закрываем задачу
        task = self.put_tasks_id_actions_close(task_id, task_body)

        return task

    @allure.title('Добавить согласование')
    def add_agreements_in_task(self, approver_id, synctoken, task_id, params=None):

        # Формируем тело запроса для добавления согласующего
        task_body = {
            'approverId': approver_id,
            'syncToken': synctoken,
        }

        # Добавляем согласующего в задачу
        task = self.post_tasks_id_agreements(task_id, task_body, params)

        return task

    @allure.title('Добавить задачу в избранное')
    def add_task_in_favourites(self, task):

        # Формируем тело запроса для добавления задачи в избранное
        task_body = {
            'syncToken': task['syncToken'],
        }

        # Добавляем задачу в избранное
        task = self.post_tasks_id_favourites(task['id'], task_body)

        return task

    @allure.title('Обновление задачи')
    def update_task(self, sync_token, task_id, task_mass={}, params=None):

        json_task = {}
        # -------subject---------------------
        if "subject" in task_mass:
            json_task["subject"] = task_mass["subject"]
        else:
            json_task["subject"] = "AutomationApiTestTask " + self.manager.time.get_date_time_Y_m_d_H_M_S()

        # -------initiatorId---------------------
        if "initiatorId" in task_mass:
            json_task["initiatorId"] = task_mass["initiatorId"]
        else:
            json_task["initiatorId"] = self.manager.group_data.users['test_user09']['user_id']

        # -------beginDate---------------------
        if "beginDate" in task_mass:
            if isinstance(task_mass["beginDate"], str):
                json_task["beginDate"] = task_mass["beginDate"]
            else:
                json_task["beginDate"] = self.manager.time.get_date_increased_x_days_json(task_mass["beginDate"])

        # -------endDate-----------------------
        if "endDate" in task_mass:
            if isinstance(task_mass["endDate"], str):
                json_task["endDate"] = task_mass["endDate"]
            else:
                json_task["endDate"] = self.manager.time.get_date_increased_x_days_json(task_mass["endDate"])

        # -------laboriousness-------------------
        if "laboriousness" in task_mass: json_task["laboriousness"] = task_mass["laboriousness"]

        # -------customFieldCollection------------
        if "customFieldCollection" in task_mass: json_task["customFieldCollection"] = task_mass[
            "customFieldCollection"]

        # -------syncToken---------------------
        json_task["syncToken"] = sync_token

        updated_task = self.manager.api_tasks.put_tasks_id(task_id, json_task, params)

        return updated_task

    @allure.title('Отмена задачи')
    def cancel_task(self, sync_token, task_id, text='AutomationApiTest Cancel'):

        cancel_body = {
            "text": text,
            "syncToken": sync_token
        }

        task = self.put_tasks_id_cancel(task_id, cancel_body)

        return task

    @allure.title('Добавить предшественника')
    def add_previous_to_task(self, task_one_id, task_which_added_to_task_one_id):

        # Формируем тело для добавления предшественника
        add_previous_task = {
            "previousId": task_which_added_to_task_one_id
        }

        # Добавление задачи предшественника
        task = self.manager.api_nodes.post_add_previous_to_task(task_one_id, add_previous_task)

        return task

    @allure.title('Делегировать согласование')
    def delegate_agreement_in_task(self, sync_token, task_id, new_approver):

        delegate_task = {
            "newApproverId": self.manager.group_data.users[new_approver]['user_id'],
            "syncToken": sync_token
        }

        # Делегирование задачи
        delegate_agreement_task = self.manager.api_tasks.put_tasks_id_actions_delegate_agreement(task_id, delegate_task)

        return delegate_agreement_task

    @allure.title('Добавить дополнительное описание к задаче')
    def add_additional_descriptions_in_task(self, task_id, descriptions_mass={}):
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
        # Добавляем описание к задаче
        task = self.post_tasks_id_description(task_id, descriptions_body)

        return task

    @allure.title('Добавить вложения в задачу')
    def add_attachments_in_task(self, task_id, file_id):
        task_body = {'fileIds': file_id}

        task = self.post_tasks_id_add_attachments(task_id, task_body)

        return task

    @allure.title('Удалить вложения из задачи')
    def delete_attachments_from_task(self, task_id, attachment_id):
        task_body = {'attachmentIds': attachment_id}

        task = self.post_tasks_id_delete_attachments(task_id, task_body)

        return task

    @allure.title('Изменить запланированное время задачи')
    def change_planned_time_in_task(self, task_id, task_body, sync_token, params=None):

        task_body2 = {}

        # --------- plannedTimeOfClarification ----------
        if 'plannedTimeOfClarification' in task_body:
            task_body2['plannedTimeOfClarification'] = task_body['plannedTimeOfClarification']

        # --------- plannedTimeOfFeedback ----------
        if 'plannedTimeOfFeedback' in task_body:
            task_body2['plannedTimeOfFeedback'] = task_body['plannedTimeOfFeedback']

        # --------- plannedTimeOfApproval ----------
        if 'plannedTimeOfApproval' in task_body:
            task_body2['plannedTimeOfApproval'] = task_body['plannedTimeOfApproval']

        # ------ syncToken --------
        task_body2['syncToken'] = sync_token

        task = self.put_tasks_id_actions_change_planned_time(task_id, task_body2, params)

        return task

    @allure.title('Сменить исполнителя в задаче')
    def change_contractor_in_task(self, task_synctoken, task_id, contractor_id, params=None):
        task_body = {
            'syncToken': task_synctoken,
            'contractorId': contractor_id
        }

        task = self.put_tasks_id_actions_change_contractor(task_id, task_body, params)

        return task

    @allure.title('Обновление обозревателей')
    def refresh_observer_in_task(self, task_synctoken, task_id, user_id, action='Add', params=None):
        task_body = {
            'users': [
                {
                    'id': user_id,
                    'action': action
                }
            ],
            'syncToken': task_synctoken
        }

        task = self.put_tasks_id_observers(task_id, task_body, params)

        return task

    @allure.title("Проверка на равенство параметров в счётчиках по фактическому времени")
    def checking_the_equality_params_in_counters(self, task_counters, search_param, params):

        """
           task_counter - json [counters] из задачи
           search_param - Параметр по которому осуществлять поиск в task_counter. Например, 'type' или 'status'
           params - Параметры которые нужно проверять в task_counters. Передавать ввиде {'Executor': 1} или {'Executor': 10, 'ContractorExecution': 1}
           Если цикл не нашёл элементов [counters] или search_param в task_counter - будет ошибка None.
        """

        for items in task_counters:
            if items[search_param] in params:
                if items['adjustedTotalMinutes'] != params[items['type']]:
                    return False
        return True


