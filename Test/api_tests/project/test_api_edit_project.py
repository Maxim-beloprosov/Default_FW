import allure
import pytest
from Test.api_tests.api_base import ApiBase


@allure.feature('Api - Project')
@allure.story('Редактирование проекта')
class TestApiProjectEdit(ApiBase):

    @allure.title('Редактирование заголовка проекта')
    @allure.description('Кантышев Николай')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_project_title_edit(self):

        # Создаём проект
        project = self.create_project()

        # Создаём переменную, в которую заносим новое название проекта с указанным временем изменения
        newtitle = 'Test Project Auto - Change Title ' + self.APP.time.get_date_time_Y_m_d_H_M_S()

        # Изменяем название созданного проекта
        project['subject'] = newtitle

        # Обновляем проект
        project = self.APP.api_projects.put_projects_id(project['id'], project)

        # Сравниваем значения созданного тикета с ожидаемыми значениям
        assert project['subject'] == newtitle


    @allure.title('Добавление обозревателя в проект')
    @allure.description('Кантышев Николай')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_project_add_observer(self):

        # Создаём проект
        project = self.create_project()

        # Создание переменной с обозревателем
        new_observer = self.APP.group_data.users['test_user04']['user_id']

        # Добавление обозревателя в проект
        project = self.APP.api_actions_in_project.upd_observer_in_project(new_observer, project['syncToken'], project['id'])

        # Сравниваем значения созданного тикета с ожидаемыми значениям
        assert project['observers'][0]['id'] == new_observer


    @allure.title('Удаление обозревателя из проекта')
    @allure.description('Кантышев Николай')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_project_del_observer(self):

        # Создаём проект
        project = self.create_project()

        # Добавление обозревателя в проект
        project = self.APP.api_actions_in_project.upd_observer_in_project(self.APP.group_data.users['test_user08']['user_id'],
                                                                          project['syncToken'], project['id'])

        # Удаление обозревателя из проекта
        project = self.APP.api_actions_in_project.upd_observer_in_project(self.APP.group_data.users['test_user08']['user_id'],
                                                                          project['syncToken'], project['id'], 'Delete')

        # Сравниваем значения созданного тикета с ожидаемыми значениям
        assert len(project['observers']) == 0

    @allure.title('Добавление согласующего в проект')
    @allure.description('Кантышев Николай')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    def test_project_add_observer(self):

        # Создаём проект
        project = self.create_project()

        # Создание переменной с обозревателем
        new_approver = self.users['test_user04']['user_id']

        # Добавляем согласующего в проект
        project = self.APP.api_actions_in_project.add_agreement_in_project(project['syncToken'], project['id'], new_approver)

        assert project['agreements'][0]['approver']['id'] == new_approver

