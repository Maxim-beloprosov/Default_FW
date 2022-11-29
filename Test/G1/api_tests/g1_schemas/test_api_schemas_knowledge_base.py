import allure
import pytest

from Test.G1.api_tests.g1_api_base import G1ApiBase


@allure.epic('G1')
@allure.feature('API')
@allure.story('Проверка схем запросов. База знаний.')
class TestApiKnowledgeBase(G1ApiBase):

    @allure.title('GET api/KnowledgeBase/Nodes')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_knowledge_base_nodes(self):
        self.APP.g1_api_knowledge_base.get_knowledge_base_nodes()
        assert self.APP.group_data.response.status_code == 200

    @allure.title('GET api/KnowledgeBase/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_get_knowledge_base_id(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()
        nodes = self.APP.g1_api_knowledge_base.get_knowledge_base_nodes()

        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token()
        knowledge_base = self.APP.g1_api_knowledge_base.get_knowledge_base_id(nodes[0]['Id'])
        assert self.APP.group_data.response.status_code == 200
        assert 'Name' in knowledge_base
        assert 'Parent' in knowledge_base
        assert 'CreatedDate' in knowledge_base
        assert 'IsRead' in knowledge_base
        assert 'IsEditor' in knowledge_base

    @allure.title('POST api/KnowledgeBase')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_post_knowledge_base(self):
        name = "TestKnowledgeBase AutomationApiTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        description = 'TestDescription AutomationApiTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        create_knowledge_base = self.APP.g1_api_knowledge_base.post_knowledge_base({"Name": name,"Description": description})
        assert self.APP.group_data.response.status_code == 200
        assert create_knowledge_base['Name'] == name
        assert create_knowledge_base['Description'] == description
        assert 'Parent' in create_knowledge_base
        assert 'CreatedDate' in create_knowledge_base
        assert 'CreatedDate' in create_knowledge_base
        assert 'LastEditDate' in create_knowledge_base
        assert 'OrderNum' in create_knowledge_base
        assert 'IsRead' in create_knowledge_base
        assert 'IsEditor' in create_knowledge_base

    @allure.title('DELETE api/KnowledgeBase/id')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Макаров Кирилл Геннадьевич')
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.Gandiva1
    def test_delete_knowledge_base(self):
        self.APP.g1_settings.branch = 'TestNpg'
        self.APP.g1_api_token.get_token()
        name = "TestKnowledgeBase AutomationApiTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        description = 'TestDescription AutomationApiTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        create_knowledge_base = self.APP.g1_api_knowledge_base.post_knowledge_base({"Name": name,"Description": description})

        self.APP.g1_settings.branch = 'test_compose'
        self.APP.g1_api_token.get_token()
        self.APP.g1_api_knowledge_base.delete_knowledge_base_id(create_knowledge_base['Id'])
        assert self.APP.group_data.response.status_code == 200
