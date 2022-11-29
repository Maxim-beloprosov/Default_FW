from selenium.webdriver.common.by import By
import allure
from fw.web.AnyPage import AnyPage


class Locator:
    access_view_button = (By.XPATH, '//div[@test_id="kb-dropdown-articleAccess-reader"]')
    access_edit_button = (By.XPATH, '//div[@test_id="kb-dropdown-articleAccess-editor"]')
    add_permissions_button = (By.XPATH, '(//button[@test_id="button-execute"])[1]')
    all_articles_button = (By.XPATH, '//nav[@data-manual="kb_goto_tabs"]/a[@data-manual="kb_goto_article"]')
    all_but_add_permission_button = (By.XPATH, '(//button[@test_id="button-execute"])[1]')
    all_but_permissions_window_search = (By.XPATH, '(//input[@test_id="custom-input"])[1]')
    article_search = (By.XPATH, '//div[@data-manual="kb_tree_search"]//input[@class="search"]')
    article_search_input_trash = (By.XPATH, '//div[@class = "sideblock knowledgebase__block"]//input')
    button_create_article = (By.XPATH, '//button[@test_id="kb-button-create"]')
    change_edit_permissions_all_users = (By.XPATH, '//div[@test_id="kb-dropdown-articleAccess-editor-All"]')
    change_edit_permissions_all_but = (By.XPATH, '//div[@test_id = "kb-dropdown-articleAccess-editor-NotAny"]')
    change_edit_permissions_someone = (By.XPATH, '//div[@test_id="kb-dropdown-articleAccess-editor-Some"]')
    change_view_permissions_someone = (By.XPATH, '(//div[@class="rightside"]//div[@class="contextmenu__elem"])[2]')
    change_view_permissions = (By.XPATH, '(//div[@class="rightside"]//div[@class="contextmenu__elem"])[1]')
    check_active_all_users_permission = (By.XPATH, '//div[@test_id="kb-dropdown-articleAccess-reader"]//div[@test_id="kb-dropdown-articleAccess-reader-all" '
                                                   'and @class="action-submenu__item action-submenu__item_active"]')
    check_active_edit_all_users_permission = (By.XPATH, '//div[@test_id="kb-dropdown-articleAccess-editor-All" and '
                                                        '@class="action-submenu__item action-submenu__item_active"]')
    check_active_only_me_permission = (By.XPATH, '//div[@test_id="kb-dropdown-articleAccess-reader-justMe" and '
                                                 '@class="action-submenu__item action-submenu__item_active"]')
    check_active_edit_only_me_permission = (By.XPATH, '//div[@test_id="kb-dropdown-articleAccess-editor-justMe" and '
                                                      '@class="action-submenu__item action-submenu__item_active"]')
    cke_contents = (By.XPATH, '//div[@class="noarticle"]')
    delete_button = (By.XPATH, '(//div[@class="popup__buttons"]//button)[2]')
    delete_switch = (By.XPATH, '//div[@class="popup__deleteAll"]//div[@class="switch-wrapper switch-wrapper_bg"]')
    description_text = (By.XPATH, '//div[@class="cke-supreme__content"]')
    edit_button = (By.XPATH, '(//div[@class = "article__header"]//button)[1]')
    edit_permissions_all_but = (By.XPATH, '//div[@test_id = "kb-dropdown-articleAccess-editor-NotAny"]')
    edit_permissions_someone_button = (By.XPATH, '//div[@test_id = "kb-dropdown-articleAccess-editor-Some"]')
    edit_permissions_only_me = (By.XPATH, '//div[@test_id = "kb-dropdown-articleAccess-editor-justMe"]')
    edit_permissions_button = (By.XPATH, '//div[@class="access__edit"]')
    move_delete_button = (By.XPATH, '//div[@test_id="kb-dropdown-delete"]')
    name_text = (By.XPATH, '//div[@class="article__header"]//h2')
    repair_checkbox = (By.XPATH, '//label[@class="checkbox item__checkbox popup__checkbox"]')
    repair_button_in_repair_window = (By.XPATH, '(//div[@class="fixed-panel__content"]/button[@class="button   button_pink button_medium "])[2]')
    restore_button = (By.XPATH, '//div[@class = "article__controll"]/button')
    settings_button = (By.XPATH, '//div[@test_id = "ticket-setup"]//button')
    settings_button_wait = (By.XPATH, '//div[@test_id="ticket-setup"]')
    someone_permissions_window_search = (By.XPATH, '(//input[@test_id="custom-input"])[1]')
    switcher_view_permissions = (By.XPATH, '//div[@class="popup-groups-and-users__search-panel-left"]//label[@class="switch"]')
    tab_all_counts = (By.XPATH, '//a[@data-manual="kb_goto_article"]/div[@class = "nav__count"]')
    tabs_knowledge_base_nav = (By.XPATH, '//nav[@data-manual="kb_goto_tabs"]')
    trash_button = (By.XPATH, '//nav//a[@data-manual = "kb_goto_trash"]')
    trash_counts = (By.XPATH, '//a[@data-manual="kb_goto_trash"]/div[@class="nav__count"]')
    view_permissions_all_users = (By.XPATH, '//div[@test_id="kb-dropdown-articleAccess-reader-all"]')
    view_permissions_all_but = (By.XPATH, '//div[@test_id = "kb-dropdown-articleAccess-reader-NotAny"]')
    view_permissions_button = (By.XPATH, '//div[@class="access__view"]')
    view_permissions_only_me = (By.XPATH, '//div[@test_id = "kb-dropdown-articleAccess-reader-justMe"]')
    view_permissions_someone_button = (By.XPATH, '//div[@test_id = "kb-dropdown-articleAccess-reader-Some"]')
    wait_search_results = (By.XPATH, '//div[@class="search__wrap"]')
    wait_search_results_in_permissions = (By.XPATH, '//div[@class="popup-groups-and-users__scrollbar-element"][1]')


class KnowledgeBaseArticle(AnyPage):

    def page_loaded(self):
        """
        Ждем появления элементов страницы
        """
        self.find_element(Locator.cke_contents)

    @allure.step('Нажать кнопку "Создать статью"')
    def btn_create_article(self):
        # Нажимаем кнопку "Создать статью"
        self.click_element(Locator.button_create_article)
        return self

    @allure.step('Наведение на кнопку "Настройки"')
    def move_to_settings_button(self):
        # Наводимся на кнопку "Настройки"
        self.find_element(Locator.settings_button)
        self.move_to_element(Locator.settings_button)

    @allure.step('Наведение на кнопку "Права просмотра"')
    def move_to_access_view_button(self):
        # Наводимся на кнопку "Настройки"
        self.move_to_element(Locator.settings_button)
        # Наводимся на кнопку "Права просмотра"
        self.move_to_element(Locator.access_view_button)

    @allure.step('Наведение на кнопку "Права редактирования"')
    def move_to_access_edit_button(self):
        # Наводимся на кнопку "Настройки"
        self.move_to_element(Locator.settings_button)
        # Наводимся на кнопку "Права редактирования"
        self.move_to_element(Locator.access_edit_button)

    @allure.step('Нажать кнопку "Редактировать"')
    def button_edit_article(self):
        # Нажимаем на кнопку "Редактировать"
        self.find_element(Locator.edit_button)
        self.click_element(Locator.edit_button)
        return self

    @allure.step('Переход к статье')
    def move_to_article(self, article_name):
        # Нажимаем кнопку "База знаний"
        self.manager.web_any_page.click_knowledge_base_left_menu()
        # Ищем статью
        self.send_keys_slow(Locator.article_search, article_name, 100)
        self.find_element(Locator.wait_search_results)
        results_in_search = (By.XPATH, f'//div[@class="search__wrap"]//p[contains(text(), "{article_name}")]')
        # Нажимаем по статье
        self.click_element(results_in_search)
        return self

    @allure.step('Проверка, что у статьи стоит право просмотра статьи на "Все пользователи"')
    def all_users_view_permissions_of_article_check(self):
        # Наводимся на кнопку "Настройки"
        self.move_to_settings_button()
        # Наводимся на кнопку "Права просмотра"
        self.move_to_access_view_button()
        # Убеждаемся, что стоит право "Все пользователи"
        self.move_to_element(Locator.check_active_all_users_permission)
        permission_name = self.get_tag_text(Locator.check_active_all_users_permission)
        return "Все пользователи" in permission_name

    @allure.step('Проверка, что у статьи стоит право просмотра статьи на "Только я"')
    def only_me_view_permissions_of_article_check(self):
        # Наводимся на кнопку "Права просмотра"
        self.move_to_access_view_button()
        # Убеждаемся, что стоит право "Только я"
        self.move_to_element(Locator.check_active_only_me_permission)
        permission_name = self.get_tag_text(Locator.check_active_only_me_permission)
        return "Только я" in permission_name

    @allure.step('Проверка, что пользователи были выбраны корректно при выставлении права просмотра статьи на "Некоторые пользователи"')
    def someone_view_permissions_of_article_check(self, first_user, second_user):
        first_search_user = self.manager.group_data.users[first_user]['Surname']
        second_search_user = self.manager.group_data.users[second_user]['Surname']
        # Наводимся на кнопку "Настройки"
        self.move_to_settings_button()
        # Наводимся на кнопку "Права просмотра"
        self.move_to_access_view_button()
        # Нажимаем на право "Некоторые пользователи"
        self.click_element(Locator.view_permissions_someone_button)
        # Кликаем по свитчеру "Выбранные"
        self.click_element(Locator.switcher_view_permissions)
        # Проверяем, что выбранные ранее пользователи отображаются в выбранных
        locator_article = (By.XPATH, f"//div[@class='popup-groups-and-users__scrollbar-element']//div[contains(text(), '{first_search_user}')]")
        first_user_name = self.get_tag_text(locator_article)
        locator_article_second = (By.XPATH, f"//div[@class='popup-groups-and-users__scrollbar-element']//div[contains(text(), '{second_search_user}')]")
        second_user_name = self.get_tag_text(locator_article_second)
        return first_search_user in first_user_name and second_search_user in second_user_name

    @allure.step('Проверка, что пользователи были выбраны корректно при выставлении права просмотра статьи на "Все, кроме..."')
    def all_but_view_permissions_of_article_check(self, first_user, second_user):
        first_search_user = self.manager.group_data.users[first_user]['Surname']
        second_search_user = self.manager.group_data.users[second_user]['Surname']
        # Наводимся на кнопку "Настройки"
        self.move_to_settings_button()
        # Наводимся на кнопку "Права просмотра"
        self.move_to_access_view_button()
        # Нажимаем на право "Все кроме..."
        self.click_element(Locator.view_permissions_all_but)
        # Кликаем по свитчеру "Выбранные"
        self.click_element(Locator.switcher_view_permissions)
        # Проверяем, что выбранные ранее пользователи отображаются в выбранных
        locator_article = (By.XPATH, f"//div[@class='popup-groups-and-users__scrollbar-element']//div[contains(text(), '{first_search_user}')]")
        first_user_name = self.get_tag_text(locator_article)
        locator_article_second = (By.XPATH, f"//div[@class='popup-groups-and-users__scrollbar-element']//div[contains(text(), '{second_search_user}')]")
        second_user_name = self.get_tag_text(locator_article_second)
        return first_search_user in first_user_name and second_search_user in second_user_name

    @allure.step('Проверка, что у статьи стоит право редактирования статьи на "Все пользователи"')
    def all_users_edit_permissions_of_article_check(self):
        # Наводимся на кнопку "Настройки"
        self.move_to_settings_button()
        # Наводимся на кнопку "Права редактирования"
        self.move_to_access_edit_button()
        # Убеждаемся, что стоит право "Все пользователи"
        permission_name = self.get_tag_text(Locator.check_active_edit_all_users_permission)
        return "Все пользователи" in permission_name

    @allure.step('Проверка, что у статьи стоит право просмотра статьи на "Только я"')
    def only_me_edit_permissions_of_article_check(self):
        # Наводимся на кнопку "Настройки"
        self.move_to_settings_button()
        # Наводимся на кнопку "Права просмотра"
        self.move_to_access_edit_button()
        # Убеждаемся, что стоит право "Только я"
        permission_name = self.get_tag_text(Locator.check_active_edit_only_me_permission)
        return "Только я" in permission_name

    @allure.step('Проверка, что пользователи были выбраны корректно при выставлении права редактирования статьи на "Некоторые пользователи"')
    def someone_edit_permissions_of_article_check(self, first_user, second_user):
        first_search_user = self.manager.group_data.users[first_user]['Surname']
        second_search_user = self.manager.group_data.users[second_user]['Surname']
        # Наводимся на кнопку "Настройки"
        self.move_to_settings_button()
        # Наводимся на кнопку "Права просмотра"
        self.move_to_access_edit_button()
        # Нажимаем на право "Некоторые пользователи"
        self.click_element(Locator.edit_permissions_someone_button)
        # Кликаем по свитчеру "Выбранные"
        self.click_element(Locator.switcher_view_permissions)
        # Проверяем, что выбранные ранее пользователи отображаются в выбранных
        locator_article = (By.XPATH, f"//div[@class='popup-groups-and-users__scrollbar-element']//div[contains(text(), '{first_search_user}')]")
        self.move_to_element(locator_article)
        first_user_name = self.get_tag_text(locator_article)
        locator_article_second = (By.XPATH, f"//div[@class='popup-groups-and-users__scrollbar-element']//div[contains(text(), '{second_search_user}')]")
        self.move_to_element(locator_article_second)
        second_user_name = self.get_tag_text(locator_article_second)
        return first_search_user in first_user_name and second_search_user in second_user_name

    @allure.step('Проверка, что пользователи были выбраны корректно при выставлении права просмотра статьи на "Все, кроме..."')
    def all_but_edit_permissions_of_article_check(self, first_user, second_user):
        check = False
        first_search_user = self.manager.group_data.users[first_user]['Surname']
        second_search_user = self.manager.group_data.users[second_user]['Surname']
        # Наводимся на кнопку "Настройки"
        self.move_to_settings_button()
        # Наводимся на кнопку "Права просмотра"
        self.move_to_access_edit_button()
        # Нажимаем на право "Все кроме..."
        self.click_element(Locator.edit_permissions_all_but)
        # Кликаем по свитчеру "Выбранные"
        self.click_element(Locator.switcher_view_permissions)
        # Проверяем, что выбранные ранее пользователи отображаются в выбранных
        locator_article = (By.XPATH, f"//div[@class='popup-groups-and-users__scrollbar-element']//div[contains(text(), '{first_search_user}')]")
        first_user_name = self.get_tag_text(locator_article)
        locator_article_second = (By.XPATH, f"//div[@class='popup-groups-and-users__scrollbar-element']//div[contains(text(), '{second_search_user}')]")
        second_user_name = self.get_tag_text(locator_article_second)
        return first_search_user in first_user_name and second_search_user in second_user_name

    @allure.step('Изменяем права просмотра статьи на "Все пользователи"')
    def change_view_permissions_of_article_all_users(self):
        # Наводимся на кнопку "Настройки"
        self.move_to_settings_button()
        # Наводимся на кнопку "Права просмотра"
        self.move_to_access_view_button()
        # Меняем права просмотра на "Все пользователи"
        self.click_element(Locator.view_permissions_all_users)
        return self

    @allure.step('Изменяем права просмотра статьи на "Некоторые пользователи"')
    def change_view_permissions_of_article_someone(self, first_user, second_user):
        first_search_user = self.manager.group_data.users[first_user]['Surname']
        second_search_user = self.manager.group_data.users[second_user]['Surname']
        # Наводимся на кнопку "Настройки"
        self.move_to_settings_button()
        # Наводимся на кнопку "Права просмотра"
        self.move_to_access_view_button()
        # Меняем права просмотра на "Некоторые пользователи"
        self.click_element(Locator.view_permissions_someone_button)
        # Вводим название 1-го пользователя
        self.send_keys_slow(Locator.someone_permissions_window_search, first_search_user, 100)
        self.find_element(Locator.wait_search_results_in_permissions)
        # Находим первого пользователя
        locator_article = (By.XPATH, f"//div[@class='popup-groups-and-users__scrollbar-content']//div[contains(text(), '{first_search_user}')]")
        # Выбираем первого пользователя
        self.click_element(locator_article)
        # Вводим название 2-го пользователя
        self.clear_and_send_keys(Locator.someone_permissions_window_search, second_search_user)
        self.find_element(Locator.wait_search_results_in_permissions)
        # Выбираем второго пользователя
        locator_article_second = (By.XPATH, f"//div[@class='popup-groups-and-users__scrollbar-content']//div[contains(text(), '{second_search_user}')]")
        # Выбираем второго пользователя
        self.click_element(locator_article_second)
        # Нажимаем кнопку "Добавить"
        self.click_element(Locator.add_permissions_button)
        self.move_to_element(Locator.settings_button_wait)
        return self

    @allure.step('Изменяем права просмотра статьи на "Только я"')
    def change_view_permissions_of_article_only_me(self):
        # Наводимся на кнопку "Настройки"
        self.move_to_settings_button()
        # Наводимся на кнопку "Права просмотра"
        self.move_to_access_view_button()
        # Изменяем права просмотра статьи на "Только я"
        self.click_element(Locator.view_permissions_only_me)
        return self

    @allure.step('Изменяем права просмотра статьи на "Все, кроме..."')
    def change_view_permissions_of_article_all_but(self, first_user, second_user):
        first_search_user = self.manager.group_data.users[first_user]['Surname']
        second_search_user = self.manager.group_data.users[second_user]['Surname']
        # Наводимся на кнопку "Настройки"
        self.move_to_settings_button()
        # Наводимся на кнопку "Права просмотра"
        self.move_to_access_view_button()
        # Меняем права просмотра на "Все, кроме..."
        self.click_element(Locator.view_permissions_all_but)
        # Вводим название 1-го пользователя
        self.send_keys_slow(Locator.all_but_permissions_window_search, first_search_user, 100)
        self.find_element(Locator.wait_search_results_in_permissions)
        # Находим первого пользователя
        locator_article = (By.XPATH, f"//div[@class='popup-groups-and-users__scrollbar-content']//div[contains(text(), '{first_search_user}')]")
        # Выбираем первого пользователя
        self.click_element(locator_article)
        # Вводим название 2-го пользователя
        self.clear_and_send_keys(Locator.all_but_permissions_window_search, second_search_user)
        self.find_element(Locator.wait_search_results_in_permissions)
        # Выбираем второго пользователя
        locator_article_second = (By.XPATH, f"//div[@class='popup-groups-and-users__scrollbar-content']//div[contains(text(), '{second_search_user}')]")
        # Выбираем второго пользователя
        self.click_element(locator_article_second)
        # Нажимаем кнопку "Добавить"
        self.click_element(Locator.all_but_add_permission_button)
        self.move_to_element(Locator.settings_button_wait)
        return self

    @allure.step('Изменяем права редактирования статьи на "Все пользователи"')
    def change_edit_permissions_of_article_all_users(self):
        # Наводимся на кнопку "Настройки"
        self.move_to_settings_button()
        # Наводимся на кнопку "Права редактирования"
        self.move_to_access_edit_button()
        # Выбираем право на редактирование статьи
        self.click_element(Locator.change_edit_permissions_all_users)
        return self

    @allure.step('Изменяем права редактирования статьи на "Некоторые пользователи"')
    def change_edit_permissions_of_article_someone(self, first_user, second_user):
        first_search_user = self.manager.group_data.users[first_user]['Surname']
        second_search_user = self.manager.group_data.users[second_user]['Surname']
        # Наводимся на кнопку "Настройки"
        self.move_to_settings_button()
        # Наводимся на кнопку "Права редактирования"
        self.move_to_access_edit_button()
        # Изменяем права просмотра статьи на "Некоторые пользователи"
        self.click_element(Locator.change_edit_permissions_someone)
        # Вводим название 1-го пользователя
        self.send_keys_slow(Locator.someone_permissions_window_search, first_search_user, 100)
        self.find_element(Locator.wait_search_results_in_permissions)
        # Находим первого пользователя
        locator_article = (By.XPATH, f"//div[@class='popup-groups-and-users__scrollbar-content']//div[contains(text(), '{first_search_user}')]")
        # Выбираем первого пользователя
        self.click_element(locator_article)
        # Вводим название 2-го пользователя
        self.clear_and_send_keys(Locator.someone_permissions_window_search, second_search_user)
        self.find_element(Locator.wait_search_results_in_permissions)
        # Выбираем второго пользователя
        locator_article_second = (By.XPATH, f"//div[@class='popup-groups-and-users__scrollbar-content']//div[contains(text(), '{second_search_user}')]")
        # Выбираем второго пользователя
        self.click_element(locator_article_second)
        # Нажимаем кнопку "Добавить"
        self.click_element(Locator.add_permissions_button)
        self.move_to_element(Locator.settings_button_wait)
        return self

    @allure.step('Изменяем права редактирования статьи на "Только я"')
    def change_edit_permissions_of_article_only_me(self):
        # Наводимся на кнопку "Настройки"
        self.move_to_settings_button()
        # Наводимся на кнопку "Права редактирования"
        self.move_to_access_edit_button()
        # Изменяем права просмотра статьи на "Только я"
        self.click_element(Locator.edit_permissions_only_me)
        return self

    @allure.step('Изменяем права редактирования статьи на "Все, кроме..."')
    def change_edit_permissions_of_article_all_but(self, first_user, second_user):
        first_search_user = self.manager.group_data.users[first_user]['Surname']
        second_search_user = self.manager.group_data.users[second_user]['Surname']
        # Наводимся на кнопку "Настройки"
        self.move_to_element(Locator.settings_button_wait)
        self.move_to_settings_button()
        # Наводимся на кнопку "Права редактирования"
        self.move_to_access_edit_button()
        # Изменяем права редактирования статьи на "Все, кроме..."
        self.click_element(Locator.change_edit_permissions_all_but)
        # Вводим название 1-го пользователя
        self.send_keys_slow(Locator.all_but_permissions_window_search, first_search_user, 100)
        self.find_element(Locator.wait_search_results_in_permissions)
        # Находим первого пользователя
        locator_article = (By.XPATH, f"//div[@class='popup-groups-and-users__scrollbar-content']//div[contains(text(), '{first_search_user}')]")
        # Выбираем первого пользователя
        self.click_element(locator_article)
        # Вводим название 2-го пользователя
        self.clear_and_send_keys(Locator.all_but_permissions_window_search, second_search_user)
        self.find_element(Locator.wait_search_results_in_permissions)
        # Выбираем второго пользователя
        locator_article_second = (By.XPATH, f"//div[@class='popup-groups-and-users__scrollbar-content']//div[contains(text(), '{second_search_user}')]")
        # Выбираем второго пользователя
        self.click_element(locator_article_second)
        # Нажимаем кнопку "Добавить"
        self.click_element(Locator.all_but_add_permission_button)
        self.move_to_element(Locator.settings_button_wait)
        return self

    @allure.step('Удаление статьи с удалением подстатей')
    def delete_articles_with_subarticles(self):
        # Наводимся к элементу настроек
        self.move_to_element(Locator.settings_button)
        # Нажимаем в раскрывшейся менюшке кнопку "Удалить"
        self.click_element(Locator.move_delete_button)
        # Нажимаем в раскрывшемся окне свитчер для удаления подстатей
        self.click_element(Locator.delete_switch)
        # Нажимаем кнопку "Удалить"
        self.click_element(Locator.delete_button)
        self.find_element(Locator.cke_contents)
        return self

    @allure.step('Удаление статьи')
    def delete_article(self):
        # Наводимся к элементу настроек
        self.move_to_element(Locator.settings_button)
        # Нажимаем в раскрывшейся менюшке кнопку "Удалить"
        self.click_element(Locator.move_delete_button)
        # Нажимаем кнопку "Удалить"
        self.click_element(Locator.delete_button)
        self.find_element(Locator.cke_contents)
        return self

    @allure.step('Проверка, что удаленная статья появилась в вкладке "В корзине"')
    def check_deleted_article_in_trash_knowledge_base(self, article_name, article_description):
        # Нажимаем кнопку "В корзине"
        self.button_trash_knowledge_base()
        # Вводим в поле ввода название статьи
        self.send_keys_slow(Locator.article_search_input_trash, article_name, 100)
        # Ищем нужную статью
        locator_article = (By.XPATH, f"//div[@class='search__list']/div[@class='search__list']//p[contains(text(), '{article_name}')]")
        # Нажимаем по найденной статье
        self.click_element(locator_article)
        # Получаем название статьи
        name = self.get_name()
        description = self.get_description()
        # Убеждаемся, что нашлась корректная статья
        return name == article_name and description == article_description

    @allure.step('Проверка, что удаленная статья и ее дочерняя статья появилась в вкладке "В корзине"')
    def check_deleted_article_and_subarticle_in_trash_knowledge_base(self, article_first_name, article_first_description, article_second_name, article_second_description):
        # Нажимаем кнопку "В корзине"
        self.button_trash_knowledge_base()
        # Вводим в поле ввода название статьи-родителя
        self.send_keys_slow(Locator.article_search_input_trash, article_first_name, 100)
        # Ищем нужную статью
        locator_article = (By.XPATH, f"//div[@class='search__list']/div[@class='search__list']//p[contains(text(), '{article_first_name}')]")
        # Нажимаем по найденной статье
        self.click_element(locator_article)
        # Получаем название статьи
        first_name = self.get_name()
        first_description = self.get_description()
        # Вводим в поле ввода название дочерней статьи
        self.clear_and_send_keys(Locator.article_search_input_trash, article_second_name)
        # Ищем нужную статью
        locator_article = (By.XPATH, f"//div[@class='search__list']/div[@class='search__list']//p[contains(text(), '{article_second_name}')]")
        # Нажимаем по найденной статье
        self.click_element(locator_article)
        # Получаем название статьи
        second_name = self.get_name()
        second_description = self.get_description()
        # Убеждаемся, что нашлась корректная статья
        return first_name == article_first_name and first_description == article_first_description and second_name == article_second_name and \
               second_description == article_second_description

    @allure.step('Нажать кнопку "В корзине"')
    def button_trash_knowledge_base(self):
        # Нажимаем кнопку "В корзине"
        self.click_element(Locator.trash_button)
        self.find_element(Locator.trash_counts)
        return self

    @allure.step('Восстановление статьи')
    def button_restore_article(self, delete_article):
        # Нажимаем кнопку "В корзине"
        self.button_trash_knowledge_base()
        # Вводим в поле ввода название удалившейся статьи
        self.send_keys_slow(Locator.article_search_input_trash, delete_article, 100)
        # Ищем нужную статью
        locator_article = (By.XPATH, f"//div[@class='search__list']/div[@class='search__list']//p[contains(text(), '{delete_article}')]")
        # Нажимаем по найденной статье
        self.click_element(locator_article)
        # Нажимаем кнопку восстановить (серая кнопка с круглой стрелкой)
        self.click_element(Locator.restore_button)
        # В раскрывшемся окне нажимаем чекбокс "Перейти к восстановленной статье"
        self.click_element(Locator.repair_checkbox)
        # Нажимаем кнопку "Восстановить"
        self.click_element(Locator.repair_button_in_repair_window)
        self.find_element(Locator.tab_all_counts)
        return self

    @allure.step('Проверка, что восстановленная статья появилась в вкладке "Все статьи"')
    def check_restored_article_in_all_knowledge_base(self, repaired_article):
        self.move_to_element(Locator.tabs_knowledge_base_nav)
        self.click_element(Locator.all_articles_button)
        self.send_keys_slow(Locator.article_search_input_trash, repaired_article, 100)
        locator_article = (By.XPATH, f"//div[@class='search__list']//p[contains(text(), '{repaired_article}')]")
        self.click_element(locator_article)
        name = self.get_name()
        return name == repaired_article

    @allure.step('Возвращаем название статьи')
    def get_name(self):
        # Отображаем информацию из описания тикета
        name = self.get_tag_text(Locator.name_text)
        return name

    @allure.step('Возвращаем описание статьи')
    def get_description(self):
        # Отображаем информацию из описания тикета
        description = self.get_tag_text(Locator.description_text)
        return description