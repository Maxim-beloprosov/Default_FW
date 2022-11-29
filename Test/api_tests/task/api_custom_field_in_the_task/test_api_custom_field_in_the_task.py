import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Task')
@allure.story('Задачи. Работа с доп. полями.')
class TestApiCustomFieldInTheTask(ApiBase):

    test_data = [
        ('Текст', 'Text', None, 'ApiTestCustomField Text'),
        ('Дата', 'Date', None, '2022-07-18T00:00:00Z'),
        ('Справочник "Пользователи"', 'UserDictionary', None, {'id': '96ba2212-bb12-11ec-8ed5-0217dc7a50e7'})
    ]

    @allure.title('Создание задачи с различными типами доп. полей ({field_name})')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('field_name, field_type, value, correct_value', test_data)
    def test_create_task_with_custom_field(self, field_name, field_type, value, correct_value):
        # Создаем задачу с доп. полем
        task = self.create_task_with_custom_field(field_name, field_type, value)
        # Получаем список доп. полей в задаче
        custom_field_list = self.APP.api_task_custom_field_collection.get_task_custom_field_collection_id(task['id'])
        assert custom_field_list[0]['name'] == field_name
        assert custom_field_list[0]['data']['type'] == field_type

    @allure.title('Редактирование значений доп. полей в задаче в статусе "В работе" ({field_name})')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('field_name, field_type, value, correct_value', test_data)
    def test_edit_values_custom_field_in_task_with_status_work(self, field_name, field_type, value, correct_value):
        # Создаем задачу с доп. полем
        task = self.create_task_with_custom_field(field_name, field_type, value)
        # Получаем список доп. полей в задаче
        custom_field_list = self.APP.api_task_custom_field_collection.get_task_custom_field_collection_id(task['id'])
        # Редактируем значения в доп. полях
        custom_field = self.APP.api_actions_in_task_with_custom_field.edit_values_in_custom_field_from_task(task['id'], custom_field_list[0]['id'], field_type, correct_value)
        assert custom_field[0]['id'] == custom_field_list[0]['id']
        assert custom_field[0]['data']['type'] == field_type
        if field_type == 'Text' or field_type == 'Date':
            assert custom_field[0]['data']['value'] == correct_value
        else:
            assert custom_field[0]['data']['value']['id'] == correct_value['id']

    @allure.title('Удаление доп. поля из задачи')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_delete_custom_field_in_task(self):
        # Создаем задачу с доп. полем
        task = self.create_task_with_custom_field('Текст', 'Text', None)
        # Получаем список доп. полей в задаче
        custom_field_list = self.APP.api_task_custom_field_collection.get_task_custom_field_collection_id(task['id'])
        # Удаляем доп. поле
        custom_field = self.APP.api_task_custom_field_collection.put_task_custom_field_collection_id(task['id'], [{'id': custom_field_list[0]['id'], 'isDelete': True}])
        assert not custom_field

    @allure.title('Добавление доп. поля после создания задачи')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('field_name, field_type, value, correct_value', test_data)
    def test_add_custom_field_in_task_after_create(self, field_name, field_type, value, correct_value):
        # Создаем задачу
        task = self.create_task()
        # Добавляем доп. поле
        self.APP.api_actions_in_task_with_custom_field.add_custom_field_in_task(task['id'], field_name, field_type, value)
        # Получаем список доп. полей в задаче
        custom_field_list = self.APP.api_task_custom_field_collection.get_task_custom_field_collection_id(task['id'])
        assert custom_field_list[0]['name'] == field_name
        assert custom_field_list[0]['data']['type'] == field_type

    @allure.title('Редактирование значений доп. полей в задаче исполнителем в статусе "На согласовании"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('field_name, field_type, value, correct_value', test_data)
    def test_edit_values_custom_field_in_task_contractor_in_status_agreement(self, field_name, field_type, value, correct_value):
        # Создаем задачу с доп. полем
        task = self.create_task_with_custom_field(field_name, field_type, value)
        # Добавляем согласующего
        task = self.APP.api_actions_in_task.add_agreements_in_task(self.APP.group_data.users['test_user03']['user_id'], task['syncToken'], task['id'])
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Получаем список доп. полей в задаче
        custom_field_list = self.APP.api_task_custom_field_collection.get_task_custom_field_collection_id(task['id'])
        # Редактируем значения в доп. полях
        custom_field = self.APP.api_actions_in_task_with_custom_field.edit_values_in_custom_field_from_task(task['id'], custom_field_list[0]['id'], field_type, correct_value)
        assert custom_field[0]['id'] == custom_field_list[0]['id']
        assert custom_field[0]['data']['type'] == field_type
        if field_type == 'Text' or field_type == 'Date':
            assert custom_field[0]['data']['value'] == correct_value
        else:
            assert custom_field[0]['data']['value']['id'] == correct_value['id']

    @allure.title('Редактирование значений доп. полей в задаче исполнителем в статусе "В работе"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('field_name, field_type, value, correct_value', test_data)
    def test_edit_values_custom_field_in_task_contractor_in_status_work(self, field_name, field_type, value, correct_value):
        # Создаем задачу с доп. полем
        task = self.create_task_with_custom_field(field_name, field_type, value)
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Получаем список доп. полей в задаче
        custom_field_list = self.APP.api_task_custom_field_collection.get_task_custom_field_collection_id(task['id'])
        # Редактируем значения в доп. полях
        custom_field = self.APP.api_actions_in_task_with_custom_field.edit_values_in_custom_field_from_task(task['id'], custom_field_list[0]['id'], field_type, correct_value)
        assert custom_field[0]['id'] == custom_field_list[0]['id']
        assert custom_field[0]['data']['type'] == field_type
        if field_type == 'Text' or field_type == 'Date':
            assert custom_field[0]['data']['value'] == correct_value
        else:
            assert custom_field[0]['data']['value']['id'] == correct_value['id']

    @allure.title('Редактирование значений доп. полей в задаче исполнителем в статусе "На уточнении у исп."')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('field_name, field_type, value, correct_value', test_data)
    def test_edit_values_custom_field_in_task_contractor_in_status_clarification_contractor(self, field_name, field_type, value, correct_value):
        # Создаем задачу с доп. полем
        task = self.create_task_with_custom_field(field_name, field_type, value)
        # Добавляем согласующего
        task = self.APP.api_actions_in_task.add_agreements_in_task(self.APP.group_data.users['test_user03']['user_id'], task['syncToken'], task['id'])
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Задаем вопрос-уточнение исполнителю
        task = self.APP.api_actions_in_task.clarification_ask_to_contractor_in_task(task['syncToken'], task['id'])
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Получаем список доп. полей в задаче
        custom_field_list = self.APP.api_task_custom_field_collection.get_task_custom_field_collection_id(task['id'])
        # Редактируем значения в доп. полях
        custom_field = self.APP.api_actions_in_task_with_custom_field.edit_values_in_custom_field_from_task(task['id'], custom_field_list[0]['id'], field_type, correct_value)
        assert custom_field[0]['id'] == custom_field_list[0]['id']
        assert custom_field[0]['data']['type'] == field_type
        if field_type == 'Text' or field_type == 'Date':
            assert custom_field[0]['data']['value'] == correct_value
        else:
            assert custom_field[0]['data']['value']['id'] == correct_value['id']

    @allure.title('Редактирование значений доп. полей в задаче исполнителем в статусе "На уточнении у иниц."')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('field_name, field_type, value, correct_value', test_data)
    def test_edit_values_custom_field_in_task_contractor_in_status_clarification_initiator(self, field_name, field_type, value, correct_value):
        # Создаем задачу с доп. полем
        task = self.create_task_with_custom_field(field_name, field_type, value)
        # Добавляем согласующего
        task = self.APP.api_actions_in_task.add_agreements_in_task(self.APP.group_data.users['test_user03']['user_id'],
                                                                   task['syncToken'], task['id'])
        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user03')
        # Задаем вопрос-уточнение инициатору
        task = self.APP.api_actions_in_task.clarification_ask_to_initiator_in_task(task['syncToken'], task['id'])
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Получаем список доп. полей в задаче
        custom_field_list = self.APP.api_task_custom_field_collection.get_task_custom_field_collection_id(task['id'])
        # Редактируем значения в доп. полях
        custom_field = self.APP.api_actions_in_task_with_custom_field.edit_values_in_custom_field_from_task(task['id'], custom_field_list[0]['id'], field_type, correct_value)
        assert custom_field[0]['id'] == custom_field_list[0]['id']
        assert custom_field[0]['data']['type'] == field_type
        if field_type == 'Text' or field_type == 'Date':
            assert custom_field[0]['data']['value'] == correct_value
        else:
            assert custom_field[0]['data']['value']['id'] == correct_value['id']

    @allure.title('Редактирование значений доп. полей в задаче исполнителем в статусе "В проверке"')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Мещеряков Евгений Евгеньевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('field_name, field_type, value, correct_value', test_data)
    def test_edit_values_custom_field_in_task_contractor_in_status_resolved(self, field_name, field_type, value, correct_value):
        # Создаем задачу с доп. полем
        task = self.create_task_with_custom_field(field_name, field_type, value)
        # Перелогиниваемся на исполнителя
        self.APP.api_token.get_token('test_user02')
        # Отправляем задачу в проверку
        self.APP.api_actions_in_task.resolve_task(task['syncToken'], task['id'])
        # Получаем список доп. полей в задаче
        custom_field_list = self.APP.api_task_custom_field_collection.get_task_custom_field_collection_id(task['id'])
        # Редактируем значения в доп. полях
        custom_field = self.APP.api_actions_in_task_with_custom_field.edit_values_in_custom_field_from_task(task['id'], custom_field_list[0]['id'], field_type, correct_value)
        assert custom_field[0]['id'] == custom_field_list[0]['id']
        assert custom_field[0]['data']['type'] == field_type
        if field_type == 'Text' or field_type == 'Date':
            assert custom_field[0]['data']['value'] == correct_value
        else:
            assert custom_field[0]['data']['value']['id'] == correct_value['id']
