import email
import imaplib
import os


class MailLoader:
    def __init__(self, username, password):
        username = username
        password = password

        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.mail.login(username, password)

    def get_last_email_with_params(self, sender=None, subject=None):
        self.mail.select('INBOX', readonly=True)

        if sender is not None and subject is not None:
            print(f'Searching for mail from: {sender}, with subject: "{subject}"')
            typ, messages = self.mail.search(None, 'FROM', sender, 'SUBJECT "{}"'.format(subject))
            return messages[0].split()[-1]

        elif sender is not None and subject is None:
            print(f'Searching for mail from: {sender}')
            typ, messages = self.mail.search(None, 'FROM', sender)
            return messages[0].split()[-1]

        elif sender is None and subject is not None:
            print(f'Searching for mail with subject: "{subject}"')
            typ, messages = self.mail.search(None, 'SUBJECT "{}"'.format(subject))
            return messages[0].split()[-1]

        else:
            print(f'Searching for last unseen mail')
            typ, messages = self.mail.search(None, 'UNSEEN')
            return messages[0].split()[-1]

    def get_mail_attachment(self, supplier, mail_id, file_name):
        file_path = ''
        typ, data = self.mail.fetch(mail_id, '(RFC822)')
        if typ != 'OK':
            print('Error fetching mail.')
            raise

        email_body = data[0][1]
        mail = email.message_from_bytes(email_body)
        for part in mail.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            attachment_name = part.get_filename()

            if bool(attachment_name):
                save_folder = os.path.join('../TemporaryStorage', supplier)

                if not os.path.exists(save_folder):
                    os.makedirs(save_folder)

                file_path = os.path.join(save_folder, file_name)

                fp = open(file_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()

        return file_path
