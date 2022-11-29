import allure

from fw.api.service_catalog.service_catalogs import ServiceCatalogs


class ActionsInServiceCatalog(ServiceCatalogs):

    @allure.title('Создание услуги')
    def create_service(self, parent_responsibility_group_id, service_id, typeType="Normal", isActive=True):

        # Подготовка тела запроса
        service_body = {
            "name": "AutomationApiTestCreateService " + self.manager.time.get_date_time_Y_m_d_H_M_S(),
            "parentId": service_id,
            "typeType": typeType,
            "approveTimeNormative": 40,
            "approveTimeHard": 40,
            "initiatorTimeNormative": 40,
            "initiatorTimeNotify": 40,
            "initiatorTimeWait": 40,
            "serviceResponsibilityGroups": [
                {
                    "responsibilityGroupId": parent_responsibility_group_id,
                    "timeNormative": 40,
                    "timeHard": 40,
                }
            ],
            "isActive": isActive,
            "initiatorAccessType": "All",
        }

        # Ищем нужную услугу
        services = self.manager.api_gandiva_services.post_gandiva_services(service_body)

        return services

    @allure.title('Поиск услуги')
    def search_service(self, search, type='Service', result_view='List'):

        # Подготовка тела запроса
        service_search = {
            "search": search,
            "filter":
                {
                    "type": type,
                    "serviceTypes": ["Normal"]
                },
            "resultView": result_view

        }
        # Ищем нужную услугу
        services = self.post_gandiva_services_for_tickets_filter(service_search)

        return services

    @allure.title('Поиск каталогов услуг с учетом фильтра')
    def search_service_catalog_with_filter(self, search="Automation service catalogs", service_type="Catalog",
                                           isdeleted=False, isactive=True):
        # Подготовка тела запроса
        service_search = {
            "search": search,
            "skip": 0,
            "take": 1000,
            "filter": {
                "type": service_type
            },
            "isDeleted": isdeleted,
            "isActive": isactive,
        }
        # Ищем нужную услугу
        services = self.post_service_catalogs_filter_list(service_search)

        return services

    @allure.title('Поиск услуги с фильтром по ГО')
    def search_service_filter_rg(self, parent_responsibility_group_id, result_view='TreeList'):
        # Подготовка тела запроса
        service_search = {
            "skip": 0,
            "take": 1000,
            "resultView": result_view,
            "filter": {
                "responsibilityGroups": [
                    parent_responsibility_group_id
                ],
            }
        }
        # Ищем нужную услугу
        services = self.post_gandiva_services_for_tickets_filter(service_search)

        return services

    @allure.title('Выбор нужной услуги по дереву пути')
    def choose_service_with_treepathname(self, parent_service_search, treepathname='Отдел тестирования Гандивы\\'
                                                                                   'Automation service catalogs test'):
        service_id = ' '

        # Цикл выбора нужной услуги с фильтром по дереву пути
        for i in parent_service_search['items']:
            if i['treePathName'] == treepathname:
                service_id = i['id']
                break

        return service_id

    @allure.title('Проверка наличия услуги в ГО')
    def check_service(self, parent_responsibility_group_id, service_create):

        # Ставим флаг
        check = False

        # Ищем данную услугу
        search = self.search_service_filter_rg(
            parent_responsibility_group_id)

        # Цикл проверки наличия искомой услуги в ГО
        for service in search['items']:
            if service_create['name'] in service['name']:
                check = True
                break

        return check

