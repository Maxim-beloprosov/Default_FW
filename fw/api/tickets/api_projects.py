import allure

from fw.api.api_base import APIBase


class ApiProjects(APIBase):

    @allure.step('Получение проекта по номеру. GET /api/Projects/DocumentNumber/{number}')
    def get_projects_document_number(self, number, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Projects/DocumentNumber/{number}', params)

    @allure.step('Список проектов. POST /api/Projects/Filter')
    def post_project_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Projects/Filter', body, params)

    @allure.step('Получение проекта по ключу. GET /api/Projects/{id}')
    def get_projects_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Projects/{id}', params)

    @allure.step('Обновление проекта. PUT /api/Projects/{id}')
    def put_projects_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}', body, params)

    @allure.step('Создать новый проект. POST api/Projects')
    def post_projects(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Projects', body, params)

    @allure.step('Изменить запланированное время проекта. PUT /api/Projects/{id}/Actions/ChangePlannedTime')
    def put_projects_id_actions_change_planned_time(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/ChangePlannedTime', body, params)

    @allure.step('Назначить на себя. PUT /api/Projects/{id}/Actions/AssignToMe')
    def put_projects_id_actions_assign_to_me(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/AssignToMe', body, params)

    @allure.step('Смена исполнителя. PUT /api/Projects/{id}/Actions/ChangeContractor')
    def put_projects_id_actions_change_contractor(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/ChangeContractor', body, params)

    @allure.step('Очистка исполнителя в проекте. PUT /api/Projects/{id}/Actions/ClearContractor')
    def put_projects_id_actions_clear_contractor(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/ClearContractor', body, params)

    @allure.step('Согласовать. PUT /api/Projects/{id}/Actions/Approve')
    def put_projects_id_actions_approve(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/Approve', body, params)

    @allure.step('Отклонить. PUT /api/Projects/{id}/Actions/Reject')
    def put_projects_id_actions_reject(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/Reject', body, params)

    @allure.step('Перевод проекта на проверку. PUT /api/Projects/{id}/Actions/Resolve')
    def put_projects_id_actions_resolve(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/Resolve', body, params)

    @allure.step('Делегировать согласование. PUT /api/Projects/{id}/Actions/DelegateAgreement')
    def put_projects_id_actions_delegate_agreement(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/DelegateAgreement', body, params)

    @allure.step('Перевод проекта из ожидания в работу. PUT /api/Projects/{id}/Actions/ToWork')
    def put_projects_id_actions_to_work(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/ToWork', body, params)

    @allure.step('Возвращение проекта из проверки в работу. PUT /api/Projects/{id}/Actions/BackToWork')
    def put_projects_id_actions_back_to_work(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/BackToWork', body, params)

    @allure.step('Возврат на доработку. PUT /api/Projects/{id}/Actions/ReturnToRework')
    def put_projects_id_actions_return_to_work(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/ReturnToRework', body, params)

    @allure.step('Отмена проекта. PUT /api/Projects/{id}/Actions/Cancel')
    def put_projects_id_actions_cancel(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/Cancel', body, params)

    @allure.step('Закрытие проекта. PUT /api/Projects/{id}/Actions/Close')
    def put_projects_id_actions_close(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/Close', body, params)

    @allure.step('Апеллировать. PUT /api/Projects/{id}/Actions/Appeal')
    def put_projects_id_actions_appeal(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/Appeal', body, params)

    @allure.step('Задать вопрос-уточнение инициатору. PUT /api/Projects/{id}/Actions/Clarifications/AskInitiator')
    def put_projects_id_actions_clarifications_ask_initiator(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/Clarifications/AskInitiator', body, params)

    @allure.step('Задать вопрос-уточнение исполнителю. PUT /api/Projects/{id}/Actions/Clarifications/AskContractor')
    def put_projects_id_actions_clarifications_ask_contractor(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/Clarifications/AskContractor', body, params)

    @allure.step('Инициатор отвечает на вопрос-уточнение. PUT /api/Projects/{id}/Actions/Clarifications/InitiatorAnswer')
    def put_projects_id_actions_clarifications_initiator_answer(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/Clarifications/InitiatorAnswer', body, params)

    @allure.step('Обновление инициатора в проекте. PUT /api/Projects/{id}/Actions/ChangeInitiator')
    def put_projects_id_actions_change_initiator(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/ChangeInitiator', body, params)

    @allure.step('Исполнитель отвечает на вопрос-уточнение. PUT /api/Projects/{id}/Actions/Clarifications/ContractorAnswer')
    def put_projects_id_actions_clarifications_contractor_answer(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/Clarifications/ContractorAnswer', body, params)

    @allure.step('Присоединиться к уточнению. PUT /api/Projects/{id}/Actions/Clarifications/Join')
    def put_projects_id_actions_clarifications_join(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/Clarifications/Join', body, params)

    @allure.step('Отменить уточнение. PUT /api/Projects/{id}/Actions/Clarifications/Cancel')
    def put_projects_id_actions_clarifications_cancel(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Actions/Clarifications/Cancel', body, params)

    @allure.step('Список доступных пользователей для согласования. POST /api/Projects/Agreements/Filter')
    def post_projects_agreements_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Projects/Agreements/Filter', body, params)

    @allure.step('Добавить согласование. POST /api/Projects/{id}/Agreements')
    def post_projects_id_agreements(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Projects/{id}/Agreements', body, params)

    @allure.step('Список уровней согласования (история согласований). GET /api/Projects/{id}/Agreements')
    def get_projects_id_agreements(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Projects/{id}/Agreements', params)

    @allure.step('Удалить согласование. DELETE /api/Projects/{id}/Agreements/{agreementId}')
    def delete_projects_id_agreements_agreement_id(self, id, agreementId, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/Projects/{id}/Agreements/{agreementId}', params)

    @allure.step('Список доступных обозревателей-пользователей и групп. POST /api/Projects/Observers/Filter')
    def post_projects_observers_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Projects/Observers/Filter', body, params)

    @allure.step('Обновление обозревателей. PUT /api/Projects/{id}/Observers')
    def put_projects_id_observers(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Observers', body, params)

    @allure.step('Добавить обозревателя. POST /api/Projects/{id}/Observers')
    def post_projects_id_observers(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Projects/{id}/Observers', body, params)

    @allure.step('Удалить обозревателя. DELETE /api/Projects/{id}/Observers/{observerId}')
    def delete_projects_id_observers_observer_id(self, id, observerId, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/Projects/{id}/Observers/{observerId}', params)

    @allure.step('Сохранение проектов в избранных. POST /api/Projects/{id}/Favourites')
    def post_projects_id_favorites(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Projects/{id}/Favourites', body, params)

    @allure.step('Удаление проектов из избранных. DELETE /api/Projects/{id}/Favourites')
    def delete_projects_id_favorites(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/Projects/{id}/Favourites', params)

    @allure.step('Добавить вложение. POST /api/Projects/{id}/Attachments')
    def post_projects_id_attachments(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Projects/{id}/Attachments', body, params)

    @allure.step('Добавить вложение. POST /api/Projects/{id}/AddAttachments')
    def post_projects_id_add_attachments(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Projects/{id}/AddAttachments', body, params)

    @allure.step('Удалить вложение. DELETE /api/Projects/{id}/DeleteAttachments')
    def delete_projects_id_delete_attachments(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'/api/Projects/{id}/DeleteAttachments', params)

    @allure.step('Получение файла из проекта по идентификатору проекта и идентификатору файла. GET /api/Projects/{id}/Files/{fileId}')
    def get_projects_id_files_file_id(self, id, fileId, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Projects/{id}/Files/{fileId}', params)

    @allure.step('Получение миниатюры файла из проекта по идентификатору проекта и идентификатору файла. GET /api/Projects/{id}/Files/{fileId}/Miniature')
    def get_projects_id_files_file_id_miniature(self, id, fileId, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Projects/{id}/Files/{fileId}/Miniature', params)

    @allure.step('Получение информации по файлу из проекта по идентификатору проекта и идентификатору файла. GET /api/Projects/{id}/Files/{fileId}/Info')
    def get_projects_id_files_file_id_info(self, id, fileId, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Projects/{id}/Files/{fileId}/Info', params)

    @allure.step('Возвращает список участников тикета. GET /api/Projects/{id}/Members')
    def get_projects_id_members(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Projects/{id}/Members', params)

    @allure.step('Добавление нового блока в описание тикета. POST /api/Projects/{id}/Description')
    def post_projects_id_description(self, id, body, params=None):
        return self.requests_POST(self.get_base_url() + f'/api/Projects/{id}/Description', body, params)

    @allure.step('Редактирование блока описания тикета. PUT /api/Projects/{id}/Description/{descId}')
    def put_projects_id_description_desc_id(self, id, descId, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/Projects/{id}/Description/{descId}', body, params)

    @allure.step('Получить список доступных действий над тикетом. GET /api/Projects/{id}/Actions')
    def get_projects_id_actions(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'/api/Projects/{id}/Actions', params)
