class G1Settings:

    # branch = 'Stage'
    # branch = 'StageForm'
    branch = 'StageNpg'
    # branch = 'Test'
    # branch = 'TestForm'
    # branch = 'TestNpg'
    # branch = 'test_compose'

    # API
    Authorization = True
    content_type = True
    use_internal_link_in_api = False

    GLOBAL = {
        'Stage': {
            'Name': 'Stage',
            'main_page': 'https://web-stage.gandiva.ru/',
            'Internal_Link': 'http://agat-test-tssm:93/',
            'API': {
                'Token_url': "",
                'Client_id': '',
                'Client_secret': '',
                'Internal_Link': 'http://agat-test-tssm:83/',
                'External_Link': 'https://api-stage.gandiva.ru/',
                'AUTH_URL': 'https://api-stage.gandiva.ru/Token',
                'CERT_FILE': '',
                'client_id': '',
                'realm_name': '',
            },
            'SQL_SERVER': {
                'TypeSQL': 'SQL_Server',
                'SERVER': '192.168.1.162',
                'PORT': 1433,
                'DATABASE': 'TSSM_Release',
                'login': 'TSSMOwner',
                'password': 'renwOMSST',
                'DRIVER': '{SQL Server Native Client 11.0}',
            },
            'USERS': {
                'SystemOperator': {
                    'Name': "",
                    'User_id': "",
                    'client_secret': "",
                    'Login': "test1",
                    'ApiLogin': "agat\\test1",
                    'Password': "Q258999m",
                    },
            }
        },

        'StageForm': {
            'Name': 'StageForm',
            'main_page': 'https://web-stage-form.gandiva.ru/',
            'Internal_Link': 'http://agat-test-tssm:94/',
            'API': {
                'Token_url': "",
                'Client_id': '',
                'Client_secret': '',
                'Internal_Link': 'http://agat-test-tssm:84/',
                'External_Link': 'https://api-stage-form.gandiva.ru/',
                'AUTH_URL': 'https://auth-feature-testing1.gandiva.ru/connect/token',
                'CERT_FILE': '',
                'client_id': '',
                'realm_name': '',
            },
            'SQL_SERVER': {
                'TypeSQL': '',
                'SERVER': '',
                'PORT': 2424,
                'DATABASE': '',
                'login': '',
                'password': '',
                'DRIVER': '',
            },
            'USERS': {
                'SystemOperator': {
                    'Name': "",
                    'User_id': "",
                    'client_secret': "",
                    'Login': "admin",
                    'Password': "admin",
                    },
            }
        },

        'StageNpg': {
            'Name': 'StageNpg',
            'main_page': 'https://web-stage-npg.gandiva.ru/',
            'Internal_Link': 'http://agat-test-tssm:8093/',
            'API': {
                'Token_url': "",
                'Client_id': '',
                'Client_secret': '',
                'Internal_Link': 'http://agat-test-tssm:99/',
                'External_Link': 'https://api-stage-npg.gandiva.ru/',
                'AUTH_URL': 'https://api-stage-npg.gandiva.ru/Token',
                'CERT_FILE': '',
                'client_id': '',
                'realm_name': '',
            },
            'SQL_SERVER': {
                'TypeSQL': 'PostgreSQL',
                'SERVER': '192.168.0.95',
                'PORT': 5432,
                'DATABASE': 'gandiva_stage',
                'login': 'sa',
                'password': 'renwOMSST',
                'DRIVER': '',
            },
            'USERS': {
                'SystemOperator': {
                    'Name': "",
                    'User_id': "",
                    'client_secret': "",
                    'Login': "test1",
                    'ApiLogin': "agat\\test1",
                    'Password': "Q258999m",
                    },
            }
        },

        'Test': {
            'Name': 'Test',
            'main_page': 'https://web-test.gandiva.ru/',
            'Internal_Link': 'http://agat-test-tssm:96/',
            'API': {
                'Token_url': "",
                'Client_id': '',
                'Client_secret': '',
                'Internal_Link': 'http://agat-test-tssm:86/',
                'External_Link': 'https://api-test.gandiva.ru/',
                'AUTH_URL': 'https://api-test.gandiva.ru/Token',
                'CERT_FILE': '',
                'client_id': '',
                'realm_name': '',
            },
            'SQL_SERVER': {
                'TypeSQL': '',
                'SERVER': '',
                'PORT': 2424,
                'DATABASE': '',
                'login': '',
                'password': '',
                'DRIVER': '',
            },
            'USERS': {
                'SystemOperator': {
                    'Name': "",
                    'User_id': "",
                    'client_secret': "",
                    'Login': "test1",
                    'ApiLogin': "agat\\test1",
                    'Password': "Q258999m",
                },
            }
        },

        'TestForm': {
            'Name': 'TestForm',
            'main_page': 'https://web-test-form.gandiva.ru/',
            'Internal_Link': 'http://agat-test-tssm:94/',
            'API': {
                'Token_url': "",
                'Client_id': '',
                'Client_secret': '',
                'Internal_Link': 'http://agat-test-tssm:87/',
                'External_Link': 'https://api-test-form.gandiva.ru/',
                'AUTH_URL': 'https://api-test-form.gandiva.ru/Token',
                'CERT_FILE': '',
                'client_id': '',
                'realm_name': '',
            },
            'SQL_SERVER': {
                'TypeSQL': '',
                'SERVER': '',
                'PORT': 2424,
                'DATABASE': '',
                'login': '',
                'password': '',
                'DRIVER': '',
            },
            'USERS': {
                'SystemOperator': {
                    'Name': "",
                    'User_id': "",
                    'client_secret': "",
                    'Login': "",
                    'Password': "",
                },
            }
        },

        'TestNpg': {
            'Name': 'TestNpg',
            'main_page': 'https://web-npg.gandiva.ru/',
            'Internal_Link': 'http://agat-test-tssm:8083/',
            'API': {
                'Token_url': "",
                'Client_id': '',
                'Client_secret': '',
                'Internal_Link': 'http://agat-test-tssm:89/',
                'External_Link': 'https://api-npg.gandiva.ru/',
                'AUTH_URL': 'https://api-npg.gandiva.ru/Token',
                'CERT_FILE': '',
                'client_id': '',
                'realm_name': '',
            },
            'SQL_SERVER': {
                'TypeSQL': '',
                'SERVER': '',
                'PORT': 2424,
                'DATABASE': 'gandiva_test',
                'login': '',
                'password': '',
                'DRIVER': '',
            },
            'USERS': {
                'SystemOperator': {
                    'Name': "",
                    'User_id': "",
                    'client_secret': "",
                    'Login': "test1",
                    'ApiLogin': "agat\\test1",
                    'Password': "Q258999m",
                },
            }
        },

        'test_compose': {
            'Name': 'test_compose',
            'main_page': 'https://test-compose.gandiva.ru/',
            'Internal_Link': 'https://test-compose.gandiva.ru/',
            'API': {
                'Token_url': "",
                'Client_id': '',
                'Client_secret': '',
                'Internal_Link': 'https://api-test-compose.gandiva.ru/',
                'External_Link': 'https://api-test-compose.gandiva.ru/',
                'AUTH_URL': 'https://api-test-compose.gandiva.ru/Token',
                'CERT_FILE': '',
                'client_id': '',
                'realm_name': '',
            },
            'SQL_SERVER': {
                'TypeSQL': '',
                'SERVER': '',
                'PORT': 2424,
                'DATABASE': '',
                'login': '',
                'password': '',
                'DRIVER': '',
            },
            'USERS': {
                'SystemOperator': {
                    'Name': "",
                    'User_id': "",
                    'client_secret': "",
                    'Login': "test1",
                    'ApiLogin': "agat\\test1",
                    'Password': "Q258999m",
                },
            }
        },

    }

    mobile_stand = {
        'appium_server': 'http://127.0.0.1:4723/wd/hub',
        'Android_emulator_Nexus5': {
            'platformName': "Android",
            'platformVersion': "11",
            'deviceName': 'Nexus5',
            # 'app': "D:\TestGandiva2\TestGandiva\Data\Gandiva II03_08_20 debg.apk",
            'appPackage': "com.proton.gandiva2.test",
            'appActivity': "com.proton.gandiva2.ui.base.activity.SplashActivity",
        }
    }
