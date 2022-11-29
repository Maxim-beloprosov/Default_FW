import allure

from fw.g1_api.g1_api_base import G1APIBase


class G1ApiCommon(G1APIBase):

    @allure.step('Поиск хэштегов по названию. GET api/Common/HashTags/Search')
    def get_common_hash_tags_search(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Common/HashTags/Search', params)

    @allure.step('Возвращает вложение с уникальной меткой guid. GET api/Common/Attachments/{guid}')
    def get_common_attachments_guid(self, guid, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Common/Attachments/{guid}', params)

    @allure.step('Возвращает вложение с уникальной меткой guid(Info). GET api/Common/Attachments/{guid}/Info')
    def get_common_attachments_guid_info(self, guid, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Common/Attachments/{guid}/Info', params)

    @allure.step('Возвращает Base64 вложение с уникальной меткой guid. GET api/Common/AttachmentsBase64/{guid}')
    def get_common_attachments_base64_guid(self, guid, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Common/AttachmentsBase64/{guid}', params)

    @allure.step('Возвращает список избранных элементов для данного пользователя. GET api/Common/Favourites')
    def get_common_favourites(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Common/Favourites', params)

    @allure.step('Поиск задач/заявок/проектов по номеру в строке или тексту. GET api/Common/Find')
    def get_common_find(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Common/Find', params)

    @allure.step('Возвращает картинку по пути. GET api/Common/ProcessCommentImages')
    def get_common_process_comment_images(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Common/ProcessCommentImages', params)

    @allure.step('POST api/Common/PushNotificationToken')
    def post_common_push_notification_token(self, params=None):
        return self.requests_POST(self.get_base_url() + f'api/Common/PushNotificationToken', params)

    @allure.step('Подписка на пуш уведомления. POST api/Common/SubscribeForNotifications')
    def post_common_subscribe_for_notifications(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Common/SubscribeForNotifications', body, params)

    @allure.step('Отмена подписки на пуш уведомления. POST api/Common/UnsubscribeForNotifications')
    def post_common_unsubscribe_for_notifications(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Common/UnsubscribeForNotifications', body, params)

    @allure.step('Проверка доступности сервера АПИ. GET api/Common/ping')
    def get_common_ping(self, params=None):
        return self.requests_GET(self.get_base_url() + 'api/Common/ping', params)

    @allure.step('Сохраняет файлы во временное хранилище. POST api/Common/Attachments/Upload')
    def post_common_attachments_upload(self, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Common/Attachments/Upload', params)

    @allure.step('Сохраняет файлы в формате base64 во временное хранилище. POST api/Common/Attachments/UploadBase64')
    def post_common_attachments_upload_base64(self, body, params=None):
        return self.requests_POST(self.get_base_url() + 'api/Common/Attachments/UploadBase64', body, params)

    @allure.step('Помечает комментарий как прочитанный. PUT api/Common/Comments/{id}/Read')
    def put_common_comments_id_read(self, id, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Common/Comments/{id}/Read', params)

    @allure.step('Редактирование комментария. PUT api/Common/Comments/{id}')
    def put_common_comments_id(self, id, params=None):
        return self.requests_PUT(self.get_base_url() + f'api/Common/Comments/{id}', params)

    @allure.step('Удаление комментария. DELETE api/Common/Comments/{id}')
    def delete_common_comments_id(self, id, params=None):
        return self.requests_DELETE(self.get_base_url() + f'api/Common/Comments/{id}', params)
