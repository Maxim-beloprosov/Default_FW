import os
import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - FileManager')
@allure.story('Файловый менеджер. Фильтрация')
class TestApiFileManagerFilter(ApiBase):

    @allure.title('Фильтрация по "Изображения"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_filter_by_images(self):

        # Создание пути до файла
        file_path = os.path.join(self.APP.api_file_manager_files.get_project_root(), 'data', 'files_for_test', 'TestApiFile.png')

        # Загрузка файла на сервер
        uploaded_file = self.APP.api_file_manager_files.post_upload_files_to_server(file_path)

        # Фильтрация файлов по категории "Изображения"
        filtered_files = self.APP.api_actions_in_file_manager_files_list.get_file_list({"fileCategories": ["Images"]})['filesMetadata']

        # Получение списка известных расширений файлов
        files_extensions = self.APP.api_actions_in_file_manager_files_extensions.get_all_extensions_files()

        # Получение списка допустимых базовых типов файлов
        files_mime_types = self.APP.api_actions_in_file_manager_files_extensions.get_all_base_type_files()

        for items in filtered_files:
            assert items['category'] == 'Images'
            assert items['contentType'].split('/')[1] in files_extensions or \
                   items['contentType'] in files_mime_types

    @allure.title('Фильтрация по "Видеозаписи"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_filter_by_videos(self):

        # Создание пути до файла
        file_path = os.path.join(self.APP.api_file_manager_files.get_project_root(), 'data', 'files_for_test', 'TestApiFile.mp4')

        # Загрузка файла на сервер
        uploaded_file = self.APP.api_file_manager_files.post_upload_files_to_server(file_path)

        # Фильтрация файлов по категории "Видеозаписи"
        filtered_files = self.APP.api_actions_in_file_manager_files_list.get_file_list({"fileCategories": ["Videos"]})['filesMetadata']

        # Получение списка известных расширений файлов
        files_extensions = self.APP.api_actions_in_file_manager_files_extensions.get_all_extensions_files()

        # Получение списка допустимых базовых типов файлов
        files_mime_types = self.APP.api_actions_in_file_manager_files_extensions.get_all_base_type_files()

        for items in filtered_files:
            assert items['category'] == 'Videos'
            assert items['contentType'].split('/')[1] in files_extensions or \
                   items['contentType'] in files_mime_types

    @allure.title('Фильтрация по "Аудиозаписи"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_filter_by_audios(self):

        # Создание пути до файла
        file_path = os.path.join(self.APP.api_file_manager_files.get_project_root(), 'data', 'files_for_test', 'TestApiFile.mp3')

        # Загрузка файла на сервер
        uploaded_file = self.APP.api_file_manager_files.post_upload_files_to_server(file_path)

        # Фильтрация файлов по категории "Аудиозаписи"
        filtered_files = self.APP.api_actions_in_file_manager_files_list.get_file_list({"fileCategories": ["Audios"]})['filesMetadata']

        # Получение списка известных расширений файлов
        files_extensions = self.APP.api_actions_in_file_manager_files_extensions.get_all_extensions_files()

        # Получение списка допустимых базовых типов файлов
        files_mime_types = self.APP.api_actions_in_file_manager_files_extensions.get_all_base_type_files()

        for items in filtered_files:
            assert items['category'] == 'Audios'
            assert items['contentType'].split('/')[1] in files_extensions or \
                   items['contentType'] in files_mime_types

    @allure.title('Фильтрация по "Документы"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_filter_by_documents(self):

        # Создание пути до файла
        file_path = os.path.join(self.APP.api_file_manager_files.get_project_root(), 'data', 'files_for_test', 'TestApiFile.xlsx')

        # Загрузка файла на сервер
        uploaded_file = self.APP.api_file_manager_files.post_upload_files_to_server(file_path)

        # Фильтрация файлов по категории "Документы"
        filtered_files = self.APP.api_actions_in_file_manager_files_list.get_file_list({"fileCategories": ["Documents"]})['filesMetadata']

        # Получение списка известных расширений файлов
        files_extensions = self.APP.api_actions_in_file_manager_files_extensions.get_all_extensions_files()

        # Получение списка допустимых базовых типов файлов
        files_mime_types = self.APP.api_actions_in_file_manager_files_extensions.get_all_base_type_files()

        for items in filtered_files:
            assert items['category'] == 'Documents'
            assert items['contentType'].split('/')[1] in files_extensions or \
                   items['contentType'] in files_mime_types

    @allure.title('Фильтрация по "Прочее"')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_filter_by_undefinded(self):

        # Создание пути до файла
        file_path = os.path.join(self.APP.api_file_manager_files.get_project_root(), 'data', 'files_for_test', 'TestApiFile.tga')

        # Загрузка файла на сервер
        uploaded_file = self.APP.api_file_manager_files.post_upload_files_to_server(file_path)

        # Фильтрация файлов по категории "Прочее"
        filtered_files = self.APP.api_actions_in_file_manager_files_list.get_file_list({"fileCategories": ["Undefinded"]})['filesMetadata']

        # Получение списка известных расширений файлов
        files_extensions = self.APP.api_actions_in_file_manager_files_extensions.get_all_extensions_files()

        # Получение списка допустимых базовых типов файлов
        files_mime_types = self.APP.api_actions_in_file_manager_files_extensions.get_all_base_type_files_without_undefinded()

        for items in filtered_files:
            assert items['category'] == 'Undefinded'
            assert items['contentType'].split('/')[1] not in files_extensions or \
                items['contentType'] not in files_mime_types

    @allure.title('Фильтрация по неизвестной категории')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_filter_by_not_exist_categories(self):

        # Фильтрация файлов по категории "Potato"
        filtered_files = self.APP.api_actions_in_file_manager_files_list.get_file_list({"fileCategories": ["Potato"]})

        assert filtered_files['status'] == 400

    params = [
        'Potato',
        "-2020-09-12T07:39:08.248Z",
        "-2020-09-12 07:39:08.248",
        "~2020-09-12T07:39:08.248Z",
        "~2020-09-12 07:39:08.248"
    ]

    @allure.title('Фильтрация по некорректной дате создания(createdDateFrom)')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('param', params)
    def test_api_filter_by_not_correct_created_date_from(self, param):

        # Фильтрация файлов по категории "Potato"
        filtered_files = self.APP.api_actions_in_file_manager_files_list.get_file_list({"createdDateFrom": param})

        assert filtered_files['status'] == 400

    @allure.title('Фильтрация по некорректной дате создания(createdDateTo)')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('param', params)
    def test_api_filter_by_not_correct_created_date_to(self, param):

        # Фильтрация файлов по категории "Potato"
        filtered_files = self.APP.api_actions_in_file_manager_files_list.get_file_list({"createdDateTo": param})

        assert filtered_files['status'] == 400

    params = [
        -1,
        0,
        2147483647,
        2147483648
    ]

    @allure.title('Фильтрация с разным параметром skip')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('skip_length', params)
    def test_api_filter_by_different_param_on_skip(self, skip_length):

        # Фильтрация файлов по категории "Potato"
        filtered_files = self.APP.api_actions_in_file_manager_files_list.get_file_list({'skip': skip_length})

        if skip_length <= -1 or skip_length >= 2147483648:
            assert filtered_files['status'] == 400
        else:
            assert 'status' not in filtered_files

    params = [
        0,
        1,
        1000,
        1001
    ]

    @allure.title('Фильтрация с разным параметром take')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('take_length', params)
    def test_api_filter_by_different_param_on_take(self, take_length):

        # Фильтрация файлов по категории "Potato"
        filtered_files = self.APP.api_actions_in_file_manager_files_list.get_file_list({'take': take_length})

        if take_length <= 0 or take_length >= 1001:
            assert filtered_files['status'] == 400
        else:
            assert 'status' not in filtered_files

    @allure.title('Фильтрация с сортировкой по неизвестному параметру')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_filter_by_not_exist_sort_propeties(self):

        # Фильтрация файлов по категории "Potato"
        filtered_files = self.APP.api_actions_in_file_manager_files_list.get_file_list({
            "sortProperties": [
                {
                    "name": "Potato",
                }
            ]
        })

        assert filtered_files['status'] == 400

    @allure.title('Фильтрация без авторизации')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_filter_without_authorize_in_system(self):

        # Деавторизируемся
        self.APP.settings.Authorization = False

        # Фильтрация файлов
        filtered_files = self.APP.api_actions_in_file_manager_files_list.get_file_list({'take': 100})

        assert filtered_files.status_code == 401



