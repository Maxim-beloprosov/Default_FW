import allure

from Test.test_base import TestBase


class ApiBase(TestBase):

    def setup_class(self):
        self.APP.scripts_users.update_users_settings(take_non_updatable_keys=True)
        self.status_ticket = self.APP.group_data.Status_ticket
        self.users = self.APP.group_data.users

    def setup_method(self):
        self.APP.api_token.get_token('test_user09')

    def teardown_method(self):
        self.APP.settings.Authorization = True

    def teardown_class(self):
        pass

    def setup_module(self):
        self.APP.scripts_environment.update_environment_file(web=False)

    @allure.step('Создание задачи с доп. полем')
    def create_task_with_custom_field(self, field_name, field_type, value=None, params=None):
        task_body = {
            'subject': "AutomationApiTestTask " + self.APP.time.get_date_time_Y_m_d_H_M_S(),
            'descriptionContent': [
                {
                "type": "Text",
                        "text": "AutomationApiTestDescription " + self.APP.time.get_date_time_Y_m_d_H_M_S()
                }
            ],
            'contractorId': self.APP.group_data.users['test_user02']['user_id'],
            "customFieldCollection":
                [
                    {
                        "name": field_name,
                        "data": {
                            "type": field_type,
                            "value": value
                        },
                        "customFieldSources": [],
                        "orderPath": "0",
                    }
                ]

        }
        task = self.APP.api_tasks.post_tasks(task_body, params)

        return task

    @allure.step('Создание заявки с услугой, в которой предусмотрены доп. поля')
    def create_request_with_custom_fields(self, service_name, data_type='Text', value=''):

        service = self.APP.api_actions_in_service_catalog.search_service(service_name)
        request_mass = {
            'descriptionContent': [
                    {
                        "type": "Text",
                        "text": "AutomationApiTestDescription " + self.APP.time.get_date_time_Y_m_d_H_M_S()
                    },
                ],
            'serviceId': service['items'][0]['id'],
                        'customFieldCollection': [
            {
                "sourceId": service['items'][0]['id'],
                "sourceType": "GandivaService",
                "customFieldSources": [
                {
                    "sourceType": "GandivaService",
                    "sourceId": service['items'][0]['id']
                }
            ],
                "data": {
                    "defaultSettingType": "None",
                    "type": data_type,
                    "value": value
                },
            }
        ],
        }

        request = self.APP.api_requests.post_requests(request_mass)

        return request

    @allure.step('Формирование списка ID всех согласующих')
    def list_id_all_approver(self, ticket):

        approvers_id = []
        # Получаем список id всех согласующих
        for approver in ticket:
            approvers_id.append(approver['approver']['id'])
        return approvers_id

    @allure.step('Формирование списка ID всех чатов текущего пользователя')
    def list_id_all_chat_for_user(self, messenger_list):
        messenger_list_id = []
        for messenger in messenger_list:
            messenger_list_id.append(messenger['id'])
        return messenger_list_id

    @allure.step(
        'Цикл для поиска коммента в списке непрочитанных комментов. Если искомый коммент найден - вовращаем False')
    def comment_in_the_list_of_unread_comments(self, comment_list, comment_id):
        if comment_list['items'] != []:
            for item in comment_list['items']:
                for comment in item['comments']:
                    if comment['id'] == comment_id:
                        return False
        return True

    @allure.step('Цикл для определения роли пользователя в чате')
    def user_role_in_chat(self, participants_list, participant_name):
        # Переменная для сохранения роли пользователя
        user_role = ''
        # получаем роль нужного нам пользователя
        for participant in participants_list['participants']:
            if participant['id'] == self.APP.group_data.users[participant_name]['user_id']:
                user_role = participant['role']
        return user_role

    @allure.step('Цикл для проверки присутствуют ли входное значение в входном списке. Если да - возвращаем True')
    def filter_find_another_id_response_in_ticket(self, filter_response, ticket_param, ticket_expected_response):
        """
         filter_response - приходящий json после фильтрации. Передавать с параметром ['items'].
         ticket_param - параметр по которому проверять. Например. 'ticketType', 'initiator' и т.д
         ticket_expected_response - ожидаемый результат в параметре ticket_param. Например, 'Task', или id пользователя.
        """

        # Переменная для сохранения начального значения. Ответ None означает, что фильтрация пришла на вход пустая.
        tickets_temp = None
        count = 0
        # Получаем ответ: есть ли входное значение в входном списке
        for items in filter_response:
            if items[ticket_param]['id'] == ticket_expected_response:
                tickets_temp = True
                break
            count += 1
            if count == len(filter_response):
                tickets_temp = False
        return tickets_temp

    @allure.step('Цикл для проверки присутствует ли пользоватлем в тикете со статусом согласования(все уровни согласования). Если да - возвращаем True')
    def filter_find_approver_with_agreement_status(self, filter_response, agreements_status, user):
        """"
         filter_response - приходящий json после фильтрации. Передавать с параметром ['items'].
         ticket_expected_response - статус согласования
         user_id - id пользователя у коготорого нужно найти нужный статус согласования
        """

        # Переменная для сохранения начального значения. Ответ None означает, что фильтрация пришла на вход пустая.
        tickets_temp = None
        agreements_levels_in_tickets = None
        # Получаем ответ: есть ли входное значение в входном списке
        for items in filter_response:
            if items['ticketType'] == 'Task':
                agreements_levels_in_tickets = self.APP.api_tasks.get_all_levels_agreements(items['id'])
            elif items['ticketType'] == 'Request':
                agreements_levels_in_tickets = self.APP.api_requests.get_requests_id_agreements(items['id'])
            elif items['ticketType'] == 'Project':
                agreements_levels_in_tickets = self.APP.api_projects.get_projects_id_agreements(items['id'])

            for levels in agreements_levels_in_tickets:
                for approvers_list in levels['agreements']:
                    if self.users[user]['user_id'] == approvers_list['approver']['id'] and approvers_list['status'] == agreements_status:
                        tickets_temp = True
                        break
            if not tickets_temp:
                return False

        return tickets_temp

    @allure.step('Цикл для проверки есть ли другие ответы помимо ожидаемого. Если да - возвращаем False')
    def filter_find_another_response_in_ticket(self, filter_response, ticket_param, ticket_expected_response):
        """"
         filter_response - приходящий json после фильтрации. Передавать с параметром ['items'].
         ticket_param - параметр по которому проверять. Например. 'ticketType', 'initiator' и т.д
         ticket_expected_response - ожидаемый результат в параметре ticket_param. Например, 'Task', или id пользователя.
        """

        # Переменная для сохранения начального значения. Ответ None означает, что фильтрация пришла на вход пустая.
        tickets_temp = None
        count = 0
        # Получаем ответ: есть ли другие статусы помимо входного в функцию
        for items in filter_response:
            if items[ticket_param] != ticket_expected_response:
                tickets_temp = False
                break
            count = count + 1
            if count == len(filter_response):
                tickets_temp = True
        return tickets_temp

    @allure.step('Цикл для проверки входит время тикета в диапазон входного времени. Если да - возвращаем True')
    def filter_within_the_time_range(self, filter_response, ticket_time, ticket_time_expected_more, ticket_time_expected_less):
        """
         filter_response - приходящий json после фильтрации. Передавать с параметром ['items'].
         ticket_time - параметр времени. Например: 'beginDate', 'endDate', 'createDate' и т.д
         ticket_time_expected_more - начальная временная точка.
         ticket_time_expected_less - конечная временная точка.
        """

        # Переменная для сохранения начального значения. Ошибка None означает, что ответ от фильтра пришёл без единого элемента
        tickets_temp = None
        for items in filter_response:
            # Преобразовать в формат datetime из формата '%Y-%m-%dT%H:%M:%SZ'
            datetime_in_ticket = self.APP.time.convert_to_correct_datetime_from_format_in(items[ticket_time], '%Y-%m-%dT%H:%M:%SZ')
            # Добавить 3 часа времени из-за разницы часового пояса
            datetime_in_ticket = self.APP.time.update_time_in_date_in(str(datetime_in_ticket), 180, '%Y-%m-%d %H:%M:%S')

            # Преобразовать в формат datetime из формата '%Y-%m-%dT%H:%M:%S+03:00'
            datetime_created_date_from = self.APP.time.convert_to_correct_datetime_from_string(
                ticket_time_expected_more, '%Y-%m-%dT%H:%M:%S+03:00')
            datetime_created_date_to = self.APP.time.convert_to_correct_datetime_from_string(ticket_time_expected_less, '%Y-%m-%dT%H:%M:%S+03:00')

            # Проверка, что datetime в тикете лежит в пределах заданных дат. Если все тикеты лежат - возвращаем True.
            if datetime_in_ticket >= datetime_created_date_from and datetime_in_ticket <= datetime_created_date_to:
                tickets_temp = True
            else:
                tickets_temp = False
                break
        return tickets_temp

    @allure.step('Цикл для проверки правильная ли группа ответственности в заявках. Если да - возвращаем True')
    def filter_correct_responsibility_group(self, filter_response, ticket_expected_responsibility_group_id):
        """
         filter_response - приходящий json после фильтрации. Передавать с параметром ['items'].
         ticket_expected_responsibility_group_id - id группы ответственности, которая должна быть в заявке(ах)
        """

        # Переменная для сохранения правильная ли ГО. Ответ None означает, что фильтрация пришла на вход пустая.
        ticket_temp = None
        for items in filter_response:
            current_responsibility_group_id = self.APP.api_requests.get_requests_id_responsibility_group(items['id'])['id']
            if current_responsibility_group_id == ticket_expected_responsibility_group_id:
                ticket_temp = True
            elif current_responsibility_group_id != ticket_expected_responsibility_group_id:
                ticket_temp = False
                break
        return ticket_temp

    @allure.step('Цикл для проверки присутствует ли пользователь в списке тикетов на роли согласующего. Если да - возвращаем True')
    def filter_have_current_user_in_role_approver(self, filter_response, expected_user):
        """
         filter_response - приходящий json после фильтрации. Передавать с параметром ['items'].
         response_expected_user_id_in_role_approver - id пользователя, которого мы хотим найти на роли Согласующего тикета(ов)
        """

        # Переменная для сохранения находится ли пользователь в списке согласующих. Ответ None означает, что фильтрация пришла на вход пустая.
        ticket_temp = None
        for items in filter_response:
            approvers_id = []
            if items['ticketType'] == 'Task':
                task_id = self.APP.api_tasks.get_tasks_id(items['id'])
                for approver in task_id['agreements']:
                    approvers_id.append(approver['approver']['id'])
            elif items['ticketType'] == 'Request':
                request_id = self.APP.api_requests.get_requests_id(items['id'])
                for approver in request_id['agreements']:
                    approvers_id.append(approver['approver']['id'])
            elif items['ticketType'] == 'Project':
                project_id = self.APP.api_projects.get_projects_id(items['id'])
                for approver in project_id['agreements']:
                    approvers_id.append(approver['approver']['id'])


            if self.users[expected_user]['user_id'] in approvers_id:
                ticket_temp = True
            elif self.users[expected_user]['user_id'] not in approvers_id:
                ticket_temp = False
                break
        return ticket_temp

    @allure.step('Цикл для проверки присутствует ли элемент в json ответе. Если да - возвращаем True')
    def filter_response_have_element_in_json(self, filter_response, response_expected_element):
        """
         filter_response - приходящий json после фильтрации. Передавать с параметром ['items'].
         response_expected_element - элемент который мы хотим проверить, присутствует ли в json filter_response. Например, 'contractor'
        """

        # Переменная для сохранения ответа, присутствует ли элемент в json ответе. Ответ None означает, что фильтрация пришла на вход пустая.
        ticket_temp = None
        for items in filter_response:
            if response_expected_element in items:
                ticket_temp = True
            elif response_expected_element not in items:
                ticket_temp = False
                break
        return ticket_temp

    @allure.step('Цикл для проверки отсутствует ли элемент в json ответе. Если да - возвращаем True')
    def filter_response_not_have_element_in_json(self, filter_response, response_expected_element):
        """
         filter_response - приходящий json после фильтрации. Передавать с параметром ['items'].
         response_expected_element - элемент который мы хотим проверить, отсутствует ли в json filter_response. Например, 'contractor'
        """

        # Переменная для сохранения ответа, отсутствует ли элемент в json ответе. Ответ None означает, что фильтрация пришла на вход пустая.
        ticket_temp = None
        for items in filter_response:
            if response_expected_element in items:
                ticket_temp = False
                break
            elif response_expected_element not in items:
                ticket_temp = True
        return ticket_temp

    @allure.step('Цикл для вывода всех пользователей в один список из тикета')
    def output_all_users_id_in_ticket(self, ticket_id, ticket_type):

        users_list_temp = []
        ticket_info = ''
        responsibility_group = ''
        if ticket_type == 'Task':
            ticket_info = self.APP.api_tasks.get_tasks_id(ticket_id)
        elif ticket_type == 'Request':
            ticket_info = self.APP.api_requests.get_requests_id(ticket_id)
            responsibility_group = self.APP.api_requests.get_requests_id_responsibility_group(
                ticket_id)
        elif ticket_type == 'Project':
            ticket_info = self.APP.api_projects.get_projects_id(ticket_id)

        users_list_temp.append(ticket_info['initiator']['id'])

        if 'contractors' in ticket_info:
            for items in ticket_info['contractors']:
                users_list_temp.append(items['id'])

        if 'contractor' in ticket_info:
            users_list_temp.append(ticket_info['contractor']['id'])

        for items in ticket_info['agreements']:
            users_list_temp.append(items['id'])

        for items in ticket_info['observers']:
            users_list_temp.append(items['id'])

        if ticket_type == 'Request':
            for items in responsibility_group['users']:
                users_list_temp.append(items['id'])

        return users_list_temp

    @allure.step('Цикл для проверки есть ли другие роли в тикете помимо ожидаемого. Если да - возвращаем False')
    def filter_find_another_access_in_ticket(self, filter_response, ticket_param, ticket_expected_response, user):
        # Переменная для сохранения начального значения
        tickets_temp = None
        count = 0
        # Получаем ответ: есть ли другие статусы помимо входного в функцию
        for i in filter_response:
            ticket_paricipation = self.APP.api_tickets.post_tickets_id_users_userId_access_by_participation(i['id'],
                                                                                                            self.users[user]['user_id'])
            if ticket_expected_response not in ticket_paricipation[ticket_param]:
                tickets_temp = False
                break
            count = count + 1
            if (count == len(filter_response)):
                tickets_temp = True
        return tickets_temp

    @allure.step('Цикл для проверки присутствуют ли тикеты в входном списке. Если да - возвращаем True')
    def filter_find_another_id_in_ticket(self, ticket_list, ticket_id):
        # Переменная для сохранения начального значения
        tickets_temp = None
        count = 0
        # Получаем ответ: есть ли входное значение в входном списке
        for i in ticket_list['items']:
            if i['id'] == ticket_id:
                tickets_temp = True
                break
            count = count + 1
            if (count == len(ticket_list['items'])):
                tickets_temp = False
        return tickets_temp

    @allure.step('Получить ID текущего согласования для конкретного пользователя')
    def agreement_id(self, ticket_agreements, approver_id):

        # Получаем список id всех согласующих
        for item in ticket_agreements:
            if item['approver']['id'] == approver_id:
                agreement_id = item['id']
        return agreement_id

