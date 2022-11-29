import allure

from fw.api.tickets.api_task_custom_field_collection.api_task_custom_field_collection import \
    ApiTaskCustomFieldCollection


class ActionsInTaskWithCustomField(ApiTaskCustomFieldCollection):

    @allure.title('Изменить значения доп. поля в задаче')
    def edit_values_in_custom_field_from_task(self, task_id, custom_field_id, field_type, value):
        custom_field_body = [{'id': custom_field_id,
                              'data':  {
                                    'defaultSettingType': 'None',
                                    'type': field_type,
                                    'value': value,
                                    }
                              }
                             ]

        # Обновляем значение доп. поля
        custom_field = self.put_task_custom_field_collection_id(task_id, custom_field_body, params=None)

        return custom_field

    @allure.title('Добавить доп. поле в задачу')
    def add_custom_field_in_task(self, task_id, name, field_type, value):
        custom_field_body = [
                    {
                        "name": name,
                        "data": {
                            "type": field_type,
                            "value": value
                        },
                        "customFieldSources": [],
                        "orderPath": "0",
                    }
                ]

        # Добавляем доп. поле
        custom_field = self.put_task_custom_field_collection_id(task_id, custom_field_body, params=None)

        return custom_field
