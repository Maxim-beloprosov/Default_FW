import pytest

from Test.test_base import TestBase
import json


class TestServiceImport(TestBase):
    def setup_class(self):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def teardown_class(self):
        pass

    services = {}

    def import_service(self):
        """
        Скрипт импорта Услуг
        для использования требуется
        1) Выгрузить из G1 отчет "ОТЧЁТ ПО НОМЕНКЛАТУРЕ" => "НОРМАТИВЫ"
        2) в отчете заменить символ ";" на новый разделитель (например "$")
            2.1) разделитель второго уровня указываем в переменную separator_lvl_2
        3) сохраняем файл в формате CSV (где разделителем является ;)
            3.1)  разделитель первого уровня указываем в переменную separator_lvl_1
        4) В CSV файле производим замену '  ' на ' ' (удаление двойных пробелов)
        5) В CSV файле каждую строку оборачиваем одинарными кавычками, добавляем запятую в конец каждой строки (легко делается через макросы в Notepad++)
        6) то, что получилось закидываем в переменную 'services'

        ОГРАНИЧЕНИЯ
        1) пользователи в созданные ГО НЕ добавляются
        2) "isBossApprove" "isBossObserver" не добавляется, все проставляется хардкодное значение False
        3) "approveUsers" "observerUsers" хардкодное значение []
        4) обрабатываются услуги, в которых нет Эскалации (для услуг с эскалацией поведение не известно)
        5) Добавление доп. полей работает только для типа строка.
        :return:
        """
        separator_lvl_1 = ';'
        separator_lvl_2 = '$ '
        for index in range(0, len(self.services)):

            # Строку из CSV файла делим по символу ;
            service = self.services[index].split(separator_lvl_1)

            # Ищем/создаём каталог услуг
            catalog_lvl_0 = self.catalogs_filter(service[1], create_if_not_found=True)
            catalog_lvl_1 = self.catalogs_filter(service[2], parentId=catalog_lvl_0, create_if_not_found=True)
            catalog_lvl_2 = self.catalogs_filter(service[3], parentId=catalog_lvl_1, create_if_not_found=True)

            if (catalog_lvl_0 is None) or (catalog_lvl_1 is None) or (catalog_lvl_2 is None):
                print('Ошибка поиска/создания каталога услуг, выполнение прервано!"')
                break

            body = {
                "name": service[4],
                "parentId": catalog_lvl_2,
                "typeType": "Normal",
                "isBossApprove": False,
                "isBossObserver": False,
                "workScheduleOverridden": False,
                "approveTimeNormative": int(service[7]),
                "approveTimeHard": 30,
                "initiatorTimeNormative": int(service[8]),
                "initiatorTimeNotify": int(service[9]),
                "initiatorTimeWait": int(service[10]),
                "approveUsers": [],
                "observerUsers": [],
                "serviceResponsibilityGroups": [
                    {
                        "responsibilityGroupId": self.get_responsibility_group_id(int(service[13]), create_if_not_found=False),
                        "timeNormative": int(service[6]),
                        "timeHard": int(service[5]),
                        "orderNumber": 0
                    }
                ],
                "isActive": True,
                "initiatorAccessType": "All",
            }
            response = self.APP.api_gandiva_services.post_gandiva_services(body)
            # Если что то пойдет не так, будут ответы от сервера.
            print(response)
            assert 'errors' not in response

            id_service = response['catalogId']
            service_template = []

            if service[28] != '':

                st_name = service[27].split(separator_lvl_2)
                st_enabled = service[28].split(separator_lvl_2)
                st_obligatory = service[29].split(separator_lvl_2)
                st_type = service[30].split(separator_lvl_2)
                st_obligatory_init_cont = service[31].split(separator_lvl_2)

                for index_st in range(0, len(st_name)):
                    if (st_enabled[index_st] == 'Да') and (st_type[index_st] == '-1'):
                        field = {
                            "name": st_name[index_st],
                            "data": {
                                "type": "Text",
                                "value": ""
                            },
                            "permissions": [
                                {
                                    "roleType": "Initiator",
                                    "ruleType": "View",
                                    "permission": True
                                }, {
                                    "roleType": "Approver",
                                    "ruleType": "View",
                                    "permission": True
                                }, {
                                    "roleType": "Contractor",
                                    "ruleType": "View",
                                    "permission": True
                                }, {
                                    "roleType": "Observer",
                                    "ruleType": "View",
                                    "permission": True
                                }, {
                                    "roleType": "Initiator",
                                    "ruleType": "EditValueOnly",
                                    "permission": True
                                }, {
                                    "roleType": "Approver",
                                    "ruleType": "EditValueOnly",
                                    "permission": True
                                }, {
                                    "roleType": "Contractor",
                                    "ruleType": "EditValueOnly",
                                    "permission": True
                                }, {
                                    "roleType": "Observer",
                                    "ruleType": "EditValueOnly",
                                    "permission": True
                                }, {
                                    "roleType": "Initiator",
                                    "ruleType": "Edit",
                                    "permission": True
                                }, {
                                    "roleType": "Approver",
                                    "ruleType": "Edit",
                                    "permission": True
                                }, {
                                    "roleType": "Contractor",
                                    "ruleType": "Edit",
                                    "permission": True
                                }, {
                                    "roleType": "Observer",
                                    "ruleType": "Edit",
                                    "permission": True
                                },
                            ],
                            "orderPath": f"{index_st}"
                        }
                        if st_obligatory[index_st] == 'Да':
                            if st_obligatory_init_cont[index_st] == '2':
                                field["permissions"].append(
                                    {
                                        "roleType": "Initiator",
                                        "ruleType": "Obligatory",
                                        "permission": True
                                    }
                                )
                            else:
                                field["permissions"].append(
                                    {
                                        "roleType": "Contractor",
                                        "ruleType": "Obligatory",
                                        "permission": True
                                    }
                                )

                        service_template.append(field)

                response = self.APP.api_gandiva_service_template.put_gandiva_service_template_id(id_service, service_template)
                print('service_template = ', response)

    def catalogs_filter(self, name, parentId=None, create_if_not_found=False):
        body = {
            "skip": 0,
            "take": 1000,
            "filter": {
                "type": "Catalog"
            },
            "parentId": parentId,
        }
        catalogs_list = self.APP.api_service_catalogs.post_service_catalogs_filter_parent_tree_list(body)['items']
        flag = False

        # Ищем по названию нужный каталог
        for catalog in catalogs_list:
            if name == catalog['name']:
                return catalog['id']

        # если НЕ нашли И create_if_not_found=True => создаём не найденный каталог
        if create_if_not_found:
            if flag is False:
                body = {
                    "parentId": parentId,
                    "name": name,
                }
                return self.APP.api_service_catalogs.post_service_catalogs(body)['id']

    def get_responsibility_group_id(self, name, parentId=None, create_if_not_found=False):
        body = {
            "search": name,
            "skip": 0,
            "take": 1000,
        }
        groups_list = self.APP.api_responsibility_groups.post_responsibility_groups_filter()

        flag = False

        # Ищем по названию нужный каталог
        for group in groups_list:
            if name == group['name']:
                if parentId is None:
                    return group['id']
                else:
                    # Проверяем есть ли поле parentId
                    if "parentId" in group:
                        if group["parentId"] == parentId:
                            return group['id']

        # если НЕ нашли И create_if_not_found=True => создаём
        if create_if_not_found:
            if flag is False:
                body = {
                    "parentId": parentId,
                    "name": name,
                    # "dispatcherUserId": "",
                    "isActive": True,
                }
                return self.APP.api_responsibility_groups.post_responsibility_groups(body)['id']

