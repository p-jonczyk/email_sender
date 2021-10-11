"""Contains 3 passed tests"""

import pytest
from seleniumbase import BaseCase
import config


class TestUpload(BaseCase):

    def test_NoFileUploaded_NoRedirectionAfterSubmint(self):
        """Checks if when no file is uploaded then the page remain the same
        after 'SUBMIT' is clicked"""

        self.open(config.url)
        self.click(config.submit_file)
        self.assert_element_present('#send-title')

    def test_InvalideFileExtension_NoRedirectionAfterSubmint(self):
        """Checks if when unproper file is uploded then the page remain the same
        after 'SUBMIT' is clicked and message appears"""

        self.open(config.url)
        self.choose_file(config.file_upload, config.wrong_file_format_filepath)
        self.click(config.submit_file)
        self.assert_element_present('#file_response')

    def test_ProperFileUploaded_RedirectionToCredentials(self):
        """Checks if when proper file is uploded then user is redirected to credentials
        page after 'SUBMIT' is clicked"""

        self.open(config.url)
        self.choose_file(config.file_upload, config.send_filepath)
        self.click(config.submit_file)
        self.assert_element_present(config.send_mails_button)
