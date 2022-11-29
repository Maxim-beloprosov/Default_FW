import allure

from fw.api.knowledge_base.api_knowledge_base import ApiKnowledgeBase
from fw.api.knowledge_base.api_access import ApiAccess


class ActionsInArticles(ApiKnowledgeBase, ApiAccess):

    @allure.title('Создать статью')
    def create_article(self, article_mass={}):

        json_article = {}

        # -------title---------------------
        if 'title' in article_mass:
            json_article['title'] = article_mass['title']
        else:
            json_article['title'] = 'AutomationApiTestArticle ' + self.manager.time.get_date_time_Y_m_d_H_M_S()

        # -------bodyContent--------------------
        if 'bodyContent' in article_mass:
            json_article['bodyContent'] = []
            for content in article_mass["bodyContent"]:
                if isinstance(content, str):
                    json_article["bodyContent"].append({
                            "type": "Text",
                            "text": content
                        }
                    )
                else:
                    if content["type"] == 'Text':
                        json_article["bodyContent"].append({
                                "type": 'Text',
                                "text": content["text"]
                            }
                        )
                    elif content["type"] == 'Attachment':
                        json_article["bodyContent"].append(content)
                    elif content["type"] == 'Mention':
                        mention_json = {"type": 'Mention'}
                        if 'addresseeType' in content:
                            mention_json["addresseeType"] = content["addresseeType"]
                        if 'userId' in content:
                            mention_json["userId"] = content["userId"]
                        if 'email' in content:
                            mention_json["email"] = content["email"]
                        json_article["bodyContent"].append(mention_json)
                    elif content["type"] == 'Hashtag':
                        json_article["bodyContent"].append({
                                "type": 'Hashtag',
                                "hashtag": content["hashtag"],
                            }
                        )
                    elif content["type"] == 'Rating':
                        json_article["bodyContent"].append({
                                "type": 'Rating',
                                "rating": content["rating"],
                            }
                        )
        else:
            json_article["bodyContent"] = [
                    {
                        "type": "Text",
                        "text": "AutomationApiTestDescription " + self.manager.time.get_date_time_Y_m_d_H_M_S()
                    },
                ]

        # -------parentId--------------------
        if 'parentId' in article_mass:
            json_article['parentId'] = article_mass['parentId']
        else:
            if self.manager.settings.branch == 'feature_development':
                json_article['parentId'] = self.manager.group_data.parent_id_articles['feature_development']
            elif self.manager.settings.branch == 'Testing':
                json_article['parentId'] = self.manager.group_data.parent_id_articles['Testing']

        # -------orderNumber--------------------
        if 'orderNumber' in article_mass:
            json_article['orderNumber'] = article_mass['orderNumber']

        # -------recommendationPages--------------------
        if 'recommendationPages' in article_mass:
            json_article['recommendationPages'] = article_mass['recommendationPages']

        # -------roleReaders-------
        if 'roleReaders' in article_mass:
            json_article['roleReaders'] = article_mass['roleReaders']
        else:
            json_article['roleReaders'] = {"accessType": "OnlySelf"}

        # -------roleEditors--------------------
        if 'roleEditors' in article_mass:
            json_article['roleEditors'] = article_mass['roleEditors']
        else:
            json_article['roleEditors'] = {"accessType": "OnlySelf"}

        article = self.post_create_article(json_article)

        return article

    @allure.title('Обновление статьи')
    def update_article(self, article_id, article_mass={}):

        json_article = {}

        # -------pageId--------------------
        if 'pageId' in article_mass:
            json_article['pageId'] = article_id

        # -------title---------------------
        if 'title' in article_mass:
            json_article['title'] = article_mass['title']

        # -------bodyContent--------------------
        if 'bodyContent' in article_mass:
            json_article['bodyContent'] = []
            for content in article_mass["bodyContent"]:
                if isinstance(content, str):
                    json_article["bodyContent"].append({
                            "type": "Text",
                            "text": content
                        }
                    )
                else:
                    if content["type"] == 'Text':
                        json_article["bodyContent"].append({
                                "type": 'Text',
                                "text": content["text"]
                            }
                        )
                    elif content["type"] == 'Attachment':
                        json_article["bodyContent"].append(content)
                    elif content["type"] == 'Mention':
                        mention_json = {"type": 'Mention'}
                        if 'addresseeType' in content:
                            mention_json["addresseeType"] = content["addresseeType"]
                        if 'userId' in content:
                            mention_json["userId"] = content["userId"]
                        if 'email' in content:
                            mention_json["email"] = content["email"]
                        json_article["bodyContent"].append(mention_json)
                    elif content["type"] == 'Hashtag':
                        json_article["bodyContent"].append({
                                "type": 'Hashtag',
                                "hashtag": content["hashtag"],
                            }
                        )
                    elif content["type"] == 'Rating':
                        json_article["bodyContent"].append({
                                "type": 'Rating',
                                "rating": content["rating"],
                            }
                        )

        # -------- recommendationPages ----------
        if 'recommendationPages' in article_mass:
            json_article['recommendationPages'] = article_mass['recommendationPages']

        update_article = self.put_update_article_by_id(article_id, json_article)

        return update_article

    @allure.title('Сменить расположение статьи')
    def change_location_in_article(self, article_id, new_parent_id):

        # Подготовка тела для смены расположения статьи
        change_location_body = {
            "parentId": new_parent_id,
        }

        # Смена расположения
        changed_location = self.post_move_article(article_id, change_location_body)

        return changed_location

    @allure.title('Удалить статью')
    def delete_article(self, article_id, actionType='OnlyCurrent'):

        # Подготовка тела для удаления статьи
        delete_article_body = {
            "action": "Delete",
            "actionType": actionType
        }

        # Удаление статьи
        delete_location = self.post_delete_or_restore_article(article_id, delete_article_body)

        return delete_location

    @allure.title('Восстановить статью')
    def restore_article(self, article_id, actionType='OnlyCurrent'):

        # Подготовка тела для восстановления статьи
        restore_article_body = {
            "action": "Restore",
            "actionType": actionType
        }

        # Восстановление статьи
        restore_location = self.post_delete_or_restore_article(article_id, restore_article_body)

        return restore_location

    @allure.title('Обновление прав доступа к статье')
    def update_access_rights_in_article(self, article_id, article_mass={}):

        json_article = {}

        # ------ roleType -------
        json_article['roleType'] = article_mass['roleType']

        # ------ isInherited --------
        if 'isInherited' in article_mass:
            json_article['isInherited'] = article_mass['isInherited']

        # ------- members ---------
        if 'members' in article_mass:
            json_article['members'] = article_mass['members']

        # ------- accessType ------
        json_article['accessType'] = article_mass['accessType']

        update_access_right = self.put_update_access_rights_to_article(article_id, json_article)

        return update_access_right

    @allure.title('Список пользователей в роли в статье(Выбранные)')
    def list_users_in_role_in_article(self, article_id, roleType, accessType, amount_users):

        # Подготовка тела для фильтрации пользователей в статье в роли..
        filter_users = {
            'pageId': article_id,
            'roleType': roleType,
            'accessType': accessType,
            "filterSelectionStatus": 'Selected',
            'take': amount_users
        }

        # Фильтрация пользователей/групп в статье
        list = self.put_search_sort_filter_clients_for_access_rights_to_article(filter_users)

        # Вывод списка пользователей/групп на роли...
        users_and_groups_id_list = []
        for items in list['items']:
            try:
                users_and_groups_id_list.append(items['userMember']['id'])
            except:
                users_and_groups_id_list.append(items['groupMember']['id'])

        return users_and_groups_id_list

    @allure.title('Сформировать json для изменения прав в статье')
    def get_json_for_editing_roles(self, id, access_type, member_type='User', role_type='Reader'):

        body = {
            'roleType': role_type,
            'members': [
                {
                    'id': id,
                    'memberType': member_type,
                }
            ],
            'accessType': access_type
        }
        return body

    @allure.title('Сформировать json для создания статьи с правами')
    def get_json_for_creating_article_with_roles(self, id, access_type, member_type='User', role_type='roleEditors'):

        body = {
            role_type: {
                'members': [
                    {
                        'id': id,
                        'memberType': member_type,
                    }
                ],
                'accessType': access_type
            }
        }

        return body

