import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import allure
from fw.web.AnyPage import AnyPage


class Locator:
    apply_location_button = (By.XPATH, '//button[@test_id="kb-location-apply"]')
    article_search_input = (By.XPATH, '//div[@class = "popupMoveTo__searchwrap"]/input')
    change_location_button = (By.XPATH, '//div[@test_id = "kb-location-button"]')
    change_location_link = (By.XPATH, '//div[@class = "location__title"]')
    choose_article_from_search = (By.XPATH, '(//li[@test_id="service-tree-branch"]/div[@class="tree__data tree__data_red"])[1]')
    cke_contents = (By.XPATH, '//div[@class="noarticle"]')
    edit_button = (By.XPATH, '(//div[@class = "article__header"]//button)[1]')
    edit_name = (By.XPATH, '//div[@class="subject subject__title title"]/textarea')
    edit_description = (By.XPATH, '//div[@aria-label="Editor editing area: main"]')
    fixed_panel_submit = (By.XPATH, '//button[@test_id ="fixed-panel-submit"]')
    location = (By.XPATH, '//div[@class="location__block"]')
    trash_counts = (By.XPATH, '//a[@data-manual="kb_goto_trash"]/div[@class="nav__count"]')
    wait_page_load = (By.XPATH, '//div[@class="rightside__base rightside__block"]')


class KnowledgeBaseEdit(AnyPage):

    @allure.step('Проверка выбранного расположения статьи')
    def check_article_location(self, article_location):
        check = False
        # Нажимаем на кнопку "Редактировать"
        self.manager.web_knowledge_base_article.button_edit_article()
        # Получаем расположение статьи
        self.move_to_element(Locator.wait_page_load)
        current_article_location = self.get_tag_text(Locator.location)
        if article_location in current_article_location:
            check = True
        self.button_save_article()
        return check

    @allure.step('Редактирование поля названия')
    def edit_name(self, name_text):
        # Нажимаем кнопку редактировать
        self.manager.web_knowledge_base_article.button_edit_article()
        # Находим объект
        web_element = self.find_element(Locator.edit_name)
        # Очищаем поле для ввода названия
        web_element.send_keys(Keys.CONTROL, "a")
        web_element.send_keys(Keys.DELETE)
        # Вводим название статьи
        self.send_keys(Locator.edit_name, name_text)
        return self

    @allure.step('Редактирование поля описания')
    def edit_description(self, description_text):
        # Нажимаем кнопку "Редактировать"
        self.manager.web_knowledge_base_article.button_edit_article()
        # Находим объект
        web_element = self.find_element(Locator.edit_description)
        # Очищаем поле для ввода названия
        web_element.send_keys(Keys.CONTROL, "a")
        web_element.send_keys(Keys.DELETE)
        # Вводим название статьи
        self.send_keys(Locator.edit_description, description_text)
        return self

    @allure.step('Нажать кнопку "Сохранить"')
    def button_save_article(self):
        # Нажимаем кнопку "Сохранить"
        self.click_element(Locator.fixed_panel_submit)
        self.find_element(Locator.trash_counts)
        return self

    @allure.step('Изменение расположения статьи')
    def change_location_of_article(self, correct_article):
        # Нажимаем кнопку "Редактировать"
        self.manager.web_knowledge_base_article.button_edit_article()
        # Нажимаем по элементу "Расположение"
        self.click_element(Locator.change_location_link)
        # Вводим нужное расположение
        self.send_keys_slow(Locator.article_search_input, correct_article, 100)
        # Выбираем искомую родительскую статью
        self.click_element(Locator.choose_article_from_search)
        # Нажимаем кнопку "Сохранить"
        self.click_element(Locator.apply_location_button)
        return self