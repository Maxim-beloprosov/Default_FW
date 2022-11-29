import allure

from fw.api.api_base import APIBase


class GandivaServiceTemplate(APIBase):

    @allure.step('Обновление дополнительных полей услуги. PUT /api/GandivaServiceTemplate/{id}')
    def put_gandiva_service_template_id(self, id, body, params=None):
        return self.requests_PUT(self.get_base_url() + f'/api/GandivaServiceTemplate/{id}', body, params)


