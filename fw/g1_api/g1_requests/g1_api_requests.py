import allure

from fw.g1_api.g1_api_base import G1APIBase


class G1ApiRequests(G1APIBase):

    @allure.step('Заявки в системе с учетом фильтра, сортировки с постраничным выводом')
    def get_api_requests(self, params=None):
        """
        type={type}&
        page={page}&
        size={size}&
        sort={sort}&
        descending={descending}&
        status={status}&
        doNotSearchInArchive={doNotSearchInArchive}
        """
        return self.requests_GET(self.get_base_url() + 'api/Requests', params)

    @allure.step('Заявки с комментариями по списку идентификаторов, доступно только модератору')
    def post_requests_requests_by_id_list(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Requests/RequestsByIdList', body, params)

    @allure.step('Заявка с номером Id. GET api/Requests/{id}')
    def get_requests_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Requests/{id}', params)

    @allure.step('Список вложенных заявок. GET api/Requests/{id}/SubRequests')
    def get_requests_id_sub_requests(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Requests/{id}/SubRequests', params)

    @allure.step('Список зависимых заявок, в которые вложена заявка. GET api/Requests/{id}/DependentRequests')
    def get_requests_id_dependent_requests(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Requests/{id}/DependentRequests', params)

    @allure.step('Список зависимых задач, в которые вложена заявка. GET api/Requests/{id}/DependentTasks')
    def get_requests_id_dependent_tasks(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Requests/{id}/DependentTasks', params)

    @allure.step('Комментарии для заявки с номером Id в древовидной форме. GET api/Requests/{id}/Comments')
    def get_requests_id_comments(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Requests/{id}/Comments', params)

    @allure.step('Сохраненные фильтры текущего пользователя. GET api/Requests/UserFilters')
    def get_requests_user_filters(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Requests/UserFilters', params)

    @allure.step('Метод возвращает пользователей, входящих в группу ответственности, к которой принадлежит данная заявка.')
    def get_requests_id_request_responsibility_group_users(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Requests/{id}/RequestResponsibilityGroupUsers', params)

    @allure.step('Возвращает список исполнителей для данной заявки. GET api/Requests/{id}/GetContractorsList')
    def get_requests_id_get_contractors_list(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Requests/{id}/GetContractorsList', params)

    @allure.step('Фильтрация заявок с постраничным выводом и с учетом сортировки. POST api/Requests/Filter')
    def post_requests_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Requests/Filter', body, params)

    @allure.step('Кол-во заявок с учетом фильтра. POST api/Requests/FilterCount')
    def post_requests_filter_count(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Requests/FilterCount', body, params)

    @allure.step('Возвращает отфильтрованные по статусу на период времени заявки (метод доступен только модератору). POST api/Requests/FilterByStatusOnPeriod')
    def post_requests_filter_by_status_on_period(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Requests/FilterByStatusOnPeriod', body, params)

    @allure.step('Поиск заявок с постраничным выводом и с учетом сортировки. POST api/Requests/Search')
    def post_requests_search(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Requests/Search', body, params)

    @allure.step('Кол-во заявок с учетом строки поиска. POST api/Requests/SearchCount')
    def post_requests_search_count(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Requests/SearchCount', body, params)

    @allure.step('Создание новой заявки. POST api/Requests')
    def post_requests(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Requests', body, params)

    @allure.step('Пересчитывает модель новой заявки, с учётом уже выборанного норматива. POST api/Requests/Recalculated')
    def post_requests_recalculated(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Requests/Recalculated', body, params)

    @allure.step('Возвращает макет копии заявки. GET api/Requests/{id}/Copy?mask={mask}')
    def get_requests_id_copy_mask(self, id, mask, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Requests/{id}/Copy?mask={mask}', params)

    @allure.step('Добавляет комментарий к заявке с номером id. POST api/Requests/{id}/Comments')
    def post_requests_id_comments(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Requests/{id}/Comments', body, params)

    @allure.step('Добавляет вопрос-уточнение в заявке с номером id. POST api/Requests/{id}/ClarificationQuestion')
    def post_requests_id_clarification_question(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Requests/{id}/ClarificationQuestion', body, params)

    @allure.step('Добавляет ответ на комментарий типа "уточнение-вопрос". POST api/Requests/Comments/{id}/ClarificationAnswer')
    def post_requests_comments_id_clarification_answer(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Requests/Comments/{id}/ClarificationAnswer', body, params)

    @allure.step('Присоединяет текущего пользователя к комментарию типа "уточнение-вопрос". POST api/Requests/Comments/{id}/Join')
    def post_requests_comments_id_join(self, id, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Requests/Comments/{id}/Join', params)

    @allure.step('Присоединяет текущего пользователя к комментарию типа "уточнение-вопрос". PUT api/Requests/Comments/{id}/Join')
    def put_requests_comments_id_join(self, id, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Requests/Comments/{id}/Join', params)

    @allure.step('Отменяет уточнение. POST api/Requests/Comments/{id}/CancelClarification')
    def post_requests_comments_id_cancel_clarification(self, id, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Requests/Comments/{id}/CancelClarification', params)

    @allure.step('Добавляет заявку с номером id в избранное. POST api/Requests/{id}/Favourites')
    def post_requests_id_favorites(self, id, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Requests/{id}/Favourites', params)

    @allure.step('Добавляет новый пользовательский фильтр. POST api/Requests/UserFilter')
    def post_requests_user_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Requests/UserFilter', body, params)

    @allure.step('Редактирование заявки с номером id. PUT api/Requests/{id}')
    def put_requests_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Requests/{id}', body, params)

    @allure.step('Частичное обновление заявки с номером id. Обозреватели. PUT api/Requests/{id}/Observers')
    def put_requests_id_observers(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Requests/{id}/Observers', body, params)

    @allure.step('Частичное обновление заявки с номером id. Добавление согласующих. Если согласующий не принял решение и при обновлении он не был в списке '
                 'согласующих - такой согласующий удаляется.. PUT api/Requests/v2/{id}/Approvers')
    def put_requests_id_approvers(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Requests/v2/{id}/Approvers', body, params)

    @allure.step('Частичное изменение заявки, путь заявки (норматив + доп. поля + хэштеги). PUT api/Requests/{id}/Path')
    def put_requests_id_path(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Requests/{id}/Path', body, params)

    @allure.step('Частичное обновление заявки с номером id. Исполнитель. PUT api/Requests/{id}/Contractor')
    def put_requests_id_contractor(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Requests/{id}/Contractor', body, params)

    @allure.step('Частичное обновление заявки с номером id. Инициатор. PUT api/Requests/{id}/Initiator')
    def put_requests_id_initiator(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Requests/{id}/Initiator', body, params)

    @allure.step('Частичное обновление заявки с номером id. Вложения. PUT api/Requests/{id}/Attachments')
    def put_requests_id_attachments(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Requests/{id}/Attachments', body, params)

    @allure.step('Добавляет вложения к заявке. PATCH api/Requests/{id}/Attachments')
    def patch_requests_id_attachments(self, id, params=None):
        return self.requests_PATCH(self.get_base_url() + f'api/Requests/{id}/Attachments', params)

    @allure.step('Добавить вложенную заявку с номером SubRequestId к заявке с номером Id. PUT api/Requests/{id}/SubRequests/{sub_request_id}')
    def put_requests_id_subrequests_subrequests_id(self, id, sub_request_id, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Requests/{id}/SubRequests/{sub_request_id}', None, params=params)

    @allure.step('Частичное обновление заявки с номером id. Хэштеги. PUT api/Requests/{id}/Hashtags')
    def put_requests_id_hashtags(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Requests/{id}/Hashtags', body, params)

    @allure.step('Частичное обновление заявки с номером id. Регион. PUT api/Requests/{id}/Region')
    def put_requests_id_region(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Requests/{id}/Region', body, params)

    @allure.step('Действия с заявкой, изменение её статуса. Также, какое решение принять согласующему: согласовать, отклонить или другое - делается этим методом. '
                 'PUT api/Requests/{id}/Action')
    def put_requests_id_action(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Requests/{id}/Action', body, params)

    @allure.step('Частичное обновление задачи с номером id. Дата рассмотрения заявки. PUT api/Requests/{id}/RequiredStartDate')
    def put_requests_id_required_start_date(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Requests/{id}/RequiredStartDate', body, params)

    @allure.step('Прочитать все комментарии, адресованные текущему пользователю, внутри для заявки. PUT api/Requests/{id}/ReadAll')
    def put_requests_id_read_all(self, id, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Requests/{id}/ReadAll', params)

    @allure.step('Удаляет вложенную заявку с номером SubRequestId из заявки с номером Id. DELETE api/Requests/{id}/SubRequests/{subRequestId}')
    def delete_requests_id_subrequests__subrequests_id(self, id, subRequestId, params=None):
        return self.requests_DELETE(self.get_base_url() + f'api/Requests/{id}/SubRequests/{subRequestId}', None, params=params)

    @allure.step('Удаляет заявку с номером id из избранного. DELETE api/Requests/{id}/Favourites')
    def delete_requests_id_favourites(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'api/Requests/{id}/Favourites', params)
