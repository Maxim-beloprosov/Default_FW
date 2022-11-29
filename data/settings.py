class Settings:

    python = 'python'
    path_to_project = ''
    time_element_Wait = 30

    branch = 'Testing'

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
        'Testing': {
            'Name': 'Test',
            'main_page': 'https://google.com/',
            'Internal_Link': 'https://google.com/',
            'API': {
                'Token_url': "",
                'Client_id': '',
                'Client_secret': '',
                'Internal_Link': '',
                'External_Link': '',
                'AUTH_URL': '',
                'CERT_FILE': '',
                'client_id': '',
                'realm_name': '',
            },
            'SQL_SERVER': {
                'TypeSQL': '',
                'SERVER': '',
                'PORT': '',
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
        }
    }

