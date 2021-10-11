"""Contains 7 passed tests"""

import pytest
from seleniumbase import BaseCase
import config
from basic_methods import BasicMethods as bm
from dotenv import load_dotenv
from os import getenv


class SendResnponse(BaseCase):

    # loading envariomental variables for valid gmail credentials
    load_dotenv()
    valid_email = getenv('VALID_EMAIL', 'your valid email')
    valid_password = getenv('VALID_PASSWORD', 'your valid password')

    def test_NoCredentialsGiven_NoRedirection(self):
        """Checks if no credentials are given then no redirection to page of send result"""

        bm.upload_file(self, config.send_filepath)
        bm.fill_credentials(self)
        self.click(config.send_mails_button)
        self.assert_element_visible(config.send_mails_button)

    def test_OnlyNoPasswordsGiven_NoRedirection(self):
        """Checks if no password is given but email is given
        then no redirection to page of send result"""

        bm.upload_file(self, config.send_filepath)
        bm.fill_credentials(self, self.valid_email, "",
                            config.subject_test, config.signature_test)
        self.click(config.send_mails_button)
        self.assert_element_visible(config.send_mails_button)

    def test_OnlyNoEmailGiven_NoRedirection(self):
        """Checks if no email is given but password is given
        then no redirection to page of send result"""

        bm.upload_file(self, config.send_filepath)
        bm.fill_credentials(self, "", self.valid_password,
                            config.subject_test, config.signature_test)
        self.click(config.send_mails_button)
        self.assert_element_visible(config.send_mails_button)

    def test_InvalideLoginEmail_FailPageRedirection(self):
        """Checks if when invalide gmail (login) is given then redirect to fail page"""

        bm.upload_file(self, config.send_filepath)
        bm.fill_credentials(self, config.invalid_email, self.valid_password,
                            config.subject_test, config.signature_test)
        self.click(config.send_mails_button)
        self.assert_element_present(config.fail_title)

    def test_InvalideGmailPassword_FailPageRedirection(self):
        """Checks if when invalide gmail password is given then redirect to fail page"""

        bm.upload_file(self, config.send_filepath)
        bm.fill_credentials(self, self.valid_email, config.invalid_password,
                            config.subject_test, config.signature_test)
        self.click(config.send_mails_button)
        self.assert_element_present(config.fail_title)

    def test_ValidCredentialsValidDataSet_SuccessPageRedirection(self):
        """Checks if when valide gmail credentials is given and data set has valid email addresses
        then redirect to success page"""

        bm.upload_file(self, config.send_filepath)
        bm.fill_credentials(self, self.valid_email, self.valid_password,
                            config.subject_test, config.signature_test)
        self.click(config.send_mails_button)
        self.assert_element_present(config.success_title)

    def test_ValidCredentialsInvalidDataSet_FailPageRedirection(self):
        """Checks if when valide gmail credentials is given and data set has invalid email addresses
        then redirect to fail page"""

        bm.upload_file(self, config.send_fail_filepath)
        bm.fill_credentials(self, self.valid_email, self.valid_password,
                            config.subject_test, config.signature_test)
        self.click(config.send_mails_button)
        self.assert_element_present(config.fail_title)
