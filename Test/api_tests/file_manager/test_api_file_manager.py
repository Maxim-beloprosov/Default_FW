import os
import allure
import pytest

from Test.api_tests.api_base import ApiBase


@allure.feature('Api - FileManager')
@allure.story('Файловый менеджер')
class TestApiFileManager(ApiBase):

    test_data = [
        'TestApiFile.avif',
        'TestApiFile.bmp',
        'TestApiFile.dds',
        'TestApiFile.gif',
        'TestApiFile.png',
        'TestApiFile.tga',
        'TestApiFile.tiff',
        'TestApiFile.webp',
        'TestApiFile.docx',
        'TestApiFile.pptx',
        'TestApiFile.rar',
        'TestApiFile.xlsx',
        'TestApiFile.xml',
        'TestApiFile.pdf',
        'TestApiFile.sql',
        'TestApiFile.mp3',
        'TestApiFile.mp4',
        'TestApiFile.zip',
        'TestApiFile.jpg',
        'TestApiFile.txt',
        'TestApiFile.css'
    ]

    @allure.title('Загрузка файлов разных расширений')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    @pytest.mark.parametrize("format_file", test_data)
    def test_api_upload_file_different_extension(self, format_file):

        # Создание пути до файла
        file_path = os.path.join(self.APP.api_file_manager_files.get_project_root(), 'data', 'files_for_test', format_file)

        # Загрузка файла на сервер
        uploaded_file = self.APP.api_file_manager_files.post_upload_files_to_server(file_path)

        assert 'status' not in uploaded_file

    @allure.title('Переименование файлов')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_rename_files(self):

        # Получение списка файлов с сервера
        files_list = self.APP.api_actions_in_file_manager_files_list.get_file_list({'search': 'NewFileName'})['filesMetadata']

        # Удаление файлов с названием NewFileName
        for items in files_list:
            self.APP.api_file_manager_files.delete_file_from_server_by_id(items['id'])

        # Загрузка файлов
        for items in self.test_data:

            # Создание пути до файла
            file_path = os.path.join(self.APP.api_file_manager_files.get_project_root(), 'data', 'files_for_test', items)

            # Загрузка файла на сервер
            uploaded_file = self.APP.api_file_manager_files.post_upload_files_to_server(file_path)

        # Получение списка файлов с названием Test
        files_list = self.APP.api_actions_in_file_manager_files_list.get_file_list({'search': 'TestApiFile'})['filesMetadata']

        # Переменная для проверки, что все файлы успешно переименновались
        OK = None

        # Новое название файлов
        new_file_name = 'NewFileName'

        # Переименовываем файлы
        for items in files_list:
            renamed_file = self.APP.api_file_manager_files.put_update_file_name_on_server_by_id(items['id'], {'fileName': new_file_name})
            OK = True if renamed_file.status_code == 200 else False
            if not OK:
                break

        # Получение списка файлов с сервера
        files_list2 = self.APP.api_actions_in_file_manager_files_list.get_file_list({'search': 'NewFileName'})['filesMetadata']

        assert len(files_list) == len(files_list2)
        assert OK
        for items in files_list2:
            assert items['name'] == new_file_name

    @allure.title('Удаление файлов')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_delete_files(self):

        # Загрузка файлов на сервер
        for items in self.test_data:

            # Создание пути до файла
            file_path = os.path.join(self.APP.api_file_manager_files.get_project_root(), 'data', 'files_for_test', items)

            # Загрузка файла на сервер
            uploaded_file = self.APP.api_file_manager_files.post_upload_files_to_server(file_path)

        # Получение списка файлов с сервера
        files_list = self.APP.api_actions_in_file_manager_files_list.get_file_list({'search': 'TestApiFile'})['filesMetadata']

        # Удаление файлов с названием Test
        for items in files_list:
            deleted_file = self.APP.api_file_manager_files.delete_file_from_server_by_id(items['id'])
            assert deleted_file.status_code == 200

    @allure.title('Получение информации по несуществующему файлу')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_get_info_about_not_exist_file(self):

        # Получение информации по несуществующему файлу
        file_info = self.APP.api_file_manager_files.get_info_about_file_by_id(123)

        assert file_info['status'] == 404

    @allure.title('Получение несуществующего файла')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_get_info_about_not_exist_file(self):

        # Получение несуществующего файла
        get_file = self.APP.api_file_manager_files.get_file_from_server_by_id(123)

        assert get_file['status'] == 404

    @allure.title('Удаление несуществующего файла с сервера')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    def test_api_delete_not_exist_file(self):

        # Удаление несуществующего файла
        delete_file = self.APP.api_file_manager_files.delete_file_from_server_by_id(123)

        assert delete_file['status'] == 404

    params = [
        '',
        'Равным образом консультация с широким активом требуют определения и уточнения модели развития. Повседневная практика показывает, что укрепление и развитие структуры обеспечивает широкому кругу (специалистов) участие в формировании дальнейших направлений развития. Повседневная практика показывает, что укрепление и развитие структуры обеспечивает широкому кругу (специалистов) участие в формировании дальнейших направлений развития. Значимость этих проблем настолько очевидна, что консультация с широким активом.г',
        False
    ]

    @allure.title('Обновление имени файла на сервере')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ApiTest
    @pytest.mark.parametrize('text_length', params)
    def test_api_update_file_name_on_server(self, text_length):

        # Создание пути до файла
        file_path = os.path.join(self.APP.api_file_manager_files.get_project_root(), 'data', 'files_for_test', 'TestApiFile.txt')

        # Загрузка файла на сервер
        uploaded_file = self.APP.api_file_manager_files.post_upload_files_to_server(file_path)

        # Переименование файла с названием в 0 символов
        rename_file = self.APP.api_file_manager_files.put_update_file_name_on_server_by_id(uploaded_file['id'], text_length)

        assert rename_file['status'] == 400




