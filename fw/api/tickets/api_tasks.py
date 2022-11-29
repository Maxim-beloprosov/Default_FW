import allure

from fw.api.api_base import APIBase


class ApiTasks(APIBase):

    @allure.step('Список задач. POST /api/Tasks/Filter')
    def post_tasks_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Tasks/Filter', body, params)

    @allure.step('Получение задачи по ключу. GET /api/Tasks/{id}')
    def get_tasks_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Tasks/{id}', params)

    @allure.step('Обновление задачи. PUT /api/Tasks/{id}')
    def put_tasks_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}', body, params)

    @allure.step('Получение задачи по номеру. GET /api/Tasks/DocumentNumber/{number}')
    def get_tasks_document_number(self, number, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Tasks/DocumentNumber/{number}', params)

    @allure.step('Создание задачи. POST /api/Tasks')
    def post_tasks(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Tasks', body, params)

    @allure.step('Получение файла из задачи по идентификатору задачи и идентификатору файла. GET /api/Tasks/{id}/Files/{fileId}')
    def get_tasks_id_files_file_id(self, id, fileId, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Tasks/{id}/Files/{fileId}', params)

    @allure.step('Получение миниатюры из задачи по идентификатору задачи и идентификатору файла. GET /api/Tasks/{id}/Files/{fileId}/Miniature')
    def get_tasks_id_files_file_id_miniature(self, id, fileId, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Tasks/{id}/Files/{fileId}/Miniature', params)

    @allure.step('Получение информации по файлу из задачи по идентификатору задачи и идентификатору файла. GET /api/Tasks/{id}/Files/{fileId}/Info')
    def get_tasks_id_files_file_id_info(self, id, fileId, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Tasks/{id}/Files/{fileId}/Info', params)

    @allure.step('Изменить запланированное время задачи. PUT /api/Tasks/{id}/Actions/ChangePlannedTime')
    def put_tasks_id_actions_change_planned_time(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/ChangePlannedTime', body, params)

    @allure.step('Назначить на себя. PUT /api/Tasks/{id}/Actions/AssignToMe')
    def put_tasks_id_actions_assign_to_me(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/AssignToMe', body, params)

    @allure.step('Смена исполнителя. PUT /api/Tasks/{id}/Actions/ChangeContractor')
    def put_tasks_id_actions_change_contractor(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/ChangeContractor', body, params)

    @allure.step('Очистка исполнителя в задаче. PUT /api/Tasks/{id}/Actions/ClearContractor')
    def put_tasks_id_actions_clear_contractor(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/ClearContractor', body, params)

    @allure.step('Согласовать задачу. PUT /api/Tasks/{id}/Actions/Approve')
    def put_tasks_id_actions_approve(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/Approve', body, params)

    @allure.step('Отклонить задачу. PUT /api/Tasks/{id}/Actions/Reject')
    def put_tasks_id_actions_reject(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/Reject', body, params)

    @allure.step('Добавить согласование. POST /api/Tasks/{id}/Agreements')
    def post_tasks_id_agreements(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Tasks/{id}/Agreements', body, params)

    @allure.step('Перевод задачи на проверку. PUT /api/Tasks/{id}/Actions/Resolve')
    def put_tasks_id_actions_resolve(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/Resolve', body, params)

    @allure.step('Отмена задачи. PUT /api/Tasks/{id}/Actions/Cancel')
    def put_tasks_id_cancel(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/Cancel', body, params)

    @allure.step('Апеллировать. PUT /api/Tasks/{id}/Actions/Appeal')
    def put_tasks_id_actions_appeal(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/Appeal', body, params)

    @allure.step('Задать вопрос-уточнение инициатору. PUT /api/Tasks/{id}/Actions/Clarifications/AskInitiator')
    def put_tasks_id_actions_clarifications_ask_initiator(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/Clarifications/AskInitiator', body, params)

    @allure.step('Добавить согласование. POST /api/Tasks/{id}/Agreements')
    def post_tasks_id_agreements(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Tasks/{id}/Agreements', body, params)

    @allure.step('Возвращение задачи из проверки в работу. PUT /api/Tasks/{id}/Actions/BackToWork')
    def put_tasks_id_actions_back_to_work(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/BackToWork', body, params)

    @allure.step('Возврат на доработку. PUT /api/Tasks/{id}/Actions/ReturnToRework')
    def put_tasks_id_actions_return_to_rework(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/ReturnToRework', body, params)

    @allure.step('Оценка и закрытие задачи. PUT /api/Tasks/{id}/Actions/Close')
    def put_tasks_id_actions_close(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/Close', body, params)

    @allure.step('Задать вопрос-уточнение исполнителю. PUT /api/Tasks/{id}/Actions/Clarifications/AskContractor')
    def put_tasks_id_actions_clarifications_ask_contractor(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/Clarifications/AskContractor', body, params)

    @allure.step('Перевод задачи из ожидания в работу. PUT /api/Tasks/{id}/Actions/ToWork')
    def put_tasks_id_actions_to_work(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/ToWork', body, params)

    @allure.step('Отменить уточнение. PUT /api/Tasks/{id}/Actions/Clarifications/Cancel')
    def put_tasks_id_actions_clarifications_cancel(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/Clarifications/Cancel', body, params)

    @allure.step('Инициатор отвечает на вопрос-уточнение. PUT /api/Tasks/{id}/Actions/Clarifications/InitiatorAnswer')
    def put_tasks_id_actions_clarifications_initiator_answer(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/Clarifications/InitiatorAnswer', body, params)

    @allure.step('Аппеляция. PUT /api/Tasks/{id}/Actions/Appeal')
    def put_tasks_id_actions_appeal(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/Appeal', body, params)

    @allure.step('Удалить согласование. DELETE /api/Tasks/{id}/Agreements/{agreementId}')
    def delete_tasks_id_agreements_agreement_id(self, id, agreementId, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/Tasks/{id}/Agreements/{agreementId}', params=params)

    @allure.step('Исполнитель отвечает на вопрос-уточнение. PUT /api/Tasks/{id}/Actions/Clarifications/ContractorAnswer')
    def put_tasks_id_actions_clarifications_contractor_answer(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/Clarifications/ContractorAnswer', body, params)

    @allure.step('Делегировать согласование. PUT /api/Tasks/{id}/Actions/DelegateAgreement')
    def put_tasks_id_actions_delegate_agreement(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/DelegateAgreement', body, params)

    @allure.step('Добавить задачу в избранное. POST /api/Tasks/{id}/Favourites')
    def post_tasks_id_favourites(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Tasks/{id}/Favourites', body, params)

    @allure.step('Список уровней согласования (история согласований). GET /api/Tasks/{id}/Agreements')
    def get_all_levels_agreements(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Tasks/{id}/Agreements', params)

    @allure.step('Добавление нового блока в описание тикета. POST /api/Tasks/{id}/Description')
    def post_tasks_id_description(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Tasks/{id}/Description', body, params)

    @allure.step('Добавить вложения. POST /api/Tasks/{id}/AddAttachments')
    def post_tasks_id_add_attachments(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Tasks/{id}/AddAttachments', body, params)

    @allure.step('Удалить вложения. POST /api/Tasks/{id}/DeleteAttachments')
    def post_tasks_id_delete_attachments(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Tasks/{id}/DeleteAttachments', body, params)

    @allure.step('Редактирование блока описания тикета. PUT /api/Tasks/{id}/Description/{descId}')
    def put_tasks_id_description_desc_id(self, id, descId, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Description/{descId}', body, params)

    @allure.step('Обновление обозревателей. PUT /api/Tasks/{id}/Observers')
    def put_tasks_id_observers(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Observers', body, params)

    @allure.step('Обновление инициатора в задаче. PUT /api/Tasks/{id}/Actions/ChangeInitiator')
    def put_tasks_id_actions_change_initiator(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Tasks/{id}/Actions/ChangeInitiator', body, params)

# PUT
# /api/Tasks/{id}/Actions/Delegate
# Делегировать исполнение
#
#
# PUT
# /api/Tasks/{id}/Actions/Reject
# Отклонить
#
#
# PUT
# /api/Tasks/{id}/Actions/Clarifications/Join
# Присоединиться к уточнению.
#
#
# DELETE
# /api/Tasks/{id}/Favourites
# Удаление проектов из избранных
#
#
# POST
# /api/Tasks/{id}/Agreements
# Добавить согласование
#
#
# DELETE
# /api/Tasks/{id}/Agreements/{agreementId}
# Удалить согласование
#
#
# POST
# /api/Tasks/{id}/Observers
# Добавить обозревателя
#
#
# DELETE
# /api/Tasks/{id}/Observers/{observerId}
# Удалить обозревателя
#
#
# GET
# /api/Tasks/{id}/Members
# Возвращает список участников тикета
#
#
# GET
# /api/Tasks/{id}/Actions
# Получить список доступных действий над тикетом