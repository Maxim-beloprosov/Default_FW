import allure
import pytest

from Test.web_tests.web_base import WebBase

@allure.epic('G2')
@allure.feature('Web - Task')
@allure.story('Изменение статуса задачи из статуса "Отклонена"')
class TestWebChangeStatusTheTaskFromRejected(WebBase):

    @allure.title('Смена статуса с "Отклонена" на "На согласовании" при апелляции')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.CRITICAL
    @pytest.mark.WebTest
    def test_change_status_in_task_from_rejected_to_agreement(self):
        # Создаем задачу
        task = self.create_task(
            {'approvers': ['test_user01'], "descriptionContent": ["TestDescription AutomationWebTests " + self.APP.time.get_date_time_Y_m_d_H_M_S()]})
        # Логинимся под согласующим
        self.APP.api_token.get_token('test_user01')
        # Отклоняем задачу
        task = self.APP.api_actions_in_task.reject_task(task['syncToken'], task['id'], text='AutomationWebTest Reject')
        # Переходим в нужный тикет
        self.APP.web_tickets_base.go_to_need_ticket(task['ticketType'], task['docNumber'])
        # Апеллируем
        self.APP.web_tickets_base.appeal_a_ticket()
        correct_status = 'На согласовании'
        # Ожидаем, пока будет корректный статус у заявки в апи, далее получаем актуальный статус заявки с WEB
        actual_status = self.APP.web_tickets_base.waiting_and_check_status_ticket(
            self.APP.group_data.Status_ticket['request_and_task']['ENG'][correct_status])
        # Сравниваем 2 статуса заявки
        assert correct_status == actual_status