import allure

from fw.api.api_base import APIBase


class ApiGroups(APIBase):

    @allure.step('Поиск групп с учетом фильтра. POST /api/Groups/Filter')
    def post_search_group_with_including_filter(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Groups/Filter', body, params)

    @allure.step('Создание группы. POST /api/Groups')
    def post_create_users_group(self, body, params=None):
        return self.requests_POST(self.get_base_url() + '/api/Groups', body, params)

#
# POST
# /api/Groups
# Создание группы
#

# GET
# /api/Groups/{id}
# Получение группы по ключу
#
#
# PUT
# /api/Groups/{id}
# Обновление группы
#
#
# DELETE
# /api/Groups/{id}
# Удаление группы
#
#
# POST
# /api/Groups/{id}/Tree
# Возвращаем группу с родительскими и родительскими дочерними группами
#

#
# POST
# /api/Groups/Users/GetByGroups
# Возвращаем список пользователей имеющихся в группах заданных списком groups
#
#
# POST
# /api/Groups/Users/GetIdGuidByGroups
# Возвращаем список идентификаторов пользователей имеющихся в группах заданных списком groups
#
#
# POST
# /api/Groups/Members/Filter
# Поиск групп или пользователей с учетом фильтра в карточке Группы.
#
#
# PUT
# /api/Groups/{id}/Members
# Обновление участников группы
#
#
# POST
# /api/Groups/ChildrenCount
# Получение кол-ва дочерних групп
#
#
# POST
# /api/Groups/AdditionalInfo
# Получение дополнительной информации по группе
#
#
# POST
# /api/Groups/{id}/Move
# Перемещение группы
