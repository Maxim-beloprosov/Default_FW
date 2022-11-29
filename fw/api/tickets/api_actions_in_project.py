import allure

from fw.api.tickets.api_projects import ApiProjects


class ActionsInProject(ApiProjects):


    @allure.step('Добавляем дополнительное описание')
    def add_additional_description(self, project_id, text_additional_description):
        # Формируем тело запроса для изменения дополнительного описания
        task_body = {
            "contentParts":
                [
                    {
                        "type": "Text",
                        "text": text_additional_description
                    }
                ]
        }

        # Изменяем дополнительное описание
        project = self.post_projects_id_description(project_id, task_body)

        return project

    @allure.step('Изменить дополнительное описание')
    def edit_additional_description(self, sync_token, project_id, desc_id, text_additional_description):
        # Формируем тело запроса для изменения дополнительного описания
        task_body = {
            'syncToken': sync_token,
            "contentParts": {
                "type": "Text",
                "text": text_additional_description
            }
        }

        # Изменяем дополнительное описание
        project = self.put_projects_id_description_desc_id(project_id, desc_id, task_body)

        return project

    @allure.title('Отправить проект в проверку')
    def send_project_to_resolved(self, sync_token, project_id):

        # Формируем тело запроса для перевода проекта в проверку
        request_body = {
            "syncToken": sync_token
        }

        # Переводим проект в проверку
        project = self.manager.api_projects.put_projects_id_actions_resolve(project_id, request_body)
        return project


    @allure.title('Согласовать проект')
    def approve_project(self, sync_token, project_id):

        # Формирование тела запроса для согласования
        request_body = {
            'syncToken': sync_token
        }

        # Согласуем проект
        project = self.put_projects_id_actions_approve(project_id, request_body)

        return project


    @allure.title('Отклонить проект')
    def reject_project(self, sync_token, project_id):

        # Подготовка данных для отклонения заявки
        reason = "TestReasonRejected AutomationApiTests" + self.manager.time.get_date_time_Y_m_d_H_M_S()

        # Формируем тело запроса для принятии отрицательного решения по согласованию
        request_body = {
            "syncToken": sync_token,
            'text': reason
        }

        # Принимаем отрицательное решение согласующим
        project = self.manager.api_projects.put_projects_id_actions_reject(project_id, request_body)
        return project


    @allure.title('Обновление обозревателя в проекте - добавление/удаление')
    def upd_observer_in_project(self, user_id, sync_token, project_id, action='Add'):

        # Подготовка тела запроса
            project_body = {
                'users': [{
                    'id': user_id,
                    'action': action,
                }],
                'syncToken': sync_token,
            }
            projects_observer = self.put_projects_id_observers(project_id, project_body)

            return projects_observer

    @allure.title('Получение списка согласующих из проекта')
    def get_all_approvers_in_project(self, project_agreements):

        # Создание отдельной переменной для получения id всех согласующих из проекта
        approvers_list = []

        # Цикл для получения id согласующих из проекта
        for counter in range(len(project_agreements)):
           approvers_list.append(project_agreements[counter]['approver']['id'])

        return approvers_list

    @allure.title('Полчуение списка обозревателей из проекта')
    def get_all_observers_in_project(self, project_observers):

        # Инициализация массива(списка) для получения id всех обозревателей из проекта
        observers_list = []

        # Цикл для получения id обозревателей из проекта
        for counter in range(len(project_observers)):
            observers_list.append(project_observers[counter]['id'])

        return observers_list

    @allure.title('Добавление согласования')
    def add_agreement_in_project(self, sync_token, project_id, user_id):

        # Формирование тела запроса
        project_body = {
            'approverId': user_id,
            'syncToken': sync_token
        }

        project = self.post_projects_id_agreements(project_id, project_body)

        return project











