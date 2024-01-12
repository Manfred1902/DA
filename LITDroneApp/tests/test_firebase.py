import unittest
from unittest.mock import patch, MagicMock


class TestFirebase(unittest.TestCase):
    @patch('firebase.MDApp.get_running_app')
    @patch('firebase.login.pb.auth')
    @patch('firebase.pyrebase.auth')
    def test_login_success(self, mock_auth):
        pass

    @patch('firebase.login.pb.auth')
    def test_login_fail(self, mock_auth):
        pass
