import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from fw.web.AnyPage import AnyPage
import time


class Locator:
    page_loaded = (By.XPATH, '//div[@class="sidebar-catalogue-list__content"]')
    value_a_catalogue_loaded = (By.XPATH, '//div[contains(@class, "ticket-list-wrap__content ticket-list ps")]')
    button_create_catalogue = (By.XPATH, '//button[@test_id="page-header-btn-right-add"]')
    button_create_new = (By.XPATH, '//div[@class="select-entity-or-create__text"]/span/span')
    button_add_in_tree = (By.XPATH, '//div[@test_id="sidebar-btn-add"]')
    click_to_first_catalogue_in_tree = (By.XPATH, '//div[@class="sidebar-catalogue-list__content"]/div')
    click_to_first_line_in_catalogue = (By.XPATH, '//div[@test_id="table-row-0"]')
    button_add_catalogue_in_pop_up_block = (By.XPATH, '//div[@test_id="context-menu-add-guide"]')
    button_delete_catalogue_in_pop_up_block = (By.XPATH, '//div[@test_id="context-menu-delete"]')
    button_change_catalogue_in_pop_up_block = (By.XPATH, '//div[@test_id="context-menu-change"]')
    button_duplicate_catalogue_in_pop_up_block = (By.XPATH, '//div[@test_id="context-menu-duplicate"]')
    fill_name_catalogue = (By.XPATH, '//input[@test_id="enter-guide-name"]')
    number_of_entries_in_search_catalogue = (By.XPATH, '//div[@class="search-panel__input-result"] ')
    fill_a_name_additional_field = (By.XPATH, '//input[@test_id="flex-input"]')
    click_status_for_used = (By.XPATH, '//div[@test_id="tab-use"]')
    click_status_for_not_used = (By.XPATH, '//div[@test_id="tab-not-use"]')
    button_create_in_pop_up_block = (By.XPATH, '//div[contains(@class, "buttons-panel-for-popup")]/button[@test_id="button-execute"]')
    button_add_in_pop_up_block = (By.XPATH, '//div[@class="fixed-panel__content"]/button')
    button_confirm_delete_object = (By.XPATH, '//button[@test_id="button-execute"]')
    button_to_add_value = (By.XPATH, '//button[@test_id="page-header-btn-right-add"]')
    button_cross_in_pop_up_block = (By.XPATH, '//span[@test_id="popup-close"]')
    button_cancel_in_pop_up_block = (By.XPATH, '//button[@test_id="button-cancel"]')
    button_add_value_in_catalogue = (By.XPATH, '//div[@test_id="add-guide-row-on-clear-guide"]')
    button_add_value = (By.XPATH, '//div[@test_id="context-menu-add-guide-row"]')
    button_delete_in_pop_up_block_value = (By.XPATH, '//div[@class ="top-buttons"]/button')
    search_tree = (By.XPATH, '//input[@test_id="custom-input"]')
    fill_mandatory_field = (By.XPATH, '//div[@class="guide-types-picker"]//input')
    wait_pop_up_block = (By.XPATH, '//span[@class="popup__title"]')
    name_catalogue = (By.XPATH, '//h1[@class="page-header__title"]')
    content_in_pop_up_block = (By.XPATH, '//div[@class="content"]')
    wait_check_box = (By.XPATH, '//span[@class="popup__title"]')


class CustomFieldDictionary(AnyPage):

    def page_loaded(self):
        """
        Ждем появления элементов страницы
        """
        self.find_element(Locator.page_loaded)

    def value_a_catalogue_loaded(self):
        """
        Ждем появления значений справочника
        """
        self.find_element(Locator.value_a_catalogue_loaded)

    @allure.step('Нажать кнопку "Создать справочник"')
    def button_create_catalogue(self):
        self.click_element(Locator.button_create_catalogue)
        return self

    @allure.step('Нажать кнопку "создайте новый"')
    def button_create_new(self):
        self.click_element(Locator.button_create_new)
        return self

    @allure.step('Нажать кнопку "Добавить" в дереве')
    def button_add_in_tree(self):
        self.click_element(Locator.button_add_in_tree)
        return self

    @allure.step('Нажать на первый справочник в дереве правой кнопкой мыши')
    def button_right_click_on_the_first_catalogue_in_tree(self):
        self.right_click(Locator.click_to_first_catalogue_in_tree)
        return self

    @allure.step('Нажать на первый справочник в дереве')
    def button_click_on_the_first_catalogue_in_tree(self):
        self.click_element(Locator.click_to_first_catalogue_in_tree)
        return self

    @allure.step('Нажать кнопку Добавить справочник во всплывающем меню в дереве')
    def button_add_catalogue_in_pop_up_block_in_tree(self):
        self.page_loaded()
        # Нажимаем на правую кнопку мыши в дереве
        self.button_right_click_on_the_first_catalogue_in_tree()
        # Нажимаем на кнопку "Добавить справочник" во всплывающем меню
        self.click_element(Locator.button_add_catalogue_in_pop_up_block)
        return self

    @allure.step('Нажать кнопку Удалить во всплывающем меню в дереве')
    def button_delete_in_pop_up_block_in_tree(self):
        self.page_loaded()
        # Нажимаем на правую кнопку мыши в дереве
        self.button_right_click_on_the_first_catalogue_in_tree()
        # Нажимаем на кнопку "Удалить" во всплывающем меню
        self.click_element(Locator.button_delete_catalogue_in_pop_up_block)
        return self

    @allure.step('Нажать кнопку Изменить во всплывающем меню в дереве')
    def button_change_in_pop_up_block_in_tree(self):
        self.page_loaded()
        # Нажимаем на правую кнопку мыши в дереве
        self.button_right_click_on_the_first_catalogue_in_tree()
        # Нажимаем на кнопку "Изменить" во всплывающем меню
        self.click_element(Locator.button_change_catalogue_in_pop_up_block)
        return self

    @allure.step('Нажать кнопку Дублировать во всплывающем меню в дереве')
    def button_duplicate_in_pop_up_block_in_tree(self):
        self.page_loaded()
        # Нажимаем на правую кнопку мыши в дереве
        self.button_right_click_on_the_first_catalogue_in_tree()
        # Нажимаем на кнопку "Дублировать" во всплывающем меню
        self.click_element(Locator.button_duplicate_catalogue_in_pop_up_block)
        return self

    @allure.step('Нажать на первую строку справочника правой кнопкой мыши')
    def button_right_click_on_the_first_line_in_catalogue(self):
        self.right_click(Locator.click_to_first_line_in_catalogue)
        return self

    @allure.step('Нажать кнопку Добавить значение во всплывающем меню в справочнике')
    def button_add_value_in_pop_up_block_in_catalogue(self):
        self.page_loaded()
        # Нажимаем на правую кнопку мыши в справочнике
        self.button_right_click_on_the_first_line_in_catalogue()
        # Нажимаем на кнопку "Добавить значение" во всплывающем меню
        self.click_element(Locator.button_add_value)
        return self

    @allure.step('Нажать кнопку Удалить во всплывающем меню в справочнике')
    def button_delete_in_pop_up_block_in_catalogue(self):
        self.page_loaded()
        # Нажимаем на правую кнопку мыши в справочнике
        self.button_right_click_on_the_first_line_in_catalogue()
        # Нажимаем на кнопку "Удалить" во всплывающем меню
        self.click_element(Locator.button_delete_catalogue_in_pop_up_block)
        return self

    @allure.step('Нажать кнопку Изменить во всплывающем меню в справочнике')
    def button_change_in_pop_up_block_in_catalogue(self):
        self.page_loaded()
        # Нажимаем на правую кнопку мыши в справочнике
        self.button_right_click_on_the_first_line_in_catalogue()
        # Нажимаем на кнопку "Изменить" во всплывающем меню
        self.click_element(Locator.button_change_catalogue_in_pop_up_block)
        return self

    @allure.step('Нажать кнопку Дублировать во всплывающем меню в справочнике')
    def button_duplicate_in_pop_up_block_in_catalogue(self):
        self.page_loaded()
        # Нажимаем на правую кнопку мыши в справочнике
        self.button_right_click_on_the_first_line_in_catalogue()
        # Нажимаем на кнопку "Дублировать" во всплывающем меню
        self.click_element(Locator.button_duplicate_catalogue_in_pop_up_block)
        return self

    @allure.step('Заполнение название справочника')
    def fill_name_catalogue(self, name_text):
        self.send_keys_slow(Locator.fill_name_catalogue, name_text, 100)
        return self

    @allure.step('Заполнение названия поля')
    def fill_name_field(self, name_text):
        self.send_keys_slow(Locator.fill_a_name_additional_field, name_text, 100)
        return self

    @allure.step('Проверка количества значений в строке поиска')
    def get_count_values(self):
        self.value_a_catalogue_loaded()
        time.sleep(0.3)
        # Отображаем информацию по количеству записей справочника в поисковой строке (n записей)
        check_number_of_entries = self.get_tag_text(Locator.number_of_entries_in_search_catalogue)
        # Разделяем строку на несколько элементов, между которыми стоит пробел ("n" и "записей")
        only_count = check_number_of_entries.split()
        # Первый элемент присваиваем и фиксируем его числом
        count_values = int(only_count[0])
        return count_values

    @allure.step('Нажать на статус Используется')
    def click_status_for_used(self):
        self.click_element(Locator.click_status_for_used)
        return self

    @allure.step('Нажать на статус Не используется')
    def click_status_for_not_used(self):
        self.click_element(Locator.click_status_for_not_used)
        return self

    @allure.step('Нажать кнопку Создать во всплывающем меню')
    def button_create_in_pop_up_block(self):
        self.click_element(Locator.button_create_in_pop_up_block)
        return self

    @allure.step('Подвердить удаление обьекта')
    def confirm_delete_object(self):
        self.click_element(Locator.button_confirm_delete_object)
        self.refresh_the_page()
        return self

    @allure.step('Удаление значения в пользовательском справочнике через ПКМ на строку и кнопку Изменить')
    def delete_value_first(self):
        # Переходим к удалению значения
        self.button_delete_in_pop_up_block_in_catalogue()
        # Подтверждаем удаление значения
        self.confirm_delete_object()
        return self

    @allure.step('Удаление значения в пользовательском справочнике через ПКМ на строку и кнопку Удалить')
    def delete_value_second(self):
        # Переходим к редактированию значения
        self.button_change_in_pop_up_block_in_catalogue()
        # Нажимаем кнопку Удалить
        self.button_delete_in_pop_up_block_value()
        # Подтверждаем удаление значения
        self.confirm_delete_object()
        return self

    @allure.step('Нажать кнопку Добавить значение')
    def button_to_add_value(self):
        # Ожидаем, пока появятся значения справочника
        self.find_element(Locator.value_a_catalogue_loaded)
        time.sleep(0.3)
        self.click_element(Locator.button_to_add_value)
        return self

    @allure.step('Нажать на крестик во всплывающем блоке')
    def button_cross_in_pop_up_block(self):
        time.sleep(0.2)
        self.click_element(Locator.button_cross_in_pop_up_block)
        return self

    @allure.step('Нажать кнопку Отменить во всплывающем блоке')
    def button_cancel_in_pop_up_block(self):
        # Ожидаем, пока появится всплывающее меню
        self.find_element(Locator.wait_pop_up_block)
        self.click_element(Locator.button_cancel_in_pop_up_block)
        return self

    @allure.step('Проверяем, есть ли первая строка в справочнике')
    def checking_the_presence_of_first_string_in_catalogue(self):
        try:
            (By.CSS_SELECTOR, '[test_id="table-row-0"]')
        except NoSuchElementException:
            return False
        return True

    @allure.step('Удаляем все значения пользовательского справочника')
    def delete_all_value_a_custom_field_dictionary(self):
        # Проверяем,есть ли строки в пользовательском справочнике
        self.page_loaded()
        check = self.checking_the_presence_of_first_string_in_catalogue()
        if check == True:
            # Если строки есть, получаем их количество
            count = self.get_count_values()
            # Удаляем все строки
            for i in range(0, count):
                # Пока есть строки в пользовательском справочнике, удаляем их
                self.button_delete_in_pop_up_block_in_catalogue()
                self.confirm_delete_object()
                self.refresh_the_page()
                self.value_a_catalogue_loaded()
            self.refresh_the_page()
        return self

    @allure.step('Нажать кнопку Добавить в справочнике')
    def button_add_in_catalogue(self):
        time.sleep(1)
        self.value_a_catalogue_loaded()
        self.click_element(Locator.button_add_value_in_catalogue)
        return self

    @allure.step('Нажать кнопку Добавить во всплывающем меню')
    def button_add_in_pop_up_block(self):
        self.click_element(Locator.button_add_in_pop_up_block)
        time.sleep(1)
        return self

    @allure.step('Нажать кнопку Удалить в меню Значение')
    def button_delete_in_pop_up_block_value(self):
        self.click_element(Locator.button_delete_in_pop_up_block_value)
        return self

    @allure.step('Ввод текста в поиск дерева')
    def fill_text_for_search_in_tree(self, name_text):
        self.page_loaded()
        self.send_keys_slow(Locator.search_tree, name_text, 100)
        return self

    @allure.step('Заполнение обязательного поля')
    def fill_mandatory_field(self, name_text):
        self.send_keys_slow(Locator.fill_mandatory_field, name_text, 100)
        return self

    @allure.step('Переходим в справочник с нужным названием')
    def go_to_catalogue_in_list(self, name_catalogue):
        time.sleep(1)
        catalogue_item_name = (By.XPATH, f'//div[contains(text(),"{name_catalogue}")]')
        self.move_to_element(catalogue_item_name)
        self.click_element(catalogue_item_name)
        return self

    @allure.step('Добавляем значение в пользовательский справочник через кнопку Добавить значение')
    def add_value_a_custom_field_dictionary_first(self):
        self.button_to_add_value()
        text_value = 'TestValue AutomationWebTests ' + self.manager.time.get_date_time_Y_m_d_H_M_S()
        self.fill_mandatory_field(text_value)
        self.button_add_in_pop_up_block()
        # Ждем, пока значение с нужным текстом появится
        locator_text_value = (By.XPATH, f'//*[text()="{text_value}"]')
        self.find_element(locator_text_value)
        return self

    @allure.step('Добавляем значение в пользовательский справочник через ПКМ на строку и кнопку Добавить значение')
    def add_value_a_custom_field_dictionary_second(self):
        self.button_add_value_in_pop_up_block_in_catalogue()
        text_value = 'TestValue AutomationWebTests ' + self.manager.time.get_date_time_Y_m_d_H_M_S()
        self.fill_mandatory_field(text_value)
        self.button_add_in_pop_up_block()
        # Ждем, пока значение с нужным текстом появится
        locator_text_value = (By.XPATH, f'//*[text()="{text_value}"]')
        self.find_element(locator_text_value)
        return self

    @allure.step('Добавляем значение в пользовательский справочник через кнопку Добавить, когда справочник пуст')
    def add_value_a_custom_field_dictionary_third(self):
        self.button_add_in_catalogue()
        text_value = 'TestValue AutomationWebTests ' + self.manager.time.get_date_time_Y_m_d_H_M_S()
        self.fill_mandatory_field(text_value)
        self.button_add_in_pop_up_block()
        # Ждем, пока значение с нужным текстом появится
        locator_text_value = (By.XPATH, f'//*[text()="{text_value}"]')
        self.find_element(locator_text_value)
        return self

    @allure.step('Возвращаем заголовок всплывающего окна')
    def get_title_pop_up_block(self):
        time.sleep(0.3)
        title = self.get_tag_text(Locator.wait_pop_up_block)
        return title

    @allure.step('Возвращаем название справочника')
    def get_name_custom_field_dictionary(self):
        time.sleep(0.3)
        title = self.get_tag_text(Locator.name_catalogue)
        return title

    @allure.step('Проверяем статус пользовательского справочника')
    def check_status_custom_field_dictionary(self, status):
        if status == 'use':
            attribute = self.get_tag_attribute(Locator.click_status_for_used, 'class')
            if 'tab_active' in attribute:
                return True
            else:
                return False
        else:
            attribute = self.get_tag_attribute(Locator.click_status_for_not_used, 'class')
            if 'tab_active' in attribute:
                return True
            else:
                return False



