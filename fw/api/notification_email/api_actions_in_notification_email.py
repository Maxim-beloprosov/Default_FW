import time

import allure

from fw.api.notification_email.api_notification_email import ApiNotificationEmail


class ActionsInNotificationEmail(ApiNotificationEmail):

    @allure.title('Получение списка почтовых уведомлений')
    def notification_email_logs(self, user_email, sending_status='Sent'):

        mails_body = {
            'sendingStatus': sending_status,
            'intendedAddress': user_email,
            'take': 10,
            'skip': 0,
        }

        sent_mails = self.post_notification_email_logs_mails(mails_body, params={'order': 'Desc'})

        return sent_mails

    def mail_in_mail_list(self, mail_list, number):
        for mail in mail_list['items']:
            if number in mail['subject']:
                return True
            return False

    @allure.title('Метод проверки, пришло ли письмо')
    def check_email_logs(self, user_mail, ticket_doc_number, count=3, is_active=True):
        if is_active:
            for i in range(count):
                sent_mails = self.notification_email_logs(user_mail)
                if self.mail_in_mail_list(sent_mails, ticket_doc_number):
                    return True
                time.sleep(5)
            return False
        else:
            for i in range(count):
                sent_mails = self.notification_email_logs(user_mail)
                if self.mail_in_mail_list(sent_mails, ticket_doc_number):
                    return False
                time.sleep(5)
            return True
