#!/usr/bin/python3
"""
Unittest for Users
"""
import models
from models import user
from models.base_model import BaseModel
from models.user import User
import unittest
import os
import pycodestyle


class TestUser(unittest.TestCase):
    """
    Starting Test
    """
    @classmethod
    def setUpClass(cls):
        '''Test'''
        print('------------Init Testing---------------\n')
        cls.my_user = User()
        cls.my_user.first_name = "Betty"
        cls.my_user.last_name = "Bar"
        cls.my_user.email = "airbnb@mail.com"
        cls.my_user.password = "root"

    def test_is_an_instance(self):
        """
        Instantiating Users
        """
        my_user = User()
        self.assertIsInstance(my_user, User)

    def test_type_instance(self):
        """
        type instance
        """
        self.assertIs(type(self.my_user.first_name), str)
        self.assertIs(type(self.my_user.last_name), str)
        self.assertIs(type(self.my_user.email), str)
        self.assertIs(type(self.my_user.password), str)

    def test_type_instance(self):
        """
        type instance
        """
    def test_attributes(self):
        self.assertTrue(hasattr(user, "__init__"))
        self.assertTrue(hasattr(user, "__str__"))
        self.assertTrue(user, "first_name")
        self.assertTrue(user, "last_name")
        self.assertTrue(user, "email")
        self.assertTrue(user, "password")

    def test_pycodestyle(self):
        """Test style PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "code style errors")

    @classmethod
    def tearDownClass(cls):
        '''Test'''


if __name__ == '__main__':
    unittest.main()
