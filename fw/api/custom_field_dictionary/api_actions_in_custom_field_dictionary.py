import allure

from fw.api.custom_field_dictionary.api_custom_field_dictionary import ApiCustomFieldDirectory


class ActionsInCustomFieldDirectory(ApiCustomFieldDirectory):

    @allure.title('Создание пользовательского справочника')
    def create_custom_field_dictionary(self, value_type="Text"):

        # Подготовка тела для создания пользовательского справочника
        custom_field_body = {
            "name": 'AutomationApiTest ' + self.manager.time.get_date_time_Y_m_d_H_M_S(),
            "isActive": True,
            "createdFields": [
                {
                    "isObligatory": True,
                    "isForSearch": True,
                    "isForShow": True,
                    "data": {
                        "value": 'AutomationApiTestValue ' + self.manager.time.get_date_time_Y_m_d_H_M_S(),
                        "type": value_type
                    },
                    "name": 'AutomationApiTest2 ' + self.manager.time.get_date_time_Y_m_d_H_M_S(),
                    "isActive": True,
                    "orderNumber": 0,
                }
            ]
        }

        # Создаем пользовательский справочник
        create_custom_field_directory = self.post_custom_field_dictionary(custom_field_body)

        return create_custom_field_directory

    @allure.title('Редактирование пользовательского справочника')
    def change_custom_field_dictionary(self, custom_field_directory, name='AutomationApiTest ', isActive=True,
                                      value='AutomationApiTestValue ', value_type="Text", created_field_name='name'):

        # Подготовка тела для создания пользовательского справочника
        change_custom_field_body = {
            "name": name + self.manager.time.get_date_time_Y_m_d_H_M_S(),
            "isActive": isActive,
            "createdFields": [
                {
                    "isObligatory": True,
                    "isForSearch": True,
                    "isForShow": True,
                    "data": {
                        "value": value + self.manager.time.get_date_time_Y_m_d_H_M_S(),
                        "type": value_type
                    },
                    "name": created_field_name,
                    "isActive": True,
                    "orderNumber": 0,
                }
            ]
        }

        # Изменяем данные пользовательского справочника
        custom_field_directory = self.put_custom_field_dictionary(custom_field_directory['id'], change_custom_field_body)

        return custom_field_directory

    @allure.title('Добавление значений в пользовательский справочник')
    def add_value_to_custom_field_dictionary(self, custom_field_dictionary_id, custom_fields_id, text_value=None):

        if text_value == None:
            # Подготовка данных для добавления значения
            text_value = "TestValue AutomationApiTest " + self.manager.time.get_date_time_Y_m_d_H_M_S()

        # Формируем тело запроса для добавления значения в пользовательский справочник
        add_value_body = [
            {
                "rowValues": [
                    {
                        "type": "Text",
                        "fieldId": custom_fields_id,
                        "value": text_value
                    }
                ]
            }
        ]

        # Добавляем значение в пользовательский справочник
        add_value_custom = self.post_update_field_dictionary(custom_field_dictionary_id, add_value_body)

        return add_value_custom

    @allure.title('Удаление значений в пользовательский справочник')
    def delete_value_to_custom_field_dictionary(self, custom_field_dictionary_id, rowId_id):

        # Формируем тело запроса для удаления значения в пользовательском справочнике
        delete_value_body = [
            {
                "rowId": rowId_id,
                "isDelete": True,
                "rowValues": []
            }
        ]

        # Удаляем значение из пользовательского справочника
        delete_value_custom = self.post_update_field_dictionary(custom_field_dictionary_id, delete_value_body)

        return delete_value_custom

    @allure.title('Редактирование значений в пользовательский справочник')
    def edit_value_to_custom_field_dictionary(self, custom_field_dictionary_id, customFields_id, rowId_id, text_value=None):

        if text_value == None:
            # Подготовка данных для добавления значения
            text_value = "TestValue AutomationApiTest " + self.manager.time.get_date_time_Y_m_d_H_M_S()

        # Формируем тело запроса для редактирования значения в пользовательском справочнике
        edit_value_body = [
            {
                "rowId": rowId_id,
                "rowValues": [
                    {
                        "type": "Text",
                        "fieldId": customFields_id,
                        "value": text_value
                    }
                ]
            }
        ]

        # Редактируем значение в пользовательский справочник
        edit_value_custom = self.post_update_field_dictionary(custom_field_dictionary_id, edit_value_body)

        return edit_value_custom

    @allure.title('Список значений в пользовательском справочнике с учетом фильтра')
    def search_value_to_custom_field_dictionary(self, custom_field_dictionary_id, search=None, skip=0, take=20):

        # Формируем тело запроса для поиска значений в пользовательском справочнике
        search_value_body = {
                "search": search,
                "skip": skip,
                "take": take
            }

        # Получаем список созданных значении из пользовательского справочника
        search_value_custom = self.post_search_values_of_custom_field_dictionary(custom_field_dictionary_id, search_value_body)

        return search_value_custom

    @allure.title('Отдельный список из id значений')
    def search_id_value_to_custom_field_dictionary(self, custom_field_dictionary_id, search=None, skip=0, take=20):
        # Формируем тело запроса для поиска значений в пользовательском справочнике
        search_value_body = {
            "search": search,
            "skip": skip,
            "take": take
        }

        # Получаем список созданных значении из пользовательского справочника
        search_value_custom = self.post_search_values_of_custom_field_dictionary(custom_field_dictionary_id, search_value_body)

        # Выносим id значений в отдельный список
        list_id_value = []
        for item in search_value_custom['items']:
            list_id_value.append(item['rowId'])

        return list_id_value