from fw.fw_base import FWBase
from time import sleep

import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class WebBase(FWBase):

    def GetDriver(self):
        if self.manager.driver_instance.driver is None:
            self.manager.driver_instance.get_driver()
        return self.manager.driver_instance.driver

    def allure_screenshot(self):
        try:
            allure.attach(self.GetDriver().get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except Exception as e:
            print(str(e))

    @allure.step('Open main page')
    def open_main_page(self):
        main_page = self.manager.settings.GLOBAL[self.manager.settings.branch]['main_page']
        title = self.GetDriver().title
        if main_page not in title:
            self.GetDriver().get(main_page)

    @allure.step('GoTo URL - {page}')
    def goto_page(self, page):
        title = self.GetDriver().title
        if page not in title:
            self.GetDriver().get(page)

    @allure.step('click')
    def click_element(self, locator):
        try:
            web_element = self.find_element(locator)
            web_element.click()

        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)
        except StaleElementReferenceException as e:
            self.allure_StaleElementReferenceException(e)

    @allure.step('Send keys')
    def send_keys(self, locator, text):
        try:
            web_element = self.find_element(locator)
            web_element.send_keys(text)

        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)
        except StaleElementReferenceException as e:
            self.allure_StaleElementReferenceException(e)

    @allure.step('Clear and send keys')
    def clear_and_send_keys(self, locator, text):
        try:
            web_element = self.find_element(locator)
            self.scroll_to_element(locator)
            web_element.clear()
            web_element.send_keys(text)

        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)
        except StaleElementReferenceException as e:
            self.allure_StaleElementReferenceException(e)

    def get_tag_text(self, locator):
        try:
            text = self.find_element(locator).text
            return text
        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)

    def get_tag_attribute(self, locator, attribute_name):
        try:
            return self.find_element(locator).get_attribute(attribute_name)
        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)

    def scroll_to_element(self, locator):
        try:
            element = self.find_element(locator).location_once_scrolled_into_view
            script = "window.scrollBy(" + str(element['x'] - 180) + ", " + str(element['y'] - 180) + ")"
            self.GetDriver().execute_script(script)
        except StaleElementReferenceException as e:
            self.allure_ElementNotVisibleException(e)

    @allure.step('Clear')
    def clear_keys(self, locator):
        try:
            self.find_element(locator).clear()
        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)

    def get_current_url(self):
        return self.GetDriver().current_url

    @allure.step('Right click')
    def right_click(self, locator):
        try:
            action_chains = ActionChains(self.GetDriver())
            element = self.find_element(locator)
            action_chains.context_click(element).perform()
        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)

    @allure.step('Double click')
    def double_click(self, locator):
        try:
            action_chains = ActionChains(self.GetDriver())
            action_chains.double_click(self.GetDriver().find_element(locator)).perform()
        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)

    @allure.step('Refresh page')
    def refresh_the_page(self):
        try:
            self.GetDriver().refresh()
        except StaleElementReferenceException:
            pass

    @allure.step('Ввод текста в iframe с удалением предыдущего текста')
    def send_keys_in_frame_with_delete_text(self, locator_frame, locator_in_frame, text):
        frame = self.find_element(locator_frame)
        self.GetDriver().switch_to.frame(frame)
        self.clear_and_send_keys(locator_in_frame, text)
        self.GetDriver().switch_to.default_content()

    @allure.step('Ввод текста в iframe без удаления предыдущего текста')
    def send_keys_in_frame_without_delete_text(self, locator_frame, locator_in_frame, text):
        frame = self.find_element(locator_frame)
        self.GetDriver().switch_to.frame(frame)
        self.send_keys(locator_in_frame, text)
        self.GetDriver().switch_to.default_content()

    @allure.step('Send keys')
    def send_keys_slow(self, locator, text, delay):
        """
        Замедленный вод текста в текстовое поле
        :param locator: адрес поля
        :param text: вводимый текст
        :param delay: задержка в милл. сек. между вводимыми буквами
        :return:
        """
        waiting_time = (1 / 1000) * delay
        try:
            self.scroll_to_element(locator)
            for char in text:
                sleep(waiting_time)
                self.find_element(locator).send_keys(char)
        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)

    @allure.step('screenshot')
    def allure_screenshot(self):
        try:
            allure.attach(self.GetDriver().get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except Exception as e:
            print(str(e))

    @allure.step("select_element_by_visible_text:")
    def select_element_by_visible_text(self, locator, text):
        select = Select(self.GetDriver().find_element(locator))
        select.select_by_visible_text(text)

    @allure.step("move_to_element")
    def move_to_element(self, locator):
        actions = ActionChains(self.GetDriver())
        element = self.find_element(locator)
        actions.move_to_element(element)
        actions.perform()

    # остановщик теста при ошибке
    @allure.step('ElementNotVisibleException')
    def allure_ElementNotVisibleException(self, exeption_text):
        self.allure_screenshot()
        assert True == False

    # остановщик теста при ошибке
    @allure.step('NoSuchElementException')
    def allure_NoSuchElementException(self, exeption_text):
        self.allure_screenshot()
        assert True == False

    # остановщик теста при ошибке
    @allure.step('StaleElementReferenceException')
    def allure_StaleElementReferenceException(self, exeption_text):
        assert True == False

    def get_count_elements(self, locator):
        result = len(self.GetDriver().find_elements_by_xpath(locator))
        return result

    @allure.step('get_console_log')
    def get_console_log(self):
        print(self.GetDriver().get_log('browser'))

    def find_element(self, locator, wait=None):
        if wait is None:
            wait = self.manager.settings.time_element_Wait
        try:
            web_element = WebDriverWait(self.GetDriver(), wait).until(EC.presence_of_element_located(locator))
            return web_element
        except:
            self.allure_screenshot()
            raise

    def find_elements(self, locator):
        try:
            return WebDriverWait(self.GetDriver(), self.manager.settings.time_element_Wait).until(EC.presence_of_all_elements_located(locator))
        except:
            self.allure_screenshot()
            raise

    @allure.step('Проверяем, есть ли элемент на странице')
    def check_is_there_element_on_the_page(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    @allure.step('Переключиться на последнюю страницу в браузере')
    def move_to_last_page_in_browser(self):
        pages = self.GetDriver().window_handles
        self.GetDriver().switch_to.window(pages[-1])
        return self

    def waiting_for_item_not_display(self, locator):
        try:
            WebDriverWait(self.GetDriver(), self.manager.settings.time_element_Wait).until_not(EC.visibility_of_element_located(locator))
        except:
            self.allure_screenshot()