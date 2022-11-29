import allure

from fw.fw_base import FWBase


class MobileBase(FWBase):

    _button_enter = '//android.widget.Button'

    def GetADriver(self):
        if self.manager.appium_instance.appium_driver is None:
            self.manager.appium_instance.get_Appium_Driver_Instance()
        return self.manager.appium_instance.appium_driver

    @allure.step('Задержка')
    def appium_driver_sleep(self, time):
        self.GetADriver().implicitly_wait(time)

    @allure.step('Переключить контекст')
    def appium_driver_switch_to(self, context):
        self.GetADriver().switch_to.context(context)

    def click_button_enter(self):
        self.click_by_xpath(self._button_enter)
        self.appium_driver_switch_to('WEBVIEW_chrome')
        return self.manager.mob_auth

    @allure.step('click')
    def click_by_xpath(self, locator):
        self.GetADriver().find_element(locator).click()

    @allure.step('Ввод текста')
    def send_keys_by_xpath(self, locator, text):
        self.GetADriver().find_element(locator).send_keys(text)

    def hide_keyboard(self):
        self.GetADriver().hide_keyboard()

    @allure.step('Ввод текста')
    def clear_and_send_keys_by_xpath(self, locator, text):
        self.clear_text(locator)
        self.GetADriver().find_element(locator).send_keys(text)

    def get_tag_text(self, locator):
        text = self.GetADriver().find_element(locator).text
        return text

    @allure.step('Очистка текстового поля')
    def clear_text(self, locator):
        self.GetADriver().find_element(locator).clear()

    @allure.step('Задержка')
    def sleep_mob(self, time):
        self.GetADriver().implicitly_wait(time)

    @allure.step('Переключить контекст')
    def driver_switch_to(self, context):
        self.GetADriver().switch_to.context(context)
