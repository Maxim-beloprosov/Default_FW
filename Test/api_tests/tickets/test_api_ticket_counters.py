import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Ticket')
@allure.story('Счетчики')
class TestApiCounts(ApiBase):

    @allure.title('Проверка счетчика в задачах во вкладке "Все"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_task_all(self):

        # Получение кол-ва задач во вкладке "Все"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Task", "All")

        # Создание задачи
        self.create_task()

        # Проверка, что кол-во задач увеличилось на 1 при создании новой задачи
        check = self.APP.api_actions_in_tickets.check_counts("Task", "All", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в задачах во вкладке "От меня"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_task_i_am_initiator(self):

        # Логинимся под пользователя
        self.APP.api_token.get_token('test_user01')

        # Получение кол-ва задач во вкладке "От меня"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Task", "IAmInitiator")

        # Создание задачи
        self.create_task()

        # Проверка, что кол-во задач увеличилось на 1 при создании новой задачи
        check = self.APP.api_actions_in_tickets.check_counts("Task", "IAmInitiator", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в задачах во вкладке "На мне"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_task_i_am_contractor(self):

        # Логинимся под пользователя
        self.APP.api_token.get_token('test_user01')

        # Получение кол-ва задач во вкладке "На мне"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Task", "IAmContractor")

        # Создание задачи
        self.create_task({"contractorId": 'test_user01'})

        # Проверка, что кол-во задач увеличилось на 1 при создании новой задачи
        check = self.APP.api_actions_in_tickets.check_counts("Task", "IAmContractor", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в задачах во вкладке "Мои согласования"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @pytest.mark.skip(reason='Разные статусы у пользователя в разных микросервисах. https://dev.azure.com/gandiva-agat/Gandiva%20II/_workitems/edit/18933/')
    def test_api_check_counts_in_task_my_agreements(self):

        # Логинимся под пользователя
        self.APP.api_token.get_token('test_user01')

        # Получение кол-ва задач во вкладке "Мои согласования"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Task", "MyAgreements")

        # Логинимся под другого пользователя
        self.APP.api_token.get_token('test_user05')

        # Создание задачи
        self.create_task({"approvers": ['test_user01']})

        # Логинимся под пользователя
        self.APP.api_token.get_token('test_user07')

        # Проверка, что кол-во задач увеличилось на 1 при создании новой задачи
        check = self.APP.api_actions_in_tickets.check_counts("Task", "MyAgreements", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в задачах во вкладке "Обозреваемые"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_task_my_observers(self):

        # Логинимся под пользователя
        self.APP.api_token.get_token('test_user01')

        # Получение кол-ва задач во вкладке "Обозреваемые"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Task", "MyObservers")

        # Создание задачи
        self.create_task({"observers": ['test_user01']})

        # Проверка, что кол-во задач увеличилось на 1 при создании новой задачи
        check = self.APP.api_actions_in_tickets.check_counts("Task", "MyObservers", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в задачах во вкладке "В избранном"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_task_my_favourites(self):

        # Логинимся под пользователя
        self.APP.api_token.get_token('test_user01')

        # Получение кол-ва задач во вкладке "Добавить в избранное"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Task", "MyFavourites")

        # Создание задачи
        task = self.create_task()

        # Добавление задачи в избранное
        self.APP.api_tasks.post_tasks_id_favourites(task['id'], {'syncToken': task['syncToken']})

        # Проверка, что кол-во задач увеличилось на 1 при создании новой задачи
        check = self.APP.api_actions_in_tickets.check_counts("Task", "MyFavourites", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в заявках во вкладке "Все"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_request_all(self):

        # Получение кол-ва заявок во вкладке "Все"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Request", "All")

        # Создание заявки
        self.create_request()

        # Проверка, что кол-во заявок увеличилось на 1 при создании новой заявки
        check = self.APP.api_actions_in_tickets.check_counts("Request", "All", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в заявках во вкладке "От меня"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_request_i_am_initiator(self):

        # Получение кол-ва заявок во вкладке "От меня"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Request", "IAmInitiator")

        # Создание заявки
        self.create_request()

        # Проверка, что кол-во заявок увеличилось на 1 при создании новой заявки
        check = self.APP.api_actions_in_tickets.check_counts("Request", "IAmInitiator", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в заявках во вкладке "На мне"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_request_i_am_contractor(self):

        # Логинимся под пользователя
        self.APP.api_token.get_token('test_user01')

        # Получение кол-ва заявок во вкладке "На мне"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Request", "IAmContractor")

        # Создание заявки
        request = self.create_request()

        # Назначение исполнителя
        self.APP.api_actions_in_tickets.appoint_contractor(request['id'], request['syncToken'], request['initiator']['id'])

        # Проверка, что кол-во заявок увеличилось на 1 при создании новой заявки
        check = self.APP.api_actions_in_tickets.check_counts("Request", "IAmContractor", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в заявках во вкладке "На моих ГО"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_request_my_responsibility_groups(self):

        # Логинимся под пользователя
        self.APP.api_token.get_token('test_user01')

        # Получение кол-ва заявок во вкладке "На моих ГО"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Request", "MyResponsibilityGroups")

        # Создание заявки
        self.create_request()

        # Проверка, что кол-во заявок увеличилось на 1 при создании новой заявки
        check = self.APP.api_actions_in_tickets.check_counts("Request", "MyResponsibilityGroups", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в заявках во вкладке "Мои согласования"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_request_my_agreements(self):

        # Логинимся под пользователя
        self.APP.api_token.get_token('test_user01')

        # Получение кол-ва заявок во вкладке "Мои согласования"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Request", "MyAgreements")

        # Логинимся под другого пользователя
        self.APP.api_token.get_token('test_user05')

        # Создание заявки
        self.create_request({"approvers": ['test_user01']})

        # Логинимся под пользователя
        self.APP.api_token.get_token('test_user01')

        # Проверка, что кол-во заявок увеличилось на 1 при создании новой заявки
        check = self.APP.api_actions_in_tickets.check_counts("Request", "MyAgreements", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в заявках во вкладке "Обозреваемые"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_request_my_observers(self):
        # Логинимся под пользователя
        self.APP.api_token.get_token('test_user01')

        # Получение кол-ва заявок во вкладке "Обозреваемые"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Request", "MyObservers")

        # Создание заявки
        self.create_request({"observers": ['test_user01']})

        # Проверка, что кол-во заявок увеличилось на 1 при создании новой заявки
        check = self.APP.api_actions_in_tickets.check_counts("Request", "MyObservers", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в заявках во вкладке "В избранном"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_request_my_favourites(self):
        # Логинимся под пользователя
        self.APP.api_token.get_token('test_user01')

        # Получение кол-ва заявок во вкладке "Добавить в избранное"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Request", "MyFavourites")

        # Создание заявки
        request = self.create_request()

        # Добавление заявки в избранное
        self.APP.api_requests.post_requests_id_favourites(request['id'], {'syncToken': request['syncToken']})

        # Проверка, что кол-во заявок увеличилось на 1 при создании новой заявки
        check = self.APP.api_actions_in_tickets.check_counts("Request", "MyFavourites", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в проектах во вкладке "Все"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_project_all(self):

        # Получение кол-ва проектов во вкладке "Все"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Project", "All")

        # Создание проекта
        self.create_project()

        # Проверка, что кол-во проектов увеличилось на 1 при создании нового проекта
        check = self.APP.api_actions_in_tickets.check_counts("Project", "All", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в проектах во вкладке "От меня"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_project_i_am_initiator(self):

        # Получение кол-ва проектов во вкладке "От меня"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Project", "IAmInitiator")

        # Создание проекта
        self.create_project()

        # Проверка, что кол-во проектов увеличилось на 1 при создании нового проекта
        check = self.APP.api_actions_in_tickets.check_counts("Project", "IAmInitiator", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в проектах во вкладке "На мне"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_project_i_am_contractor(self):

        # Логинимся под пользователя
        self.APP.api_token.get_token('test_user01')

        # Получение кол-ва проектов во вкладке "На мне"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Project", "IAmContractor")

        # Создание проекта
        self.create_project({"contractorId": 'test_user01'})

        # Проверка, что кол-во проектов увеличилось на 1 при создании нового проекта
        check = self.APP.api_actions_in_tickets.check_counts("Project", "IAmContractor", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в проектах во вкладке "Мои согласования"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_project_my_agreements(self):

        # Логинимся под пользователя
        self.APP.api_token.get_token('test_user01')

        # Получение кол-ва проектов во вкладке "Мои согласования"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Project", "MyAgreements")

        # Логинимся под другого пользователя
        self.APP.api_token.get_token('test_user05')

        # Создание проекта
        self.create_project({"approvers": ['test_user01']})

        # Логинимся под пользователя
        self.APP.api_token.get_token('test_user01')

        # Проверка, что кол-во проектов увеличилось на 1 при создании нового проекта
        check = self.APP.api_actions_in_tickets.check_counts("Project", "MyAgreements", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в проектах во вкладке "Обозреваемые"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_project_my_observers(self):

        # Логинимся под пользователя
        self.APP.api_token.get_token('test_user01')

        # Получение кол-ва проектов во вкладке "Обозреваемые"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Project", "MyObservers")

        # Создание проекта
        self.create_project({"observers": ['test_user01']})

        # Проверка, что кол-во проектов увеличилось на 1 при создании нового проекта
        check = self.APP.api_actions_in_tickets.check_counts("Project", "MyObservers", old_counts)

        assert check == True

    @allure.title('Проверка счетчика в проектах во вкладке "В избранном"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_api_check_counts_in_project_my_favourites(self):

        # Логинимся под пользователя
        self.APP.api_token.get_token('test_user01')

        # Получение кол-ва проектов во вкладке "Добавить в избранное"
        old_counts = self.APP.api_actions_in_tickets.get_counts("Project", "MyFavourites")

        # Создание проекта
        project = self.create_project()

        # Добавление заявки в избранное
        self.APP.api_projects.post_projects_id_favorites(project['id'], {'syncToken': project['syncToken']})

        # Проверка, что кол-во проектов увеличилось на 1 при создании нового проекта
        check = self.APP.api_actions_in_tickets.check_counts("Project", "MyFavourites", old_counts)

        assert check == True



