from src.file_man import UnixFS
import os


def test_rm(mocker):
    mocker.patch('os.remove')
    UnixFS.rm('file')
    os.remove.assert_called_once_with('file')
