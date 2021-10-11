from seleniumbase import BaseCase
import config


class BasicMethods(BaseCase):
    def upload_file(self, filepath):
        """Opens url and uploads choosen file then redirect to credentials (send) page

        Parameters:
        filepath: filepath of your test file"""

        self.open_url(config.url)
        self.choose_file(config.file_upload, filepath)
        self.click(config.submit_file)

    def fill_credentials(self, email="", password="", subject="", signature=""):
        """Fills credentials to send emails 

        Parameters:
        email: gmail address from which mails will be sent
        password: password to given gmail account
        subject: subject of email
        signature: signature at the end of every email"""

        self.type(config.email_input, email)
        self.type(config.password_input, password)
        self.type(config.subject_input, subject)
        self.type(config.signature_input, signature)
