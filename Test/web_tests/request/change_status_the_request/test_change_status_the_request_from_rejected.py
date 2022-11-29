import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Request')
@allure.story('Изменение статуса заявки из статуса "Отклонено"')
class TestChangeStatusTheRequestFromRejected(WebBase):

    @allure.title('Смена статуса с "Отклонено" на "На согласовании"')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    @allure.description('Белопросов Максим')
    def test_change_status_in_request_from_rejected_to_agreement(self):
        # Создаем заявку с согласующим
        approver = 'test_user05'
        request = self.create_request({"approvers": [approver], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Авторизуемся согласующим
        self.APP.api_token.get_token(approver)
        # Отклоняем согласование
        request = self.APP.api_actions_in_request.reject_request(request['syncToken'], request['id'])
        # Авторизуемся инициатором
        self.APP.web_any_page.check_autorizated_user_and_loging_other_user_if_need(self.users['test_user09'])
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(request['ticketType'], request['docNumber'])
        # Апеллируем заявку
        correct_status = self.APP.web_tickets_base.appeal_a_ticket()
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status