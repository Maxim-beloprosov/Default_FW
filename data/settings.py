class Settings:

    python = 'python'
    path_to_project = ''
    time_element_Wait = 30

    branch = 'feature_development'
    # branch = 'test_compose'
    # branch = 'Testing'
    # branch = 'Staging'

    mobile_branch = 'pixel_5'

    # API
    Authorization = True
    content_type = True
    use_internal_link_in_api = False

    # WEB
    selenium_server = 'http://127.0.0.1:4444/wd/hub'
    Browser = {
        'Name': 'chrome',
        'headless': False,
        'Remote': False
    }

    GLOBAL = {
        'feature_development': {
            'Name': 'development',
            'main_page': 'https://feature-development.gandiva.ru/',
            'Internal_Link': 'https://feature-development.gandiva.ru/',
            'API': {
                'Token_url': "",
                'Client_id': '',
                'Client_secret': '',
                'Internal_Link': '',
                'External_Link': 'https://api-feature-development.gandiva.ru',
                'AUTH_URL': 'https://auth-feature-development.gandiva.ru/connect/token',
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
                    'User_id': "10c37c2c-b0e9-11ec-90da-ae981e1e0fca",
                    'client_secret': "bNxKnPEZTpnnSom9nhYuBMdmyOboBGPNKOM/tMCaTQYWgDgVU1ueJDGpVcDrb9Ak",
                    'Login': "",
                    'Password': "",
                    },
            }
        },

        'Testing': {
            'Name': 'Test',
            'main_page': 'https://feature-testing1.gandiva.ru/',
            'Internal_Link': 'https://feature-testing1.gandiva.ru/',
            'API': {
                'Token_url': "",
                'Client_id': '',
                'Client_secret': '',
                'Internal_Link': '',
                'External_Link': 'https://api-feature-testing1.gandiva.ru',
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
                    'User_id': "aef26e5a-ecb5-11ec-b445-fe4aed3ff546",
                    'client_secret': "iuyo0EIT1OQvmgYzXBRCzg8DnE7VJBfRPHMXrz2ICss0jGy86tGuWA0+mI0Ylp9j",
                    'Login': "admin",
                    'Password': "admin",
                    },
            }
        },

        'Staging': {
            'Name': 'Staging',
            'main_page': 'https://feature-staging.gandiva.ru/',
            'Internal_Link': 'https://feature-staging.gandiva.ru/',
            'API': {
                'Token_url': "",
                'Client_id': '',
                'Client_secret': '',
                'Internal_Link': '',
                'External_Link': 'https://api-feature-staging.gandiva.ru',
                'AUTH_URL': 'https://auth-feature-staging.gandiva.ru/connect/token',
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
                    'User_id': "8facf0a6-476c-11ea-bf0a-1c6f6555ae82",
                    'client_secret': "lxTI4OeKbZZQwvYY8AVxLDU3igOcvh/F5jaJHUzI32nfzoubPo/9HqqAJ6ydTdSE",
                    'Login': "admin",
                    'Password': "admin",
                    },
            }
        },

        'test_compose': {
            'Name': 'development',
            'main_page': 'https://web-test-compose.gandiva.ru/',
            'Internal_Link': 'https://web-test-compose.gandiva.ru/',
            'API': {
                'Token_url': "",
                'Client_id': '',
                'Client_secret': '',
                'Internal_Link': '',
                'External_Link': 'https://api-test-compose.gandiva.ru',
                'AUTH_URL': 'https://auth-test-compose.gandiva.ru/connect/token',
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
                    'User_id': "8facf0a6-476c-11ea-bf0a-1c6f6555ae82",
                    'client_secret': "8OydZFzbPoPdo+1C2h+7MQb6+a0VUG6OoWbPejrO/67QOn1UGRdmDPujiZtOUJ6x",
                    'Login': "",
                    'Password': "",
                },
            }
        },

    }

    mobile_stand = {
        'appium_server': 'http://127.0.0.1:4723/',
        'pixel_5': {
            'platformName': "Android",
            'platformVersion': "33",
            'deviceName': 'pixel_5',
            # 'app': "E:\Selenium\Gandiva_2_25_08_22.apk",
            'appPackage': "com.proton.gandiva2.test",
            'appActivity': "com.proton.gandiva2.ui.base.activity.SplashActivity",
        }
    }

    log_lvl = {
        'API': {
            'request_type': True,
            'url': True,
            'headers': False,
            'body': True,
            'status_code': True,
            'response': True,
        }
    }
