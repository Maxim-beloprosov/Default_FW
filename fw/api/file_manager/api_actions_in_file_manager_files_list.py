import allure

from fw.api.file_manager.api_file_manager_files_list import ApiFileManagerFilesList

class ActionsFileManagerFilesList(ApiFileManagerFilesList):

    @allure.title('Получение списка файлов по заданному фильтру')
    def get_file_list(self, filter_params={}):

        # Формируем тело запроса
        file_search = {}

        # ----- skip -----
        if 'skip' in filter_params:
            file_search['skip'] = filter_params['skip']
        else:
            file_search['skip'] = 0

        # ----- take -----
        if 'take' in filter_params:
            file_search['take'] = filter_params['take']
        else:
            file_search['take'] = 100

        # ----- fileCategories -----
        if 'fileCategories' in filter_params:
            file_search['fileCategories'] = filter_params['fileCategories']

        # ---- search -----
        if 'search' in filter_params:
            file_search['search'] = filter_params['search']

        # ----- createdDateFrom -----
        if 'createdDateFrom' in filter_params:
            file_search['createdDateFrom'] = filter_params['createdDateFrom']

        # ----- createdDateTo -----
        if 'createdDateTo' in filter_params:
            file_search['createdDateTo'] = filter_params['createdDateTo']

        # ----- sortProperties -----
        if 'sortProperties' in filter_params:
            file_search['sortProperties'] = filter_params['sortProperties']

        # Ищем нужные файлы
        files_list = self.post_files_list_filter(file_search)

        return files_list