import allure
from selenium.webdriver.common.by import By

from fw.web.AnyPage import AnyPage


class Locator:
    cke_contents = (By.XPATH, '//div[@class="left-panel-default__scroll ps"]')
    search_tree = (By.XPATH, '//div[@class="left-panel-default__search-dialogs"]//input')
    input_text_in_chat = (By.XPATH, '//div[@class="chat-footer"]//textarea')
    send_message = (By.XPATH, '//div[@class="microphone-or-send"]/button')
    left_panel_preloader = (By.XPATH, '//div[contains(@class, "left-panel-default__scroll")]//div[contains(@class, "preloader")]')
    title_on_the_page_messenger = (By.XPATH, '//h1[@class="page-title__text"]')


class MessengerWeb(AnyPage):

    def page_loaded(self):
        """
        Ждем появления элементов страницы
        """
        self.waiting_for_item_not_display(Locator.left_panel_preloader)

    @allure.step('Ввод текста в поиск дерева чатов')
    def fill_text_for_search_in_tree(self, name_text):
        self.send_keys_slow(Locator.search_tree, name_text, 100)
        return self

    @allure.step('Выбрать чат')
    def select_chat(self, name_chat):
        chat_name = (By.XPATH, f'//div[@class="chat-participants"]//div[contains(text(),"{name_chat}")]')
        self.click_element(chat_name)
        return self

    @allure.step('Ввод текста для сообщения')
    def fill_text_for_message(self, name_text):
        self.send_keys_slow(Locator.input_text_in_chat, name_text, 100)
        return self

    @allure.step('Нажать кнопку Отправить')
    def button_send_message(self):
        self.click_element(Locator.send_message)
        return self

    @allure.step('Получаем текст заголовка страницы мессенджера')
    def get_text_title_on_the_page_messenger(self):
        text_title = self.get_tag_text(Locator.title_on_the_page_messenger)
        return text_title

