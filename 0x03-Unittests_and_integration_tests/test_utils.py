#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for the access_nested_map function in the utils module.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function for different inputs.

        Parameters:
        - nested_map (dict): The nested map to access.
        - path (tuple): The path to navigate within the nested map.
        - expected_result: The expected result after accessing the nested map.

        Returns:
        None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    def test_access_nested_map_exception(self, nested_map, path, expected_exception_message):
        """
        Test that access_nested_map raises a KeyError for specific inputs.

        Parameters:
        - nested_map (dict): The nested map to access.
        - path (tuple): The path to navigate within the nested map.
        - expected_exception_message (str): The expected error message.

        Returns:
        None
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_exception_message)


    if __name__ == '__main__':
        unittest.main()
