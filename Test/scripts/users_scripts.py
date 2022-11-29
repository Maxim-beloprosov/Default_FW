import pytest

from Test.test_base import TestBase
import json


class TestUsersScripts(TestBase):
    users = {
        'test_Boss03': {
            'user_id': "",
            'Login': "testboss03",
            'Password': "Qwerty1",
            'secret': "bNxKnPEZTpnnSom9nhYuBMdmyOboBGPNKOM/tMCaTQYWgDgVU1ueJDGpVcDrb9Ak",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_boss3@mail.ru",
            'EmailPas': "Goodpass123",
            'EmailExternalPas': "WXRi9TrGZzay0g9qXJhF",

            'Name': "Test",
            'Surname': "BossThree",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "",
            'ActualAddressId': "",
        },
        'test_Boss02': {
            'user_id': "",
            'Login': "testboss02",
            'Password': "Qwerty1",
            'secret': "",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_boss02@mail.ru",
            'EmailPas': "Goodpass123",
            'EmailExternalPas': "DfcnPw70Pu1nzngHVZKR",

            'Name': "Test",
            'Surname': "BossTwo",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "test_Boss03",
            'ActualAddressId': "НН, Московское ш., 294г",
        },
        'test_Boss01': {
            'user_id': "",
            'Login': "testboss01",
            'Password': "Qwerty1",
            'secret': "",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_boss1@mail.ru",
            'EmailPas': "Goodpass123",
            'EmailExternalPas': "",

            'Name': "Test",
            'Surname': "Boss",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "test_Boss02",
            'ActualAddressId': "",
        },
        'test_user01': {
            'user_id': "",
            'Login': "testuser01",
            'Password': "Qwerty1",
            'secret': "",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_user1@mail.ru",
            'EmailPas': "Asdfgh12",
            'EmailExternalPas': "",

            'Name': "Test",
            'Surname': "UserOne",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "test_Boss01",
            'ActualAddressId': "",
        },
        'test_user02': {
            'user_id': "",
            'Login': "testuser02",
            'Password': "Qwerty1",
            'secret': "",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_user2@mail.ru",
            'EmailPas': "Asdfgh12",
            'EmailExternalPas': "",

            'Name': "Test",
            'Surname': "UserTwo",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "test_Boss01",
            'ActualAddressId': "",
        },
        'test_user03': {
            'user_id': "",
            'Login': "testuser03",
            'Password': "Qwerty1",
            'secret': "",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_user3@mail.ru",
            'EmailPas': "Asdfgh12",
            'EmailExternalPas': "",

            'Name': "Test",
            'Surname': "UserThree",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "test_Boss01",
            'ActualAddressId': "",
        },
        'test_user04': {
            'user_id': "",
            'Login': "testuser04",
            'Password': "Qwerty1",
            'secret': "",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_user4@mail.ru",
            'EmailPas': "Asdfgh12",
            'EmailExternalPas': "",

            'Name': "Test",
            'Surname': "UserFour",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "test_Boss01",
            'ActualAddressId': "",
        },
        'test_user05': {
            'user_id': "",
            'Login': "testuser05",
            'Password': "Qwerty1",
            'secret': "",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_user5@mail.ru",
            'EmailPas': "",
            'EmailExternalPas': "",

            'Name': "Test",
            'Surname': "UserFive",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "test_Boss02",
            'ActualAddressId': "",
        },
        'test_user06': {
            'user_id': "",
            'Login': "testuser06",
            'Password': "Qwerty1",
            'secret': "",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_user6@mail.ru",
            'EmailPas': "",
            'EmailExternalPas': "",

            'Name': "Test",
            'Surname': "UserSix",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "test_Boss02",
            'ActualAddressId': "",
        },
        'test_user07': {
            'user_id': "",
            'Login': "testuser07",
            'Password': "Qwerty1",
            'secret': "",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_user7@mail.ru",
            'EmailPas': "",
            'EmailExternalPas': "",

            'Name': "Test",
            'Surname': "UserSeven",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "",
            'ActualAddressId': "",
        },
        'test_user08': {
            'user_id': "",
            'Login': "testuser08",
            'Password': "Qwerty1",
            'secret': "",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_user8@mail.ru",
            'EmailPas': "Goodpass123",
            'EmailExternalPas': "",

            'Name': "Test",
            'Surname': "UserEight",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "",
            'ActualAddressId': "",
        },
        'test_user09': {
            'user_id': "",
            'Login': "testuser09",
            'Password': "Qwerty1",
            'secret': "",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_user9@mail.ru",
            'EmailPas': "Goodpass123",
            'EmailExternalPas': "",

            'Name': "Test",
            'Surname': "UserNine",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "",
            'ActualAddressId': "",
        },
        'test_user10': {
            'user_id': "",
            'Login': "testuser10",
            'Password': "Qwerty1",
            'secret': "",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_user10@mail.ru",
            'EmailPas': "Goodpass123",
            'EmailExternalPas': "",

            'Name': "Test",
            'Surname': "UserTen",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "",
            'ActualAddressId': "",
        },
        'test_user11': {
            'user_id': "",
            'Login': "testuser11",
            'Password': "Qwerty1",
            'secret': "",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_user11@mail.ru",
            'EmailPas': "Goodpass123",
            'EmailExternalPas': "",

            'Name': "Test",
            'Surname': "UserEleven",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "",
            'ActualAddressId': "",
        },
        'test_user12': {
            'user_id': "",
            'Login': "testuser12",
            'Password': "Qwerty1",
            'secret': "",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_user12@mail.ru",
            'EmailPas': "Goodpass123",
            'EmailExternalPas': "",

            'Name': "Test",
            'Surname': "UserTwelve",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "",
            'ActualAddressId': "",
        },
        'test_user13': {
            'user_id': "",
            'Login': "testuser13",
            'Password': "Qwerty1",
            'secret': "",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_user13@mail.ru",
            'EmailPas': "Goodpass123",
            'EmailExternalPas': "",

            'Name': "Test",
            'Surname': "UserThirteen",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "",
            'ActualAddressId': "",
        },
        'test_user14': {
            'user_id': "",
            'Login': "testuser14",
            'Password': "Qwerty1",
            'secret': "",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_user14@mail.ru",
            'EmailPas': "Goodpass123",
            'EmailExternalPas': "",

            'Name': "Test",
            'Surname': "UserFourteen",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "",
            'ActualAddressId': "",
        },
    }

    groups = ['Отдел тестирования Гандивы (Automation)', 'Automation responsibility groups']
    RG = {
        'Група_тестирования_№1': ['test_Boss01', 'test_user01', 'test_user02', 'test_user03', 'test_user04'],
        'Група_тестирования_№2': ['test_Boss02', 'test_user05', 'test_user06'],
        'Група_тестирования_№3': ['test_Boss01', 'test_Boss02', 'test_Boss03', 'test_user07', 'test_user01']
    }

    service_template = {
        'Тестовый_Тип_1': {
                "name": 'Тестовый_Тип_1',
                "typeType": "Normal",
                "initiatorAccessType": "All",
                "isActive": True,
                "isBossApprove": False,
                "isBossObserver": False,
                "workScheduleOverridden": False,
                "approveTimeNormative": 14400,
                "approveTimeHard": 21600,
                "initiatorTimeNormative": 2880,
                "initiatorTimeNotify": 2880,
                "initiatorTimeWait": 2880,
                "approveUsers": [],
                "observerUsers": [],
                "serviceResponsibilityGroups": [{
                        "responsibilityGroupId": 'Група_тестирования_№1',
                        "timeNormative": 21600,
                        "timeHard": 21600,
                        "orderNumber": 21600
                    }
                ]
            },
        'Тестовый_Тип_2': {
            "name": "Тестовый_Тип_2",
            "typeType": "Normal",
            "initiatorAccessType": "All",
            "isActive": True,
            "isBossApprove": False,
            "isBossObserver": False,
            "workScheduleOverridden": False,
            "approveTimeNormative": 21600,
            "approveTimeHard": 21600,
            "initiatorTimeNormative": 21600,
            "initiatorTimeNotify": 21600,
            "initiatorTimeWait": 21600,
            "approveUsers": ["test_Boss01"],
            "observerUsers": ["test_Boss02"],
            "serviceResponsibilityGroups": [{
                "responsibilityGroupId": 'Група_тестирования_№1',
                "timeNormative": 21600,
                "timeHard": 21600,
                "orderNumber": 21600
                }
            ],
        },
        'Тестовый_Тип_3': {
                "name": 'Тестовый_Тип_3',
                "typeType": "Normal",
                "initiatorAccessType": "All",
                "isActive": True,
                "isBossApprove": False,
                "isBossObserver": False,
                "workScheduleOverridden": False,
                "approveTimeNormative": 14400,
                "approveTimeHard": 21600,
                "initiatorTimeNormative": 2880,
                "initiatorTimeNotify": 2880,
                "initiatorTimeWait": 2880,
                "approveUsers": [],
                "observerUsers": [],
                "serviceResponsibilityGroups": [{
                        "responsibilityGroupId": 'Група_тестирования_№2',
                        "timeNormative": 21600,
                        "timeHard": 21600,
                        "orderNumber": 21600
                    }
                ]
            },
        # 'Тестовый_Тип_4': '',
        # 'Тестовый_Тип_5': '',
        # 'Тестовый_Тип_6_Лист_допуска': '',
        # 'Тестовый_Тип_7_Лист_допуска': '',
        # 'Тестовый_Тип_8_Лист_допуска': '',
        # "Тестовый_Тип_9_Групповая_заявка": '',
        # 'Тестовый_Тип_10_Групповая_заявка': '',
        # 'Тестовый_Тип_11_Групповая_заявка': '',
        # 'Тестовый_Тип_12_Заявка_по_телефону': '',
        # 'Тестовый_Тип_13_Заявка_с_уволенным_согласующим': '',
        # 'Тестовый_Тип_14_Доп_поля': '',
        # 'Тестовый_Тип_15_обязательные_доп_поля': '',
        # 'Тестовый_Тип_16_согласующий_в_отпуске': '',
        # 'Тестовый_Тип_17_обозреватель_в_отпуске': '',
        'Тестовый_Тип_18_Добавлять_руководителя_инициатора_согласующим': {
                "name": 'Тестовый_Тип_18_Добавлять_руководителя_инициатора_согласующим',
                "typeType": "Normal",
                "initiatorAccessType": "All",
                "isActive": True,
                "isBossApprove": True,
                "isBossObserver": False,
                "workScheduleOverridden": False,
                "approveTimeNormative": 14400,
                "approveTimeHard": 21600,
                "initiatorTimeNormative": 2880,
                "initiatorTimeNotify": 2880,
                "initiatorTimeWait": 2880,
                "approveUsers": [],
                "observerUsers": [],
                "serviceResponsibilityGroups": [{
                        "responsibilityGroupId": 'Група_тестирования_№1',
                        "timeNormative": 21600,
                        "timeHard": 21600,
                        "orderNumber": 21600
                    }
                ]
            },
        'Тестовый_Тип_19_Добавлять_руководителя_инициатора_обозревателем': {
                "name": 'Тестовый_Тип_19_Добавлять_руководителя_инициатора_обозревателем',
                "typeType": "Normal",
                "initiatorAccessType": "All",
                "isActive": True,
                "isBossApprove": False,
                "isBossObserver": True,
                "workScheduleOverridden": False,
                "approveTimeNormative": 14400,
                "approveTimeHard": 21600,
                "initiatorTimeNormative": 2880,
                "initiatorTimeNotify": 2880,
                "initiatorTimeWait": 2880,
                "approveUsers": [],
                "observerUsers": [],
                "serviceResponsibilityGroups": [{
                        "responsibilityGroupId": 'Група_тестирования_№1',
                        "timeNormative": 21600,
                        "timeHard": 21600,
                        "orderNumber": 21600
                    }
                ]
            },
    }

    @pytest.mark.TemplateUsers
    def test_bringing_users_to_the_template(self):
        body = {
            "search": "Automation",
            "searchType": "Like",
            "skip": 0,
            "take": 100,
        }
        users = self.APP.api_users.post_users_filter(body)
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

                                response = self.APP.api_users.put_users_id(self.users[user_example]['user_id'], body)
                                assert 'errors' not in response
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

                user_response = self.APP.api_users.post_users(user_body)
                assert 'errors' not in user_response
                # Запись ИД пользователя в шаблон, для последующего использования
                self.users[user_example]['user_id'] = user_response['id']
                print(f"Пользователь создан {user_example}")

        for user in self.users:
            # Запросить все ключи с сервера
            secrets_list = self.APP.api_users.get_users_user_id_secrets(self.users[user]['user_id'])
            assert 'errors' not in secrets_list
            # если нет ключа создаём
            # если есть делаем регенерацию ключа
            if len(secrets_list) == 0:
                body_secret = {
                    "name": f"{self.users[user]['Login']} {self.APP.time.get_date_Users_API()} + 365days",
                    "expireTime": f"{self.APP.time.get_date_time_for_api_g2(365)}"
                }
                secrets_response = self.APP.api_users.post_users_user_id_secrets(self.users[user]['user_id'], body_secret)
                assert 'errors' not in secrets_response
                print(f"Пользователю {user} создан API ключ {body_secret['name']}")
            else:
                secrets_response = self.APP.api_users.post_users_user_id_secrets_secret_id(secrets_list[0]['userId'], secrets_list[0]['secretId'], {})
                assert 'errors' not in secrets_response
                print(f"Пользователю {user} Востановлен API ключ \"{secrets_response['name']}\"")
            self.users[user]['secret'] = secrets_response['secret']
            self.users[user]['secretId'] = secrets_response['secretId']

        with open('users.json', 'w', newline='') as outfile:
            json.dump(self.users, outfile)

    @pytest.mark.TemplateResponsibilityGroup
    def test_responsibility_group(self):
        # Наполнение self.users данными из файла users.json
        with open('users.json') as json_file:
            self.users = json.load(json_file)

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
                response = self.APP.api_responsibility_groups.put_responsibility_groups_id(parent_id, parent_group_body)
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
                    parent_id_2 = self.APP.api_responsibility_groups.put_responsibility_groups_id(group["id"], parent_group_body)['id']
                    assert 'errors' not in parent_id_2
                    print(f"Обновляем каталог (Automation responsibility groups)")
                # Если среди каталогов нет нужного - создаём
                else:
                    response = self.APP.api_responsibility_groups.delete_responsibility_groups_id_users(group["id"])
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
                    response = self.APP.api_responsibility_groups.put_responsibility_groups_id(group['id'], body)
                    assert 'errors' not in response
                    print(f"Обновляем ГО - {group_name}")
                    group_id = group['id']
                    flag = True
                    # В найденой и обновленной ГО, берем список пользователей (только активных)
                    users_list = self.APP.api_responsibility_groups.post_responsibility_groups_id_users_filter(group['id'], {"skip": 0, "take": 100, "isDeleted": False})["items"]
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
                            self.APP.api_responsibility_groups.post_responsibility_groups_id_users(group['id'], body)
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
                    self.APP.api_responsibility_groups.post_responsibility_groups_id_users(group['id'], body)
                    print(f"Пользователь {user_name_template} в ГО {group_name} - добавлен")

            self.RG[group_name].append(group_id)

        with open('responsibility_groups.json', 'w', newline='') as outfile:
            json.dump(self.RG, outfile)

    @pytest.mark.TemplateServiceCatalogs
    def test_service_catalogs(self):
        # Чтение данных из файла о созданных ГО
        with open('responsibility_groups.json') as json_file:
            self.RG = json.load(json_file)
        # Чтение данных из файла о созданных пользователях
        with open('users.json') as json_file:
            self.users = json.load(json_file)

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
        service_catalogs_list = self.APP.api_service_catalogs.post_service_catalogs_filter_parent_tree_list(body)['items']
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
                parentId = self.APP.api_service_catalogs.put_service_catalogs_id(service['id'], body)['id']
                service_flag = True
                print(f"Корневой каталог обновлен \"{body['name']}\"")
                break
        # Если корневой элемент не найден - создаём
        if service_flag is False:
            body = {
                "parentId": None,
                "name": "Отдел тестирования Гандивы",
            }
            parentId = self.APP.api_service_catalogs.post_service_catalogs(body)['id']
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
        catalogs_list = self.APP.api_service_catalogs.post_service_catalogs_filter_parent_tree_list(body)['items']
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
                catalogs_id = self.APP.api_service_catalogs.put_service_catalogs_id(catalog['id'], body)['id']
                catalogs_flag = True
                print(f"Под. каталог обновлен \"{body['name']}\"")
                break
        if catalogs_flag is False:
            body = {
                "parentId": parentId,
                "name": 'Automation service catalogs',
            }
            catalogs_id = self.APP.api_service_catalogs.post_service_catalogs(body)['id']
            print(f"Под. каталог создан \"{body['name']}\"")

        # получить список услуг
        body = {
            "skip": 0,
            "take": 100,
            "parentId": catalogs_id,
        }
        service_list = self.APP.api_service_catalogs.post_service_catalogs_filter_parent_tree_list(body)
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

                    self.APP.api_gandiva_services.put_gandiva_services_id(service_l['id'], self.service_template[service_t])
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

                self.APP.api_gandiva_services.post_gandiva_services(self.service_template[service_t])
                print(f"Создание услуги {self.service_template[service_t]['name']}")

    def add_responsibility_groups(self, name, parentId=None, isActive=True):
        group_body = {
            "name": f"{name}",
            "parentId": f"{parentId}",
            "isActive": isActive,
        }
        return self.APP.api_responsibility_groups.post_responsibility_groups(group_body)

    def group_search(self, parent_id=None):
        filter_body = {
            "skip": 0,
            "take": 1000,
            "parentId": parent_id,
        }
        return self.APP.api_responsibility_groups.post_responsibility_groups_tree(filter_body)
