class GroupData:

    response = None
    access_token = ''
    token_type = ''
    expires_in = ''
    refresh_token = ''
    status_code = ''
    id_uploaded_file = ''


    users = {
        'test_user01': {
            'user_id': "",
            'Login': "",
            'Password': "",
            'secret': "",
            'secretId': "",

            'Email': "",
            'EmailPas': "",
            'EmailExternalPas': "",

            'Name': "",
            'Surname': "",
            'MiddleName': "",
            'Status': "",
            'Manager': "",
            'ActualAddressId': "",
        }
    }

    secret_key = {
        "Testing": {
            "test_user01": {
                "user_id": "",
                "secret": ""
            }
        }
    }
