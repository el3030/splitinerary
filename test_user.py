from user import User

import unittest


class TestUser(unittest.TestCase):
    def test_create_object_success(self):
        # arrange
        first_name = 'Tim'
        last_name = 'Paine'
        email = 'tkp2108@columbia.edu'
        # act
        user = User(first_name, last_name, email)
        # assert
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
        self.assertEqual(user.email, email)
