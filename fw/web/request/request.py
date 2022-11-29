from selenium.webdriver.common.by import By
import allure
import time

from fw.web.web_base import WebBase


class Locator:
    button_tree_services = (By.CSS_SELECTOR, '[test_id="service-tree-btn"]')
    search_services_in_tree = (By.XPATH, '//div[@class="popup-service__search"]/input')
    apply_services = (By.CSS_SELECTOR, '[test_id="apply-service"]')
    contractors_rgs = (By.XPATH, '//div[@class ="contractors"]/div[4]')


class RequestCreate(WebBase):


    @allure.step('Выбор услуги из дерева при создании заявки')
    def select_services_in_tree(self, name_text):
        # Переходим в дерево услуг
        self.click_element(Locator.button_tree_services)
        # Ищем услугу
        self.send_keys_slow(Locator.search_services_in_tree, name_text, 100)
        # Выбираем услугу
        catalogue_item_name = (By.XPATH, f'//li[@test_id="service-tree-branch"]//p[contains(text(),"{name_text}")]')
        self.click_element(catalogue_item_name)
        # Применяем услугу
        self.click_element(Locator.apply_services)
        # Ждем появления элементов страницы
        self.find_element(Locator.contractors_rgs)


