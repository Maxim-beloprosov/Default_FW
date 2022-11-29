import allure

from fw.g1_api.g1_api_base import G1APIBase


class G1ApiActivity(G1APIBase):

    @allure.step('Лента активности непрочитанных комментариев пользователя с постраничным выводом элементов (заявок и задач). GET api/Activity')
    def get_activity(self, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Activity', params)

    @allure.step('Количество непрочитанных комментариев в ленте активности текущего пользователя (заявок и задач). GET api/Activity/Count')
    def get_activity_count(self, params=None):
        return self.requests_GET(self.get_base_url() + 'api/Activity/Count', params)

    @allure.step('Заявка - Элемент ленты активности текущего пользователя. GET api/Activity/Requests/{id}')
    def get_activity_requests_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Activity/Requests/{id}', params)

    @allure.step('Задача - Элемент ленты активности текущего пользователя. GET api/Activity/Tasks/{id}')
    def get_activity_tasks_id(self, id, params=None):
        return self.requests_GET(self.get_base_url() + f'api/Activity/Tasks/{id}', params)
