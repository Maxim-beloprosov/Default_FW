import allure
import pytest

from Test.web_tests.web_base import WebBase


@allure.feature('Web - Knowledge Base')
@allure.story('Редактирование статьи')
class TestEditKnowledgeBase(WebBase):

    @allure.title('Редактирование названия статьи')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_edit_name_of_article(self):

        # Создаем статью
        name = 'TestKnowledgeBase AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        description = 'TestDescription AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_action_in_article.create_article({'title': name, 'bodyContent': [description]})

        # Переходим к статье
        self.APP.web_knowledge_base_article.move_to_article(name)

        # Редактируем название статьи
        new_name = "TestKnowledgeBase AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_edit.edit_name(new_name)

        # Сохраняем статью
        self.APP.web_knowledge_base_create.button_save_article()

        # Сравниваем получаемые значения
        actual_name = self.APP.web_knowledge_base_article.get_name()
        actual_description = self.APP.web_knowledge_base_article.get_description()
        assert new_name == actual_name
        assert description == actual_description


    @allure.title('Редактирование описания статьи')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_edit_description_of_article(self):

        # Создаем статью
        name = 'TestKnowledgeBase AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        description = 'TestDescription AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_action_in_article.create_article({'title': name, 'bodyContent': [description]})

        # Переходим к статье
        self.APP.web_knowledge_base_article.move_to_article(name)

        # Редактируем описание статьи
        new_description = "TestKnowledgeBase AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_edit.edit_description(new_description)

        # Сохраняем статью
        self.APP.web_knowledge_base_edit.button_save_article()

        # Сравниваем получаемые значения
        actual_description = self.APP.web_knowledge_base_article.get_description()
        actual_name = self.APP.web_knowledge_base_article.get_name()
        assert new_description == actual_description
        assert actual_name == name

    @allure.title('Редактирование расположения статьи')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_edit_location_of_article(self):

        # Создаем статью
        name = 'TestKnowledgeBase AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        description = 'TestDescription AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_action_in_article.create_article({'title': name, 'bodyContent': [description]})

        # Переходим к статье
        self.APP.web_knowledge_base_article.move_to_article(name)

        # Меняем расположение статьи
        self.APP.web_knowledge_base_edit.change_location_of_article("AutoTestsKnowledgeBase")

        # Сохраняем статью
        self.APP.web_knowledge_base_edit.button_save_article()

        # Сравниваем получаемые значения
        location_changed = self.APP.web_knowledge_base_edit.check_article_location("AutoTestsKnowledgeBase")
        actual_description = self.APP.web_knowledge_base_article.get_description()
        actual_name = self.APP.web_knowledge_base_article.get_name()
        assert actual_name == name
        assert actual_description == description
        assert location_changed == True

    @allure.title('Изменение прав просмотра статьи на "Все пользователи"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_edit_view_permission_of_article_all_users(self):

        # Создаем статью
        name = 'TestKnowledgeBase AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        description = 'TestDescription AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_action_in_article.create_article({'title': name, 'bodyContent': [description], 'roleReaders': {'accessType': 'OnlySelf'}})

        # Переходим к статье
        self.APP.web_knowledge_base_article.move_to_article(name)

        # Меняем право на просмотр статьи на "Все пользователи"
        self.APP.web_knowledge_base_article.change_view_permissions_of_article_all_users()

        # Сравниваем получаемые значения
        all_users_permission_check = self.APP.web_knowledge_base_article.all_users_view_permissions_of_article_check()
        actual_description = self.APP.web_knowledge_base_article.get_description()
        actual_name = self.APP.web_knowledge_base_article.get_name()
        assert actual_description == description
        assert actual_name == name
        assert all_users_permission_check == True

    @allure.title('Изменение прав просмотра статьи на "Некоторые пользователи"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_edit_view_permission_of_article_someone(self):

        # Создаем статью
        name = 'TestKnowledgeBase AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        description = 'TestDescription AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_action_in_article.create_article({'title': name, 'bodyContent': [description]})

        # Переходим к статье
        self.APP.web_knowledge_base_article.move_to_article(name)

        # Меняем право на просмотр статьи на "Некоторые пользователи"
        self.APP.web_knowledge_base_article.change_view_permissions_of_article_someone("test_user05", "test_user07")

        # Сравниваем получаемые значения
        someone_permission_check = self.APP.web_knowledge_base_article.someone_view_permissions_of_article_check("test_user05", "test_user07")
        actual_description = self.APP.web_knowledge_base_article.get_description()
        actual_name = self.APP.web_knowledge_base_article.get_name()
        assert actual_description == description
        assert actual_name == name
        assert someone_permission_check == True

    @allure.title('Изменение прав просмотра статьи на "Только я"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_edit_view_permission_of_article_only_me(self):
        # Создаем статью
        name = 'TestKnowledgeBase AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        description = 'TestDescription AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_action_in_article.create_article({'title': name, 'bodyContent': [description]})

        # Переходим к статье
        self.APP.web_knowledge_base_article.move_to_article(name)

        # Меняем право на просмотр статьи на "Только я"
        self.APP.web_knowledge_base_article.change_view_permissions_of_article_only_me()

        # Сравниваем получаемые значения
        only_me_permission_check = self.APP.web_knowledge_base_article.only_me_view_permissions_of_article_check()
        actual_description = self.APP.web_knowledge_base_article.get_description()
        actual_name = self.APP.web_knowledge_base_article.get_name()
        assert actual_description == description
        assert actual_name == name
        assert only_me_permission_check == True

    @allure.title('Изменение прав просмотра статьи на "Все, кроме..."')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_edit_view_permission_of_article_all_but(self):

        # Создаем статью
        name = 'TestKnowledgeBase AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        description = 'TestDescription AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_action_in_article.create_article({'title': name, 'bodyContent': [description]})

        # Переходим к статье
        self.APP.web_knowledge_base_article.move_to_article(name)

        # Меняем право на просмотр статьи на "Все, кроме..."
        self.APP.web_knowledge_base_article.change_view_permissions_of_article_all_but("test_user05", "test_user07")

        # Сравниваем получаемые значения
        all_but_permission_check = self.APP.web_knowledge_base_article.all_but_view_permissions_of_article_check("test_user05", "test_user07")
        actual_description = self.APP.web_knowledge_base_article.get_description()
        actual_name = self.APP.web_knowledge_base_article.get_name()
        assert actual_description == description
        assert actual_name == name
        assert all_but_permission_check == True

    @allure.title('Изменение прав редактирования статьи на "Все пользователи"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_edit_permission_of_article_all_users(self):

        # Создаем статью
        name = 'TestKnowledgeBase AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        description = 'TestDescription AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_action_in_article.create_article({'title': name, 'bodyContent': [description], 'roleEditors': {'accessType': 'OnlySelf'}})

        # Переходим к статье
        self.APP.web_knowledge_base_article.move_to_article(name)

        # Меняем право редактирования статьи на "Все пользователи"
        self.APP.web_knowledge_base_article.change_edit_permissions_of_article_all_users()

        # Сравниваем получаемые значения
        all_users_permission_check = self.APP.web_knowledge_base_article.all_users_edit_permissions_of_article_check()
        actual_description = self.APP.web_knowledge_base_article.get_description()
        actual_name = self.APP.web_knowledge_base_article.get_name()
        assert actual_description == description
        assert actual_name == name
        assert all_users_permission_check == True

    @allure.title('Изменение прав редактирования статьи на "Некоторые пользователи"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_edit_permission_of_article_someone(self):
        # Создаем статью
        name = 'TestKnowledgeBase AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        description = 'TestDescription AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_action_in_article.create_article({'title': name, 'bodyContent': [description]})

        # Переходим к статье
        self.APP.web_knowledge_base_article.move_to_article(name)

        # Меняем право редактирования статьи на "Некоторые пользователи"
        self.APP.web_knowledge_base_article.change_edit_permissions_of_article_someone("test_user05", "test_user07")

        # Сравниваем получаемые значения
        someone_permission_check = self.APP.web_knowledge_base_article.someone_edit_permissions_of_article_check("test_user05", "test_user07")
        actual_description = self.APP.web_knowledge_base_article.get_description()
        actual_name = self.APP.web_knowledge_base_article.get_name()
        assert actual_description == description
        assert actual_name == name
        assert someone_permission_check == True

    @allure.title('Изменение прав редактирования статьи на "Только я"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_edit_permission_of_article_only_me(self):
        # Создаем статью
        name = 'TestKnowledgeBase AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        description = 'TestDescription AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_action_in_article.create_article({'title': name, 'bodyContent': [description]})

        # Переходим к статье
        self.APP.web_knowledge_base_article.move_to_article(name)

        # Меняем право редактирования статьи на "Только я"
        self.APP.web_knowledge_base_article.change_edit_permissions_of_article_only_me()

        # Сравниваем получаемые значения
        only_me_permission_check = self.APP.web_knowledge_base_article.only_me_edit_permissions_of_article_check()
        actual_description = self.APP.web_knowledge_base_article.get_description()
        actual_name = self.APP.web_knowledge_base_article.get_name()
        assert actual_description == description
        assert actual_name == name
        assert only_me_permission_check == True

    @allure.title('Изменение прав редактирования статьи на "Все, кроме..."')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_edit_permission_of_article_all_but(self):
        # Создаем статью
        name = 'TestKnowledgeBase AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        description = 'TestDescription AutomationWebTests ' + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.api_action_in_article.create_article({'title': name, 'bodyContent': [description]})

        # Переходим к статье
        self.APP.web_knowledge_base_article.move_to_article(name)

        # Меняем право редактирования статьи на "Все, кроме..."
        self.APP.web_knowledge_base_article.change_edit_permissions_of_article_all_but("test_user05", "test_user07")

        # Сравниваем получаемые значения
        all_but_permission_check = self.APP.web_knowledge_base_article.all_but_edit_permissions_of_article_check("test_user05", "test_user07")
        actual_description = self.APP.web_knowledge_base_article.get_description()
        actual_name = self.APP.web_knowledge_base_article.get_name()
        assert actual_description == description
        assert actual_name == name
        assert all_but_permission_check == True