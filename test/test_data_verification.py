"""Contains 2 passed tests"""

import pytest
from seleniumbase import BaseCase
import config
from basic_methods import BasicMethods as bm


class TestDisplayFile(BaseCase):

    def test_NoErrorsFileUploaded_NoErrorsDisplayed(self):
        """Checks if when proper file with no errors: valid e-mails addresses and with message content
        is uploaded then no 'Possible errors' are shown and data are displayed in table"""

        bm.upload_file(self, config.send_filepath)
        # checks if data are displayed in table
        self.assert_element_present('#file-content')
        error_msg = self.get_text('#error_msg')
        # error_msg is empty -> pass test
        self.assert_equal(error_msg, "", "There are no possible errors")

    def test_FileUploadedWithErrors_ErrorsDisplayed(self):
        """Checks if when proper file with errors: invalide e-mails addresses and with no message content
        is uploaded then 'Possible errors' are shown and data are displayed in table"""

        bm.upload_file(self, config.send_fail_filepath)
        # checks if data are displayed in table
        self.assert_element_present('#file-content')
        error_msg = self.get_text('#error_msg')
        # error_msg is not empty -> pass test
        self.assert_not_equal(error_msg, "", "There are possible errors")
