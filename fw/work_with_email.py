import smtplib
import email
from email.mime.text import MIMEText


class WorkWithEmail:
    sender = 'email'
    pas = 'password'

    def send_mail(self):
        # server = smtplib.SMTP('smtp.mail.ru', 587)
        server = smtplib.SMTP('smtp.mail.ru')
        server.starttls()

        try:
            server.login(self.sender, self.pas)

            msg = MIMEText('Ну ваще чёрная магия !!')
            msg['Subject'] = 'Рус текст!'

            server.sendmail(self.sender, self.sender, msg.as_string())
        except Exception as e:
            print(e)

    def list_mail_POP3(self):
        import poplib
        pop3server = poplib.POP3_SSL('pop.mail.ru')

        pop3server.user(self.sender)
        pop3server.pass_(self.pas)

        pop3info = pop3server.stat()  # access mailbox status
        mailcount = pop3info[0]  # toral email
        print("Total no. of Email : ", mailcount)
        print("\n\nStart Reading Messages\n\n")
        for i in range(mailcount):
            for message in pop3server.retr(i + 1):
                print(message)
        pop3server.quit()

    def list_mail_imap(self):
        import imaplib
        mail = imaplib.IMAP4_SSL('imap.mail.ru')
        mail.login(self.sender, self.pas)
        mail.list()
        mail.select()
        result, data = mail.uid('search', None, "ALL")  # Выполняет поиск и возвращает UID писем.
        mail_list = []

        for email_uid in data[0].split():
            message_aggregated = {}
            result, data = mail.uid('fetch', email_uid, '(RFC822)')
            raw_email = email.message_from_bytes(data[0][1])

            message_aggregated['From'] = raw_email.get_all('From')
            message_aggregated['To'] = raw_email.get_all('Delivered-To')
            message_aggregated['Subject'] = raw_email.get_all('Subject')
            # message_aggregated['raw_email'] = raw_email

            try:
                message_aggregated['message_body'] = raw_email.get_payload(decode=True).decode('UTF-8')
            except:
                message_aggregated['message_body'] = raw_email.get_payload(decode=True)
            finally:
                message_aggregated['message_body'] = raw_email.get_payload()
            mail_list.append(message_aggregated)







