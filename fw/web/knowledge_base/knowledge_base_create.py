import time

from selenium.webdriver.common.by import By
import allure
from fw.web.AnyPage import AnyPage

class Locator:
    add_attachments = (By.XPATH, '//div[@class="toolbar toolbar toolbar_btn-pink"]//button[@class="button   button_pink button_big "]')
    add_permissions_button = (By.XPATH, '(//button[@test_id="button-execute"])[1]')
    all_but_add_permission_button = (By.XPATH, '(//button[@test_id="button-execute"])[2]')
    all_but_permission = (By.XPATH, '(//div[@class="access__view"]//div[@class="contextmenu__elem"])[4]')
    all_but_permissions_window_search = (By.XPATH, '(//input[@test_id="custom-input"])[3]')
    all_users_permission = (By.XPATH, '(//div[@class="access__view"]//div[@class="contextmenu__elem"])[1]')
    apply_location_button = (By.XPATH, '//button[@test_id="kb-location-apply"]')
    article_search_input = (By.XPATH, '//div[@class = "popupMoveTo__searchwrap"]/input')
    attachments = (By.XPATH, '//button[@test_id="toolbar-file"]')
    cke_contents = (By.XPATH, '//div[@class="noarticle"]')
    cke_editable_themed = (By.CSS_SELECTOR, '//div[@class="ck ck-editor__main"]')
    change_edit_permissions_all_users = (By.XPATH, '(//div[@class="rightside"]//div[@class="contextmenu__elem"])[5]')
    change_edit_permissions_only_me = (By.XPATH, '(//div[@class="rightside"]//div[@class="contextmenu__elem"])[7]')
    change_edit_permissions_someone = (By.XPATH, '(//div[@class="rightside"]//div[@class="contextmenu__elem"])[6]')
    change_edit_permissions_all_but = (By.XPATH, '(//div[@class="rightside"]//div[@class="contextmenu__elem"])[8]')
    change_location_button = (By.XPATH, '//div[@test_id = "kb-location-button"]')
    change_view_permissions_all_users = (By.XPATH, '(//div[@class="rightside"]//div[@class="contextmenu__elem"])[1]')
    change_view_permissions_someone = (By.XPATH, '(//div[@class="rightside"]//div[@class="contextmenu__elem"])[2]')
    change_view_permissions_all_but = (By.XPATH, '(//div[@class="rightside"]//div[@class="contextmenu__elem"])[4]')
    choose_article_from_search = (By.XPATH, '(//li[@test_id="service-tree-branch"]/div[@class="tree__data tree__data_red"])[1]')
    choose_type_of_files = (By.XPATH, '//div[@class="dropdown-select-category"]')
    choose_images = (By.XPATH, '(//div[@class="dropdown-select-category__content-item"])[2]')
    description_iframe = (By.XPATH, '//div[@class="ck ck-editor__main"]')
    input_text_description = (By.XPATH, '//div[@aria-label="Editor editing area: main"]')
    edit_button = (By.XPATH, '(//div[@class = "article__header"]//button)[1]')
    edit_permissions_button = (By.XPATH, '//div[@class="access__edit"]')
    fixed_panel_submit = (By.XPATH, '//button[@test_id ="fixed-panel-submit"]')
    only_me_permission = (By.XPATH, '(//div[@class="rightside"]//div[@class="contextmenu__elem"])[3]')
    someone_permissions_window_search = (By.XPATH, '(//input[@test_id="custom-input"])[2]')
    someone_permission_button = (By.XPATH, '//div[@test_id="kb-dropdown-articleAccess-reader-Some"]')
    subject_textarea = (By.XPATH, '//div[@test_id="kb-create-article-title"]/textarea')
    trash_counts = (By.XPATH, '//a[@data-manual="kb_goto_trash"]/div[@class="nav__count"]')
    view_permissions_button = (By.XPATH, '//div[@class="access__view"]')
    wait_search_results_in_permissions = (By.XPATH, '//div[@class="popup-groups-and-users__scrollbar-element"][1]')


class KnowledgeBaseCreate(AnyPage):

    @allure.step('Заполнение поля названия')
    def fill_name(self, name_text):
        # Очищаем поле ввода и пишем название статьи
        self.clear_and_send_keys(Locator.subject_textarea, name_text)
        return self

    @allure.step('Заполнение поля описания')
    def fill_description(self, description_text):
        self.clear_and_send_keys(Locator.input_text_description, ' ' + description_text)

        return self

    @allure.step('Изменение расположения статьи')
    def choose_location_of_article(self, correct_article):
        # Нажимаем по элементу "Расположение"
        self.click_element(Locator.change_location_button)
        # Вводим нужное расположение
        self.send_keys_slow(Locator.article_search_input, correct_article, 100)
        # Выбираем искомую родительскую статью
        self.click_element(Locator.choose_article_from_search)
        # Нажимаем кнопку "Сохранить"
        self.click_element(Locator.apply_location_button)
        return self

    @allure.step('Изменяем права просмотра статьи на "Все пользователи"')
    def change_view_permissions_of_article_all_users(self):
        # Нажимаем по элементу "Вид"
        self.click_element(Locator.view_permissions_button)
        # Изменяем права просмотра статьи на "Все пользователи"
        self.click_element(Locator.all_users_permission)
        return self

    @allure.step('Изменяем права просмотра статьи на "Только я"')
    def change_view_permissions_of_article_only_me(self):
        # Нажимаем по элементу "Вид"
        self.click_element(Locator.view_permissions_button)
        # Изменяем права просмотра статьи на "Только я"
        self.click_element(Locator.only_me_permission)
        return self

    @allure.step('Изменяем права просмотра статьи на "Некоторые пользователи"')
    def change_view_permissions_of_article_someone(self, first_user, second_user):
        first_search_user = self.manager.group_data.users[first_user]['Surname']
        second_search_user = self.manager.group_data.users[second_user]['Surname']
        # Нажимаем по элементу "Вид"
        self.click_element(Locator.view_permissions_button)
        # Изменяем права просмотра статьи на "Некоторые пользователи"
        self.click_element(Locator.change_view_permissions_someone)
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
        return self

    @allure.step('Изменяем права просмотра статьи на "Все, кроме..."')
    def change_view_permissions_of_article_all_but(self, first_user, second_user):
        first_search_user = self.manager.group_data.users[first_user]['Surname']
        second_search_user = self.manager.group_data.users[second_user]['Surname']
        # Нажимаем по элементу "Вид"
        self.click_element(Locator.view_permissions_button)
        # Изменяем права просмотра статьи на "Все, кроме..."
        self.click_element(Locator.all_but_permission)
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
        return self

    @allure.step('Изменяем права редактирования статьи на "Все пользователи"')
    def change_edit_permissions_of_article_all_users(self):
        # Нажимаем по элементу "Редактирование"
        self.click_element(Locator.edit_permissions_button)
        # Выбираем право на редактирование статьи
        self.click_element(Locator.change_edit_permissions_all_users)
        return self

    @allure.step('Изменяем права редактирования статьи на "Только я"')
    def change_edit_permissions_of_article_only_me(self):
        # Нажимаем по элементу "Редактирование"
        self.click_element(Locator.edit_permissions_button)
        # Выбираем право на редактирование статьи
        self.click_element(Locator.change_edit_permissions_only_me)
        return self

    @allure.step('Изменяем права редактирования статьи на "Некоторые пользователи"')
    def change_edit_permissions_of_article_someone(self, first_user, second_user):
        first_search_user = self.manager.group_data.users[first_user]['Surname']
        second_search_user = self.manager.group_data.users[second_user]['Surname']
        # Нажимаем по элементу "Редактирование"
        self.click_element(Locator.edit_permissions_button)
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
        return self

    @allure.step('Изменяем права редактирования статьи на "Все, кроме..."')
    def change_edit_permissions_of_article_all_but(self, first_user, second_user):
        first_search_user = self.manager.group_data.users[first_user]['Surname']
        second_search_user = self.manager.group_data.users[second_user]['Surname']
        # Нажимаем по элементу "Редактирование"
        self.click_element(Locator.edit_permissions_button)
        # Изменяем права просмотра статьи на "Все, кроме..."
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
        return self

    @allure.step('Нажать кнопку "Сохранить"')
    def button_save_article(self):
        # Наводимся на кнопку "Сохранить"
        self.move_to_element(Locator.fixed_panel_submit)
        # Нажимаем кнопку "Сохранить"
        self.click_element(Locator.fixed_panel_submit)
        self.find_element(Locator.trash_counts)
        return self


