import allure
from selenium.webdriver.common.by import By

from fw.web.tickets.tickets_base import TicketsBase


class Locator:
    page_loaded = (By.XPATH, '//div[@class="async-wrapper-constructor-type-field-editor"]')
    search_panel = (By.XPATH, '//div[@class="search-panel-container"]')
    append_description_editor = (By.XPATH, '//div[@test_id="append-description-editor"]')
    show_more = (By.XPATH, '//div[@class="show-more__btn"]//span')
    append_description_open_editor = (By.CSS_SELECTOR, '[test_id="append-description-open-editor"]')
    append_description_editor_iframe = (By.CSS_SELECTOR, '[test_id="append-description-editor"] iframe')
    cke_editable_themed = (By.CSS_SELECTOR, '.cke_editable_themed')
    append_description_submit_btn = (By.CSS_SELECTOR, '[test_id="append-description-submit-btn"]')
    contractors_activator_in_projects = (By.XPATH, '(//section[@class="sidebar-ticket ticket-sidebar__wrap border"]//div[@class="user-avatar"])[1]')
    button_edit_contractor = (By.XPATH, '//div[@test_id="-dropdown-content"]//div[@class="action"]')
    contractors_search_input = (By.XPATH, '//div[@test_id="anchor"]//input')


class ProjectId(TicketsBase):

    def page_loaded(self):
        """
        Ждем появления элементов страницы
        """
        self.find_element(Locator.page_loaded)
        self.find_element(Locator.search_panel)

    @allure.step('Нажать кнопку Показать все')
    def click_show_more(self):
        self.page_loaded()
        self.click_element(Locator.show_more)
        return self

    @allure.step('Добавить дополнительное описание')
    def add_additional_description(self, information_text):
        # Кнопка добавления дополнительного описания
        self.click_element(Locator.append_description_open_editor)
        # Вводим текст в поле "описание"
        self.find_element(Locator.append_description_editor)
        self.send_keys_in_frame_with_delete_text(Locator.append_description_editor_iframe, Locator.cke_editable_themed, information_text)
        # Кнопка добавления дополнилнительного описания
        self.click_element(Locator.append_description_submit_btn)
        return self

    @allure.step('Изменение исполнителя')
    def changing_contractor(self, correct_contractor):
        # Нажимаем на аватар исполнителя
        self.click_element(Locator.contractors_activator_in_projects)
        # Нажимаем на кнопку Изменить
        self.click_element(Locator.button_edit_contractor)
        # Поиск пользователя для добавления
        self.send_keys_slow(Locator.contractors_search_input, correct_contractor, 100)
        # Выбор пользователя из списка
        locator_contractor = (By.XPATH, f"//div[contains(@class, 'item__name')][contains(text(), '{correct_contractor}')]")
        self.click_element(locator_contractor)
        self.waiting_the_correct_contractor(correct_contractor)
        return correct_contractor





