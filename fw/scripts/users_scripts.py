import os

from fw.fw_base import FWBase
import json


class UsersScripts(FWBase):
    file_data = None

    def update_users_settings(self, update_api_keys=False, take_non_updatable_keys=False):
        if take_non_updatable_keys:
            for user in self.manager.group_data.users:
                self.manager.group_data.users[user]['user_id'] = self.manager.group_data.secret_key[self.manager.settings.branch][user]['user_id']
                self.manager.group_data.users[user]['secret'] = self.manager.group_data.secret_key[self.manager.settings.branch][user]['secret']
        else:
            # Проверяем существование файла пользователей
            users_settings = os.path.exists(os.path.join(self.manager.api_users.get_project_root(), 'Data', 'users2.json'))
            if users_settings:
                # если файл есть - считываем данные
                with open(os.path.join(self.manager.api_users.get_project_root(), 'data', 'users2.json')) as json_file:
                    self.file_data = json.load(json_file)
                # Проверяем наличие нужного branch в файле
                if self.manager.settings.branch in self.file_data:
                    self.users = self.file_data[self.manager.settings.branch]['users']
                else:
                    self.update_users_to_the_template()
                # проверяем наличие user_id у пользователей
                # проверяем поля, которые могут измениться из-за внешних систем
                for user in self.users:
                    if self.users[user]['user_id'] == '' or \
                            self.users[user]['Password'] != self.manager.group_data.users[user]['Password'] or \
                            self.users[user]['EmailPas'] != self.manager.group_data.users[user]['EmailPas'] or \
                            self.users[user]['EmailExternalPas'] != self.manager.group_data.users[user]['EmailExternalPas']:
                        self.update_users_to_the_template()
                        break
                if update_api_keys:
                    self.update_users_secrets()
            else:
                # если файла нет - обновляем пользоватлеей + обновление ключей
                self.update_users_to_the_template()
                self.update_users_secrets()
            self.manager.group_data.users = self.users

    def update_users_to_the_template(self):
        self.users = self.manager.group_data.users
        body = {
            "search": "Automation",
            "searchType": "Like",
            "skip": 0,
            "take": 100,
        }
        users = self.manager.api_users.post_users_filter(body)
        assert 'errors' not in users
        # обход всех пользователей из шаблона
        for user_example in self.users:
            user_found = False
            # обход всех пользователей найденных по слову Automation
            for user in users['items']:
                # Проверяем по ФИО + login существует ли пользователь
                if self.users[user_example]['Login'] == user['login']:
                    if self.users[user_example]['Name'] == user['name']:
                        if self.users[user_example]['MiddleName'] == user['middleName']:
                            if self.users[user_example]['Surname'] == user['surname']:
                                # Запись ИД пользователя в шаблон, для последующего использования
                                self.users[user_example]['user_id'] = user['id']
                                # редактирование пользователя
                                body = {
                                    "email": self.users[user_example]['Email'],
                                    "name": self.users[user_example]['Name'],
                                    "middleName": self.users[user_example]['MiddleName'],
                                    "surname": self.users[user_example]['Surname'],
                                }
                                if self.users[user_example]['Manager'] != '':
                                    body["managerId"] = self.users[self.users[user_example]['Manager']]['user_id']

                                response = self.manager.api_users.put_users_id(self.users[user_example]['user_id'], body)
                                assert 'errors' not in response

                                # Выставляем статус пользователя.
                                if self.users[user_example]['Status'] == 'Work':
                                    status = 'Active'
                                else:
                                    status = 'Blocked'

                                response_change_status = self.manager.api_users.put_users_id_change_status(self.users[user_example]['user_id'], {},
                                                                                                           params={'accountInputStatus': status})
                                assert 'errors' not in response_change_status
                                user_found = True
                                print(f"Пользователь обновлен {user_example}")
                                break

            if user_found is False:
                # создать пользователя
                user_body = {
                    "email": self.users[user_example]['Email'],
                    "name": self.users[user_example]['Name'],
                    "middleName": self.users[user_example]['MiddleName'],
                    "surname": self.users[user_example]['Surname'],
                    "login": self.users[user_example]['Login']
                }
                if self.users[user_example]['Manager'] != '':
                    user_body["managerId"] = self.users[self.users[user_example]['Manager']]['user_id']

                user_response = self.manager.api_users.post_users(user_body)
                assert 'errors' not in user_response
                # Запись ИД пользователя в шаблон, для последующего использования
                self.users[user_example]['user_id'] = user_response['id']
                print(f"Пользователь создан {user_example}")

        # Проверяем наличие данных self.file_data
        if self.file_data is None:
            self.file_data = {
                self.manager.settings.branch: {
                    'users': ''
                }
            }
        # Проверяем что в self.file_data есть ветка с текущим branch
        if self.manager.settings.branch not in self.file_data:
            self.file_data[self.manager.settings.branch] = {}

        # Перезаписываем файл users.json
        self.file_data[self.manager.settings.branch]['users'] = self.users
        with open(os.path.join(self.manager.api_users.get_project_root(), 'data', 'users2.json'), 'w', newline='') as outfile:
            json.dump(self.file_data, outfile)

        # После создания файла записываем данные в group_data.users для использования в текущем запуске.
        self.manager.group_data.users = self.users

    def update_users_secrets(self):
        # Чтение данных из файла о созданных пользователях
        with open(os.path.join(self.manager.api_users.get_project_root(), 'data', 'users2.json')) as json_file:
            self.file_data = json.load(json_file)
            self.users = self.file_data[self.manager.settings.branch]['users']

        for user in self.users:
            # Запросить все ключи пользователя с сервера
            secrets_list = self.manager.api_users.get_users_user_id_secrets(self.users[user]['user_id'])
            assert 'errors' not in secrets_list
            flag_create_secrets_key = False
            secrets_response = None
            for secret in secrets_list:
                if "AutomationApiSecretKey" == secret['name']:
                    secrets_response = self.manager.api_users.post_users_user_id_secrets_secret_id(secret['userId'], secret['secretId'], {})
                    assert 'errors' not in secrets_response
                    flag_create_secrets_key = True
                    print(f"Пользователю {user} Востановлен API ключ \"{secrets_response['name']}\"")
            if flag_create_secrets_key is False:
                secrets_response = self.create_secrets_key(user)

            self.users[user]['secret'] = secrets_response['secret']
            self.users[user]['secretId'] = secrets_response['secretId']

        self.file_data[self.manager.settings.branch]['users'] = self.users
        with open(os.path.join(self.manager.api_users.get_project_root(), 'data', 'users2.json'), 'w', newline='') as outfile:
            json.dump(self.file_data, outfile)

    def responsibility_group(self):
        self.RG = self.manager.group_data.RG
        # Чтение данных из файла о созданных пользователях
        with open(os.path.join(self.manager.api_users.get_project_root(), 'data', 'users2.json')) as json_file:
            self.file_data = json.load(json_file)
        self.users = self.file_data[self.manager.settings.branch]['users']

        parent_id = parent_id_2 = group_id = None
        responsibility_groups_list = self.group_search()
        # Поиск корневого каталога
        parent_group = False
        for responsibility_group in responsibility_groups_list['items']:
            # Если найден нужный корневой каталог, перезаписываем его настройки.
            if 'Отдел тестирования Гандивы (Automation)' == responsibility_group['name']:
                parent_id = responsibility_group['id']
                parent_group = True

                parent_group_body = {
                    "name": 'Отдел тестирования Гандивы (Automation)',
                    "parentId": None,
                    "dispatcherUserId": None,
                    "managerUserId": None,
                    "isActive": True,
                    "isDeleted": False
                }
                response = self.manager.api_responsibility_groups.put_responsibility_groups_id(parent_id, parent_group_body)
                assert 'errors' not in response
                print(f"Корневой каталог ГО обновлен ({parent_group_body['name']})")
                break
        # Если обошли все корневые каталоги и НЕ нащли нужный, создаём.
        if parent_group is False:
            parent_id = self.add_responsibility_groups('Отдел тестирования Гандивы (Automation)')['id']
            print(f"Корневой каталог ГО создан (Отдел тестирования Гандивы (Automation))")

        # Поиск вложенных каталогов
        responsibility_groups_list = self.group_search(parent_id)
        # Если каталогов нет - создаём
        if len(responsibility_groups_list['items']) == 0:
            parent_id_2 = self.add_responsibility_groups('Automation responsibility groups', parent_id)['id']
            print(f"Создаем под. каталог (Automation responsibility groups)")
        # иначе проверяем все каталоги что есть.
        else:
            # Делаем обход по всем вложенным каталогам
            for group in responsibility_groups_list['items']:
                # Если нашли нужный, накатываем настройки каталога из шаблона
                if group["name"] == 'Automation responsibility groups':
                    parent_group_body = {
                        "name": 'Automation responsibility groups',
                        "parentId": f"{parent_id}",
                        "dispatcherUserId": None,
                        "managerUserId": None,
                        "isActive": True,
                        "isDeleted": False
                    }
                    parent_id_2 = self.manager.api_responsibility_groups.put_responsibility_groups_id(group["id"], parent_group_body)
                    parent_id_2 = parent_id_2['id']
                    assert 'errors' not in parent_id_2
                    print(f"Обновляем каталог (Automation responsibility groups)")
                # Если среди каталогов нет нужного - создаём
                else:
                    response = self.manager.api_responsibility_groups.delete_responsibility_groups_id_users(group["id"])
                    assert 'errors' not in response
                    print(f"Создаем под. каталог (Automation responsibility groups)")

        # Получаем список вложенных ГО
        responsibility_groups_list = self.group_search(parent_id_2)
        # Перебираем все ГО из списка шаблонов
        for group_name in self.RG:
            flag = False
            # Сравниваем с каждым существующим ГО
            for group in responsibility_groups_list['items']:
                # Если найдена нужная ГО, накатываем настройки ГО из шаблона
                if group_name == group['name']:
                    body = {
                        "name": group_name,
                        "parentId": parent_id_2,
                        "dispatcherUserId": None,
                        "managerUserId": None,
                        "isActive": True,
                        "isDeleted": False
                    }
                    response = self.manager.api_responsibility_groups.put_responsibility_groups_id(group['id'], body)
                    assert 'errors' not in response
                    print(f"Обновляем ГО - {group_name}")
                    group_id = group['id']
                    flag = True
                    # В найденой и обновленной ГО, берем список пользователей (только активных)
                    users_list = self.manager.api_responsibility_groups.post_responsibility_groups_id_users_filter(group['id'], {"skip": 0, "take": 100, "isDeleted": False})[
                        "items"]
                    # Делаем обход всех пользователей из шаблона. (которые должны быть в данной ГО)
                    for user_name_template in self.RG[group_name]:
                        user_flag = False
                        for user in users_list:
                            # Если найден нужный пользователь, ничего не делаем, заканчиваем обход пользователей
                            if self.users[user_name_template]['user_id'] == user['id']:
                                user_flag = True
                                print(f"Пользователь {user_name_template} в ГО {group_name} - есть")
                                break
                        # Если обошли всех пользователей и не нашли нужного, добавляем
                        if user_flag is False:
                            body = {"users": [self.users[user_name_template]['user_id']]}
                            self.manager.api_responsibility_groups.post_responsibility_groups_id_users(group['id'], body)
                            print(f"Пользователь {user_name_template} в ГО {group_name} - добавлен")
            # Если НЕ нашли нужной ГО создаём её.
            if flag is False:
                group = self.add_responsibility_groups(group_name, parent_id_2)
                print(f"Создаем ГО - {group_name}")
                # Делаем обход всех пользователей из шаблона. (которые должны быть в данной ГО)
                group_id = group['id']
                for user_name_template in self.RG[group_name]:
                    # Добавляем пользователей из списка шаблона
                    body = {"users": [self.users[user_name_template]['user_id']]}
                    self.manager.api_responsibility_groups.post_responsibility_groups_id_users(group['id'], body)
                    print(f"Пользователь {user_name_template} в ГО {group_name} - добавлен")

            self.RG[group_name].append(group_id)

        with open(os.path.join(self.manager.api_users.get_project_root(), 'data', 'responsibility_groups.json'), 'w', newline='') as outfile:
            json.dump(self.RG, outfile)

    def service_catalogs(self):
        self.service_template = self.manager.group_data.service_template
        # Чтение данных из файла о созданных ГО
        with open(os.path.join(self.manager.api_users.get_project_root(), 'data', 'responsibility_groups.json')) as json_file:
            self.RG = json.load(json_file)
        # Чтение данных из файла о созданных пользователях
        with open(os.path.join(self.manager.api_users.get_project_root(), 'data', 'users2.json')) as json_file:
            self.file_data = json.load(json_file)
        self.users = self.file_data[self.manager.settings.branch]['users']

        parentId = catalogs_id = None
        # Поиск корневого каталога
        body = {
            "skip": 0,
            "take": 1000,
            "filter": {
                "type": "Catalog"
            },
            "parentId": None,
        }
        service_catalogs_list = self.manager.api_service_catalogs.post_service_catalogs_filter_parent_tree_list(body)['items']
        assert 'errors' not in service_catalogs_list
        service_flag = False

        # Обход всех найденных корневых элементов
        for service in service_catalogs_list:
            # Если корневой элемент найден по имени
            if 'Отдел тестирования Гандивы' == service['name']:
                body = {
                    "parentId": None,
                    "name": "Отдел тестирования Гандивы",
                    "isActive": True
                }
                # обновляем его настройки.
                parentId = self.manager.api_service_catalogs.put_service_catalogs_id(service['id'], body)['id']
                service_flag = True
                print(f"Корневой каталог обновлен \"{body['name']}\"")
                break
        # Если корневой элемент не найден - создаём
        if service_flag is False:
            body = {
                "parentId": None,
                "name": "Отдел тестирования Гандивы",
            }
            parentId = self.manager.api_service_catalogs.post_service_catalogs(body)['id']
            print(f"Корневой каталог создан \"{body['name']}\"")

        body = {
            "skip": 0,
            "take": 100,
            "filter": {
                "type": "Catalog"
            },
            "parentId": parentId,
            "isDeleted": False
        }
        # Ищем вложенные каталоги
        catalogs_list = self.manager.api_service_catalogs.post_service_catalogs_filter_parent_tree_list(body)['items']
        catalogs_flag = False

        # Обход всех найденных элементов
        for catalog in catalogs_list:
            # Каталог найден по имени - обновляем.
            if 'Automation service catalogs' == catalog['name']:
                body = {
                    "parentId": parentId,
                    "name": 'Automation service catalogs',
                    "isActive": True
                }
                catalogs_id = self.manager.api_service_catalogs.put_service_catalogs_id(catalog['id'], body)['id']
                catalogs_flag = True
                print(f"Под. каталог обновлен \"{body['name']}\"")
                break
        if catalogs_flag is False:
            body = {
                "parentId": parentId,
                "name": 'Automation service catalogs',
            }
            catalogs_id = self.manager.api_service_catalogs.post_service_catalogs(body)['id']
            print(f"Под. каталог создан \"{body['name']}\"")

        # получить список услуг
        body = {
            "skip": 0,
            "take": 100,
            "parentId": catalogs_id,
        }
        service_list = self.manager.api_service_catalogs.post_service_catalogs_filter_parent_tree_list(body)
        for service_t in self.service_template:
            service_flag = False
            for service_l in service_list['items']:
                if service_l["name"] == service_t:
                    self.service_template[service_t]['parentId'] = catalogs_id

                    # self.service_template[service_t]['serviceResponsibilityGroups'][0]["responsibilityGroupId"] = \
                    #   self.RG[self.service_template[service_t]['serviceResponsibilityGroups'][0]["responsibilityGroupId"]][-1]
                    # Удалено поле ГО, т.к. механика АПИ метода по обновлению
                    # если такая ГО уже есть - выдать ошибку
                    # если такой ГО нет в списке - добавить

                    # удаляем поле 'serviceResponsibilityGroups' из тела сообщения на обновление услуги (причина описана выше)
                    del self.service_template[service_t]['serviceResponsibilityGroups']

                    approveUsers = []
                    for approve_user in self.service_template[service_t]["approveUsers"]:
                        approveUsers.append({"id": self.users[approve_user]['user_id'], "isDelete": False})
                    self.service_template[service_t]["approveUsers"] = approveUsers

                    observerUsers = []
                    for observer_users in self.service_template[service_t]["observerUsers"]:
                        observerUsers.append({"id": self.users[observer_users]['user_id'], "isDelete": False})
                    self.service_template[service_t]["observerUsers"] = observerUsers

                    response_services = self.manager.api_gandiva_services.put_gandiva_services_id(service_l['id'], self.service_template[service_t])
                    self.service_template[service_t]['Id'] = service_l['id']
                    self.service_template[service_t]['catalogId'] = response_services['catalogId']
                    service_flag = True
                    print(f"Обновление услуги {self.service_template[service_t]['name']}")
                    break
            if service_flag is False:
                self.service_template[service_t]['parentId'] = catalogs_id
                self.service_template[service_t]['serviceResponsibilityGroups'][0]["responsibilityGroupId"] = \
                    self.RG[self.service_template[service_t]['serviceResponsibilityGroups'][0]["responsibilityGroupId"]][-1]

                approveUsers = []
                for approve_user in self.service_template[service_t]["approveUsers"]:
                    approveUsers.append(self.users[approve_user]['user_id'])
                self.service_template[service_t]["approveUsers"] = approveUsers
                observerUsers = []
                for observer_users in self.service_template[service_t]["observerUsers"]:
                    observerUsers.append(self.users[observer_users]['user_id'])
                self.service_template[service_t]["observerUsers"] = observerUsers

                response_services = self.manager.api_gandiva_services.post_gandiva_services(self.service_template[service_t])
            print(f"Создание услуги {self.service_template[service_t]['name']}")

    def add_responsibility_groups(self, name, parentId=None, isActive=True):
        group_body = {
            "name": f"{name}",
            "isActive": isActive,
        }
        if parentId != None:
            group_body["parentId"] = f"{parentId}"
        response = self.manager.api_responsibility_groups.post_responsibility_groups(group_body)
        return response

    def group_search(self, parent_id=None):
        filter_body = {
            "skip": 0,
            "take": 1000,
            "parentId": parent_id,
        }
        return self.manager.api_responsibility_groups.post_responsibility_groups_tree(filter_body)

    def create_secrets_key(self, user):
        body_secret = {
            "name": "AutomationApiSecretKey",
            "expireTime": f"{self.manager.time.get_date_time_for_api_g2(365)}"
        }
        secrets_response = self.manager.api_users.post_users_user_id_secrets(self.users[user]['user_id'], body_secret)
        assert 'errors' not in secrets_response
        print(f"Пользователю {user} создан API ключ {body_secret['name']}")
        return secrets_response
