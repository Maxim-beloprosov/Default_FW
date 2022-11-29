import allure

from fw.api.file_manager.api_file_manager_files_extensions import ApiFileManagerFilesExtensions

class ActionsFileManagerFilesExtensions(ApiFileManagerFilesExtensions):

    @allure.title('Получени списка всех известных расширений файлов')
    def get_all_extensions_files(self):

        json = self.get_list_known_file_extensions()
        files_name = []

        for items in json:
            files_name.append(items['name'])

        return files_name

    @allure.title('Получение списка допустимых базовых типов файлов')
    def get_all_base_type_files(self):

        json = self.post_get_list_allowed_base_file_types()
        files_name = []

        for items in json:
            files_name.append(items['name'])

        return files_name

    @allure.title('Получение списка допустимых базовых типов файлов (Нет категории Undefinded)')
    def get_all_base_type_files_without_undefinded(self):

        json = self.post_get_list_allowed_base_file_types()
        files_name = []

        for items in json:
            if items['categoty'] != 'Undefinded':
                files_name.append(items['name'])

        return files_name