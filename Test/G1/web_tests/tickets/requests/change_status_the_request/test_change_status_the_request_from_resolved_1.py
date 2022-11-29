import allure
import pytest

from Test.G1.web_tests.g1_web_base import G1WebBase


@allure.epic('G1')
@allure.feature('Web - Request')
@allure.story('Изменение статуса заявки из статуса "В проверке"')
class TestChangeStatusTheRequestFromRejected(G1WebBase):

    pass