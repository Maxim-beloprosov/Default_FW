import allure

from fw.api.users.api_users import ApiUsers


class ActionsInProfile(ApiUsers):

    @allure.title('Изменить фамилию пользователя')
    def change_second_name(self, text, user_id):
        # Подготавливаем тело запроса
        body = {
            "surname": text
        }

        # Обновляем данные пользователя
        user = self.put_users_id(user_id, body)

        return user

    @allure.title('Изменить имя пользователя')
    def change_first_name(self, text, user_id):
        # Подготавливаем тело запроса
        body = {
            "name": text
        }

        # Обновляем данные пользователя
        user = self.put_users_id(user_id, body)

        return user

    @allure.title('Изменить отчество пользователя')
    def change_middle_name(self, text, user_id):
        # Подготавливаем тело запроса
        body = {
            "middleName": text
        }

        # Обновляем данные пользователя
        user = self.put_users_id(user_id, body)

        return user

    @allure.title('Изменить моб. телефон пользователя')
    def change_mobile_phone(self, text, user_id):
        # Подготавливаем тело запроса
        body = {
            "mobilePhone": text
        }

        # Обновляем данные пользователя
        user = self.put_users_id(user_id, body)

        return user

    @allure.title('Изменить email пользователя')
    def change_email(self, text, user_id):
        # Подготавливаем тело запроса
        body = {
            "email": text
        }

        # Обновляем данные пользователя
        user = self.put_users_id(user_id, body)

        return user

    @allure.title('Изменить руководителя пользователя')
    def change_manager(self, manager_id, user_id):
        # Подготавливаем тело запроса
        body = {
            "managerId": manager_id
        }

        # Обновляем данные пользователя
        user = self.put_users_id(user_id, body)

        return user

    @allure.title('Изменить заместителя пользователя')
    def change_alternate(self, alternate_id, user_id):
        # Подготавливаем тело запроса
        body = {
            "alternateId": alternate_id
        }

        # Обновляем данные пользователя
        user = self.put_users_id(user_id, body)

        return user

    @allure.title('Сбросить все поля к дефолт значениям(только test_user15)')
    def set_default_values(self, user_id):
        # Подготавливаем тело запроса
        body = {
            "email": "test_user15@mail.ru",
            "name": "Test",
            "middleName": "Automation",
            "surname": "UserFifteen",
            "mobilePhone": '+79293451230',
            "managerId": None,
            "alternateId": None,
            "departmentId": None,
            "organizationId": None,
            "positionId": None,
            "actualAddressId": None,
            "legalAddressId": None,
            "cityPhone": None,
            "internalPhone": None
        }

        # Обновляем данные пользователя
        user = self.put_users_id(user_id, body)

        return user

    @allure.title('Получить Id отдела по названию')
    def get_department_id(self, search_text):

        # Подготавливаем тело запроса
        body = {
            "take": 1,
            "search": search_text,
            "searchType": "Like"
        }

        # Получаем id отдела
        department = self.manager.api_departments.post_departments_filter(body)

        return department['items'][0]['id']

    @allure.title('Получить Id организации по названию')
    def get_organization_id(self, search_text):

        # Подготавливаем тело запроса
        body = {
            "take": 1,
            "search": search_text,
            "searchType": "Like"
        }

        # Получаем id организации
        organization = self.manager.api_organizations.post_organizations_filter(body)

        return organization['items'][0]['id']

    @allure.title('Изменить отдел пользователя')
    def change_department(self, department_id, user_id):

        # Подготавливаем тело запроса
        body = {
            "departmentId": department_id
        }

        # Обновляем данные пользователя
        user = self.put_users_id(user_id, body)

        return user

    @allure.title('Изменить организацию пользователя')
    def change_organization(self, organization_id, user_id):

        # Подготавливаем тело запроса
        body = {
            "organizationId": organization_id
        }

        # Обновляем данные пользователя
        user = self.put_users_id(user_id, body)

        return user

    @allure.title('Получить Id должности по названию')
    def get_position_id(self, search_text):

        # Подготавливаем тело запроса
        body = {
            "take": 1,
            "search": search_text,
            "searchType": "Like"
        }

        # Получаем id должности
        position = self.manager.api_positions.post_positions_filter(body)

        return position['items'][0]['id']

    @allure.title('Изменить должность пользователя')
    def change_position(self, position_id, user_id):

        # Подготавливаем тело запроса
        body = {
            "positionId": position_id
        }

        # Обновляем данные пользователя
        user = self.put_users_id(user_id, body)

        return user

    @allure.title('Получить Id адреса по названию')
    def get_addresses_id(self, search_text):

        # Подготавливаем тело запроса
        body = {
            "take": 1,
            "search": search_text,
            "searchType": "Like"
        }

        # Получаем id адреса
        address = self.manager.api_addresses.post_addresses_filter(body)

        return address['items'][0]['id']

    @allure.title('Изменить адрес пользователя')
    def change_address(self, address_id, user_id):

        # Подготавливаем тело запроса
        body = {
            "actualAddressId": address_id
        }

        # Обновляем данные пользователя
        user = self.put_users_id(user_id, body)

        return user

    @allure.title('Изменить юридический адрес пользователя')
    def change_legal_address(self, address_id, user_id):

        # Подготавливаем тело запроса
        body = {
            "legalAddressId": address_id
        }

        # Обновляем данные пользователя
        user = self.put_users_id(user_id, body)

        return user

    @allure.title('Изменить городской телефон пользователя')
    def change_city_phone(self, number, user_id):
        # Подготавливаем тело запроса
        body = {
            "cityPhone": number
        }

        # Обновляем данные пользователя
        user = self.put_users_id(user_id, body)

        return user

    @allure.title('Изменить городской телефон пользователя')
    def change_internal_phone(self, number, user_id):

        # Подготавливаем тело запроса
        body = {
            "internalPhone": number
        }

        # Обновляем данные пользователя
        user = self.put_users_id(user_id, body)

        return user
