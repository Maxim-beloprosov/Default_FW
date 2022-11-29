import allure
import pytest

from Test.web_tests.web_base import WebBase


@allure.feature('Web - Knowledge Base')
@allure.story('Создание статей')
class TestCreateKnowledgeBase(WebBase):

    @allure.title('Создание статьи с базовыми параметрами')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_create_article_with_base_params(self):

        # Нажимаем на кнопку "База знаний" в левом меню, переходим на страницу
        self.APP.web_any_page.click_knowledge_base_left_menu()

        # Нажимаем на кнопку "Создать статью"
        self.APP.web_knowledge_base_article.btn_create_article()

        # Заполняем название
        correct_name = "TestKnowledgeBase AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_name(correct_name)

        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_description(correct_description)

        # Создаем статью
        self.APP.web_knowledge_base_create.button_save_article()

        # Сравниваем получаемые значения
        actual_name = self.APP.web_knowledge_base_article.get_name()
        actual_description = self.APP.web_knowledge_base_article.get_description()
        assert correct_name == actual_name
        assert correct_description == actual_description

    @allure.title('Создание статьи с выбором расположения')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_create_article_with_location(self):

        # Нажимаем на кнопку "База знаний" в левом меню, переходим на страницу
        self.APP.web_any_page.click_knowledge_base_left_menu()

        # Нажимаем на кнопку "Создать статью"
        self.APP.web_knowledge_base_article.btn_create_article()

        # Заполняем название
        correct_name = "TestKnowledgeBase AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_name(correct_name)

        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_description(correct_description)

        # Выбираем расположение статьи
        location = 'AutoTestsKnowledgeBase'
        self.APP.web_knowledge_base_create.choose_location_of_article(location)

        # Создаем статью
        self.APP.web_knowledge_base_create.button_save_article()

        # Сравниваем получаемые значения и проверяем, что выбрано правильное расположение статьи
        actual_name = self.APP.web_knowledge_base_article.get_name()
        actual_description = self.APP.web_knowledge_base_article.get_description()
        check = self.APP.web_knowledge_base_edit.check_article_location(location)
        assert correct_name == actual_name
        assert correct_description == actual_description
        assert check == True

    @allure.title('Создание статьи с выбором права на просмтор "Все пользователи"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_create_article_with_view_permission_all_users(self):

        # Нажимаем на кнопку "База знаний" в левом меню, переходим на страницу
        self.APP.web_any_page.click_knowledge_base_left_menu()

        # Нажимаем на кнопку "Создать статью"
        self.APP.web_knowledge_base_article.btn_create_article()

        # Заполняем название
        correct_name = "TestKnowledgeBase AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_name(correct_name)

        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_description(correct_description)

        # Изменяем права на просмотр статьи
        self.APP.web_knowledge_base_create.change_view_permissions_of_article_all_users()

        # Создаем статью
        self.APP.web_knowledge_base_create.button_save_article()

        # Сравниваем получаемые значения и проверяем, что доступ к статье имеют все пользователи
        actual_name = self.APP.web_knowledge_base_article.get_name()
        actual_description = self.APP.web_knowledge_base_article.get_description()
        check = self.APP.web_knowledge_base_article.all_users_view_permissions_of_article_check()
        assert correct_name == actual_name
        assert correct_description == actual_description
        assert check == True

    @allure.title('Создание статьи с выбором права на просмтор "Некоторые пользователи"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_create_article_with_view_permission_someone_users(self):

        # Нажимаем на кнопку "База знаний" в левом меню, переходим на страницу
        self.APP.web_any_page.click_knowledge_base_left_menu()

        # Нажимаем на кнопку "Создать статью"
        self.APP.web_knowledge_base_article.btn_create_article()

        # Заполняем название
        correct_name = "TestKnowledgeBase AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_name(correct_name)

        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_description(correct_description)

        # Изменяем права на просмотр статьи на "Некоторые пользователи"
        self.APP.web_knowledge_base_create.change_view_permissions_of_article_someone("test_user05", "test_user07")

        # Создаем статью
        self.APP.web_knowledge_base_create.button_save_article()

        # Сравниваем получаемые значения и проверяем, что доступ к статье имеют некоторые пользователи
        actual_name = self.APP.web_knowledge_base_article.get_name()
        actual_description = self.APP.web_knowledge_base_article.get_description()
        check = self.APP.web_knowledge_base_article.someone_view_permissions_of_article_check("test_user05", "test_user07")
        assert correct_name == actual_name
        assert correct_description == actual_description
        assert check == True

    @allure.title('Создание статьи с выбором права на просмтор "Только я"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_create_article_with_view_permission_only_me(self):

        # Нажимаем на кнопку "База знаний" в левом меню, переходим на страницу
        self.APP.web_any_page.click_knowledge_base_left_menu()

        # Нажимаем на кнопку "Создать статью"
        self.APP.web_knowledge_base_article.btn_create_article()

        # Заполняем название
        correct_name = "TestKnowledgeBase AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_name(correct_name)

        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_description(correct_description)

        # Изменяем права на просмотр статьи на "Только я"
        self.APP.web_knowledge_base_create.change_view_permissions_of_article_only_me()

        # Создаем статью
        self.APP.web_knowledge_base_create.button_save_article()

        # Сравниваем получаемые значения и проверяем, что доступ к статье имею только я
        actual_name = self.APP.web_knowledge_base_article.get_name()
        actual_description = self.APP.web_knowledge_base_article.get_description()
        check = self.APP.web_knowledge_base_article.only_me_view_permissions_of_article_check()
        assert correct_name == actual_name
        assert correct_description == actual_description
        assert check == True

    @allure.title('Создание статьи с выбором права на просмтор "Все кроме..."')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_create_article_with_view_permission_all_but(self):

        # Нажимаем на кнопку "База знаний" в левом меню, переходим на страницу
        self.APP.web_any_page.click_knowledge_base_left_menu()

        # Нажимаем на кнопку "Создать статью"
        self.APP.web_knowledge_base_article.btn_create_article()

        # Заполняем название
        correct_name = "TestKnowledgeBase AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_name(correct_name)

        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_description(correct_description)

        # Изменяем права на просмотр статьи на "Все кроме..."
        self.APP.web_knowledge_base_create.change_view_permissions_of_article_all_but("test_user05", "test_user07")

        # Создаем статью
        self.APP.web_knowledge_base_create.button_save_article()

        # Сравниваем получаемые значения и проверяем, что доступ к статье имеют все, кроме...
        actual_name = self.APP.web_knowledge_base_article.get_name()
        actual_description = self.APP.web_knowledge_base_article.get_description()
        check = self.APP.web_knowledge_base_article.all_but_view_permissions_of_article_check("test_user05", "test_user07")
        assert correct_name == actual_name
        assert correct_description == actual_description
        assert check == True

    @allure.title('Создание статьи с выбором права на редактирование "Все пользователи"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_create_article_with_edit_permission_all_users(self):

        # Нажимаем на кнопку "База знаний" в левом меню, переходим на страницу
        self.APP.web_any_page.click_knowledge_base_left_menu()

        # Нажимаем на кнопку "Создать статью"
        self.APP.web_knowledge_base_article.btn_create_article()

        # Заполняем название
        correct_name = "TestKnowledgeBase AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_name(correct_name)

        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_description(correct_description)

        # Изменяем права на редактирование статьи
        self.APP.web_knowledge_base_create.change_edit_permissions_of_article_all_users()

        # Создаем статью
        self.APP.web_knowledge_base_create.button_save_article()

        # Сравниваем получаемые значения и проверяем, что доступ к редактированию статьи имеют все пользователи
        actual_name = self.APP.web_knowledge_base_article.get_name()
        actual_description = self.APP.web_knowledge_base_article.get_description()
        check = self.APP.web_knowledge_base_article.all_users_edit_permissions_of_article_check()
        assert correct_name == actual_name
        assert correct_description == actual_description
        assert check == True

    @allure.title('Создание статьи с выбором права на редактирование "Некоторые пользователи"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_create_article_with_edit_permission_someone_users(self):

        # Нажимаем на кнопку "База знаний" в левом меню, переходим на страницу
        self.APP.web_any_page.click_knowledge_base_left_menu()

        # Нажимаем на кнопку "Создать статью"
        self.APP.web_knowledge_base_article.btn_create_article()

        # Заполняем название
        correct_name = "TestKnowledgeBase AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_name(correct_name)

        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_description(correct_description)

        # Изменяем права на просмотр статьи на "Некоторые пользователи"
        self.APP.web_knowledge_base_create.change_edit_permissions_of_article_someone("test_user05", "test_user07")

        # Создаем статью
        self.APP.web_knowledge_base_create.button_save_article()

        # Сравниваем получаемые значения и проверяем, что доступ к редактированию статьи имеют некоторые пользователи
        actual_name = self.APP.web_knowledge_base_article.get_name()
        actual_description = self.APP.web_knowledge_base_article.get_description()
        check = self.APP.web_knowledge_base_article.someone_edit_permissions_of_article_check("test_user05", "test_user07")
        assert correct_name == actual_name
        assert correct_description == actual_description
        assert check == True

    @allure.title('Создание статьи с выбором права на редактирование "Только я"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_create_article_with_edit_permission_only_me(self):

        # Нажимаем на кнопку "База знаний" в левом меню, переходим на страницу
        self.APP.web_any_page.click_knowledge_base_left_menu()

        # Нажимаем на кнопку "Создать статью"
        self.APP.web_knowledge_base_article.btn_create_article()

        # Заполняем название
        correct_name = "TestKnowledgeBase AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_name(correct_name)

        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_description(correct_description)

        # Изменяем права на просмотр статьи на "Только я"
        self.APP.web_knowledge_base_create.change_edit_permissions_of_article_only_me()

        # Создаем статью
        self.APP.web_knowledge_base_create.button_save_article()

        # Сравниваем получаемые значения и проверяем, что доступ к редактированию статьи имею только я
        actual_name = self.APP.web_knowledge_base_article.get_name()
        actual_description = self.APP.web_knowledge_base_article.get_description()
        check = self.APP.web_knowledge_base_article.only_me_edit_permissions_of_article_check()
        assert correct_name == actual_name
        assert correct_description == actual_description
        assert check == True

    @allure.title('Создание статьи с выбором права на редактирование "Все кроме..."')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.WebTest
    def test_create_article_with_edit_permission_all_but(self):

        # Нажимаем на кнопку "База знаний" в левом меню, переходим на страницу
        self.APP.web_any_page.click_knowledge_base_left_menu()

        # Нажимаем на кнопку "Создать статью"
        self.APP.web_knowledge_base_article.btn_create_article()

        # Заполняем название
        correct_name = "TestKnowledgeBase AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_name(correct_name)

        # Заполняем описание
        correct_description = "TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        self.APP.web_knowledge_base_create.fill_description(correct_description)

        # Изменяем права на просмотр статьи на "Все кроме..."
        self.APP.web_knowledge_base_create.change_edit_permissions_of_article_all_but("test_user05", "test_user07")

        # Создаем статью
        self.APP.web_knowledge_base_create.button_save_article()

        # Сравниваем получаемые значения и проверяем, что доступ к редактированиб статьи имеют все пользователи, кроме...
        actual_name = self.APP.web_knowledge_base_article.get_name()
        actual_description = self.APP.web_knowledge_base_article.get_description()
        check = self.APP.web_knowledge_base_article.all_but_edit_permissions_of_article_check("test_user05", "test_user07")
        assert correct_name == actual_name
        assert correct_description == actual_description
        assert check == True
