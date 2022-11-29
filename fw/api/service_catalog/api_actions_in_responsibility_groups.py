import allure

from fw.api.service_catalog.responsibility_groups import ResponsibilityGroups


class ActionsInResponsibilityGroups(ResponsibilityGroups):

    @allure.title('Поиск группы ответственности')
    def search_responsibility_group(self, name, is_deleted=False, is_active=True, result_view='List'):

        # Подготовка тела запроса для поиска ГО
        responsibility_group_body = {
            'search': name,
            'skip': 0,
            'take': 10,
            'isDeleted': is_deleted,
            'isActive': is_active,
            'resultView': result_view,
        }

        # Ищем нужную ГО
        responsibility_group = self.post_responsibility_groups_filter(responsibility_group_body)

        return responsibility_group

    @allure.title('Создание группы ответственности')
    def create_responsibility_group(self, parent_responsibility_group_id, dispatcher_id=None, is_active=True):

        # Подготовка тела запроса для создания ГО
        responsibility_group_body = {
            'parentId': parent_responsibility_group_id,
            'name': 'AutomationApiTest ' + self.manager.time.get_date_time_Y_m_d_H_M_S(),
            'isActive': is_active,
        }
        if dispatcher_id:
            responsibility_group_body['dispatcherUserId'] = dispatcher_id

        # Создаем группу ответственности
        responsibility_group = self.post_responsibility_groups(responsibility_group_body)

        return responsibility_group

    @allure.title('Создание группы ответственности с диспетчером')
    def create_responsibility_group_with_dispatcher(self, parent_responsibility_group_id, dispatcher=None, user=None,
                                                    is_active=True):
        # Подготовка тела запроса для создания ГО
        responsibility_group_body = {
            'parentId': parent_responsibility_group_id,
            'name': 'AutomationApiTest ' + self.manager.time.get_date_time_Y_m_d_H_M_S(),
            'dispatcherUserId': self.manager.group_data.users[dispatcher]['user_id'],
            "responsibilityGroupMembers": [
                {
                    "id": self.manager.group_data.users[dispatcher]['user_id'],
                    "type": "User",
                },

                {
                    "id": self.manager.group_data.users[user]['user_id'],
                    "type": "User",
                }
            ],

            'isActive': is_active,
        }

        # Создаем группу ответственности
        responsibility_group = self.post_responsibility_groups(responsibility_group_body)

        return responsibility_group

    @allure.title('Добавление пользователей в группу ответственности')
    def add_user_in_responsibility_group(self, user_id, responsibility_group_id):

        # Формируем тело запроса для добавления пользователя в ГО
        responsibility_group_body = {
            'users': [user_id, ],
        }

        # добавляем пользователя в ГО
        responsibility_group = self.post_responsibility_groups_id_users(responsibility_group_id, responsibility_group_body)

        return responsibility_group

    @allure.title('Поиск пользователя в группе ответственности')
    def search_user_in_responsibility_group(self, user, responsibility_group_id):
        """"Пользователя (user) указывать так, как он записан в Gandiva"""

        # Формируем тело запроса для поиска пользователей в ГО
        responsibility_group_body = {
            'search': user,
            'skip': 0,
            'take': 1,
        }

        # Ищем пользователя в группе ответственности
        user_in_responsibility_group = self.post_responsibility_groups_id_users_filter(responsibility_group_id, responsibility_group_body)

        return user_in_responsibility_group

    @allure.title('Удаление пользователя из группы ответственности')
    def delete_user_onto_responsibility_group(self, user_id, responsibility_group_id):

        # Формируем тело запроса для удаления пользователя из ГО
        responsibility_group_body = [user_id]

        # Удаляем пользователя из ГО
        self.delete_responsibility_groups_id_users(responsibility_group_id, body=responsibility_group_body)

    @allure.title('Редактирование группы ответственности (изменение статуса)')
    def edit_status_in_responsibility_group(self, responsibility_group_id, is_active=False):

        # Подготовка тела запроса для редактирования группы ответственности
        responsibility_group_body = {
            'isActive': is_active
        }

        # Редактируем группу ответственности
        responsibility_group = self.put_responsibility_groups_id(responsibility_group_id, responsibility_group_body)

        return responsibility_group

    @allure.title('Удаление группы ответственности')
    def delete_responsibility_group(self, responsibility_group_id):

        # Подготовка тела запроса для удаления группы ответственности
        responsibility_group_body = {
            'isDeleted': True
        }

        # Удаляем группу ответственности
        responsibility_group = self.put_responsibility_groups_id(responsibility_group_id, responsibility_group_body)

        return responsibility_group

    @allure.title('Перемещение группы ответственности')
    def move_responsibility_group(self, parent_responsibility_group_id, responsibility_group_id):
        # Формируем тело запроса для перемещения группы ответственности
        responsibility_group_body = {
            'parentId': parent_responsibility_group_id
        }

        # Перемещаем группу ответственности
        responsibility_group = self.put_responsibility_groups_id(responsibility_group_id, responsibility_group_body)

        return responsibility_group

    @allure.title('Переименование группы ответственности')
    def rename_responsibility_group(self, responsibility_group_id, new_rg_name):
        # Формируем тело запроса для переименования группы ответственности
        responsibility_group_body = {
            'name': new_rg_name
        }

        # Переименовываем группу ответственности
        responsibility_group = self.put_responsibility_groups_id(responsibility_group_id, responsibility_group_body)

        return responsibility_group

    @allure.title('Проверка наличия искомой ГО в поиске по ГО')
    def find_responsibility_group_in_search(self, responsibility_group_name):

        # Поиск группы ответственности
        responsibility_group_search = self.search_responsibility_group(responsibility_group_name)

        # Ставим флаг
        rg_check = False

        # Цикл проверки наличия искомой ГО в поиске по ГО
        for rg_list in responsibility_group_search['items']:
            if responsibility_group_name in rg_list['name']:
                rg_check = True
                break

        return rg_check



