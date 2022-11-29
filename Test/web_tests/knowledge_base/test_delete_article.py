import allure
import pytest

from Test.web_tests.web_base import WebBase


@allure.feature('Web - Knowledge Base')
@allure.story('Удаление статьи')
class TestEditKnowledgeBase(WebBase):

    @allure.title('Удаление статьи без подстатей')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_delete_article(self):
        # Создаем статью
        name = 'TestKnowledgeBase AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        description = 'TestDescription AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_action_in_article.create_article({'title': name, 'bodyContent': [description]})

        # Переходим к статье
        self.APP.web_knowledge_base_article.move_to_article(name)

        # Удаляем статью
        self.APP.web_knowledge_base_article.delete_article()

        # Проверяем, что удаленная статья есть в корзине
        check = self.APP.web_knowledge_base_article.check_deleted_article_in_trash_knowledge_base(name, description)
        assert check == True

    @allure.title('Удаление статьи с подстатьями')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_delete_article_with_subarticles(self):
        # Создаем 1-ую статью
        first_name = 'TestKnowledgeBase AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        first_description = 'TestDescription AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        parent = self.APP.api_action_in_article.create_article({'title': first_name, 'bodyContent': [first_description]})


        # Создаем 2-ую статью
        second_name = 'TestSecondKnowledgeBase AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        second_description = 'TestSecondDescription AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_action_in_article.create_article({'title': second_name, 'bodyContent': [second_description], 'parentId': parent['id']})

        # Переходим к статье
        self.APP.web_knowledge_base_article.move_to_article(first_name)

        # Удаляем статью с дочерней статьей
        self.APP.web_knowledge_base_article.delete_articles_with_subarticles()

        # Проверяем, что удаленная статья и подстатья есть в корзине
        check = self.APP.web_knowledge_base_article.check_deleted_article_and_subarticle_in_trash_knowledge_base(first_name, first_description, second_name,
                                                                                                                 second_description)
        assert check == True

