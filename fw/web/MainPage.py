from fw.web.AnyPage import AnyPage
from selenium.webdriver.common.by import By
import allure


class MainPage(AnyPage):

    @allure.step('input_text_in_search - {text}')
    def input_text_in_search(self, text):
        element = self.GetDriver().find_element(By.XPATH, '//input[@name="text"]')
        element.send_keys(text)
        self.allure_screenshot()
        return self

    @allure.step('click_button_submit')
    def click_button_submit(self):
        self.GetDriver().find_element(By.XPATH, '//button[@type="submit"]').click()
        self.allure_screenshot()
        return self.manager.web_search
