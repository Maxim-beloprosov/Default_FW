class GroupData:

    response = None
    access_token = ''
    token_type = ''
    expires_in = ''
    refresh_token = ''
    status_code = ''
    id_uploaded_file = ''

    Status_ticket = {
        'request_and_task': {
            'RUS': {
                'В работе': 'В работе',
                'В проверке': 'В проверке',
                'Отменена': 'Отменена',
                'В ожидании': 'В ожидании',
                'В ожидании предшественника': 'В ожидании предшеств.',
                'На согласовании': 'На согласовании',
                'Отклонена': 'Отклонена',
                'На уточнении у иниц.': 'На уточнении у иниц.',
                'На уточнении у исп.': 'На уточнении у исп.',
                'Закрыта': 'Закрыта'
            },
            'ENG': {
                'В работе': 'Active',
                'В проверке': 'Resolved',
                'Отменена': 'Canceled',
                'В ожидании': 'Waiting',
                'В ожидании предшественника': 'WaitingPrevious',
                'На согласовании': 'Agreement',
                'Отклонена': 'Rejected',
                'На уточнении у иниц.': 'InitiatorClarification',
                'На уточнении у исп.': 'ContractorClarification',
                'Закрыта': 'Closed'
            }
        },
        'project': {
            'RUS': {
                'В работе': 'В работе',
                'В проверке': 'В проверке',
                'Отменён': 'Отменён',
                'В ожидании': 'В ожидании',
                'В ожидании предшественника': 'В ожидании предшеств.',
                'На согласовании': 'На согласовании',
                'Отклонён': 'Отклонён',
                'На уточнении у иниц.': 'На уточнении у иниц.',
                'На уточнении у исп.': 'На уточнении у исп.',
                'Закрыт': 'Закрыт'
            }
        },
        'ENG': {
            'В работе': 'Active',
            'В проверке': 'Resolved',
            'Отменено': 'Canceled',
            'В ожидании': 'Waiting',
            'В ожидании предшественника': 'WaitingPrevious',
            'На согласовании': 'Agreement',
            'Отклонено': 'Rejected',
            'На уточнении у иниц.': 'InitiatorClarification',
            'На уточнении у исп.': 'ContractorClarification',
            'Закрыта': 'Closed'
        }
    }

    g1_Status_ticket = {
        'Request': {
            'ENG': {
                'None': 0,
                'New': 1,
                'Pending': 2,
                'Agreement': 3,
                'Clarification': 4,
                'Reject': 5,
                'WorkInProgress': 6,
                'Canceled': 7,
                'Resolved': 8,
                'Closed': 9,
                'WaitPending': 10,
                'WaitDependency': 11,
                'WaitPlanPublishing': 12,
                'ContractorClarification': 13
            },
            'RUS': {
                'Отсутствует': 0,
                'Новый': 1,
                'На рассмотрении': 2,
                'На согласовании': 3,
                'На уточнении': 4,
                'Отклонена': 5,
                'В работе': 6,
                'Отменено': 7,
                'Проверка выполнения': 8,
                'Закрыта': 9,
                'Ожидает': 10,
                'Ожидает предшественника': 11,
                'Ожидает публикации плана': 12,
                'На уточнении у исполнителя': 13
            }
        },
        'Task': {
            'ENG': {
                'None': 0,
                'New': 1,
                'WorkInProgress': 2,
                'Closed': 3,
                'Canceled': 4,
                'Resolved': 5,
                'WaitDependency': 6,
                'WaitPlanPublishing': 7,
                'Agreement': 8,
                'WaitPending': 9,
            },
            'RUS': {
                'Не установлен': 0,
                'Новая': 1,
                'В работе': 2,
                'Закрыта': 3,
                'Отменена': 4,
                'Проверка выполнения': 5,
                'Ожидает предшественника': 6,
                'Ожидает публикации плана': 7,
                'На согласовании': 8,
                'Ожидает': 9
            }
        },
        'WEB': {
                'В работе': 'В работе',
                'Проверка выполнения': 'Проверка выполнения',
                'Отменено': 'Отменено',
                'Ожидает': 'Ожидает',
                'В ожидании предшественника': 'В ожидании предшеств.',
                'На согласовании': 'На согласовании',
                'Отклонена': 'Отклонена',
                'На уточнении у инициатора': 'На уточнении у инициатора',
                'На уточнении у исполнителя': 'На уточнении у исполнителя',
                'Закрыта': 'Закрыта'
        }
    }

    g1_tickets_actions = {
        'ENG': {
            'None': 0,
            'ToPending': 1,
            'Approve': 2,
            'Reject': 3,
            'ToWork': 4,
            'ToResolve': 5,
            'ToRework': 6,
            'Close': 7,
            'Cancel': 8,
            'AssignToSelf': 9,
            'CancelClarification': 10,
            'AppealToHigherChief': 11,
            'Escalate': 12
        },
        'RUS': {
            'Действие не выбрано': 0,
            'Передать на рассмотрение': 1,
            'Согласовать': 2,
            'Отклонить': 3,
            'Взять в работу': 4,
            'Отправить на проверку': 5,
            'Вернуть на доработку': 6,
            'Оценить и закрыть': 7,
            'Отменить заявку': 8,
            'Назначить заявку на себя': 9,
            'Отменить уточнение': 10,
            'Апеллировать вышестоящему': 11,  # Только для заявок
            'Эскалировать заявоку': 12
        }
    }

    g1_result_status = {
        'ENG': {
            'Success': 0,
            'Error': 1
        },
        'RUS': {
            'Успех': 0,
            'Ошибка': 1
        }
    }

    g1_clarification_type = {
        'ENG': {
            'ToInitiator': 0,
            'ToContractor': 1
        },
        'RUS': {
            'Уточнение инициатору': 0,
            'Уточнение исполнителю': 1
        }
    }

    g1_copy_mask = {
        'Task': {
            'ENG': {
                'None': 0,
                'CopySubject': 1,
                'CopyDescription': 2,
                'CopyApprovers': 4,
                'CopyAttachments': 8,
                'CopyObservers': 16,
                'CopyToDoList': 32
            },
            'RUS': {
                'Норматив': 1,
                'Описание': 2,
                'согласующие': 4,
                'Вложения': 8,
                'Обозреватели': 16,
                'Список дел': 32
            }
        }
    }

    g1_approver_status = {
        'ENG': {
            'None': 0,
            'Pending': 1,
            'Clarification': 2,
            'Approved': 3,
            'Reject': 4,
            'Cancel': 5
        },
        'RUS': {
            'Не установлен': 0,
            'Ожидает согласования': 1,
            'На уточнении у инициатора': 2,
            'Согласовано': 3,
            'Отклонена': 4,
            'Отменено': 5
        }
    }

    users = {
        'test_Boss03': {
            'user_id': "",
            'Login': "testboss03",
            'Password': "Qwerty1",
            'secret': "jjwqtpBHllk3HDpwxsrZAGAzAFogywuOctGS7Y9cSFZxFDJP+4pUWStOvyxA2L7i",
            'secretId': "c48b2a09-7dc9-48af-976d-f8c2c2dfdbc5",
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
            'secret': "yssR4L+wH3ic3DeYPTqC1nWr9i1rGgfD/8JQ1uLf56jfMG+lzji6ROn+6AmM+xEc",
            'secretId': "1ce73cae-38dd-426a-b6f7-a5152557817f",
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
            'secret': "bm+GOy/X8+8Y7vjoSYGSGalocUYkNqRSWlHMMnX5zMkH9aaASOmo4y4rbsuWtP9Z",
            'secretId': "f8f79bd3-15a5-4867-990e-4330a1b77a91",
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
            'secret': "H/r5xm0QmoWZWa8m4ZAWJZGJlSRGfdQSw4ObjK1eIW/DuK1iopUmeh6Su15/sWoq",
            'secretId': "70ae0c60-391b-44d4-8c0d-0d26e7883722",
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
            'secret': "SI60lu7o6drE7JlzKQXNiFWykCaNMI+bymTdvV8MSspJHsvktINsfjsMkIkli5Xh",
            'secretId': "44982fda-52b8-43ac-8790-d6a4f8f452ae",
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
            'secret': "mf0/zENsRwUDzdPeioI9qz+bccv1TaAHd1eLh7juAC/5EsKCf1EXkcTxgiDr8HwS",
            'secretId': "2fff3633-5e2f-4782-b836-f20da98efd81",
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
            'secret': "fAS5MMEqOrWGvQaymI/OaW6OUespDTYk6QNyPC8HOl76yKEFrzpzEgw0zYKQEMLo",
            'secretId': "e7a54c96-b6df-417b-bac8-8b43bb3114f1",
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
            'secret': "CRXg70sQHBTc4xVKh62OCNms29Yd2JaLNKfEFq78Q9VSxwm3NKuDi+TPYbkl7haq",
            'secretId': "d69f4cb8-a2dc-468f-bf90-e66cec437b90",
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
            'secret': "GT8drici38eR2tALHZhFfP6+njuDCi4vAA0QE/63Sap9qst2fPz0YM8lx0e4v/DT",
            'secretId': "8ba0fa19-2df7-4b11-9174-8c1bf057ca02",
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
            'secret': "QU5KIW3GUAOzEuFIt2yY9Y3FM5EQrG2Yt+DL3vyfCAJyFWhHh8fXcgIE+puuMoyO",
            'secretId': "2b9673ee-7d6d-4b65-b99e-681a95f7cea7",
            'SyncAD': False,

            'Email': "gandiva_test_user7@mail.ru",
            'EmailPas': "",
            'EmailExternalPas': "",

            'Name': "Test",
            'Surname': "UserSeven",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "test_Boss03",
            'ActualAddressId': "",
        },
        'test_user08': {
            'user_id': "",
            'Login': "testuser08",
            'Password': "Qwerty1",
            'secret': "rF2GoecgTlCkshyhnZJlm+i7tjKreaEbSqpUz5rZYz6MYB+JvCm/bNodTXLAI+dd",
            'secretId': "65f9a00b-0cd0-47a4-86d0-e24dca423516",
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
            'secret': "L7922r+jy1fvTEmxgVKs72sPRMu92NkMKAcGAfXyj73HSmknA8fAnI4KIf0Qr9Zq",
            'secretId': "bf3e035f-6988-410d-96ca-e2f83e836a61",
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
            'secret': "VtMA1rpL3Emn0uUcp1Cfj0mbbmflYP1MSKy743cCwoRi84tiZSXreIjjcIkXI2up",
            'secretId': "406ec096-e968-4a3e-b7b7-84fbd5db189d",
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
            'secret': "Xq7ppwSnmhq5QfeRYC9C6K2bs6bNYGyr/msxrwAPJJwl5ZWCmK6f2PZ+Tf8vgMhG",
            'secretId': "358306aa-0c97-4f14-91d3-cfc40109fe54",
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
            'secret': "WCn8XGT4zXzjehWW2eHlhzaLdJqValx7fuvDqq9IAmDSdUvdvHqGnahSZf/2Wiom",
            'secretId': "7ea46e4f-825a-4489-81f7-73466e6c7889",
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
            'secret': "UiUeMQ7UsI33tMEkRVV9GSh3ct//vlDnn3XCaUJzOrlByonAuxnZmNX7cV7yOHQ5",
            'secretId': "5e73c636-9e87-476a-869e-15568d2a4210",
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
            'secret': "nCNrMJ5ZCFuCIlCOSqZlwaFlgZDgSLFmOeWfl3NKtc+2EHUNw975fY74WX4kl/tZ",
            'secretId': "28e93a0a-2b0d-4614-a1c1-ba6b708df7a5",
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
        'test_user15': {
            'user_id': "",
            'Login': "test_user15",
            'Password': "Qwerty1",
            'secret': "sb4Tmo97ShGu7VO+eWjV3rFk88GXOo3taNCqFH/B6QwBvps9l4Q80parUrdoWLrR",
            'secretId': "a13bcabb-1055-432b-ae04-41b6b3949206",
            'SyncAD': False,

            'Email': "test_user15@mail.ru",
            'EmailPas': "Goodpass123",
            'EmailExternalPas': "",

            'Name': "Test",
            'Surname': "UserFifteen",
            'MiddleName': "Automation",
            'Status': "Work",
            'Manager': "",
            'ActualAddressId': "",
        },
        'test_api_user': {
            'user_id': "",
            'Login': "testapiuser",
            'Password': "Qwerty1",
            'secret': "A8YBnMNDJNRexHg8+gWqvw7HTMTRbLHkW1eF1NjHEFwZxOnpn43XOCcBGpm19UQ2",
            'secretId': "",
            'SyncAD': False,

            'Email': "gandiva_test_api_user1@mail.ru",
            'EmailPas': "QEADZCqeadzc22",
            'EmailExternalPas': "",

            'Name': "User",
            'Surname': "TestApi",
            'MiddleName': "",
            'Status': "Work",
            'Manager': "",
            'ActualAddressId': "",
        },
        # 'Boss': {
        #     'user_id': "",
        #     'Login': "TestBoss",
        #     'Password': "Boss",
        #     'secret': "",
        #     'secretId': "",
        #     'SyncAD': False,
        #
        #     'Email': "gandiva_test_boss1@mail.ru",
        #     'EmailPas': "",
        #     'EmailExternalPas': "",
        #
        #     'Name': "Пабло",
        #     'Surname': "Эскобар",
        #     'MiddleName': None,
        #     'Status': "Work",
        #     'Manager': "",
        #     'ActualAddressId': "",
        # },
    }

    data_for_adding_user = {
        'test_users': {
            'test_user': {
                'id': "",
                'login': 'automation_api_test_',
                'name': 'testName',
                'surname': 'testSurname',
                'middleName': 'testMiddleName',
                'email': '_automation_api@test.ru',
                'mobilePhone': '+791010700',
                'cityPhone': '8 (000) 200-00-',
                'internalPhone': '8 (000) 200-00-'
            },
            'new_test_user': {
                'id': "",
                'name': 'newTestName',
                'surname': 'newSurname',
                'middleName': 'newTestMiddleName',
                'email': 'new_automation_api@test.ru',
                'mobilePhone': '+79000000',
                'cityPhone': '8 (999) 200-00-00',
                'internalPhone': '8 (999) 200-00-00'
            }
        },
        'organizations': {
            'test_organization': {
                'id': ""
            }
        },
        'departments': {
            'test_department': {
                'id': ""
            }
        },
        'positions': {
            'test_position': {
                'id': ""
            }
        },
        'addresses': {
            'test_address': {
                'id': ""
            }
        },
        'photos': {
            'test_photo': {
                'id': ""
            }
        }
    }

    groups = ['Отдел тестирования Гандивы (Automation)', 'Automation responsibility groups']

    RG = {
        'Группа_тестирования_№1': ['test_Boss01', 'test_user01', 'test_user02', 'test_user03', 'test_user04'],
        'Группа_тестирования_№2': ['test_Boss02', 'test_user05', 'test_user06'],
        'Группа_тестирования_№3': ['test_Boss01', 'test_Boss02', 'test_Boss03', 'test_user07', 'test_user01']
    }

    Attachments = {
        'Тестовое фото №1': {
            'name': 'Тестовое фото №1',
            'Id': ''
        },
        'Тестовое фото №2': {
            'name': 'Тестовое фото №2',
            'Id': ''
        }
    }

    service_template_g1 = {
        'Тестовый_Тип_1': {
            'department': 'Отдел тестирования Гандивы',
            'category': 'Программное обеспечение',
            'type': 'MS GANDIVA',
            'job_type': 'Тестовый_Тип_1',
            'Id': '',
            "typeType": "Normal",
            "note": False,
            "initiatorAccessType": "All",
            "isActive": True,
            "isBossApprover": False,
            "isBossObserver": False,
            "workScheduleOverridden": False,
            "approveTimeNormative": 14400,
            "initiatorTimeNormative": 2880,
            "initiatorTimeNotify": 2880,
            "initiatorTimeWait": 2880,
            "approverUsers": [],
            "observerUsers": [],
            "serviceResponsibilityGroups": [{
                "responsibilityGroupId": 'Тест Гандивы 1',
                "timeNormative": 21600,
                "timeHard": 21600,
                "orderNumber": 21600
            }
            ]
        },
        #'Тестовый_Тип_2',
        'Тестовый_Тип_3': {
            'department': 'Отдел тестирования Гандивы',
            'category': 'Программное обеспечение',
            'type': 'MS GANDIVA',
            'job_type': 'Тестовый_Тип_3',
            'Id': '',
            "typeType": "Normal",
            "note": "Примечание Тест",
            "initiatorAccessType": "All",
            "isActive": True,
            "isBossApprove": False,
            "isBossObserver": False,
            "workScheduleOverridden": False,
            "approveTimeNormative": 14400,
            "initiatorTimeNormative": 2880,
            "initiatorTimeNotify": 2880,
            "initiatorTimeWait": 2880,
            "approveUsers": [],
            "observerUsers": [],
            "serviceResponsibilityGroups": [{
                "responsibilityGroupId": 'Тест Гандивы 1',
                "timeNormative": 21600,
                "timeHard": 21600,
                "orderNumber": 21600
            }
            ]
        },
        #'Тестовый_Тип_4',
        #'Тестовый_Тип_5',
        #'Тестовый_Тип_6_Лист_допуска',
        #'Тестовый_Тип_7_Лист_допуска',
        #'Тестовый_Тип_8_Лист_допуска',
        #'Тестовый_Тип_9_Групповая_заявка',
        #'Тестовый_Тип_10_Групповая_заявка',
        #'Тестовый_Тип_11_Групповая_заявка',
        #'Тестовый_Тип_12_Заявка_по_телефону',
        #'Тестовый_Тип_13_Заявка_с_уволенным_согласующим',
        #'Тестовый_Тип_14_Доп_поля',
        #'Тестовый_Тип_15_обязательные_доп_поля',
        #'Тестовый_Тип_11_Групповая_заявка',
        'Тип для тестирования(2)': {
            'department': 'Отдел тестирования Гандивы',
            'category': 'Программное обеспечение',
            'type': 'MS GANDIVA',
            'job_type': 'Тип для тестирования(2)',
        },

    }


    service_template = {
        'AutomationService Тестовый Тип 1': {
            "name": 'AutomationService Тестовый Тип 1',
            'Id': '',
            'catalogId': '',
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
                "responsibilityGroupId": 'Группа_тестирования_№1',
                "timeNormative": 21600,
                "timeHard": 21600,
                "orderNumber": 21600
            }
            ]
        },
        'AutomationService Тестовый Тип 2': {
            "name": "AutomationService Тестовый Тип 2",
            'Id': '',
            'catalogId': '',
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
                "responsibilityGroupId": 'Группа_тестирования_№1',
                "timeNormative": 21600,
                "timeHard": 21600,
                "orderNumber": 21600
            }
            ],
        },
        'AutomationService Тестовый Тип 3': {
            "name": 'AutomationService Тестовый_Тип_3',
            'Id': '',
            'catalogId': '',
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
                "responsibilityGroupId": 'Группа_тестирования_№2',
                "timeNormative": 21600,
                "timeHard": 21600,
                "orderNumber": 21600
            }
            ]
        },
        'AutomationService Тестовый Тип 4': {
            "name": 'AutomationService Тестовый Тип 4',
            'Id': '',
            'catalogId': '',
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
                "responsibilityGroupId": 'Группа_тестирования_№2',
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
        'AutomationService Тестовый Тип 12 Заявка по телефону': {
            "name": 'AutomationService Тестовый Тип 12 Заявка по телефону',
            'Id': '',
            'catalogId': '',
            "typeType": "PhoneRequest",
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
                "responsibilityGroupId": 'Группа_тестирования_№1',
                "timeNormative": 21600,
                "timeHard": 21600,
                "orderNumber": 21600
            }
            ]
        },
        # 'Тестовый_Тип_13_Заявка_с_уволенным_согласующим': '',
        'AutomationService Тестовый Тип 14': {
            "name": 'AutomationService Тестовый Тип 14',
            'Id': '',
            'catalogId': '',
            "typeType": "Normal",
            "initiatorAccessType": "All",
            "isActive": True,
            "isBossApprove": False,
            "isBossObserver": False,
            "workScheduleOverridden": False,
            "approveTimeHard": 21600,
            "approveTimeNormative": 14400,
            "initiatorTimeNormative": 2880,
            "initiatorTimeNotify": 2880,
            "initiatorTimeWait": 2880,
            "approveUsers": [],
            "observerUsers": [],
            "serviceResponsibilityGroups": [{
                "responsibilityGroupId": 'Группа_тестирования_№1',
                "timeNormative": 21600,
                "timeHard": 21600,
                "orderNumber": 21600
            }
            ],
            'customFieldCollection': [
            {
                "sourceId": '6deab898-fe05-11ec-ab4a-12ae93f3e60d', "sourceType": "GandivaService", "customFieldSources": [
                {
                    "sourceType": "GandivaService",
                    "sourceId": '6deab898-fe05-11ec-ab4a-12ae93f3e60d',
                }
            ],
                "data": {
                    "defaultSettingType": "None",
                    "type": 'Text',
                    "value": ''
                },
            }
        ],
        },
        # 'Тестовый_Тип_15_обязательные_доп_поля': '',
        # 'Тестовый_Тип_16_согласующий_в_отпуске': '',
        # 'Тестовый_Тип_17_обозреватель_в_отпуске': '',
        'Тестовый_Тип_18_Добавлять_руководителя_инициатора_согласующим': {
            "name": 'Тестовый_Тип_18_Добавлять_руководителя_инициатора_согласующим',
            'Id': '',
            'catalogId': '',
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
                "responsibilityGroupId": 'Группа_тестирования_№1',
                "timeNormative": 21600,
                "timeHard": 21600,
                "orderNumber": 21600
            }
            ]
        },
        'Тестовый_Тип_19_Добавлять_руководителя_инициатора_обозревателем': {
            "name": 'Тестовый_Тип_19_Добавлять_руководителя_инициатора_обозревателем',
            'Id': '',
            'catalogId': '',
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
                "responsibilityGroupId": 'Группа_тестирования_№1',
                "timeNormative": 21600,
                "timeHard": 21600,
                "orderNumber": 21600
            }
            ]
        },
        'AutomationService Тестовый Тип 20': {
            "name": 'AutomationService Тестовый Тип 20',
            'Id': '',
            'catalogId': '',
            "typeType": "Normal",
            "initiatorAccessType": "All",
            "isActive": True,
            "isBossApprove": False,
            "isBossObserver": False,
            "workScheduleOverridden": False,
            "approveTimeNormative": 2160,
            "approveTimeHard": 2160,
            "initiatorTimeNormative": 2880,
            "initiatorTimeNotify": 2880,
            "initiatorTimeWait": 2880,
            "approveUsers": [],
            "observerUsers": [],
            "serviceResponsibilityGroups": [{
                "responsibilityGroupId": 'Група_тестирования_№1',
                "timeNormative": 21600,
                "timeHard": 21600,
                "orderNumber": 1
            },
            {
                "responsibilityGroupId": "Група_тестирования_№2",
                "timeNormative": 14400,
                "timeHard": 14400,
                "orderNumber": 2
            }
            ]
        },
    }

    secret_key = {
        "Testing": {
            "test_Boss03": {
                "user_id": "27d05b34-cd62-11ec-a596-8e8a7cded363",
                "secret": "jjwqtpBHllk3HDpwxsrZAGAzAFogywuOctGS7Y9cSFZxFDJP+4pUWStOvyxA2L7i",
            },
            "test_Boss02": {
                "user_id": "282aecc0-cd62-11ec-9b11-8e8a7cded363",
                "secret": "yssR4L+wH3ic3DeYPTqC1nWr9i1rGgfD/8JQ1uLf56jfMG+lzji6ROn+6AmM+xEc",
            },
            "test_Boss01": {
                "user_id": "287b2ae6-cd62-11ec-9ea0-8e8a7cded363",
                "secret": "bm+GOy/X8+8Y7vjoSYGSGalocUYkNqRSWlHMMnX5zMkH9aaASOmo4y4rbsuWtP9Z",
            },
            "test_user01": {
                "user_id": "28c9a612-cd62-11ec-83a4-8e8a7cded363",
                "secret": "H/r5xm0QmoWZWa8m4ZAWJZGJlSRGfdQSw4ObjK1eIW/DuK1iopUmeh6Su15/sWoq",
            },
            "test_user02": {
                "user_id": "291f50ee-cd62-11ec-b84e-8e8a7cded363",
                "secret": "SI60lu7o6drE7JlzKQXNiFWykCaNMI+bymTdvV8MSspJHsvktINsfjsMkIkli5Xh",
            },
            "test_user03": {
                "user_id": "297076f4-cd62-11ec-a111-8e8a7cded363",
                "secret": "mf0/zENsRwUDzdPeioI9qz+bccv1TaAHd1eLh7juAC/5EsKCf1EXkcTxgiDr8HwS",
            },
            "test_user04": {
                "user_id": "29bd82be-cd62-11ec-83a4-8e8a7cded363",
                "secret": "fAS5MMEqOrWGvQaymI/OaW6OUespDTYk6QNyPC8HOl76yKEFrzpzEgw0zYKQEMLo",
            },
            "test_user05": {
                "user_id": "2a0d1464-cd62-11ec-b84e-8e8a7cded363",
                "secret": "CRXg70sQHBTc4xVKh62OCNms29Yd2JaLNKfEFq78Q9VSxwm3NKuDi+TPYbkl7haq",
            },
            "test_user06": {
                "user_id": "2a5af6f2-cd62-11ec-a111-8e8a7cded363",
                "secret": "GT8drici38eR2tALHZhFfP6+njuDCi4vAA0QE/63Sap9qst2fPz0YM8lx0e4v/DT",
            },
            "test_user07": {
                "user_id": "2aab9936-cd62-11ec-a596-8e8a7cded363",
                "secret": "QU5KIW3GUAOzEuFIt2yY9Y3FM5EQrG2Yt+DL3vyfCAJyFWhHh8fXcgIE+puuMoyO",
            },
            "test_user08": {
                "user_id": "2afd268e-cd62-11ec-b6b3-8e8a7cded363",
                "secret": "rF2GoecgTlCkshyhnZJlm+i7tjKreaEbSqpUz5rZYz6MYB+JvCm/bNodTXLAI+dd",
            },
            "test_user09": {
                "user_id": "2b4fd2c6-cd62-11ec-beef-8e8a7cded363",
                "secret": "L7922r+jy1fvTEmxgVKs72sPRMu92NkMKAcGAfXyj73HSmknA8fAnI4KIf0Qr9Zq",
            },
            "test_user10": {
                "user_id": "2b9e2c0a-cd62-11ec-a4df-8e8a7cded363",
                "secret": "VtMA1rpL3Emn0uUcp1Cfj0mbbmflYP1MSKy743cCwoRi84tiZSXreIjjcIkXI2up",
            },
            "test_user11": {
                "user_id": "2bebf3a4-cd62-11ec-83a4-8e8a7cded363",
                "secret": "Xq7ppwSnmhq5QfeRYC9C6K2bs6bNYGyr/msxrwAPJJwl5ZWCmK6f2PZ+Tf8vgMhG",
            },
            "test_user12": {
                "user_id": "2c3d4754-cd62-11ec-9b11-8e8a7cded363",
                "secret": "WCn8XGT4zXzjehWW2eHlhzaLdJqValx7fuvDqq9IAmDSdUvdvHqGnahSZf/2Wiom",
            },
            "test_user13": {
                "user_id": "2c8dcb16-cd62-11ec-bcfa-8e8a7cded363",
                "secret": "UiUeMQ7UsI33tMEkRVV9GSh3ct//vlDnn3XCaUJzOrlByonAuxnZmNX7cV7yOHQ5",
            },
            "test_user14": {
                "user_id": "2cddd750-cd62-11ec-a0ae-8e8a7cded363",
                "secret": "nCNrMJ5ZCFuCIlCOSqZlwaFlgZDgSLFmOeWfl3NKtc+2EHUNw975fY74WX4kl/tZ",
            },
            "test_user15": {
                "user_id": "5de161fe-3811-11ed-ab63-a2214167e40b",
                "secret": "0FbhXM+ucqF2tGD/7s8zBLwOMoWJOOMK6agtG2RrAtJ3RZc5wy2bQ/AtwsKta9Hq",
            },
            "test_api_user": {
                "user_id": "aef26e5a-ecb5-11ec-b445-fe4aed3ff546",
                "secret": "iuyo0EIT1OQvmgYzXBRCzg8DnE7VJBfRPHMXrz2ICss0jGy86tGuWA0+mI0Ylp9j",
            },
        },
        "feature_development": {
            "test_Boss03": {
                "user_id": "d4b459da-bb11-11ec-9b14-0217dc7a50e7",
                "secret": "V7+DLvj1+Fyk7TM6SU9K4sEhdLcmlIWmUmsWcDov+qIPkRWZvCP4vZiJqExJjve4",
            },
            "test_Boss02": {
                "user_id": "3e75a40a-bb12-11ec-8e8b-0217dc7a50e7",
                "secret": "k4kwP3KVPm5RrgfEipbigGmA1j9SjS+jkujZJDZrle6c89vR4bphz8W0e4YeYLxx",
            },
            "test_Boss01": {
                "user_id": "51679280-bb12-11ec-8ed5-0217dc7a50e7",
                "secret": "d7B9OzjQWu+6fm/Wdq+OZTbm9kpJ8FSlNwvFZE5qIZeIlJrJY4AERecPEQIzjI7c",
            },
            "test_user01": {
                "user_id": "96ba2212-bb12-11ec-8ed5-0217dc7a50e7",
                "secret": "DjjSbcOE7EWt7yHsJCigOPv3Mk+7jP17dFOeOvZ7lMZYapQEi1nsiws2UWK29RMj",
            },
            "test_user02": {
                "user_id": "02399914-bb13-11ec-8ed5-0217dc7a50e7",
                "secret": "lIBC+nCPu9oBFg5KAX0LQLdW1GWazd9Do+lwAHy2lnn/lv/joEWZ2Q539TK3FrE1",
            },
            "test_user03": {
                "user_id": "1982c9a6-bb13-11ec-98ae-0217dc7a50e7",
                "secret": "NZ++rSrydH/DBTMocI87qiJUmZ0i1q1MhFMl1DRnBaJ1sxkk+/+EZ/BgerTKmndb",
            },
            "test_user04": {
                "user_id": "b6cac038-bb13-11ec-bd5d-0217dc7a50e7",
                "secret": "dpMJMm4MskWaXGSWeIsHt5lnJgkq5ifYSnVPS19LH73AF6NwHZtLIcfAShZje54M",
            },
            "test_user05": {
                "user_id": "d7d09b4a-bb13-11ec-bd5d-0217dc7a50e7",
                "secret": "+n/PwLg6lsh+b0xHps5G9VytcALak2CWDJOQOG/8UZ/ZpHwPAt8N+LxVwruPlkbg",
            },
            "test_user06": {
                "user_id": "216f9120-bb14-11ec-9437-0217dc7a50e7",
                "secret": "CrDA5VtlIh7D5Eypxf6GivnGmTeW8YY8/fqwh7sJGcNmzgskJK3HN7XutX65k13v",
            },
            "test_user07": {
                "user_id": "3541a27e-bb14-11ec-b60e-0217dc7a50e7",
                "secret": "TgMvNLTSd1TWsHDOUMt4rE/YdEZt7CNH8G5voKYNfI/mv1VANZieNhdKaoFOl3Fh",
            },
            "test_user08": {
                "user_id": "49338892-bb14-11ec-b931-0217dc7a50e7",
                "secret": "V/SdEpJpiq8mBP2u1NroLbRjBUfY6NBFs5/oCqLlIodcJpQMIcbt5GayHqHsTxxz",
            },
            "test_user09": {
                "user_id": "5cd86e44-bb14-11ec-9437-0217dc7a50e7",
                "secret": "ZRxM+/Pc+sqZT6CBeeImgFbmlP14HImlL6HfB0uoDDbSmrEdtFQLmXJuV+yu6dBL",
            },
            "test_user10": {
                "user_id": "a36fd180-bb14-11ec-882f-0217dc7a50e7",
                "secret": "eCQs4qg+7tr7tBASM00I8U/SqzR4guG8RH2WAi8Gkim6bGeMgV87G2YDEzJIRuyt",
            },
            "test_user11": {
                "user_id": "cd167890-bb14-11ec-882f-0217dc7a50e7",
                "secret": "g/rXaYChrJEF7z0GJiHfwsP57bCo5mUKY3hicG3W738IFRhxlAS3AUXwLdq1lymX",
            },
            "test_user12": {
                "user_id": "529d237e-bb15-11ec-882f-0217dc7a50e7",
                "secret": "rerZPjSWfHHfGsTdMY4BFq21IXR9bJY4fWfIeV0GHz5l/rtGV1y2zy/6yuXV2kbS",
            },
            "test_user13": {
                "user_id": "67113d72-bb15-11ec-bcb5-0217dc7a50e7",
                "secret": "A/kLTJj9BiFoUv5ZiIz6OMoTs/Pbzh9qELZ2JwHfZkImjaD2SJIsxvc9QX5ZtORH",
            },
            "test_user14": {
                "user_id": "79b0240c-bb15-11ec-a7e7-0217dc7a50e7",
                "secret": "dIgK3bjJ9dpz56LqreOeR0ravCWeIKnurYkQlSVWsUnJDHRtDqXI4Cw4OAG0EjFM",
            },
            "test_user15": {
                "user_id": "ed1e6534-33fb-11ed-97ba-6e1013091ccf",
                "secret": "sb4Tmo97ShGu7VO+eWjV3rFk88GXOo3taNCqFH/B6QwBvps9l4Q80parUrdoWLrR",
            },
            "test_api_user": {
                "user_id": "10c37c2c-b0e9-11ec-90da-ae981e1e0fca",
                "secret": "A8YBnMNDJNRexHg8+gWqvw7HTMTRbLHkW1eF1NjHEFwZxOnpn43XOCcBGpm19UQ2",
            },
        },
        "test_compose": {
            "test_Boss03": {
                "user_id": "d6f83c48-13d1-11ed-8ab7-0242ac120003",
                "secret": "k9kkwyQJfkaAAisUAgBL7C8NLjFuB9qp5Tkl4SVJl2v5X6oUo3COY04svnM0mvsK",
            },
            "test_Boss02": {
                "user_id": "d713d624-13d1-11ed-8ab7-0242ac120003",
                "secret": "OHnuBVsLWkArJUynHtd5aMpE9/0Ngx6OFbj3brHotOLhq3z9r/5E+QiEfXqv2Jcg",
            },
            "test_Boss01": {
                "user_id": "d7306a14-13d1-11ed-8ab7-0242ac120003",
                "secret": "4/5MBT6ROaNq9SJfe1zxmNOXH9cZ6rcnW2osUGEyMs9XlkzLhfFqeMIhbqTTWQYM",
            },
            "test_user01": {
                "user_id": "d7483068-13d1-11ed-8ab7-0242ac120003",
                "secret": "LgJNw4/iIVJTGYapIWjKUSr2KgQ7hg0cdZGArGhHXA5ZsnClvWr4/YCXnSBjnZe5",
            },
            "test_user02": {
                "user_id": "d76270fe-13d1-11ed-8ab7-0242ac120003",
                "secret": "ozUwpQ+Keya1ot34lJ0sLns5HQQiOQK2UYJaBcSa3BSE7Sn/+jkShMLR3d/NGOLv",
            },
            "test_user03": {
                "user_id": "d77b9c5a-13d1-11ed-8ab7-0242ac120003",
                "secret": "e2tWR/GEMrIs8NSvPVbg1X9o9U1Jmzrbf7+FTaev+5rzCJM4bCJQoPT8urTOihPp",
            },
            "test_user04": {
                "user_id": "d79999bc-13d1-11ed-8ab7-0242ac120003",
                "secret": "e88p6l13htofSGa9tjExlQa1fPGIFT2ykCIRy21sRaAnK+2WVrvUQuOeGnnmR0Gh",
            },
            "test_user05": {
                "user_id": "d7b052a6-13d1-11ed-8ab7-0242ac120003",
                "secret": "JCBHDQhmauicaNWsIvUFFPCRo3ihttL04ccAzllCjljlnAqPErV1d5w9Jv0dXk8j",
            },
            "test_user06": {
                "user_id": "d7c79a10-13d1-11ed-8ab7-0242ac120003",
                "secret": "BGgLczt+Yf8xmhfEcAiMjXOzwe9/OhBF42YSvsr2/qXQFklXkWVESF6uXTV4BnA6",
            },
            "test_user07": {
                "user_id": "d7e02846-13d1-11ed-8ab7-0242ac120003",
                "secret": "VAsqVkjFbrTTczfSi8Qslrk5FpFyZ6O1wBWtmd0BGpsalKp/gU38L3mTCpwiiY3c",
            },
            "test_user08": {
                "user_id": "d7ff9b5e-13d1-11ed-8ab7-0242ac120003",
                "secret": "ByslFpPpm2TQ7/9Ogjfan/QGu4iWnwl99Tv015eS7jPgOhaM66E7IvxIqZs83Ip6",
            },
            "test_user09": {
                "user_id": "d81cc31e-13d1-11ed-8ab7-0242ac120003",
                "secret": "pf15xJPPXJnJxlW1NBXlsg6qyp4CDkJZMyXbP4SZCO5pGNVg9EZcgyMIy9cuuyIu",
            },
            "test_user10": {
                "user_id": "d83be65e-13d1-11ed-8ab7-0242ac120003",
                "secret": "j077slHoSHol3baSl1m+YFqlnc+4h+q4tpnH/9Hh+zGqV4y5Vz0lw3+euLWAJvW8",
            },
            "test_user11": {
                "user_id": "d85e5054-13d1-11ed-8ab7-0242ac120003",
                "secret": "IaKLbm4tEKg2ORFly6zm3aMLwMDIJgKepzKE6NMBHjzEEQln1M+GMYW+KQMsr1rX",
            },
            "test_user12": {
                "user_id": "d87d3b18-13d1-11ed-8ab7-0242ac120003",
                "secret": "BZn5jngyOyBYMotEj/i7Car7F/Fp/uzOnm+BdC5TNY5XxI/7IxB/f5PkgdS/jQfn",
            },
            "test_user13": {
                "user_id": "d89b0918-13d1-11ed-8ab7-0242ac120003",
                "secret": "ErHcPjNEJqOlItcVd1tj3sTV+xWLhFaSYZqFcrVkewr8q1LoWvl+G96Qhnn/V3UB",
            },
            "test_user14": {
                "user_id": "d8ba7e56-13d1-11ed-8ab7-0242ac120003",
                "secret": "VMZ34Br0GOoWEED08rXZ2Q9ldVz6EsmSRVbIrL/jx2ZZdyEh/DSJkkRSJJwjLmk8",
            },
            "test_api_user": {
                "user_id": "8facf0a6-476c-11ea-bf0a-1c6f6555ae82",
                "secret": "8OydZFzbPoPdo+1C2h+7MQb6+a0VUG6OoWbPejrO/67QOn1UGRdmDPujiZtOUJ6x",
            },
        }
    }

    parent_id_articles = {
        'feature_development': '3d281364-9ff5-4fc5-96aa-7e0a89e01dce',
        'Testing': 'c7254143-a907-44e6-ae62-0b65089868e0'
    }

    g1_users = {
        'Boss2': {
            'Name': 'test',
            'SureName': 'Boss2',
            'log': 'test Boss2',
            'Region': 'Нижний Новгород',
            'Login': 'test_Boss2',
            'Password': 'qwerty',
            'Email': 'gandiva_test_boss2@mail.ru',
            'EmailPassword': 'Asdfgh12',
            'Chief': '',
            'Alternate': '',
            'IsActual': True
        },
            'Boss1': {
            'Name': 'test',
            'SureName': 'Boss1',
            'log': 'test Boss1',
            'Region': 'Нижний Новгород',
            'Login': 'test_Boss1',
            'Password': 'qwerty',
            'Email': 'gandiva_test_boss1@mail.ru',
            'EmailPassword': 'Asdfgh12',
            'Chief': 'test Boss2',
            'Alternate': '',
            'IsActual': True
        },
        'User1': {
            'Name': 'test',
            'SureName': 'user1',
            'log': 'test user1',
            'Region': 'Нижний Новгород',
            'Login': 'test_user1',
            'Password': 'qwerty',
            'Email': 'gandiva_test_user1@mail.ru',
            'EmailPassword': 'Asdfgh12',
            'Chief': 'test Boss1',
            'Alternate': '',
            'IsActual': True
        },
        'User2': {
            'Name': 'test',
            'SureName': 'user2',
            'log': 'test user2',
            'Region': 'Нижний Новгород',
            'Login': 'test_user2',
            'Password': 'qwerty',
            'Email': 'gandiva_test_user2@mail.ru',
            'EmailPassword': 'Asdfgh12',
            'Chief': 'test Boss1',
            'Alternate': '',
            'IsActual': True
        },
        'User3': {
            'Name': 'test',
            'SureName': 'user3',
            'log': 'test user3',
            'Region': 'Нижний Новгород',
            'Login': 'test_user3',
            'Password': 'qwerty',
            'Email': 'gandiva_test_user3@mail.ru',
            'EmailPassword': 'Asdfgh12',
            'Chief': 'test Boss1',
            'Alternate': '',
            'IsActual': True
        },
        'User4': {
            'Name': 'test',
            'SureName': 'user4',
            'log': 'test user4',
            'Region': 'Волгоград',
            'Login': 'test_user4',
            'Password': 'qwerty',
            'Email': 'gandiva_test_user4@mail.ru',
            'EmailPassword': 'Asdfgh12',
            'Chief': 'test Boss1',
            'Alternate': '',
            'IsActual': True
        },
        'User5': {
            'Name': 'test',
            'SureName': 'user5',
            'log': 'test user5',
            'Region': 'Нижний Новгород',
            'Login': 'test_user5',
            'Password': 'qwerty',
            'Email': 'gandiva_test_user5@mail.ru',
            'EmailPassword': 'Asdfgh12',
            'Chief': 'test Boss1',
            'Alternate': '',
            'IsActual': True
        },
        'User6': {
            'Name': 'test',
            'SureName': 'user6',
            'log': 'test user6',
            'Region': 'Нижний Новгород',
            'Login': 'test_user6',
            'Password': 'qwerty',
            'Email': 'gandiva_test_user6@mail.ru',
            'EmailPassword': 'Asdfgh12',
            'Chief': 'test Boss1',
            'Alternate': '',
            'IsActual': True
        },
        'User7': {
            'Name': 'test',
            'SureName': 'user7',
            'log': 'test user7',
            'Region': 'Нижний Новгород',
            'Login': 'test_user7',
            'Password': 'qwerty',
            'Email': 'gandiva_test_user7@mail.ru',
            'EmailPassword': 'Asdfgh12',
            'Chief': 'test Boss1',
            'Alternate': '',
            'IsActual': True
        },
        'User8': {
            'Name': 'test',
            'SureName': 'user8',
            'log': 'test user8',
            'Region': 'Нижний Новгород',
            'Login': 'test_user8',
            'Password': 'qwerty',
            'Email': 'gandiva_test_user8@mail.ru',
            'EmailPassword': 'Asdfgh12',
            'Chief': 'test Boss1',
            'Alternate': '',
            'IsActual': False
        },
        'User9': {
            'Name': 'test',
            'SureName': 'user9',
            'log': 'test user9',
            'Region': 'Нижний Новгород',
            'Login': 'test_user9',
            'Password': 'qwerty',
            'Email': 'gandiva_test_user9@mail.ru',
            'EmailPassword': 'Asdfgh12',
            'Chief': 'test Boss2',
            'Alternate': '',
            'IsActual': False
        },
        'User10': {
            'Name': 'test',
            'SureName': 'user10',
            'log': 'test user10',
            'Region': 'Все регионы',
            'Login': 'test_user10',
            'Password': 'qwerty',
            'Email': 'gandiva_test_user10@mail.ru',
            'EmailPassword': 'Asdfgh12',
            'Chief': '',
            'Alternate': '',
            'IsActual': True
        },
        'User11': {
            'Name': 'test',
            'SureName': 'user11',
            'log': 'test user11',
            'Region': 'Все регионы',
            'Login': 'test_user11',
            'Password': 'qwerty',
            'Email': 'gandiva_test_user11@mail.ru',
            'EmailPassword': 'Asdfgh12',
            'Chief': '',
            'Alternate': '',
            'IsActual': True
        },
        'SystemOperator': {
            'Name': 'test',
            'SureName': 'SystemOperator',
            'log': 'system operator',
            'Region': 'Все регионы',
            'Login': 'system_operator',
            'Password': 'qwerty',
            'Email': '',
            'EmailPassword': '',
            'Chief': '',
            'Alternate': '',
            'IsActual': True
        },
    }
