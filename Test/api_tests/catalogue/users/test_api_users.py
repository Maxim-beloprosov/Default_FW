import allure
import pytest

from Test.api_tests.api_base import ApiBase

@allure.feature('Api - Users')
@allure.story('Создание и редактирование пользователя(сотрудника)')
class TestApiUsers(ApiBase):

    # Подготовка значении для тестов
    def setup_class(self):
        self.APP.api_actions_users.search_users_for_change()
        self.APP.api_actions_users.search_organization_for_change()
        self.APP.api_actions_users.search_departments_for_change()
        self.APP.api_actions_users.search_positions_for_change()
        self.APP.api_actions_users.search_addresses_for_change()
        self.APP.api_actions_users.search_photo_id_for_change()

    # Изначально логинимся под модератором
    def setup_method(self):
        self.APP.api_token.get_token('SystemOperator')

    # Сброс всех полей к дефолтным значениям
    def teardown_method(self):
        self.APP.api_actions_users.user_default_fields(self.APP.group_data.data_for_adding_user['test_users']['automation_api_test_178']['id'])

    @allure.title('Создание пользователя - с обязательными полями')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Хикматов Рустем Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_add_user_with_required_fields(self):

        data_value = {
            'login': self.APP.group_data.data_for_adding_user['test_users']['test_user']['login'],
            'name': self.APP.group_data.data_for_adding_user['test_users']['test_user']['name'],
            'surname': self.APP.group_data.data_for_adding_user['test_users']['test_user']['surname']
        }

        # Получаем количество созданных пользователей по имени
        search_count = self.APP.api_actions_users.search_users_count(search_name='testName')

        # Создаем пользователя с обязательными полями
        add_user = self.APP.api_actions_users.add_user(search_count, data_value)

        # Проверяем наличие созданого пользователя в списке
        assert add_user['login'] == data_value['login'] + str(search_count)
        assert add_user['name'] == data_value['name']
        assert add_user['surname'] == data_value['surname']

    @allure.title('Создание пользователя - со всеми полями')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Хикматов Рустем Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_add_user_with_all_fields(self):

        data_value = {
            'login': self.APP.group_data.data_for_adding_user['test_users']['test_user']['login'],
            'name': self.APP.group_data.data_for_adding_user['test_users']['test_user']['name'],
            'surname': self.APP.group_data.data_for_adding_user['test_users']['test_user']['surname'],
            'middleName': self.APP.group_data.data_for_adding_user['test_users']['test_user']['middleName'],
            'photoId': self.APP.group_data.data_for_adding_user['photos']['avatar_automationTestApi']['id'],
            'email': self.APP.group_data.data_for_adding_user['test_users']['test_user']['email'],
            'mobilePhone': self.APP.group_data.data_for_adding_user['test_users']['test_user']['mobilePhone'],
            'managerId': self.APP.group_data.data_for_adding_user['test_users']['api.test.manager']['id'],
            'alternateId': self.APP.group_data.data_for_adding_user['test_users']['api.test.alternate']['id'],
            'organizationId': self.APP.group_data.data_for_adding_user['organizations']['organization_automationTestApi']['id'],
            'departmentId': self.APP.group_data.data_for_adding_user['departments']['department_automationTestApi']['id'],
            'positionId': self.APP.group_data.data_for_adding_user['positions']['position_automationTestApi']['id'],
            'actualAddressId': self.APP.group_data.data_for_adding_user['addresses']['address_automationTestApi']['id'],
            'legalAddressId': self.APP.group_data.data_for_adding_user['addresses']['address_automationTestApi']['id'],
            'cityPhone': self.APP.group_data.data_for_adding_user['test_users']['test_user']['cityPhone'],
            'internalPhone': self.APP.group_data.data_for_adding_user['test_users']['test_user']['internalPhone']
        }

        # Получаем количество созданных пользователей по имени
        search_count = self.APP.api_actions_users.search_users_count(search_name='testName')

        # Создаем пользователя со всеми полями
        add_user = self.APP.api_actions_users.add_user(search_count, data_value)

        # Проверяем наличие созданого пользователя в списке
        assert add_user['login'] == data_value['login'] + str(search_count)
        assert add_user['name'] == data_value['name']
        assert add_user['surname'] == data_value['surname']
        assert add_user['middleName'] == data_value['middleName']
        assert add_user['photoId'] == data_value['photoId']
        assert add_user['email'] == str(search_count) + data_value['email']
        assert add_user['mobilePhone'] == data_value['mobilePhone'] + str(search_count)
        assert add_user['manager']['id'] == data_value['managerId']
        assert add_user['alternate']['id'] == data_value['alternateId']
        assert add_user['organization']['id'] == data_value['organizationId']
        assert add_user['department']['id'] == data_value['departmentId']
        assert add_user['position']['id'] == data_value['positionId']
        assert add_user['actualAddress']['id'] == data_value['actualAddressId']
        assert add_user['legalAddress']['id'] == data_value['legalAddressId']
        assert add_user['cityPhone'] == data_value['cityPhone'] + str(search_count)
        assert add_user['internalPhone'] == data_value['internalPhone'] + str(search_count)

    test_data_00 = [
        ('name'),
        ('surname')
    ]

    @allure.title('Редактирование пользователя - с обязательными полями')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Хикматов Рустем Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_fields", test_data_00)
    def test_change_user_with_required_fields(self, set_fields):

        # Получаем пользоателя по id
        user_id = self.APP.group_data.data_for_adding_user['test_users']['automation_api_test_178']['id']

        # Подготавливаем значения (ОР) для проверки (метод не используется во время редактирования)
        value_change_user = self.APP.api_actions_users.value_change_user(set_fields)

        # Редактируем созданого пользователя
        change_user = self.APP.api_actions_users.change_user(user_id, set_fields)

        # Проверяем изменения значений на новые данные
        assert change_user[set_fields] == value_change_user

    test_data_01 = [
        ('middleName'),
        ('photoId'),
        ('email'),
        ('mobilePhone'),
        ('manager'),
        ('alternate'),
        ('organization'),
        ('department'),
        ('position'),
        ('actualAddress'),
        ('legalAddress'),
        ('cityPhone'),
        ('internalPhone')
    ]

    @allure.title('Редактирование пользователя - со всеми полями')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Хикматов Рустем Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('set_fields', test_data_01)
    def test_change_user_with_all_fields(self, set_fields):

        # Получаем пользоателя по id
        user_id = self.APP.group_data.data_for_adding_user['test_users']['automation_api_test_178']['id']

        # Подготавливаем значения (ОР) для проверки (метод не используется во время редактирования)
        value_change_user = self.APP.api_actions_users.value_change_user(set_fields)

        # Редактируем созданого пользователя
        change_user = self.APP.api_actions_users.change_user(user_id, set_fields)

        # Проверяем изменения значений на новые данные
        if change_user[set_fields] != value_change_user:
            # Для проверки полей с id значениями
            assert change_user[set_fields]['id'] == value_change_user
        else:
            assert change_user[set_fields] == value_change_user

    @allure.title('Активация пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Хикматов Рустем Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_activation_user(self):

        # Создаем пользователя с обязательными полями
        add_user = self.APP.api_actions_users.add_user()

        # Смена статуса (Активация) из "Неактивный" в "Активный"
        change_status_active_user = self.APP.api_actions_users.active_user(add_user['id'])

        # Проверка статуса с ожидаемым
        assert change_status_active_user['status'] == 'Working'

    test_data_02 = [
        ({'accountInputStatus': 'Blocked'}, 'Blocked'),
        ({'accountInputStatus': 'Active'}, 'Working')
    ]

    @allure.title('Изменение статуса пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Хикматов Рустем Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_status, expected", test_data_02)
    def test_change_status_user(self, set_status, expected):

        # Получаем пользоателя по id
        user_id = self.APP.group_data.data_for_adding_user['test_users']['automation_api_test_178']['id']

        # Смена статусов Работает/Заблокирован
        user_change_status = self.APP.api_actions_users.change_status_block_active_user(user_id, set_status)

        # Проверка статуса с ожидаемым
        assert user_change_status['status'] == expected

    test_data_03 = [
        ({'hidePersonalInfo': True}, True),
        ({'hidePersonalInfo': False}, False)
    ]

    @allure.title('Изменение настроек пользователя - Скрыть личные данные')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Хикматов Рустем Владимирович')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("set_personal_info, expected", test_data_03)
    def test_change_settings_personal_info_user(self, set_personal_info, expected):

        # Получаем пользоателя по id
        user_id = self.APP.group_data.data_for_adding_user['test_users']['automation_api_test_178']['id']

        # Выключаем/Включаем настройки "Скрыть личные данные"
        change_personal_info_user = self.APP.api_actions_users.change_settings_personal_info_user(user_id, set_personal_info)

        # Проверка настроек "Скрыть личные данные" с ожидаемыми
        assert change_personal_info_user['hidePersonalInfo'] == expected