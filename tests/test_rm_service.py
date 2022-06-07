from src.rm_service import RemovalService, UploadService

import unittest
from unittest import mock


class RemovalServiceTestCase(unittest.TestCase):
    @mock.patch('src.rm_service.os.path')
    @mock.patch('src.rm_service.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        rm_service = RemovalService()

        # set up the mock
        mock_path.isfile.return_value = False
        rm_service.rm("any path")

        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

        # make the file 'exist'
        mock_path.isfile.return_value = True
        rm_service.rm("any path")
        mock_os.remove.assert_called_with("any path")


class UploadServiceTestCase(unittest.TestCase):
    @mock.patch.object(RemovalService, 'rm')
    def test_upload_complete(self, mock_rm):
        # build our dependencies
        removal_service = RemovalService()
        up_service = UploadService(removal_service)

        # call upload_complete, which should, in turn, call `rm`:
        up_service.upload_complete("my uploaded file")

        # check that it called the rm method of any RemovalService
        mock_rm.assert_called_with("my uploaded file")

        # check that it called the rm method of _our_ removal_service
        removal_service.rm.assert_called_with("my uploaded file")
