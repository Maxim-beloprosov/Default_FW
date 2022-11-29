import allure
import pytest
from Test.api_tests.api_base import ApiBase

@allure.feature('Api - KnowledgeBase')
@allure.story('Создание/редактирование/удаление/восстановление статей')
class TestApiKnowledgeBaseArticles(ApiBase):

    @allure.title('Создание статьи с базовыми параметрами')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_default_params(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        assert created_article['resultType'] == 'Create'
        assert created_article['isSuccess']
        assert info_about_access_rights_article['reader'] == 'OnlySelf'
        assert info_about_access_rights_article['editor'] == 'OnlySelf'

    @allure.title('Создание статьи без названия')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_without_title(self):

        # Создание статьи
        created_article = self.APP.api_knowledge_base.post_create_article({})

        assert created_article['status'] == 400

    @allure.title('Создание статьи с названием в 1 символ')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_title_one_symbol(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({'title': 'R'})

        assert created_article['status'] == 400

    @allure.title('Создание статьи с названием в 2 символа')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_title_two_symbol(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({'title': 'RB'})

        assert created_article['resultType'] == 'Create'

    @allure.title('Создание статьи с названием в 512 символов')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_title_512_symbols(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({'title': 'С другой стороны рамки и место обучения кадров способствует подготовки и реализации модели развития. Идейные соображения высшего порядка, а также рамки и место обучения кадров обеспечивает широкому кругу (специалистов) участие в формировании новых предложений. Идейные соображения высшего порядка, а также дальнейшее развитие различных форм деятельности позволяет оценить значение новых предложений. Идейные соображения высшего порядка, а также начало повседневной работы по формированию позиции позволяет.оооооо'})

        assert created_article['resultType'] == 'Create'

    @allure.title('Создание статьи с названием более > 512 символов')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_title_more_512_symbols(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({'title': 'Значимость этих проблем настолько очевидна, что дальнейшее развитие различных форм деятельности обеспечивает широкому кругу (специалистов) участие в формировании новых предложений. Повседневная практика показывает, что реализация намеченных плановых заданий в значительной степени обуславливает создание модели развития. Разнообразный и богатый опыт консультация с широким активом обеспечивает широкому кругу. . Равным образом рамки и место обучения кадров влечет за собой процесс внедрения и модернизации системы обучения кадров, соответствует насущным потребностям.'})

        assert created_article['status'] == 400

    @allure.title('Создание статьи с названием ввиде html инъекции')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_html_injector_in_title(self):

        # Переменая содержащая в себе html инъекцию
        title_injector = '<button>Я кнопка</button>'

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({'title': title_injector})

        # Запрос информации по статье
        info_about_article = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert info_about_article['title'] == title_injector

    @allure.title('Создание статьи с html инъекцией в описании')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_html_injector_in_body_content(self):

        # Переменая содержащая в себе html инъекцию
        title_injector = '<button>Я кнопка</button>'

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({'bodyContent': [{'type': 'Text', 'text': title_injector}]})

        # Запрос информации по статье
        info_about_article = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert created_article['resultType'] == 'Create'
        assert created_article['isSuccess']
        assert info_about_article['bodyContent'][0]['text'] == title_injector

    @allure.title('Создание статьи c bodyContent без указанния типа')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_body_content_without_type(self):

        # Определяем папку родителя
        if self.APP.settings.branch == 'feature_development':
            article_parent_id = self.APP.group_data.parent_id_articles['feature_development']
        elif self.APP.settings.branch == 'Testing':
            article_parent_id = self.APP.group_data.parent_id_articles['Testing']

        # Создание статьи
        created_article = self.APP.api_knowledge_base.post_create_article({'bodyContent': [{'text': 'Text'}], 'parentId': article_parent_id})

        assert created_article['status'] == 400

    @allure.title('Создание статьи c некорректным parentId')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_uncorrect_parent_id(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({'parentId': 'Potato'})

        assert created_article['status'] == 400

    @allure.title('Создание статьи c некорректным порядковым номером')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_uncorrect_order_number(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({'orderNumber': 15.12})

        assert created_article['status'] == 400

    @allure.title('Создание статьи c порядковым номером ввиде строки')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_string_order_number(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({'orderNumber': '15'})

        assert created_article['resultType'] == 'Create'
        assert created_article['isSuccess']

    @allure.title('Создание статьи с Права доступа "Вид" - Все пользователя')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_view_all_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({'roleReaders': {'accessType': 'ALl'}})

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        assert created_article['resultType'] == 'Create'
        assert created_article['isSuccess']
        assert info_about_access_rights_article['editor'] == 'OnlySelf'
        assert info_about_access_rights_article['reader'] == 'All'

    @allure.title('Создание статьи с Права доступа "Редактирование" - Все пользователя')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_edit_all_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({'roleEditors': {'accessType': 'ALl'}})

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        assert created_article['resultType'] == 'Create'
        assert created_article['isSuccess']
        assert info_about_access_rights_article['reader'] == 'OnlySelf'
        assert info_about_access_rights_article['editor'] == 'All'

    @allure.title('Создание статьи с Права доступа "Вид" - Некоторые (Пользователи)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_view_some_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article(self.APP.api_action_in_article.get_json_for_creating_article_with_roles(self.users['test_user08']['user_id'], 'Some', 'User', 'roleReaders'))

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        # Получение списка пользователей для которых есть доступ в статью в качестве Читателя
        reader_article = self.APP.api_action_in_article.list_users_in_role_in_article(created_article['id'], 'Reader', 'Some', 100)

        assert info_about_access_rights_article['reader'] == 'Some'
        assert info_about_access_rights_article['editor'] == 'OnlySelf'
        assert self.users['test_user08']['user_id'] in reader_article
        assert len(reader_article) == 2

    @allure.title('Проверка доступа в статью с правами доступа "Вид" - Некоторые (Пользователи)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_check_access_to_article_with_view_some_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article(self.APP.api_action_in_article.get_json_for_creating_article_with_roles(self.users['test_user08']['user_id'], 'Some', 'User', 'roleReaders'))

        # Переход на пользователя, который был добавлен в Читатели
        self.APP.api_token.get_token('test_user08')

        # Запрос информации по статье
        info_about_article1 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        # Переход на пользователя, который не имеет доступа к статье
        self.APP.api_token.get_token('test_user01')

        # Запрос информации по статье
        info_about_article2 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert 'status' not in info_about_article1
        assert info_about_article2['status'] == 403

    @allure.title('Создание статьи с Права доступа "Вид" - Некоторые (Группы)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_view_some_groups(self):

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article(self.APP.api_action_in_article.get_json_for_creating_article_with_roles(users_group['id'], 'Some', 'Group', 'roleReaders'))

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        # Получение списка пользователей для которых есть доступ в статью в качестве Читателя
        reader_article = self.APP.api_action_in_article.list_users_in_role_in_article(created_article['id'], 'Reader', 'Some', 100)

        assert info_about_access_rights_article['reader'] == 'Some'
        assert info_about_access_rights_article['editor'] == 'OnlySelf'
        assert users_group['id'] in reader_article

    @allure.title('Проверка доступа в статью с правами доступа "Вид" - Некоторые (Группы)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_check_access_in_article_with_view_some_groups(self):

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article(self.APP.api_action_in_article.get_json_for_creating_article_with_roles(users_group['id'], 'Some', 'Group', 'roleReaders'))

        # Переход на пользователя из группы, которую добавили в Читатели
        self.APP.api_token.get_token('test_user08')

        # Запрос информации по статье
        info_about_article1 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        # Переход на пользователя, который не состоит в добавленной группе
        self.APP.api_token.get_token('test_user10')

        # Запрос информации по статье
        info_about_article2 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert 'status' not in info_about_article1
        assert info_about_article2['status'] == 403

    @allure.title('Создание статьи с Права доступа "Редактирование" - Некоторые (Пользователи)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_edit_some_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article(self.APP.api_action_in_article.get_json_for_creating_article_with_roles(self.users['test_user08']['user_id'], 'Some'))

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        # Получение списка пользователей для которых есть доступ в статью в качестве Редактора
        editor_article = self.APP.api_action_in_article.list_users_in_role_in_article(created_article['id'], 'Editor', 'Some', 100)

        assert info_about_access_rights_article['editor'] == 'Some'
        assert info_about_access_rights_article['reader'] == 'OnlySelf'
        assert self.users['test_user08']['user_id'] in editor_article
        assert len(editor_article) == 2

    @allure.title('Проверка доступа в статью с правами доступа "Редактирование" - Некоторые (Пользователи)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_check_access_in_article_with_edit_some_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article(self.APP.api_action_in_article.get_json_for_creating_article_with_roles(self.users['test_user08']['user_id'], 'Some'))

        # Переход на пользователя, которого добавили в Редакторы
        self.APP.api_token.get_token('test_user08')

        # Обновление информации в статье
        self.APP.api_action_in_article.put_update_article_by_id(created_article['id'], {'title': 'CorrectBehavior'})

        # Запрос информации по статье
        info_about_article1 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        # Переход на пользователя, у которого нет прав редактирования
        self.APP.api_token.get_token('test_user01')

        # Обновление информации в статье
        update_article_title = self.APP.api_action_in_article.put_update_article_by_id(created_article['id'], {'title': 'ArticleWithBug'})

        # Запрос информации по статье
        info_about_article2 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert info_about_article1['title'] == 'CorrectBehavior'
        assert update_article_title['status'] == 403
        assert info_about_article2['title'] != 'ArticleWithBug'

    @allure.title('Создание статьи с Права доступа "Редактирование" - Некоторые (Группы)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_edit_some_group(self):

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article(self.APP.api_action_in_article.get_json_for_creating_article_with_roles(users_group['id'], 'Some', "Group"))

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        # Получение списка пользователей для которых есть доступ в статью в качестве Редактора
        editor_article = self.APP.api_action_in_article.list_users_in_role_in_article(created_article['id'], 'Editor', 'Some', 100)

        assert info_about_access_rights_article['editor'] == 'Some'
        assert info_about_access_rights_article['reader'] == 'OnlySelf'
        assert users_group['id'] in editor_article
        assert len(editor_article) == 2

    @allure.title('Проверка доступа в статью с правами доступа "Редактирование" - Некоторые (Группы)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_check_access_in_article_with_edit_some_group(self):

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article(self.APP.api_action_in_article.get_json_for_creating_article_with_roles(users_group['id'], 'Some', "Group"))

        # Переход на пользователя из группы, которую добавили в Редакторы
        self.APP.api_token.get_token('test_user08')

        # Обновление информации в статье
        self.APP.api_action_in_article.put_update_article_by_id(created_article['id'], {'title': 'CorrectBehavior'})

        # Запрос информации по статье
        info_about_article1 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        # Переход на пользователя, не имеющего доступа к статье
        self.APP.api_token.get_token('test_user10')

        # Обновление информации в статье
        update_article_title = self.APP.api_action_in_article.put_update_article_by_id(created_article['id'], {'title': 'ArticleWithBug'})

        # Запрос информации по статье
        info_about_article2 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert info_about_article1['title'] == 'CorrectBehavior'
        assert update_article_title['status'] == 403
        assert info_about_article2['title'] != 'ArticleWithBug'

    @allure.title('Создание статьи с Права доступа "Вид" - Все кроме (Пользователи)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_view_all_except_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article(self.APP.api_action_in_article.get_json_for_creating_article_with_roles(self.users['test_user08']['user_id'], 'Except', "User", 'roleReaders'))

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        # Получение списка пользователей для которых нет доступ в статью в качестве Читателя
        reader_article = self.APP.api_action_in_article.list_users_in_role_in_article(created_article['id'], 'Reader', 'Except', 100)

        assert info_about_access_rights_article['reader'] == 'Except'
        assert info_about_access_rights_article['editor'] == 'OnlySelf'
        assert self.users['test_user08']['user_id'] in reader_article
        assert len(reader_article) == 1

    @allure.title('Проверка доступа в статью с правами доступа "Вид" - Все кроме (Пользователи)')
    @allure.description('Земцов Владислав')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18682')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Есть возможность открыть статью по прямой url без надлежащих прав')
    def test_api_check_access_in_article_with_view_all_except_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article(self.APP.api_action_in_article.get_json_for_creating_article_with_roles(self.users['test_user08']['user_id'], 'Except', "User", 'roleReaders'))

        # Переход на пользователя не имеющего прав просмотра
        self.APP.api_token.get_token('test_user08')

        # Запрос информации по статье
        info_about_article1 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        # Переход на пользователя, имеющего доступ к статье
        self.APP.api_token.get_token('test_user01')

        # Запрос информации по статье
        info_about_article2 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert info_about_article1['status'] == 403
        assert 'status' not in info_about_article2

    @allure.title('Создание статьи с Права доступа "Вид" - Все кроме (Группы)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_view_all_except_groups(self):

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article(self.APP.api_action_in_article.get_json_for_creating_article_with_roles(users_group['id'], 'Except', "Group", 'roleReaders'))

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        # Получение списка пользователей для которых нет доступ в статью в качестве Читателя
        reader_article = self.APP.api_action_in_article.list_users_in_role_in_article(created_article['id'], 'Reader', 'Except', 100)

        assert info_about_access_rights_article['reader'] == 'Except'
        assert info_about_access_rights_article['editor'] == 'OnlySelf'
        assert users_group['id'] in reader_article
        assert len(reader_article) == 1

    @allure.title('Проверка доступа в статью с правами доступа "Вид" - Все кроме (Группы)')
    @allure.description('Земцов Владислав')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18682')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Есть возможность открыть статью по прямой url без надлежащих прав')
    def test_api_check_access_in_article_with_view_all_except_groups(self):

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article(self.APP.api_action_in_article.get_json_for_creating_article_with_roles(users_group['id'], 'Except', "Group", 'roleReaders'))

        # Переход на пользователя не имеющего прав просмотра
        self.APP.api_token.get_token('test_user08')

        # Запрос информации по статье
        info_about_article1 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        # Переход на пользователя не имеющего прав просмотра
        self.APP.api_token.get_token('test_user10')

        # Запрос информации по статье
        info_about_article2 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert info_about_article1['status'] == 403
        assert ['status'] not in info_about_article2

    @allure.title('Создание статьи с Права доступа "Редактирование" - Все кроме (Пользователи)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_edit_all_except(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article(self.APP.api_action_in_article.get_json_for_creating_article_with_roles(self.users['test_user08']['user_id'], 'Except'))

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        # Получение списка пользователей для которых нет доступ в статью в качестве Редакторов
        editor_article = self.APP.api_action_in_article.list_users_in_role_in_article(created_article['id'], 'Editor', 'Except', 100)

        assert info_about_access_rights_article['editor'] == 'Except'
        assert info_about_access_rights_article['reader'] == 'OnlySelf'
        assert self.users['test_user08']['user_id'] in editor_article
        assert len(editor_article) == 1

    @allure.title('Проверка доступа в статью с правами доступа "Редактирование" - Все кроме (Пользователи)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_check_access_article_with_edit_all_except(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article(self.APP.api_action_in_article.get_json_for_creating_article_with_roles(self.users['test_user08']['user_id'], 'Except'))

        # Переход на пользователя не имеющего прав редактирования
        self.APP.api_token.get_token('test_user08')

        # Попытка обновить информацию статьи
        update_article_title = self.APP.api_action_in_article.put_update_article_by_id(created_article['id'], {'title': 'ArticleWithBug'})

        # Запрос информации по статье
        info_about_article1 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        # Переход на пользователя, имеющго права доступа к статье
        self.APP.api_token.get_token('test_user01')

        # Попытка обновить информацию статьи
        self.APP.api_action_in_article.put_update_article_by_id(created_article['id'], {'title': 'CorrectBehavior'})

        # Запрос информации по статье
        info_about_article2 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert update_article_title['status'] == 403
        assert info_about_article1['title'] != 'ArticleWithBug'
        assert info_about_article2['title'] == 'CorrectBehavior'

    @allure.title('Создание статьи с Права доступа "Редактирование" - Все кроме (Группы)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_edit_all_except_group(self):

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article(self.APP.api_action_in_article.get_json_for_creating_article_with_roles(users_group['id'], 'Except', "Group"))

        # Переход на другого тестового пользователя, не состоящего в добавленной группе
        self.APP.api_token.get_token('test_Boss01')

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        # Получение списка пользователей для которых нет доступ в статью в качестве Читателя
        editor_article = self.APP.api_action_in_article.list_users_in_role_in_article(created_article['id'], 'Editor', 'Except', 100)

        assert info_about_access_rights_article['editor'] == 'Except'
        assert info_about_access_rights_article['reader'] == 'OnlySelf'
        assert users_group['id'] in editor_article
        assert len(editor_article) == 1

    @allure.title('Проверка доступа в статью с правами доступа "Редактирование" - Все кроме (Группы)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_check_access_article_with_edit_all_except_group(self):

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article(self.APP.api_action_in_article.get_json_for_creating_article_with_roles(users_group['id'], 'Except', "Group"))

        # Переход на пользователя не имеющего прав редактирования
        self.APP.api_token.get_token('test_user08')

        # Попытка обновить информацию статьи
        update_article_title = self.APP.api_action_in_article.put_update_article_by_id(created_article['id'], {'title': 'ArticleWithBug'})

        # Запрос информации по статье
        info_about_article1 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        # Переход на пользователя, имеюго права редактирования статьи
        self.APP.api_token.get_token('test_user10')

        # Попытка обновить информацию статьи
        self.APP.api_action_in_article.put_update_article_by_id(created_article['id'], {'title': 'CorrectBehavior'})

        # Запрос информации по статье
        info_about_article2 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert update_article_title['status'] == 403
        assert info_about_article1['title'] != 'ArticleWithBug'
        assert info_about_article2['title'] == 'CorrectBehavior'

    @allure.title('Смена расположения статьи')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_change_location_article(self):

        # Создание 1ой статьи родителя
        created_article_parent = self.APP.api_action_in_article.create_article({})

        # Создание 2ой статьи
        created_article_children = self.APP.api_action_in_article.create_article({})

        # Смена расположения статьи
        changed_location = self.APP.api_action_in_article.change_location_in_article(created_article_children['id'], created_article_parent['id'])

        # Получение дочерних статей в 1ой статье
        children_articles = self.APP.api_knowledge_base.post_get_children_articles({'parentId': created_article_parent['id'], 'take': 20})

        assert changed_location['parentId'] == created_article_parent['id']
        assert children_articles['items'][0]['id'] == created_article_children['id']

    @allure.title('Удаление статьи')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_delete_article(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Удаление статьи
        delete_article = self.APP.api_action_in_article.delete_article(created_article['id'])

        assert delete_article['resultType'] == 'Delete'
        assert delete_article['isSuccess']

    @allure.title('Смена заголовка статьи')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_change_title_in_article(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Смена названия статьи
        change_title_article = self.APP.api_action_in_article.update_article(created_article['id'], {'title': 'Тестовое название статьи'})

        # Получение статьи по id
        info_about_article = self.APP.api_knowledge_base.get_article_by_id(change_title_article['id'])

        assert info_about_article['title'] == 'Тестовое название статьи'

    @allure.title('Смена содержания статьи')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_change_about_in_article(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Смена содержания статьи
        change_about_article = self.APP.api_action_in_article.update_article(created_article['id'], {'bodyContent': [{'type': 'Text', 'text': 'Тестовое описание статьи'}]})

        # Получение статьи по id
        info_about_article = self.APP.api_knowledge_base.get_article_by_id(change_about_article['id'])

        assert info_about_article['bodyContent'][0]['text'] == 'Тестовое описание статьи'

    @allure.title('Восстановление удалённой статьи')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_restore_deleted_article(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Удаление статьи
        delete_article = self.APP.api_action_in_article.delete_article(created_article['id'])

        # Восстановление статьи
        restore_article = self.APP.api_action_in_article.restore_article(delete_article['id'])

        # Получение статьи по id
        info_about_article = self.APP.api_knowledge_base.get_article_by_id(restore_article['id'])

        assert not info_about_article['isTrash']

    @allure.title('Изменение прав просмотра статьи на "Все пользователи"')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_change_view_rights_to_all_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав просмотра статьи на "Все пользователи"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], {'roleType': 'Reader', 'accessType': 'All'})

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        assert info_about_access_rights_article['reader'] == 'All'
        assert info_about_access_rights_article['editor'] == 'OnlySelf'

    @allure.title('Изменение прав редактирования статьи на "Все пользователи"')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_change_edit_rights_to_all_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав редактирования статьи на "Все пользователи"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], {'roleType': 'Editor', 'accessType': 'All'})

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        assert info_about_access_rights_article['reader'] == 'OnlySelf'
        assert info_about_access_rights_article['editor'] == 'All'

    @allure.title('Изменение прав просмотра статьи на "Некоторые" (Пользователи)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_change_view_rights_to_some_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав просмотра статьи на "Некоторые"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], self.APP.api_action_in_article.get_json_for_editing_roles(self.users['test_user08']['user_id'], 'Some'))

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        # Получение списка пользователей для которых есть доступ в статью в качестве Читателя
        readers_article = self.APP.api_action_in_article.list_users_in_role_in_article(created_article['id'], 'Reader', 'Some', 100)

        assert info_about_access_rights_article['reader'] == 'Some'
        assert info_about_access_rights_article['editor'] == 'OnlySelf'
        assert self.users['test_user08']['user_id'] in readers_article
        assert len(readers_article) == 2

    @allure.title('Проверка доступа в статью с изменёнными правами просмотра статьи на "Некоторые" (Пользователи)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_check_access_in_changed_article_view_rights_to_some_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав просмотра статьи на "Некоторые"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], self.APP.api_action_in_article.get_json_for_editing_roles(self.users['test_user08']['user_id'], 'Some'))

        # Переход на пользователя, который был добавлен в Редакторы
        self.APP.api_token.get_token('test_user08')

        # Запрос информации по статье
        info_about_article1 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        # Переход на пользователя, у которого нет прав просмотра статьи
        self.APP.api_token.get_token('test_user01')

        # Запрос информации по статье
        info_about_article2 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert 'status' not in info_about_article1
        assert info_about_article2['status'] == 403

    @allure.title('Изменение прав просмотра статьи на "Некоторые" (Группы)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_change_view_right_to_some_groups(self):

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав просмотра статьи на "Некоторые"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], self.APP.api_action_in_article.get_json_for_editing_roles(users_group['id'], 'Some', 'Group'))

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        # Получение списка пользователей для которых есть доступ в статью в качестве Читателя
        readers_article = self.APP.api_action_in_article.list_users_in_role_in_article(created_article['id'], 'Reader', 'Some', 100)

        assert info_about_access_rights_article['reader'] == 'Some'
        assert info_about_access_rights_article['editor'] == 'OnlySelf'
        assert users_group['id'] in readers_article
        assert len(readers_article) == 2

    @allure.title('Проверка доступа в статью с изменёнными правами просмотра статьи на "Некоторые" (Группы)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_check_access_in_changed_article_view_right_to_some_groups(self):

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав просмотра статьи на "Некоторые"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], self.APP.api_action_in_article.get_json_for_editing_roles(users_group['id'], 'Some', 'Group'))

        # Переход на пользователя из группы, которая была добавлена в Читатели
        self.APP.api_token.get_token('test_user08')

        # Запрос информации по статье
        info_about_article1 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        # Переход на пользователя, не имеющего прав просмотра статьи
        self.APP.api_token.get_token('test_user10')

        # Запрос информации по статье
        info_about_article2 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert 'status' not in info_about_article1
        assert info_about_article2['status'] == 403

    @allure.title('Изменение прав редактирования статьи на "Некоторые" (Пользователи)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_change_edit_rights_to_some_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав редактирования статьи на "Некоторые"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], self.APP.api_action_in_article.get_json_for_editing_roles(self.users['test_user08']['user_id'], 'Some', 'User', 'Editor'))

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        # Получение списка пользователей для которых есть доступ в статью в качестве Редактора
        editors_article = self.APP.api_action_in_article.list_users_in_role_in_article(created_article['id'], 'Editor', 'Some', 100)

        assert info_about_access_rights_article['editor'] == 'Some'
        assert info_about_access_rights_article['reader'] == 'OnlySelf'
        assert self.users['test_user08']['user_id'] in editors_article
        assert len(editors_article) == 2

    @allure.title('Проверка доступа в статью с изменёнными правами редактирования статьи на "Некоторые" (Пользователи)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_check_access_in_changed_article_edit_rights_to_some_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав редактирования статьи на "Некоторые"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], self.APP.api_action_in_article.get_json_for_editing_roles(self.users['test_user08']['user_id'], 'Some', 'User', 'Editor'))

        # Переход на пользователя, который был добавлен в Редакторы
        self.APP.api_token.get_token('test_user08')

        # Обновление информации в статье
        self.APP.api_action_in_article.update_article(created_article['id'], {'title': 'CorrectBehavior'})

        # Запрос информации по статье
        info_about_article1 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        # Переход на пользователя, не имеюго прав редактирования
        self.APP.api_token.get_token('test_user01')

        # Обновление информации в статье
        update_article_title = self.APP.api_action_in_article.update_article(created_article['id'], {'title': 'ArticleWithBug'})

        # Запрос информации по статье
        info_about_article2 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert info_about_article1['title'] == 'CorrectBehavior'
        assert update_article_title['status'] == 403
        assert info_about_article2['title'] != 'ArticleWithBug'

    @allure.title('Изменение прав редактирования статьи на "Некоторые" (Группы)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_change_edit_rights_to_some_groups(self):

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав редактирования статьи на "Некоторые"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], self.APP.api_action_in_article.get_json_for_editing_roles(users_group['id'], 'Some', 'Group', 'Editor'))

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        # Получение списка пользователей для которых есть доступ в статью в качестве Редактора
        editors_article = self.APP.api_action_in_article.list_users_in_role_in_article(created_article['id'], 'Editor', 'Some', 100)

        assert info_about_access_rights_article['editor'] == 'Some'
        assert info_about_access_rights_article['reader'] == 'OnlySelf'
        assert users_group['id'] in editors_article
        assert len(editors_article) == 2

    @allure.title('Проверка доступа в статью с изменёнными правами редактирования статьи на "Некоторые" (Группы)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_check_access_in_changed_article_edit_rights_to_some_groups(self):

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав редактирования статьи на "Некоторые"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], self.APP.api_action_in_article.get_json_for_editing_roles(users_group['id'], 'Some', 'Group', 'Editor'))

        # Переход на пользователя из группы, которая была добавлена в Редакторы
        self.APP.api_token.get_token('test_user08')

        # Обновление информации в статье
        self.APP.api_action_in_article.update_article(created_article['id'], {'title': 'CorrectBehavior'})

        # Запрос информации по статье
        info_about_article1 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        # Переход на пользователя, не имеющего прав редактирования
        self.APP.api_token.get_token('test_user10')

        # Обновление информации в статье
        update_article_title = self.APP.api_action_in_article.update_article(created_article['id'], {'title': 'ArticleWithBug'})

        # Запрос информации по статье
        info_about_article2 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert info_about_article1['title'] == 'CorrectBehavior'
        assert update_article_title['status'] == 403
        assert info_about_article2['title'] != 'ArticleWithBug'

    @allure.title('Изменение прав просмотра статьи на "Все кроме" (Пользователи)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_change_view_rights_to_except_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав просмотра статьи на "Все кроме"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], self.APP.api_action_in_article.get_json_for_editing_roles(self.users['test_user08']['user_id'], 'Except'))

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        # Получение списка пользователей для которых нет доступ в статью в качестве Редактора
        readers_article = self.APP.api_action_in_article.list_users_in_role_in_article(created_article['id'], 'Reader', 'Except', 100)

        assert info_about_access_rights_article['reader'] == 'Except'
        assert info_about_access_rights_article['editor'] == 'OnlySelf'
        assert self.users['test_user08']['user_id'] in readers_article
        assert len(readers_article) == 1

    @allure.title('Проверка доступа в статью с изменёнными правами просмотра статьи на "Все кроме" (Пользователи)')
    @allure.description('Земцов Владислав')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18682')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Есть возможность открыть статью по прямой url без надлежащих прав')
    def test_api_check_access_in_changed_article_view_rights_to_except_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав просмотра статьи на "Все кроме"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], self.APP.api_action_in_article.get_json_for_editing_roles(self.users['test_user08']['user_id'], 'Except'))

        # Переход на пользователя не имеющего прав просмотра
        self.APP.api_token.get_token('test_user08')

        # Запрос информации по статье
        info_about_article1 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        # Переход на пользователя, имеющего права просмотра статьи
        self.APP.api_token.get_token('test_user01')

        # Запрос информации по статье
        info_about_article2 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert info_about_article1['status'] == 403
        assert 'status' not in info_about_article2

    @allure.title('Изменение прав просмотра статьи на "Все кроме" (Группы)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_change_view_rights_to_except_groups(self):

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав просмотра статьи на "Все кроме"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], self.APP.api_action_in_article.get_json_for_editing_roles(users_group['id'], 'Except', "Group"))

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        # Получение списка пользователей для которых нет доступ в статью в качестве Редактора
        readers_article = self.APP.api_action_in_article.list_users_in_role_in_article(created_article['id'], 'Reader', 'Except', 100)

        assert info_about_access_rights_article['reader'] == 'Except'
        assert info_about_access_rights_article['editor'] == 'OnlySelf'
        assert users_group['id'] in readers_article
        assert len(readers_article) == 1

    @allure.title('Проверка доступа в статью с изменёнными правами просмотра статьи на "Все кроме" (Группы)')
    @allure.description('Земцов Владислав')
    @allure.link('https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18682')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Есть возможность открыть статью по прямой url без надлежащих прав')
    def test_api_check_access_in_changed_article_view_rights_to_except_groups(self):

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав просмотра статьи на "Все кроме"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], self.APP.api_action_in_article.get_json_for_editing_roles(users_group['id'], 'Except', "Group"))

        # Переход на пользователя из группы, которая не имееет прав просмотра
        self.APP.api_token.get_token('test_user08')

        # Запрос информации по статье
        info_about_article1 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        # Переход на пользователя, у которого есть права просмотра статьи
        self.APP.api_token.get_token('test_user10')

        # Запрос информации по статье
        info_about_article2 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert info_about_article1['status'] == 403
        assert 'status' not in info_about_article2

    @allure.title('Изменение прав редактирования статьи на "Все кроме" (Пользователи)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_change_edit_rights_to_except_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав редактирования статьи на "Все кроме"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], self.APP.api_action_in_article.get_json_for_editing_roles(self.users['test_user08']['user_id'], 'Except', "User", 'Editor'))

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        # Получение списка пользователей для которых нет доступ в статью в качестве Редактора
        editors_article = self.APP.api_action_in_article.list_users_in_role_in_article(created_article['id'], 'Editor', 'Except', 100)

        assert info_about_access_rights_article['editor'] == 'Except'
        assert info_about_access_rights_article['reader'] == 'OnlySelf'
        assert self.users['test_user08']['user_id'] in editors_article
        assert len(editors_article) == 1

    @allure.title('Проверка доступа в статью с изменёнными правами редактирования статьи на "Все кроме" (Пользователи)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_check_access_in_changed_article_edit_rights_to_except_users(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав редактирования статьи на "Все кроме"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], self.APP.api_action_in_article.get_json_for_editing_roles(self.users['test_user08']['user_id'], 'Except', "User", 'Editor'))

        # Переход на пользователя не имеющего прав редактирования
        self.APP.api_token.get_token('test_user08')

        # Попытка обновить информацию статьи
        update_article_title = self.APP.api_action_in_article.update_article(created_article['id'], {'title': 'ArticleWithBug'})

        # Запрос информации по статье
        info_about_article1 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        # Переход на пользователя, который имеет права редактирования статьи
        self.APP.api_token.get_token('test_user01')

        # Попытка обновить информацию статьи
        self.APP.api_action_in_article.update_article(created_article['id'], {'title': 'CorrectBehavior'})

        # Запрос информации по статье
        info_about_article2 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert update_article_title['status'] == 403
        assert info_about_article1['title'] != 'ArticleWithBug'
        assert info_about_article2['title'] == 'CorrectBehavior'

    @allure.title('Изменение прав редактирования статьи на "Все кроме" (Группы)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_change_edit_rights_to_except_groups(self):

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав редактирования статьи на "Все кроме"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], self.APP.api_action_in_article.get_json_for_editing_roles(users_group['id'], 'Except', "Group", 'Editor'))

        # Переход на другого тестового пользователя
        self.APP.api_token.get_token('test_Boss01')

        # Получение прав доступа у статьи
        info_about_access_rights_article = self.APP.api_access.put_return_access_rights_to_article(created_article['id'])

        # Получение списка пользователей для которых нет доступ в статью в качестве Редактора
        editors_article = self.APP.api_action_in_article.list_users_in_role_in_article(created_article['id'], 'Editor', 'Except', 100)

        assert info_about_access_rights_article['editor'] == 'Except'
        assert info_about_access_rights_article['reader'] == 'OnlySelf'
        assert users_group['id'] in editors_article
        assert len(editors_article) == 1

    @allure.title('Проверка доступа в статью с изменёнными правами редактирования статьи на "Все кроме" (Группы)')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_check_access_in_changed_article_edit_rights_to_except_groups(self):

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав редактирования статьи на "Все кроме"
        self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], self.APP.api_action_in_article.get_json_for_editing_roles(users_group['id'], 'Except', "Group", 'Editor'))

        # Переход на пользователя из группы, которая не имеет прав редактирования
        self.APP.api_token.get_token('test_user08')

        # Попытка обновить информацию статьи
        update_article_title = self.APP.api_action_in_article.update_article(created_article['id'], {'title': 'ArticleWithBug'})

        # Запрос информации по статье
        info_about_article1 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        # Переход на пользователя из группы, которая не имеет прав редактирования
        self.APP.api_token.get_token('test_user10')

        # Попытка обновить информацию статьи
        self.APP.api_action_in_article.update_article(created_article['id'], {'title': 'CorrectBehavior'})

        # Запрос информации по статье
        info_about_article2 = self.APP.api_action_in_article.get_article_by_id(created_article['id'])

        assert update_article_title['status'] == 403
        assert info_about_article1['title'] != 'ArticleWithBug'
        assert info_about_article2['title'] == 'CorrectBehavior'

    @allure.title('Изменение прав не существующей роли в статье')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_change_edit_rights_not_exist_article(self):

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        # Изменение прав редактирования статьи на "Все кроме"
        update_access_right_in_article = self.APP.api_action_in_article.update_access_rights_in_article(created_article['id'], self.APP.api_action_in_article.get_json_for_editing_roles(self.users['test_user01']['user_id'], 'Except', "User", 'Potato'))

        assert update_access_right_in_article['status'] == 400

    @allure.title('Создание статьи без авторизации')
    @allure.description('Земцов Владислав')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_create_article_with_non_authorization_in_gandiva(self):

        # Деавторизируемся
        self.APP.settings.Authorization = False

        # Создание статьи
        created_article = self.APP.api_action_in_article.create_article({})

        assert created_article.status_code == 401

