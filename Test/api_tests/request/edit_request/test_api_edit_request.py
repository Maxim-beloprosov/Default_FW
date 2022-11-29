import allure
import pytest
from Test.api_tests.api_base import ApiBase


@allure.feature('Api - request')
@allure.story('Редактирование заявок')
class TestApiEditRequest(ApiBase):

    @allure.title('Смена даты начала заявки')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_change_begin_date_in_request(self):

        # Создаем заявку
        request = self.create_request()

        # Меняем дату начала
        request = self.APP.api_change_request.change_begin_date(request['syncToken'], request['id'], 2)

        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В ожидании']

    @allure.title('Удалить дату начала заявки')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_delete_begin_date_in_request(self):

        # Создаем заявку
        request = self.create_request({"beginDate": 7})

        # Удаляем дату начала
        request = self.APP.api_change_request.delete_begin_date(request['syncToken'], request['id'])

        assert request['status'] == self.APP.group_data.Status_ticket['ENG']['В работе']

    @allure.title('Смена планового времени исполнения')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_change_planned_time_execution(self):

        # Создаем заявку
        request = self.create_request()

        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')

        # Меняем плановое время исполнения
        request = self.APP.api_change_request.change_planned_time_execution(request['syncToken'], request['id'])

        assert request['responsibilityGroup']['plannedTimeOfExecution'] == 1000

    @allure.title('Смена планового времени согласования')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_change_planned_time_approve(self):

        # Создаем заявку
        request = self.create_request()

        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')

        # Меняем плановое время согласования
        request = self.APP.api_change_request.change_planned_time_approve(request['syncToken'], request['id'])

        assert request['plannedTimeOfApproval'] == 1000

    @allure.title('Смена планового времени уточнения')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_change_planned_time_clarification(self):

        # Создаем заявку
        request = self.create_request()

        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')

        # Меняем плановое время согласования
        request = self.APP.api_change_request.change_planned_time_clarification(request['syncToken'], request['id'])

        assert request['plannedTimeOfClarification'] == 1000

    @allure.title('Смена трудоёмкости')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_change_laboriousness(self):

        # Создаем заявку
        request = self.create_request()

        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')

        # Меняем плановое время согласования
        request = self.APP.api_change_request.change_laboriousness(request['syncToken'], request['id'])

        assert request['responsibilityGroup']['laboriousness'] == 1000

    @allure.title('Смена услуги в заявке')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_change_service(self):

        # Создаем заявку
        request = self.create_request()

        # Перелогиниваемся на модератора
        self.APP.api_token.get_token('SystemOperator')

        # Ищем нужную услугу
        services = self.APP.api_actions_in_service_catalog.search_service(
            self.APP.group_data.service_template['AutomationService Тестовый Тип 4']['name'])

        # Меняем услугу
        request = self.APP.api_change_request.change_service_in_request(request['syncToken'], request['id'], services["items"][0]['id'])

        assert request['gandivaService']['id'] == services['items'][0]['id']

    @allure.title('Добавление вложения в заявку')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_add_attachments_in_request(self):

        # Создаем заявку
        request = self.create_request()

        # Ищем нужный файл в файловом менеджере
        attachment = self.APP.api_actions_in_file_manager_files_list.get_file_list({'search': 'Тестовое фото №1'})

        # Добавляем вложение
        request = self.APP.api_change_request.add_attachments_in_request(request['id'],
                                                                         [attachment['filesMetadata'][0]['id']])

        assert len(request['attachments']) > 0
        assert request['attachments'][0]['fileMetaData']['id'] == attachment['filesMetadata'][0]['id']

    @allure.title('Добавление нескольких вложений в заявку')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_add_few_attachments_in_request(self):

        # Создаем заявку
        request = self.create_request()

        # Ищем нужный файл в файловом менеджере
        attachment_one = self.APP.api_actions_in_file_manager_files_list.get_file_list({'search': 'Тестовое фото №1'})

        # Ищем нужный файл в файловом менеджере
        attachment_two = self.APP.api_actions_in_file_manager_files_list.get_file_list({'search': 'Тестовое фото №2'})

        # Добавляем вложения
        request = self.APP.api_change_request.add_attachments_in_request(request['id'],
                                                                         [attachment_one['filesMetadata'][0]['id'],
                                                                          attachment_two['filesMetadata'][0]['id']])

        assert len(request['attachments']) > 1

    @allure.title('Удаление вложения из заявки')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_delete_attachments_from_request(self):

        # Создаем заявку
        request = self.create_request()

        # Ищем нужный файл в файловом менеджере
        attachment = self.APP.api_actions_in_file_manager_files_list.get_file_list({'search': 'Тестовое фото №1'})

        # Добавляем вложение
        request = self.APP.api_change_request.add_attachments_in_request(request['id'],
                                                                         [attachment['filesMetadata'][0]['id']])
        # Удаляем вложение
        request = self.APP.api_change_request.delete_attachments_from_request(request['id'],
                                                                              [request['attachments'][0]['id']])
        assert len(request['attachments']) == 0

    @allure.title('Удаление нескольких вложений из заявки')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_delete_few_attachments_from_request(self):

        # Создаем заявку
        request = self.create_request()

        # Ищем нужный файл в файловом менеджере
        attachment_one = self.APP.api_actions_in_file_manager_files_list.get_file_list({'search': 'Тестовое фото №1'})

        # Ищем нужный файл в файловом менеджере
        attachment_two = self.APP.api_actions_in_file_manager_files_list.get_file_list({'search': 'Тестовое фото №2'})

        # Добавляем вложения
        request = self.APP.api_change_request.add_attachments_in_request(request['id'],
                                                                         [attachment_one['filesMetadata'][0]['id'],
                                                                          attachment_two['filesMetadata'][0]['id']])
        # Удаляем вложения
        request = self.APP.api_change_request.delete_attachments_from_request(request['id'],
                                                                              [request['attachments'][0]['id'],
                                                                               request['attachments'][1]['id']])
        assert len(request['attachments']) == 0

    @allure.title('Добавление блока описания в заявку')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_add_description_block_in_request(self):

        # Создаем заявку
        request = self.create_request()

        # Дата для описания
        date_time = self.APP.time.get_date_time_Y_m_d_H_M_S()

        # Добавляем описание к заявке
        request = self.APP.api_change_request.add_descriptions_in_request(request['id'], {'type': 'Text',
                                                                                     'text': 'AutomationApiTest Edit Text ' + date_time})
        assert 'AutomationApiTest Edit Text ' + date_time in request['contentParts'][0]['text']

    @allure.title('Добавить заявку в избранное')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_add_request_in_favourites(self):

        # Создаем заявку
        request = self.create_request()

        # Добавляем заявку в избранное
        request = self.APP.api_change_request.add_request_in_favourites(request['id'], request['syncToken'])

        # Получаем список избранных тикетов
        favourites_list = self.APP.api_tickets_filtration.filter_tickets_by_tab_favourites(request['createdDate'], 5)

        assert request['isFavourites'] == True
        assert self.APP.api_change_request.check_request_in_favourites(favourites_list, request['id'])

    @allure.title('Удалить заявку из избранного')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_delete_request_from_favourites(self):

        # Создаем заявку
        request = self.create_request()

        # Добавляем заявку в избранное
        request = self.APP.api_change_request.add_request_in_favourites(request['id'], request['syncToken'])

        # Удаляем заявку из избранного
        request = self.APP.api_requests.delete_requests_id_favourites(request['id'])

        # Получаем список избранных тикетов
        favourites_list = self.APP.api_tickets_filtration.filter_tickets_by_tab_favourites(request['createdDate'], 5)

        assert request['isFavourites'] != True
        assert request not in favourites_list['items']

    @allure.title('Добавить обозревателя в заявку')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_add_observer_request(self):

        # Создаем заявку
        request = self.create_request()

        # Добавляем обозревателя в заявку
        request = self.APP.api_change_request.add_observer(self.APP.group_data.users['test_user03']['user_id'], request['syncToken'], request['id'])

        assert self.APP.group_data.users['test_user03']['user_id'] == request['observers'][0]['id']

    @allure.title('Добавить группу обозревателей в заявку')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_add_observer_group_request(self):

        # Создаем заявку
        request = self.create_request()

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Добавляем группу обозревателей в заявку
        request = self.APP.api_change_request.add_observer_group(users_group['id'], request['syncToken'], request['id'])

        assert users_group['id'] == request['observerGroups'][0]['id']

    @allure.title('Удалить обозревателя из заявки')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_delete_observer_request(self):

        # Создаем заявку
        request = self.create_request()

        # Добавляем обозревателя в заявку
        request = self.APP.api_change_request.add_observer(self.APP.group_data.users['test_user03']['user_id'], request['syncToken'], request['id'])

        # Проверяем наличие обозревателя
        assert self.APP.group_data.users['test_user03']['user_id'] in request['observers'][0]['id']

        # Удаляем обозревателя из заявки
        request = self.APP.api_change_request.add_observer(self.APP.group_data.users['test_user03']['user_id'], request['syncToken'], request['id'], action="Delete")

        assert len(request['observers']) == 0

    @allure.title('Удалить группу обозревателей из заявки')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_delete_observer_group_request(self):

        # Создаем заявку
        request = self.create_request()

        # Поиск группы, если не найдена - создать
        users_group = self.APP.api_actions_in_group.search_and_check_existence_group('AutomationApiGroupUsers')

        # Добавляем группу обозревателей в заявку
        request = self.APP.api_change_request.add_observer_group(users_group['id'], request['syncToken'], request['id'])

        # Получаем Id всех групп в заявке
        group_ids = self.APP.api_change_request.get_observer_groups_ids(request['observerGroups'])

        # Проверяем наличие группы обозревателей
        assert users_group['id'] in group_ids

        # Удаляем группу обозревателей из заявки
        request = self.APP.api_change_request.add_observer_group(users_group['id'], request['syncToken'], request['id'], action="Delete")

        assert len(request['observerGroups']) == 0

    @allure.title('Добавление согласующего обозревателем')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.NORMAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_add_approver_by_observer(self):

        # Создаем заявку с обозревателем
        request = self.create_request({'observers': ['test_user15']})

        # Перелогиниваемся на обозревателя
        self.APP.api_token.get_token('test_user15')

        # Добавляем согласующего
        request = self.APP.api_change_request.add_approver(request['syncToken'], request['id'], 'test_user02')

        assert request['status'] == 400

    @allure.title('Действие "Назначить на себя" из статуса "Проверка выполнения"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.NORMAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_assign_request_to_me_different_status_first(self):

        # Создаем заявку
        request = self.create_request()

        # Перелогиниваемся на участника ГО
        self.APP.api_token.get_token('test_user02')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Отправляем заявку на проверку
        request = self.APP.api_actions_in_request.send_request_to_resolved(request['syncToken'], request['id'])

        # Перелогиниваемся на другого участника ГО
        self.APP.api_token.get_token('test_user04')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        assert request['status'] == 400

    @allure.title('Действие "Назначить на себя" из статуса "Закрыта"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.NORMAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_assign_request_to_me_different_status_second(self):

        # Создаем заявку
        request = self.create_request()

        # Перелогиниваемся на участника ГО
        self.APP.api_token.get_token('test_user02')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Отправляем заявку на проверку
        request = self.APP.api_actions_in_request.send_request_to_resolved(request['syncToken'], request['id'])

        # Перелогиниваемся на инициатора
        self.APP.api_token.get_token('test_user09')

        # Закрываем заявку
        request = self.APP.api_actions_in_request.close_request(request['syncToken'], request['id'], 5)

        # Перелогиниваемся на участника ГО
        self.APP.api_token.get_token('test_user04')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        assert request['status'] == 400

    @allure.title('Действие "Назначить на себя" из статуса "Отклонена"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.NORMAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_assign_request_to_me_different_status_third(self):

        # Создаем заявку
        request = self.create_request({'approvers': ['test_user10']})

        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user10')

        # Отклоняем заявку
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])

        # Перелогиниваемся на участника ГО
        self.APP.api_token.get_token('test_user04')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        assert request['status'] == 400

    @allure.title('Действие "Назначить на себя" из статуса "На согласовании", пользователь = исполнителю')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.NORMAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_assign_request_to_me_different_status_fourth(self):
        # Создаем заявку
        request = self.create_request({'approvers': ['test_user10']})

        # Перелогиниваемся на участника ГО
        self.APP.api_token.get_token('test_user04')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Назначаем заявку на себя ещё раз
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        assert request['status'] == 400

    @allure.title('Действие "Назначить на себя" из статуса "В работе", пользователь = исполнителю')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.NORMAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_assign_request_to_me_different_status_fifth(self):

        # Создаем заявку
        request = self.create_request()

        # Перелогиниваемся на участника ГО
        self.APP.api_token.get_token('test_user04')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Назначаем заявку на себя ещё раз
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        assert request['status'] == 400

    @allure.title('Действие "Назначить на себя" из статуса "На уточнении у инициатора", пользователь = исполнителю')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.NORMAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_assign_request_to_me_different_status_sixth(self):

        # Создаем заявку
        request = self.create_request({'approvers': ['test_user10']})

        # Перелогиниваемся на согласующего
        self.APP.api_token.get_token('test_user10')

        # Задаём вопрос-уточнение инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        # Перелогиниваемся на участника ГО
        self.APP.api_token.get_token('test_user04')

        # Назначаем заявку на себя
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        # Назначаем заявку на себя ещё раз
        request = self.APP.api_actions_in_request.assign_to_me(request['syncToken'], request['id'])

        assert request['status'] == 400

    @allure.title('Отправить на проверку в заявке без исполнителя')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.NORMAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_send_request_to_resolved_without_contractor(self):

        # Создаем заявку
        request = self.create_request()

        # Перелогиниваемся на участника ГО
        self.APP.api_token.get_token('test_user02')

        # Отправляем заявку на проверку
        request = self.APP.api_actions_in_request.send_request_to_resolved(request['syncToken'], request['id'])

        assert request['status'] == 403

    @allure.title('Задать вопрос-уточнение инициатору, пользователь не согласующий, исполнитель или участник го')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.NORMAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_ask_to_initiator_observer(self):

        # Создаем заявку
        request = self.create_request({'observers': ['test_user10']})

        # Перелогиниваемся на обозревателя
        self.APP.api_token.get_token('test_user10')

        # Задаём вопрос-уточнение инициатору
        request = self.APP.api_clarifications.ask_to_initiator_clarification(request['syncToken'], request['id'])

        assert request['status'] == 403

    @allure.title('Задать вопрос-уточнение исполнителю, пользователь не= согласующему')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.NORMAL
    @pytest.mark.ApiTest
    @allure.description('Кустов Антон Владимирович')
    def test_api_ask_to_contractor_observer(self):

        # Создаем заявку
        request = self.create_request({'observers': ['test_user10']})

        # Перелогиниваемся на обозревателя
        self.APP.api_token.get_token('test_user10')

        # Задаём вопрос-уточнение исполнителю
        request = self.APP.api_clarifications.ask_to_contractor_clarification(request['syncToken'], request['id'])

        assert request['status'] == 403
