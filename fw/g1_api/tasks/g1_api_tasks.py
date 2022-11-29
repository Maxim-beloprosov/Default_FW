import allure

from fw.g1_api.g1_api_base import G1APIBase


class G1ApiTasks(G1APIBase):

    @allure.step('Задачи в системе с учетом фильтра, сортировки с постраничным выводом. GET api/Tasks')
    def get_tasks(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Tasks', params)

    @allure.step('Задача с номером Id. GET api/Tasks/{id}')
    def get_tasks_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Tasks/{id}', params)

    @allure.step('Комментарии для задачи с номером Id в древовидной форме. GET api/Tasks/{id}/comments')
    def get_tasks_id_comments(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Tasks/{id}/comments', params)

    @allure.step('Список вложенных заявок. GET api/Tasks/{id}/SubRequests')
    def get_tasks_id_sub_requests(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Tasks/{id}/SubRequests', params)

    @allure.step('Список вложенных задач. GET api/Tasks/{id}/SubTasks')
    def get_tasks_id_sub_tasks(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Tasks/{id}/SubTasks', params)

    @allure.step('Список зависимых задач, в которые вложена задача. GET api/Tasks/{id}/DependentTasks')
    def get_tasks_id_dependent_tasks(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Tasks/{id}/DependentTasks', params)

    @allure.step('Осуществляет поиск сотрудников, которым можно делегировать задачу. GET api/Tasks/{id}/SearchAvailableContractors')
    def get_tasks_id_search_available_contractors(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Tasks/{id}/SearchAvailableContractors', params)

    @allure.step('Фильтрация задач с постраничным выводом и с учетом сортировки. POST api/Tasks/Filter')
    def post_tasks_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Tasks/Filter', body, params)

    @allure.step('Кол-во задач с учетом фильтра. POST api/Tasks/FilterCount')
    def post_tasks_filter_count(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Tasks/FilterCount', body, params)

    @allure.step('Поиск задач с постраничным выводом и с учетом сортировки. POST api/Tasks/Search')
    def post_tasks_search(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Tasks/Search', body, params)

    @allure.step('Кол-во задач с учетом строки поиска. POST api/Tasks/SearchCount')
    def post_tasks_search_count(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Tasks/SearchCount', body, params)

    @allure.step('Создание новой задачи. POST api/Tasks')
    def post_tasks(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Tasks', body, params)

    @allure.step('Создание списка(множества) новых задач. POST api/Tasks/v3/CreateMultipleTasks')
    def post_tasks_v3_create_multiple_tasks(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Tasks/v3/CreateMultipleTasks', body, params)

    @allure.step('Возвращает макет копии задачи. GET api/Tasks/{id}/Copy')
    def get_tasks_id_copy(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Tasks/{id}/Copy', params)

    @allure.step('Добавляет задачу с номером id в избранное. POST api/Tasks/{id}/Favourites')
    def post_tasks_id_favourites(self, id, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Tasks/{id}/Favourites', params)

    @allure.step('Добавляет заявку с номером requestId к задаче с номером Id. PUT api/Tasks/{id}/SubRequests/{request_id}')
    def put_tasks_id_sub_requests_request_id(self, id, request_id, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Tasks/{id}/SubRequests/{request_id}', None, params=params)

    @allure.step('Добавляет вложенную задачу с номером subTaskId к задаче с номером Id. PUT api/Tasks/{id}/SubTasks/{sub_task_id}')
    def put_tasks_id_sub_task_id(self, id, sub_task_id, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Tasks/{id}/SubTasks/{sub_task_id}', None, params=params)

    @allure.step('Добавляет комментарий к задаче с номером id. POST api/Tasks/{id}/Comments')
    def post_tasks_id_comments(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Tasks/{id}/Comments', body, params)

    @allure.step('Редактирование задачи с номером id. PUT api/Tasks/{id}')
    def put_tasks_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Tasks/{id}', body, params)

    @allure.step('Обозреватели.Частичное обновление задачи с номером id. PUT api/Tasks/{id}/Observers')
    def put_tasks_id_observers(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Tasks/{id}/Observers', body, params)

    @allure.step('Согласующие. Частичное обновление задачи с номером id. PUT api/Tasks/{id}/Approvers')
    def put_tasks_id_approvers(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Tasks/{id}/Approvers', body, params)

    @allure.step('Частичное обновление задачи с номером id. Вложения. PUT api/Tasks/{id}/Attachments')
    def put_tasks_id_attachments(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Tasks/{id}/Attachments', body, params)

    @allure.step('Добавляет вложения к задаче. PATCH api/Tasks/{id}/Attachments')
    def patch_tasks_id_attachments(self, id,params=None):
        return self.requests_PATCH(self.get_base_url() + f'api/Tasks/{id}/Attachments', params)

    @allure.step('Частичное обновление заявки с номером id. Хэштеги. PUT api/Tasks/{id}/Hashtags')
    def put_tasks_id_hashtags(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Tasks/{id}/Hashtags', body, params)

    @allure.step('Устанавливает исполнителя для задачи с номером id. PUT api/Tasks/{id}/Contractor')
    def put_tasks_id_contractor(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Tasks/{id}/Contractor', body, params)

    @allure.step('Частичное обновление заявки с номером id. Инициатор. PUT api/Tasks/{id}/Initiator')
    def put_tasks_id_initiator(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Tasks/{id}/Initiator', body, params)

    @allure.step('Частичное обновление задачи с номером id. Список дел. PUT api/Tasks/{id}/TodoList')
    def put_tasks_id_todo_list(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Tasks/{id}/TodoList', body, params)

    @allure.step('Частичное обновление задачи с номером id. Приоритет. PUT api/Tasks/{id}/Priority')
    def put_tasks_id_priority(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Tasks/{id}/Priority', body, params)

    @allure.step('Частичное обновление задачи с номером id. Даты начала и окончания задачи. PUT api/Tasks/{id}/RequiredDate')
    def put_tasks_id_required_date(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Tasks/{id}/RequiredDate', body, params)

    @allure.step('Редактирование темы задачи PUT api/Tasks/{id}/Subject')
    def put_tasks_id_subject(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Tasks/{id}/Subject', body, params)

    @allure.step('Редактирование Описания задачи PUT api/Tasks/{id}/Description')
    def put_tasks_id_description(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Tasks/{id}/Description', body, params)

    @allure.step('Частичное обновление с номером id. Действия с задачей PUT api/Tasks/{id}/Action')
    def put_tasks_id_action(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Tasks/{id}/Action', body, params)

    @allure.step('Прочитать все комментарии задачи, адресованные текущему пользователю. PUT api/Tasks/{id}/ReadAll')
    def put_tasks_id_read_all(self, id, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Tasks/{id}/ReadAll', params)

    @allure.step('Удаляет задачу с номером id из избранного. DELETE api/Tasks/{id}/Favourites')
    def delete_tasks_id_favourites(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'api/Tasks/{id}/Favourites', params)

    @allure.step('Удаляет заявку с номером requestId из задачи с номером Id DELETE api/Tasks/{id}/SubRequests/{requestId}')
    def delete_tasks_id_sub_requests_request_id(self, id, requestId, params=None):
        return self.requests_DELETE(self.get_base_url() + f'api/Tasks/{id}/SubRequests/{requestId}', None, params)

    @allure.step('Удаляет вложенную задачу с номером subTaskId из задачи с номером Id. DELETE api/Tasks/{id}/SubTasks/{subTaskId}')
    def delete_tasks_id_sub_tasks_sub_task_id(self, id, subTaskId, params=None):
        return self.requests_DELETE(self.get_base_url() + f'api/Tasks/{id}/SubTasks/{subTaskId}', None, params)
