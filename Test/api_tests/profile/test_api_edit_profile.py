import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Profile')
@allure.story('Редактирование профиля')
class TestApiEditProfile(ApiBase):

    # Изначально логинимся под 15 пользователем
    def setup_method(self):
        self.APP.api_token.get_token('test_user15')

    # Сброс всех полей к дефолт значениям
    def teardown_method(self):
        self.APP.api_actions_in_profile.set_default_values(self.users['test_user15']['user_id'])

    @allure.title('Изменить фамилию пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_change_second_name(self):

        # Меняем фамилию пользователя
        user = self.APP.api_actions_in_profile.change_second_name('SurnameChanged', self.users['test_user15']['user_id'])

        assert user['surname'] == 'SurnameChanged'

    @allure.title('Изменить имя пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_change_first_name(self):

        # Меняем имя пользователя
        user = self.APP.api_actions_in_profile.change_first_name('NameChanged', self.users['test_user15']['user_id'])

        assert user['name'] == 'NameChanged'

    @allure.title('Изменить отчество пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_change_middle_name(self):

        # Меняем отчество пользователя
        user = self.APP.api_actions_in_profile.change_middle_name('NameChanged', self.users['test_user15']['user_id'])

        assert user['middleName'] == 'NameChanged'

    @allure.title('Изменить моб. телефон пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_change_mobile_phone(self):

        # Меняем мобильный телефон пользователя
        user = self.APP.api_actions_in_profile.change_mobile_phone('123789456', self.users['test_user15']['user_id'])

        assert user['mobilePhone'] == '123789456'

    @allure.title('Изменить email пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_change_email(self):

        # Меняем email пользователя
        user = self.APP.api_actions_in_profile.change_email('testMail@gandiva.ru', self.users['test_user15']['user_id'])

        assert user['email'] == 'testMail@gandiva.ru'

    @allure.title('Изменить руководителя пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_change_manager(self):

        # Меняем руководителя пользователя
        user = self.APP.api_actions_in_profile.change_manager(self.users['test_Boss03']['user_id'], self.users['test_user15']['user_id'])

        assert user['manager']['id'] == self.users['test_Boss03']['user_id']

    @allure.title('Изменить заместителя пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_change_alternate(self):

        # Меняем заместителя пользователя
        user = self.APP.api_actions_in_profile.change_alternate(self.users['test_Boss03']['user_id'], self.users['test_user15']['user_id'])

        assert user['alternate']['id'] == self.users['test_Boss03']['user_id']

    @allure.title('Изменить отдел пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_change_department(self):

        # Логинимся под пользователем с правами модератора
        self.APP.api_token.get_token()

        # Получаем id отдела
        department_id = self.APP.api_actions_in_profile.get_department_id('Отдел тестирования')

        # Меняем отдел пользователя
        user = self.APP.api_actions_in_profile.change_department(department_id, self.users['test_user15']['user_id'])

        assert user['department']['id'] == department_id

    @allure.title('Изменить организацию пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_change_organization(self):

        # Логинимся под пользователем с правами модератора
        self.APP.api_token.get_token()

        # Получаем id организации
        organization_id = self.APP.api_actions_in_profile.get_organization_id('Протон ООО')

        # Меняем организацию пользователя
        user = self.APP.api_actions_in_profile.change_organization(organization_id, self.users['test_user15']['user_id'])

        assert user['organization']['id'] == organization_id

    @allure.title('Изменить должность пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_change_position(self):

        # Логинимся под пользователем с правами модератора
        self.APP.api_token.get_token()

        # Получаем id должности
        position_id = self.APP.api_actions_in_profile.get_position_id('Инженер по тестированию')

        # Меняем должность пользователя
        user = self.APP.api_actions_in_profile.change_position(position_id, self.users['test_user15']['user_id'])

        assert user['position']['id'] == position_id

    @allure.title('Изменить адрес пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_change_address(self):

        # Логинимся под пользователем с правами модератора
        self.APP.api_token.get_token()

        # Получаем id адреса
        address_id = self.APP.api_actions_in_profile.get_addresses_id('Нижний Новгород')

        # Меняем фактический адрес пользователя
        user = self.APP.api_actions_in_profile.change_address(address_id, self.users['test_user15']['user_id'])

        assert user['actualAddress']['id'] == address_id

    @allure.title('Изменить юридический адрес пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_change_legal_address(self):

        # Логинимся под пользователем с правами модератора
        self.APP.api_token.get_token()

        # Получаем id адреса
        address_id = self.APP.api_actions_in_profile.get_addresses_id('Нижний Новгород')

        # Меняем юридический адрес пользователя
        user = self.APP.api_actions_in_profile.change_legal_address(address_id, self.users['test_user15']['user_id'])

        assert user['legalAddress']['id'] == address_id

    @allure.title('Изменить городской телефон пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_change_email(self):

        # Меняем городской телефон пользователя
        user = self.APP.api_actions_in_profile.change_city_phone('123123', self.users['test_user15']['user_id'])

        assert user['cityPhone'] == '123123'

    @allure.title('Изменить внутренний телефон пользователя')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_change_email(self):

        # Меняем внутренний телефон пользователя
        user = self.APP.api_actions_in_profile.change_internal_phone('123123', self.users['test_user15']['user_id'])

        assert user['internalPhone'] == '123123'
