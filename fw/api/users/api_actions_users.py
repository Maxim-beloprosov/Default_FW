import allure

from fw.api.users.api_users import ApiUsers


class ActionsInUsers(ApiUsers):

    @allure.step ('Создание пользователя')
    def add_user(self, count_value=None, fields_mass={}):

        # Поиск количества(count) пользователей для создания уникальных полей
        if count_value is None:
            search_count = self.post_users_filter_count({'search': 'testName'})
            count = search_count['totalCount']
        else:
            count = count_value

        json_user_body = {}
        # Подготовка данных для создания уникального логина пользователя
        if 'login' in fields_mass:
            json_user_body['login'] = fields_mass['login'] + str(count)
        else:
            json_user_body['login'] = self.manager.group_data.data_for_adding_user['test_users']['test_user']['login'] + str(count)

        # Создаем данные - поле 'name'
        if 'name' in fields_mass:
            json_user_body['name'] = fields_mass['name']
        else:
            json_user_body['name'] = self.manager.group_data.data_for_adding_user['test_users']['test_user']['name']

        # Создаем данные - поле 'surname'
        if 'surname' in fields_mass:
            json_user_body['surname'] = fields_mass['surname']
        else:
            json_user_body['surname'] = self.manager.group_data.data_for_adding_user['test_users']['test_user']['surname']

        # Создаем данные - поле 'middleName'
        if 'middleName' in fields_mass:
            json_user_body['middleName'] = fields_mass['middleName']

        # Создаем данные - поле 'photoId'
        if 'photoId' in fields_mass:
            json_user_body['photoId'] = fields_mass['photoId']

        # Создаем данные - поле 'email'
        if 'email' in fields_mass:
            json_user_body['email'] = str(count) + fields_mass['email']

        # Создаем данные - поле 'mobilePhone'
        if 'mobilePhone' in fields_mass:
            json_user_body['mobilePhone'] = fields_mass['mobilePhone'] + str(count)

        # Создаем данные - поле 'managerId'
        if 'managerId' in fields_mass:
            json_user_body['managerId'] = fields_mass['managerId']

        # Создаем данные - поле 'alternateId'
        if 'alternateId' in fields_mass:
            json_user_body['alternateId'] = fields_mass['alternateId']

        # Создаем данные - поле 'organizationId'
        if 'organizationId' in fields_mass:
            json_user_body['organizationId'] = fields_mass['organizationId']

        # Создаем данные - поле 'departmentId'
        if 'departmentId' in fields_mass:
            json_user_body['departmentId'] = fields_mass['departmentId']

        # Создаем данные - поле 'positionId'
        if 'positionId' in fields_mass:
            json_user_body['positionId'] = fields_mass['positionId']

        # Создаем данные - поле 'actualAddressId'
        if 'actualAddressId' in fields_mass:
            json_user_body['actualAddressId'] = fields_mass['actualAddressId']

        # Создаем данные - поле 'legalAddressId'
        if 'legalAddressId' in fields_mass:
            json_user_body['legalAddressId'] = fields_mass['legalAddressId']

        # Создаем данные - поле 'cityPhone'
        if 'cityPhone' in fields_mass:
            json_user_body['cityPhone'] = fields_mass['cityPhone'] + str(count)

        # Создаем данные - поле 'internalPhone'
        if 'internalPhone' in fields_mass:
            json_user_body['internalPhone'] = fields_mass['internalPhone'] + str(count)

        # Создаем пользователя
        response = self.post_users(json_user_body)
        return response

    @allure.step('Сбросить все поля к дефолтным значениям')
    def user_default_fields(self, user_id):

        # Формируем тело запроса
        change_user_body = {
            'name': self.manager.group_data.data_for_adding_user['test_users']['test_user']['name'],
            'surname': self.manager.group_data.data_for_adding_user['test_users']['test_user']['surname'],
            'middleName': self.manager.group_data.data_for_adding_user['test_users']['test_user']['middleName'],
            'photoId': self.manager.group_data.data_for_adding_user['photos']['avatar_automationTestApi']['id'],
            'email': '000' + self.manager.group_data.data_for_adding_user['test_users']['test_user']['email'],
            'mobilePhone': self.manager.group_data.data_for_adding_user['test_users']['test_user']['mobilePhone'] + '00',
            'managerId': self.manager.group_data.data_for_adding_user['test_users']['api.test.manager']['id'],
            'alternateId': self.manager.group_data.data_for_adding_user['test_users']['api.test.alternate']['id'],
            'organizationId': self.manager.group_data.data_for_adding_user['organizations']['organization_automationTestApi']['id'],
            'departmentId': self.manager.group_data.data_for_adding_user['departments']['department_automationTestApi']['id'],
            'positionId': self.manager.group_data.data_for_adding_user['positions']['position_automationTestApi']['id'],
            'actualAddressId': self.manager.group_data.data_for_adding_user['addresses']['address_automationTestApi']['id'],
            'legalAddressId': self.manager.group_data.data_for_adding_user['addresses']['address_automationTestApi']['id'],
            'cityPhone': self.manager.group_data.data_for_adding_user['test_users']['test_user']['cityPhone'] + '00',
            'internalPhone': self.manager.group_data.data_for_adding_user['test_users']['test_user']['internalPhone'] + '00'
        }

        # Редактируем пользователя
        change_user = self.put_users_id(user_id, change_user_body)

        return change_user

    @allure.step('Редактирование пользователя')
    def change_user(self, user_id, set_fields):

        # Значения для редактирования пользователя
        fields_values = {
            'name': {'name': self.manager.group_data.data_for_adding_user['test_users']['new_test_user']['name']},
            'surname': {'surname': self.manager.group_data.data_for_adding_user['test_users']['new_test_user']['surname']},
            'middleName': {'middleName': self.manager.group_data.data_for_adding_user['test_users']['new_test_user']['middleName']},
            'photoId': {'photoId': self.manager.group_data.data_for_adding_user['photos']['avatar_automationTestApi']['id']},
            'email': {'email': self.manager.group_data.data_for_adding_user['test_users']['new_test_user']['email']},
            'mobilePhone': {'mobilePhone': self.manager.group_data.data_for_adding_user['test_users']['new_test_user']['mobilePhone']},
            'manager': {'managerId': self.manager.group_data.data_for_adding_user['test_users']['api.test.newmanager']['id']},
            'alternate': {'alternateId': self.manager.group_data.data_for_adding_user['test_users']['api.test.new.alternate']['id']},
            'organization': {'organizationId': self.manager.group_data.data_for_adding_user['organizations']['new_organization_automationTestApi']['id']},
            'department': {'departmentId': self.manager.group_data.data_for_adding_user['departments']['new_department_automationTestApi']['id']},
            'position': {'positionId': self.manager.group_data.data_for_adding_user['positions']['new_position_automationTestApi']['id']},
            'actualAddress': {'actualAddressId': self.manager.group_data.data_for_adding_user['addresses']['new_address_automationTestApi']['id']},
            'legalAddress': {'legalAddressId': self.manager.group_data.data_for_adding_user['addresses']['new_address_automationTestApi']['id']},
            'cityPhone': {'cityPhone': self.manager.group_data.data_for_adding_user['test_users']['new_test_user']['cityPhone']},
            'internalPhone': {'internalPhone': self.manager.group_data.data_for_adding_user['test_users']['new_test_user']['internalPhone']}
        }

        # Формурием тело запроса с нужным значением
        # Если в 'fields_values' есть ключ из 'set_fields', то добавляем тело в 'fields_body'
        if set_fields in fields_values:
            fields_body = fields_values[set_fields]

        # Редактируем пользователя
        change_user = self.put_users_id(user_id, fields_body)

        return change_user

    @allure.step('Получение значений, используемые при редактировании пользователя, для проверки')
    def value_change_user(self, set_fields):

        # Значения для проверки
        fields_values = {
            'name': self.manager.group_data.data_for_adding_user['test_users']['new_test_user']['name'],
            'surname': self.manager.group_data.data_for_adding_user['test_users']['new_test_user']['surname'],
            'middleName': self.manager.group_data.data_for_adding_user['test_users']['new_test_user']['middleName'],
            'photoId': self.manager.group_data.data_for_adding_user['photos']['avatar_automationTestApi']['id'],
            'email': self.manager.group_data.data_for_adding_user['test_users']['new_test_user']['email'],
            'mobilePhone': self.manager.group_data.data_for_adding_user['test_users']['new_test_user']['mobilePhone'],
            'manager': self.manager.group_data.data_for_adding_user['test_users']['api.test.newmanager']['id'],
            'alternate': self.manager.group_data.data_for_adding_user['test_users']['api.test.new.alternate']['id'],
            'organization': self.manager.group_data.data_for_adding_user['organizations']['new_organization_automationTestApi']['id'],
            'department': self.manager.group_data.data_for_adding_user['departments']['new_department_automationTestApi']['id'],
            'position': self.manager.group_data.data_for_adding_user['positions']['new_position_automationTestApi']['id'],
            'actualAddress': self.manager.group_data.data_for_adding_user['addresses']['new_address_automationTestApi']['id'],
            'legalAddress': self.manager.group_data.data_for_adding_user['addresses']['new_address_automationTestApi']['id'],
            'cityPhone': self.manager.group_data.data_for_adding_user['test_users']['new_test_user']['cityPhone'],
            'internalPhone': self.manager.group_data.data_for_adding_user['test_users']['new_test_user']['internalPhone']
        }

        # Получаем нужное значение для проверки
        set_field_value = fields_values[set_fields]

        return set_field_value

    @allure.step('Поиск созданных пользователей по имени')
    def search_users(self, search_name=None):

        # Формируем тело запроса для поиска пользователей
        search_body = {
            "search": search_name,
            "take": 10,
            "sortProperties": [
                {
                    "name": "createdDate",
                    "descending": True
                }
            ]
        }

        # Получаем список пользователей
        search_user = self.post_users_filter(search_body)

        return search_user

    @allure.step('Количество созданных пользователей по имени')
    def search_users_count(self, search_name=None):

        # Формируем тело запроса для поиска пользователей
        search_body = {
            "search": search_name
        }

        search_count = self.post_users_filter_count(search_body)
        count = search_count['totalCount']

        return count

    @allure.step('Список из id созданных пользователей')
    def search_id_users(self, search=None):

        # Формируем тело запроса для поиска пользователей
        search_body = {
            "search": search,
            "take": 10,
            "sortProperties": [
                {
                    "name": "createdDate",
                    "descending": True
                }
            ]
        }

        # Получаем список пользователей
        search_users = self.post_users_filter(search_body)

        # Формируем список id из всех найденых пользователей
        users_list_id = []
        for item in search_users['items']:
            users_list_id.append(item['id'])

        return users_list_id

    @allure.step('Активация аккаунта пользователя')
    def active_user(self, user_id):

        # Смена статуса
        active_body = self.put_users_id_change_status(user_id, params={'accountInputStatus': 'Active'})

        return active_body

    @allure.step('Изменение статуса аккаунта пользователя')
    def change_status_block_active_user(self, user_id, users_status):

        # Смена статуса
        change_status = self.put_users_id_change_status(user_id, params=users_status)

        return change_status

    @allure.step('Изменение настройки пользователя - скрыть личные данные')
    def change_settings_personal_info_user(self, user_id, personal_info):

        # Включение/выключения настройки
        settings = self.put_users_id_settings(user_id, personal_info)

        return settings

    # Поиск необходимых пользователей для редактирования
    def search_users_for_change(self):

        # Формируем тело запроса
        search_body = {
            "search": "automationTestApi",
            "skip": 0,
            "take": 10,
            "status": [
                "Working"
            ]
        }

        # Получаем пользователей с помощью поиска
        users = self.post_users_filter(search_body)
        # Список необходимых пользователей
        logins = ['automation_api_test_178', 'api.test.manager', 'api.test.newmanager', 'api.test.alternate', 'api.test.new.alternate']

        # Формируем список необходимых пользователей из поиска
        # Пробегаемся по списку logins
        for login in logins:
            # Пробегаемся по списку users
            for user in users['items']:

                if user['login'] == login:
                    self.manager.group_data.data_for_adding_user['test_users'][login] = user
                    break

    # Поиск необходимых организации для редактирования
    def search_organization_for_change(self):

        # Формируем тело запроса
        search_body = {
            "search": "automationTestApi",
            "skip": 0,
            "take": 10
        }

        # Получаем организации с помощью поиска
        organizations = self.manager.api_organizations.post_organizations_filter(search_body)
        # Список необходимых организации
        names = ['organization_automationTestApi', 'new_organization_automationTestApi']

        # Формируем список необходимых организации из поиска
        for name in names:
            for organization in organizations['items']:
                if organization['name'] == name:
                    self.manager.group_data.data_for_adding_user['organizations'][name] = organization
                    break

    # Поиск необходимых отделов для редактирования
    def search_departments_for_change(self):

        # Формируем тело запроса
        search_body = {
            "search": "automationTestApi",
            "skip": 0,
            "take": 10
        }

        # Получаем отделы с помощью поиска
        departments = self.manager.api_departments.post_departments_filter(search_body)
        # Список необходимых отделов
        names = ['department_automationTestApi', 'new_department_automationTestApi']

        # Формируем список необходимых организации из поиска
        for name in names:
            for department in departments['items']:
                if department['name'] == name:
                    self.manager.group_data.data_for_adding_user['departments'][name] = department
                    break

    # Поиск необходимых должностей для редактирования
    def search_positions_for_change(self):

        # Формируем тело запроса
        search_body = {
            "search": "automationTestApi",
            "skip": 0,
            "take": 10
        }

        # Получаем должности с помощью поиска
        positions = self.manager.api_positions.post_positions_filter(search_body)
        # Список необходимых должностей
        names = ['position_automationTestApi', 'new_position_automationTestApi']

        # Формируем список необходимых должностей из поиска
        for name in names:
            for position in positions['items']:
                if position['name'] == name:
                    self.manager.group_data.data_for_adding_user['positions'][name] = position
                    break

    # Поиск необходимых адрессов для редактирования
    def search_addresses_for_change(self):

        # Формируем тело запроса
        search_body = {
            "search": "automationTestApi",
            "skip": 0,
            "take": 10
        }

        # Получаем адресса с помощью поиска
        addresses = self.manager.api_addresses.post_addresses_filter(search_body)
        # Список необходимых адрессов
        names = ['address_automationTestApi', 'new_address_automationTestApi']

        # Формируем список необходимых адрессов из поиска
        for name in names:
            for address in addresses['items']:
                if address['name'] == name:
                    self.manager.group_data.data_for_adding_user['addresses'][name] = address
                    break

    # Поиск необходимых фотографии для редактирования
    def search_photo_id_for_change(self):

        # Формируем тело запроса
        search_body = {
            "search": "avatar_automationTestApi",
            "skip": 0,
            "take": 10
        }

        # Получаем фотографии с помощью поиска
        photos = self.manager.api_file_manager_files_list.post_files_list_filter(search_body)
        # Список необходимых фотографии
        names = ['avatar_automationTestApi', 'new_avatar_automationTestApi']

        # Формируем список необходимых фотографии из поиска
        for name in names:
            for photo in photos['filesMetadata']:
                if photo['name'] == name:
                    self.manager.group_data.data_for_adding_user['photos'][name] = photo
                    break