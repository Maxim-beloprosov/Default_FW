import allure
import pytest

from Test.web_tests.web_base import WebBase


@allure.feature('Web - Knowledge Base')
@allure.story('Восстановление статей')
class TestCreateKnowledgeBase(WebBase):

    @allure.title('Восстановление статьи')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_restore_article(self):
        # Создаем статью
        name = 'TestKnowledgeBase AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        description = 'TestDescription AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_action_in_article.create_article({'title': name, 'bodyContent': [description]})

        # Переходим к статье
        self.APP.web_knowledge_base_article.move_to_article(name)

        # Удаляем статью
        self.APP.web_knowledge_base_article.delete_article()

        # Переходим в корзину
        self.APP.web_knowledge_base_article.button_trash_knowledge_base()

        # Восстанавливаем статью
        self.APP.web_knowledge_base_article.button_restore_article(name)

        # Проверяем, что статья есть в вкладке "Все статьи"
        check = self.APP.web_knowledge_base_article.check_restored_article_in_all_knowledge_base(name)
        assert check == True