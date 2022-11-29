import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - ResponsibilityGroup')
@allure.story('Группы ответственности')
class TestApiResponsibilityGroup(ApiBase):

    # Изначально логинимся под модератором
    def setup_method(self):
        self.APP.api_token.get_token('SystemOperator')

    @allure.title('Создание группы ответственности')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_create_responsibility_group(self):
        # Ищем нужную ГО
        parent_responsibility_group = self.APP.api_actions_in_responsibility_groups.search_responsibility_group('AutomationApiTest')
        # Создаем группу ответственности
        responsibility_group = self.APP.api_actions_in_responsibility_groups.create_responsibility_group(
            parent_responsibility_group['items'][0]['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert responsibility_group['parentId'] == parent_responsibility_group['items'][0]['id']
        assert responsibility_group['isActive']
        assert not responsibility_group['isDeleted']
        # TODO у созданной ГО только родитель должен быть ? ... добавить проверки остальных полей

    @allure.title('Создание группы ответственности с диспетчером')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_create_responsibility_group_with_dispatcher(self):
        # Ищем нужную ГО
        parent_responsibility_group = self.APP.api_actions_in_responsibility_groups.search_responsibility_group('AutomationApiTest')
        # Создаем группу ответственности с диспетчером
        responsibility_group = self.APP.api_actions_in_responsibility_groups.create_responsibility_group_with_dispatcher(
            parent_responsibility_group['items'][0]['id'], 'test_Boss03', 'test_user06')

        dispatcher_id = responsibility_group['dispatcherUserId']

        # Сравниваем получаемые значения с ожидаемыми
        assert responsibility_group['parentId'] == parent_responsibility_group['items'][0]['id']
        assert responsibility_group['dispatcherUserId'] == dispatcher_id
        assert responsibility_group['isActive']
        assert not responsibility_group['isDeleted']
        # TODO у созданной ГО только родитель должен быть ? ... добавить проверки остальных полей

    @allure.title('Добавление пользователя в ГО')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_add_user_in_responsibility_group(self):
        # Ищем нужную ГО
        parent_responsibility_group = self.APP.api_actions_in_responsibility_groups.search_responsibility_group('AutomationApiTest')
        # Создаем группу ответственности
        responsibility_group = self.APP.api_actions_in_responsibility_groups.create_responsibility_group(parent_responsibility_group['items'][0]['id'])
        # добавляем пользователя в ГО
        self.APP.api_actions_in_responsibility_groups.add_user_in_responsibility_group(
            self.APP.group_data.users['test_user01']['user_id'], responsibility_group['id'])

        # Ищем пользователя в ГО
        user_in_responsibility_group = self.APP.api_actions_in_responsibility_groups.search_user_in_responsibility_group(
            'UserOne Test', responsibility_group['id'])

        # Сравниваем получаемые значения с ожидаемыми
        assert user_in_responsibility_group['items'][0]['id'] == self.APP.group_data.users['test_user01']['user_id']
        assert len(user_in_responsibility_group['items']) == 1

    @allure.title('Удаление пользователя из ГО')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_delete_user_from_responsibility_group(self):
        # Ищем нужную ГО
        parent_responsibility_group = self.APP.api_actions_in_responsibility_groups.search_responsibility_group('AutomationApiTest')
        # Создаем группу ответственности
        responsibility_group = self.APP.api_actions_in_responsibility_groups.create_responsibility_group(parent_responsibility_group['items'][0]['id'])
        # добавляем пользователя в ГО
        self.APP.api_actions_in_responsibility_groups.add_user_in_responsibility_group(self.APP.group_data.users['test_user01']['user_id'],
            responsibility_group['id'])

        # Удаляем пользователя из ГО
        self.APP.api_actions_in_responsibility_groups.delete_user_onto_responsibility_group(
            self.APP.group_data.users['test_user01']['user_id'], responsibility_group['id'])

        # Ищем пользователя в ГО
        user_in_responsibility_group = self.APP.api_actions_in_responsibility_groups.search_user_in_responsibility_group(
            'UserOne Test', responsibility_group['id'])

        # Сравниваем получаемые значения с ожидаемыми
        assert user_in_responsibility_group['items'] == []

    @allure.title('Редактирование группы ответственности (Изменение статуса)')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_edit_responsibility_group(self):
        # Ищем нужную ГО
        parent_responsibility_group = self.APP.api_actions_in_responsibility_groups.search_responsibility_group('AutomationApiTest')
        # Создаем группу ответственности
        responsibility_group = self.APP.api_actions_in_responsibility_groups.create_responsibility_group(parent_responsibility_group['items'][0]['id'])
        assert responsibility_group['isActive'] == True

        # Редактируем группу ответственности
        responsibility_group = self.APP.api_actions_in_responsibility_groups.edit_status_in_responsibility_group(responsibility_group['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert responsibility_group['isActive'] == False

    @allure.title('Удаление группы ответственности')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_delete_responsibility_group(self):
        # Ищем нужную ГО
        parent_responsibility_group = self.APP.api_actions_in_responsibility_groups.search_responsibility_group('AutomationApiTest')
        # Создаем группу ответственности
        responsibility_group = self.APP.api_actions_in_responsibility_groups.create_responsibility_group(parent_responsibility_group['items'][0]['id'])
        # Удаляем группу ответственности
        responsibility_group = self.APP.api_actions_in_responsibility_groups.delete_responsibility_group(responsibility_group['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert responsibility_group['isDeleted']

    @allure.title('Перемещение группы ответственности')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_move_responsibility_group(self):
        # Ищем нужную ГО
        parent_responsibility_group = self.APP.api_actions_in_responsibility_groups.search_responsibility_group('AutomationApiTest')
        # Создаем группу ответственности
        responsibility_group = self.APP.api_actions_in_responsibility_groups.create_responsibility_group(parent_responsibility_group['items'][0]['id'])
        # Ищем нужную ГО
        parent_responsibility_group = self.APP.api_actions_in_responsibility_groups.search_responsibility_group('AutoApiTest')
        # Перемещаем группу ответственности
        responsibility_group = self.APP.api_actions_in_responsibility_groups.move_responsibility_group(
            parent_responsibility_group['items'][0]['id'], responsibility_group['id'])
        # Сравниваем получаемые значения с ожидаемыми
        assert responsibility_group['parentId'] == parent_responsibility_group['items'][0]['id']

    @allure.title('Переименование группы ответственности')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_rename_responsibility_group(self):

        # Ищем нужную ГО
        parent_responsibility_group = self.APP.api_actions_in_responsibility_groups.search_responsibility_group('AutomationApiTest')

        # Создаем группу ответственности
        responsibility_group = self.APP.api_actions_in_responsibility_groups.create_responsibility_group(parent_responsibility_group['items'][0]['id'])

        # Создаем новое имя группы ответственности
        new_rg_name = 'AutomationApiTest ' + self.APP.time.get_date_time_Y_m_d_H_M_S()

        # Переименуем группу ответственности
        responsibility_group = self.APP.api_actions_in_responsibility_groups.rename_responsibility_group(responsibility_group['id'], new_rg_name)

        # Сравниваем получаемые значения с ожидаемыми
        assert responsibility_group['name'] == new_rg_name

    @allure.title('Поиск группы ответственности')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_search_responsibility_group(self):

        # Ищем нужную ГО
        parent_responsibility_group = self.APP.api_actions_in_responsibility_groups.search_responsibility_group('AutomationApiTest')

        # Создаем группу ответственности
        responsibility_group = self.APP.api_actions_in_responsibility_groups.create_responsibility_group(parent_responsibility_group['items'][0]['id'])

        # Проверяем, нашлась ли нужная группа ответственности
        rg_search = self.APP.api_actions_in_responsibility_groups.find_responsibility_group_in_search(responsibility_group['name'])

        assert rg_search is True

    @allure.title('Проверка соответствия списка услуг к ГО')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_check_service_catalogs_in_rg(self):

        # Ищем нужную ГО
        parent_responsibility_group = self.APP.api_actions_in_responsibility_groups.search_responsibility_group('AutomationApiTest')

        # Ищем родительскую услугу
        parent_service_search = self.APP.api_actions_in_service_catalog.search_service_catalog_with_filter('Automation service catalogs test')

        # Выбираем нужную услугу
        service_id = self.APP.api_actions_in_service_catalog.choose_service_with_treepathname(parent_service_search)

        # Создание услуги
        service_create = self.APP.api_actions_in_service_catalog.create_service(parent_responsibility_group['items'][0]['id'], service_id)

        # Проверяем, прикреплена ли данная услуга к ГО
        check = self.APP.api_actions_in_service_catalog.check_service(parent_responsibility_group['items'][0]['id'],service_create)

        assert check is True
