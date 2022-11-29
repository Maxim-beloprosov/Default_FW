import allure

from fw.api.api_base import APIBase


class ApiRequests(APIBase):

    @allure.step('Список заявок. POST /api/Requests/Filter')
    def post_requests_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Requests/Filter', body, params)

    @allure.step('Получение заявки по ключу. GET /api/Requests/{id}')
    def get_requests_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Requests/{id}', params)

    @allure.step('Обновление заявки. PUT /api/Requests/{id}')
    def put_requests_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}', body, params)

    @allure.step('Получение заявки по номеру. GET /api/Requests/DocumentNumber/{number}')
    def get_requests_document_number(self, number, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Requests/DocumentNumber/{number}', params)

    @allure.step('Создание заявки. POST /api/Requests')
    def post_requests(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Requests', body, params)

    @allure.step('Создание заявки по телефону. POST /api/Requests/Phone')
    def post_requests_phone(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Requests/Phone', body, params)

    @allure.step('Получение текущей группы ответственности по заявке. GET /api/Requests/{id}/ResponsibilityGroup')
    def get_requests_id_responsibility_group(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Requests/{id}/ResponsibilityGroup', params)

    @allure.step('Обновление планового времени в заявке. PUT /api/Requests/{id}/Actions/ChangePlannedTime')
    def put_requests_id_actions_change_planned_time(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/ChangePlannedTime', body, params)

    @allure.step('Обновление инициатора. PUT /api/Requests/{id}/Actions/ChangeInitiator')
    def put_requests_id_actions_change_initiator(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/ChangeInitiator', body, params)

    @allure.step('Обновление услуги в заявке. PUT /api/Requests/{id}/Actions/ChangeGandivaService')
    def put_requests_id_actions_change_gandiva_service(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/ChangeGandivaService', body, params)

    @allure.step('Назначить на себя. PUT /api/Requests/{id}/Actions/AssignToMe')
    def put_requests_id_actions_assign_to_me(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/AssignToMe', body, params)

    @allure.step('Смена исполнителя. PUT /api/Requests/{id}/Actions/ChangeContractor')
    def put_requests_id_actions_change_contractor(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/ChangeContractor', body, params)

    @allure.step('Удаление исполнителя. PUT /api/Requests/{id}/Actions/ClearContractor')
    def put_requests_id_actions_clear_contractor(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/ClearContractor', body, params)

    @allure.step('Согласовать. PUT /api/Requests/{id}/Actions/Approve')
    def put_requests_id_actions_approve(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/Approve', body, params)

    @allure.step('Отклонить. PUT /api/Requests/{id}/Actions/Reject')
    def put_requests_id_actions_reject(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/Reject', body, params)

    @allure.step('Апеллировать. PUT /api/Requests/{id}/Actions/Appeal')
    def put_requests_id_actions_appeal(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/Appeal', body, params)

    @allure.step('Делегировать согласование. PUT /api/Requests/{id}/Actions/DelegateAgreement')
    def put_requests_id_actions_delegate_agreement(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/DelegateAgreement', body, params)

    @allure.step('Эскалирование заявки. PUT /api/Requests/{id}/Actions/Escalate')
    def put_requests_id_actions_escalate(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/Escalate', body, params)

    @allure.step('Перевод заявки на проверку. PUT /api/Requests/{id}/Actions/Resolve')
    def put_requests_id_actions_resolve(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/Resolve', body, params)

    @allure.step('Перевод заявки из ожидания в работу. PUT /api/Requests/{id}/Actions/ToWork')
    def put_requests_id_actions_to_work(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/ToWork', body, params)

    @allure.step('Возвращение заявки из проверки в работу. PUT /api/Requests/{id}/Actions/BackToWork')
    def put_requests_id_actions_back_to_work(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/BackToWork', body, params)

    @allure.step('Возврат на доработку. PUT /api/Requests/{id}/Actions/ReturnToRework')
    def put_requests_id_actions_return_to_work(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/ReturnToRework', body, params)

    @allure.step('Отмена заявки. PUT /api/Requests/{id}/Actions/Cancel')
    def put_requests_id_actions_cancel(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/Cancel', body, params)

    @allure.step('Оценка и закрытие заявки. PUT /api/Requests/{id}/Actions/Close')
    def put_requests_id_actions_close(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/Close', body, params)

    @allure.step('Задать вопрос-уточнение инициатору. PUT /api/Requests/{id}/Actions/Clarifications/AskInitiator')
    def put_requests_id_actions_clarifications_ask_initiator(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/Clarifications/AskInitiator', body, params)

    @allure.step('Задать вопрос-уточнение исполнителю. PUT /api/Requests/{id}/Actions/Clarifications/AskContractor')
    def put_requests_id_actions_clarifications_ask_contractor(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/Clarifications/AskContractor', body, params)

    @allure.step('Инициатор отвечает на вопрос-уточнение. PUT /api/Requests/{id}/Actions/Clarifications/InitiatorAnswer')
    def put_requests_id_actions_clarifications_initiator_answer(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/Clarifications/InitiatorAnswer', body, params)

    @allure.step('Исполнитель отвечает на вопрос-уточнение. PUT /api/Requests/{id}/Actions/Clarifications/ContractorAnswer')
    def put_requests_id_actions_clarifications_contractor_answer(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/Clarifications/ContractorAnswer', body, params)

    @allure.step('Присоединиться к уточнению. PUT /api/Requests/{id}/Actions/Clarifications/Join')
    def put_requests_id_actions_clarifications_join(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/Clarifications/Join', body, params)

    @allure.step('Отменить уточнение. PUT /api/Requests/{id}/Actions/Clarifications/Join')
    def put_requests_id_actions_clarifications_cancel(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Actions/Clarifications/Cancel', body, params)

    @allure.step('Список доступных пользователей для согласования. POST /api/Requests/Agreements/Filter')
    def post_requests_agreements_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Requests/Agreements/Filter', body, params)

    @allure.step('Добавить согласование. POST /api/Requests/{id}/Agreements')
    def post_requests_id_agreements(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Requests/{id}/Agreements', body, params)

    @allure.step('Список уровней согласования (история согласований). GET /api/Requests/{id}/Agreements')
    def get_requests_id_agreements(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Requests/{id}/Agreements', params)

    @allure.step('Удалить согласование. DELETE /api/Requests/{id}/Agreements/{agreementId}')
    def delete_requests_id_agreements_agreement_id(self, id, agreementId, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/Requests/{id}/Agreements/{agreementId}', params)

    @allure.step('Список доступных обозревателей-пользователей и групп. POST /api/Requests/Observers/Filter')
    def post_requests_id_observers_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Requests/Observers/Filter', body, params)

    @allure.step('Обновление обозревателей. PUT /api/Requests/{id}/Observers')
    def put_requests_id_observers(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Observers', body, params)

    @allure.step('Сохранение заявок в избранных. POST /api/Requests/{id}/Favourites')
    def post_requests_id_favourites(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Requests/{id}/Favourites', body, params)

    @allure.step('Удаление заявок из избранных. DELETE /api/Requests/{id}/Favourites')
    def delete_requests_id_favourites(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/Requests/{id}/Favourites', params)

    @allure.step('Добавить вложения. POST /api/Requests/{id}/AddAttachments')
    def post_requests_id_add_attachments(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Requests/{id}/AddAttachments', body, params)

    @allure.step('Удалить вложения. POST /api/Requests/{id}/DeleteAttachments')
    def post_requests_id_delete_attachments(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Requests/{id}/DeleteAttachments', body, params)

    @allure.step('Получение файла из заявки по идентификатору заявки и идентификатору файла. GET /api/Requests/{id}/Files/{fileId}')
    def get_requests_id_files_file_id(self, id, fileId, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Requests/{id}/Files/{fileId}', params)

    @allure.step('Получение миниатюры из заявки по идентификатору заявки и идентификатору файла. GET /api/Requests/{id}/Files/{fileId}/Miniature')
    def get_requests_id_files_file_id_miniature(self, id, fileId, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Requests/{id}/Files/{fileId}/Miniature', params)

    @allure.step('Получение информации по файлу из заявки по идентификатору заявки и идентификатору файла. GET /api/Requests/{id}/Files/{fileId}/Info')
    def get_requests_id_files_file_id_info(self, id, fileId, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Requests/{id}/Files/{fileId}/Info', params)

    @allure.step('Возвращает список участников тикета. GET /api/Requests/{id}/Members')
    def get_requests_id_members(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Requests/{id}/Members', params)

    @allure.step('Добавление нового блока в описание тикета. POST /api/Requests/{id}/Description')
    def post_requests_id_description(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Requests/{id}/Description', body, params)

    @allure.step('Редактирование блока описания тикета. PUT /api/Requests/{id}/Description/{descId}')
    def put_requests_id_description_desc_id(self, id, descId, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Requests/{id}/Description/{descId}', body, params)

    @allure.step('Получить список доступных действий над тикетом. GET /api/Requests/{id}/Actions')
    def get_requests_id_actions(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Requests/{id}/Actions', params)