import allure

from fw.application_manager import ApplicationManager


class TestBase:

    APP = ApplicationManager()

    def setup_class(self):
        self.main_page = self.APP.settings.GLOBAL[self.APP.settings.branch]['main_page']

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def teardown_class(self):
        pass

    @allure.step('Создание задачи.')
    def create_task(self, tasks_mass={}):
        response = self.create_tickets(tasks_mass, ticket_type='Task')
        return response

    @allure.step('Создание заявки.')
    def create_request(self, request_mass={}):
        response = self.create_tickets(request_mass, ticket_type='Request')
        return response

    @allure.step('Создание проекта.')
    def create_project(self, project_mass={}):
        response = self.create_tickets(project_mass, ticket_type='Project')
        return response

    def get_service_id(self, service_name):
        service_search = {
            "search": self.APP.group_data.service_template[service_name]['name'],
            "filter":
                {
                    "type": "Service",
                    "serviceTypes": ["Normal"]
                },
            "resultView": "List",
            "skip": 0,
            "take": 50,
        }

        services = self.APP.api_gandiva_services_for_tickets.post_gandiva_services_for_tickets_filter(service_search)
        for serv in services['items']:
            if serv['name'] == service_name:
                return serv['id']

    @allure.step('Создание {ticket_type}.')
    def create_tickets(self, tickets_mass={}, ticket_type='Task'):
        """
        Создание задачи / заявки
        В данном методе происходит формирование JSON тела для создания заявки/задачи.
        json_request - итоговое тело запроса.
        Формирование JSON происходит по средством разбора входящего списка tickets_mass, по каждому полю в отдельности.

        Пустое входное значение => задача будет создана с телом ниже (contractorId соответствует  test_user02)
        Задача по умолчанию
         {
            'subject': 'AutomationApiTestTask 2022.06.07 19:56:47',
            'descriptionContent': [{
                    'type': 'Text',
                    'text': 'AutomationApiTestDescription 2022.06.07 19:56:47'}],
            'contractorId': '02399914-bb13-11ec-8ed5-0217dc7a50e7'
         }

         Пустое входное значение => заявка будет создана с телом ниже (serviceId соответствует 'AutomationService Тестовый Тип 1')
        {
            'descriptionContent': [{
                    'type': 'Text',
                    'text': 'AutomationApiTestDescription 2022.06.30 15:39:13'
                }
            ],
            'serviceId': '9275a4ca-f2fc-11ec-bb21-fe4aed3ff546'
        }

        "subject"
            1) только для задач
            2) если есть в tasks_mass то будет подставлено входное значение, иначе подставлено дефолтное
            Пример: {"subject": 'Передаваемый текст ...'}
        "contractorId"
            1) только для задач
            2) если есть в tasks_mass то будет подставлено входное значение, иначе подставлено дефолтное
            Пример: {"contractorId": 'test_user01'}

        "descriptionContent"
            1) для задач и заявок
            2) если есть в tasks_mass то будет подставлено входное значение, иначе подставлено дефолтное
            3) можно передать одним из способов
                1) {"descriptionContent": ['Text 123123']}
                2) {"descriptionContent": [{
                            'type': 'Text',
                            'text': 'Text 123123'}]
                    }
                3) {"descriptionContent": [{'type': 'Attachment', ... }]}
            4) "descriptionContent" - для типов Attachment, Mention, Hashtag, Rating передаём в том виде как должно быть в JSON-е на создание задачи

        "beginDate"
            1) для задач и заявок
            2) может быть передано в виде смещения от текущей даты или в виде готовой даты
            Пример: {"beginDate": 2}
            Пример: {'beginDate': '1970-01-01T00:00:00+03:00'}

        "endDate"
            1) только для задач
            2) может быть передано в виде смещения или в виде готовой даты
            Пример: {"endDate": 2}
            Пример: {'endDate': '1970-01-01T00:00:00+03:00'}

        "approvers"
            1) для задач и заявок
            2) передаём в виде списка тестовых пользователей
            Пример: {"approvers": ['test_user03', 'test_user04']}

        "observers"
            1) для задач и заявок
            2) передаём в виде списка тестовых пользователей
            Пример: {"observers": ['test_user03']}

        "serviceId"
            1) только для заявок
            2) если есть в tasks_mass то будет подставлено входное значение, иначе подставлено дефолтное
            3) передаём ввиде названия тестовой услуги 'AutomationService Тестовый Тип 1',
             Пример: {"serviceId": 'AutomationService Тестовый Тип 1'}

        "customFieldCollection"
            1) только для заявок
            2) если есть в tasks_mass то будет подставлено входное значение

        Для остальных полей
        "observerGroupIds"
        "laboriousness"
        "attachments"
            1) для задач и заявок
            2) если есть в tasks_mass то будет подставлено входное значение
        """
        # -------subject---------------------
        json_request = {}
        if ticket_type == 'Task':
            if "subject" in tickets_mass:
                json_request["subject"] = tickets_mass["subject"]
            else:
                json_request["subject"] = "AutomationApiTestTask " + self.APP.time.get_date_time_Y_m_d_H_M_S()
        elif ticket_type == 'Project':
            if 'subject' in tickets_mass:
                json_request['subject'] = tickets_mass['subject']
            else:
                json_request['subject'] = 'AutomationApiTestProject ' + self.APP.time.get_date_time_Y_m_d_H_M_S()

        # -------descriptionContent------------
        if "descriptionContent" in tickets_mass:
            json_request["descriptionContent"] = []
            for content in tickets_mass["descriptionContent"]:
                if isinstance(content, str):
                    json_request["descriptionContent"].append({
                            "type": "Text",
                            "text": content
                        }
                    )
                else:
                    if content["type"] == 'Text':
                        json_request["descriptionContent"].append({
                                "type": 'Text',
                                "text": content["text"]
                            }
                        )
                    elif content["type"] == 'Attachment':
                        json_request["descriptionContent"].append(content)
                    elif content["type"] == 'Mention':
                        mention_json = {"type": 'Mention'}
                        if 'addresseeType' in content:
                            mention_json["addresseeType"] = content["addresseeType"]
                        if 'userId' in content:
                            mention_json["userId"] = content["userId"]
                        if 'email' in content:
                            mention_json["email"] = content["email"]
                        json_request["descriptionContent"].append(mention_json)
                    elif content["type"] == 'Hashtag':
                        json_request["descriptionContent"].append({
                                "type": 'Hashtag',
                                "hashtag": content["hashtag"],
                            }
                        )
                    elif content["type"] == 'Rating':
                        json_request["descriptionContent"].append({
                                "type": 'Rating',
                                "rating": content["rating"],
                            }
                        )
        else:
            json_request["descriptionContent"] = [
                    {
                        "type": "Text",
                        "text": "AutomationApiTestDescription " + self.APP.time.get_date_time_Y_m_d_H_M_S()
                    },
                ]

        # -------beginDate---------------------
        if "beginDate" in tickets_mass:
            if isinstance(tickets_mass["beginDate"], str):
                json_request["beginDate"] = tickets_mass["beginDate"]
            else:
                json_request["beginDate"] = self.APP.time.get_date_increased_x_days_json(tickets_mass["beginDate"])

        # -------endDate-----------------------
        if ticket_type == 'Task' or ticket_type == 'Project':
            if "endDate" in tickets_mass:
                if isinstance(tickets_mass["endDate"], str):
                    json_request["endDate"] = tickets_mass["endDate"]
                else:
                    json_request["endDate"] = self.APP.time.get_date_increased_x_days_json(tickets_mass["endDate"])

        # -------contractorId-------------------
        if ticket_type == 'Task' or ticket_type == 'Project':
            if "contractorId" in tickets_mass:
                json_request["contractorId"] = self.APP.group_data.users[tickets_mass["contractorId"]]['user_id']
            else:
                json_request["contractorId"] = self.APP.group_data.users['test_user02']['user_id']

        # -------approvers----------------------
        if "approvers" in tickets_mass:
            json_request["approvers"] = []
            for approver in tickets_mass["approvers"]:
                json_request["approvers"].append(self.APP.group_data.users[approver]['user_id'])

        # -------observers----------------------
        if "observers" in tickets_mass:
            json_request["observers"] = []
            for observer in tickets_mass["observers"]:
                json_request["observers"].append(self.APP.group_data.users[observer]['user_id'])

        # -------observerGroupIds----------------
        if "observerGroupIds" in tickets_mass: json_request["observerGroupIds"] = tickets_mass["observerGroupIds"]

        # -------laboriousness-------------------
        if "laboriousness" in tickets_mass: json_request["laboriousness"] = tickets_mass["laboriousness"]

        # -------serviceId-----------------------
        if ticket_type == 'Request':
            if "serviceId" in tickets_mass:
                json_request["serviceId"] = self.get_service_id(tickets_mass["serviceId"])
            else:
                json_request["serviceId"] = self.get_service_id(self.APP.group_data.service_template['AutomationService Тестовый Тип 1']['name'])

        # -------customFieldCollection------------
        if "customFieldCollection" in tickets_mass: json_request["customFieldCollection"] = tickets_mass["customFieldCollection"]

        # -------attachments----------------------
        if "attachments" in tickets_mass: json_request["attachments"] = tickets_mass["attachments"]

        if ticket_type == 'Request':
            response = self.APP.api_requests.post_requests(json_request)
            return response
        if ticket_type == 'Task':
            response = self.APP.api_tasks.post_tasks(json_request)
            return response
        if ticket_type == 'Project':
            response = self.APP.api_projects.post_projects(json_request)
            return response

    @allure.step('Создание g1 заявки')
    def g1_create_request(self, tickets_mass={}):
        json_request = {}

        # -------JobType init----------------------------
        if "JobType" in tickets_mass:
            job_type = tickets_mass["JobType"]
        else:
            job_type = 'Тестовый_Тип_1'

        # -------Department---------------------
        department = self.APP.group_data.service_template_g1[job_type]['department']

        # Получаем все корневые departments
        get_departments = self.APP.g1_api_work_normative.get_work_normative_departments()
        # Ищем нужный департамент, возвращаем его ID
        department_id = self.cycle_search(get_departments, department)

        json_request['Department'] = {
            'Id': department_id
        }

        # -------Category-----------------------
        categories = self.APP.group_data.service_template_g1[job_type]['category']

        get_categories = self.APP.g1_api_work_normative.get_work_normative_departments_department_id_categories(department_id)
        categories_id = self.cycle_search(get_categories, categories)

        json_request['Category'] = {
            'Id': categories_id
        }

        # -------RequestType-----------------------
        request_type = self.APP.group_data.service_template_g1[job_type]['type']

        get_request_type = self.APP.g1_api_work_normative.get_work_normative_categories_category_id_request_types(categories_id)
        request_type_id = self.cycle_search(get_request_type, request_type)

        json_request['RequestType'] = {
            'Id': request_type_id
        }

        # -------JobType-------
        get_job_types = self.APP.g1_api_work_normative.get_work_normative_request_types_request_type_id_job_types(request_type_id)
        job_type_id = self.cycle_search(get_job_types, job_type)

        json_request['JobType'] = {
            'Id': job_type_id
        }

        # -------Description----------------------------
        if "Description" in tickets_mass:
            description = tickets_mass["Description"]
        else:
            description = 'API Test request ' + self.APP.time.get_time_now()
        json_request["Description"] = description

        # -------Region----------------------------
        if "Region" in tickets_mass:
            json_request["Region"] = {
                'Id': self.APP.g1_api_users_wrapper.get_user_id_region(tickets_mass["Region"])
            }

        # -------RequiredStartDate-------------------
        if "RequiredStartDate" in tickets_mass:
            json_request["RequiredStartDate"] = self.APP.time.get_date_increased_x_days_json(tickets_mass["RequiredStartDate"])

        # -------NormativeTime-----------------------
        if "NormativeTime" in tickets_mass:
            json_request["NormativeTime"] = tickets_mass["NormativeTime"]

        # -------Laboriousness-----------------------
        if "Laboriousness" in tickets_mass:
            json_request["Laboriousness"] = tickets_mass["Laboriousness"]

        # -------PlanTimeExecution-----------------------
        if "PlanTimeExecution" in tickets_mass:
            json_request["PlanTimeExecution"] = tickets_mass["PlanTimeExecution"]

        # -------PlanTimeApproval-----------------------
        if "PlanTimeApproval" in tickets_mass:
            json_request["PlanTimeApproval"] = tickets_mass["PlanTimeApproval"]

        # -------PlanTimeClarification---------------------
        if "PlanTimeClarification" in tickets_mass:
            json_request["PlanTimeClarification"] = tickets_mass["PlanTimeClarification"]

        # -------CustomFields-----------------------------
        if "CustomFields" in tickets_mass:
            json_request["CustomFields"] = tickets_mass["CustomFields"]

        # -------Approvers--------------------------------
        if "Approvers" in tickets_mass:
            json_request['Approvers'] = []
            for user_login in tickets_mass['Approvers']:
                user_response = self.APP.g1_api_users.get_users_profile(params={"login": user_login})
                json_request['Approvers'].append({
                    "Id": user_response["Id"],
                    "IsUserAdded": True
                })

        # -------Initiator------------------------------
        if "Initiator" in tickets_mass:
            json_request["Initiator"] = tickets_mass["Initiator"]

        # -------Contractor------------------------------
        if "Contractor" in tickets_mass:
            json_request["Contractor"] = tickets_mass["Contractor"]

        # -------Attachments------------------------------
        if "Attachments" in tickets_mass:
            upload_url = self.APP.g1_api_base.get_base_url() + 'api/Common/Attachments/Upload'
            response_file = self.APP.g1_api_base.upload_file(tickets_mass["Attachments"], upload_url)
            json_request['Attachments'] = response_file

        request = self.APP.g1_api_requests.post_requests(json_request)
        return request

    @allure.step('Создание g1 задачи')
    def g1_create_task(self, tickets_mass={}):
        json_request = {}

        # -------NewContractor------------------------------
        if "NewContractor" in tickets_mass:
            contractor_id = self.APP.g1_api_users.get_users_profile({'login': tickets_mass["NewContractor"]})['Id']
            json_request["NewContractor"] = {'Id': contractor_id}

        else:
            user01_id = self.APP.g1_api_users.get_users_search(params={'text': 'test user1', 'kind': 'Any'})[0]['Id']
            json_request["NewContractor"] = {'Id': user01_id}

        # -------Attachments------------------------------
        if "Attachments" in tickets_mass:
            upload_url = self.APP.g1_api_base.get_base_url() + 'api/Common/Attachments/Upload'
            response_file = self.APP.g1_api_base.upload_file(tickets_mass["Attachments"], upload_url)
            json_request['Attachments'] = response_file

        # -------Approvers--------------------------------
        if "Approvers" in tickets_mass:
            json_request['Approvers'] = []
            for user_login in tickets_mass['Approvers']:
                user_response = self.APP.g1_api_users.get_users_profile(params={'login': user_login})
                json_request['Approvers'].append({
                    "Id": user_response["Id"],
                    "IsUserAdded": True
                })

        # -------Subject--------------------------------
        if "Subject" in tickets_mass:
            json_request['Subject'] = tickets_mass['Subject']
        else:
            json_request['Subject'] = 'AutomationApiTest Subject ' + self.APP.time.get_time_now()

        # -------Description--------------------------------
        if "Description" in tickets_mass:
            json_request['Description'] = tickets_mass['Description']
        else:
            json_request['Description'] = 'AutomationApiTest Description ' + self.APP.time.get_time_now()

        # -------Initiator------------------------------
        if "Initiator" in tickets_mass:
            json_request["Initiator"] = tickets_mass["Initiator"]

        # -------RequiredStartDate-------------------
        if "RequiredStartDate" in tickets_mass:
            json_request["RequiredStartDate"] = self.APP.time.get_date_increased_x_days_json(tickets_mass["RequiredStartDate"])

        # -------Observers--------------------------------
        if "Observers" in tickets_mass:
            json_request['Observers'] = []
            for user_login in tickets_mass['Observers']:
                user_response = self.APP.g1_api_users.get_users_profile(params={'login': user_login})
                json_request['Observers'].append({
                    "Id": user_response["Id"],
                })

        task = self.APP.g1_api_tasks.post_tasks(json_request)
        return task

    def cycle_search(self, response_json, text):
        id = -1
        i = 0
        if 'name' in response_json[0]:
            key_name = 'name'
            key_id = 'id'
        else:
            key_name = 'Name'
            key_id = 'Id'

        while i < len(response_json):
            if response_json[i][key_name] == text:
                id = response_json[i][key_id]
                break
            else:
                i = i + 1
        return id