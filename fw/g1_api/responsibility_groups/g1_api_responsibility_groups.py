import allure

from fw.g1_api.g1_api_base import G1APIBase


class G1ApiResponsibilityGroups(G1APIBase):

    @allure.step('Возвращает состав группы ответственности по идентификатору группы ответственности GET api/ResponsibilityGroups/{Id}/Users')
    def get_responsibility_groups_id_users(self, Id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/ResponsibilityGroups/{Id}/Users', params)