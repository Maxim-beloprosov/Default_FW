import allure

from fw.api.tickets.api_request_custom_field_collection.api_request_custom_field_collection import \
    ApiRequestCustomFieldCollection


class ActionsInRequestWithCustomField(ApiRequestCustomFieldCollection):

    @allure.title('Изменить значения доп. поля в заявке')
    def edit_values_in_custom_field_from_request(self, custom_field_id, field_type, value):
        custom_field_body = {
            'defaultSettingType': 'None',
            'type': field_type,
            'value': value
        }

        # Обновляем значение доп. поля
        custom_field = self.put_request_custom_field_collection_id(custom_field_id, custom_field_body)

        return custom_field
