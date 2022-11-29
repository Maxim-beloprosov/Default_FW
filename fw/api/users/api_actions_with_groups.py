import allure

from fw.api.users.api_groups import ApiGroups


class ActionsInGroups(ApiGroups):

    @allure.title('Поиск групп с учетом фильтра')
    def search_group_with_including_filter(self, group_mass={}, amount_groups=20):

        json_group = {}

        # ----- parentId -----
        if 'parentId' in group_mass:
            json_group['parentId'] = group_mass['parentId']

        # ----- search ------
        if 'search' in group_mass:
            json_group['search'] = group_mass['search']

        # ------ filter ------
        if 'filter' in group_mass:
            json_group['filter'] = group_mass['filter']

        # ------ take ------
        json_group['take'] = amount_groups

        # ----- isActive -----
        if 'isActive' in group_mass:
            json_group['isActive'] = group_mass['isActive']

        # ----- isDeleted -----
        if 'isDeleted' in group_mass:
            json_group['isDeleted'] = group_mass['isDeleted']

        search_group = self.post_search_group_with_including_filter(json_group)

        return search_group

    @allure.title('Создание пользовательской группы')
    def create_users_group(self, group_mass={}):

        json_group = {}

        # ---- name ----
        if 'name' in group_mass:
            json_group['name'] = group_mass['name']
        else:
            json_group['name'] = 'AutomationApiGroupUsers'

        # ----- parentId -----
        if 'parentid' in group_mass:
            json_group['parentId'] = group_mass['parentId']

        # ------ orderNumber ------
        if 'orderNumber' in group_mass:
            json_group['orderNumber'] = group_mass['orderNumber']

        # ------ members -------
        if 'members' in group_mass:
            json_group['members'] = group_mass['members']

        created_group = self.post_create_users_group(json_group)

        return created_group

    @allure.title('Поиск и проверка существования группы тестовых пользователей пользователей')
    def search_and_check_existence_group(self, name_group):

        # AutomationApiGroupUsers - группа тестовых пользователей

        # Подготовка тела для поиска группы тестовых пользователей
        filter_body = {
            "search": name_group,
            "filter": {
                "groupType": "All",
                "userCount": {
                    "min": 10,
                    "max": 10
                },
                "groupCount": {
                    "min": 0,
                    "max": 0
                },
                "userIds": [
                    self.manager.group_data.users['test_user01']['user_id'],
                    self.manager.group_data.users['test_user02']['user_id'],
                    self.manager.group_data.users['test_user03']['user_id'],
                    self.manager.group_data.users['test_user04']['user_id'],
                    self.manager.group_data.users['test_user05']['user_id'],
                    self.manager.group_data.users['test_user06']['user_id'],
                    self.manager.group_data.users['test_user07']['user_id'],
                    self.manager.group_data.users['test_user08']['user_id'],
                    self.manager.group_data.users['test_user09']['user_id']
                ]
            },
            "isActive": True,
            "isDeleted": False
        }

        # Поиск пользовательской группы тестовых пользователей (Если группа не найдена, создать)
        users_group = self.search_group_with_including_filter(filter_body, 1000)

        # Создание группы, если она не была найдена
        if (len(users_group) == 0):
            created_group = self.manager.api_actions_in_group.create_users_group({'members': [
                {'id': self.manager.group_data.users['test_user01']['user_id'], 'memberType': 'User'},
                {'id': self.manager.group_data.users['test_user02']['user_id'], 'memberType': 'User'},
                {'id': self.manager.group_data.users['test_user03']['user_id'], 'memberType': 'User'},
                {'id': self.manager.group_data.users['test_user04']['user_id'], 'memberType': 'User'},
                {'id': self.manager.group_data.users['test_user05']['user_id'], 'memberType': 'User'},
                {'id': self.manager.group_data.users['test_user06']['user_id'], 'memberType': 'User'},
                {'id': self.manager.group_data.users['test_user07']['user_id'], 'memberType': 'User'},
                {'id': self.manager.group_data.users['test_user08']['user_id'], 'memberType': 'User'},
                {'id': self.manager.group_data.users['test_user09']['user_id'], 'memberType': 'User'}
            ]})

            # Повторный поиск группы
            users_group = self.search_group_with_including_filter(filter_body, 1000)

        # Поиск необходимой группы, если пришло больше 1 элемента
        if len(users_group) > 1:
            for items in users_group['items']:
                if items['title'] == name_group:
                    users_group = items
                    return users_group

        # Если была найдена не та группа
        if users_group[0]['title'] != name_group:
            users_group = 'Expected group not found'

        return users_group
