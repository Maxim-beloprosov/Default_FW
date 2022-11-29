import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Пользовательские фильтры в задачах.')
class TestApiTaskUserFilters(G1ApiBase):

    @allure.title('POST api/TaskUserFilters')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_task_user_filters(self):
        name = "TestTaskUserFilter AutomationApiTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()

        body = {
            "Name": name,
            "Filter": {"Initiators": [1, 2],
                       "Contractors": [1, 2],
                       "Statuses": [1, 2],
                       "HashTags": [1, 2]
                       }
        }
        create_task_user_filter = self.APP.g1_api_task_user_filters.post_task_user_filters(body)
        assert self.APP.group_data.response.status_code == 200
        assert 'Error' in create_task_user_filter
        assert 'Target' in create_task_user_filter
        assert 'Status' in create_task_user_filter

    @allure.title('PUT api/TaskUserFilters/RenameName/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_task_user_filters_rename_name_id(self):
        user_task_filters_list = self.APP.g1_api_task_user_filters.get_task_user_filters()
        name = "TestTaskUserFilter AutomationApiTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        rename_task_user_filter = self.APP.g1_api_task_user_filters.put_task_user_filters_rename_name_id(user_task_filters_list[0]['Id'], {'name': name})
        assert self.APP.group_data.response.status_code == 200
        assert 'Target' in rename_task_user_filter
        assert 'Error' in rename_task_user_filter
        assert 'Status' in rename_task_user_filter

    @allure.title('GET api/TaskUserFilters')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_access_sheet_id(self):
        get_task_user_filter = self.APP.g1_api_task_user_filters.get_task_user_filters()
        assert self.APP.group_data.response.status_code == 200
        assert get_task_user_filter
        assert 'Id' in get_task_user_filter[0]
        assert 'Filter' in get_task_user_filter[0]
        assert 'Name' in get_task_user_filter[0]

    @allure.title('PUT api/TaskUserFilters/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_put_task_user_filters_id(self):
        user_task_filters_list = self.APP.g1_api_task_user_filters.get_task_user_filters()
        name = "TestTaskUserFilter AutomationApiTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        change_task_user_filter = self.APP.g1_api_task_user_filters.put_task_user_filters_id(user_task_filters_list[0]['Id'], {"Name": name, "Filter":{"Initiators":[2,3],"Contractors":[3,4],"Statuses":[5,6],"HashTags":[1,2]}})
        assert self.APP.group_data.response.status_code == 200
        assert change_task_user_filter['Target'] == user_task_filters_list[0]['Id']
        assert 'Error' in change_task_user_filter
        assert 'Status' in change_task_user_filter

    @allure.title('DELETE api/TaskUserFilters/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_delete_task_user_filters_id(self):
        body = {
            "Name": "TestTaskUserFilter AutomationApiTests " + self.APP.time.get_date_time_Y_m_d_H_M_S(),
            "Filter": {
                "Initiators": [1, 2],
                "Contractors": [1, 2],
                "Statuses": [1, 2],
                "HashTags": [1, 2]
            }
        }
        create_task_user_filter = self.APP.g1_api_task_user_filters.post_task_user_filters(body)
        delete_task_user_filter = self.APP.g1_api_task_user_filters.delete_task_user_filters_id(create_task_user_filter['Target'])
        assert self.APP.group_data.response.status_code == 200
        assert 'Target' in delete_task_user_filter
        assert 'Error' in delete_task_user_filter
        assert 'Status' in delete_task_user_filter
